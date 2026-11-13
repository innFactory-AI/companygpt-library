# Editing a template with code execution

Recipe for bulk or free-form changes in a template's layout that the `create_*_from_template` tools cannot make
(e.g. replace a term in every paragraph, table and footer; add 40 table rows in the template's style; rebuild a
sheet; add slides from the master's layouts). Use it only when code execution is available. Without it, use the
companyFILES template tools from `SKILL.md`.

## 1. Get the file into the sandbox

1. `list_templates` → exact `name` and `type` (`docx`, `xlsx`, `potx`, `odt`).
2. `attach_template_to_chat { "name": "<name>", "type": "<type>" }`.
3. Tell the user the template is attached and that you continue with their **next message**. The sandbox only sees
   the file from then on, usually at `/mnt/data/<name>.<ext>` (a `potx` arrives as `<name>.pptx`).
4. In the next turn, check first:

```python
import os
print([f for f in os.listdir("/mnt/data") if not f.startswith(".")])
```

If the file is missing: is code execution on for this chat/agent, and did the user send a new message? Otherwise
fall back to the template tools.

## 2. Check the libraries

```python
import importlib
for m in ("docx", "openpyxl", "pptx"):
    try:
        importlib.import_module(m); print(m, "ok")
    except ImportError:
        print(m, "MISSING")
```

`docx` = python-docx, `openpyxl`, `pptx` = python-pptx. If the one you need is missing, fall back to the template
tools. There is no ODT library in the standard sandbox (`import odf` usually fails): use `create_odt_from_template`
for ODT. The sandbox has no LibreOffice either, so it cannot render a document to PDF or an image.

For a template without `{{}}` whose content sits as sample text in text boxes, example slides, content controls or
sample table rows, use the scripts of **en-powerpoint** (path D, `pptx_inventory.py` / `pptx_fill.py`) and
**en-word-odt** (`docx_inventory.py` / `docx_fill.py`) instead of hand-written replace code.

## 3. Rules

- Never overwrite the input. Save under a new name in `/mnt/data/`, e.g. `/mnt/data/offer_acme.docx`; files the
  code writes there come back as chat attachments.
- Change text inside existing runs so fonts, colours and styles stay. Replacing `paragraph.text` wipes run
  formatting.
- Re-open the result and check it (leftover placeholders, row counts) before you report success.
- Output only the result file, not the code, unless the user asks.

## 4. Word (python-docx)

Replace text everywhere (body, tables, headers, footers), keeping formatting. A placeholder split across several
runs is joined into the first run of the paragraph:

```python
from docx import Document

SRC, OUT = "/mnt/data/<name>.docx", "/mnt/data/<result>.docx"
values = {"{customer}": "Acme Corp", "{date}": "2025-05-08"}

def paragraphs(doc):
    def walk(container):
        for p in container.paragraphs:
            yield p
        for t in container.tables:
            for row in t.rows:
                for cell in row.cells:
                    yield from walk(cell)
    yield from walk(doc)
    for s in doc.sections:
        for part in (s.header, s.footer, s.first_page_header, s.first_page_footer):
            yield from walk(part)

def replace(p, old, new):
    if old not in p.text:
        return
    for r in p.runs:                      # simple case: inside one run
        if old in r.text:
            r.text = r.text.replace(old, new)
            return
    full = p.text.replace(old, new)       # split across runs: keep the first run's style
    p.runs[0].text = full
    for r in p.runs[1:]:
        r.text = ""

doc = Document(SRC)
for p in paragraphs(doc):
    for old, new in values.items():
        replace(p, old, new)
doc.save(OUT)
```

Add table rows in the style of an existing row (copy the row's XML):

```python
import copy
table = doc.tables[0]
template_row = table.rows[1]              # styled data row
for item in items:                        # items = list of lists
    new_tr = copy.deepcopy(template_row._tr)
    template_row._tr.addprevious(new_tr)  # or table._tbl.append(new_tr)
    row = table.rows[[r._tr for r in table.rows].index(new_tr)]
    for cell, value in zip(row.cells, item):
        for p in cell.paragraphs[1:]:
            p._p.getparent().remove(p._p)
        para = cell.paragraphs[0]
        if para.runs:
            para.runs[0].text = str(value)
            for r in para.runs[1:]:
                r.text = ""
        else:
            para.add_run(str(value))
table._tbl.remove(template_row._tr)      # drop the sample row if it only served as a pattern
```

Check: `[p.text for p in paragraphs(Document(OUT)) if "{" in p.text]` should be empty (or only intended braces).

## 5. Excel (openpyxl)

```python
from openpyxl import load_workbook
wb = load_workbook("/mnt/data/<name>.xlsx")      # keep formulas: no data_only=True
ws = wb["Sheet1"]
for row in ws.iter_rows():
    for c in row:
        if isinstance(c.value, str) and "{{customer}}" in c.value:
            c.value = c.value.replace("{{customer}}", "Acme Corp")
start = 5                                         # first data row of the template
for i, rec in enumerate(records):
    for j, v in enumerate(rec, start=1):
        cell = ws.cell(row=start + i, column=j, value=v)
        cell._style = ws.cell(row=start, column=j)._style   # copy the template row's style
wb.save("/mnt/data/<result>.xlsx")
```

- openpyxl does not keep charts, shapes and some drawings of an existing workbook. If the template has charts, use
  `fill_excel_template` / `create_excel_from_template` instead (they keep them), or warn the user before.
- Formulas are not recalculated by openpyxl; Excel recalculates on open. Write formulas as strings (`"=SUM(B5:B20)"`).
- Inserting rows (`ws.insert_rows`) does not shift formulas, merged cells or defined names; prefer writing into
  prepared rows or appending below.

## 6. PowerPoint (python-pptx)

```python
from pptx import Presentation
prs = Presentation("/mnt/data/<name>.pptx")       # a potx template arrives as .pptx

def replace_in_shapes(shapes, old, new):
    for sh in shapes:
        if sh.shape_type == 6:                    # group
            replace_in_shapes(sh.shapes, old, new)
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if old in r.text:
                        r.text = r.text.replace(old, new)
        if getattr(sh, "has_table", False) and sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells:
                    for p in cell.text_frame.paragraphs:
                        for r in p.runs:
                            if old in r.text:
                                r.text = r.text.replace(old, new)

for slide in prs.slides:
    replace_in_shapes(slide.shapes, "{{title}}", "Q4 Results")
```

New slides in the master's design: use a layout, then fill its placeholders.

```python
for i, l in enumerate(prs.slide_layouts):
    print(i, l.name, [(ph.placeholder_format.idx, ph.name) for ph in l.placeholders])
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Next Steps"
slide.placeholders[1].text_frame.text = "Owner: PMO"   # idx from the listing above
prs.save("/mnt/data/<result>.pptx")
```

python-pptx has no "duplicate slide" function. Build new slides from layouts, or use the companyFILES tools
(`append_slides_to_powerpoint` with `reference_slide`, `add_slides_from_layouts`) for clone-and-refill. To copy
example slides with plain text boxes (and their images and charts), use `pptx_fill.py` from **en-powerpoint**.
