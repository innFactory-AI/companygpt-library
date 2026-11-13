# Vorlage per Code-Ausführung bearbeiten

Rezept für Massen- oder freie Änderungen im Layout einer Vorlage, die die `create_*_from_template`-Tools nicht
können (z. B. einen Begriff in jedem Absatz, jeder Tabelle und Fußzeile ersetzen; 40 Tabellenzeilen im Stil der
Vorlage anfügen; ein Tabellenblatt neu aufbauen; Folien aus den Layouts des Masters anlegen). Nutze es nur, wenn
Code-Ausführung verfügbar ist. Ohne sie verwendest du die companyFILES-Vorlagen-Tools aus `SKILL.md`.

## 1. Datei in die Sandbox bringen

1. `list_templates` → exakter `name` und `type` (`docx`, `xlsx`, `potx`, `odt`).
2. `attach_template_to_chat { "name": "<name>", "type": "<type>" }`.
3. Sag dem Nutzer, dass die Vorlage angehängt ist und du mit seiner **nächsten Nachricht** weitermachst. Die Sandbox
   sieht die Datei erst ab dann, meist unter `/mnt/data/<name>.<ext>` (eine `potx` kommt als `<name>.pptx` an).
4. Prüfe im nächsten Zug zuerst:

```python
import os
print([f for f in os.listdir("/mnt/data") if not f.startswith(".")])
```

Fehlt die Datei: Ist Code-Ausführung für diesen Chat/Agenten an, und hat der Nutzer eine neue Nachricht geschickt?
Sonst weiche auf die Vorlagen-Tools aus.

## 2. Bibliotheken prüfen

```python
import importlib
for m in ("docx", "openpyxl", "pptx"):
    try:
        importlib.import_module(m); print(m, "ok")
    except ImportError:
        print(m, "FEHLT")
```

`docx` = python-docx, `openpyxl`, `pptx` = python-pptx. Fehlt die benötigte, weiche auf die Vorlagen-Tools aus. Für
ODT gibt es in der Standard-Sandbox keine Bibliothek (`import odf` schlägt meist fehl): nimm für ODT
`create_odt_from_template`. LibreOffice gibt es in der Sandbox auch nicht, sie kann also kein Dokument als PDF oder
Bild rendern.

Für eine Vorlage ohne `{{}}`, deren Inhalt als Blindtext in Textfeldern, Musterfolien, Inhaltssteuerelementen oder
Musterzeilen steht, nimm statt selbst geschriebenem Ersetzungscode die Skripte aus dem **de-powerpoint** (Weg D,
`pptx_inventory.py` / `pptx_fill.py`) und dem **de-word-odt** (`docx_inventory.py` / `docx_fill.py`).

## 3. Regeln

- Überschreibe nie die Eingabe. Speichere unter neuem Namen in `/mnt/data/`, z. B. `/mnt/data/angebot_acme.docx`;
  Dateien, die der Code dort schreibt, kommen als Chat-Anhänge zurück.
- Ändere Text innerhalb der vorhandenen Runs, damit Schriften, Farben und Formatvorlagen bleiben. `paragraph.text`
  zu ersetzen löscht die Run-Formatierung.
- Öffne das Ergebnis erneut und prüfe es (übrig gebliebene Platzhalter, Zeilenzahl), bevor du Erfolg meldest.
- Gib nur die Ergebnisdatei aus, nicht den Code, außer der Nutzer fragt danach.

## 4. Word (python-docx)

Text überall ersetzen (Fließtext, Tabellen, Kopf- und Fußzeilen), Formatierung bleibt. Ein über mehrere Runs
verteilter Platzhalter wird im ersten Run des Absatzes zusammengeführt:

