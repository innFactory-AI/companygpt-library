---
name: en-powerpoint
description: 'Build and refine PowerPoint (.pptx) presentations with companyFILES MCP tools. Use when asked to create a presentation, build a deck, add or fix slides, use a corporate slide master / Folienmaster, or work with a .pptx the user attached in the chat ("make a deck in this design", "add slides to this presentation"). Covers all three build paths: from scratch (create_powerpoint), from a {{placeholder}} template (create_powerpoint_from_template), and from a corporate master WITHOUT any placeholders via its native slide layouts (describe_pptx_template, create_powerpoint_from_layouts, add_slides_from_layouts, set_powerpoint_slide_fields). Also covers iterative editing (append_slides_to_powerpoint, update_powerpoint_slide, read_powerpoint_slides), clone-and-refill of template slides, styled tables, speaker notes, images and charts, and design decks whose example slides only hold plain text boxes with sample text ("Text", "XXX", "TITEL"), filled with code execution.'
---

# PowerPoint Skill

Everything needed to build, extend and repair `.pptx` decks.

## Tool map

| Tool                              | Purpose                                                             |
| --------------------------------- | ------------------------------------------------------------------- |
| `create_powerpoint`               | New deck from Markdown or a typed `slides` array (built-in design)  |
| `create_powerpoint_from_template` | New deck from a POTX/PPTX template that contains `{{placeholders}}` |
| `describe_pptx_template`          | Read a deck's **native slide layouts** — no `{{}}` needed           |
| `create_powerpoint_from_layouts`  | New deck by instantiating those native layouts (corporate design)   |
| `add_slides_from_layouts`         | Append layout-native slides to an existing deck, **in place**       |
| `set_powerpoint_slide_fields`     | Patch one slide's native placeholders (text + images), in place     |
| `append_slides_to_powerpoint`     | Append slides to an existing deck, in place                         |
| `update_powerpoint_slide`         | Replace one slide of an existing deck, in place                     |
| `read_powerpoint_slides`          | Read slide numbers, titles, text **and each slide's layout/slots**  |
| `list_my_files`                   | Find a deck the user attached in the chat (`file_id`)               |
| `list_templates`                  | Find available templates (`type: "potx"`) before building           |
| `list_image_templates`            | Find images in the image library (`img:<name>`)                     |
| `embed_chart_in_document`         | Chart.js chart as a new deck; `title` adds a title slide            |

---

## 1. Work iteratively — do not one-shot a deck

**A deck of more than ~6 slides must be built in several tool calls.** One giant
`create_powerpoint` call is the most common failure mode: the arguments get truncated, layout
choices cannot be corrected, and a single bad slide means regenerating everything.

The loop:

```
PLAN   → write the outline in your reply first (slide number, role/layout, headline, content sketch)
PROBE  → describe_pptx_template / list_templates / read_powerpoint_slides — learn what exists
SEED   → create_powerpoint* with the FIRST 3–5 slides only → keep the returned id (document_id)
EXTEND → append_slides_to_powerpoint (path A/B) or add_slides_from_layouts (path C)
         in chunks of 3–5 slides, repeatedly
REFINE → set_powerpoint_slide_fields or update_powerpoint_slide for individual fixes
VERIFY → read_powerpoint_slides to confirm slide count, order, titles and that no sample text is left
```

**Never report a deck as done before you have read it back.** Slides that still show the
template's sample text ("Text", "XXX", "TITEL", "Lorem ipsum") or that came out empty are a
failure, not a result. Fix them, or tell the user exactly which slides are not filled and why.

### PLAN before the first tool call

For anything beyond a couple of slides, show the user a plan and let them react. It costs one
message and prevents rebuilding a 20-slide deck.

```
Plan — "Digitalstrategie 2027" (12 slides, corporate master `folienmaster`)

 #  Layout / role      Headline                      Content
 1  title              Digitalisierungsstrategie 2027 Author + date
 2  section            1. Ausgangslage
 3  content            Kernbefunde                   3 bullets, 1 nested
 4  two-content        Handlungsoptionen             Option A | Option B
 5  section            2. Zielbild
 …
12  closing            —                             Contact block

I'll build 1–5 first, then append 6–12 in two chunks. Say if the structure should change.
```

### Rules of thumb

- **Chunk size 3–5 slides** per call. Long bullet text or `htmlTable` content → 2–3.
- **Keep the `document_id`.** The first create call returns the deck's `id`; every
  append/update/patch call on that deck keeps the _same_ id. Reuse it; never build a second deck
  to fix the first.
- **One bad slide → patch that slide.** `set_powerpoint_slide_fields` (layout-native) or
  `update_powerpoint_slide` (built-in / clone mode). Both preserve slide count and position.
- **`read_powerpoint_slides` between chunks** when you have appended several times, to confirm
  you are numbering slides from the right base.
- **Report progress**, e.g. "slides 1–5 done, appending 6–9 next", and render the returned
  `markdownLink` so the user can open the intermediate state.
- **Never re-create to append.** `add_slides_from_layouts` / `append_slides_to_powerpoint`
  exist precisely so a deck can grow across turns.

Every slide in a **typed** `slides` array (`create_powerpoint`, `append_slides_to_powerpoint`,
`update_powerpoint_slide`) **requires a `title`** (it is a mandatory field, including for `section`
slides) — a slide without a `title` fails validation. The layout tools' `slides` have a different
shape — `layout`, `fields`, `images`, `notes` — and no `title` field; a title goes in
`fields.title`.

---

## 2. Pick the build path

Decide once, at the start. Mixing paths in one deck produces inconsistent design.

| Situation                                                   | Path                                    |
| ----------------------------------------------------------- | --------------------------------------- |
| No template mentioned, companyFILES design is fine          | **A** `create_powerpoint`               |
| A template exists **and** contains `{{key}}` markup         | **B** `create_powerpoint_from_template` |
| A corporate master / Folienmaster with **no** `{{}}` markup | **C** `create_powerpoint_from_layouts`  |
| A design deck whose **example slides** carry the design as plain text boxes with sample text, and whose layouts have (almost) no text slots | **D** clone and fill the example slides (code execution, §4a) |

**How to tell B, C and D apart:** run `describe_pptx_template` on the template and read
`hasLegacyPlaceholders`.

