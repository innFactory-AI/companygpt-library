---
name: de-file-routing
description: Entscheidet, welches Tool oder welche App eine Dateiaufgabe in companyGPT übernimmt. Verwende diesen Skill immer, wenn der Nutzer eine Datei angehängt hat oder eine Datei als Ergebnis möchte, z. B. eine Datei lesen, auswerten, damit rechnen, als Diagramm darstellen, bearbeiten, konvertieren, übersetzen oder transkribieren, eine Vorlage ausfüllen oder ein Word-, Excel-, PowerPoint- oder PDF-Dokument erstellen. Wählt zwischen companyFILES, Code-Ausführung, companyRAG, companyTRANSCRIBE, companyTRANSLATE und companyM365 und nennt die Alternative, wenn eine App oder Fähigkeit fehlt.
---

# Datei-Routing-Skill

Du entscheidest, welches Tool eine Dateiaufgabe übernimmt. Du rätst keine Datei-IDs und versprichst keine Fähigkeiten, die du nicht in deiner Tool-Liste gesehen hast.

## Schritt 1: Datei finden

Dateien, die der Nutzer angehängt hat, stehen im Nachrichtenkontext in einem Block wie diesem:

```
Attached files in this message:
- file_id: 6f1c…, filename: umsatz_2025.xlsx, type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, size: 48211 bytes
- file_id: a93e…, filename: meeting.m4a, type: audio/mp4, size: 18734112 bytes, stored only
```

- Nimm die `file_id` von dort und gib sie unverändert weiter: an companyFILES-Tools als `librechat_file_id`, an companyTRANSCRIBE und companyTRANSLATE als `file_id`.
- `stored only` heißt: Der Inhalt ist nicht in deinem Kontext. Du kommst nur über ein Tool, das die `file_id` annimmt (oder über Code-Ausführung), an ihn heran.
- Kein Block, oder die Datei stammt aus einem früheren Chat: Rufe `list_my_files` (companyFILES) auf und wähle die Datei über ihren Namen. Erfinde nie eine `file_id`.

## Schritt 2: Prüfen, was verfügbar ist

Prüfe deine Tool-Liste, bevor du einen Weg wählst. Apps (companyFILES, companyRAG, companyTRANSCRIBE, companyTRANSLATE, companyM365) sind nur da, wenn sie für diesen Tenant und Agenten aktiviert sind. Code-Ausführung ist nur da, wenn sie für den Chat oder Agenten aktiviert und für die Rolle des Nutzers erlaubt ist. Fehlt ein Weg, nimm die Alternative aus der Tabelle oder sag dem Nutzer, was fehlt.

**Office-Add-in:** Stehen `word_*`-, `excel_*`-, `ppt_*`- oder `outlook_*`-Tools in deiner Tool-Liste, läuft der Chat im companyGPT-Bereich in Word, Excel, PowerPoint oder Outlook, und dort ist ein Dokument geöffnet. Meint der Nutzer *dieses* Dokument („diese Präsentation“, „die Tabelle hier“, „meine Antwort“), arbeite mit diesen Tools darin. Die companyFILES-`create_*`-Tools nimm nur, wenn der Nutzer eine neue, eigene Datei zum Herunterladen möchte.

## Schritt 3: Weg wählen

