---
name: en-word-odt
description: 'Create and read Word (.docx) and ODT (.odt) documents with companyFILES MCP tools. Use when asked to write a report, letter, or document in Word or OpenDocument format, convert Markdown or HTML to Word/ODT, extract text from a Word file, or create a document with headers, footers, table of contents, or page numbers. Also fills a corporate Word document or form that has no {{placeholders}} (sample text, text boxes, content controls, tables) with code execution.'
---

# Word & ODT Skill

Tools for creating Word (.docx) and ODT (.odt) documents, plus reading Word files.

## Tools in This Skill

| Tool                    | Purpose                                                                         |
| ----------------------- | ------------------------------------------------------------------------------- |
| `create_word`           | Create Word (.docx) from Markdown or plain text                                 |
| `create_word_from_html` | Create Word from HTML with optional CSS                                         |
| `create_word_from_json` | Dump JSON data into Word as a plain key/value listing                           |
| `create_odt`            | Create ODT from Markdown (LibreOffice/OpenOffice)                               |
| `create_odt_from_html`  | Create ODT from HTML                                                            |
| `read_word`             | Read a Word (.docx) file → text, HTML, Markdown (from base64 or LibreChat file) |
| `read_word_content`     | Read stored Word document content by document_id → markdown-like string         |
| `append_to_word`        | Append Markdown content to an existing stored Word document in-place            |
| `replace_word_content`  | Replace entire content of an existing stored Word document in-place             |

## Decision Guide

```
User wants to create a Word document from...
  Markdown / plain text  → create_word          (most common)
  HTML + CSS             → create_word_from_html
  Raw JSON data (dump)   → create_word_from_json  (no layout control)
  A template             → see en-templates   (create_word_from_template)

User wants OpenDocument format (LibreOffice)...
  From Markdown          → create_odt
  From HTML              → create_odt_from_html
  From template          → see en-templates   (create_odt_from_template)

User wants to READ a Word file...
  From base64 / LibreChat attachment  → read_word
  From stored document (document_id)  → read_word_content

User wants to EDIT an existing stored Word document...
  Inspect current content first       → read_word_content
  Add more content at the end         → append_to_word    (keeps existing content)
  Rewrite the whole document          → replace_word_content

User wants to FILL a corporate document / form in its own layout...
  It has {{placeholders}}             → see en-templates (create_word_from_template)
  No {{}}: sample text, text boxes,   → "Filling a corporate document without {{placeholders}}"
  content controls, empty tables         below (code execution)
```

## Tool Usage

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

`format` can be `"markdown"` (default) or `"plain"`. Note: `create_word` has **no `author` field** — only `create_word_from_html`, `create_odt` and `create_odt_from_html` accept `author`.

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

Supports inline images via `doc:<documentId>` (stored companyFILES doc), `lc:<file_id>` (LibreChat attachment) or `img:<name>` (image library, see `list_image_templates` in **en-templates**) URI: `<img src="doc:abc123..." />`. The same syntax works in Markdown for `create_word`: `![alt](doc:<uuid>)`, `![alt](lc:<file_id>)` or `![alt](img:<name>)`. An unknown `img:` name fails the call with an error naming it.

### create_word_from_json

```json
{
  "json_content": "{\"customer\":\"Acme Corp\",\"items\":[{\"name\":\"Widget\",\"qty\":2}]}",
  "filename": "order_data"
}
```

Writes the JSON as a simple listing under the heading "Document Generated from JSON": one paragraph per field (`key: value`, key in bold); nested objects and arrays are indented, array items appear as `[0]`, `[1]`, …. There is no element schema (no headings, tables or styling from JSON) and no title, author or page options — only `json_content` and `filename`. For a designed document, turn the data into Markdown and use `create_word`.

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

Accepts any one of `file_content` (base64), `librechat_file_id` (LibreChat attachment), or `document_id` (stored companyFILES doc). Returns `{ text, html, markdown }`.

### read_word_content

Read the content of a stored Word document (created or uploaded via companyFILES). Accepts `document_id` **or** `librechat_file_id`. Returns a markdown-like string plus character count — use this before appending or replacing to understand the current state.

```json
{
  "document_id": "uuid-of-stored-word-doc"
}
```

