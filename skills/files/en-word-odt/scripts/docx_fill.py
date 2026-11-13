"""Fill a corporate .docx that has no {{placeholders}}: paragraphs, tables, text boxes, content controls.

Usage:
  python3 docx_fill.py SOURCE.docx PLAN.json OUTPUT.docx

PLAN.json (keys come from docx_inventory.py on SOURCE; all keys refer to the unchanged source):
{
  "paragraphs": {
    "B3": "Offer for Acme Corp",                 # replace the text, keep the paragraph's formatting
    "B7": ["First point", "Second point"],       # more paragraphs in the same style (copies of B7)
    "B9": "Line one<br>line two",                # <br> = line break inside the paragraph
    "B12": null,                                 # delete the paragraph
    "H1.0": "Acme Corp | Offer 2026-117"         # header/footer paragraphs work the same way
  },
  "tables": {
    "BT0": { "start_row": 1, "rows": [["Item", "2", "1,200 EUR"], ["Service", "1", null]], "trim": true }
  },                                             # rows beyond the table copy its last row; null keeps a cell
  "content_controls": { "Customer": "Acme Corp", "Approved": true },   # by tag or title; bool = checkbox
  "replace": { "Musterfirma GmbH": "Acme Corp" },  # substring everywhere (body, tables, boxes, headers)
  "delete_tables": ["BT2"]
}

- A paragraph keeps its paragraph style and the formatting of its first text run; images and text boxes
  anchored in it stay. Text boxes are updated in both copies Word stores (DrawingML and VML fallback).
- Never overwrite the source. Prints a report, then the leftover-sample-text check (exit 2 if found).
"""
import copy
import json
import os
import re
import subprocess
import sys

from docx import Document
from docx.oxml.ns import qn

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_inventory import (FALLBACK, MC, W14, cc_name, cell_paragraphs, cells_of, paragraphs,  # noqa: E402
                            parts, rows_of, tables)

CHOICE = "{%s}Choice" % MC
ALT = "{%s}AlternateContent" % MC
KEEP_RUN_CHILDREN = {qn("w:drawing"), qn("w:pict"), qn("w:object"), ALT}
TEXT_CONTAINERS = {qn("w:hyperlink"), qn("w:smartTag"), qn("w:ins"), qn("w:fldSimple"), qn("w:proofErr"),
                   qn("w:del"), qn("w:sdt")}


# ---------------------------------------------------------------- paragraph text

def _first_rpr(p):
    for r in p.iter(qn("w:r")):
        if next(r.iterancestors(qn("w:p")), None) is p and r.find(qn("w:t")) is not None:
            rpr = r.find(qn("w:rPr"))
            return copy.deepcopy(rpr) if rpr is not None else None
    mark = p.find(qn("w:pPr") + "/" + qn("w:rPr"))
    if mark is not None:
        rpr = copy.deepcopy(mark)
        for child in list(rpr):
            if child.tag in (qn("w:ins"), qn("w:del"), qn("w:moveFrom"), qn("w:moveTo")):
                rpr.remove(child)
        return rpr
    return None


def _strip_placeholder_style(rpr):
    if rpr is None:
        return None
    style = rpr.find(qn("w:rStyle"))
    if style is not None and style.get(qn("w:val"), "").lower() in ("placeholdertext", "platzhaltertext"):
        rpr.remove(style)
    return rpr


def set_paragraph(p, text):
    """Replace the text of p; keep pPr, bookmarks and runs that carry drawings/text boxes."""
    rpr = _strip_placeholder_style(_first_rpr(p))
    anchor = None
    for child in list(p):
        removable = child.tag in TEXT_CONTAINERS or (
            child.tag == qn("w:r") and not any(c.tag in KEEP_RUN_CHILDREN for c in child))
        if removable:
            if anchor is None:
                anchor = child.getprevious()
            p.remove(child)
    runs = []
    for i, part in enumerate(re.split(r"<br\s*/?>|\v", str(text))):
        r = p.makeelement(qn("w:r"), {})
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        if i:
            r.append(r.makeelement(qn("w:br"), {}))
        t = r.makeelement(qn("w:t"), {})
        t.text = part
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r.append(t)
        runs.append(r)
    if anchor is None:
        ppr = p.find(qn("w:pPr"))
        for r in reversed(runs):
            if ppr is not None:
                ppr.addnext(r)
            else:
                p.insert(0, r)
    else:
        for r in reversed(runs):
            anchor.addnext(r)