- `true` → the deck uses `{{}}` → path **B** (see also **en-templates**)
- `false` → look at the layouts' `slots`:
  - the layouts you need have text slots (`title`, `body:*`, …) → path **C**
  - the layouts have **no or almost no text slots**, but `read_powerpoint_slides` (with
    `include_layouts: false`) shows text on the deck's own slides ("Text", "XXX", "TITEL",
    "UNTERTITEL", "Text 1 … Text 4", an agenda with "01 XXX") → path **D**. The design lives in
    the example slides, not in the layouts. A layout slide built from such a master comes out
    **empty** (only background, logo and footer), and `set_powerpoint_slide_fields` reports
    `unknownFields` for every key.
- Mixed decks are common: a title layout with real slots, but content slides as example slides.
  Decide per slide type; when in doubt, use path D for the whole deck so all slides come from
  the same source.

`list_templates` (`type: "potx"`) lists candidates and, for `{{}}` decks, a per-slide placeholder
breakdown. It does **not** return the layout catalog — use `describe_pptx_template` for that.

A deck the user attached to the chat needs no template upload for path C — see the next section.
Path B is the exception: `create_powerpoint_from_template` only takes a `template_name`.

---

## 2a. The user attached a `.pptx` in the chat

This is the common case: someone drops their Folienmaster or an existing deck into the
conversation and asks for a presentation "in this design", or asks to extend the deck they just
sent. For a corporate master (no `{{}}`), **do not ask them to upload it as a template** — the
layout tools, `read_powerpoint_slides`, `append_slides_to_powerpoint` and `update_powerpoint_slide`
take the attachment directly. `create_powerpoint_from_template` does not: it has only
`template_name`, no `document_id` / `librechat_file_id`.

```
FIND    file_id from the "Attached files in this message:" block
        (no block: list_my_files → pick the .pptx by filename; list_documents /
        search_documents work too — pass the entry's id)
PROBE   describe_pptx_template { "librechat_file_id": "<file_id>" }
        → hasLegacyPlaceholders decides the path (B vs C)
        read_powerpoint_slides { "librechat_file_id": "<file_id>" } if the deck has content
        you need to see or extend — it reports each slide's layout and slot keys
        → layouts without text slots + sample text on the slides = path D (§4a)
BUILD   (path C)
        new deck   → create_powerpoint_from_layouts { "librechat_file_id": ..., "slides": [...] }
        extend it  → add_slides_from_layouts     { "librechat_file_id": ..., "slides": [...] }
        fix one    → set_powerpoint_slide_fields { "librechat_file_id": ..., "slide_number": n, ... }
```

**An attached `{{}}` deck (path B)** has two routes:

- To fill it with `create_powerpoint_from_template` (images, charts, `repeat`), it must be
  uploaded as a template first (web UI, `open_companyfiles_ui page="upload"`); then call the tool
  with that `template_name`.
- Or edit the attachment itself in clone mode (§5): `update_powerpoint_slide` with
  `reference_slide` equal to `slide_number` plus `placeholders` fills a slide in place;
  `append_slides_to_powerpoint` with `reference_slide` plus `placeholders` adds a filled copy.

**`librechat_file_id` and `document_id` are interchangeable inputs.** The server resolves either,
PVC first. Pass whichever id the listing gave you.

**New deck or edited deck?** Two different intents, two different tools:

| The user wants                                | Tool                             | Result                                          |
| --------------------------------------------- | -------------------------------- | ----------------------------------------------- |
| A presentation **in the design of** this deck | `create_powerpoint_from_layouts` | A **new** document; the attachment is untouched |
| More slides **in** this deck                  | `add_slides_from_layouts`        | The **same** deck, extended in place            |
| A slide of this deck changed                  | `set_powerpoint_slide_fields`    | The **same** deck, one slide patched            |

For an attachment, "in place" means: the file is rewritten on the shared LibreChat volume when
that volume is mounted (same `file_id`); otherwise the modified copy is saved as a new
companyFILES document. The response `message` says which happened — pass that on rather than
promising the user their original file changed.

**A deck built from Markdown has no fillable layouts.** `add_slides_from_layouts` refuses it and
names `append_slides_to_powerpoint` instead; that refusal is correct, don't work around it.

---

## 3. Path A — from scratch (`create_powerpoint`)

### Markdown mode (fast, text-heavy decks)

`#` or `##` starts a new slide. All slides get the `default` layout. A line of exactly `???`
starts speaker notes, which run until the next `#`/`##` heading.

