---
name: en-marketing-library
description: 'Find and use the marketing library (images, icons and approved slides) of companyFILES with search_library. Use when a deck, document or PDF needs pictures, icons, a feature or process slide with icons, or a ready-made company slide (references, about us, team, pricing), when the user asks for brand assets, icons or "our slides", or wants to pick icons themselves. Covers search_library, img:/icon:/slide: references, the icon grid (slides[].iconGrid), library slides (librarySlide, insert_library_slides, replace for names), the icon picker (show_icon_picker) and the usage rights (internal only, credit, expired).'
---

# Marketing Library Skill

The organisation's (and the user's own) pictures, icons and approved slides, searchable by meaning and usable in every
document tool. Look here first, before using an external image or drawing something yourself.

## Tool map

| Tool                    | Purpose                                                                         |
| ----------------------- | ------------------------------------------------------------------------------- |
| `search_library`        | Search images, icons and slides by meaning (German or English)                  |
| `list_image_templates`  | List/filter images only (same index, same fields)                               |
| `view_image`            | Look at an image from the library: `{ "image_template": "<name>" }`             |
| `show_icon_picker`      | The user picks icons in a widget; the choice arrives as their next chat message |
| `insert_library_slides` | Put library slides unchanged into a deck or a new deck                          |
| `update_powerpoint_slide` | With `replace`: change a name or date on a slide, keep its design             |

Building the deck or document itself is the job of **en-powerpoint**, **en-word-odt**, **en-pdf**.

## 1. Workflow

1. **Search first.** `search_library` for every picture, icon or slide you need. Prefer the organisation's assets
   over anything external or generated.
2. **Use the `ref` exactly as returned**: `img:<name>`, `icon:<set>/<name>`, `slide:<collection>/<id>`. Never invent
   a ref; a wrong one fails with `unknown_ref` and no document is created.
3. **Check `rights`** of every result you use (section 5) and tell the user what applies.
4. **Build** with the refs (sections 3 and 4), then render the `markdownLink` of the result.
5. If the user wants to **choose icons themselves**, call `show_icon_picker` (section 6) instead of guessing.

## 2. `search_library`

```json
{ "query": "Sicherheit Baustelle", "kind": "icon", "style": "outline", "limit": 10 }
{ "query": "team meeting office", "kind": "image", "aspect_ratio": "16:9", "language": "en" }
{ "query": "references customers", "kind": "slide", "collection": "sales" }
```

| Parameter      | Meaning                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------- |
| `query`        | Free text; all words must match; umlauts folded, word starts match from 3 letters        |
| `kind`         | `image`, `icon` or `slide` (omit = all)                                                  |
| `set`, `style` | Icon set and style (`outline`, `filled`, `duotone`, `other`), icons only                                  |
| `collection`   | Slide collection, slides only                                                            |
| `orientation`  | `landscape`, `portrait`, `square` (images)                                               |
| `aspect_ratio` | Number or `"16:9"` (±10 %, closest first): pass the target area so little gets cropped   |
| `language`     | Language of the returned texts: `de` (default) or `en`; search covers both               |
| `limit`        | Up to 100, default 20                                                                    |

Each result has `ref`, `kind`, `scope` (`org` or `user`), `displayName`, `description`, `tags`, `aspectRatio`,
`orientation`; icons also `set`, `style`, `recolorable`; slides `collection`, `collectionDisplayName`, `index`; and
`rights` (section 5). A personal asset and an organisation asset with the same ref are both listed: the ref resolves
to the personal one, the organisation entry has `shadowed: true`. Hidden and expired assets are never listed.

No hit? Try a synonym or the other language, drop `style`/`set`, then a broader query. Say so if the library has
nothing suitable; do not silently substitute a different source.

## 3. Icons

Reference: `icon:<set>/<name>`, optionally `?color=brand` (the CI primary colour) or `?color=RRGGBB`.

- Works in **every image input** of PowerPoint, Word, PDF and ODT: `slides[].image`, Markdown `![alt](icon:…)`,
  HTML `<img src="icon:…">`, layout `images`, `{%name}` pictures. PowerPoint and Word get a sharp vector with a PNG
  fallback; the alt text comes from the icon.
- **Recolouring only works for one-colour icons** (`recolorable: true`). Multi-colour and raster icons stay as they
  are and the result says so in `notes`.
- **Word templates** (`create_word_from_template`, `{%logo}` / `{IMAGE logo}`) need the object form
  `{ "logo": { "icon": "icon:brand-line/lock", "width": 3 } }`. A bare string fails there.
- PowerPoint layout slots and `{%name}` take `"icon:…"` or `{ "icon": "icon:…", "fit": "contain" }`.

### Icon grid for feature and process slides

`slides[].iconGrid` (in `create_powerpoint`, `append_slides_to_powerpoint`, `update_powerpoint_slide`) lays out 3–6
points evenly under the slide title in the deck design. **`type` is still required** on the slide, use `"default"`.

