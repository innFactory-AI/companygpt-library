---
name: de-settings-ui
description: 'Die companyFILES-Web-UI öffnen, Einstellungen anzeigen und Hilfe zu den verfügbaren Tools erhalten. Verwenden, wenn Dokumente angezeigt, Dateien durchsucht, der Dateimanager geöffnet, Vorlagen verwaltet, Einstellungen geändert, Branding/Farben oder die Corporate Identity (CI) angezeigt, die CI für ein selbst erstelltes Dokument (z. B. per Code-Ausführung) gebraucht oder Hilfe zur Nutzung der companyFILES-Tools gewünscht werden. Auch verwenden, wenn der Benutzer statt rohem JSON eine interaktive eingebettete Ansicht möchte.'
---

# Einstellungen & UI Skill

Tools, um die companyFILES-Web-App als eingebettete UI zu öffnen, Einstellungen abzurufen und Hilfe zu den Tools zu erhalten.

## Tools in diesem Skill

| Tool                   | Zweck                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------- |
| `open_companyfiles_ui` | Die companyFILES-Web-App als eingebetteten iframe öffnen                           |
| `get_corporate_ci`     | Die Corporate Identity (CI) als JSON: Farben, Schriften, Größen, Seitenformat, Kopf-/Fußzeile, Seitenzahlen, Logo |
| `get_settings`         | Wie `get_corporate_ci` (älterer Name)                                              |
| `help`                 | Anwendungsbeispiele für jede companyFILES-Tool-Kategorie abrufen                   |

## Entscheidungshilfe

```
Benutzer sagt „zeig meine Dateien“ / „Dateimanager öffnen“  → open_companyfiles_ui page="documents"
Benutzer sagt „Vorlagen verwalten / durchsuchen“            → open_companyfiles_ui page="templates"
Benutzer sagt „eine Datei hochladen“ (über die UI)          → open_companyfiles_ui page="documents"
Benutzer sagt „eine Vorlage hochladen“ (über die UI)        → open_companyfiles_ui page="upload"
Benutzer sagt „Einstellungen öffnen“ / „Präferenzen ändern“ → open_companyfiles_ui page="settings"

Benutzer fragt nach CI / Farben / Schriften / Logo          → get_corporate_ci
Dokument außerhalb der companyFILES-Tools (Code-Interpreter) → zuerst get_corporate_ci, dann die Werte anwenden
Benutzer fragt, wie ein Tool funktioniert / braucht Beispiele → help (mit topic)
```

**Rufe das Tool immer sofort auf – beschreibe nie nur, was der Benutzer tun könnte.**

## Tool-Verwendung

### open_companyfiles_ui

Rendert die companyFILES-SPA als eingebetteten interaktiven iframe im Chat.

```json
{
  "page": "documents"
}
```

Verfügbare Seiten (Enum – nur diese vier Werte werden akzeptiert):
| Seite | Zeigt |
|------|-------|
| `documents` | Dokumentliste (einschließlich Chat-Uploads), Datei-Upload, Vorschau, Download |
| `templates` | Vorlagen-Browser, Hochladen persönlicher Vorlagen |
| `upload` | Formular zum Hochladen einer neuen Vorlage |
| `settings` | Reiter **Meine Einstellungen** (persönliche Farben, Typografie, Dokument-Standards, Logo) und **Organisation** (Firmendaten, Organisationsfarben und -logo – ohne Admin-Berechtigung nur lesbar; Admins bearbeiten zusätzlich Typografie und Dokument-Standards der Organisation) |

Die Einstellungsseite enthält keine Spracheinstellung – die Sprache wird im Kontomenü der companyFILES-Web-App umgestellt. Die Seite **Visualisierungen** der Web-App (Diagramme, Schaubilder und Karten aus dem Chat) ist kein `page`-Wert und kann nicht mit `open_companyfiles_ui` geöffnet werden.

> Hinweis: UI-Widgets erfordern einen Chat-Client, der MCP-UI-Rendering unterstützt (z. B. LibreChat). Google Gemini fällt auf Text zurück.

---

### get_corporate_ci

Liefert die aufgelöste Corporate Identity: die Organisationseinstellungen mit den persönlichen Überschreibungen des Nutzers. `get_settings` liefert dieselbe Antwort (älterer Name).

```json
{}
```

Beispielantwort (gekürzt; nur gesetzte Werte erscheinen, Farben mit `#`):