> **`title` adds a slide.** Passing the top-level `title` argument to `create_powerpoint`
> prepends a generated dark title slide (title, author, today's date). So `n` content slides plus
> `title` = `n + 1` slides, and every later `slide_number` shifts by one. Omit `title` when you
> want to author the opening slide yourself. `append_slides_to_powerpoint` never adds one.

```json
{
  "markdown": "# Quarterly Results\n\n- Revenue: €1.2M\n- Growth: 15%\n\n???\nOpen with the revenue number.\n\n## Key Highlights\n\n- Launched new product\n- Expanded to 3 markets",
  "filename": "q4_results",
  "title": "Q4 2025 Results",
  "author": "Strategy Team"
}
```

Inline images in `create_powerpoint` Markdown use `doc:<documentId>`, `lc:<file_id>` or `img:<name>`
(image library, see §6):

```markdown
![Chart](doc:abc12345-...)
![Attachment](lc:xyz-librechat-file-id)
![Team](img:office-team)
```

### Typed slides mode (layout control)

Pass `slides` instead of `markdown`. When both are given, `slides` wins.

| `type`         | Visual                                                 | Fields                                                               |
| -------------- | ------------------------------------------------------ | -------------------------------------------------------------------- |
| `"default"`    | Accent bar + title + stacked content                   | `title`, `content`, `bullets`, `code`, `table`, `htmlTable`, `image` |
| `"section"`    | Dark background, large centred title — chapter divider | `title`, `subtitle`                                                  |
| `"text-image"` | Title on top, text/bullets left, image right           | `title`, `content`, `bullets`, `htmlTable`, `image`, `imageAlt`      |

Every type also accepts `notes` (speaker notes). Unknown `type` values fall back to `"default"`.
Omitting `image` on a `text-image` slide draws a skeleton placeholder box — useful for drafts.

**Titles stay on one line** (content, title and section slides): a long title is set smaller (down to 16 pt), and one
over about 60 characters is cut with "…". Keep slide titles short and put details in the content.

```json
{
  "slides": [
    { "type": "section", "title": "Q4 2025 Results", "subtitle": "Strategy Team" },
    {
      "type": "default",
      "title": "Key Metrics",
      "bullets": ["Revenue: €1.2M", "Growth: 15%", "NPS: 72"],
      "notes": "Lead with revenue; growth is YoY, not QoQ — expect that question."
    },
    {
      "type": "text-image",
      "title": "System Architecture",
      "bullets": ["Microservices", "Auto-scaling", "99.9% uptime"],
      "image": "https://www.example.com/architecture.png",
      "imageAlt": "Architecture diagram"
    }
  ],
  "title": "Q4 2025 Results",
  "filename": "q4_results"
}
```

`bullets` is a flat `string[]` here — for nested bullets use path C (`level`) or a template.
The `image` field takes `lc:<file_id>` (chat attachment or generated image, see `list_my_files`),
`doc:<document_id>`, `img:<name>` (image library), a base64 data URI or a public http(s) URL (see §6).
`imageFit` sets how it fills its area: `"contain"` (default, whole image, centred), `"cover"` (fills the
area, crops) or `"stretch"` (distorts — only on request). The same holds in `append_slides_to_powerpoint`
and `update_powerpoint_slide`.

**Native chart on a slide:** add `chart` to a `default` slide (below the text) or a `text-image` slide
(replaces the image — use `image` **or** `chart`, not both). It is a real, editable PowerPoint chart
("Edit Data" opens the numbers in Excel), in the corporate identity's colours and font. `section`
slides show none. Same data shape as `show_interactive_chart`:

```json
{
  "type": "default",
  "title": "Revenue per quarter",
  "bullets": ["Q3 is the strongest quarter"],
  "chart": {
    "type": "bar",
    "labels": ["Q1", "Q2", "Q3"],
    "datasets": [{ "label": "2026", "data": [12, 15, 19] }],
    "showValues": true
  }
}
```

`chart.type`: `bar`, `horizontalBar`, `stackedBar`, `line`, `area`, `pie`, `doughnut`, `scatter`, `radar`
(`pie`/`doughnut` show only the first dataset). Optional: `title`, `showLegend`, `showValues`,
`numberFormat` (Excel format, e.g. `"#,##0"`), `xAxisTitle`, `yAxisTitle`. Limits: at most 20 datasets with
1000 points each; every dataset needs exactly one number per label, otherwise the tool fails and names the
series. Also works in `append_slides_to_powerpoint` and `update_powerpoint_slide`.

### Styled tables — `htmlTable`

Use `htmlTable` instead of `table` when cells need colour, bold or alignment. Supported on
`default` and `text-image`; it takes precedence over `table`.

| Inline CSS                        | Effect      |
| --------------------------------- | ----------- |
| `background-color: #hex`          | Cell fill   |
| `color: #hex`                     | Text colour |
| `font-weight: bold`               | Bold        |
| `font-style: italic`              | Italic      |
| `text-align: left\|center\|right` | Alignment   |

`<th>` cells get the theme's header fill/text automatically unless overridden.

```json
{
  "type": "default",
  "title": "Revenue by Region",
  "htmlTable": "<table><tr><th>Region</th><th>Q1</th><th>vs PY</th></tr><tr><td style=\"font-weight:bold\">DACH</td><td>€1.2M</td><td style=\"color:#16A34A\">+18%</td></tr><tr><td style=\"font-weight:bold\">US</td><td>€0.8M</td><td style=\"color:#DC2626\">-3%</td></tr></table>"
}
```

For a plain grid, `table: string[][]` (first row = header) is enough.

---

## 4. Path C — corporate master without `{{}}` (layout-native)

This is the path for a deck the design team shipped, e.g. a `Corporate-Master.pptx`. Such
decks carry **no `{{}}` markup**, only named slide layouts with OOXML's own placeholders.
Content is bound to those placeholders and **no formatting is written**, so fonts, colours,
logos and geometry come from the master. ("Reset layout" in PowerPoint changes nothing — that is
the proof.)

Upload such a master as a template (a `.pptx` is stored as type `potx`) — or, if the user attached
it in the chat, use its `librechat_file_id` directly (section 2a).

### Step 1 — `describe_pptx_template`

```json
{ "template_name": "folienmaster" }
```

Returns:

```json
{
  "hasLegacyPlaceholders": false,
  "slideSize": { "widthEmu": 12192000, "heightEmu": 6858000 },
  "roleMap": { "title": "slideLayout5.xml", "section": "slideLayout8.xml", "content": "slideLayout9.xml" },
  "layouts": [
    {
      "layoutId": "slideLayout11.xml",
      "name": "Titel_mit_Inhalt",
      "masterId": "slideMaster3.xml",
      "role": "content",
      "exampleSlides": [4],
      "slots": [
        { "key": "title", "type": "title" },
        { "key": "body:10", "type": "body", "hint": "Mastertextformat bearbeiten" },
        { "key": "pic:14", "type": "pic", "isImage": true, "aspectRatio": 1.78 }
      ]
    },
    {
      "layoutId": "slideLayout9.xml",
      "name": "Inhalt",
      "role": "content",
      "exampleSlides": [],
      "slots": [{ "key": "title" }, { "key": "body:12" }, { "key": "body:13" }]
    }
  ]
}
```

Reading it:

- **`layoutId` is the stable identifier.** Layout **names repeat** across slide masters
  (a real deck had `Präsentationstitel` 3× across 5 masters). Prefer `layoutId`.
- **Slot keys are `type` or `type:idx`.** The `idx` matters: `body:12` + `body:13` on the same
  layout means a two-column layout — fill both to use both columns. The number does **not** tell
  you which box is left or on top: `body:13` can be the right column. Check the position (the `at`
  value of `--lists`, see "Lists come from the template" below), or fill the columns with texts that
  don't depend on their order.
- **`role`** is inferred from the layout name (German + English keywords) and its slot
  composition. Roles: `title`, `title-image`, `section`, `content`, `two-content`,
  `title-only`, `closing`, `reference`. `roleMap` picks one layout per role.
- **`hint`** is the layout's own prompt text and is only a hint — real masters often say
  "Mastertextformat bearbeiten" or lorem ipsum. Judge by name + slot shape, not by hint.
- **`isImage` slots (`pic:*`) take an image through the separate `images` argument**, not through
  `fields`. `aspectRatio` (width ÷ height of the slot frame) tells you what will crop well — the
  image is centre-cropped to that ratio, never stretched. From the image library pick an image with a
  close `aspectRatio` (`list_image_templates` with `aspect_ratio`). A slot you pass no image for stays empty
  and comes back in `imageSlotsNotFilled`; don't promise the user a picture then.
- **`acceptsChart` slots** (placeholder types `chart`, `obj`, `body`) take a native chart through the
  separate `charts` argument (see "Charts" below). `read_powerpoint_slides` reports `acceptsChart` too.

### Step 2 — `create_powerpoint_from_layouts`

Each slide picks its layout by `layoutId`, layout name, or role — mix freely.

```json
{
  "template_name": "folienmaster",
  "filename": "strategie-2027",
  "slides": [
    {
      "layout": "title",
      "fields": { "title": "Digitalisierungsstrategie 2027", "body:11": "Dr. Max Mustermann\n27.07.2026" },
      "notes": "Begrüßung, 2 Minuten."
    },
    { "layout": "Kapiteltrenner", "fields": { "title": "1. Ausgangslage" } },
    {
      "layout": "slideLayout11.xml",
      "fields": {
        "title": "Kernbefunde",
        "body:10": [
          "Drei Systeme decken 80 % ab",
          { "text": "Redundante Datenhaltung", "level": 1 },
          "Betriebskosten +9 % p. a."
        ]
      }
    },
    {
      "layout": "Inhalt",
      "fields": {
        "title": "Handlungsoptionen",
        "body:12": ["Option A: Konsolidierung", "Aufwand: hoch"],
        "body:13": ["Option B: Schnittstellen", "Aufwand: mittel"]
      }
    },
    { "layout": "closing", "fields": { "body:11": "Muster GmbH\n12345 Musterstadt" } }
  ]
}
```

**Images** go in a per-slide `images` object, keyed like `fields` (exact slot key, the bare type
`pic`, or the synonyms `image`/`picture`/`photo`). Sources are the usual three:

```json
{
  "layout": "title-image",
  "fields": { "title": "Standort München" },
  "images": { "pic:14": { "librechat_file_id": "abc-attachment-id" } }
}
```

`{ "document_id": "..." }` (a PVC upload), `{ "image_template": "..." }` (image library) and
`{ "base64": "..." }` work the same way, and so do plain strings: `"images": { "pic:14": "lc:abc-attachment-id" }`
(also `doc:<document_id>`, `img:<name>` or a `data:image/…` URI). The picture inherits its position and
size from the layout and is cropped to the slot's aspect ratio (`cover`). To show the whole image
instead, use the object form with `"fit": "contain"` (a frame in the image's ratio, centred in the
slot); `"stretch"` only on request. An unresolvable `lc:`/`doc:`/`img:` reference aborts the call and
the error names it.

**Charts** go in a per-slide `charts` object, keyed like `fields` (exact slot key such as `chart:15`, or
the bare type; `content`/`chart` take the first free chart, obj or body slot). The chart fills the slot's
frame (from the layout, else the slide master; no frame is an error naming the slot) in the deck's theme
colours (Design → Colors) and fonts. A slot takes a field **or** a chart, not both. Same chart object as
`slides[].chart` above:

```json
{
  "layout": "Diagramm",
  "fields": { "title": "Revenue per quarter" },
  "charts": {
    "chart:15": {
      "type": "bar",
      "labels": ["Q1", "Q2", "Q3"],
      "datasets": [{ "label": "2026", "data": [12, 15, 19] }]
    }
  }
}
```

`charts` works the same in `add_slides_from_layouts` and `set_powerpoint_slide_fields`.

**Slot values** accept three shapes:

| Value                             | Result                                              |
| --------------------------------- | --------------------------------------------------- |
| `"one line"`                      | One paragraph at level 0; `\n` splits into paragraphs |
| `["a", "b"]`                      | One paragraph per item, all at level 0              |
| `[{ "text": "sub", "level": 1 }]` | One paragraph at `level` 0–8                        |

Inline `**bold**`, `*italic*` and `~~strikethrough~~` are formatted; font, size and colour stay the layout's. Links
appear as "text (url)", not clickable.

Omitted slots stay empty and show the layout prompt in PowerPoint.

**Lists come from the template, not from you.** The tool writes no bullet or numbering settings.
Every paragraph takes the marker of its level from the placeholder's list style in the master: a
bullet, a number, or nothing. A string and an array look **the same**. The array only splits the
text into paragraphs; it does not switch bullets on or off. That means:

- **Never type list markers.** No `•`, `-`, `–`, `*`, `1.`, `a)` or `→` at the start of a line. On a
  bulleted level you get `• • text` or `• 1. text`. Write the bare text and let the template mark it.
- **A paragraph cannot switch its bullet off.** In a placeholder whose level 0 is bulleted, every
  level-0 line gets a bullet, including a heading or an intro sentence. Put headings into the
  layout's `title`/`ctrTitle` slot, or into a layout that has a heading slot or a level without a
  marker. Don't write "OPTION A" as the first bullet of a column.
- **Numbered or plain lines need a level or slot that is styled that way.** If the template numbers a
  level, use it; otherwise the list is bulleted, so don't add your own numbers. Agenda items, steps
  and chapter numbers go into slots that are not bulleted. If none fits, write the items without
  numbers.
- **Many corporate masters use level 0 for plain text and level 1 for bullets** (sample text "Edit
  Master text styles / Second level …"). On such a master, write intro text at level 0 and the list
  items with `"level": 1`.

You cannot see from `describe_pptx_template` which level is bulleted. With code execution, read it from
the template (see below). Without code, follow the rules above. After building, read the deck back
with `read_powerpoint_slides`: lines that start with `•`, `-` or a number you typed are a mistake. Tell
the user that bullets come from the template, and ask them to check one content slide.

**If code execution is available**, look up the list style and position of every slot before
you plan. Attach the template (`attach_template_to_chat`, see **en-templates**) and run the
bundled script. It is only there when the skill was installed as a package (zip / sync):

```bash
python3 /mnt/data/skills/en-powerpoint/scripts/pptx_inventory.py "/mnt/data/<template>.pptx" --lists
```

```text
== slideLayout9.xml "Text_Box_OB"
  body:13      at 52%,30%  L0=bullet '•'  L1=bullet '–'  L2=none …
  body:14      at  5%,30%  L0=bullet '•'  L1=bullet '–'  L2=none …
```

`L0=bullet` = level-0 lines get a bullet. `L0=number arabicPeriod` = numbered. `L0=none` = plain
text. A bullet shown as `'§'` or `'n'` is a symbol-font character (a square, a dash, …), still a
bullet. `at x%,y%` is the slot's top-left corner: here `body:14` is the **left** column, although
its number is higher. If the script is missing, follow the rules above without it.

**Base deck options:**

- `drop_template_slides` (default `true`) removes the source deck's own slides. Slide masters,
  layouts, themes and media are **always** kept.
- `drop_template_slides: false` keeps them and appends after them — but the result is saved as a
  **new** document. To grow a deck in place use `add_slides_from_layouts` (step 3).
- Instead of `template_name`, pass `document_id` (a stored `.pptx`) or `librechat_file_id` (an
  attachment) to use that deck as the base. Because layouts survive, a deck built this way can be
  extended later — that is the iterative path for path C.
- `role_map` overrides inference: `{ "content": "slideLayout4.xml" }`.

**Response** reports per slide: `layoutId`, `layoutName`, `filledSlots`, `filledImageSlots`,
`unknownFields`, `emptySlots`. Always check `unknownFields` — a typo'd slot key is reported, not
silently dropped. Picture slots that got no image are listed in `imageSlotsNotFilled` (with a
`note`).

### Step 3 — `add_slides_from_layouts` (grow the deck in place)

The in-place sibling of step 2: same `slides` array, but it targets an existing deck by
`document_id` / `librechat_file_id` and **keeps the same document**. This is how a path-C deck
grows across turns — never re-create the deck to add slides to it.

```json
{
  "document_id": "<id>",
  "slides": [
    { "layout": "Kapiteltrenner", "fields": { "title": "2. Zielbild" } },
    { "layout": "slideLayout11.xml", "fields": { "title": "Roadmap", "body:10": ["Q1", "Q2"] } }
  ]
}
```

- `insert_after: n` places the new slides after slide `n` (`0` = before slide 1). Omit to append.
- Returns `slides_before` / `slides_after` / `slides_added` plus the same per-slide report.
- Refuses a deck whose layouts carry no native placeholders (a Markdown-built deck) and names
  `append_slides_to_powerpoint` instead — nothing is written in that case. It also refuses, without
  writing, when no slot gets filled at all (typically: none of the passed keys matches a slot).

### Step 4 — `set_powerpoint_slide_fields` (patch one slide)

Patches **one** slide in place. Only the slots you pass change; every other slot, shape, image
and the slide's position stay untouched. Slots the layout offers but the slide does not yet carry
are added — including picture slots.

```json
{
  "document_id": "<id>",
  "slide_number": 3,
  "fields": { "title": "Kernbefunde (überarbeitet)", "body:10": ["Neuer Punkt 1", "Neuer Punkt 2"] },
  "images": { "pic:14": { "librechat_file_id": "abc-attachment-id" } }
}
```

Either `fields` or `images` is enough — pass both only when you mean to change both. This is the
tool to call repeatedly across turns while the user reviews the deck. Accepts `librechat_file_id`
too (the attachment is updated on the shared volume when available).

### How a `layout` reference resolves

A slide's `layout` is matched in this order: a `layoutId` → a role (an explicit `role_map` entry
overrides the inferred `roleMap`) → a layout name. `{{slide_type:x}}` markers play no part here;
they only route `repeat` records in `create_powerpoint_from_template` (see **en-templates**).
**Never ask the user to type `{{}}` markers into a corporate master** — that is exactly what
path C removes.

---

## 4a. Path D — design deck with sample text on its example slides

Many corporate templates are not built the way PowerPoint intends. The designers placed the
content areas as **plain text boxes on example slides** (title slide, agenda, chapter divider,
content slide, closing slide) and filled them with sample text: "Text", "XXX", "TITEL",
"UNTERTITEL", "Text 1 … Text 4", "01 XXX". The layouts behind those slides carry only background,
logo, footer and slide number. That is why the layout tools of path C find nothing to fill.

The way to use such a deck is the way a person would: **duplicate the right example slide, type
over its text boxes, delete the example slides you did not use.** companyFILES has no tool for
editing plain text boxes, so this path needs code execution.

**Plan first, the same way as in §1:** for every slide of the new deck, name the example slide
it copies ("slide 5 = content slide with three bullets") and the text for each of its boxes. One
example slide can be used as often as needed; example slides that are not needed are dropped.
Keep the text roughly as long as the sample. The boxes have a fixed size, and nobody can see the
slide before the user opens it.

### If code execution is available

The deck the user attached is in the sandbox at `/mnt/data/<filename>.pptx` (a companyFILES
template: `attach_template_to_chat` first, see **en-templates**). This skill ships two scripts,
under `/mnt/data/skills/en-powerpoint/scripts/` when it was installed as a package:

1. **Inventory**: list every shape with its id and paragraphs:

   ```bash
   python3 /mnt/data/skills/en-powerpoint/scripts/pptx_inventory.py "/mnt/data/<deck>.pptx"
   ```

   Each line reads `id=<shape id> <kind> "<name>"  [0] 'paragraph 0'  [1] 'paragraph 1' …`.
   `box` = plain text box (path D content), `ph:*` = a real placeholder, `tbl` = table (cells as
   `r<row>c<col>`), `in=<id>` = inside a group. `!DUMMY` marks sample text. Big decks: add
   `--slides 1-10` (the output of one call is limited to about 64 KB).
   - `fit≈22ch×3 lines` = roughly how much text the box holds as designed. The coloured tile or
     rounded box behind a text box is sized for its sample text. Plan your texts within this
     limit: a heading of 6 characters needs a short replacement, not a sentence.
   - `<r>` inside a paragraph marks a change of formatting, e.g. `'01 <r>TITEL'` = bold number +
     normal title. Keep the `<r>` in your text (`"02 <r>PORTFOLIO"`) so both formats stay.

2. **Fill**: write a plan and build the deck in one call:

   ```bash
   cat > /tmp/plan.json <<'EOF'
   {"slides": [
     {"from": 1, "texts": {"8": "Annual Report 2026", "18": "Berlin, 28 October 2026"}, "notes": "Welcome"},
     {"from": 2, "texts": {"3": ["Market", "Products", "Team", "Outlook"]}},
     {"from": 5, "texts": {"4": ["Strength one", "Strength two", "Strength three"], "6": "01 COMPANY"}},
     {"from": 5, "texts": {"4": ["Second slide", "in the same design"], "6": "02 PRODUCTS"}},
     {"from": 8, "replace": {"Musterfirma": "Acme Corp"}}
   ]}
   EOF
   python3 /mnt/data/skills/en-powerpoint/scripts/pptx_fill.py "/mnt/data/<deck>.pptx" /tmp/plan.json "/mnt/data/<result>.pptx"
   ```

   - `from` = example slide number, `texts` = shape id → new text. Shape ids stay the same on
     every copy of an example slide.
   - A text is a string (`\n` = new paragraph, `<br>` = line break), a list of paragraphs (one per
     bullet; `null` keeps a paragraph), or `{"<paragraph index>": "text"}` to change single lines
     of a box (a box with `'XXX'  ''  'XXX'` = heading, spacer, description).
   - Also available: `tables` (shape id → rows × cells), `images` (shape id → `/mnt/data/<image>`,
     swaps a picture and keeps its frame), `delete` (shape ids, e.g. an "ABBILDUNG" box you have no
     picture for), `replace` (substring on the whole slide), `notes`.
   - Write the plan to `/tmp` in the **same** call. Files in `/mnt/data` become chat attachments,
     and `/tmp` is emptied after every call.
   - The script keeps each paragraph's formatting (font, size, colour, bullet), copies charts and
     images with the slide, and refuses to overwrite the source.

3. **Check**: the fill script ends with a check and exits with code 2 if sample text is left
   (`CHECK FAILED` with slide, shape id and text). Fix the plan and run it again. A
   `FIT WARNING` means a text is too long for its box or the shape behind it and will spill over
   the design: shorten exactly those texts and run again until no warning is left. You can also check
   on its own: `pptx_inventory.py "/mnt/data/<result>.pptx" --check`. Run the inventory on the
   result once more and compare it with your plan before you answer.

4. **Answer**: the result comes back as a chat attachment. Say which example slide each slide
   came from, and that you could only check the text, not the look. Ask the user to look for text
   that is too long for its box.

**Do not write your own fill code when the scripts are there.** Check first:
`ls /mnt/data/skills/en-powerpoint/scripts/`. Code that writes all text into the largest shape,
or that calls `text_frame.clear()` / sets `paragraph.text`, wipes the template's fonts and bullets,
covers pictures with text and leaves the sample text in the other boxes.

**Without the scripts** (the skill was pasted as a single `SKILL.md`): do the same steps with
python-pptx yourself (`import pptx` first; if it fails, see "without code execution").

- Walk all shapes, including groups (`shape.shapes`) and table cells.
- Replace text **per paragraph**: put the text into the paragraph's first run, empty the other runs,
  and remove or copy whole paragraphs. Setting `shape.text` or `text_frame.text` wipes the
  formatting.
- To duplicate a slide, add a slide with the same layout, copy the source slide's `spTree`
  children, and copy its relationships (images, charts) with new relationship ids.
- Remove unused slides from `prs.slides._sldIdLst` and drop their relationship.
- Search the result for leftover sample text before you answer.

**Limits of the sandbox:**

- The sandbox has no LibreOffice, so nothing renders a slide to an image for a look.
- Each call stops after about 15 seconds. The scripts need about one second, even for large decks.
- A single file can be at most about 25 MB.

### Without code execution

There is no tool route that fills these text boxes. Do **not** build layout slides that come out
empty, and do not switch to `create_powerpoint` and call it the template. Tell the user plainly:

- The template keeps its content areas as plain text boxes on example slides. companyGPT can only
  fill these with code execution. They can turn code execution on for the chat or agent, or ask an
  admin for the `RUN_CODE` permission.
- Alternatively, the slide master can be rebuilt once with real placeholders in its layouts
  (PowerPoint: View → Slide Master → Insert Placeholder). After that, path C works without code.
- Offer what does work right now: the slide texts as a structured outline to paste into the
  template, or a deck in the companyFILES design (path A), clearly labelled as **not** the
  corporate template.

---

## 5. Iterative editing of any deck

All three tools below target the deck with `document_id` **or** `librechat_file_id` (a LibreChat
attachment, updated in place on the shared volume when it is mounted).

### `append_slides_to_powerpoint`

Two mutually exclusive modes.

**(1) Generate** — `markdown` or `slides`, same schema as `create_powerpoint`:

```json
{
  "document_id": "<id>",
  "slides": [
    { "type": "section", "title": "Part 2: Deep Dive" },
    { "type": "default", "title": "Technical Details", "bullets": ["Detail A", "Detail B"] }
  ]
}
```

**(2) Clone-and-refill** — `reference_slide` copies an **existing slide of this same deck**
(its design, layout, fonts, background) and refills its `{{placeholders}}`. This is how a
`{{}}`-template deck is extended so the new slide looks identical to the template:

```json
{
  "document_id": "<id>",
  "reference_slide": 4,
  "placeholders": { "region": "APAC", "revenue": "€0.9M" },
  "notes": "APAC is the newest market — numbers are 2 quarters old."
}
```

`reference_slide` cannot be combined with `markdown`/`slides`. In clone mode use the top-level
`notes` field; in generate mode use `slides[].notes`.

Clone-mode limits:

- Structured fields (`bullets`, `code`, `table`) are **not** rendered — the cloned slide only has
  the shapes the template defines. Feed content in through `{{placeholders}}`.
- Only `{{text placeholders}}` are refilled; image (`{%name}`) refill is not supported here — use
  `create_powerpoint_from_template` for that.

### `update_powerpoint_slide`

Replaces one slide, keeping its position and the total slide count. Same two modes:

```json
{
  "document_id": "<id>",
  "slide_number": 3,
  "slides": [{ "type": "section", "title": "Chapter 2", "subtitle": "The Deep Dive" }]
}
```

```json
{ "document_id": "<id>", "slide_number": 3, "reference_slide": 4, "placeholders": { "region": "EMEA" } }
```

Or quick text-only: `{ "document_id": "<id>", "slide_number": 2, "markdown": "## New Title\n\n- Bullet" }`
(`##` sets the title, `???` adds notes).

When `reference_slide` equals `slide_number`, the slide is refilled in place — the way to fix a
slide that still shows raw `{{placeholders}}`.

### `read_powerpoint_slides`

```json
{ "document_id": "<id>" }
```

Returns `{ slide_count, hasLegacyPlaceholders, layoutsAvailable, slides: [...] }`, each slide with
`{ slideNumber, title, textLines, layoutId, layoutName, role, slots, emptySlots }`. Use it before
editing a deck you did not just build, and after several appends to confirm numbering.

`slideNumber` is the position **PowerPoint shows** (`sldIdLst` order), not an internal file
number — so it is the number to pass to `set_powerpoint_slide_fields` / `update_powerpoint_slide`
even on a deck whose slides were reordered before it reached us.

The layout fields are what make an unfamiliar deck editable: `layoutId` feeds
`add_slides_from_layouts`, `slots` shows what each slide currently says, and `emptySlots` lists
the keys still free. Pass `include_layouts: false` for a text-only read of a very large deck
(`slideNumber`, `title`, `textLines` only).

---

## 6. Charts and images in slides

- **Chart as its own slide:** `embed_chart_in_document` with `document_type: "powerpoint"` renders
  the chart onto its own slide; with `title` set, a generated title slide comes first, so the deck
  has **two** slides. The result is a deck — keep appending to it with
  `append_slides_to_powerpoint`. Its `id` is a `.pptx`, **not an image**: passed as `doc:<id>` or
  as an image `document_id` it is rejected as "not an image".
- **Chart on a content slide:** use the native chart — `slides[].chart` (generated decks, §3) or
  `charts` per slot (corporate decks, path C). It stays editable in PowerPoint. Only if a picture is
  wanted (or the deck is a `{{}}` template, where `charts` just renames series), reference a stored
  chart image as `![chart](doc:<id>)` in Markdown, through a `{%name}` image placeholder in a `{{}}`
  template, or through a layout picture slot (`images`, path C).
- **Image library:** the organisation's (and the user's own) stock photos, key visuals and icons.
  Find them with `list_image_templates` (`search`, `tag`, `orientation`, `aspect_ratio` sorts by
  closeness, `limit`); each result has `ref` (`"img:<name>"`), description, tags and `aspectRatio`.
  Pass `aspect_ratio` of the target area (a slot's `aspectRatio` from `describe_pptx_template`, 16:9 =
  1.78) so little is cropped; look at a candidate with `view_image { "image_template": "<name>" }`.
  An unknown `img:` name fails the call with an error that names it.
