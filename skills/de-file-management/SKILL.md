---
name: de-file-management
description: 'Dateien mit companyFILES MCP-Tools hochladen, herunterladen, auflisten, suchen und verwalten. Verwenden, wenn eine Datei hochgeladen, ein Dokument gefunden, gespeicherte Dateien aufgelistet, ein Download-Link abgerufen, Dokumente nach Name oder Typ gesucht, ein ZIP-Archiv erstellt, eine Text-/Code-Datei gespeichert, E-Mails, Archive oder andere Formate als Markdown gelesen oder ein gespeichertes Bild angesehen werden sollen. Deckt auch das Ermitteln von LibreChat-Datei-IDs für andere Tools ab.'
---

# Dateiverwaltungs-Skill

Tools zum Hochladen, Auflisten, Suchen, Herunterladen, Archivieren, Lesen und Erstellen von Textdateien in companyFILES.

## Tools in diesem Skill

| Tool                           | Zweck                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `upload_file`                  | Beliebige Datei (base64) zur Speicherung hochladen – liefert eine Dokument-ID                               |
| `download_stored_file`         | Download-Informationen zu einer gespeicherten Datei oder einem Chat-Upload abrufen                          |
| `list_documents`               | Alle deine Dokumente auflisten, einschließlich Chat-Uploads (keine Parameter)                               |
| `search_documents`             | Dokumente und Chat-Uploads nach Dateiname, Typ oder Zeitraum durchsuchen                                    |
| `list_my_files`                | Alle zugänglichen Dateien auflisten (LibreChat + PVC-Speicher)                                              |
| `create_zip_from_stored_files` | Gespeicherte Dokumente und/oder Chat-Uploads in einem ZIP-Archiv bündeln                                    |
| `create_text_file`             | Beliebige Text-/Code-Datei erstellen und speichern (.sql, .csv, .json, .py usw.)                            |
| `read_file`                    | Nahezu jede Datei als Markdown lesen (E-Mails, ZIP, ältere Office-Formate, OCR) – **sofern verfügbar**      |
| `save_file_part`               | Einen E-Mail-Anhang oder ZIP-Eintrag als neues Dokument speichern – **sofern verfügbar**                    |
| `convert_to_markdown`          | Eine ganze Datei (z. B. eine E-Mail mit Anhängen) als ein `.md`-Dokument speichern – **sofern verfügbar**   |
| `view_image`                   | Ein gespeichertes oder im Chat angehängtes Bild ansehen                                                     |

## Angehängte Dateien

Hat der Benutzer Dateien angehängt, stehen sie im Nachrichtenkontext in einem Block `Attached files in this message:` mit einer Zeile pro Datei: `- file_id: …, filename: …, type: …, size: … bytes` (plus `stored only`, wenn der Inhalt nicht in deinem Kontext ist). Übergib diese `file_id` als `librechat_file_id` (oder als `document_id`, wo ein Tool eine LibreChat-`file_id` annimmt). Nutze `list_my_files` nur, wenn es keinen solchen Block gibt, z. B. für eine Datei aus einem früheren Chat. Rate nie eine ID. Welches Tool bzw. welche App zu welcher Dateiaufgabe passt (companyFILES, Code-Ausführung, companyRAG, Transkription, Übersetzung): siehe **de-file-routing**.

## Entscheidungshilfe

```
Benutzer will eine Datei hochladen                          → upload_file
Benutzer will einen Download-Link für eine gespeicherte Datei → download_stored_file
Benutzer will Dokumente durchsehen / auflisten              → list_documents  (oder open_companyfiles_ui aus dem de-settings-ui)
Benutzer will ein bestimmtes Dokument finden                → search_documents
Benutzer will alle Dateien inkl. Chat-Uploads sehen         → list_my_files
Benutzer will Dateien in einem ZIP bündeln                  → create_zip_from_stored_files
Benutzer will eine Code-/Textdatei erstellen                → create_text_file
Benutzer will eine E-Mail, ein ZIP oder ein anderes Format öffnen → read_file  (sofern verfügbar)
Benutzer will einen Anhang dieser E-Mail / dieses ZIPs als eigene Datei → save_file_part  (sofern verfügbar)
Benutzer will, dass du dir ein Bild ansiehst                → view_image
```

## Tool-Verwendung

### upload_file

Maximale Größe: standardmäßig 50 MB (das Limit kann je Umgebung abweichen). Der Inhalt muss base64-kodiert sein.

```json
{
  "content": "<base64-encoded file content>",
  "filename": "logo.png",
  "mime_type": "image/png"
}
```

