---
name: de-word-odt
description: 'Erstellt und liest Word- (.docx) und ODT-Dokumente (.odt) mit companyFILES MCP-Tools. Verwenden, wenn ein Bericht, Brief oder Dokument im Word- oder OpenDocument-Format geschrieben, Markdown oder HTML in Word/ODT umgewandelt, Text aus einer Word-Datei gelesen oder ein Dokument mit Kopf- und Fußzeilen, Inhaltsverzeichnis oder Seitenzahlen erstellt werden soll. Befüllt außerdem ein Firmendokument oder Formular ohne {{Platzhalter}} (Blindtext, Textfelder, Inhaltssteuerelemente, Tabellen) per Code-Ausführung.'
---

# Word & ODT Skill

Tools zum Erstellen von Word- (.docx) und ODT-Dokumenten (.odt) sowie zum Lesen von Word-Dateien.

## Tools in diesem Skill

| Tool                    | Zweck                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `create_word`           | Word (.docx) aus Markdown oder reinem Text erstellen                                        |
| `create_word_from_html` | Word aus HTML mit optionalem CSS erstellen                                                  |
| `create_word_from_json` | JSON-Daten als einfache Schlüssel/Wert-Auflistung in Word ausgeben                          |
| `create_odt`            | ODT aus Markdown erstellen (LibreOffice/OpenOffice)                                         |
| `create_odt_from_html`  | ODT aus HTML erstellen                                                                      |
| `read_word`             | Word-Datei (.docx) lesen → Text, HTML, Markdown (aus base64 oder LibreChat-Datei)           |
| `read_word_content`     | Inhalt eines gespeicherten Word-Dokuments per document_id lesen → Markdown-ähnlicher String |
| `append_to_word`        | Markdown-Inhalt an ein vorhandenes gespeichertes Word-Dokument direkt anfügen               |
| `replace_word_content`  | Gesamten Inhalt eines vorhandenen gespeicherten Word-Dokuments direkt ersetzen              |

## Entscheidungshilfe

```
Nutzer möchte ein Word-Dokument erstellen aus...
  Markdown / reinem Text    → create_word          (häufigster Fall)
  HTML + CSS                → create_word_from_html
  Rohen JSON-Daten (Dump)   → create_word_from_json  (keine Layoutsteuerung)
  Einer Vorlage             → siehe de-templates   (create_word_from_template)

Nutzer möchte OpenDocument-Format (LibreOffice)...
  Aus Markdown              → create_odt
  Aus HTML                  → create_odt_from_html
  Aus Vorlage               → siehe de-templates   (create_odt_from_template)

Nutzer möchte eine Word-Datei LESEN...
  Aus base64 / LibreChat-Anhang           → read_word
  Aus gespeichertem Dokument (document_id) → read_word_content

Nutzer möchte ein vorhandenes gespeichertes Word-Dokument BEARBEITEN...
  Zuerst aktuellen Inhalt prüfen          → read_word_content
  Weiteren Inhalt am Ende anfügen         → append_to_word    (behält vorhandenen Inhalt)
  Gesamtes Dokument neu schreiben         → replace_word_content

Nutzer möchte ein Firmendokument / Formular in seinem eigenen Layout BEFÜLLEN...
  Es hat {{Platzhalter}}                  → siehe de-templates (create_word_from_template)
  Kein {{}}: Blindtext, Textfelder,       → „Firmendokument ohne {{Platzhalter}} befüllen“
  Inhaltssteuerelemente, leere Tabellen      unten (Code-Ausführung)
```

## Verwendung der Tools

### create_word

```json
{
  "content": "# Annual Report\n\n## Summary\n\nThis year we achieved...",
  "filename": "annual_report",
  "title": "Annual Report 2025",
  "page_size": "A4",
  "page_orientation": "portrait",
  "header_text": "Confidential",
  "footer_text": "Acme Corp",
  "show_page_numbers": true,
  "page_number_position": "footer",
  "page_number_format": "{page} / {pages}",
  "include_toc": true
}
```