- **Image sources** differ by tool:
  - `create_powerpoint` Markdown: `doc:<documentId>` (stored image), `lc:<file_id>` (LibreChat
    attachment — see `list_my_files`), `img:<name>` (image library), a base64 data URI or a public
    http(s) URL.
  - `image` fields in `slides[]`, and Markdown in `append_slides_to_powerpoint` /
    `update_powerpoint_slide`: `lc:<file_id>`, `doc:<document_id>`, `img:<name>`, a base64 data URI
    (`data:image/…`) or a public http(s) URL. Prefer `lc:`/`doc:`/`img:` over base64. In
    `slides[].image` an unresolvable reference is an error that names it; in Markdown the slide falls
    back to the alt text.
  - http(s) images must come from a **publicly reachable** host; internal or private addresses
    are refused.
  - `{%name}` template images and layout picture slots (`images`) take
    `{ base64 | document_id | librechat_file_id | image_template }`; layout `images` also take the
    strings `lc:…`, `doc:…`, `img:…` or `data:image/…`.
- **Images are never distorted** unless asked for (`stretch`):

  | Where                         | Default                                         | Option                        |
  | ----------------------------- | ----------------------------------------------- | ----------------------------- |
  | `slides[].image`              | `contain`: whole image, centred in its area     | `imageFit: "cover"` crops     |
  | Layout picture slots          | `cover`: fills the slot, centre crop            | `{ …, "fit": "contain" }`     |
  | `{%name}` template pictures   | `cover`; `contain` for names containing "logo"  | `fit` per image               |