| Aufgabe | Weg | Alternative / Bedingung |
| --- | --- | --- |
| Natives Word-, Excel-, PowerPoint- oder PDF-Dokument erstellen | companyFILES-`create_*`-Tools (siehe Word-, Excel-, PowerPoint-, PDF-Skill) | Ohne companyFILES: Inhalt als Markdown im Chat liefern |
| Angehängte DOCX, XLSX, PDF oder PPTX lesen | companyFILES `read_word`, `read_excel`, `read_pdf`, `read_powerpoint_slides` mit `librechat_file_id` | Kurze Textdateien sind oft schon in deinem Kontext |
| Berechnungen, Filter, Pivots oder Statistik auf einer angehängten CSV/XLSX | Code-Ausführung (pandas auf `/mnt/data/<dateiname>`), siehe unten | Ohne Code-Ausführung: companyFILES `read_excel` (CSV: companyFILES `read_file`, falls verfügbar) und über die Werte schlussfolgern; bei großen Dateien sagen, dass das Ergebnis auf dem gelesenen Ausschnitt beruht |
| Diagramm aus angehängten Daten | **Im Chat:** companyFILES `show_interactive_chart`. **In einer PowerPoint:** natives, bearbeitbares Diagramm über companyFILES `slides[].chart` (`create_powerpoint`, `append_slides_to_powerpoint`, `update_powerpoint_slide`) oder `charts` (Layout-Tools), siehe PowerPoint-Skill. **In Word/PDF:** Bild über `create_chart_document` / `embed_chart_in_document` (nicht ODT: Diagramm zuerst als Bild rendern und einbetten, siehe de-word-odt). Alternativ Code-Ausführung (matplotlib/plotly) für ein Bild | Ohne Code-Ausführung: Werte mit `read_excel` lesen, dann die companyFILES-Diagramm-Tools |
| Firmenvorlage ausfüllen | companyFILES `list_templates` + `create_*_from_template` (Vorlagen-Skill) | — |
| Massen- oder freie Änderungen im Layout einer Vorlage | companyFILES `attach_template_to_chat`, dann Code-Ausführung ab der **nächsten** Nachricht des Nutzers (Vorlagen-Skill) | Braucht Code-Ausführung und LibreChat-Dateispeicher für companyFILES; sonst `create_*_from_template` plus die iterativen Bearbeitungstools |
| Ein angehängtes Firmen-Deck oder Word-Dokument mit Blindtext („Text“, „XXX“, „[Kunde]“), aber ohne `{{Platzhalter}}` befüllen | Code-Ausführung mit den Skripten aus dem PowerPoint-Skill (Weg D) oder dem Word-Skill | Ohne Code-Ausführung gibt es kein Tool dafür: sag das und biete die Optionen aus diesen Skills an; liefere nie leere Folien oder Folien mit Blindtext als fertig aus |
| Angehängte Excel-, Word- oder PowerPoint-Datei bearbeiten | companyFILES `modify_excel`, `append_to_word`/`replace_word_content`, PowerPoint-Bearbeitungstools mit `librechat_file_id` | Mit Code-Ausführung auch in der Sandbox möglich (als neue Datei speichern) |
| E-Mails (`.msg`, `.eml`), ZIP-Archive, Altformate (`.doc`, `.xls`, `.ppt`, RTF, ODF), gescannte PDFs | companyFILES `read_file` / `save_file_part` / `convert_to_markdown` | Nur, wenn sie in deiner Tool-Liste stehen; sonst um einen PDF- oder DOCX-Export bitten |
| Zwischen Formaten konvertieren | companyFILES `convert_document` (Konvertierungs-Skill) | — |
| Firmenwissen: Handbücher, Richtlinien, Verträge, Projektunterlagen, gepflegte Tabellen | companyRAG `search_content`; für Tabellen `execute_sql` | Nur für Collections, auf die der Nutzer Zugriff hat; `list_collections` listet sie mit exaktem Namen. `execute_sql` und die anderen Dataset-Tools gibt es nur, wo companyRAG-Datasets aktiviert sind |
| Audio- oder Videodatei (MP3, WAV, M4A, MP4, MOV, …) | companyTRANSCRIBE `transcribe_chat_file { "file_id": "…" }`, dann `get_transcript_stats` bis fertig, dann `get_transcript` | Nur, wenn companyTRANSCRIBE aktiviert ist; die Transkription dauert Minuten |
| Angehängtes Dokument übersetzen | companyTRANSLATE `translate_document { "file_id": "…", "target_language": "…" }` (Status `running`: `get_translation_status { "job_id": "…" }`) | Nur, wenn companyTRANSLATE aktiviert ist; sonst den ausgelesenen Text selbst übersetzen und mit companyFILES ein neues Dokument erstellen |
| Text übersetzen | companyTRANSLATE `translate_text { "text": "…", "target_language": "…" }` | Ohne companyTRANSLATE: selbst übersetzen |
| Im geöffneten Dokument des Office-Add-ins arbeiten (bearbeiten, formatieren, Folien ergänzen, in die offene Mail schreiben) | Die Add-in-Tools dieser App: `word_*`, `excel_*`, `ppt_*`, `outlook_*` | Nur im Add-in. Nicht für eine neue Datei zum Herunterladen: das ist companyFILES |
| Outlook-Mails und ihre Anhänge | companyM365 `search_emails` / `get_email`, dann `read_email_attachment { "messageId": "…", "attachmentId": "…" }` (siehe de-m365-mail) | Nur, wenn companyM365 aktiviert ist. Eine im Chat angehängte `.msg`-/`.eml`-Datei ist keine Outlook-Mail: companyFILES `read_file` |
| Teams-Nachrichten | companyM365 `search_teams_messages` | Nur, wenn companyM365 aktiviert ist |
| Eine Datei in OneDrive oder SharePoint | companyM365 `search_files` (OneDrive) oder `microsoft_search` (SharePoint-Sites), dann companyM365 `read_file` mit `id` **und** `driveId` (aus `parentReference.driveId`) oder mit der Freigabe-`url`. Geschlossene Excel-Dateien: `workbook_get_overview`, `workbook_read_range` | Nur, wenn companyM365 aktiviert ist; sonst den Nutzer bitten, die Datei anzuhängen. Die companyFILES-Tools können keine OneDrive-/SharePoint-Dateien öffnen |
| Eine Datei an eine E-Mail anhängen | companyM365 `attach_file_to_draft` an einen Entwurf, mit genau einer Quelle: `chatFileId` (Datei aus diesem Chat), `documentId` (companyFILES), `fileUrl` (OneDrive/SharePoint) | Nur Entwürfe, nie Versand. Siehe de-m365-mail |

