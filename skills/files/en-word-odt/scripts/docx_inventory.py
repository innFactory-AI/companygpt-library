"""List the paragraphs, tables, text boxes and content controls of a .docx with stable keys.

Usage:
  python3 docx_inventory.py DOC.docx                # non-empty paragraphs of body, headers, footers
  python3 docx_inventory.py DOC.docx --all          # include empty paragraphs
  python3 docx_inventory.py DOC.docx --range B40-B120
  python3 docx_inventory.py DOC.docx --check        # only report leftover sample text; exit 2 if any

Keys (use them in docx_fill.py):
  B12   paragraph 12 of the body        H1.3 / F2.0  paragraph of header1.xml / footer2.xml
  BT0   table 0 of the body (rows/cells shown as r<row>c<col>)
Every paragraph is counted in document order, including those inside tables, text boxes and
content controls, so a key stays valid as long as the file is unchanged.
Lines marked !DUMMY look like sample text (XXX, Lorem, [Name], "Klicken oder tippen Sie hier" ...).
"""
import re
import sys

from docx import Document
from docx.oxml.ns import qn

MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
W14 = "http://schemas.microsoft.com/office/word/2010/wordml"
FALLBACK = "{%s}Fallback" % MC

DUMMY = re.compile(
    r"^\s*(x{2,}|text(\s*\d+)?|titel|untertitel|title|subtitle|überschrift|headline|"
    r"platzhalter|placeholder|lorem ipsum.*|tt\.mm\.jjjj|dd\.mm\.yyyy|musterfirma|max mustermann)\s*$",
    re.IGNORECASE,
)
DUMMY_ANYWHERE = re.compile(
    r"x{3,}|lorem ipsum|klicken oder tippen sie|click or tap here|klicken sie hier|click here to|"
    r"\[\s*[A-Za-zÄÖÜäöü][^\]\[]{0,39}\]|<<\s*\w+|«\s*\w+|\{\{\s*\w+",
    re.IGNORECASE,
)


def is_dummy(text):
    return bool(text.strip()) and bool(DUMMY.match(text) or DUMMY_ANYWHERE.search(text))


def parts(doc):
    """[(prefix, element)] for body, headers and footers in a stable order."""
    out = [("B", doc.element.body)]
    extra = []
    for part in doc.part.package.iter_parts():
        name = str(part.partname)
        m = re.match(r"/word/(header|footer)(\d+)\.xml$", name)
        if m and hasattr(part, "_element"):
            extra.append(("H" if m.group(1) == "header" else "F", int(m.group(2)), part._element))
    for kind, num, el in sorted(extra, key=lambda x: (x[0] != "H", x[1])):
        out.append((f"{kind}{num}.", el))
    return out


def in_fallback(el):
    return any(a.tag == FALLBACK for a in el.iterancestors())


def paragraphs(root):
    return [p for p in root.iter(qn("w:p")) if not in_fallback(p)]


def tables(root):
    return [t for t in root.iter(qn("w:tbl")) if not in_fallback(t)]


def _nearest(el, tag):
    return next(el.iterancestors(tag), None)


def rows_of(tbl):
    """Rows of this table, also when wrapped in a content control or customXml (not nested tables)."""
    return [r for r in tbl.iter(qn("w:tr")) if _nearest(r, qn("w:tbl")) is tbl]


def cells_of(tr):
    return [c for c in tr.iter(qn("w:tc")) if _nearest(c, qn("w:tr")) is tr]


def cell_paragraphs(tc):
    return [p for p in tc.iter(qn("w:p")) if _nearest(p, qn("w:tc")) is tc and not in_fallback(p)]


def own_text(p):
    """Text of this paragraph only (not of text boxes anchored in it)."""
    out = []
    for el in p.iter(qn("w:t"), qn("w:tab"), qn("w:br"), qn("w:cr"), qn("w:delText")):
        if next(el.iterancestors(qn("w:p")), None) is not p or el.tag == qn("w:delText"):
            continue
        if el.tag == qn("w:t"):
            out.append(el.text or "")
        else:
            out.append("\t" if el.tag == qn("w:tab") else "⏎")
    return "".join(out)