- See **en-charts-diagram** for chart/diagram creation, **en-templates** for `{%image}`
  placeholders, `charts` (renames series only — the template's chart data stays) and `repeat`.

---

## 7. Gotchas

- **Never fall back to path A when a corporate master was requested.** If a layout call is
  rejected, fix the call — do not switch to `create_powerpoint`. Its output uses the built-in
  design, so the one thing that was asked for (the corporate master) is exactly what is lost, and
  a deck named after the master that does not use it reads as success when it is a failure. If you
  cannot get the call through, say so and stop; do not ship a substitute silently.
- **Pass `slides`, `fields` and `role_map` as real JSON, not as a string.** A serialised
  `"[{\"layout\":…}]"` is tolerated by the server, but only as a safety net — send structured
  arguments. A schema rejection means the _shape_ is wrong: re-read this file's example rather than
  retrying the same payload.
- **`slides` beats `markdown`** when both are passed to the same call.
- **`title` on `create_powerpoint` prepends an extra generated title slide** — it shifts every
  `slide_number`. Omit it to author slide 1 yourself.
- **`reference_slide` + `markdown`/`slides` is an error.** Pick one mode.
- **`slide_number` is 1-based**; out of range is an error that reports the real slide count.
- **A layout without text slots is not a blank slide to fill.** If `describe_pptx_template` lists
  no `title`/`body` slots for the layouts you need, a layout slide stays empty: background, logo
  and footer only. That is path D (§4a), not a call to retry with other field names.
- **"Done" means read back and free of sample text.** A deck that still shows "Text", "XXX" or
  "TITEL", or has empty content slides, must not be reported as finished. Claiming it is done
  and the user finding the sample text themselves is the worst outcome.
- **`unknownFields` / `emptySlots`** in a layout response are the signal that a slot key was
  wrong — re-read `describe_pptx_template` rather than guessing. Common synonyms are accepted
  (`title` for a `ctrTitle` placeholder, `subtitle` for `subTitle`, `content`/`bullets` for
  `body`), but exact slot keys are always safest.
- **Typed list markers double up.** `"• Point"` or `"1. Point"` in a layout slot shows as `• • Point`
  or `• 1. Point`, because the template's list style adds its own marker. Bullets and numbers
  come only from the template (see "Lists come from the template").
- **A synonym fills one slot, not all matching ones.** On a layout with two body placeholders
  (`body:12`, `body:13`) a single `bullets` fills the **first free** one and reports the other in
  `emptySlots` — it is not duplicated into both. To fill both columns, address them by exact key.
  Exact keys win over synonyms, so `{ "body:13": "right", "content": "left" }` fills both correctly.
- **`subtitle` on a master with no `subTitle` placeholder** (common on corporate masters: the
  subtitle line of a title layout is a plain `body` placeholder) falls back to the first free
  `body` slot instead of landing in `unknownFields`.
- **`create_powerpoint_from_template` refuses a template with no `{{}}` placeholders** — when
  `images`, `charts` and `speaker_notes` are also absent — and names the layout tools in the error.
  That is path C's cue, not a broken template — do not retry the legacy tool and do not add `{{}}`
  markers to a corporate master.
- **`pic:*` slots take images via `images`, not `fields`.** A `pic` key inside `fields` fills
  nothing — the slot stays empty.
- **Only `add_slides_from_layouts` keeps the document id** when extending a path-C deck.
  `create_powerpoint_from_layouts` with `drop_template_slides: false` produces a _new_ document —
  useful when the user wants a copy, wrong when they asked to extend what they have.
- **`append_slides_to_powerpoint` on a corporate deck gives you companyFILES-styled slides.** Its
  generated slides carry their own design and are remapped onto the deck's first layout, so on a
  design deck they look off. The response says so in `designNote`; use `add_slides_from_layouts`.
- **Layout names are not unique.** Ambiguous name references resolve to the first match and log a
  warning; use `layoutId`.
- **`list_templates` does not include the layout catalog.** `describe_pptx_template` does.
- **Do not write formatting in path C.** Passing colours/fonts is neither possible nor wanted —
  the master owns the design.
- **Downloads:** every create call, and every append/update/patch call on a companyFILES
  document, returns `{ id, filename, downloadUrl, markdownLink }` (plus `librechat_file_id` when the
  deck is also stored as a chat file). Always render `markdownLink` in the reply. On a chat
  attachment updated in place, the response carries `librechat_file_id`, `filename` and `message`
  but **no** download link — tell the user the attached deck was updated. If the attachment could
  not be updated in place, a new document with its own `id` and `markdownLink` is returned.
- **Theming (path A):** `create_powerpoint` applies the CI from the settings automatically: colours,
  theme fonts, link colour, the company name in the file properties and – on content slides – footer
  text, slide number and the logo (when "logo in documents" is on, at the slide edge of the configured
  logo position; title and section slides stay without). No theme arguments needed.
- **Path B (templates):** only `{{company_name}}` is auto-filled (from the company name in settings);
  a logo needs a `{%logo}` image placeholder and an explicit `images` entry. Path C writes no
  formatting; the template defines the look.

---

## 8. End-to-end test drive

A single run that exercises every slide feature. Useful for verifying a deployment.

**Path A — scratch deck, built iteratively**

1. `create_powerpoint` — no `title` argument, 3 slides: `section`, `default` (bullets +
   `htmlTable` with coloured cells), `text-image` **without** `image` → expect a skeleton box.
   → 3 slides, note `document_id`. (Repeat once **with** `title` to confirm the generated title
   slide appears and shifts numbering to 4.)
2. `append_slides_to_powerpoint` — `slides`: a `default` with a `code` block and a `table`, plus
   a `text-image` **with** `image` set to a base64 data URI. → same `document_id`, 5 slides.
3. `append_slides_to_powerpoint` — `markdown` with two `##` headings and a `???` notes block.
   → 7 slides, notes visible in the presenter view.
4. `update_powerpoint_slide` — `slide_number: 2`, a single-element `slides` array of type
   `section`. → still 7 slides, slide 2 is now a divider.
5. `read_powerpoint_slides` → `slide_count: 7`, titles in the expected order.

**Path C — corporate master, built iteratively**

6. Upload the master as a `potx` template → log line
   `Auto-extracted N slide layout(s) from PPTX template …`, `placeholders` empty.
7. `describe_pptx_template` → `hasLegacyPlaceholders: false`, layouts with `layoutId`, `name`,
   `masterId`, `role`, slot keys including at least one `body:idx` pair and one `pic:*`.
8. `create_powerpoint_from_layouts` — 5 slides addressed by **role**, **name** and **layoutId**
   mixed; include multi-level bullets, a two-column layout filling `body:12` + `body:13`, a `\n`
   inside a value, and `notes` on slide 1.
   → open in PowerPoint: corporate fonts/colours/logos, real master bullets, and **"Reset
   layout" changes nothing**.
9. `set_powerpoint_slide_fields` — patch only the `title` of slide 2 → same `document_id`, same
   slide count, other slots untouched.
10. `add_slides_from_layouts` with that `document_id` → **same** `document_id`, 6 slides, the new
    one in the same corporate design. Repeat with `insert_after: 1` → the slide lands at
    position 2.
11. `set_powerpoint_slide_fields` with `images: { "pic:14": { "librechat_file_id": "<png>" } }` on
    a title-image slide → the picture fills the placeholder frame, cropped not stretched, and
    the response's `slide.filledImageSlots` lists `pic:14`.

**A deck attached in the chat (§2a)**

12. Attach a `.pptx` to a chat message → `list_my_files` shows it with a `file_id`.
13. `describe_pptx_template { "librechat_file_id": "<file_id>" }` → the same catalog as step 7,
    without any template upload.
14. `read_powerpoint_slides { "librechat_file_id": "<file_id>" }` → slides in the order
    PowerPoint shows them, each with `layoutId` and `slots`.
15. `add_slides_from_layouts` against that `file_id` → the response's `message` says the attachment
    was updated in place (same `file_id`, `librechat_file_id` in the response) or that the modified
    copy was saved as a new document (new `id` and `markdownLink`).

**Path D — design deck with sample text (code execution)**

16. Attach a deck whose content slides are plain text boxes ("Text", "XXX") →
    `describe_pptx_template` shows layouts without text slots, `read_powerpoint_slides` shows the
    sample text.
17. `pptx_inventory.py` on `/mnt/data/<deck>.pptx` → lines with `box` and `!DUMMY`.
18. `pptx_fill.py` with a plan that uses one example slide twice, a list of bullets, a
    `{"0": …, "2": …}` paragraph map and a `delete` → `saved … N slides`, `CHECK OK`, and the
    result arrives as a chat attachment; in PowerPoint the copies look like the example slide.
19. The same plan with one shape id left out → `CHECK FAILED` naming that slide and shape, exit code 2.

**Error paths**

20. `"layout": "GibtsNicht"` → error listing all layouts **and** roles.
21. `fields: { "untertitel": "x" }` on a layout without that slot → `unknownFields: ["untertitel"]`.
22. `slide_number: 99` on `set_powerpoint_slide_fields` → error naming the real slide count.
23. `reference_slide` together with `slides` → error.
24. A deck **with** `{{}}` markup through `describe_pptx_template` →
    `hasLegacyPlaceholders: true` → switch to `create_powerpoint_from_template`.
25. `add_slides_from_layouts` on a deck built by `create_powerpoint` → error naming
    `append_slides_to_powerpoint`, and the deck's slide count is unchanged.
26. `add_slides_from_layouts` with `insert_after` beyond the slide count → error naming the real
    count.
27. `pptx_inventory.py <corporate master> --lists` → one line per text slot with `at x%,y%` and
    `L0`…`L4`; a slot whose master level 0 is bulleted shows `L0=bullet`. Fill it with
    `["Point A", "Point B"]` (no typed `•`) → PowerPoint shows exactly one bullet per line.

`MANUAL_TESTS.md` §4.6 (corporate master) and §4.9 (deck attached in the chat) hold these
scenarios as ready-to-run cURL commands.
