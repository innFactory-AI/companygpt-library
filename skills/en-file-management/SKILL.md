---
name: en-file-management
description: 'Upload, download, list, search, and manage files with companyFILES MCP tools. Use when asked to upload a file, find a document, list stored files, get a download link, search documents by name or type, create a ZIP archive, save a text/code file, read e-mails, archives or other formats as Markdown, or look at a stored image. Also covers discovering LibreChat file IDs for use in other tools.'
---

# File Management Skill

Tools for uploading, listing, searching, downloading, archiving, reading, and creating text files in companyFILES.

## Tools in This Skill

| Tool                           | Purpose                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| `upload_file`                  | Upload any file (base64) for storage — returns document ID                                   |
| `download_stored_file`         | Get download info for a stored file or a chat upload                                         |
| `list_documents`               | List all your documents, including chat uploads (no parameters)                              |
| `search_documents`             | Search documents and chat uploads by filename, type, or date range                           |
| `list_my_files`                | List all accessible files (LibreChat + PVC storage)                                          |
| `create_zip_from_stored_files` | Bundle stored documents and/or chat uploads into a ZIP archive                               |
| `create_text_file`             | Create and store any text/code file (.sql, .csv, .json, .py, etc.)                           |
| `read_file`                    | Read almost any file as Markdown (e-mails, ZIP, legacy Office, OCR) — **if available**       |
| `save_file_part`               | Save one e-mail attachment or ZIP entry as a new document — **if available**                 |
| `convert_to_markdown`          | Save a whole file (e.g. an e-mail with attachments) as one `.md` document — **if available** |
| `view_image`                   | Look at a stored image or an image attached in the chat                                      |

## Attached Files

When the user attached files, the message context lists them in a block `Attached files in this message:` with one line per file: `- file_id: …, filename: …, type: …, size: … bytes` (plus `stored only` when the content is not in your context). Pass that `file_id` as `librechat_file_id` (or as `document_id` where a tool accepts a LibreChat `file_id`). Use `list_my_files` only when there is no such block, e.g. for a file from an earlier chat. Never guess an ID. Which tool or app fits which file task (companyFILES, code execution, companyRAG, transcription, translation): see the **en-file-routing**.

## Decision Guide

```
User wants to upload a file                   → upload_file
User wants a download link for a stored file  → download_stored_file
User wants to browse / list documents         → list_documents  (or open_companyfiles_ui from en-settings-ui)
User wants to find a specific document        → search_documents
User wants to see all files including chat uploads → list_my_files
User wants to bundle files into a ZIP         → create_zip_from_stored_files
User wants to create a code/text file         → create_text_file
User wants to open an e-mail, ZIP or other format → read_file  (if available)
User wants an attachment of that e-mail/ZIP as its own file → save_file_part  (if available)
User wants you to look at an image            → view_image
```

## Tool Usage

### upload_file

Max size: 50 MB by default (the limit can differ per environment). Content must be base64-encoded.

```json
{
  "content": "<base64-encoded file content>",
  "filename": "logo.png",
  "mime_type": "image/png"
}
```

The content is checked against the file extension (magic bytes): empty files and files whose content does not match their extension (e.g. a PDF renamed to `.docx`) are rejected with a `validation` error. Accepted are Office documents, PDF, images, ZIP and common text formats; where `read_file` is available, also formats such as `.msg`, `.eml`, `.doc`, `.xls`, `.xlsb`, `.ppt`, RTF, OpenDocument and EPUB.

Returns `{id, filename, downloadUrl, markdownLink, size, type, message}`. Use `id` as `document_id` in other tools.

---

### download_stored_file

`document_id` accepts a companyFILES document ID **or** a LibreChat `file_id` (chat upload, see `list_my_files`).

```json
{
  "document_id": "abc12345-...",
  "return_content": false
}
```

- companyFILES document → `{id, filename, downloadUrl, size, type, createdAt, expiresAt}`
- Chat upload (LibreChat `file_id`) → `{id, filename, size, type, source: "librechat", note}` — **no download link**; the `note` points to the read tools.

Set `return_content: true` to also get base64 `content` (files < 1 MB only).

> To **read** the contents of Excel/Word/PDF files, use `read_excel` / `read_word` / `read_pdf` (other formats: `read_file`) — not this tool.

---

### list_documents

```json
{}
```

No parameters. Returns `{documents, total}` — your companyFILES documents **plus** your chat uploads (LibreChat files). Each entry has `id`, `filename`, `type`, `createdAt`, `expiresAt`, `size`, `isUploaded` and, if the file lives in LibreChat, `libreChatFileId` (for chat uploads `id` is the LibreChat `file_id`). Also opens an embedded UI view for interactive browsing.

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

All parameters are optional. `search` is a case-insensitive substring match on filename. `type` values: `word`, `excel`, `powerpoint`, `pdf`, `text`, `image`, `archive`, `file`. Chat uploads are searched as well. Returns `{documents, total}` in the same shape as `list_documents`.

---