def fill_paragraph(p, value):
    """String with \\n or a list -> several paragraphs (copies of p). null in a list keeps that one."""
    wanted = value if isinstance(value, list) else str(value).split("\n")
    template = copy.deepcopy(p)
    last = p
    for i, text in enumerate(wanted):
        if i == 0:
            if text is not None:
                set_paragraph(p, text)
            continue
        clone = copy.deepcopy(template)
        for el in clone.iter():          # bookmarks must stay unique
            if el.tag in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
                el.getparent().remove(el)
        set_paragraph(clone, "" if text is None else text)
        last.addnext(clone)
        last = clone


def delete_paragraph(p):
    parent = p.getparent()
    if parent is None:                   # already gone with its container (e.g. a deleted text box)
        return
    if parent.tag == qn("w:tc") and len([c for c in parent if c.tag == qn("w:p")]) == 1:
        set_paragraph(p, "")             # a table cell needs one paragraph
        return
    parent.remove(p)


def own_runs_text(p):
    return "".join(t.text or "" for t in p.iter(qn("w:t")) if next(t.iterancestors(qn("w:p")), None) is p)


def replace_in_paragraph(p, old, new):
    full = own_runs_text(p)
    if old not in full:
        return 0
    for t in p.iter(qn("w:t")):
        if next(t.iterancestors(qn("w:p")), None) is p and t.text and old in t.text:
            t.text = t.text.replace(old, new)
            return 1
    set_paragraph(p, full.replace(old, new))   # split across runs: first run's formatting wins
    return 1


# ---------------------------------------------------------------- tables, content controls

def fill_table(tbl, spec):
    rows = rows_of(tbl)
    start = int(spec.get("start_row", 0))
    data = spec.get("rows", [])
    if not rows:
        raise ValueError("the table has no rows")
    if start > len(rows):
        raise ValueError(f"start_row {start} but the table has {len(rows)} rows")
    while len(rows) < start + len(data):
        clone = copy.deepcopy(rows[-1])
        rows[-1].addnext(clone)
        rows.append(clone)
    for ri, values in enumerate(data):
        cells = cells_of(rows[start + ri])
        for ci, value in enumerate(values):
            if value is None or ci >= len(cells):
                continue
            paras = cell_paragraphs(cells[ci])
            if not paras:
                continue
            for extra in paras[1:]:
                extra.getparent().remove(extra)
            fill_paragraph(paras[0], value)
    if spec.get("trim"):
        for r in rows[start + len(data):]:
            r.getparent().remove(r)


def fill_content_control(sdt, value, report):
    pr = sdt.find(qn("w:sdtPr"))
    content = sdt.find(qn("w:sdtContent"))
    if content is None:
        content = sdt.makeelement(qn("w:sdtContent"), {})
        sdt.append(content)
    name = cc_name(sdt)
    if pr is not None:
        for tag in ("w:showingPlcHdr", "w:dataBinding"):
            el = pr.find(qn(tag))
            if el is not None:
                pr.remove(el)
                if tag == "w:dataBinding":
                    report.append(f"  note: content control {name!r} was data-bound; binding removed so the value stays")
    box = pr.find("{%s}checkbox" % W14) if pr is not None else None
    if box is not None:
        checked = str(value).lower() in ("true", "1", "x", "yes", "ja")
        box.find("{%s}checked" % W14).set("{%s}val" % W14, "1" if checked else "0")
        for t in content.iter(qn("w:t")):
            t.text = "☒" if checked else "☐"
            break
        return
    paras = [p for p in content if p.tag == qn("w:p")]
    if not paras:                        # cell-level: content -> tc -> p
        paras = [p for tc in content if tc.tag == qn("w:tc") for p in tc if p.tag == qn("w:p")][:1]
    if paras:                            # block-level content control
        for extra in paras[1:]:
            content.remove(extra)
        fill_paragraph(paras[0], value)
        return
    runs = [r for r in content if r.tag == qn("w:r")]
    if not runs and sdt.getparent().tag != qn("w:p"):   # empty block-level control: give it a paragraph
        p = content.makeelement(qn("w:p"), {})
        content.append(p)
        fill_paragraph(p, value)
        return
    first = runs[0].find(qn("w:rPr")) if runs else None
    rpr = _strip_placeholder_style(copy.deepcopy(first) if first is not None else None)
    for r in runs:
        content.remove(r)
    for i, part in enumerate(re.split(r"<br\s*/?>|\v|\n", str(value))):
        r = content.makeelement(qn("w:r"), {})
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        if i:
            r.append(r.makeelement(qn("w:br"), {}))
        t = r.makeelement(qn("w:t"), {})
        t.text = part
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r.append(t)
        content.append(r)


