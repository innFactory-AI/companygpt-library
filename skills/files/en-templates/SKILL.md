---
name: en-templates
description: 'Create documents from templates using companyFILES MCP tools. Use when asked to fill a template, use a company template, create a document from a predefined layout, fill placeholders, use a letterhead, fill an invoice template, or create from a DOCX/XLSX/POTX/ODT template. Covers Word, Excel, ODT, and PowerPoint template filling, including image placeholders, the image library (stock images, key visuals, icons as `img:<name>`) and loop/repeat syntax, and handing a template to the code interpreter for edits the template tools cannot make.'
---

# Templates Skill

Tools for listing and filling document templates (Word, Excel, ODT, PowerPoint).

## Tools in This Skill

| Tool                                    | Purpose                                                                           |
| --------------------------------------- | --------------------------------------------------------------------------------- |
| `list_templates`                        | List all available templates (personal + global) with placeholder info            |
| `create_word_from_template`             | Fill a DOCX template with `{placeholder}` syntax                                  |
| `create_word_from_template_with_images` | Fill a DOCX template with text and image placeholders                             |
| `create_excel_from_template`            | Fill an XLSX template by cell address **or** `{{placeholder}}` name (auto-routed) |
| `fill_excel_template`                   | Fill an XLSX template using `{{placeholder}}` syntax                              |
| `create_odt_from_template`              | Fill an ODT template with `{{placeholder}}` syntax                                |
| `create_powerpoint_from_template`       | Fill a POTX/PPTX template with text, images, charts, speaker notes, slide repeat  |
| `attach_template_to_chat`               | Attach a copy of a template to the chat for the code interpreter                  |
| `list_image_templates`                  | Search the image library (image templates) for `img:<name>` references            |

## Workflow