Der Inhalt wird gegen die Dateiendung geprüft (Magic Bytes): Leere Dateien und Dateien, deren Inhalt nicht zur Endung passt (z. B. ein in `.docx` umbenanntes PDF), werden mit einem `validation`-Fehler abgelehnt. Akzeptiert werden Office-Dokumente, PDF, Bilder, ZIP und gängige Textformate; wo `read_file` verfügbar ist, auch Formate wie `.msg`, `.eml`, `.doc`, `.xls`, `.xlsb`, `.ppt`, RTF, OpenDocument und EPUB.

Liefert `{id, filename, downloadUrl, markdownLink, size, type, message}`. Verwende `id` als `document_id` in anderen Tools.

---

### download_stored_file

`document_id` akzeptiert eine companyFILES-Dokument-ID **oder** eine LibreChat-`file_id` (Chat-Upload, siehe `list_my_files`).

```json
{
  "document_id": "abc12345-...",
  "return_content": false
}
```

- companyFILES-Dokument → `{id, filename, downloadUrl, size, type, createdAt, expiresAt}`
- Chat-Upload (LibreChat-`file_id`) → `{id, filename, size, type, source: "librechat", note}` – **kein Download-Link**; die `note` verweist auf die Lese-Tools.

Setze `return_content: true`, um zusätzlich den base64-`content` zu erhalten (nur für Dateien < 1 MB).

> Um den **Inhalt** von Excel-/Word-/PDF-Dateien zu lesen, verwende `read_excel` / `read_word` / `read_pdf` (andere Formate: `read_file`) – nicht dieses Tool.

---

### list_documents

```json
{}
```

Keine Parameter. Liefert `{documents, total}` – deine companyFILES-Dokumente **plus** deine Chat-Uploads (LibreChat-Dateien). Jeder Eintrag hat `id`, `filename`, `type`, `createdAt`, `expiresAt`, `size`, `isUploaded` und, falls die Datei in LibreChat liegt, `libreChatFileId` (bei Chat-Uploads ist `id` die LibreChat-`file_id`). Öffnet zusätzlich eine eingebettete UI-Ansicht zum interaktiven Durchsuchen.

---

### search_documents

```json
{
  "search": "invoice",
  "type": "pdf",
  "created_after": "2025-01-01",
  "created_before": "2025-06-01"
}
```

Alle Parameter sind optional. `search` ist eine Teilstring-Suche im Dateinamen ohne Beachtung der Groß-/Kleinschreibung. Werte für `type`: `word`, `excel`, `powerpoint`, `pdf`, `text`, `image`, `archive`, `file`. Chat-Uploads werden ebenfalls durchsucht. Liefert `{documents, total}` in derselben Form wie `list_documents`.

---

### list_my_files

```json
{}
```

Liefert Dateien aus LibreChat (Chat-Uploads) und aus dem PVC (companyFILES-Speicher). Jeder Eintrag hat entweder `file_id` (LibreChat) oder `document_id` (PVC) oder beides. Verwende diese IDs in den Lese-Tools (`read_excel`, `read_word`, `read_pdf`, `read_file`), in `view_image` und in `convert_document`.

Hängt der Benutzer eine `.pptx` an und möchte ein Deck „in diesem Design“ oder das angehängte Deck
erweitert haben, nimm ihre `file_id` aus dem Block der angehängten Dateien (oder ermittle sie hier) und übergib sie direkt an
`describe_pptx_template` / `create_powerpoint_from_layouts` / `add_slides_from_layouts` – ein
Vorlagen-Upload ist nicht nötig. Nur `create_powerpoint_from_template` (für ein `{{}}`-Deck) nimmt
ausschließlich einen `template_name` entgegen; ein solches Deck muss daher zuerst als Vorlage hochgeladen werden. Siehe
**de-powerpoint** §2a.

---

### create_zip_from_stored_files

Maximale unkomprimierte Gesamtgröße: 50 MB. `document_ids` nimmt 1–50 IDs entgegen – companyFILES-Dokument-IDs und/oder LibreChat-`file_id`s.

```json
{
  "document_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "filename": "project_files",
  "compression_level": 6
}
```

ZIP-Archive sind **temporär** (werden standardmäßig nach 1 Tag automatisch gelöscht). Sie erscheinen nicht in `list_documents`. Lassen sich einige `document_ids` nicht auflösen, wird das ZIP trotzdem aus den übrigen erstellt; die nicht aufgelösten IDs werden im Feld `missingDocumentIds` zusammen mit einer `warning` zurückgegeben (statt eines Fehlers).

---

### create_text_file

