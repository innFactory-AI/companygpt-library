---
name: de-charts-diagram
description: 'Erstelle interaktive Diagramme, Grafiken und Karten mit companyFILES MCP-Tools. Verwende diesen Skill, wenn Daten visualisiert werden sollen, ein Balken-, Linien-, Kreis-, Streu- oder Blasendiagramm erstellt werden soll, ein Flussdiagramm, Sequenzdiagramm, ER-Diagramm, Gantt-Diagramm oder ein beliebiges Mermaid-Diagramm gezeichnet werden soll oder Standorte als Pins auf einer Karte angezeigt werden sollen. Deckt auch das Einbetten von Diagrammen in Word-, PDF- oder PowerPoint-Dokumente ab.'
---

# Charts & Diagramme Skill

Tools zum Erstellen interaktiver Diagramme (Chart.js), Grafiken (Mermaid) und Karten sowie zum Einbetten von Diagrammen in Dokumente.

## Tools in diesem Skill

| Tool                       | Zweck                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| `show_interactive_chart`   | **BEVORZUGT** – Interaktives Chart.js-Widget (Zoom, Verschieben, Typwechsel, Export)      |
| `show_interactive_diagram` | **BEVORZUGT** – Interaktives Mermaid-Diagramm-Widget (Verschieben, Zoom, Export)          |
| `show_interactive_map`     | Interaktives Karten-Widget mit Pins, Clustering und Legende (Export als PNG/JPG)          |
| `create_chart_document`    | Ein Diagrammbild in ein Word-, PDF- oder PowerPoint-Dokument einbetten                    |
| `embed_chart_in_document`  | Ein Chart.js-Diagramm rendern und in ein Dokument einbetten                               |

## Entscheidungshilfe

```
Benutzer will ein Diagramm im Chat SEHEN       → show_interactive_chart   (IMMER bevorzugt)
Benutzer will eine Grafik im Chat SEHEN        → show_interactive_diagram  (IMMER bevorzugt)
Benutzer will Standorte auf einer Karte SEHEN  → show_interactive_map

Benutzer will ein Diagramm in einer PowerPoint → natives Diagramm: slides[].chart / charts (de-powerpoint)
                                                 in PowerPoint bearbeitbar, kein Bild
Benutzer will ein Diagramm als Word/PDF SPEICHERN...
  Diagramm + optionaler Beschreibungstext      → create_chart_document
  Diagramm in einem Dokument (mehr Kontrolle)  → embed_chart_in_document

Benutzer will eine Grafik als Dokument SPEICHERN → siehe de-word-odt oder de-pdf
  (Grafik zuerst rendern, dann manuell einbetten oder in Markdown beschreiben)
```

## Tool-Verwendung

### show_interactive_chart (BEVORZUGT für Diagramme)