1. **Discover templates:** Call `list_templates` (optionally filter by `type`: `docx`, `xlsx`, `potx`, `odt`, `pdf`, `image`)
2. **Note placeholder names** from the response
3. **Fill the template** with the matching `create_*_from_template` tool
4. **Only if the template tools cannot do it** (bulk or free-form changes in the template's layout) and code execution is available: `attach_template_to_chat`, then edit with code (see below)

## Tool Usage

### list_templates

```json
{
  "type": "potx"
}
```

Returns per template: `name`, `displayName`, `description`, `category`, `tags`, placeholder lists, `loopSources`, `fields` (for PDF form templates), `size`, `isDefault`, upload dates, and scope (`"user"` personal or `"global"`).

For **POTX/PPTX** templates the response includes a per-slide breakdown (`slideInfo`):

- `slideNumber` — 1-based slide index
- `layoutName` — PowerPoint layout name (e.g. `"Title Slide"`, `"Two Content"`)
- `layoutType` — value from a `{{slide_type:xxx}}` marker on that slide (e.g. `"section"`, `"default"`, `"text-image"`)
- `textPlaceholders` — `{{key}}` placeholders on this slide
- `imagePlaceholders` — `{%name}` placeholders on this slide
- `chartPlaceholders` — `{{name}}` chart container placeholders on this slide

Use this breakdown to know exactly which placeholder goes on which slide before calling `create_powerpoint_from_template`. Filter by `type` to narrow results: `"docx"`, `"xlsx"`, `"potx"`, `"odt"`, `"pdf"`, `"image"`. Image templates (the image library) only appear with `type: "image"`; to find a fitting image, use `list_image_templates` (see below).

---

### Image library (image templates)

Admins upload organisation images (stock photos, key visuals, icons) in the companyFILES UI under Templates → Upload, users their own (PNG, JPEG, WebP, GIF, TIFF, BMP; no SVG). A personal image hides an organisation image of the same name. Find them with `list_image_templates`:

```json
{ "search": "team office", "orientation": "landscape", "aspect_ratio": 1.78, "limit": 10 }
```

All arguments are optional: `search` (all words must appear in name, description or tags), `tag`, `orientation` (`landscape`, `portrait`, `square`), `aspect_ratio` (width/height; sorts the closest first), `limit`. Each result has `ref` (`"img:<name>"`), `description`, `tags`, `width`, `height`, `aspectRatio` and `orientation`. Look at a candidate with `view_image { "image_template": "<name>" }`.

Use the image as `img:<name>` wherever an image is accepted (`slides[].image`, layout `images`, Markdown `![alt](img:<name>)`) or as `image_template` in the `{%name}` image objects of Word and PowerPoint templates. Pick an image whose `aspectRatio` is close to the target slot's, so little is cropped. An unknown name fails the call with an error naming the reference.

---

### create_word_from_template

Placeholder syntax: `{placeholder}` (single curly braces). Dotted paths: `{user.name}`.

```json
{
  "template_name": "invoice",
  "data": {
    "customer": "Acme Corp",
    "invoice_number": "INV-2025-042",
    "date": "2025-05-08",
    "total": "€4,200.00"
  },
  "filename": "invoice_acme"
}
```

**Table loop syntax** (place FOR/END-FOR in their own table rows):

```
{FOR item IN items}
{= $item.name} | {= $item.qty} | {= $item.price}
{END-FOR item}
```

Pass `items` as an array in `data`. Missing loop sources are silently skipped with a warning.

**Template expressions are not JavaScript.** Inside `{…}` commands only data paths (`$item.price`, `rows[0]`), literals, operators (`+ - * / %`, comparisons, `&& || ??`, `cond ? a : b`), the commands `FOR`, `IF` and `EXEC`, and a short allowlist of helpers work — e.g. `toFixed`, `toUpperCase`, `join`, `toLocaleDateString`, `Math.round`, `parseFloat`, `new Date(…)`. Arrow functions, `.map`/`.filter`, loops and template literals make the fill fail — compute such values beforehand and pass them in `data`.

---

### create_word_from_template_with_images

Supports text placeholders `{name}` and image placeholders `{IMAGE logo}` or the short form `{%logo}` (type it in one go, otherwise Word splits it and it stays as text).

```json
{
  "template_name": "letterhead",
  "placeholders": {
    "company": "Acme Corp",
    "date": "2025-05-08",
    "logo": {
      "data": "<base64-encoded image>",
      "width": 4,
      "height": 2,
      "extension": "png"
    }
  },
  "filename": "letter_acme"
}
```

Image via stored document or from the image library (no re-upload needed):

```json
{
  "logo": { "document_id": "abc12345-...", "width": 4, "height": 2 },
  "hero": { "image_template": "office-team", "width": 16, "height": 9, "fit": "cover" }
}
```

Image values: `{data, extension}` or `{document_id | librechat_file_id | image_template}`. `width`/`height` (cm) are optional and form a box: the image keeps its aspect ratio inside it (`fit: "contain"`, default), `"cover"` crops it to the box, `"stretch"` distorts (only on request). Only one of `width`/`height` scales the other; none = natural size, at most 16 cm wide. `create_word_from_template` takes the same image objects.

The org/user logo is **auto-injected** only into a placeholder named exactly `logo` (i.e. `{%logo}`) — and only when configured in settings and no `logo` value is passed. Differently-named image placeholders (e.g. `{%companyLogo}`) are **not** auto-filled. The logo keeps its aspect ratio (inside 4 × 2 cm).

---

### create_excel_from_template

Accepts **either** cell addresses (e.g. `"A1"`, `"Sheet2!B3"`) **or** `{{placeholder}}` names (pass the bare name without `{{ }}`) in `cell_values` — it auto-routes based on the keys you pass; mixed keys default to placeholder mode. Use `list_templates` to see available XLSX templates.

```json
{
  "template_name": "budget",
  "cell_values": {
    "A1": "Budget 2025",
    "B5": 125000,
    "Sheet2!C3": "Approved"
  },
  "filename": "budget_2025"
}
```

---

### fill_excel_template

Fills cells using `{{placeholder}}` syntax — preserves formatting, styles, formulas, and charts.

```json
{
  "template_name": "monthly_report",
  "data": {
    "company": "Acme Corp",
    "month": "May 2025",
    "total": 42000
  },
  "replace_missing": false,
  "filename": "report_may"
}
```

---

### create_odt_from_template

Fills `{{placeholder}}` syntax in ODT templates.

```json
{
  "template_name": "letter",
  "data": {
    "recipient": "John Doe",
    "date": "2025-05-08",
    "subject": "Offer Letter"
  },
  "replace_missing": false,
  "filename": "offer_letter_john"
}
```

---

### create_powerpoint_from_template

Placeholder syntax:

- **Text:** `{{key}}` anywhere in a text box
- **Image:** `{%name}` in the **alt text** (`descr` attribute) of an image shape
- **Chart:** `{{name}}` in the **alt text** of a chart container shape
- **Layout marker:** `{{slide_type:default}}`, `{{slide_type:section}}`, `{{slide_type:text-image}}` — invisible metadata marker; declares the slide's layout type for `repeat` routing (multi-source). Cleared automatically from the output. The layout-native tools (`create_powerpoint_from_layouts`, `add_slides_from_layouts`) ignore it.

Always run `list_templates` first — for POTX/PPTX it returns a per-slide breakdown including `layoutName`, `layoutType` (from the `{{slide_type:xxx}}` marker), and which text/image/chart placeholders belong to each slide.

> **If the POTX/PPTX template has NO `{{}}` placeholders** and the call passes no `images`, `charts` or `speaker_notes`, this tool refuses the call and names the layout tools instead — `list_templates` flags such templates with `hasLegacyPlaceholders: false` and a `nextStep` hint. Corporate-design slide masters (Folienmaster) shipped by design teams usually contain no `{{}}` markup at all — they carry named slide layouts instead. Run `describe_pptx_template { "template_name": "..." }`: when `hasLegacyPlaceholders` is `false`, switch to `create_powerpoint_from_layouts` (see **en-powerpoint**, "corporate master without `{{}}`"). Never ask the user to type `{{}}` markers into a corporate master. If its layouts have no text slots either and the content areas are plain text boxes with sample text on example slides ("Text", "XXX", "TITEL"), that is path D in **en-powerpoint** (code execution). The same holds for a Word template without `{{}}` (sample text, text boxes, content controls): see **en-word-odt**, "Filling a corporate document without `{{placeholders}}`".

**Basic usage (single-record fill):**

```json
{
  "template_name": "corporate_deck",
  "placeholders": {
    "title": "Q4 Results",
    "subtitle": "Finance Team",
    "date": "May 2025"
  },
  "images": {
    "logo": { "base64": "<base64-png>" },
    "chart_screenshot": { "document_id": "abc123..." }
  },
  "speaker_notes": {
    "1": "Welcome everyone to the Q4 review",
    "3": "These are the key takeaways"
  },
  "charts": {
    "revenue_chart": {
      "labels": ["Q1", "Q2", "Q3", "Q4"],
      "datasets": [{ "label": "Revenue", "values": [100, 150, 120, 180] }]
    }
  },
  "filename": "q4_deck"
}
```

`speaker_notes` keys are **1-based** slide numbers.

`charts` only renames the chart's series (`datasets[].label`). `labels` and `values` are **not** applied yet — the server logs them as "not yet implemented" and the chart keeps the template's data. Do not promise the user updated chart numbers.

Image sources per `images` entry: `base64`, `document_id`, `librechat_file_id` or `image_template` (image library, e.g. `{ "image_template": "office-team" }`). The image is fitted into the placeholder picture's frame, never distorted: `fit` per image, default `"cover"` (fills the frame, centre crop), `"contain"` for names containing "logo" (whole image, centred); `"stretch"` only on request.

No logo is placed automatically in PowerPoint templates: only `{{company_name}}` is auto-filled from the settings. To show a logo, pass it explicitly in `images` (e.g. `"logo"` for `{%logo}`).

The tool takes only `template_name` — no `document_id` / `librechat_file_id`. A `{{}}` deck attached in the chat must be uploaded as a template first, or be edited in clone mode (see **en-powerpoint** §2a).

**Single-source repeat** (duplicate one slide per data record):

```json
{
  "template_name": "team_deck",
  "repeat": {
    "slide": 3,
    "data": [
      { "name": "Alice", "role": "Engineer" },
      { "name": "Bob", "role": "Designer" }
    ]
  }
}
```

`repeat.slide` is the 1-based slide number to duplicate; the slide is replaced by N copies, one per data record. By default, slides that are **not** repeated are removed from the output — set `repeat.keep_unused_slides: true` to keep them. `create_powerpoint_from_template` also accepts top-level `title` and `author`.

**Multi-source repeat** (route each record to the slide matching its `slide_type`):

Use this when the template has multiple layout slides marked with `{{slide_type:xxx}}` and each data record should use a different layout.

```json
{
  "template_name": "dynamic_deck",
  "repeat": {
    "data": [
      { "slide_type": "section", "title": "Chapter 1" },
      { "slide_type": "default", "title": "Results", "content": "Revenue up 15%" },
      { "slide_type": "text-image", "title": "Architecture", "bullets": "Fast\nScalable" }
    ]
  }
}
```

Omit `repeat.slide` when using `slide_type` routing — the matching template slide is found automatically from its `{{slide_type:xxx}}` marker. The `slide_type` values (`default`, `section`, `text-image`) correspond to the same layout names used in `create_powerpoint`.

---

### attach_template_to_chat

Attaches a copy of a template (personal or global) to the current chat as a file, so the code interpreter can open and edit it with Python — for changes the `create_*_from_template` tools cannot make (e.g. replace a term throughout the document including tables and footers, add many table rows in the template's style, rebuild a sheet, add slides from the master's layouts).

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string (max. 100) | yes | Template name exactly as listed by `list_templates` |
| `type` | `docx` \| `xlsx` \| `potx` \| `odt` | yes | Template type as listed by `list_templates` (no `pdf`) |

```json
{ "name": "invoice", "type": "docx" }
```

- **Prerequisites:** code execution must be enabled for the chat or agent (and allowed for the user's role), and the environment must store companyFILES documents as LibreChat files. Otherwise the tool answers with an error — then stay with the template tools.
- **Next turn:** the file reaches the code interpreter only from the user's **next** message on (usually at `/mnt/data/<name>.<type>`), not in the same reply. Tell the user that the template is attached and ask them to send their next message (e.g. "go ahead").
- A `potx` template is attached as `<name>.pptx`, so python-pptx opens it directly.
- Calling it again is cheap: an unchanged template re-attaches the same file, a changed one replaces the old copy. The template itself stays unchanged.
- If it answers that the hand-off is still running, call it again with the same arguments after about 30 seconds — no second copy is created.

#### If code execution is available: edit the template with Python

1. Check that the file is there (`/mnt/data/`) and that the library loads (`import docx` / `openpyxl` / `pptx`).
2. If you add new content the template does not style (sections, tables, slides), call `get_corporate_ci` first and apply the CI's colors, fonts and sizes; where the template defines styles, the template wins.
3. Change text inside the existing runs/cells so the layout stays; never overwrite the input — save the result under a new name in `/mnt/data/`, it comes back as a chat attachment.
4. Re-open the result and check for leftover placeholders before reporting success.

The detailed recipe (Word, Excel, PowerPoint code, pitfalls such as openpyxl dropping charts) is in the bundled file `references/code-template-editing.md` — read it with the built-in `read_file` tool, path `en-templates/references/code-template-editing.md` (not the companyFILES tool of the same name). It only exists when this skill was installed as a package (zip); if only `SKILL.md` was pasted, use the four steps above.

**Fallback without code execution** (or if the file or library is missing): fill the template with the `create_*_from_template` tools above, then refine the result with the iterative tools below (`append_to_word`, `replace_word_content`, `append_slides_to_powerpoint` with `reference_slide`, `modify_excel`). ODT has no Python library in the standard sandbox: use `create_odt_from_template`.

## Post-Template Editing (Iterative Updates)

Every template tool returns the new document's `id`. Pass it as `document_id` to the iterative editing tools from **en-word-odt** and **en-powerpoint** to further modify the filled document without regenerating from scratch.

### After `create_word_from_template` / `create_word_from_template_with_images`

| Goal                         | Tool                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| Inspect current content      | `read_word_content { "document_id": "<id>" }`                                        |
| Add more sections at the end | `append_to_word { "document_id": "<id>", "content": "...", "add_page_break": true }` |
| Fully rewrite the document   | `replace_word_content { "document_id": "<id>", "content": "..." }`                   |

Example — fill a template then append a custom appendix:

```json
// Step 1: fill the template
{ "template_name": "report", "data": { "title": "Annual Report" } }
// → returns id "abc123" (use it as document_id)

// Step 2: append extra content
{ "document_id": "abc123", "content": "## Appendix A\n\nAdditional data...", "add_page_break": true }
```

### After `create_powerpoint_from_template`

| Goal                                  | Tool                                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Inspect existing slides               | `read_powerpoint_slides { "document_id": "<id>" }`                                                                  |
| Add new slides at the end             | `append_slides_to_powerpoint { "document_id": "<id>", "slides": [...] }`                                            |
| Replace a specific slide              | `update_powerpoint_slide { "document_id": "<id>", "slide_number": 3, "slides": [...] }`                             |
| **Add a slide matching the template** | `append_slides_to_powerpoint { "document_id": "<id>", "reference_slide": 2, "placeholders": {...} }`                |
| **Replace a slide, keep the look**    | `update_powerpoint_slide { "document_id": "<id>", "slide_number": 3, "reference_slide": 2, "placeholders": {...} }` |

> **Keep the template look:** appending/updating with `slides`/`markdown` renders the generic theme, which will **not** match a template deck. Use `reference_slide` + `placeholders` (clone-and-refill) instead — it copies an existing slide's design and refills its `{{placeholders}}`. See **en-powerpoint** for full details. (Clone mode refills text placeholders only; for image placeholders re-run `create_powerpoint_from_template`.)

Example — fill a template then append a custom closing slide:

```json
// Step 1: fill the template
{ "template_name": "corporate_deck", "placeholders": { "title": "Q4 Results" } }
// → returns id "def456" (use it as document_id)

// Step 2a: add a generic (non-template-styled) closing slide
{ "document_id": "def456", "slides": [{ "type": "section", "title": "Thank You", "subtitle": "Questions?" }] }

// Step 2b: OR add a slide that matches the template by cloning slide 2 and refilling it
{ "document_id": "def456", "reference_slide": 2, "placeholders": { "title": "Next Steps", "owner": "PMO" } }
```

## Key Notes

- All create tools return `{id, filename, downloadUrl, markdownLink}` — always render `markdownLink` in the reply.
- When `filename` is omitted, the filled document is named after `template_name` (`create_word_from_template_with_images`: `document`).
- `create_word_from_template_with_images` falls back to a global `default.docx` if the named template is missing, whereas `create_word_from_template` does not — verify the template exists with `list_templates` first.
- Template names are **case-sensitive** — always verify with `list_templates` first.
- User templates take priority over global templates with the same name.
- `replace_missing: false` (default) leaves unfilled `{{placeholder}}` tokens intact; `true` replaces them with empty string.
- Warnings about missing placeholders are included in the response when applicable.
- After filling a template, use the iterative tools (`append_to_word`, `append_slides_to_powerpoint`, etc.) to add or update content — the `document_id` stays the same throughout.
- `attach_template_to_chat` is the exception path for changes the template tools cannot make; it needs code execution and works from the user's next message on.