```json
{
  "company": { "name": "Acme GmbH", "url": "https://acme.example" },
  "colors": { "primary": "#336699", "primaryDark": "#264D73", "primaryLight": "#E0E8F0", "heading": "#1F2937", "link": "#2563EB" },
  "fonts": { "heading": "Georgia", "body": "Arial" },
  "fontSizesPt": { "body": 11, "h1": 24 },
  "page": {
    "size": "A4",
    "orientation": "portrait",
    "footerText": "Acme GmbH · Vertraulich",
    "pageNumbers": { "show": true, "position": "footer", "format": "{page} / {pages}" }
  },
  "logo": { "available": true, "inDocuments": true, "position": "header-right", "heightCm": 1.2, "format": "png", "widthPx": 600, "heightPx": 200, "source": "org" },
  "sources": { "companyName": "org", "primaryColor": "user" },
  "notConfigured": ["secondaryColor", "fontCode", "defaultHeaderText"],
  "usage": "Apply these values to every document you create …"
}
```

- `logo.inDocuments` sagt, ob die companyFILES-Tools das Logo in Dokumente setzen; `logo.position` ist `header-left|header-center|header-right|footer-left|footer-center|footer-right`, `logo.heightCm` die Höhe (Seitenverhältnis beibehalten).
- `notConfigured` nennt Einstellungen, die weder die Organisation noch der Nutzer gesetzt hat: dort neutrale Standards verwenden.
- Die companyFILES-Dokument-Tools wenden die CI automatisch an. Erstellst du ein Dokument selbst (z. B. mit Code-Ausführung und python-docx, python-pptx oder openpyxl), rufe vorher `get_corporate_ci` auf und übernimm Farben, Schriften, Größen, Seitenformat, Kopf-/Fußzeile, Seitenzahlen und die Logo-Position.
- Pfad und Bilddatei des Logos sind nicht enthalten. Um das Logo anzusehen oder zu ändern, verwende `open_companyfiles_ui page="settings"`.

---

### help

Liefert ausführliche Anwendungsbeispiele für eine bestimmte Tool-Kategorie.

```json
{
  "topic": "excel"
}
```

Verfügbare Themen: `excel`, `word`, `pdf`, `powerpoint`, `text`, `chart`, `mermaid`, `map`, `zip`, `upload`, `templates`, `admin`, `convert`, `read`, `settings`, `assets`, `ui`, `provenance` (KI-Kennzeichnung in den Datei-Metadaten), `all` – sowie `cad` und `docs`, wo diese Erweiterungen verfügbar sind. Ein unbekanntes Thema liefert die Liste der verfügbaren Themen.

Ohne `topic` (oder mit `"all"`) wird das vollständige Hilfedokument zurückgegeben und zusätzlich die eingebettete UI geöffnet.

## Wichtige Hinweise

- `open_companyfiles_ui` ist das Standard-Tool für jede Anfrage, Dateien/Vorlagen/Einstellungen interaktiv zu durchsuchen, anzuzeigen oder zu verwalten.
- Die CI aus den Einstellungen fließt automatisch in alle Tools zur Dokument- und Diagrammerstellung ein: Farben (`primaryColor` und die erweiterten `headingColor`, `bodyTextColor`, `linkColor`, `tableHeaderBg`, `tableHeaderText`, `codeBg`; `secondaryColor` und `accentColor` gelten nur für Charts), Typografie (`fontHeading`, `fontBody`, `fontCode`, `fontSize*`) und Dokument-Standards (`defaultPageSize`, `defaultPageOrientation`, `defaultHeaderText`, `defaultFooterText`, `defaultShowPageNumbers`, `defaultPageNumberPosition`, `defaultPageNumberFormat`, `logoInHeader` = Logo in Dokumenten, `logoPosition`, `logoHeaderHeight`). `get_corporate_ci` liefert alle diese Werte auf einmal.
- Zum Bearbeiten der Einstellungen verwende die UI (`open_companyfiles_ui page="settings"`): persönliche Werte unter **Meine Einstellungen**, Organisationswerte unter **Organisation**. Das Ändern von Organisationseinstellungen und Branding erfordert die companyFILES-Admin-Berechtigung (`ext:files:admin`); das Hochladen oder Hochstufen globaler Vorlagen erfordert die Vorlagen-Berechtigung (`ext:files:templates`). Benutzer ohne diese Berechtigungen verwalten nur ihre persönlichen Einstellungen und Vorlagen.