def sync_text_box_fallbacks(roots):
    """Word keeps a VML copy of every text box; make it match the edited DrawingML copy."""
    for root in roots:
        for alt in root.iter(ALT):
            choice, fallback = alt.find(CHOICE), alt.find(FALLBACK)
            if choice is None or fallback is None:
                continue
            new = list(choice.iter(qn("w:txbxContent")))
            old = list(fallback.iter(qn("w:txbxContent")))
            for src, dst in zip(new, old):
                if "".join(src.itertext()) == "".join(dst.itertext()):
                    continue                 # untouched box: leave Word's copy alone
                for child in list(dst):
                    dst.remove(child)
                for child in src:
                    dst.append(copy.deepcopy(child))


# ---------------------------------------------------------------- main

def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    src_path, plan_path, out_path = sys.argv[1:]
    if os.path.abspath(src_path) == os.path.abspath(out_path):
        sys.exit("Refusing to overwrite the source; pick a new output name.")
    try:
        with open(plan_path, encoding="utf-8") as fh:
            plan = json.load(fh)
    except json.JSONDecodeError as exc:
        sys.exit(f"{plan_path} is not valid JSON: {exc}")
    doc = Document(src_path)
    roots = parts(doc)
    para_by_key, table_by_key = {}, {}
    for prefix, root in roots:
        for i, p in enumerate(paragraphs(root)):
            para_by_key[f"{prefix}{i}"] = p
        for i, t in enumerate(tables(root)):
            table_by_key[f"{prefix}T{i}"] = t

    def lookup(mapping, key, what):
        if key not in mapping:
            sys.exit(f"{what} {key!r} not found — run docx_inventory.py on the source again. Nothing was saved.")
        return mapping[key]

    # Resolve every key before changing anything, so inserted paragraphs cannot shift later keys.
    para_ops = [(lookup(para_by_key, k, "paragraph"), v) for k, v in plan.get("paragraphs", {}).items()]
    table_ops = [(lookup(table_by_key, k, "table"), v) for k, v in plan.get("tables", {}).items()]
    table_dels = [lookup(table_by_key, k, "table") for k in plan.get("delete_tables", [])]
    report = []
    for old, new in plan.get("replace", {}).items():
        hits = sum(replace_in_paragraph(p, old, new) for _, root in roots for p in paragraphs(root))
        report.append(f"  replace {old!r}: {hits} paragraph(s)" if hits else f"  warning: {old!r} not found")
    cc_wanted = plan.get("content_controls", {})
    filled = set()
    for _, root in roots:
        for sdt in [s for s in root.iter(qn("w:sdt"))]:
            pr = sdt.find(qn("w:sdtPr"))
            names = {el.get(qn("w:val")) for el in (pr.find(qn("w:tag")), pr.find(qn("w:alias")))
                     if el is not None} if pr is not None else set()
            for name in names & set(cc_wanted):
                try:
                    fill_content_control(sdt, cc_wanted[name], report)
                except ValueError as exc:
                    sys.exit(f"{exc}. Nothing was saved.")
                filled.add(name)
                break
    for name in set(cc_wanted) - filled:
        report.append(f"  warning: no content control with tag/title {name!r}")
    try:
        for tbl, spec in table_ops:
            fill_table(tbl, spec)
    except ValueError as exc:
        sys.exit(f"{exc}. Nothing was saved.")
    for p, value in para_ops:
        if value is None:
            delete_paragraph(p)
        else:
            fill_paragraph(p, value)
    for tbl in table_dels:
        tbl.getparent().remove(tbl)
    sync_text_box_fallbacks([root for _, root in roots])
    doc.save(out_path)
    print(f"saved {out_path}: {len(para_ops)} paragraph(s), {len(table_ops)} table(s), "
          f"{len(filled)} content control(s) filled")
    for line in report:
        print(line)
    check = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docx_inventory.py")
    sys.stdout.flush()
    sys.exit(subprocess.call([sys.executable, check, out_path, "--check"]))


if __name__ == "__main__":
    main()
