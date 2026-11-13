---
name: en-charts-diagram
description: 'Create interactive charts, diagrams and maps with companyFILES MCP tools. Use when asked to visualize data, create a bar/line/pie/scatter/bubble chart, draw a flowchart, sequence diagram, ER diagram, Gantt chart, or any Mermaid diagram, or show locations as pins on a map. Also covers embedding charts or diagrams into Word, PDF, or PowerPoint documents.'
---

# Charts & Diagrams Skill

Tools for creating interactive charts (Chart.js), diagrams (Mermaid) and maps, plus embedding charts in documents.

## Tools in This Skill

| Tool                       | Purpose                                                                      |
| -------------------------- | ---------------------------------------------------------------------------- |
| `show_interactive_chart`   | **PREFERRED** — Interactive Chart.js widget (zoom, pan, type switch, export) |
| `show_interactive_diagram` | **PREFERRED** — Interactive Mermaid diagram widget (pan, zoom, export)       |
| `show_interactive_map`     | Interactive map widget with pins, clustering and legend (export PNG/JPG)     |
| `create_chart_document`    | Embed a chart image in a Word, PDF, or PowerPoint document                   |
| `embed_chart_in_document`  | Render a Chart.js chart and embed it in a document                           |

## Decision Guide

```
User wants to SEE a chart in chat            → show_interactive_chart   (ALWAYS preferred)
User wants to SEE a diagram in chat          → show_interactive_diagram  (ALWAYS preferred)
User wants to SEE locations on a map         → show_interactive_map

User wants a chart in a PowerPoint deck      → native chart: slides[].chart / charts (en-powerpoint)
                                               editable in PowerPoint, not a picture
User wants to SAVE a chart as Word/PDF...
  Chart + optional description text          → create_chart_document
  Chart embedded in a doc (more control)     → embed_chart_in_document

User wants to SAVE a diagram as a document   → see en-word-odt or en-pdf
  (render diagram first, then embed manually, or describe in Markdown)
```

## Tool Usage

### show_interactive_chart (PREFERRED for charts)

Supported chart types: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`, `waterfall`, `funnel`, `area`, `stackedBar`, `horizontalBar`

```json
{
  "chart_type": "bar",
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "datasets": [
    { "label": "Revenue", "data": [100, 150, 120, 180] },
    { "label": "Costs", "data": [80, 110, 90, 140] }
  ],
  "title": "Quarterly Performance",
  "x_axis_label": "Quarter",
  "y_axis_label": "EUR"
}
```

Optional: `x_axis_label`, `y_axis_label`, and `options` (a raw Chart.js options object merged over the defaults). Datasets also accept `borderWidth` and `fill`.

**Scatter chart** (use `{x, y}` data points):

```json
{
  "chart_type": "scatter",
  "labels": [],
  "datasets": [
    {
      "label": "Points",
      "data": [
        { "x": 1, "y": 2 },
        { "x": 3, "y": 4 }
      ]
    }
  ]
}
```

**Bubble chart** (add `r` for radius):

```json
{
  "chart_type": "bubble",
  "labels": [],
  "datasets": [
    {
      "label": "Bubbles",
      "data": [
        { "x": 1, "y": 2, "r": 10 },
        { "x": 3, "y": 4, "r": 5 }
      ]
    }
  ]
}
```

The widget includes: zoom/pan, chart type switcher, and an export menu with PNG (1x/2x/4x), Copy CSV and Copy Image.

---

### show_interactive_diagram (PREFERRED for diagrams)

Supported diagram types (Mermaid syntax): flowchart, sequence, class, state, ER, Gantt, pie, mindmap, timeline, and more.

```json
{
  "code": "graph TD\n  A[Start] --> B{Decision}\n  B -->|Yes| C[Do this]\n  B -->|No| D[Do that]\n  C --> E[End]\n  D --> E",
  "title": "Decision Flow",
  "theme": "default"
}
```

The Mermaid source goes in the **`code`** parameter (not `mermaid_code`).

**Themes:** `default`, `dark`, `forest`, `neutral`

The widget includes: pan/zoom, a theme switcher, and export as SVG, PNG (2x) or JPG. After an export, "Copy link" copies the download link of the exported file.

---

### show_interactive_map

Interactive map (OpenStreetMap tiles) with pins. `map_type`: `world` (free pan/zoom) or `germany` (with an overlay of the German state borders).

```json
{
  "map_type": "germany",
  "title": "Sites",
  "pins": [
    { "lat": 48.137, "lng": 11.575, "label": "Munich", "category": "own" },
    { "lat": 52.52, "lng": 13.405, "label": "Berlin", "category": "partner", "details": { "Employees": 42 } }
  ],
  "legend": [
    { "category": "own", "color": "#2563EB", "label": "Own sites" },
    { "category": "partner", "color": "#F59E0B", "label": "Partners" }
  ]
}
```

Each pin needs `lat` + `lng` and a `label`; optional `tooltip` (hover text), `category` (pin color via `legend`), `color` (explicit hex color) and `details` (key-value pairs shown in the click popup). Up to 5,000 pins. Nearby pins are clustered by default (`cluster: false` turns this off). Optional: `center` (`{ "lat": …, "lng": … }`), `zoom` (1–20), `show_state_borders`.

Only where Azure Maps is configured for the environment: `address` instead of `lat`/`lng` (geocoded), `route` (`waypoints`, `travel_mode`: `car`, `pedestrian`, `bicycle`), `distance_matrix_from`, `isochrone` and `reverse_geocode`. Without Azure Maps these options make the call fail — do not use them unless you know they are available.

The response is the map widget plus a text line `Interactive map: [title](url) — open the link for PNG/JPG export.`

---

### create_chart_document

Renders a chart image and embeds it in a document with an optional description below.

Supports extended chart types: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`, `waterfall`, `funnel`, `area`, `stackedBar`, `horizontalBar`

