---
name: en-convert
description: 'Convert documents between formats with companyFILES MCP tools. Use when asked to convert a file, change format, export Word to PDF, convert Excel to CSV or JSON, transform Markdown to Word or PDF, or convert HTML to Word. Also covers listing all supported conversion pairs.'
---

# Convert Skill

Tools for converting documents between formats.

## Tools in This Skill

| Tool                        | Purpose                                    |
| --------------------------- | ------------------------------------------ |
| `convert_document`          | Convert a file between supported formats   |
| `get_supported_conversions` | List all supported format conversion pairs |

## Supported Conversions

| From     | To                             |
| -------- | ------------------------------ |
| Excel    | CSV, JSON, Markdown, HTML      |
| CSV      | Excel, JSON, Markdown, HTML    |
| JSON     | Excel, CSV, Markdown           |
| Word     | Text, Markdown, HTML, PDF      |
| Markdown | Word, PDF, HTML, Text, ODT     |
| HTML     | Word, PDF, Markdown, Text, ODT |
| PDF      | Text                           |

> When in doubt, call `get_supported_conversions` to get the full current list.

PDF can only be converted to plain text. `excel` means `.xlsx`. Other formats — e.g. `.doc`, `.xls`, `.xlsb`, `.ppt`, OpenDocument, Outlook `.msg`/`.eml` or ZIP — are not inputs for `convert_document`: read them with `read_file`, or save them as one Markdown document with `convert_to_markdown` (both in the **en-file-management**, only where available).

## Tool Usage

### convert_document

Input can be base64 `file_content`, a `librechat_file_id`, or a `document_id` (stored companyFILES doc).

```json
{
  "file_content": "<base64-encoded file>",
  "from_format": "word",
  "to_format": "pdf",
  "filename": "converted_document",
  "title": "My Document",
  "author": "Alice"
}
```

Using a LibreChat file ID:

```json
{
  "librechat_file_id": "<file_id from list_my_files>",
  "from_format": "excel",
  "to_format": "csv",
  "filename": "data_export"
}
```

`from_format` (source) values: `excel`, `word`, `pdf`, `csv`, `json`, `markdown`, `html` — note `text` is **not** a valid source.
`to_format` (target) values: `excel`, `word`, `pdf`, `csv`, `json`, `markdown`, `html`, `text`, `odt`.

Returns `{id, filename, downloadUrl, markdownLink}` — always render `markdownLink` in the reply.

---

### get_supported_conversions

```json
{}
```

Returns `{ conversions: [{ from, to: [...] }] }` — one entry per source format with its possible targets.

## Key Notes

- `title` and `author` are only used when the output is `word`, `pdf` or `odt`.
- To get a file ID to convert, take the `file_id` of an attachment from the `Attached files in this message:` block, or use `list_my_files` (from **en-file-management**) to discover `librechat_file_id` or `document_id` values.
- For reading document content without conversion, use `read_excel` / `read_word` / `read_pdf` from their respective skills.