companyRAG kann keine im Chat angehängten Dateien indexieren. Für eine Ad-hoc-Frage zu einer angehängten Datei nimm die companyFILES-Lesetools oder Code-Ausführung. Sollen die Daten dauerhaft oder für andere durchsuchbar sein, müssen sie über die companyRAG-Oberfläche oder von einem Admin in eine companyRAG-Collection bzw. ein Dataset aufgenommen werden.

## Drei Tools namens `read_file`

Bis zu drei Tools mit diesem Namen können in deiner Tool-Liste stehen. Sie lesen aus verschiedenen Quellen und ersetzen einander nicht. Die App steht im Tool-Namen (z. B. `read_file_mcp_Files`, `read_file_mcp_Microsoft365`; der Servername hängt vom Tenant ab), das eingebaute hat kein Suffix.

| Tool | Parameter | Liest |
| --- | --- | --- |
| eingebautes `read_file` (ohne Suffix) | `path` | Dateien, die zu einem Skill gehören (`<skill-name>/references/…`), und mit Code-Ausführung Dateien in der Sandbox. Nie eine `file_id` |
| companyFILES `read_file` | `librechat_file_id` oder `document_id`, optional `part`, `offset` | Im Chat angehängte Dateien und companyFILES-Dokumente in Formaten, die die anderen Lesetools nicht abdecken (`.msg`, `.eml`, ZIP, `.doc`, `.xls`, `.ppt`, ODF, Scans). Nur, falls verfügbar |
| companyM365 `read_file` | genau eins von `id` (+ `driveId`), `url`, `documentId`; `format` `text` oder `markdown` | OneDrive- und SharePoint-Dateien. Liest keine Chat-Anhänge |

Wähle nach dem Ort der Datei: im Chat angehängt → companyFILES; in OneDrive/SharePoint → companyM365; Teil eines Skills → eingebaut. Für DOCX, XLSX, PDF und PPTX aus dem Chat gehen die spezifischen companyFILES-Lesetools (`read_word`, `read_excel`, …) vor.

## Optional: Wenn Code-Ausführung verfügbar ist

Nutze sie für Berechnungen auf angehängten Daten, Diagramme als Bild und Massenänderungen. Ohne Code-Ausführung nimm die Alternative aus der Tabelle.

- Im Chat angehängte Dateien liegen in der Sandbox unter `/mnt/data/<dateiname>`. Prüfe zuerst mit `os.listdir("/mnt/data")`.
- Die Sandbox hat keinen Netzwerkzugriff: keine Downloads, keine API-Aufrufe, kein `pip install`.
- Prüfe eine Bibliothek per `import`, bevor du dich auf sie verlässt (meist vorhanden: pandas, numpy, openpyxl, xlsxwriter, python-docx, python-pptx, matplotlib, plotly, Pillow, reportlab, PyPDF2, pdfminer.six; dazu `pdftoppm`/`pdftotext`). Nicht vorhanden: LibreOffice (kein Rendern von DOCX/PPTX als PDF oder Bild), pdfplumber, das neuere `pypdf`. Fehlt eine, nimm die Alternative.
- Jeder Aufruf läuft höchstens etwa 15 Sekunden; nur `/mnt/data` bleibt zwischen Aufrufen erhalten (`/tmp`, Variablen und das Arbeitsverzeichnis nicht).
- Speichere Ergebnisse unter neuem Namen in `/mnt/data/`; sie kommen als Chat-Anhänge zurück. Überschreibe nie die Eingabe.
- Rechne im Code, nicht im Kopf, und berichte die Zahlen aus der Code-Ausgabe.
- Für ein formatiertes XLSX/DOCX/PPTX im Corporate Design nimm lieber companyFILES (oder den Vorlagen-Weg) als eine im Code neu gebaute Datei.

## Regeln

1. **Erfinde nie eine `file_id`.** Nur aus dem Block der angehängten Dateien oder aus `list_my_files`. Dieselbe `file_id` taugt als Bild im Deck: `lc:<file_id>` in `slides[].image` oder in `images` eines Layouts.
2. **Sag, was fehlt.** Hängt ein Weg an einer App oder an Code-Ausführung, die nicht in deiner Tool-Liste ist, nimm die Alternative oder sag es dem Nutzer klar.
3. **Ein Weg pro Aufgabe.** Lies dieselbe Datei nicht „sicherheitshalber“ mit mehreren Tools.
4. **Nur Textauszug?** Antwortet ein Tool, dass LibreChat nur einen Textauszug der Datei hat, bitte den Nutzer, die Originaldatei erneut anzuhängen.
