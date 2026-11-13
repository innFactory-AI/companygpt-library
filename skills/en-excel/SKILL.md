---
name: en-excel
description: 'Create, read, and modify Excel (.xlsx) spreadsheets with companyFILES MCP tools. Use when asked to create a spreadsheet, export data to Excel, read or parse an Excel file, edit cells, add sheets, apply formulas, conditional formatting, or auto-filters. Covers CSV-to-Excel, JSON-to-Excel, 2D array input, advanced multi-sheet workbooks, in-place modification, and analysing attached spreadsheets.'
---

# Excel Skill

Tools for creating, reading, and modifying Excel (.xlsx) spreadsheets via companyFILES.

## Tools in This Skill

| Tool                     | Purpose                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ |
| `create_excel_from_csv`  | Create Excel from CSV text                                                     |
| `create_excel`           | Create Excel from a 2D array                                                   |
| `create_excel_from_json` | Create Excel from JSON (array of objects)                                      |
| `create_excel_advanced`  | Create multi-sheet workbooks with formulas, validation, conditional formatting |
| `modify_excel`           | Edit an existing Excel file in-place by document ID                            |
| `read_excel`             | Read Excel to JSON (values only)                                               |
| `read_excel_detailed`    | Read Excel with formulas, comments, hyperlinks, named ranges, and metadata     |

## Decision Guide

```
User wants to create Excel from...
  CSV text            → create_excel_from_csv
  JSON array          → create_excel_from_json
  2D array / table    → create_excel
  Complex workbook    → create_excel_advanced  (formulas, multiple sheets, formatting)

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

```json
{
  "sheets": [
    {
      "name": "Sales",
      "data": [
        ["Product", "Q1", "Q2", "Total"],
        ["Widget A", 100, 150, { "formula": "SUM(B2:C2)" }],
        ["Widget B", 200, 180, { "formula": "SUM(B3:C3)" }]
      ],
      "has_headers": true,
      "auto_filter": true,
      "conditional_formatting": [
        {
          "range": "B2:C3",
          "type": "greaterThan",
          "values": [150],
          "style": { "backgroundColor": "00FF00" }
        }
      ]
    }
  ],
  "filename": "sales_report"
}
```

**Formula syntax:** Use `{"formula": "SUM(A1:A10)"}` object — no leading `=`.

**Conditional formatting types:** `greaterThan`, `lessThan`, `equal`, `between`, `containsText`, `duplicateValues`

**Other per-sheet options:** `column_widths` (number array), `protected` (boolean). Top-level: `named_ranges` and `properties` (`{title, subject, author, company}`). Individual cells may also be extended objects: `{"value": ..., "comment": ..., "validation": ..., "style": ..., "numberFormat": ...}`. Such an object needs `value` (plus at least one of the other keys); a formula goes **inside** `value`, not next to it: `{"value": {"formula": "SUM(A1:A3)"}, "comment": "Total"}`. A `formula` key beside `value` and `comment` is ignored; an object without `value` (e.g. `{"formula": …, "comment": …}`) is written as a plain formula and its other keys are dropped.

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

## Key Notes

- All create tools return `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id` when the document is also stored as a chat file) — always render `markdownLink` in the reply.
- `modify_excel` requires a `document_id` or `librechat_file_id` pointing to an `.xlsx` file; it errors if the doc type is not Excel. A chat attachment (`librechat_file_id`) is updated in place when possible — the response then contains `librechat_file_id`, `filename`, `modifications` and `message`, but no download link. Otherwise the modified copy is saved as a new document with a new `id` and `markdownLink`.
- Sheet names must match the workbook — call `read_excel` first to see them; an unknown name errors with the available sheets.
- Cell addresses support sheet prefix: `"Sheet2!B3"`.
- The org/user CI is applied automatically when configured in settings: colours, font, page size and orientation, header/footer with page numbers, and the company name in the file properties. Excel gets no logo.
- To fill a template with `{{placeholder}}` syntax, use `fill_excel_template` from the **en-templates** instead.
