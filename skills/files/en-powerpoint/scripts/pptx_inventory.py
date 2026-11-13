"""List every text-bearing shape of a .pptx so the agent can address it by slide + shape id.

Usage:
  python3 pptx_inventory.py DECK.pptx                 # all slides
  python3 pptx_inventory.py DECK.pptx --slides 2-5,8  # some slides (big decks: stdout is limited)
  python3 pptx_inventory.py DECK.pptx --check         # only report leftover dummy text; exit 2 if any
  python3 pptx_inventory.py DECK.pptx --lists         # per layout + text slot: position, bullet/number/none per level

Output per slide: layout name, then one line per shape:
  id=<shape id> <kind> "<name>" followed by its paragraphs as  [0] text  [1] text ...
Kinds: ph:<type> = real placeholder (layout tools can fill it), box = plain shape/text box,
pic = picture, tbl = table (cells as r<row>c<col>), chart/smartart/ole = graphic frame.
Shapes inside groups are listed with their own id; the group id is shown as  in=<group id>.
<r> inside a paragraph marks a change of formatting (e.g. '01 <r>TITEL' = bold number, normal title):
keep the <r> in your new text to keep both formats.
Lines marked  !DUMMY  look like sample text (Text, XXX, TITEL, Lorem ...).
fit≈<chars>ch×<lines> lines = roughly how much text the box holds as designed (the decoration behind a
box is sized for its sample text); "(no wrap)" boxes stay on one line and grow sideways.
"""
import re
import sys

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

DUMMY = re.compile(
    r"^\s*("
    r"x{2,}|text(\s*\d+)?|titel|untertitel|title|subtitle|überschrift|headline|"
    r"abbildung|bild|image|picture|foto|photo|grafik|logo|firmenlogo|"
    r"platzhalter|placeholder|lorem ipsum.*|ipsum.*|"
    r"(klicken|click) .*(bearbeiten|edit|add|hinzuzufügen|einzugeben).*|"
    r"text(masterformat|platzhalter).*|\d{2}\s+titel"
    r")\s*$",
    re.IGNORECASE,
)
DUMMY_ANYWHERE = re.compile(r"x{3,}|lorem ipsum|\[\s*(text|name|datum|date|titel|title)\s*\]", re.IGNORECASE)


A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
EMU_PER_PT = 12700
NO_FIT = {"ph:footer", "ph:slide_number", "ph:date"}


def _char_em(ch, bold):
    """Rough glyph width in em: enough to tell 'fits' from 'clearly too long'."""
    if ch.isspace():
        w = 0.28
    elif ch.isupper() or ch.isdigit():
        w = 0.66
    elif ch in "il.,;:'|!":
        w = 0.28
    else:
        w = 0.52
    return w * (1.06 if bold else 1.0)


def para_font(p, txbody):
    """(size in pt, bold) of a paragraph: run, end-of-paragraph mark, the box's list style, else 18 pt."""
    size, bold = None, False
    for el in list(p._p.iter(A_NS + "rPr")) + list(p._p.iter(A_NS + "endParaRPr")):
        if size is None and el.get("sz"):
            size = int(el.get("sz")) / 100
        if el.get("b") == "1":
            bold = True
    if size is None:
        lvl = (p.level or 0) + 1
        for d in txbody.iter(A_NS + "lvl%dpPr" % lvl):
            r = d.find(A_NS + "defRPr")
            if r is not None and r.get("sz"):
                size = int(r.get("sz")) / 100
                break
    return size or 18.0, bold


def box_metrics(shape):
    """Usable width/height in pt, whether the box wraps, and its autofit mode."""
    body = shape.text_frame._txBody
    bp = body.find(A_NS + "bodyPr")
    ins = {k: int(bp.get(k, d)) / EMU_PER_PT for k, d in
           (("lIns", 91440), ("rIns", 91440), ("tIns", 45720), ("bIns", 45720))}
    fit = "fixed"
    if bp.find(A_NS + "spAutoFit") is not None:
        fit = "grow"
    elif bp.find(A_NS + "normAutofit") is not None:
        fit = "shrink"
    width = (shape.width or 0) / EMU_PER_PT - ins["lIns"] - ins["rIns"]
    height = (shape.height or 0) / EMU_PER_PT - ins["tIns"] - ins["bIns"]
    return {"w": max(width, 1), "h": max(height, 1), "wrap": bp.get("wrap") != "none", "fit": fit}