`format` kann `"markdown"` (Standard) oder `"plain"` sein. Hinweis: `create_word` hat **kein `author`-Feld** — nur `create_word_from_html`, `create_odt` und `create_odt_from_html` akzeptieren `author`.

### create_word_from_html

```json
{
  "html": "<h1>Report</h1><p>Content here.</p><table>...</table>",
  "css": "h1 { color: #336699; } body { font-family: Arial; }",
  "filename": "report",
  "title": "My Report",
  "show_page_numbers": true
}
```

Unterstützt Inline-Bilder über die URI `doc:<documentId>` (gespeichertes companyFILES-Dokument), `lc:<file_id>` (LibreChat-Anhang) oder `img:<name>` (Bildbibliothek, siehe `list_image_templates` im **de-templates**): `<img src="doc:abc123..." />`. Dieselbe Syntax funktioniert in Markdown für `create_word`: `![alt](doc:<uuid>)`, `![alt](lc:<file_id>)` oder `![alt](img:<name>)`. Ein unbekannter `img:`-Name bricht den Aufruf mit einem Fehler ab, der ihn nennt.

### create_word_from_json

```json
{
  "json_content": "{\"customer\":\"Acme Corp\",\"items\":[{\"name\":\"Widget\",\"qty\":2}]}",
  "filename": "order_data"
}
```

Schreibt das JSON als einfache Auflistung unter der Überschrift "Document Generated from JSON": ein Absatz pro Feld (`key: value`, Schlüssel fett); verschachtelte Objekte und Arrays werden eingerückt, Array-Einträge erscheinen als `[0]`, `[1]`, …. Es gibt kein Element-Schema (keine Überschriften, Tabellen oder Formatierung aus JSON) und keine Optionen für Titel, Autor oder Seite — nur `json_content` und `filename`. Für ein gestaltetes Dokument wandle die Daten in Markdown um und verwende `create_word`.

### create_odt

```json
{
  "content": "# Letter\n\nDear John,\n\nPlease find enclosed...",
  "filename": "letter",
  "title": "Formal Letter",
  "author": "Jane",
  "page_size": "A4",
  "header_text": "Private & Confidential",
  "show_page_numbers": true
}
```

### create_odt_from_html

```json
{
  "html": "<h1>Document</h1><p>Content</p>",
  "filename": "document",
  "page_size": "A4"
}
```

### read_word

```json
{
  "file_content": "<base64-encoded docx>"
}
```

Akzeptiert genau eines von `file_content` (base64), `librechat_file_id` (LibreChat-Anhang) oder `document_id` (gespeichertes companyFILES-Dokument). Liefert `{ text, html, markdown }`.

### read_word_content

Liest den Inhalt eines gespeicherten Word-Dokuments (über companyFILES erstellt oder hochgeladen). Akzeptiert `document_id` **oder** `librechat_file_id`. Liefert einen Markdown-ähnlichen String plus Zeichenanzahl — nutze das vor dem Anfügen oder Ersetzen, um den aktuellen Stand zu kennen.

```json
{
  "document_id": "uuid-of-stored-word-doc"
}
```

Liefert `{ document_id, librechat_file_id, filename, character_count, content }`.

### append_to_word

Fügt Markdown (oder reinen Text) an ein vorhandenes Word-Dokument an. Bestimme das Ziel mit `document_id` **oder** `librechat_file_id`. Standardmäßig wird vor dem neuen Inhalt ein Seitenumbruch eingefügt. Das Dokument wird direkt aktualisiert — gleiche `document_id`.

```json
{
  "document_id": "uuid-of-stored-word-doc",
  "content": "## New Section\n\nAdditional content here...",
  "format": "markdown",
  "add_page_break": true
}
```

`add_page_break` ist standardmäßig `true`. Verwende `false`, um auf derselben Seite weiterzuschreiben.

### replace_word_content

