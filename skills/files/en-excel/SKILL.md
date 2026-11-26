---
name: en-excel
description: 'Create, read, and modify Excel (.xlsx) spreadsheets with companyFILES MCP tools. Use when asked to create a spreadsheet, export data to Excel, build an analysis, comparison, cost calculation or management summary as Excel, read or parse an Excel file, edit cells, add sheets, apply formulas, number formats, conditional formatting, charts or auto-filters. Covers report-quality workbooks (title, assumptions sheet, totals, charts, print setup), CSV-to-Excel, JSON-to-Excel, 2D array input, in-place modification, and analysing attached spreadsheets.'
---

# Excel Skill

Tools for creating, reading, and modifying Excel (.xlsx) spreadsheets via companyFILES.

> **Office add-in:** if `excel_*` tools are in your tool list, the chat runs inside Excel and a document is open there. When the user means the open workbook, work in it with those tools instead of this skill. This skill is for new files to download (see en-file-routing).

## Tools in This Skill

| Tool                     | Purpose                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ |
| `create_excel_from_csv`  | Create Excel from CSV text                                                     |
| `create_excel`           | Create Excel from a 2D array                                                   |
| `create_excel_from_json` | Create Excel from JSON (array of objects)                                      |
| `create_excel_advanced`  | Report workbooks: title, multiple sheets, formulas, formats, charts, print setup |
| `modify_excel`           | Edit an existing Excel file in place (values, formats, merges, sheet options)  |
| `read_excel`             | Read Excel to JSON (values only)                                               |
| `read_excel_detailed`    | Read Excel with formulas, comments, hyperlinks, named ranges, and metadata     |

## Decision Guide

```
User wants to create Excel from...
  CSV text            → create_excel_from_csv
  JSON array          → create_excel_from_json
  2D array / table    → create_excel
  Analysis, comparison, calculation, management summary, anything people read or print
                      → create_excel_advanced with "preset": "report" + title + chart  (see design rules)
  Complex workbook    → create_excel_advanced  (formulas, multiple sheets, formatting, charts)

User wants to edit an existing Excel file → modify_excel  (requires document_id or librechat_file_id)

User wants to read / parse Excel content...
  Just values         → read_excel
  Formulas & metadata → read_excel_detailed
  .xls / .xlsb / .ods → read_file  (en-file-management, if available)

User wants calculations / pivots / statistics on an attached sheet
                      → code execution if available, else read_excel + step-by-step (see "Optional" below)
```

## Attached Spreadsheets

A spreadsheet the user attached appears in the `Attached files in this message:` block (`- file_id: …, filename: …`). Pass that `file_id` as `librechat_file_id` to `read_excel`, `read_excel_detailed` or `modify_excel`; use `list_my_files` only if there is no such block. Never guess an ID. For other file tasks and apps, see the **en-file-routing**.

## Design Rules for Report Workbooks

Apply these to every workbook people read, print or pass on (analyses, comparisons, offers, cost calculations,
management summaries). A plain data export (`create_excel_from_csv` / `_json`) does not need them.

**What comes first:**

1. **Follow the user's instructions to the letter:** sheet names, column headers, order and formulas exactly as they
   give them. A nicer layout that calculates something else misses the task.
2. **Existing file: its own style wins** over every rule here. Find the input cells first (they usually stand out by
   their own font colour or fill), write only there and leave existing formulas unchanged.
3. **Only as much structure as the content needs.** A simple list gets a title, number formats and totals, but no
   assumptions sheet. The full structure below is meant for multi-part analyses.

**Structure and calculation:**

- **Sheet order** (for multi-part analyses): overview/management summary → detail sheets → comparison / pros and cons →
  findings and next steps → assumptions and sources. Leave out what doesn't exist.