Funktioniert mit praktisch **jeder** Text-/Code-Endung (`.sql`, `.csv`, `.json`, `.xml`, `.html`, `.css`, `.js`, `.ts`, `.tsx`, `.jsx`, `.py`, `.java`, `.kt`, `.swift`, `.scala`, `.go`, `.rs`, `.rb`, `.php`, `.c`, `.h`, `.cpp`, `.cs`, `.yaml`, `.yml`, `.toml`, `.md`, `.txt`, `.log`, `.sh`, `.bash`, `.zsh`, `.env`, `.ini`, `.cfg`, `.conf`, `.properties`, `.graphql`, `.proto`, …). Die Liste ist eine **Blocklist, keine Allowlist** – jede nicht gesperrte Textendung wird akzeptiert. Einige ausführbare Endungen sind aus Sicherheitsgründen gesperrt (z. B. `.ps1`, `.bat`, `.exe`) und werden abgelehnt, obwohl sie Text sind.

```json
{
  "content": "SELECT * FROM orders WHERE status = 'pending';",
  "filename": "pending_orders.sql"
}
```

```json
{
  "content": "#!/bin/bash\necho 'Hello World'",
  "filename": "hello.sh"
}
```

---

### read_file / save_file_part / convert_to_markdown (sofern verfügbar)

Diese drei Tools gibt es nur, wo das erweiterte Lesen von Dateien aktiviert ist – stehen sie nicht in deiner Tool-Liste, sind sie nicht verfügbar. `read_file` liest Formate, die die anderen Lese-Tools nicht abdecken: Outlook-`.msg`- und `.eml`-E-Mails (Header, Text, Anhänge), ZIP-Archive (Einträge), `.doc`, `.xls`, `.xlsb`, `.ppt`, `.rtf`, OpenDocument (`.odt`/`.ods`/`.odp`), EPUB, HTML, CSV/JSON/XML, Jupyter-Notebooks, Bilder und gescannte PDFs (OCR). Für `.docx`/`.xlsx`/`.pdf` bleiben die regulären Lese-Tools die erste Wahl.

```json
{
  "librechat_file_id": "<file_id of the attachment>",
  "part": "0",
  "offset": 0
}
```

Alle drei nehmen `document_id` oder `librechat_file_id` entgegen. `read_file` liefert das Markdown eines Teils seitenweise (fahre mit dem am Ende angegebenen `offset` fort; `max_chars` legt die Seitengröße fest), die Liste der Teile (E-Mail-Anhänge oder ZIP-Einträge mit IDs wie `"0.1"`), E-Mail-Header und Warnungen. Einen Anhang liest du, indem du seine `part`-ID übergibst. `save_file_part` (`part` erforderlich, z. B. `"0.2"`) speichert diesen Teil mit seinen Originalbytes als neues companyFILES-Dokument, sodass die regulären Tools damit arbeiten können; `convert_to_markdown` speichert die ganze Datei (oder einen `part` samt seinen Unterteilen) als ein `.md`-Dokument. Läuft eine lange Konvertierung (OCR, LibreOffice) noch, meldet das Tool dies – rufe es nach etwa 30 Sekunden erneut auf.

---

### view_image

Gibt dir ein gespeichertes Bild (PNG, JPEG, WebP, GIF) zurück, damit du es beschreiben oder analysieren kannst – z. B. ein hochgeladenes Foto oder ein exportiertes Diagramm.

```json
{
  "document_id": "abc12345-..."
}
```

Nimmt `document_id`, `librechat_file_id` oder `image_template` (ein Bild aus der Bildbibliothek, siehe `list_image_templates` im **de-templates**) entgegen.

## Wichtige Hinweise

- `upload_file` prüft Dateigröße (standardmäßig max. 50 MB), Endung und Inhalt (die Bytes müssen zur Endung passen).
- Eine `document_id` aus einem beliebigen Erstellungs-/Upload-Tool kann wiederverwendet werden: bei der ZIP-Erstellung, beim Einfügen von Bildern in Vorlagen (`document_id` in Bild-Platzhaltern) und in `doc:`-URI-Verweisen im Markdown/HTML der Erstellungs-Tools (`create_word*`, `create_odt*`, `create_pdf*`, `create_powerpoint`; nicht in Append-/Replace-/Update-Tools). Bilder aus der Bildbibliothek funktionieren genauso als `img:<name>`.
- Liegt bei LibreChat nur der Textauszug einer Chat-Datei vor (hochgeladen „als Text“), antworten Tools, die die Originaldatei benötigen: „Von dieser Datei liegt bei LibreChat nur ein Textauszug vor – bitte die Originaldatei erneut hochladen.“ Gib das weiter und bitte den Benutzer, die Originaldatei erneut anzuhängen.
- Dokumente werden nach einer Aufbewahrungsfrist automatisch gelöscht (standardmäßig 365 Tage; kann je Umgebung abweichen).
- Wo die CAD-Erweiterung verfügbar ist, haben CAD-/BIM-/3D-Dateien (DXF, STEP, IFC, STL, …) eigene Tools (`describe_model`, `query_model`, …; siehe **de-cad-bim**).
- Zum interaktiven Durchsuchen von Dateien verwende `open_companyfiles_ui` aus dem **de-settings-ui**.