```python
from docx import Document

SRC, OUT = "/mnt/data/<name>.docx", "/mnt/data/<ergebnis>.docx"
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
    for r in p.runs:                      # einfacher Fall: innerhalb eines Runs
        if old in r.text:
            r.text = r.text.replace(old, new)
            return
    full = p.text.replace(old, new)       # über Runs verteilt: Stil des ersten Runs behalten
    p.runs[0].text = full
    for r in p.runs[1:]:
        r.text = ""

doc = Document(SRC)
for p in paragraphs(doc):
    for old, new in values.items():
        replace(p, old, new)
doc.save(OUT)
```

Tabellenzeilen im Stil einer vorhandenen Zeile anfügen (XML der Zeile kopieren):

```python
import copy
table = doc.tables[0]
template_row = table.rows[1]              # formatierte Datenzeile
for item in items:                        # items = Liste von Listen
    new_tr = copy.deepcopy(template_row._tr)
    template_row._tr.addprevious(new_tr)  # oder table._tbl.append(new_tr)
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
table._tbl.remove(template_row._tr)      # Musterzeile entfernen, wenn sie nur als Vorlage diente
```

Prüfung: `[p.text for p in paragraphs(Document(OUT)) if "{" in p.text]` sollte leer sein (oder nur gewollte
Klammern enthalten).

## 5. Excel (openpyxl)

```python
from openpyxl import load_workbook
wb = load_workbook("/mnt/data/<name>.xlsx")      # Formeln behalten: kein data_only=True
ws = wb["Sheet1"]
for row in ws.iter_rows():
    for c in row:
        if isinstance(c.value, str) and "{{customer}}" in c.value:
            c.value = c.value.replace("{{customer}}", "Acme Corp")
start = 5                                         # erste Datenzeile der Vorlage
for i, rec in enumerate(records):
    for j, v in enumerate(rec, start=1):
        cell = ws.cell(row=start + i, column=j, value=v)
        cell._style = ws.cell(row=start, column=j)._style   # Stil der Vorlagenzeile übernehmen
wb.save("/mnt/data/<ergebnis>.xlsx")
```

- openpyxl behält Diagramme, Formen und manche Zeichnungen einer bestehenden Arbeitsmappe nicht. Hat die Vorlage
  Diagramme, nimm stattdessen `fill_excel_template` / `create_excel_from_template` (die behalten sie) oder weise
  den Nutzer vorher darauf hin.
- openpyxl berechnet Formeln nicht neu; Excel rechnet beim Öffnen. Schreibe Formeln als Text (`"=SUM(B5:B20)"`).
- Zeilen einfügen (`ws.insert_rows`) verschiebt keine Formeln, verbundenen Zellen oder Namen; schreibe besser in
  vorbereitete Zeilen oder hänge unten an.

## 6. PowerPoint (python-pptx)

```python
from pptx import Presentation
prs = Presentation("/mnt/data/<name>.pptx")       # eine potx-Vorlage kommt als .pptx an

def replace_in_shapes(shapes, old, new):
    for sh in shapes:
        if sh.shape_type == 6:                    # Gruppe
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
    replace_in_shapes(slide.shapes, "{{title}}", "Q4-Ergebnisse")
```

Neue Folien im Design des Masters: ein Layout verwenden und dessen Platzhalter füllen.

```python
for i, l in enumerate(prs.slide_layouts):
    print(i, l.name, [(ph.placeholder_format.idx, ph.name) for ph in l.placeholders])
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Nächste Schritte"
slide.placeholders[1].text_frame.text = "Verantwortlich: PMO"   # idx aus der Liste oben
prs.save("/mnt/data/<ergebnis>.pptx")
```

python-pptx hat keine Funktion „Folie duplizieren“. Baue neue Folien aus Layouts oder nutze für Klonen und
Neubefüllen die companyFILES-Tools (`append_slides_to_powerpoint` mit `reference_slide`, `add_slides_from_layouts`).
Um Musterfolien mit einfachen Textfeldern (samt Bildern und Diagrammen) zu kopieren, nimm `pptx_fill.py` aus dem
**de-powerpoint**.