```json
{
  "chart_type": "line",
  "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
  "datasets": [{ "label": "Sales", "data": [50, 70, 65, 90, 110] }],
  "title": "Monthly Sales Trend",
  "description": "Sales grew steadily throughout Q1 and Q2.",
  "output_format": "word",
  "filename": "sales_trend"
}
```

`output_format` options: `word` (default), `pdf`, `powerpoint`

---

### embed_chart_in_document

More control over chart dimensions when embedding.

Supported types: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`

```json
{
  "chart_type": "bar",
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "datasets": [{ "label": "Revenue", "data": [100, 150, 120, 180] }],
  "document_type": "pdf",
  "title": "Quarterly Revenue",
  "width": 1400,
  "height": 900,
  "filename": "revenue_chart"
}
```

`document_type` options: `word`, `powerpoint`, `pdf`

### Chart in a PowerPoint deck: native, not a picture

For `.pptx` use the native, editable chart of the PowerPoint tools instead of `create_chart_document` /
`embed_chart_in_document` (those render a picture). The data is the same as in `show_interactive_chart`
(`labels` + `datasets`), but the key is `type` (not `chart_type`) and the types are `bar`, `horizontalBar`,
`stackedBar`, `line`, `area`, `pie`, `doughnut`, `scatter`, `radar` (no `bubble`/`polarArea`/`waterfall`/`funnel`;
use `create_chart_document` for those). `scatter` takes numeric labels as x values. Generated deck
(`create_powerpoint`, `append_slides_to_powerpoint`, `update_powerpoint_slide`):

```json
{
  "slides": [
    {
      "type": "default",
      "title": "Revenue per quarter",
      "chart": { "type": "bar", "labels": ["Q1", "Q2", "Q3"], "datasets": [{ "label": "2026", "data": [12, 15, 19] }] }
    }
  ]
}
```

Corporate deck (`create_powerpoint_from_layouts`, `add_slides_from_layouts`, `set_powerpoint_slide_fields`): the
same object per slot in `charts`, e.g. `"charts": { "chart:15": { "type": "bar", … } }`; the slot must report
`acceptsChart` in `describe_pptx_template`. Details: en-powerpoint.

## Key Notes

- `show_interactive_chart` and `show_interactive_diagram` return a **widget** (rendered in LibreChat) plus a text line such as `Interactive chart: [Title](viewer-url) · [Download PNG](url)` (`Interactive diagram: …` for diagrams). Pass these on as plain Markdown links — **never** embed the download URL as an image (`![](…)`): it is an authenticated download endpoint, not an image the browser can load. If the PNG fallback could not be rendered, the line only contains the viewer link.
- Document-embedding tools return `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id` when the document is also stored as a chat file) — always render `markdownLink`.
- The org/user color palette is automatically applied to chart colors when configured in settings.
- Google Gemini models cannot render interactive widgets — responses fall back to text/JSON data.
- `create_chart_document` and `embed_chart_in_document` with `powerpoint` produce a picture, not an editable chart. Prefer the native chart for decks.
- `show_interactive_chart` and `create_chart_document` accept all 13 chart types; `area`, `stackedBar`, `horizontalBar` are mapped to their static equivalents when rendering as images. `embed_chart_in_document` only accepts the 8 base types and rejects the extended ones — use `create_chart_document` for those.