def context(p, table_index):
    bits = []
    for a in p.iterancestors():
        if a.tag == qn("w:tc"):
            tr, tbl = _nearest(a, qn("w:tr")), _nearest(a, qn("w:tbl"))
            if tr is not None and tbl is not None:
                bits.append(f"T{table_index.get(tbl, '?')}r{rows_of(tbl).index(tr)}c{cells_of(tr).index(a)}")
            break
    for a in p.iterancestors():
        if a.tag == qn("w:txbxContent"):
            bits.append("textbox")
            break
    for a in p.iterancestors():
        if a.tag == qn("w:sdt"):
            bits.append("cc:" + cc_name(a))
            break
    style = p.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    if style is not None:
        bits.append("style=" + style.get(qn("w:val")))
    return " ".join(bits)


def cc_name(sdt):
    pr = sdt.find(qn("w:sdtPr"))
    if pr is None:
        return "?"
    for tag in ("w:tag", "w:alias"):
        el = pr.find(qn(tag))
        if el is not None and el.get(qn("w:val")):
            return el.get(qn("w:val"))
    return "(unnamed)"


def content_controls(root):
    out = []
    for sdt in root.iter(qn("w:sdt")):
        if in_fallback(sdt):
            continue
        pr = sdt.find(qn("w:sdtPr"))
        kind = "text"
        if pr is not None:
            for child in pr:
                local = child.tag.split("}")[1]
                if local in ("date", "comboBox", "dropDownList", "picture", "checkbox", "richText", "docPartObj"):
                    kind = local
        content = sdt.find(qn("w:sdtContent"))
        text = "".join(t.text or "" for t in content.iter(qn("w:t"))) if content is not None else ""
        placeholder = pr is not None and pr.find(qn("w:showingPlcHdr")) is not None
        bound = pr is not None and pr.find(qn("w:dataBinding")) is not None
        out.append((cc_name(sdt), kind, text, placeholder, bound))
    return out


def clip(text, n=100):
    return text if len(text) <= n else text[: n - 1] + "…"


def in_range(key, spec):
    if not spec:
        return True
    m = re.match(r"([A-Z]\d*\.?)(\d+)-(?:[A-Z]\d*\.?)?(\d+)$", spec)
    k = re.match(r"([A-Z]\d*\.?)(\d+)$", key)
    return bool(m and k and k.group(1) == m.group(1) and int(m.group(2)) <= int(k.group(2)) <= int(m.group(3)))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    path, check, show_all = args[0], "--check" in args, "--all" in args
    spec = args[args.index("--range") + 1] if "--range" in args else None
    doc = Document(path)
    findings = []
    for prefix, root in parts(doc):
        tbls = tables(root)
        table_index = {t: i for i, t in enumerate(tbls)}
        paras = paragraphs(root)
        if not check:
            label = "body" if prefix == "B" else ("header " if prefix[0] == "H" else "footer ") + prefix[1:-1]
            print(f"\n== {label}: {len(paras)} paragraphs, {len(tbls)} tables")
            for i, t in enumerate(tbls):
                rows = rows_of(t)
                cols = max((len(cells_of(r)) for r in rows), default=0)
                print(f"  {prefix}T{i}: {len(rows)} rows x {cols} cols")
        for i, p in enumerate(paras):
            key = f"{prefix}{i}"
            text = own_text(p)
            dummy = is_dummy(text)
            if dummy:
                findings.append(f"{key} {clip(text, 60)!r}")
            if check or not in_range(key, spec) or (not text.strip() and not show_all):
                continue
            ctx = context(p, table_index)
            print(f"  {key}{' !DUMMY' if dummy else ''} {('[' + ctx + '] ') if ctx else ''}{clip(text)!r}")
        ccs = content_controls(root)
        for name, kind, text, placeholder, bound in ccs:
            if placeholder:
                findings.append(f"content control {name!r} still shows its placeholder")
        if ccs and not check:
            print("  content controls (fill by tag/alias):")
            for name, kind, text, placeholder, bound in ccs:
                flags = (" placeholder" if placeholder else "") + (" data-bound" if bound else "")
                print(f"    {name!r} {kind}{flags}: {clip(text, 60)!r}")
    if check:
        if findings:
            print(f"CHECK FAILED: {len(findings)} place(s) still look like sample text:")
            for f in findings:
                print("  " + f)
            print("Fill them, delete them, or tell the user why they stay (e.g. a signature line).")
            sys.exit(2)
        print("CHECK OK: no sample text found.")


if __name__ == "__main__":
    main()