### list_my_files

```json
{}
```

Returns files from both LibreChat (chat uploads) and PVC (companyFILES storage). Each entry has either `file_id` (LibreChat) or `document_id` (PVC) or both. Use these IDs in read tools (`read_excel`, `read_word`, `read_pdf`, `read_file`), `view_image` and `convert_document`.

When the user attaches a `.pptx` and asks for a deck "in this design" or wants the attached deck
extended, take its `file_id` from the attached-files block (or find it here), then hand it straight to
`describe_pptx_template` / `create_powerpoint_from_layouts` / `add_slides_from_layouts` — no
template upload needed. Only `create_powerpoint_from_template` (for a `{{}}` deck) takes nothing
but a `template_name`, so such a deck must be uploaded as a template first. See
**en-powerpoint** §2a.

---

### create_zip_from_stored_files

Max total uncompressed size: 50 MB. `document_ids` takes 1–50 IDs — companyFILES document IDs and/or LibreChat `file_id`s.

```json
{
  "document_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "filename": "project_files",
  "compression_level": 6
}
```

ZIP archives are **temporary** (auto-deleted after 1 day by default). They do not appear in `list_documents`. If some `document_ids` can't be resolved the ZIP is still created from the rest, and the unresolved IDs are returned in a `missingDocumentIds` field plus a `warning` (rather than failing).

---

### create_text_file

Works with essentially **any** text/code extension (`.sql`, `.csv`, `.json`, `.xml`, `.html`, `.css`, `.js`, `.ts`, `.tsx`, `.jsx`, `.py`, `.java`, `.kt`, `.swift`, `.scala`, `.go`, `.rs`, `.rb`, `.php`, `.c`, `.h`, `.cpp`, `.cs`, `.yaml`, `.yml`, `.toml`, `.md`, `.txt`, `.log`, `.sh`, `.bash`, `.zsh`, `.env`, `.ini`, `.cfg`, `.conf`, `.properties`, `.graphql`, `.proto`, …). The list is a **blocklist, not an allowlist** — any unblocked text extension is accepted. A few executable extensions are blocked for security (e.g. `.ps1`, `.bat`, `.exe`) and will be rejected even though they're text.

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

### read_file / save_file_part / convert_to_markdown (if available)

These three tools exist only where the extended file reading is enabled — if they are not in your tool list, they are not available. `read_file` reads formats the other readers do not cover: Outlook `.msg` and `.eml` e-mails (headers, body, attachments), ZIP archives (entries), `.doc`, `.xls`, `.xlsb`, `.ppt`, `.rtf`, OpenDocument (`.odt`/`.ods`/`.odp`), EPUB, HTML, CSV/JSON/XML, Jupyter notebooks, images and scanned PDFs (OCR). For `.docx`/`.xlsx`/`.pdf` the regular readers stay the first choice.

```json
{
  "librechat_file_id": "<file_id of the attachment>",
  "part": "0",
  "offset": 0
}
```

All three take `document_id` or `librechat_file_id`. `read_file` returns the Markdown of one part, paged (continue with the `offset` given at the end; `max_chars` sets the page size), the list of parts (e-mail attachments or ZIP entries with ids such as `"0.1"`), e-mail headers and warnings. Read an attachment by passing its `part` id. `save_file_part` (`part` required, e.g. `"0.2"`) stores that part with its original bytes as a new companyFILES document, so the regular tools work on it; `convert_to_markdown` saves the whole file (or one `part` and its children) as one `.md` document. If a long conversion (OCR, LibreOffice) is still running, the tool says so — call it again after about 30 seconds.

---

### view_image

Hands a stored image (PNG, JPEG, WebP, GIF) back to you so you can describe or analyze it — e.g. an uploaded photo or an exported chart.

```json
{
  "document_id": "abc12345-..."
}
```

Takes `document_id`, `librechat_file_id` or `image_template` (an image from the image library, see `list_image_templates` in the **en-templates**).

## Key Notes

- `upload_file` validates file size (max 50 MB by default), extension and content (the bytes must match the extension).
- `document_id` from any create/upload tool can be reused in ZIP creation, template image injection (`document_id` in image placeholders), and `doc:` URI references in the Markdown/HTML of the create tools (`create_word*`, `create_odt*`, `create_pdf*`, `create_powerpoint`; not in append/replace/update tools). Images from the image library work the same way as `img:<name>`.
- If LibreChat holds only the text extract of a chat file (uploaded "as text"), tools that need the original file answer: "Von dieser Datei liegt bei LibreChat nur ein Textauszug vor – bitte die Originaldatei erneut hochladen." Pass this on and ask the user to attach the original file again.
- Documents are auto-deleted after a retention period (default 365 days; can differ per environment).
- Where the CAD extension is available, CAD/BIM/3D files (DXF, STEP, IFC, STL, …) have their own tools (`describe_model`, `query_model`, …; see the **en-cad-bim**).
- For interactive file browsing, use `open_companyfiles_ui` from the **en-settings-ui**.
