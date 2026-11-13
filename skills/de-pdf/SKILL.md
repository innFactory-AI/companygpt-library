---
name: de-pdf
description: 'Erstelle und lies PDF-Dokumente und fülle PDF-Formulare mit companyFILES MCP-Tools aus. Verwende diesen Skill, wenn ein PDF-Bericht erzeugt, Inhalte als PDF exportiert, ein PDF aus HTML oder Markdown erstellt, Text aus einem PDF gelesen oder extrahiert, ein PDF-Formular ausgefüllt oder ein Formular für die finale Abgabe schreibgeschützt (flatten) gemacht werden soll.'
---

# PDF Skill

Tools zum Erstellen von PDF-Dokumenten, zum Lesen von PDF-Inhalten und zum Ausfüllen bzw. Fixieren (flatten) von PDF-Formularen.

## Tools in diesem Skill

| Tool                        | Zweck                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| `create_pdf`                | PDF aus Markdown mit Kopfzeilen, Fußzeilen und Seitenzahlen erstellen                                   |
| `create_pdf_from_html`      | PDF aus HTML mit eigenem CSS erstellen                                                                  |
| `read_pdf`                  | Text und Metadaten aus einem PDF extrahieren                                                            |
| `read_pdf_form_fields`      | Die ausfüllbaren Felder **jedes** hochgeladenen/erstellten PDFs auflisten (keine Vorlage nötig)         |
| `fill_pdf_form_fields`      | Die Felder **jedes** hochgeladenen/erstellten PDFs ausfüllen und als neues PDF speichern (`flatten` für schreibgeschützt) |
| `list_pdf_form_templates`   | Die persönlichen PDF-Formularvorlagen des Benutzers und ihre Felder auflisten                           |
| `fill_pdf_form`             | Eine persönliche PDF-Formularvorlage ausfüllen – die Felder bleiben bearbeitbar                         |
| `fill_and_flatten_pdf_form` | Eine persönliche PDF-Formularvorlage ausfüllen und fixieren (schreibgeschützt / final)                  |

## Entscheidungshilfe

```
Benutzer will ein PDF ERSTELLEN aus...
  Markdown             → create_pdf
  HTML / CSS           → create_pdf_from_html

Benutzer will ein PDF LESEN → read_pdf  (gescanntes PDF ohne Textebene → read_file mit OCR, falls verfügbar)

Benutzer will ein PDF-Formular AUSFÜLLEN...
  Ein hochgeladenes/beliebiges PDF (BEVORZUGT, keine Vorlage nötig):
    1. read_pdf_form_fields   (exakte Feldnamen + Typen ermitteln)
    2. fill_pdf_form_fields   (flatten=true setzen, um das Ergebnis zu sperren)
  Eine persönliche PDF-Formularvorlage (eine Vorlage vom Typ pdf):
    1. list_pdf_form_templates  (verfügbare Vorlagen + Felder ermitteln)
    2. fill_pdf_form            (bearbeitbar) ODER fill_and_flatten_pdf_form (gesperrt)
```

## Tool-Verwendung

### create_pdf

```json
{
  "markdown": "# Monatsbericht\n\n## Zusammenfassung\n\nIn diesem Monat haben wir...",
  "filename": "monthly_report",
  "title": "Monatsbericht – Mai 2025",
  "author": "Finanzen",
  "page_size": "A4",
  "page_orientation": "portrait",
  "header_text": "Vertraulich",
  "footer_text": "Acme Corp",
  "show_page_numbers": true,
  "page_number_position": "footer",
  "page_number_format": "{page} / {pages}"
}
```

### create_pdf_from_html

```json
{
  "html": "<h1>Rechnung</h1><table>...</table>",
  "css": "body { font-family: Arial; } h1 { color: #336699; }",
  "filename": "invoice",
  "title": "Rechnung #1234",
  "page_size": "A4",
  "show_page_numbers": true
}
```

Unterstützt eingebettete Bilder über die URI `doc:<documentId>` (gespeichertes Dokument), `lc:<file_id>` (LibreChat-Anhang) oder `img:<name>` (Bildbibliothek, siehe `list_image_templates`): `<img src="doc:abc123..." />`. Dasselbe gilt für Markdown-Bilder in `create_pdf`: `![alt](doc:<uuid>)`, `![alt](lc:<file_id>)` oder `![alt](img:<name>)`.

### read_pdf

```json
{
  "file_content": "<base64-kodiertes pdf>"
}
```

Akzeptiert genau eines von `file_content` (base64), `librechat_file_id` oder `document_id`. Liefert den extrahierten Text und die Metadaten. `read_pdf` liest nur die Textebene des PDFs (keine OCR) – für ein gescanntes PDF ohne Text verwende, wo verfügbar, `read_file` aus dem **de-file-management**.

### read_pdf_form_fields

Untersucht die Formularfelder **jedes** hochgeladenen oder erstellten PDFs – keine Registrierung als Vorlage nötig. Akzeptiert `document_id` **oder** `librechat_file_id`.

```json
{
  "document_id": "abc12345-..."
}
```

Liefert `{ document_id, filename, fieldCount, fields }`, wobei jedes Feld `name`, `type` (`text`, `checkbox`, `dropdown`, `radio`), den aktuellen Wert und (bei Dropdown/Radio) `options` enthält. Rufe dieses Tool zuerst auf, um vor dem Ausfüllen die exakten Feldnamen zu erhalten. (Datumsfelder erscheinen als `text`; Signatur- und Schaltflächenfelder werden nicht aufgelistet.)