Ersetzt den gesamten Inhalt eines vorhandenen Word-Dokuments durch neues Markdown. Bestimme das Ziel mit `document_id` **oder** `librechat_file_id`. Alle Seitenlayout-Optionen (`page_size`, `header_text` usw.) funktionieren wie bei `create_word`. Das Dokument wird direkt aktualisiert — gleiche `document_id`.

```json
{
  "document_id": "uuid-of-stored-word-doc",
  "content": "# Updated Report\n\nFully rewritten content...",
  "format": "markdown",
  "page_size": "A4",
  "header_text": "Confidential",
  "show_page_numbers": true
}
```

## Gemeinsame Seitenoptionen (alle Erstellungstools außer `create_word_from_json`)

| Parameter               | Werte                               | Standard           |
| ----------------------- | ----------------------------------- | ------------------ |
| `page_size`             | `A4`, `Letter`, `Legal`, `A3`, `A5` | `A4`               |
| `page_orientation`      | `portrait`, `landscape`             | `portrait`         |
| `page_number_position`  | `header`, `footer`                  | `footer`           |
| `page_number_alignment` | `left`, `center`, `right`           | `center`           |
| `page_number_format`    | String mit `{page}` und `{pages}`   | `{page} / {pages}` |

## Muster für die iterative Dokumentbearbeitung

Lange Dokumente, die ein einzelnes Kontextfenster übersteigen, baust du abschnittsweise auf:

1. `create_word` — Dokument mit dem ersten Abschnitt erstellen; die zurückgegebene `id` notieren (als `document_id` übergeben)
2. `append_to_word` — für jeden weiteren Abschnitt erneut aufrufen
3. Optional `read_word_content`, um vor dem Weitermachen den aktuellen Stand zu prüfen
4. `replace_word_content` — falls ein Abschnitt komplett neu geschrieben werden muss

Alle drei direkt arbeitenden Tools (`read_word_content`, `append_to_word`, `replace_word_content`) arbeiten mit vorhandenen Dokumenten, die per `document_id` **oder** `librechat_file_id` (ein LibreChat-Anhang, der direkt auf dem gemeinsamen Volume aktualisiert wird) identifiziert werden, nicht mit base64-Dateiinhalt.

## Firmendokument ohne `{{Platzhalter}}` befüllen

Ein Briefbogen, eine Angebotsvorlage, ein Formular oder eine Berichtsvorlage, die der Nutzer anhängt,
hat meist keine `{{Platzhalter}}`. Stattdessen gibt es Blindtext („[Kunde]“, „XXX“, „Lorem ipsum“,
„Max Mustermann“), Textfelder, Inhaltssteuerelemente („Klicken oder tippen Sie hier, um Text
einzugeben.“), Kontrollkästchen und Tabellen mit einer leeren Musterzeile. `replace_word_content` und
`append_to_word` können so ein Dokument nicht befüllen. Sie schreiben es im companyFILES-Layout neu
oder hängen am Ende an, und das gewünschte Layout geht verloren. Nutze sie dafür nicht.

### Wenn Code-Ausführung verfügbar ist

Das Dokument liegt in der Sandbox unter `/mnt/data/<dateiname>.docx`. Dieser Skill bringt zwei Skripte
mit, unter `/mnt/data/skills/de-word-odt/scripts/`, wenn er als Paket installiert wurde:

1. **Inventur**:

   ```bash
   python3 /mnt/data/skills/de-word-odt/scripts/docx_inventory.py "/mnt/data/<dokument>.docx"
   ```

   Sie listet jeden nicht leeren Absatz mit einem Key auf: `B12` (Hauptteil), `H1.0` / `F1.2`
   (Kopf-/Fußzeile), die Tabellenzelle (`[T0r1c2]`), `textbox`, Formatvorlage. Dazu Tabellen
   (`BT0: 3 rows x 3 cols`) und Inhaltssteuerelemente mit Tag/Titel, Typ und ob sie noch ihren
   Platzhalter zeigen. `!DUMMY` markiert Blindtext. Lange Dokumente: `--range B0-B150`; leere Absätze:
   `--all`.