Unterstützte Diagrammtypen: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`, `waterfall`, `funnel`, `area`, `stackedBar`, `horizontalBar`

```json
{
  "chart_type": "bar",
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "datasets": [
    { "label": "Umsatz", "data": [100, 150, 120, 180] },
    { "label": "Kosten", "data": [80, 110, 90, 140] }
  ],
  "title": "Quartalsentwicklung",
  "x_axis_label": "Quartal",
  "y_axis_label": "EUR"
}
```

Optional: `x_axis_label`, `y_axis_label` und `options` (ein rohes Chart.js-Optionsobjekt, das über die Standardwerte gelegt wird). Datasets akzeptieren außerdem `borderWidth` und `fill`.

**Streudiagramm** (verwende `{x, y}`-Datenpunkte):

```json
{
  "chart_type": "scatter",
  "labels": [],
  "datasets": [
    {
      "label": "Punkte",
      "data": [
        { "x": 1, "y": 2 },
        { "x": 3, "y": 4 }
      ]
    }
  ]
}
```

**Blasendiagramm** (ergänze `r` für den Radius):

```json
{
  "chart_type": "bubble",
  "labels": [],
  "datasets": [
    {
      "label": "Blasen",
      "data": [
        { "x": 1, "y": 2, "r": 10 },
        { "x": 3, "y": 4, "r": 5 }
      ]
    }
  ]
}
```

Das Widget bietet: Zoom/Verschieben, einen Diagrammtyp-Umschalter und ein Exportmenü mit PNG (1x/2x/4x), CSV kopieren und Bild kopieren.

---

### show_interactive_diagram (BEVORZUGT für Grafiken)

Unterstützte Grafiktypen (Mermaid-Syntax): Flussdiagramm, Sequenz, Klasse, Zustand, ER, Gantt, Kreis, Mindmap, Zeitleiste und weitere.

```json
{
  "code": "graph TD\n  A[Start] --> B{Entscheidung}\n  B -->|Ja| C[Das tun]\n  B -->|Nein| D[Etwas anderes tun]\n  C --> E[Ende]\n  D --> E",
  "title": "Entscheidungsablauf",
  "theme": "default"
}
```

Der Mermaid-Quelltext gehört in den Parameter **`code`** (nicht `mermaid_code`).

**Themes:** `default`, `dark`, `forest`, `neutral`

Das Widget bietet: Verschieben/Zoom, einen Theme-Umschalter und Export als SVG, PNG (2x) oder JPG. Nach einem Export kopiert „Link kopieren“ den Download-Link der exportierten Datei.

---

### show_interactive_map

Interaktive Karte (OpenStreetMap-Kacheln) mit Pins. `map_type`: `world` (freies Verschieben/Zoomen) oder `germany` (mit eingeblendeten Grenzen der deutschen Bundesländer).

```json
{
  "map_type": "germany",
  "title": "Standorte",
  "pins": [
    { "lat": 48.137, "lng": 11.575, "label": "München", "category": "own" },
    { "lat": 52.52, "lng": 13.405, "label": "Berlin", "category": "partner", "details": { "Mitarbeitende": 42 } }
  ],
  "legend": [
    { "category": "own", "color": "#2563EB", "label": "Eigene Standorte" },
    { "category": "partner", "color": "#F59E0B", "label": "Partner" }
  ]
}
```

Jeder Pin braucht `lat` + `lng` und ein `label`; optional sind `tooltip` (Hover-Text), `category` (Pinfarbe über `legend`), `color` (explizite Hex-Farbe) und `details` (Schlüssel-Wert-Paare, die im Klick-Popup angezeigt werden). Bis zu 5.000 Pins. Nahe beieinanderliegende Pins werden standardmäßig zusammengefasst (`cluster: false` schaltet das ab). Optional: `center` (`{ "lat": …, "lng": … }`), `zoom` (1–20), `show_state_borders`.

Nur wenn Azure Maps für die Umgebung konfiguriert ist: `address` statt `lat`/`lng` (wird geokodiert), `route` (`waypoints`, `travel_mode`: `car`, `pedestrian`, `bicycle`), `distance_matrix_from`, `isochrone` und `reverse_geocode`. Ohne Azure Maps schlägt der Aufruf mit diesen Optionen fehl – verwende sie nur, wenn du sicher weißt, dass sie verfügbar sind.

Die Antwort besteht aus dem Karten-Widget und einer Textzeile `Interactive map: [title](url) — open the link for PNG/JPG export.`

---

### create_chart_document

Rendert ein Diagrammbild und bettet es in ein Dokument ein, optional mit einer Beschreibung darunter.

Unterstützt erweiterte Diagrammtypen: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`, `waterfall`, `funnel`, `area`, `stackedBar`, `horizontalBar`

```json
{
  "chart_type": "line",
  "labels": ["Jan", "Feb", "Mär", "Apr", "Mai"],
  "datasets": [{ "label": "Verkäufe", "data": [50, 70, 65, 90, 110] }],
  "title": "Monatlicher Verkaufstrend",
  "description": "Die Verkäufe sind im ersten und zweiten Quartal stetig gestiegen.",
  "output_format": "word",
  "filename": "sales_trend"
}
```