- **Title area:** every report sheet gets `title` and a `subtitle` with scope, date and basis ("As of 25 Nov 2026 ·
  all prices net"). Never put the title into a header cell or an all-caps "section" row.
- **Calculate, don't type:** every parameter sits in its own labelled cell, for analyses on an **assumptions sheet**
  with a source column. Formulas reference it absolutely (`Assumptions!$B$4`, never `B5*1.05`); the overview links to
  the detail sheets (`Sites!G21`). **Never type in a computed result.** Totals are `SUM` formulas.
- **Same formula across the whole row:** periods and sites all follow the same pattern. A single cell that deviates in
  the middle of a row is the most common error nobody notices. Catch denominators that can be 0 (`IFERROR(B5/C5,0)`).
- **Origin of every fixed number:** every number you enter gets a source where the reader sees it (source column, note
  or cell comment). If it came from the user, say so ("provided by the user").
- **Formulas that calculate everywhere:** English function names and comma as separator (`SUM`, `IF`, `IFERROR`).
  Prefer well-established functions such as `SUMIFS`, `INDEX`/`MATCH`, `IFERROR`, `SUMPRODUCT`. **No** `XLOOKUP`,
  `XMATCH`, `FILTER`, `SORT`, `UNIQUE` or `SEQUENCE`: older Excel versions, LibreOffice and previews don't calculate
  them, and spilled results only land in the first cell. Look up with `INDEX`/`MATCH`; sort and filter the data
  beforehand. `TEXTJOIN`, `CONCAT`, `IFS`, `SWITCH`, `MAXIFS` and `MINIFS` only work with the prefix `_xlfn.`
  (`_xlfn.IFS(…)`), otherwise Excel shows `#NAME?`.
- **Sheet names with spaces** are quoted in references: `'Assumptions 2026'!$B$4` (without quotes: `#VALUE!`).

**Formats and look:**

- **Number formats on every numeric cell, formula and total cells included** (otherwise Excel shows `19380` instead of
  `19,380 €`). Put the unit in the header ("Cost (€ net)"):
  - currency `#,##0 "€";-#,##0 "€";"–"` (unit prices `#,##0.00 "€"`)
  - counts `#,##0;-#,##0;"–"`, factor `0.0"x"`, percent `0.0%` stored as a fraction (0.19, not 19)
  - years as text (`"2026"`), otherwise they show up as `2,026` in a number column.
- **Colours come from the CI, everything else stays neutral:** the tools colour the title and header row in the CI
  colours automatically. Don't add signal colours of your own (no blue, yellow, green or red). Formulas, links and text
  keep the normal text colour; totals are bold with a thin top border (`"borders": {"top": "thin"}`). Only input and
  assumption cells get a light fill: `colors.primaryLight` from `get_corporate_ci`, and if the CI provides no colour,
  neutral grey `F2F2F2`. Pros and cons or ratings get no colour; the column header says what is meant.
- **Long text:** comments and pros/cons columns wrap (`wrapText` + `verticalAlignment: "top"`; long strings wrap
  automatically). Column width 30–50; longer text wraps instead of widening the column.
- **Freeze panes:** `preset: "report"` freezes only the rows down to the header, and that is usually enough. Freeze a
  column only if column A is a short row label and the table has more than 8 columns (`"freeze": "B5"`). Never freeze a
  wide text column or more than one column, otherwise there is hardly any room left to scroll.
- **Notes and sources** go under the table (`notes`), never as loose rows in the middle of the data.
- **Chart, required for comparisons:** every comparison, cost calculation, scenario and time series gets one native
  chart (`charts`) on the overview, placed under the table, for the key message (e.g. cost per site and offer). Only
  plain lists, data exports and fill-in templates go without one. Keep it plain: at most 2–3 series, short category
  names, a brief title.
- **Values on the bars (`show_values`) only with few bars** (up to about 8 in total, i.e. series × categories). With
  more, still build the chart, just without `show_values`: the numbers are in the table and the labels would overlap.
  A label shows the value only, without series or category name.
- **Meant to be filled in:** a new workbook that others are to fill in gets a short legend (which cells to fill) and
  one example row with realistic values. A file you were only asked to edit gets no such row.
- **Print:** `preset: "report"` turns gridlines off and prints wide tables landscape on one page width; for narrower
  sheets set `options.orientation` / `fit_to_width` yourself if needed.

**Check before you answer:** all totals are formulas, no currency cell without a format, the assumptions sheet is
referenced, nothing hard-coded, a comparison has its chart. The tools store formulas without a calculated result (Excel calculates on opening), so
you don't see error values. Check 2–3 formulas against the `layout` in the response, if in doubt with
`read_excel_detailed`: does every address point to the right row and column? A formula without errors is not
automatically right; a range shifted by one row calculates the wrong number without any warning.

## Tool Usage

### create_excel_from_csv

```json
{
  "csv_content": "Name,Age\nAlice,30\nBob,25",
  "filename": "people",
  "sheet_name": "Sheet1"
}
```

### create_excel

```json
{
  "data": [
    ["Name", "Age"],
    ["Alice", "30"],
    ["Bob", "25"]
  ],
  "has_headers": true,
  "filename": "people"
}
```

### create_excel_from_json

```json
{
  "json_content": "[{\"name\":\"Alice\",\"age\":30},{\"name\":\"Bob\",\"age\":25}]",
  "filename": "people"
}
```

### create_excel_advanced

Report example with two sheets: an overview that calculates from an assumptions sheet, totals as formulas, currency
formats on every numeric cell (formula and total cells included), a note and a chart. With `title` the table header is
in **row 4** and the data starts in **row 5**: write every formula with these sheet rows.

```json
{
  "sheets": [
    {
      "name": "Overview",
      "preset": "report",
      "title": "Cost comparison of sites",
      "subtitle": "As of 25 Nov 2026 · all prices net",
      "has_headers": true,
      "data": [
        ["Site", "Offer A (€)", "Offer B (€)", "Comment"],
        ["North", { "formula": "Assumptions!$B$2*Assumptions!$B$4" }, { "formula": "Assumptions!$B$2*Assumptions!$B$5" }, "Offer B includes on-site installation and training"],
        ["South", { "formula": "Assumptions!$B$3*Assumptions!$B$4" }, { "formula": "Assumptions!$B$3*Assumptions!$B$5" }, "same scope"],
        ["Total", { "formula": "SUM(B5:B6)" }, { "formula": "SUM(C5:C6)" }, ""]
      ],
      "number_formats": { "B:C": "#,##0 \"€\";-#,##0 \"€\";\"–\"" },
      "cell_styles": {
        "A7:D7": { "bold": true, "borders": { "top": "thin" } }
      },
      "notes": ["Sources: offers of 20 Nov 2026; areas from the floor plan (sheet Assumptions)."],
      "charts": [
        {
          "type": "column",
          "title": "Cost per site",
          "labels_range": "A5:A6",
          "data_ranges": ["B5:B6", "C5:C6"],
          "anchor": "A11",
          "show_values": true
        }
      ]
    },
    {
      "name": "Assumptions",
      "has_headers": true,
      "data": [
        ["Parameter", "Value", "Source"],
        ["Area North (m²)", 1200, "Floor plan"],
        ["Area South (m²)", 800, "Floor plan"],
        ["Price offer A (€/m²)", 12.5, "Offer A, 20 Nov 2026"],
        ["Price offer B (€/m²)", 11.9, "Offer B, 20 Nov 2026"]
      ],
      "number_formats": { "B2:B3": "#,##0;-#,##0;\"–\"", "B4:B5": "#,##0.00 \"€\"" },
      "cell_styles": { "B2:B5": { "backgroundColor": "F2F2F2" } }
    }
  ],
  "filename": "cost_comparison"
}
```

The input cells `B2:B5` have a neutral grey fill here; if `get_corporate_ci` returns `colors.primaryLight`, use that
value (without `#`).

The response contains `layout` per sheet (`headerRow`, `firstDataRow`, `lastDataRow`, `lastColumn`, `notesRows`): use
these rows for follow-up `modify_excel` calls.

**Formula syntax:** Use `{"formula": "SUM(A1:A10)"}` object — no leading `=`.

**Per-sheet options:**

| Option | Effect |
| --- | --- |
| `title`, `subtitle` | Title in row 1 (bold, CI colour), grey subtitle in row 2; data starts at row 4 |
| `has_headers` / `header_row` | First data row is the table header (row 4 with a title); `header_row` = sheet row of the header when `data` has rows above it |
| `preset` | `"report"`: gridlines off, freeze and print titles at the header, landscape and fit to page width above 8 columns. `"data"`: plain table |
| `number_formats` | `{"C5:H14": "…"}` or whole columns `{"C:H": "…"}` (= the data rows incl. totals) |
| `cell_styles` | Styles by range, like in `modify_excel` (fill, font colour, bold, alignment, `wrapText`, `indent`, `border`, `borders` per side) |
| `merge_cells`, `row_heights` | `["A10:D10"]`, `{"5": 58}` (points) |
| `notes` | Notes/sources under the table, each a merged, wrapped grey row |
| `options` | `freeze` ("A5" = rows 1–4 stay visible; "B5" also freezes column A), `show_gridlines`, `orientation`, `fit_to_width`, `print_title_rows` ("4:4"), `tab_color` |
| `charts` | Native Excel charts that read cells: `type` (`column` = vertical, `bar` = horizontal, `stacked_column`, `line`, `area`, `pie`, `doughnut`), `labels_range`, `data_ranges` (same length, also `'Other sheet'!B5:B8`), `anchor` (top-left cell below the table), optional `title`, `series_names`, `show_values`, `width`/`height` in cm |
| `table_style` | `"none"` turns off the default table look (borders, zebra rows, wrapped long text) |
| `column_widths`, `auto_filter`, `protected`, `conditional_formatting` | as before |

Without `column_widths`, columns are sized from the content (max. 60; longer text wraps and the row gets taller). A
formula cell without a number format takes the format of its column when all numbers there share one.

**Conditional formatting types:** `greaterThan`, `lessThan`, `equal`, `between`, `containsText`, `duplicateValues`

**Other options:** top-level `named_ranges` and `properties` (`{title, subject, author, company}`). Individual cells may also be extended objects: `{"value": ..., "comment": ..., "validation": ..., "style": ..., "numberFormat": ...}`. Such an object needs `value` (plus at least one of the other keys); a formula goes **inside** `value`, not next to it: `{"value": {"formula": "SUM(A1:A3)"}, "comment": "Total"}`. A `formula` key beside `value` and `comment` is ignored; an object without `value` (e.g. `{"formula": …, "comment": …}`) is written as a plain formula and its other keys are dropped. For many cells, prefer the range options (`number_formats`, `cell_styles`) over per-cell objects: they cost far fewer tokens.

### modify_excel

Modifies an existing Excel file. Identify the target with `document_id` (updated **in-place** — same ID) **or** `librechat_file_id` (a LibreChat attachment; if the volume isn't writable the modified copy is saved as a **new** document).

```json
{
  "document_id": "<id from upload_file or any create_excel* call>",
  "set_cells": {
    "A1": "Updated Title",
    "Sheet2!B5": { "formula": "SUM(B2:B4)" }
  },
  "append_rows": {
    "Sheet1": [["New Row", 100, 200]]
  },
  "number_formats": { "B2:B100": "#,##0.00" },
  "auto_filter": { "Sheet1": true },
  "add_sheets": [{ "name": "Summary", "data": [["Total", 500]], "has_headers": false }],
  "delete_sheets": ["OldSheet"],
  "rename_sheets": { "OldName": "NewName" }
}
```

**Formatting an existing sheet into the report look** — one call with ranges instead of per-cell objects:

```json
{
  "librechat_file_id": "<file_id of the attachment>",
  "number_formats": { "Costs!C2:H13": "#,##0 \"€\";-#,##0 \"€\";\"–\"" },
  "cell_styles": {
    "Costs!A13:H13": { "bold": true, "borders": { "top": "thin" } },
    "Costs!B2:B12": { "wrapText": true, "verticalAlignment": "top" }
  },
  "merge_cells": ["Costs!A15:H15"],
  "row_heights": { "Costs!15": 45 },
  "sheet_options": { "Costs": { "freeze": "A2", "show_gridlines": false, "orientation": "landscape", "fit_to_width": true } }
}
```

`cell_styles` changes only the given properties; values and the rest of the formatting stay. Existing charts are kept. If the
file already has a style of its own (colours, fonts, input cells), keep it instead of applying the report look.

### read_excel

```json
{
  "file_content": "<base64-encoded xlsx>",
  "include_headers": true,
  "sheet_name": "Sheet1"
}
```

Accepts any one of `file_content` (base64), `librechat_file_id`, or `document_id` (most common — reading a previously created/stored file). `sheet_name` is optional.

`read_excel` and `read_excel_detailed` read `.xlsx` workbooks. For `.xls`, `.xlsb` or `.ods`, use `read_file` from the **en-file-management** (only where available) — it returns the content as Markdown.

### read_excel_detailed

```json
{
  "document_id": "<id of stored xlsx>",
  "include_headers": true,
  "sheet_name": "Sheet1"
}
```

Same input options as `read_excel` (`file_content` / `librechat_file_id` / `document_id`, optional `sheet_name`). Returns values, formulas, comments, validation rules, hyperlinks, named ranges, merged cells, and workbook properties.

## Optional: If Code Execution Is Available — Analysing Attached Spreadsheets

For calculations, filters, group-bys, pivots, statistics or charts on an attached CSV/XLSX, code execution is more reliable than reading values and computing in your head.

1. The attachment is in the sandbox at `/mnt/data/<filename>` (check with `os.listdir("/mnt/data")`).
2. `import pandas` first; if it is missing, use the fallback. Load with `pd.read_excel(path, sheet_name=None)` (all sheets) or `pd.read_csv(path, sep=None, engine="python")`; German exports often need `decimal=","` and `thousands="."`.
3. Look at shape, columns and dtypes before you compute. Report the figures from the code output, not estimates.
4. Result as a file: for a formatted workbook in the corporate design, pass the result table to `create_excel_advanced` / `create_excel_from_json`. A file written in the sandbox (save under a new name in `/mnt/data/`, never overwrite the input) comes back as a chat attachment but without the companyFILES CI – if you style it in the sandbox yourself (openpyxl), call `get_corporate_ci` first and apply its font, colours and page format.

**Fallback without code execution:** `read_excel { "librechat_file_id": "<file_id>" }` (per sheet with `sheet_name` for large workbooks), compute from the returned values step by step and show your intermediate figures. For a chart use `show_interactive_chart` / `create_chart_document` (**charts-diagram-skill**). If the file is too large to read completely, say so and analyse a named sheet or range.

### Building the workbook in the sandbox yourself

The companyFILES tools cover title area, formats, charts and print setup, so prefer `create_excel_advanced`. If you
still build a workbook with openpyxl (e.g. a chart type the tool lacks), apply the same design rules and:

1. Call `get_corporate_ci` first and use its font and colours; whatever is listed under `notConfigured` stays neutral
   (black, greys).
2. Set `number_format` on **every** numeric cell yourself, formula and total cells included (openpyxl does not inherit
   formats; a date otherwise shows as `45337`, 30% as `0.3`).
3. `ws.sheet_view.showGridLines = False`; for wide sheets `ws.page_setup.orientation = "landscape"`,
   `ws.page_setup.fitToWidth = 1`, `ws.page_setup.fitToHeight = 0`, `ws.sheet_properties.pageSetUpPr.fitToPage = True`;
   freeze under the header (`ws.freeze_panes = "A5"`, columns only by the rule above).
4. Charts: `chart.roundedCorners = False`, `chart.legend.overlay = False` and `.overlay = False` on every title you set
   (`chart.title`, `chart.x_axis.title` …); for charts with axes (not pie/doughnut) `chart.x_axis.delete = False` and
   `chart.y_axis.delete = False`. Otherwise Excel may draw the title or legend over the plot, round the frame or hide
   the axes. Always spell out data labels in full (only with few bars, see above): Excel reads a missing switch as
   "on" and then writes series, category and legend key next to every bar:
   `DataLabelList(showVal=True, showSerName=False, showCatName=False, showLegendKey=False, showPercent=False,
   dLblPos="outEnd")` (pie/doughnut without `dLblPos`), plus `chart.dataLabels.numFmt = '#,##0 "€"'` without
   decimals.
5. Pitfalls: in merged cells write only the top-left cell. Never save a workbook loaded with `data_only=True`; that
   replaces every formula with a fixed value. To read formulas *and* values, load twice. Load `.xlsm` with
   `keep_vba=True`, otherwise the macros are lost.
6. If LibreOffice is available (`soffice`), recalculate before handing the file over so formula results are stored, and
   search the result for error values (`#REF!`, `#DIV/0!`, `#NAME?`, `#VALUE!`); never hand over a file with error
   values. Without LibreOffice, say that the values appear after opening in Excel.

## Key Notes

- All create tools return `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id` when the document is also stored as a chat file) — always render `markdownLink` in the reply.
- `modify_excel` requires a `document_id` or `librechat_file_id` pointing to an `.xlsx` file; it errors if the doc type is not Excel. A chat attachment (`librechat_file_id`) is updated in place when possible — the response then contains `librechat_file_id`, `filename`, `modifications` and `message`, but no download link. Otherwise the modified copy is saved as a new document with a new `id` and `markdownLink`.
- Sheet names must match the workbook — call `read_excel` first to see them; an unknown name errors with the available sheets.
- Ranges in `number_formats`, `cell_styles`, `merge_cells` and `row_heights` use sheet rows. With a `title`, the header is row 4; check the `layout` in the create response.
- Cell addresses support sheet prefix: `"Sheet2!B3"`.
- The org/user CI is applied automatically when configured in settings: colours, font, page size and orientation, header/footer with page numbers, and the company name in the file properties. Excel gets no logo.
- To fill a template with `{{placeholder}}` syntax, use `fill_excel_template` from the **en-templates** instead.