Funktioniert auch bei verschlüsselten PDFs – siehe [Verschlüsselte PDFs](#verschlüsselte-pdfs-nur-owner-passwort) unten.

### fill_pdf_form_fields

Füllt die Felder eines beliebigen hochgeladenen/erstellten PDFs aus und speichert das Ergebnis als **neues** PDF (das leere Originalformular bleibt erhalten). Akzeptiert `document_id` **oder** `librechat_file_id`.

```json
{
  "document_id": "abc12345-...",
  "values": {
    "fullName": "Alice Smith",
    "agree": true,
    "department": "Engineering"
  },
  "flatten": false,
  "filename": "application_alice"
}
```

Werte: Strings für Text-, Datums-, Dropdown- und Radio-Felder, Booleans für Checkboxen. Setze `flatten: true`, um das Ergebnis schreibgeschützt zu machen.

### Verschlüsselte PDFs (nur Owner-Passwort)

Viele Behörden- und Versicherungsformulare setzen ein **Owner-Passwort** mit **leerem User-Passwort**, nur um die Bearbeitung zu blockieren. Laut PDF-Spezifikation probieren Viewer zuerst das leere User-Passwort aus. Deshalb öffnen sich diese Dateien überall ganz normal und wirken ungeschützt – sie sind aber vollständig AES-verschlüsselt.

Beide Tools kommen damit zurecht, also **behandle solche Dateien ganz normal**: Lies die Felder und fülle sie dann aus. Das ausgefüllte Ergebnis behält seine ursprüngliche Verschlüsselung und wird in jedem Viewer angezeigt.

Eine Einschränkung: **`flatten: true` funktioniert nicht** bei einem verschlüsselten PDF und liefert einen eindeutigen Fehler. Fülle ohne `flatten` aus (das Ergebnis bleibt bearbeitbar, was der Benutzer meist ohnehin möchte), oder bitte den Benutzer, den Schutz zuerst zu entfernen (das PDF in einem Editor öffnen und neu speichern oder in ein neues PDF drucken), falls er ausdrücklich ein gesperrtes Ergebnis braucht.

Verwende die Optionswerte aus `read_pdf_form_fields` beim Ausfüllen **wörtlich**. Bei verschlüsselten PDFs sind Radio- und Checkbox-Optionen die rohen Exportwerte des Formulars – oft knappe Codes wie `18a`, `19c` oder `0`/`1` statt lesbarer Beschriftungen. Rate oder verschönere sie nie; gib genau das zurück, was das Lese-Tool gemeldet hat, sonst wird das Feld als übersprungen gemeldet und die gültigen Optionen werden aufgelistet.

### list_pdf_form_templates

```json
{}
```

Liefert `{ templates: [{ name, uploadedAt, size, fields }] }` – die persönlichen PDF-Formularvorlagen des Benutzers mit Feldnamen, Typen (text, checkbox, radio, dropdown) und Optionen.

### fill_pdf_form

```json
{
  "template_name": "application",
  "values": {
    "fullName": "Alice Smith",
    "email": "alice@example.com",
    "agree": true,
    "department": "Engineering"
  },
  "filename": "application_alice"
}
```

Die Felder bleiben nach dem Ausfüllen **bearbeitbar**.

### fill_and_flatten_pdf_form

```json
{
  "template_name": "application",
  "values": {
    "fullName": "Alice Smith",
    "agree": true
  },
  "filename": "application_alice_final"
}
```

Das Formular wird **fixiert** (schreibgeschützt) – verwende das für finale Fassungen und Archivkopien.

## Gemeinsame Seitenoptionen (Erstell-Tools)

| Parameter               | Werte                               | Standard           |
| ----------------------- | ----------------------------------- | ------------------ |
| `page_size`             | `A4`, `Letter`, `Legal`, `A3`, `A5` | `A4`               |
| `page_orientation`      | `portrait`, `landscape`             | `portrait`         |
| `page_number_position`  | `header`, `footer`                  | `footer`           |
| `page_number_alignment` | `left`, `center`, `right`           | `center`           |
| `page_number_format`    | String mit `{page}` und `{pages}`   | `{page} / {pages}` |

## Wichtige Hinweise

- Alle Erstell-Tools liefern `{id, filename, downloadUrl, markdownLink}` – gib in der Antwort immer `markdownLink` aus.
- **Um ein beliebiges hochgeladenes PDF auszufüllen**, verwende `read_pdf_form_fields` + `fill_pdf_form_fields` – keine Vorlage nötig. Die Tools `*_pdf_form` / `*_form_templates` funktionieren nur mit den persönlichen PDF-Formularvorlagen des Benutzers.
- PDF-Formularvorlagen sind persönlich: Es sind die eigenen Vorlagen des Benutzers vom Typ `pdf`. Globale oder vom Admin verwaltete PDF-Formularvorlagen gibt es nicht. Der Vorlagen-Upload in der companyFILES-Weboberfläche akzeptiert derzeit nur .docx, .xlsx, .potx und .pptx, daher lassen sich persönliche PDF-Formularvorlagen nur über die REST-API hinzufügen – in der Praxis füllst du PDFs mit `read_pdf_form_fields` + `fill_pdf_form_fields` aus.
- Wird bei `fill_pdf_form` / `fill_and_flatten_pdf_form` kein `filename` angegeben, heißt die Ausgabe `<YYYYMMDD>_<template_name>.pdf`.
- Typen der Feldwerte: Strings für Text-, Dropdown- und Radio-Felder, Booleans für Checkboxen.
- Die CI der Organisation bzw. des Benutzers wird automatisch angewendet, wenn sie konfiguriert ist: Farben, Schriften und Größen, Seitenformat, Kopf-/Fußzeile, Seitenzahlen und das Logo an der eingestellten Position. Schriften, die auf dem Server nicht installiert sind, erscheinen als Ersatzschrift gleicher Art.