`output_format`-Optionen: `word` (Standard), `pdf`, `powerpoint`

---

### embed_chart_in_document

Mehr Kontrolle über die Diagrammabmessungen beim Einbetten.

Unterstützte Typen: `bar`, `line`, `pie`, `doughnut`, `radar`, `scatter`, `bubble`, `polarArea`

```json
{
  "chart_type": "bar",
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "datasets": [{ "label": "Umsatz", "data": [100, 150, 120, 180] }],
  "document_type": "pdf",
  "title": "Quartalsumsatz",
  "width": 1400,
  "height": 900,
  "filename": "revenue_chart"
}
```

`document_type`-Optionen: `word`, `powerpoint`, `pdf`

### Diagramm in einer PowerPoint: nativ, nicht als Bild

Für `.pptx` nimmst du das native, bearbeitbare Diagramm der PowerPoint-Tools statt `create_chart_document` /
`embed_chart_in_document` (die rendern ein Bild). Die Daten sind dieselben wie bei `show_interactive_chart`
(`labels` + `datasets`), der Schlüssel heißt aber `type` (nicht `chart_type`), und die Typen sind `bar`,
`horizontalBar`, `stackedBar`, `line`, `area`, `pie`, `doughnut`, `scatter`, `radar` (kein
`bubble`/`polarArea`/`waterfall`/`funnel`; dafür `create_chart_document`). `scatter` nimmt numerische Labels als
x-Werte. Generierter Foliensatz (`create_powerpoint`, `append_slides_to_powerpoint`, `update_powerpoint_slide`):

```json
{
  "slides": [
    {
      "type": "default",
      "title": "Umsatz je Quartal",
      "chart": { "type": "bar", "labels": ["Q1", "Q2", "Q3"], "datasets": [{ "label": "2026", "data": [12, 15, 19] }] }
    }
  ]
}
```

Corporate-Foliensatz (`create_powerpoint_from_layouts`, `add_slides_from_layouts`, `set_powerpoint_slide_fields`):
dasselbe Objekt je Slot in `charts`, z. B. `"charts": { "chart:15": { "type": "bar", … } }`; der Slot muss in
`describe_pptx_template` `acceptsChart` melden. Details: de-powerpoint.

## Wichtige Hinweise

- `show_interactive_chart` und `show_interactive_diagram` liefern ein **Widget** (in LibreChat gerendert) und zusätzlich eine Textzeile wie `Interactive chart: [Title](viewer-url) · [Download PNG](url)` (`Interactive diagram: …` bei Grafiken). Gib diese als normale Markdown-Links weiter – bette die Download-URL **niemals** als Bild ein (`![](…)`): Sie ist ein authentifizierter Download-Endpunkt, kein Bild, das der Browser laden kann. Konnte der PNG-Fallback nicht gerendert werden, enthält die Zeile nur den Viewer-Link.
- Die Tools zum Einbetten in Dokumente liefern `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id`, wenn das Dokument zusätzlich als Chat-Datei gespeichert wird) – gib immer `markdownLink` aus.
- Die Farbpalette der Organisation bzw. des Benutzers wird automatisch auf die Diagrammfarben angewendet, wenn sie in den Einstellungen konfiguriert ist.
- Google-Gemini-Modelle können keine interaktiven Widgets rendern – die Antworten fallen dann auf Text/JSON-Daten zurück.
- `create_chart_document` und `embed_chart_in_document` mit `powerpoint` erzeugen ein Bild, kein bearbeitbares Diagramm. Für Foliensätze bevorzuge das native Diagramm.
- `show_interactive_chart` und `create_chart_document` akzeptieren alle 13 Diagrammtypen; `area`, `stackedBar` und `horizontalBar` werden beim Rendern als Bild auf ihre statischen Entsprechungen abgebildet. `embed_chart_in_document` akzeptiert nur die 8 Basistypen und lehnt die erweiterten ab – verwende dafür `create_chart_document`.
