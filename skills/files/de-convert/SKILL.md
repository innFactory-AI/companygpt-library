---
name: de-convert
description: 'Konvertiere Dokumente zwischen Formaten mit companyFILES MCP-Tools. Verwende diesen Skill, wenn eine Datei konvertiert oder ihr Format geändert werden soll, Word als PDF exportiert, Excel in CSV oder JSON umgewandelt, Markdown in Word oder PDF überführt oder HTML in Word konvertiert werden soll. Deckt auch das Auflisten aller unterstützten Konvertierungspaare ab.'
---

# Konvertierungs-Skill

Tools zum Konvertieren von Dokumenten zwischen Formaten.

## Tools in diesem Skill

| Tool                        | Zweck                                                   |
| --------------------------- | ------------------------------------------------------- |
| `convert_document`          | Eine Datei zwischen unterstützten Formaten konvertieren |
| `get_supported_conversions` | Alle unterstützten Konvertierungspaare auflisten        |

## Unterstützte Konvertierungen

| Von      | Nach                           |
| -------- | ------------------------------ |
| Excel    | CSV, JSON, Markdown, HTML      |
| CSV      | Excel, JSON, Markdown, HTML    |
| JSON     | Excel, CSV, Markdown           |
| Word     | Text, Markdown, HTML, PDF      |
| Markdown | Word, PDF, HTML, Text, ODT     |
| HTML     | Word, PDF, Markdown, Text, ODT |
| PDF      | Text                           |

> Rufe im Zweifel `get_supported_conversions` auf, um die vollständige aktuelle Liste zu erhalten.

PDF lässt sich nur in reinen Text konvertieren. `excel` steht für `.xlsx`. Andere Formate – z. B. `.doc`, `.xls`, `.xlsb`, `.ppt`, OpenDocument, Outlook `.msg`/`.eml` oder ZIP – sind keine Eingaben für `convert_document`: Lies sie mit `read_file` oder speichere sie mit `convert_to_markdown` als ein Markdown-Dokument (beide im **de-file-management**, nur wo verfügbar).

## Tool-Verwendung

### convert_document

Die Eingabe kann base64-kodierter `file_content`, eine `librechat_file_id` oder eine `document_id` (gespeichertes companyFILES-Dokument) sein.

```json
{
  "file_content": "<base64-kodierte Datei>",
  "from_format": "word",
  "to_format": "pdf",
  "filename": "converted_document",
  "title": "Mein Dokument",
  "author": "Alice"
}
```

Mit einer LibreChat-Datei-ID:

```json
{
  "librechat_file_id": "<file_id aus list_my_files>",
  "from_format": "excel",
  "to_format": "csv",
  "filename": "data_export"
}
```

Werte für `from_format` (Quelle): `excel`, `word`, `pdf`, `csv`, `json`, `markdown`, `html` – beachte: `text` ist **keine** gültige Quelle.
Werte für `to_format` (Ziel): `excel`, `word`, `pdf`, `csv`, `json`, `markdown`, `html`, `text`, `odt`.

Liefert `{id, filename, downloadUrl, markdownLink}` – gib in der Antwort immer `markdownLink` aus.

---

### get_supported_conversions

```json
{}
```

Liefert `{ conversions: [{ from, to: [...] }] }` – einen Eintrag pro Quellformat mit seinen möglichen Zielformaten.

## Wichtige Hinweise

- `title` und `author` werden nur verwendet, wenn die Ausgabe `word`, `pdf` oder `odt` ist.
- Um eine Datei-ID für die Konvertierung zu erhalten, nimm die `file_id` eines Anhangs aus dem Block `Attached files in this message:` oder ermittle mit `list_my_files` (aus dem **de-file-management**) die Werte für `librechat_file_id` oder `document_id`.
- Um Dokumentinhalte ohne Konvertierung zu lesen, verwende `read_excel` / `read_word` / `read_pdf` aus den jeweiligen Skills.
