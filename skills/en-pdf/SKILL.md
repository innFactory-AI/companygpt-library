---
name: en-pdf
description: 'Create and read PDF documents, and fill PDF forms with companyFILES MCP tools. Use when asked to generate a PDF report, export content as PDF, create a PDF from HTML or Markdown, read or extract text from a PDF, fill a PDF form, or flatten a form for final delivery.'
---

# PDF Skill

Tools for creating PDF documents, reading PDF content, and filling/flattening PDF forms.

## Tools in This Skill

| Tool                        | Purpose                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------- |
| `create_pdf`                | Create PDF from Markdown with headers, footers, page numbers                           |
| `create_pdf_from_html`      | Create PDF from HTML with custom CSS                                                   |
| `read_pdf`                  | Extract text and metadata from a PDF                                                   |
| `read_pdf_form_fields`      | List the fillable fields of **any** uploaded/created PDF (no template needed)          |
| `fill_pdf_form_fields`      | Fill **any** uploaded/created PDF's fields, saving a new PDF (`flatten` for read-only) |
| `list_pdf_form_templates`   | List the user's personal PDF form templates and their fields                           |
| `fill_pdf_form`             | Fill a personal PDF form template — fields remain editable                             |
| `fill_and_flatten_pdf_form` | Fill and flatten a personal PDF form template (read-only / final)                      |

## Decision Guide

```
User wants to CREATE a PDF from...
  Markdown             → create_pdf
  HTML / CSS           → create_pdf_from_html

User wants to READ a PDF → read_pdf  (scanned PDF without text layer → read_file with OCR, if available)

User wants to FILL a PDF form...
  An uploaded/arbitrary PDF (PREFERRED, no template needed):
    1. read_pdf_form_fields   (discover exact field names + types)
    2. fill_pdf_form_fields   (set flatten=true to lock the result)
  A personal PDF form template (a template of type pdf):
    1. list_pdf_form_templates  (discover available templates + fields)
    2. fill_pdf_form            (editable) OR fill_and_flatten_pdf_form (locked)
```

## Tool Usage

### create_pdf

```json
{
  "markdown": "# Monthly Report\n\n## Executive Summary\n\nThis month we achieved...",
  "filename": "monthly_report",
  "title": "Monthly Report – May 2025",
  "author": "Finance",
  "page_size": "A4",
  "page_orientation": "portrait",
  "header_text": "Confidential",
  "footer_text": "Acme Corp",
  "show_page_numbers": true,
  "page_number_position": "footer",
  "page_number_format": "{page} / {pages}"
}
```

### create_pdf_from_html

```json
{
  "html": "<h1>Invoice</h1><table>...</table>",
  "css": "body { font-family: Arial; } h1 { color: #336699; }",
  "filename": "invoice",
  "title": "Invoice #1234",
  "page_size": "A4",
  "show_page_numbers": true
}
```

Supports inline images via `doc:<documentId>` (stored doc), `lc:<file_id>` (LibreChat attachment) or `img:<name>` (image library, see `list_image_templates`) URI: `<img src="doc:abc123..." />`. The same applies to Markdown images in `create_pdf`: `![alt](doc:<uuid>)`, `![alt](lc:<file_id>)` or `![alt](img:<name>)`.

### read_pdf

```json
{
  "file_content": "<base64-encoded pdf>"
}
```

Accepts any one of `file_content` (base64), `librechat_file_id`, or `document_id`. Returns extracted text and metadata. `read_pdf` reads the PDF's text layer only (no OCR) — for a scanned PDF without text, use `read_file` from the **en-file-management** where available.

### read_pdf_form_fields

Inspect the form fields of **any** uploaded or created PDF — no template registration needed. Accepts `document_id` **or** `librechat_file_id`.

```json
{
  "document_id": "abc12345-..."
}
```

Returns `{ document_id, filename, fieldCount, fields }`, where each field has `name`, `type` (`text`, `checkbox`, `dropdown`, `radio`), current value, and (for dropdown/radio) `options`. Call this first to get exact field names before filling. (Date fields appear as `text`; signature and push-button fields are not listed.)

Works on encrypted PDFs too — see [Encrypted PDFs](#encrypted-pdfs-owner-password-only) below.

### fill_pdf_form_fields

Fill the fields of any uploaded/created PDF and save the result as a **new** PDF (the original blank form is preserved). Accepts `document_id` **or** `librechat_file_id`.

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

Values: strings for text/date/dropdown/radio fields, booleans for checkboxes. Set `flatten: true` to make the result read-only.

### Encrypted PDFs (owner-password only)

Many authority and insurance forms set an **owner password** with an **empty user password** purely to block editing. The PDF spec makes viewers try the empty user password first, so these files open normally everywhere and look unprotected — but they are fully AES-encrypted.

Both tools handle them, so **treat such files as normal**: read the fields, then fill them. The filled result keeps its original encryption and renders in every viewer.

One limitation: **`flatten: true` does not work** on an encrypted PDF and returns a clear error. Fill without `flatten` (the result stays editable, which is usually what the user wants anyway), or tell them to remove the protection first (open the PDF in an editor and re-save, or print it to a new PDF) if they specifically need a locked result.

Use the option values from `read_pdf_form_fields` **verbatim** when filling. On encrypted PDFs, radio and checkbox options are the form's raw export values — often terse codes like `18a`, `19c` or `0`/`1` rather than readable labels. Never guess or prettify them; pass back exactly what the read tool reported, or the field is reported as skipped with the valid options listed.

### list_pdf_form_templates

```json
{}
```

Returns `{ templates: [{ name, uploadedAt, size, fields }] }` — the user's personal PDF form templates with field names, types (text, checkbox, radio, dropdown) and options.

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

Fields remain **editable** after filling.

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

Form is **flattened** (read-only) — use for final/archival copies.

## Common Page Options (create tools)

| Parameter               | Values                              | Default            |
| ----------------------- | ----------------------------------- | ------------------ |
| `page_size`             | `A4`, `Letter`, `Legal`, `A3`, `A5` | `A4`               |
| `page_orientation`      | `portrait`, `landscape`             | `portrait`         |
| `page_number_position`  | `header`, `footer`                  | `footer`           |
| `page_number_alignment` | `left`, `center`, `right`           | `center`           |
| `page_number_format`    | string with `{page}` and `{pages}`  | `{page} / {pages}` |

## Key Notes

- All create tools return `{id, filename, downloadUrl, markdownLink}` — always render `markdownLink` in the reply.
- **To fill an arbitrary uploaded PDF**, use `read_pdf_form_fields` + `fill_pdf_form_fields` — no template needed. The `*_pdf_form` / `*_form_templates` tools only work with the user's personal PDF form templates.
- PDF form templates are personal: they are the user's own templates of type `pdf`. There are no global or admin-managed PDF form templates. The template upload in the companyFILES web UI currently accepts only .docx, .xlsx, .potx and .pptx, so personal PDF form templates can only be added through the REST API — in practice, fill PDFs with `read_pdf_form_fields` + `fill_pdf_form_fields`.
- When `filename` is omitted on `fill_pdf_form` / `fill_and_flatten_pdf_form`, the output is named `<YYYYMMDD>_<template_name>.pdf`.
- Field value types: strings for text/dropdown/radio fields, booleans for checkboxes.
- The org/user CI is applied automatically when configured: colours, fonts and sizes, page format, header/footer, page numbers and the logo at the configured position. Fonts not installed on the server render as a fallback of the same kind.