```json
{
  "type": "default",
  "title": "How we work",
  "iconGrid": {
    "items": [
      { "icon": "icon:brand/search", "title": "Analysis", "text": "We understand goals and starting point." },
      { "icon": "icon:brand/pencil", "title": "Concept", "text": "We design the solution with you." },
      { "icon": "icon:brand/rocket", "title": "Delivery", "text": "We ship in short iterations." }
    ],
    "color": "brand"
  }
}
```

- 3 items → 3 × 1, 4 → 2 × 2, 5 → 3 + 2, 6 → 3 × 2; `columns: 2|3` overrides.
- Fewer than 3 or more than 6 items is an error: split over several slides. `title` one short line, `text` at most
  300 characters.
- Icons only as `icon:<set>/<name>` (no `img:`, `lc:`, `doc:`). `color` (`"brand"` or a hex colour) recolours all
  one-colour icons; an item's own `?color=` wins.
- Other content fields (`bullets`, `image`, …) on that slide are ignored (a warning says so).
- Pick icons of one set and one style so the grid looks uniform.

## 4. Library slides

Approved slides of the company (own master, layout, notes, charts, pictures). **Insert them unchanged**: do not
rebuild them with `create_powerpoint`, that loses the approved design.

| Goal                              | Call                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| New deck from library slides only | `insert_library_slides { "slides": [{ "ref": "slide:sales/257" }, { "ref": "slide:sales/258" }], "filename": "Customer" }` |
| Into an existing deck             | `insert_library_slides { "document_id": "<id>", "slides": [{ "ref": "slide:sales/257", "position": 2 }] }` |
| Into a chat attachment            | `insert_library_slides { "librechat_file_id": "<id>", "slides": [{ "ref": "slide:sales/257" }] }`        |
| Mixed with generated slides       | `create_powerpoint` → `slides: [{ "type": "default", "title": "Agenda", "bullets": [...] }, { "librarySlide": "slide:sales/257" }]` |

- `position` is 1-based in the resulting deck; omitted = appended in the given order.
- `librarySlide` is a field of the slide object and takes no other field. The layout tools (`create_powerpoint_from_layouts`,
  `add_slides_from_layouts`) take the same entries in their `slides` list.
- The result has `slides_before`, `slides_after`, `inserted [{ref, position, title}]` and `notes` (section 5).
- A slow insertion answers "läuft noch" (still running): call again with the **same arguments**, the slides are not
  inserted twice.
- The inserted slide brings its own theme; it does not adopt the target deck's colours. Say so if the decks differ.

### Change a name or date: `replace`

Edit the inserted slide in place, nothing else changes (design, formatting, pictures, charts, notes):

```json
{
  "document_id": "<id>",
  "slide_number": 3,
  "replace": [{ "find": "Customer X", "replace_with": "ACME" }]
}
```

Literal and case-sensitive, every occurrence on the slide, pairs in order, within one paragraph only (not across
paragraphs or line breaks). The result lists `replaced: [{find, count}]`; if no pair matches, the call fails with
`no_match` and writes nothing: read the slide with `read_powerpoint_slides`, then use the exact text. `replace`
cannot be combined with `markdown`, `slides` or `reference_slide`.

Do not "improve" library slide texts beyond that. For larger changes, tell the user the slide is approved content.

## 5. Usage rights: always respect them

Every asset can carry rights. Search results show them as `rights { usable, internalOnly, credit?, expiresAt? }`; the
document tools enforce them.

| Signal                                   | What to do                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- |
| Error `asset_expired` (with the ref)     | The rights have run out. Nothing was written. **Pick another asset** (search again).        |
| `notes`: "…nur intern verwenden" / internal only | Tell the user the asset is for internal documents only; do not use it in external material. |
| `notes`: credit text (`Bildnachweis „© …“`) | Tell the user and **add the credit** to the document (caption, footer or last slide).     |
| `unknown_ref`                            | The ref does not exist (typo, hidden or deleted). Search again, never guess.                |
| `rights.expiresAt` close                 | Mention it when delivering ("licence valid until …").                                       |

`notes` of a result are part of the answer: read them every time, and pass credit and internal-only hints on in your
reply.

## 6. Let the user choose icons: `show_icon_picker`

```json
{ "query": "security", "set": "brand-line", "multiple": true }
```

All arguments are optional; `multiple` defaults to true (false = exactly one icon). The widget only offers usable
icons. The call does **not** return the choice: it arrives as the user's **next chat message**, e.g.
`Selected icons: icon:brand-line/lock, icon:brand-line/shield` (German UI: `Ausgewählte Icons: …`). Stop after calling
the tool, wait for that message, then use the refs unchanged. To pick icons yourself, use `search_library`.

## 7. Gotchas

- `type` stays required on a slide with `iconGrid` (`"default"`).
- Word template pictures: object form `{ "icon": "icon:…" }`, never a bare string.
- A recolour request on a multi-colour icon does nothing; check `recolorable` before promising a colour.
- `kind: "slide"` finds approved slides only; hidden and expired slides never appear.
- External http(s) images are the last resort, only when the library has nothing, and the user should know.