2. **Befüllen**: Plan und Ausgabe in einem Aufruf:

   ```bash
   cat > /tmp/plan.json <<'EOF'
   {
     "paragraphs": {"B2": "vielen Dank für Ihre Anfrage.", "B3": ["Beratung", "Implementierung", "Schulung"],
                    "B18": "Erika Beispiel", "B20": null, "H1.0": "Acme GmbH | Angebot 2026-117"},
     "tables": {"BT0": {"start_row": 1, "rows": [["Beratung", "2", "2.400 €"], ["Schulung", "1", "900 €"]], "trim": true}},
     "content_controls": {"Kunde": "Acme GmbH", "Freigabe": true},
     "replace": {"[Kunde]": "Acme GmbH"}
   }
   EOF
   python3 /mnt/data/skills/de-word-odt/scripts/docx_fill.py "/mnt/data/<dokument>.docx" /tmp/plan.json "/mnt/data/<ergebnis>.docx"
   ```

   - `paragraphs`: Key → Text. Eine Liste oder `\n` fügt Absätze in derselben Formatierung hinzu
     (z. B. weitere Bullets), `<br>` ist ein Zeilenumbruch, `null` löscht den Absatz. Bilder und
     Textfelder, die im Absatz verankert sind, bleiben erhalten.
   - `tables`: befüllt Zeilen ab `start_row` (0 = Kopfzeile). Mehr Zeilen, als die Tabelle hat, kopieren
     ihre letzte Zeile samt Formatierung. `null` behält eine Zelle, und `trim` entfernt nicht genutzte
     Musterzeilen.
   - `content_controls`: per Tag oder Titel. `true`/`false` setzt ein Kontrollkästchen. Die
     Platzhalter-Formatierung („Klicken oder tippen…“) wird entfernt.
   - `replace`: Teilstring überall: Hauptteil, Tabellen, Textfelder, Kopf- und Fußzeilen.
   - Textfelder werden in beiden Kopien aktualisiert, die Word speichert (sonst zeigen ältere Viewer den
     alten Text). Die Formatierung kommt aus dem Absatz und seinem ersten Run.
   - Keys beziehen sich immer auf das **Quelldokument**. Das Skript löst alle auf, bevor es etwas ändert.
     Schreib den Plan im selben Aufruf nach `/tmp`, denn Dateien in `/mnt/data` werden zu Chat-Anhängen.

3. **Prüfen**: Das Befüll-Skript endet mit einer Prüfung (Exit-Code 2 und `CHECK FAILED`, wenn Blindtext
   oder ein Platzhalter eines Inhaltssteuerelements übrig ist). `docx_inventory.py "<ergebnis>" --check`
   prüft einzeln. Absichtlich leere Felder (eine Unterschriftszeile) sind in Ordnung; nenne sie in der
   Antwort.

4. **Antworten**: Das Ergebnis kommt als Chat-Anhang zurück. Nenne, was du befüllt hast und was der
   Nutzer noch selbst ausfüllen muss. Du kannst nur den Text prüfen, nicht das Seitenlayout. Bitte den
   Nutzer, Zeilen- und Seitenumbrüche zu prüfen.

**Ohne die Skripte** (nur `SKILL.md` wurde eingefügt): Nutze python-docx (zuerst `import docx`).

- Geh alle Absätze durch, auch Tabellenzellen, Textfelder (`w:txbxContent`), Kopf- und Fußzeilen.
- Ändere Text in den vorhandenen Runs; `paragraph.text` zu setzen löscht die Formatierung.
- Kopiere eine Tabellenzeile mit `copy.deepcopy(row._tr)`.
- Inhaltssteuerelemente sind `w:sdt`-Elemente. Entferne `w:showingPlcHdr`, nachdem du eines befüllt
  hast.