Returns `{ document_id, librechat_file_id, filename, character_count, content }`.

### append_to_word

Append Markdown (or plain text) to an existing Word document. Identify the target with `document_id` **or** `librechat_file_id`. A page break is inserted before the new content by default. The document is updated in-place — same `document_id`.

```json
{
  "document_id": "uuid-of-stored-word-doc",
  "content": "## New Section\n\nAdditional content here...",
  "format": "markdown",
  "add_page_break": true
}
```

`add_page_break` defaults to `true`. Use `false` to continue on the same page.

### replace_word_content

Replace the entire content of an existing Word document with new Markdown. Identify the target with `document_id` **or** `librechat_file_id`. All page layout options (`page_size`, `header_text`, etc.) work the same as `create_word`. The document is updated in-place — same `document_id`.

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

## Common Page Options (all create tools except `create_word_from_json`)

| Parameter               | Values                              | Default            |
| ----------------------- | ----------------------------------- | ------------------ |
| `page_size`             | `A4`, `Letter`, `Legal`, `A3`, `A5` | `A4`               |
| `page_orientation`      | `portrait`, `landscape`             | `portrait`         |
| `page_number_position`  | `header`, `footer`                  | `footer`           |
| `page_number_alignment` | `left`, `center`, `right`           | `center`           |
| `page_number_format`    | string with `{page}` and `{pages}`  | `{page} / {pages}` |

## Iterative Document Editing Pattern

For long documents that exceed a single context window, build them section by section:

1. `create_word` — create the document with the first section; note the returned `id` (pass it as `document_id`)
2. `append_to_word` — call repeatedly for each additional section
3. Optionally `read_word_content` to inspect the current state before continuing
4. `replace_word_content` — if a section needs to be fully rewritten

All three in-place tools (`read_word_content`, `append_to_word`, `replace_word_content`) operate on existing documents identified by `document_id` **or** `librechat_file_id` (a LibreChat attachment, updated in-place on the shared volume), not on base64 file content.

## Filling a corporate document without `{{placeholders}}`

A letterhead, offer template, form or report template the user attached usually has no
`{{placeholders}}`. Instead it has sample text ("[Kunde]", "XXX", "Lorem ipsum", "Max Mustermann"),
text boxes, content controls ("Klicken oder tippen Sie hier, um Text einzugeben."), checkboxes and
tables with an empty sample row. `replace_word_content` and `append_to_word` cannot fill such a
document. They rewrite it in the companyFILES layout or append to its end, so the layout the user
wanted is lost. Do not use them for this.

### If code execution is available

The document is in the sandbox at `/mnt/data/<filename>.docx`. This skill ships two scripts,
under `/mnt/data/skills/en-word-odt/scripts/` when it was installed as a package:

1. **Inventory**:

   ```bash
   python3 /mnt/data/skills/en-word-odt/scripts/docx_inventory.py "/mnt/data/<doc>.docx"
   ```

   It lists every non-empty paragraph with a key: `B12` (body), `H1.0` / `F1.2` (header/footer),
   the table cell (`[T0r1c2]`), `textbox`, style. It lists tables (`BT0: 3 rows x 3 cols`) and
   content controls with tag/title, type and whether they still show their placeholder. `!DUMMY`
   marks sample text. Long documents: `--range B0-B150`; empty paragraphs: `--all`.

2. **Fill**: plan and output in one call:

   ```bash
   cat > /tmp/plan.json <<'EOF'
   {
     "paragraphs": {"B2": "Thank you for your enquiry.", "B3": ["Consulting", "Implementation", "Training"],
                    "B18": "Erika Example", "B20": null, "H1.0": "Acme Corp | Offer 2026-117"},
     "tables": {"BT0": {"start_row": 1, "rows": [["Consulting", "2", "2,400 EUR"], ["Training", "1", "900 EUR"]], "trim": true}},
     "content_controls": {"Customer": "Acme Corp", "Approved": true},
     "replace": {"[Kunde]": "Acme Corp"}
   }
   EOF
   python3 /mnt/data/skills/en-word-odt/scripts/docx_fill.py "/mnt/data/<doc>.docx" /tmp/plan.json "/mnt/data/<result>.docx"
   ```

   - `paragraphs`: key → text. A list or `\n` adds paragraphs in the same style (e.g. more
     bullets), `<br>` is a line break, `null` deletes the paragraph. Images and text boxes anchored
     in a paragraph stay.
   - `tables`: fills rows from `start_row` (0 = header). More rows than the table has copy its
     last row with its formatting. `null` keeps a cell, and `trim` removes unused sample rows.
   - `content_controls`: by tag or title. `true`/`false` ticks a checkbox. The placeholder style
     ("Klicken oder tippen…") is removed.
   - `replace`: substring everywhere: body, tables, text boxes, headers, footers.
   - Text boxes are updated in both copies Word stores (otherwise older viewers show the old
     text). Formatting comes from the paragraph and its first run.
   - Keys always refer to the **source** document. The script resolves all of them before it
     changes anything. Write the plan to `/tmp` in the same call, because files in `/mnt/data`
     become chat attachments.

