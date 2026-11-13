---
name: en-settings-ui
description: 'Open the companyFILES web UI, view settings, and get help on available tools. Use when asked to show documents, browse files, open the file manager, manage templates, change settings, view branding/colors or the corporate identity (CI), need the CI for a document created another way (e.g. with code execution), or get help on how to use companyFILES tools. Also use when the user wants an interactive embedded view instead of raw JSON.'
---

# Settings & UI Skill

Tools for opening the companyFILES web app as an embedded UI, retrieving settings, and getting tool help.

## Tools in This Skill

| Tool                   | Purpose                                                     |
| ---------------------- | ----------------------------------------------------------- |
| `open_companyfiles_ui` | Open the companyFILES web app as an embedded iframe         |
| `get_corporate_ci`     | The corporate identity (CI) as JSON: colors, fonts, sizes, page format, header/footer, page numbers, logo |
| `get_settings`         | Same as `get_corporate_ci` (older name)                     |
| `help`                 | Get usage examples for any companyFILES tool category       |

## Decision Guide

```
User says "show my files" / "open file manager"    → open_companyfiles_ui page="documents"
User says "manage / browse templates"               → open_companyfiles_ui page="templates"
User says "upload a file" (via UI)                  → open_companyfiles_ui page="documents"
User says "upload a template" (via UI)              → open_companyfiles_ui page="upload"
User says "open settings" / "change preferences"   → open_companyfiles_ui page="settings"

User asks about CI / colors / fonts / logo          → get_corporate_ci
Document outside the companyFILES tools (code interpreter) → first get_corporate_ci, then apply the values
User asks how to use a tool / needs examples        → help (with topic)
```

**Always call the tool immediately — never just describe what the user could do.**

## Tool Usage

### open_companyfiles_ui

Renders the companyFILES SPA as an embedded interactive iframe in the chat.

```json
{
  "page": "documents"
}
```

Available pages (enum — only these four values are accepted):
| Page | Shows |
|------|-------|
| `documents` | Document list (including chat uploads), file upload, preview, download |
| `templates` | Template browser, upload personal templates |
| `upload` | Template upload form (upload a new template) |
| `settings` | Tabs **My Settings** (Meine Einstellungen: personal colors, typography, document defaults, logo) and **Organization** (Organisation: company info, org colors and logo — read-only without the admin permission; admins also edit org typography and document defaults) |

The settings page has no language setting — the language is switched in the account menu of the companyFILES web app. The web app's **Visualizations** page (charts, diagrams and maps from the chat) is not one of the page values and cannot be opened with `open_companyfiles_ui`.

> Note: UI widgets require a chat client that supports MCP UI rendering (e.g. LibreChat). Google Gemini falls back to text.

---

### get_corporate_ci

Returns the resolved corporate identity: the organization settings with the user's personal overrides. `get_settings` returns the same answer (older name).

```json
{}
```

Example response (shortened; only configured values appear, colors with `#`):

```json
{
  "company": { "name": "Acme Ltd", "url": "https://acme.example" },
  "colors": { "primary": "#336699", "primaryDark": "#264D73", "primaryLight": "#E0E8F0", "heading": "#1F2937", "link": "#2563EB" },
  "fonts": { "heading": "Georgia", "body": "Arial" },
  "fontSizesPt": { "body": 11, "h1": 24 },
  "page": {
    "size": "A4",
    "orientation": "portrait",
    "footerText": "Acme Ltd · Confidential",
    "pageNumbers": { "show": true, "position": "footer", "format": "{page} / {pages}" }
  },
  "logo": { "available": true, "inDocuments": true, "position": "header-right", "heightCm": 1.2, "format": "png", "widthPx": 600, "heightPx": 200, "source": "org" },
  "sources": { "companyName": "org", "primaryColor": "user" },
  "notConfigured": ["secondaryColor", "fontCode", "defaultHeaderText"],
  "usage": "Apply these values to every document you create …"
}
```

- `logo.inDocuments` says whether the companyFILES tools put the logo into documents; `logo.position` is `header-left|header-center|header-right|footer-left|footer-center|footer-right`, `logo.heightCm` the height (keep the aspect ratio).
- `notConfigured` lists settings neither the organization nor the user has set: use neutral defaults there.
- The companyFILES document tools apply the CI automatically. When you create a document yourself (e.g. with code execution and python-docx, python-pptx or openpyxl), call `get_corporate_ci` first and apply the colors, fonts, sizes, page format, header/footer, page numbers and logo position.
- The logo's path and image file are not included. To view or change the logo, use `open_companyfiles_ui page="settings"`.

---

### help

Get detailed usage examples for a specific tool category.

```json
{
  "topic": "excel"
}
```

Available topics: `excel`, `word`, `pdf`, `powerpoint`, `text`, `chart`, `mermaid`, `map`, `zip`, `upload`, `templates`, `admin`, `convert`, `read`, `settings`, `assets`, `ui`, `provenance` (AI marking in file metadata), `all` — plus `cad` and `docs` where those extensions are available. An unknown topic returns the list of available topics.

Omitting `topic` (or using `"all"`) returns the full help document and also opens the embedded UI.

## Key Notes

- `open_companyfiles_ui` is the default tool for any request to browse, view, or manage files/templates/settings interactively.
- The CI from the settings automatically feeds all document and chart creation tools: colors (`primaryColor` and the extended `headingColor`, `bodyTextColor`, `linkColor`, `tableHeaderBg`, `tableHeaderText`, `codeBg`; `secondaryColor` and `accentColor` apply to charts only), typography (`fontHeading`, `fontBody`, `fontCode`, `fontSize*`), and document defaults (`defaultPageSize`, `defaultPageOrientation`, `defaultHeaderText`, `defaultFooterText`, `defaultShowPageNumbers`, `defaultPageNumberPosition`, `defaultPageNumberFormat`, `logoInHeader` = logo in documents, `logoPosition`, `logoHeaderHeight`). `get_corporate_ci` returns all of these values at once.
- To edit settings, use the UI (`open_companyfiles_ui page="settings"`): personal values on **My Settings**, organization values on **Organization**. Changing organization settings and branding requires the companyFILES admin permission (`ext:files:admin`); uploading or promoting global templates requires the template permission (`ext:files:templates`). Users without these permissions manage only their personal settings and templates.