- Das Rezept zum Ersetzen auf Run-Ebene steht im **de-templates** (`references/code-template-editing.md`).

**Grenzen:**

- Die Sandbox hat kein LibreOffice, also gibt es weder ein Rendering noch einen PDF-Export des
  Ergebnisses. Für ein PDF nutzt du `convert_document` (de-convert) auf dem fertigen DOCX, falls
  verfügbar.
- Für ODT gibt es in der Sandbox keine Python-Bibliothek.
- Alte Formularfelder (`FORMTEXT`) und nachverfolgte Änderungen werden nicht behandelt; sag es, wenn das
  Dokument sie nutzt.

### Ohne Code-Ausführung

Kein Tool befüllt so ein Dokument in seinem eigenen Layout. Sag das dem Nutzer klar und biete an:

- Code-Ausführung einschalten (Chat-/Agent-Einstellung oder die Berechtigung `RUN_CODE` von einem
  Admin).
- Das Dokument einmal zu einer echten Vorlage machen: in Word den Blindtext durch `{{Platzhalter}}`
  ersetzen und es als Vorlage hochladen. Danach befüllt `create_word_from_template` es ohne Code
  (de-templates).
- Die Texte als Liste zum Einfügen, oder ein neues Dokument mit `create_word` im companyFILES-/CI-Design,
  klar als nicht ihre Vorlage gekennzeichnet.

## Wichtige Hinweise

- Alle Erstellungstools liefern `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id`, wenn das Dokument zusätzlich als Chat-Datei gespeichert wird) — gib `markdownLink` immer in der Antwort aus.
- Die direkt bearbeitenden Tools (`append_to_word`, `replace_word_content`) liefern bei einem companyFILES-Dokument dieselbe `id` und einen aktualisierten `markdownLink`. Bei einem direkt aktualisierten Chat-Anhang (`librechat_file_id`) liefern sie nur `{librechat_file_id, filename, message}` — es gibt keinen Download-Link; teile dem Nutzer mit, dass die angehängte Datei aktualisiert wurde. Lässt sich der Anhang nicht direkt aktualisieren, wird die geänderte Kopie als **neues** Dokument gespeichert und dessen neue `id`/`markdownLink` zurückgegeben — verwende ab dann diese id.
- Inline-Bilder lassen sich über `doc:<documentId>`, `lc:<file_id>` oder `img:<name>` (Bildbibliothek) im Markdown oder HTML der Erstellungstools (`create_word`, `create_word_from_html`, `create_odt`, `create_odt_from_html`) referenzieren — SVG wird für Word automatisch in PNG umgewandelt. `append_to_word` und `replace_word_content` lösen diese Referenzen nicht auf.
- Nicht gesetzte Seiten-/Kopf-/Fußzeilenoptionen greifen auf die Theme-Standards der Organisation bzw. des Benutzers zurück (z. B. `defaultPageSize`, `defaultHeaderText`, `defaultShowPageNumbers`), bevor die dokumentierten festen Standardwerte gelten.
- Für vorlagenbasierte Word-Erstellung (Platzhalter, Schleifen, Bildeinfügung) verwende den **de-templates**. Bildplatzhalter sind dort `{IMAGE name}` oder `{%name}` (in einem Zug getippt); `width`/`height` in cm bilden einen Rahmen, in den das Bild unverzerrt eingepasst wird (`fit`: `contain` Standard, `cover` beschneidet, `stretch` nur auf Wunsch).
- ODT-Dateien lassen sich nativ in LibreOffice und Google Docs öffnen.
- Die CI der Organisation bzw. des Benutzers wird automatisch angewendet, wenn sie konfiguriert ist: Farben, Schriften und Größen, Seitenformat, Kopf-/Fußzeile, Seitenzahlen und das Logo an der eingestellten Position (Kopf- oder Fußzeile, links/Mitte/rechts). Für ein Dokument, das du selbst per Code-Ausführung baust, liefert `get_corporate_ci` dieselben Werte.