def text_layout(shape, m=None):
    """(lines needed, widest line in pt, average font size) for the shape's current text."""
    m = m or box_metrics(shape)
    body = shape.text_frame._txBody
    lines, widest, sizes = 0, 0.0, []
    for p in shape.text_frame.paragraphs:
        size, bold = para_font(p, body)
        sizes.append(size)
        for line in p.text.split("\v"):
            width = sum(_char_em(c, bold) for c in line) * size
            widest = max(widest, width)
            lines += max(1, -(-int(width) // int(m["w"]))) if m["wrap"] else 1
    return lines, widest, (sum(sizes) / len(sizes)) if sizes else 18.0


def container(shape, siblings, slide_area):
    """Smallest text-free shape (rounded box, colour tile, picture) the text box starts in."""
    if shape.left is None or shape.top is None:
        return None
    best = None
    for other in siblings:
        if other is shape or other.left is None or other.width is None:
            continue
        if getattr(other, "has_text_frame", False) and other.has_text_frame and other.text_frame.text.strip():
            continue
        area = other.width * other.height
        if area > 0.5 * slide_area or area <= 0:
            continue
        if other.left <= shape.left < other.left + other.width and other.top <= shape.top < other.top + other.height:
            if best is None or area < best.width * best.height:
                best = other
    return best


def capacity(shape, siblings=(), slide_area=0):
    """What the box holds as designed: max lines, max line width (pt), chars per line, wraps.

    The sample text and the decoration behind the box (if any) define the room; an auto-growing box
    is only as big as its sample text, so its own height says little.
    """
    m = box_metrics(shape)
    lines, widest, size = text_layout(shape, m)
    deco = container(shape, siblings, slide_area) if siblings else None
    margin = 8
    if m["fit"] in ("fixed", "shrink"):
        lines = max(lines, int(m["h"] // (size * 1.2)))
    elif deco is not None and m["wrap"]:
        room = (deco.top + deco.height - shape.top) / EMU_PER_PT - margin
        lines = max(lines, int(room // (size * 1.2)))
    if m["wrap"]:
        max_width = m["w"]
    else:
        max_width = max(widest, 1)
        if deco is not None:
            max_width = max(max_width, (deco.left + deco.width - shape.left) / EMU_PER_PT - 2 * margin)
    chars = max(1, int(max_width / (0.55 * size)))
    return {"lines": lines, "width": max_width, "chars": chars, "wrap": m["wrap"], "fit": m["fit"]}


def overflow(shape, cap):
    """Warning text if the shape's current text needs more room than cap allows, else None."""
    m = box_metrics(shape)
    lines, widest, _ = text_layout(shape, m)
    if not m["wrap"] and widest > cap["width"] * 1.1:
        return f"one line of ≈{int(widest)}pt in a box that does not wrap (room ≈{int(cap['width'])}pt, ≈{cap['chars']} chars)"
    if m["wrap"] and lines > cap["lines"]:
        return f"needs ≈{lines} lines, the design has room for ≈{cap['lines']} (≈{cap['chars']} chars per line)"
    return None


def fit_label(shape, siblings=(), slide_area=0):
    c = capacity(shape, siblings, slide_area)
    if not c["wrap"]:
        return f"fit≈{c['chars']}ch,1 line (no wrap)"
    return f"fit≈{c['chars']}ch×{c['lines']} lines"


RUN_MARK = "<r>"
_IGNORED_RPR_ATTRS = {"lang", "altLang", "dirty", "err", "noProof", "smtClean", "bmk"}


def rpr_key(r):
    """Formatting of a run, without attributes that do not change how it looks."""
    from lxml import etree

    rpr = r.find(A_NS + "rPr")
    if rpr is None:
        return ""
    clone = etree.fromstring(etree.tostring(rpr))
    for attr in _IGNORED_RPR_ATTRS:
        clone.attrib.pop(attr, None)
    return etree.tostring(clone)


def run_groups(p_el):
    """Runs of a paragraph grouped by formatting: [(rPr element or None, [run, ...]), ...]."""
    groups, last = [], None
    for child in p_el:
        if child.tag not in (A_NS + "r", A_NS + "fld"):
            continue
        key = rpr_key(child)
        if groups and key == last:
            groups[-1][1].append(child)
        else:
            groups.append((child.find(A_NS + "rPr"), [child]))
            last = key
    return groups


def marked_text(p):
    """Paragraph text with <r> where the formatting changes (e.g. bold number + normal title)."""
    out, last = [], None
    for child in p._p:
        if child.tag == A_NS + "br":
            out.append("\v")
        elif child.tag in (A_NS + "r", A_NS + "fld"):
            key = rpr_key(child)
            text = "".join(t.text or "" for t in child.iter(A_NS + "t"))
            if last is not None and key != last and text.strip() and "".join(out).strip():
                out.append(RUN_MARK)
            if text.strip():
                last = key
            out.append(text)
    return "".join(out)


def is_dummy(text):
    text = text.replace(RUN_MARK, "")
    return bool(text.strip()) and bool(DUMMY.match(text) or DUMMY_ANYWHERE.search(text))


def parse_ranges(spec, count):
    if not spec:
        return list(range(1, count + 1))
    out = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out.extend(range(int(a), int(b or a) + 1))
    return [n for n in out if 1 <= n <= count]


def kind_of(shape):
    if shape.is_placeholder:
        return "ph:" + str(shape.placeholder_format.type).split(".")[-1].split(" ")[0].lower()
    st = shape.shape_type
    if st == MSO_SHAPE_TYPE.PICTURE:
        return "pic"
    if getattr(shape, "has_table", False) and shape.has_table:
        return "tbl"
    if getattr(shape, "has_chart", False) and shape.has_chart:
        return "chart"
    if st == MSO_SHAPE_TYPE.GROUP:
        return "group"
    tag = shape._element.tag
    if tag.endswith("graphicFrame"):
        uri = shape._element.xpath(".//a:graphicData/@uri")
        return "smartart" if uri and "diagram" in uri[0] else "ole"
    return "box"


def walk(shapes, parent=None):
    for sh in shapes:
        yield sh, parent
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes, sh.shape_id)


def paragraphs_of(shape):
    """[(key, text)] for a shape: paragraph index for text, r<row>c<col>.<para> for tables."""
    out = []
    if getattr(shape, "has_text_frame", False) and shape.has_text_frame:
        for i, p in enumerate(shape.text_frame.paragraphs):
            out.append((str(i), marked_text(p)))
    elif getattr(shape, "has_table", False) and shape.has_table:
        for ri, row in enumerate(shape.table.rows):
            for ci, cell in enumerate(row.cells):
                text = "\n".join(p.text for p in cell.text_frame.paragraphs)
                out.append((f"r{ri}c{ci}", text))
    return out


def smartart_text(slide, shape):
    """SmartArt text lives in a separate diagram part; read it so the agent knows it is there."""
    ids = shape._element.xpath(".//*[local-name()='relIds']/@*[local-name()='dm']")
    if not ids:
        return []
    try:
        part = slide.part.related_part(ids[0])
    except KeyError:
        return []
    from lxml import etree

    root = etree.fromstring(part.blob)
    return [t.text for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t") if t.text]


def clip(text, n=90):
    text = text.replace("\v", "⏎").replace("\x0b", "⏎")
    return text if len(text) <= n else text[: n - 1] + "…"


P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
TEXT_PH = {"title", "ctrTitle", "subTitle", "body", "obj"}
MASTER_PH = {"ctrTitle": "title", "subTitle": "body", "obj": "body"}
MASTER_STYLE = {"title": "titleStyle", "ctrTitle": "titleStyle", "body": "bodyStyle",
                "subTitle": "bodyStyle", "obj": "bodyStyle"}


def ph_of(sp):
    ph = sp.find(f"{P_NS}nvSpPr/{P_NS}nvPr/{P_NS}ph")
    if ph is None:
        return None
    return ph.get("type", "body"), ph.get("idx")


def level_marker(lst_style, lvl):
    """Marker a list style defines for one level, or None when that level leaves it to the parent."""
    if lst_style is None:
        return None
    ppr = lst_style.find(f"{A_NS}lvl{lvl + 1}pPr")
    if ppr is None:
        return None
    if ppr.find(A_NS + "buNone") is not None:
        return "none"
    num = ppr.find(A_NS + "buAutoNum")
    if num is not None:
        return "number " + num.get("type", "")
    char = ppr.find(A_NS + "buChar")
    if char is not None:
        return f"bullet '{char.get('char', '')}'"
    if ppr.find(A_NS + "buBlip") is not None:
        return "bullet (picture)"
    return None


def lists_report(prs, levels=5):
    """Per layout and text placeholder: bullet / number / none for each level, resolved like PowerPoint
    does (layout placeholder → master placeholder → master text style). This is what a layout-tool slot
    value gets: companyFILES writes no bullet settings of its own."""
    print("Per slot: 'at x%,y%' = top-left corner on the slide (smaller x = further left), then the marker\n"
          "per level: L0 = top level (no 'level' / level 0), L1 = level 1, …  "
          "Layout ids and slot keys match describe_pptx_template.")
    for master in prs.slide_masters:
        m_el = master._element
        m_ph = {}
        for sp in m_el.iter(P_NS + "sp"):
            key = ph_of(sp)
            if key:
                m_ph.setdefault(key[0], sp.find(f"{P_NS}txBody/{A_NS}lstStyle"))
        tx = m_el.find(P_NS + "txStyles")
        for layout in master.slide_layouts:
            layout_id = str(layout.part.partname).rsplit("/", 1)[-1]
            rows = []
            for ph in layout.placeholders:
                sp = ph._element
                key = ph_of(sp)
                if not key or key[0] not in TEXT_PH:
                    continue
                typ, idx = key
                chain = [sp.find(f"{P_NS}txBody/{A_NS}lstStyle"),
                         m_ph.get(MASTER_PH.get(typ, typ)),
                         tx.find(P_NS + MASTER_STYLE[typ]) if tx is not None else None]
                marks = []
                for lvl in range(levels):
                    mark = next((m for m in (level_marker(s, lvl) for s in chain) if m), "none")
                    marks.append(f"L{lvl}={mark}")
                slot = f"{typ}:{idx}" if idx is not None else typ
                where = ""
                if ph.left is not None and ph.top is not None:
                    where = f"at {100 * ph.left // prs.slide_width:>2}%,{100 * ph.top // prs.slide_height:>2}%  "
                rows.append(f"  {slot:<12} {where}" + "  ".join(marks))
            if rows:
                print(f"\n== {layout_id} \"{layout.name}\"")
                print("\n".join(rows))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    path = args[0]
    if "--lists" in args:
        lists_report(Presentation(path))
        return
    check = "--check" in args
    spec = args[args.index("--slides") + 1] if "--slides" in args else None
    prs = Presentation(path)
    slides = list(prs.slides)
    numbers = parse_ranges(spec, len(slides))
    findings = []
    if not check:
        print(f"{path}: {len(slides)} slides, {len(prs.slide_layouts)} layouts, "
              f"size {prs.slide_width}x{prs.slide_height} EMU")
    for n in numbers:
        slide = slides[n - 1]
        if not check:
            print(f"\n== slide {n} | layout \"{slide.slide_layout.name}\"")
        for shape, parent in walk(slide.shapes):
            kind = kind_of(shape)
            paras = paragraphs_of(shape)
            if kind == "smartart":
                paras = [(f"s{i}", t) for i, t in enumerate(smartart_text(slide, shape))]
            dummy = [(k, t) for k, t in paras if is_dummy(t)]
            for k, t in dummy:
                findings.append(f"slide {n} id={shape.shape_id} [{k}] {clip(t, 60)!r}")
            if check or kind == "group":
                continue
            if not paras and kind not in ("pic", "chart", "smartart", "ole"):
                continue
            where = f" in={parent}" if parent else ""
            flag = "  !DUMMY" if dummy else ""
            line = f"  id={shape.shape_id} {kind} \"{clip(shape.name, 40)}\"{where}{flag}"
            if (kind == "box" or kind.startswith("ph:")) and kind not in NO_FIT and getattr(shape, "has_text_frame", False):
                if any(t.strip() for _, t in paras):
                    tops = list(slide.shapes) if parent is None else ()
                    line += f" {fit_label(shape, tops, prs.slide_width * prs.slide_height)}"
            if paras:
                line += "  " + "  ".join(f"[{k}] {clip(t)!r}" for k, t in paras)
            print(line)
        if not check and slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            if notes:
                print(f"  notes: {clip(notes, 120)!r}")
    if check:
        if findings:
            print(f"CHECK FAILED: {len(findings)} paragraph(s) still look like sample text:")
            for f in findings:
                print("  " + f)
            print("Fill them, delete the shape, or tell the user why they stay.")
            sys.exit(2)
        print(f"CHECK OK: no sample text found on {len(numbers)} slide(s).")


if __name__ == "__main__":
    main()