3. **Check**: the fill script ends with a check (exit code 2 and `CHECK FAILED` if sample text
   or a content-control placeholder is left). `docx_inventory.py "<result>" --check` checks on its
   own. Deliberately empty fields (a signature line) are fine; name them in the answer.

4. **Answer**: the result comes back as a chat attachment. Name what you filled and what stays
   for the user to fill. You can only check the text, not the page layout. Ask the user to check
   line and page breaks.

**Without the scripts** (only `SKILL.md` was pasted): use python-docx (`import docx` first).

- Walk all paragraphs, including table cells, text boxes (`w:txbxContent`), headers and footers.
- Change text in the existing runs; setting `paragraph.text` wipes the formatting.
- Copy a table row with `copy.deepcopy(row._tr)`.
- Content controls are `w:sdt` elements. Remove `w:showingPlcHdr` after filling one.
- See **en-templates** (`references/code-template-editing.md`) for the run-level replace recipe.

**Limits:**

- The sandbox has no LibreOffice, so there is no render and no PDF export of the result. For a
  PDF, use `convert_document` (convert skill) on the finished DOCX if it is available.
- ODT has no Python library in the sandbox.
- Legacy form fields (`FORMTEXT`) and tracked changes are not handled; say so if the document
  uses them.

### Without code execution

No tool fills such a document in its own layout. Tell the user plainly, and offer:

- Turn on code execution (chat/agent setting or the `RUN_CODE` permission from an admin).
- Make the document a real template once: replace the sample text with `{{placeholders}}` in
  Word and upload it as a template. After that, `create_word_from_template` fills it without code
  (en-templates).
- The filled-in texts as a list to paste in, or a new document with `create_word` in the
  companyFILES/CI design, clearly labelled as not their template.

## Key Notes

- All create tools return `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id` when the document is also stored as a chat file) — always render `markdownLink` in the reply.
- In-place edit tools (`append_to_word`, `replace_word_content`) on a companyFILES document return the same `id` and an updated `markdownLink`. On a chat attachment (`librechat_file_id`) that was updated in place, they return only `{librechat_file_id, filename, message}` — there is no download link; tell the user the attached file was updated. If the attachment cannot be updated in place, the modified copy is saved as a **new** document and its new `id`/`markdownLink` is returned — use that id from then on.
- Inline images can be referenced via `doc:<documentId>`, `lc:<file_id>` or `img:<name>` (image library) in the Markdown or HTML of the create tools (`create_word`, `create_word_from_html`, `create_odt`, `create_odt_from_html`) — SVG is auto-converted to PNG for Word. `append_to_word` and `replace_word_content` do not resolve these references.
- Unset page/header/footer options fall back to the org/user theme defaults (e.g. `defaultPageSize`, `defaultHeaderText`, `defaultShowPageNumbers`) before the documented hard defaults apply.
- For template-based Word creation (placeholders, loops, image injection), use the **en-templates**. Image placeholders there are `{IMAGE name}` or `{%name}` (typed in one go); `width`/`height` in cm form a box the image is fitted into without distortion (`fit`: `contain` default, `cover` crops, `stretch` only on request).
- ODT files open natively in LibreOffice and Google Docs.
- The org/user CI is applied automatically when configured: colours, fonts and sizes, page format, header/footer, page numbers and the logo at the configured position (header or footer, left/center/right). For a document you build yourself with code execution, `get_corporate_ci` returns the same values.
