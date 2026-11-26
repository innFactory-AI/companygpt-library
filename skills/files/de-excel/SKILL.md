---
name: de-excel
description: 'Erstelle, lies und bearbeite Excel-Tabellen (.xlsx) mit companyFILES MCP-Tools. Verwende diesen Skill, wenn eine Tabelle erstellt, Daten nach Excel exportiert, eine Auswertung, ein Vergleich, eine Kostenrechnung oder Management-Zusammenfassung als Excel gebaut, eine Excel-Datei gelesen oder ausgewertet, Zellen bearbeitet, Blätter hinzugefügt oder Formeln, Zahlenformate, bedingte Formatierung, Diagramme oder Autofilter angewendet werden sollen. Deckt Arbeitsmappen im Berichtslook (Titel, Annahmen-Blatt, Summen, Diagramme, Druckeinstellungen), CSV-zu-Excel, JSON-zu-Excel, 2D-Array-Eingaben, das direkte Bearbeiten bestehender Dateien und die Auswertung angehängter Tabellen ab.'
---

# Excel Skill

Tools zum Erstellen, Lesen und Bearbeiten von Excel-Tabellen (.xlsx) über companyFILES.

> **Office-Add-in:** Stehen `excel_*`-Tools in deiner Tool-Liste, läuft der Chat in Excel und dort ist ein Dokument geöffnet. Meint der Nutzer die geöffnete Arbeitsmappe, arbeite mit diesen Tools darin statt mit diesem Skill. Dieser Skill ist für neue Dateien zum Herunterladen (siehe de-file-routing).

## Tools in diesem Skill

| Tool                     | Zweck                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| `create_excel_from_csv`  | Excel aus CSV-Text erstellen                                                                |
| `create_excel`           | Excel aus einem 2D-Array erstellen                                                          |
| `create_excel_from_json` | Excel aus JSON (Array von Objekten) erstellen                                               |
| `create_excel_advanced`  | Berichts-Arbeitsmappen: Titel, mehrere Blätter, Formeln, Formate, Diagramme, Druck         |
| `modify_excel`           | Bestehende Excel-Datei direkt bearbeiten (Werte, Formate, Verbinden, Blattoptionen)        |
| `read_excel`             | Excel als JSON lesen (nur Werte)                                                            |
| `read_excel_detailed`    | Excel mit Formeln, Kommentaren, Hyperlinks, benannten Bereichen und Metadaten lesen         |

## Entscheidungshilfe

```
Benutzer will Excel erstellen aus...
  CSV-Text              → create_excel_from_csv
  JSON-Array            → create_excel_from_json
  2D-Array / Tabelle    → create_excel
  Auswertung, Vergleich, Kalkulation, Management-Zusammenfassung, alles zum Lesen oder Drucken
                        → create_excel_advanced mit "preset": "report" + Titel + Diagramm  (siehe Gestaltungsregeln)
  Komplexe Arbeitsmappe → create_excel_advanced  (Formeln, mehrere Blätter, Formatierung, Diagramme)

Benutzer will eine bestehende Excel-Datei bearbeiten → modify_excel  (benötigt document_id oder librechat_file_id)

Benutzer will Excel-Inhalte lesen / auswerten...
  Nur Werte             → read_excel
  Formeln & Metadaten   → read_excel_detailed
  .xls / .xlsb / .ods   → read_file  (file-management-skill, falls verfügbar)

Benutzer will Berechnungen / Pivots / Statistik auf einer angehängten Tabelle
                        → Code-Ausführung, falls verfügbar, sonst read_excel + schrittweise (siehe „Optional“ unten)
```

## Angehängte Tabellen

Eine vom Benutzer angehängte Tabelle steht im Block `Attached files in this message:` (`- file_id: …, filename: …`). Übergib diese `file_id` als `librechat_file_id` an `read_excel`, `read_excel_detailed` oder `modify_excel`; nutze `list_my_files` nur, wenn es keinen solchen Block gibt. Rate nie eine ID. Für andere Dateiaufgaben und Apps siehe **file-routing-skill**.

## Gestaltungsregeln für Berichts-Arbeitsmappen

Wende sie auf jede Arbeitsmappe an, die Menschen lesen, drucken oder weitergeben (Auswertungen, Vergleiche, Angebote,
Kostenrechnungen, Management-Zusammenfassungen). Ein reiner Datenexport (`create_excel_from_csv` / `_json`) braucht sie
nicht.

**Was zuerst gilt:**

1. **Vorgaben des Benutzers wörtlich umsetzen:** Blattnamen, Spaltenüberschriften, Reihenfolge und Formeln genau so,
   wie er sie nennt. Ein schönerer Aufbau, der etwas anderes rechnet, verfehlt die Aufgabe.
2. **Bestehende Datei: deren Stil hat Vorrang** vor allen Regeln hier. Finde zuerst die Eingabezellen (sie sind meist
   an eigener Schriftfarbe oder Füllung erkennbar), schreib nur dort und lass vorhandene Formeln unverändert.
3. **Nur so viel Aufbau, wie der Inhalt braucht.** Eine einfache Liste bekommt Titel, Zahlenformate und Summen, aber
   kein Annahmen-Blatt. Die volle Struktur unten ist für mehrteilige Auswertungen gedacht.

**Aufbau und Rechnen:**

- **Reihenfolge der Blätter** (bei mehrteiligen Auswertungen): Übersicht/Management-Zusammenfassung → Detailblätter →
  Vergleich / Vor- und Nachteile → Erkenntnisse und nächste Schritte → Annahmen und Quellen. Was es nicht gibt, fällt
  weg.
- **Titelbereich:** Jedes Berichtsblatt bekommt `title` und einen `subtitle` mit Umfang, Stand und Basis („Stand
  25.11.2026 · alle Preise netto“). Den Titel nie in eine Kopfzelle oder eine „Abschnitts“-Zeile in Großbuchstaben
  schreiben.
- **Rechnen statt eintippen:** Jeder Parameter steht in einer eigenen beschrifteten Zelle, bei Auswertungen im
  **Annahmen-Blatt** mit Quellenspalte. Formeln beziehen sich absolut darauf (`Annahmen!$B$4`, nie `B5*1.05`); die
  Übersicht verweist auf die Detailblätter (`Standorte!G21`). **Tippe nie ein berechnetes Ergebnis ein.** Summen sind
  `SUM`-Formeln.
- **Gleiche Formel über die ganze Zeile:** Perioden und Standorte rechnen alle nach demselben Muster. Eine einzeln
  abweichende Zelle mitten in einer Reihe ist der häufigste unbemerkte Fehler. Nenner, die 0 werden können, fängst du
  ab (`IFERROR(B5/C5,0)`).
- **Herkunft jeder festen Zahl:** Jede eingetragene Zahl bekommt eine Quelle dort, wo der Leser sie sieht
  (Quellenspalte, Notiz oder Zellkommentar). Stammt sie vom Benutzer, schreib das so hin („Angabe des Benutzers“).
- **Formeln, die überall rechnen:** englische Funktionsnamen und Komma als Trenner (`SUM`, `IF`, `IFERROR`). Bevorzuge
  bewährte Funktionen wie `SUMIFS`, `INDEX`/`MATCH`, `IFERROR`, `SUMPRODUCT`. **Kein** `XLOOKUP`, `XMATCH`, `FILTER`,
  `SORT`, `UNIQUE` oder `SEQUENCE`: Ältere Excel-Versionen, LibreOffice und Vorschauen rechnen sie nicht, und
  Überlauf-Ergebnisse landen nur in der ersten Zelle. Nachschlagen mit `INDEX`/`MATCH`, Sortieren und Filtern erledigst
  du vorher in den Daten. `TEXTJOIN`, `CONCAT`, `IFS`, `SWITCH`, `MAXIFS` und `MINIFS` gehen nur mit dem Präfix
  `_xlfn.` (`_xlfn.IFS(…)`), sonst zeigt Excel `#NAME?`.
- **Blattnamen mit Leerzeichen** stehen in Bezügen in Hochkommas: `'Annahmen 2026'!$B$4` (ohne sie: `#VALUE!`).

**Formate und Aussehen:**

- **Zahlenformat auf jeder Zahlenzelle, auch Formel- und Summenzellen** (sonst zeigt Excel `19380` statt `19.380 €`).
  Die Einheit steht in der Kopfzeile („Kosten (€ netto)“):
  - Währung `#,##0 "€";-#,##0 "€";"–"` (Stückpreise `#,##0.00 "€"`)
  - Anzahlen `#,##0;-#,##0;"–"`, Faktor `0.0"x"`, Prozent `0.0%` als Anteil gespeichert (0,19, nicht 19)
  - Jahreszahlen als Text (`"2026"`), sonst erscheinen sie in einer Zahlenspalte als `2.026`.
- **Farben kommen aus der CI, sonst bleibt alles neutral:** Titel und Kopfzeile färben die Tools automatisch in den
  CI-Farben. Setz keine eigenen Signalfarben (kein Blau, Gelb, Grün oder Rot). Formeln, Verweise und Texte bleiben in der
  normalen Textfarbe; Summen sind fett mit dünner Linie oben (`"borders": {"top": "thin"}`). Nur Eingabe- und
  Annahmenzellen bekommen eine helle Füllung: `colors.primaryLight` aus `get_corporate_ci`, und wenn die CI keine
  Farbe liefert, neutrales Grau `F2F2F2`. Vor- und Nachteile oder Bewertungen bekommen keine Farbe; die
  Spaltenüberschrift sagt, was gemeint ist.
- **Lange Texte:** Bemerkungs- und Vor-/Nachteil-Spalten umbrechen (`wrapText` + `verticalAlignment: "top"`; lange
  Texte werden automatisch umbrochen). Spaltenbreite 30–50; was länger ist, wird umbrochen statt breiter.
- **Fixieren:** `preset: "report"` fixiert nur die Zeilen bis zur Kopfzeile, so bleibt es meist. Eine Spalte fixierst
  du nur, wenn Spalte A eine kurze Zeilenbeschriftung ist und die Tabelle mehr als 8 Spalten hat (`"freeze": "B5"`).
  Nie eine breite Textspalte und nie mehr als eine Spalte fixieren, sonst bleibt zum Scrollen kaum Platz.
- **Notizen und Quellen** stehen unter der Tabelle (`notes`), nie als lose Zeilen mitten in den Daten.
- **Diagramm – Pflicht bei Vergleichen:** Jeder Vergleich, jede Kostenrechnung, jedes Szenario und jede Zeitreihe
  bekommt ein natives Diagramm (`charts`) auf der Übersicht, unter der Tabelle, für die wichtigste Aussage (z. B.
  Kosten je Standort und Angebot). Ohne Diagramm bleiben nur reine Listen, Datenexporte und Vorlagen zum Ausfüllen.
  Halte es schlicht: höchstens 2–3 Reihen, kurze Kategorienamen, ein knapper Titel.
- **Werte an den Balken (`show_values`) nur bei wenigen Balken** (bis etwa 8 insgesamt, also Reihen × Kategorien). Bei
  mehr baust du das Diagramm trotzdem, nur ohne `show_values`: Die Zahlen stehen in der Tabelle, die Beschriftungen
  würden sich überlappen. Eine Beschriftung zeigt nur den Wert, ohne Reihen- oder Kategorienamen.
- **Zum Ausfüllen gedacht:** Eine neue Arbeitsmappe, die andere ausfüllen sollen, bekommt eine kurze Legende (welche
  Zellen ausgefüllt werden) und eine Beispielzeile mit realistischen Werten. In eine Datei, die du nur bearbeiten
  sollst, kommt keine solche Zeile.
- **Druck:** `preset: "report"` schaltet das Gitternetz ab und druckt breite Tabellen quer auf eine Seitenbreite; für
  schmalere Blätter setz `options.orientation` / `fit_to_width` bei Bedarf selbst.

**Prüfen vor der Antwort:** Alle Summen sind Formeln, keine Währungszelle ohne Format, das Annahmen-Blatt wird
referenziert, nichts ist fest eingetippt, ein Vergleich hat sein Diagramm. Die Tools speichern Formeln ohne berechnetes Ergebnis (Excel rechnet beim
Öffnen), du siehst also keine Fehlerwerte. Prüf deshalb 2–3 Formeln gegen das `layout` der Antwort, bei Zweifel mit
`read_excel_detailed`: Zeigt jede Adresse auf die richtige Zeile und Spalte? Eine fehlerfreie Formel ist nicht
automatisch richtig; ein um eine Zeile verschobener Bereich rechnet ohne Warnung falsch.

## Tool-Verwendung

### create_excel_from_csv

```json
{
  "csv_content": "Name,Alter\nAlice,30\nBob,25",
  "filename": "people",
  "sheet_name": "Sheet1"
}
```

### create_excel

```json
{
  "data": [
    ["Name", "Alter"],
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

Berichtsbeispiel mit zwei Blättern: eine Übersicht, die aus einem Annahmen-Blatt rechnet, Summen als Formeln,
Währungsformate auf jeder Zahlenzelle (auch Formel- und Summenzellen), eine Notiz und ein Diagramm. Mit `title` steht
die Kopfzeile der Tabelle in **Zeile 4**, die Daten beginnen in **Zeile 5**: schreib jede Formel mit diesen Blattzeilen.

```json
{
  "sheets": [
    {
      "name": "Übersicht",
      "preset": "report",
      "title": "Kostenvergleich Standorte",
      "subtitle": "Stand 25.11.2026 · alle Preise netto",
      "has_headers": true,
      "data": [
        ["Standort", "Angebot A (€)", "Angebot B (€)", "Bemerkung"],
        ["Nord", { "formula": "Annahmen!$B$2*Annahmen!$B$4" }, { "formula": "Annahmen!$B$2*Annahmen!$B$5" }, "Angebot B enthält Montage vor Ort und Schulung"],
        ["Süd", { "formula": "Annahmen!$B$3*Annahmen!$B$4" }, { "formula": "Annahmen!$B$3*Annahmen!$B$5" }, "gleicher Umfang"],
        ["Summe", { "formula": "SUM(B5:B6)" }, { "formula": "SUM(C5:C6)" }, ""]
      ],
      "number_formats": { "B:C": "#,##0 \"€\";-#,##0 \"€\";\"–\"" },
      "cell_styles": {
        "A7:D7": { "bold": true, "borders": { "top": "thin" } }
      },
      "notes": ["Quellen: Angebote vom 20.11.2026; Flächen aus dem Grundriss (Blatt Annahmen)."],
      "charts": [
        {
          "type": "column",
          "title": "Kosten je Standort",
          "labels_range": "A5:A6",
          "data_ranges": ["B5:B6", "C5:C6"],
          "anchor": "A11",
          "show_values": true
        }
      ]
    },
    {
      "name": "Annahmen",
      "has_headers": true,
      "data": [
        ["Parameter", "Wert", "Quelle"],
        ["Fläche Nord (m²)", 1200, "Grundriss"],
        ["Fläche Süd (m²)", 800, "Grundriss"],
        ["Preis Angebot A (€/m²)", 12.5, "Angebot A vom 20.11.2026"],
        ["Preis Angebot B (€/m²)", 11.9, "Angebot B vom 20.11.2026"]
      ],
      "number_formats": { "B2:B3": "#,##0;-#,##0;\"–\"", "B4:B5": "#,##0.00 \"€\"" },
      "cell_styles": { "B2:B5": { "backgroundColor": "F2F2F2" } }
    }
  ],
  "filename": "kostenvergleich"
}
```

Die Eingabezellen `B2:B5` sind hier neutral grau hinterlegt; liefert `get_corporate_ci` ein `colors.primaryLight`,
nimm diesen Wert (ohne `#`).

Die Antwort enthält je Blatt `layout` (`headerRow`, `firstDataRow`, `lastDataRow`, `lastColumn`, `notesRows`): nimm
diese Zeilen für folgende `modify_excel`-Aufrufe.

**Formel-Syntax:** Verwende das Objekt `{"formula": "SUM(A1:A10)"}` – ohne führendes `=`.

**Optionen pro Blatt:**

| Option | Wirkung |
| --- | --- |
| `title`, `subtitle` | Titel in Zeile 1 (fett, CI-Farbe), grauer Untertitel in Zeile 2; die Daten beginnen in Zeile 4 |
| `has_headers` / `header_row` | Erste Datenzeile ist die Kopfzeile (mit Titel Zeile 4); `header_row` = Blattzeile der Kopfzeile, wenn `data` Zeilen darüber hat |
| `preset` | `"report"`: Gitternetz aus, Fixierung und Drucktitel an der Kopfzeile, ab 9 Spalten quer und auf eine Seitenbreite. `"data"`: einfache Tabelle |
| `number_formats` | `{"C5:H14": "…"}` oder ganze Spalten `{"C:H": "…"}` (= die Datenzeilen inkl. Summen) |
| `cell_styles` | Stile nach Bereich wie in `modify_excel` (Füllung, Schriftfarbe, fett, Ausrichtung, `wrapText`, `indent`, `border`, `borders` je Seite) |
| `merge_cells`, `row_heights` | `["A10:D10"]`, `{"5": 58}` (Punkt) |
| `notes` | Notizen/Quellen unter der Tabelle, jede als verbundene, umbrochene graue Zeile |
| `options` | `freeze` ("A5" = Zeilen 1–4 bleiben stehen; "B5" fixiert zusätzlich Spalte A), `show_gridlines`, `orientation`, `fit_to_width`, `print_title_rows` ("4:4"), `tab_color` |
| `charts` | Native Excel-Diagramme, die Zellen lesen: `type` (`column` = Säulen, `bar` = Balken, `stacked_column`, `line`, `area`, `pie`, `doughnut`), `labels_range`, `data_ranges` (gleich lang, auch `'Anderes Blatt'!B5:B8`), `anchor` (Zelle oben links unter der Tabelle), optional `title`, `series_names`, `show_values`, `width`/`height` in cm |
| `table_style` | `"none"` schaltet den Standard-Tabellenlook ab (Rahmen, Zebrastreifen, Umbruch langer Texte) |
| `column_widths`, `auto_filter`, `protected`, `conditional_formatting` | wie bisher |

Ohne `column_widths` richten sich die Spaltenbreiten nach dem Inhalt (höchstens 60; längerer Text wird umbrochen, die
Zeile wird höher). Eine Formelzelle ohne Zahlenformat übernimmt das Format ihrer Spalte, wenn alle Zahlen dort dasselbe
haben.

**Bedingte Formatierung – Typen:** `greaterThan`, `lessThan`, `equal`, `between`, `containsText`, `duplicateValues`

**Weitere Optionen:** Auf oberster Ebene `named_ranges` und `properties` (`{title, subject, author, company}`). Einzelne Zellen können auch erweiterte Objekte sein: `{"value": ..., "comment": ..., "validation": ..., "style": ..., "numberFormat": ...}`. Ein solches Objekt braucht `value` (plus mindestens einen der anderen Schlüssel); eine Formel gehört **in** `value`, nicht daneben: `{"value": {"formula": "SUM(A1:A3)"}, "comment": "Summe"}`. Ein `formula`-Schlüssel neben `value` und `comment` wird ignoriert; ein Objekt ohne `value` (z. B. `{"formula": …, "comment": …}`) wird als reine Formel geschrieben, seine übrigen Schlüssel entfallen. Für viele Zellen nimm lieber die Bereichsoptionen (`number_formats`, `cell_styles`) statt Objekten je Zelle: Das kostet weit weniger Tokens.

### modify_excel

Bearbeitet eine bestehende Excel-Datei. Gib das Ziel mit `document_id` an (wird **direkt** aktualisiert – gleiche ID) **oder** mit `librechat_file_id` (ein LibreChat-Anhang; ist das Volume nicht beschreibbar, wird die geänderte Kopie als **neues** Dokument gespeichert).

```json
{
  "document_id": "<id aus upload_file oder einem create_excel*-Aufruf>",
  "set_cells": {
    "A1": "Aktualisierter Titel",
    "Sheet2!B5": { "formula": "SUM(B2:B4)" }
  },
  "append_rows": {
    "Sheet1": [["Neue Zeile", 100, 200]]
  },
  "number_formats": { "B2:B100": "#,##0.00" },
  "auto_filter": { "Sheet1": true },
  "add_sheets": [{ "name": "Summary", "data": [["Summe", 500]], "has_headers": false }],
  "delete_sheets": ["OldSheet"],
  "rename_sheets": { "OldName": "NewName" }
}
```

**Ein bestehendes Blatt in den Berichtslook bringen** – ein Aufruf mit Bereichen statt Objekten je Zelle:

```json
{
  "librechat_file_id": "<file_id des Anhangs>",
  "number_formats": { "Kosten!C2:H13": "#,##0 \"€\";-#,##0 \"€\";\"–\"" },
  "cell_styles": {
    "Kosten!A13:H13": { "bold": true, "borders": { "top": "thin" } },
    "Kosten!B2:B12": { "wrapText": true, "verticalAlignment": "top" }
  },
  "merge_cells": ["Kosten!A15:H15"],
  "row_heights": { "Kosten!15": 45 },
  "sheet_options": { "Kosten": { "freeze": "A2", "show_gridlines": false, "orientation": "landscape", "fit_to_width": true } }
}
```

`cell_styles` ändert nur die angegebenen Eigenschaften; Werte und die übrige Formatierung bleiben. Vorhandene
Diagramme bleiben erhalten. Hat die Datei schon einen eigenen Stil (Farben, Schriften, Eingabezellen), übernimm ihn statt
des Berichtslooks.

### read_excel

```json
{
  "file_content": "<base64-kodierte xlsx>",
  "include_headers": true,
  "sheet_name": "Sheet1"
}
```

Akzeptiert genau eines von `file_content` (base64), `librechat_file_id` oder `document_id` (am häufigsten – zum Lesen einer zuvor erstellten/gespeicherten Datei). `sheet_name` ist optional.

`read_excel` und `read_excel_detailed` lesen `.xlsx`-Arbeitsmappen. Für `.xls`, `.xlsb` oder `.ods` verwende `read_file` aus dem **file-management-skill** (nur wo verfügbar) – es liefert den Inhalt als Markdown.

### read_excel_detailed

```json
{
  "document_id": "<id der gespeicherten xlsx>",
  "include_headers": true,
  "sheet_name": "Sheet1"
}
```

Dieselben Eingabeoptionen wie `read_excel` (`file_content` / `librechat_file_id` / `document_id`, optional `sheet_name`). Liefert Werte, Formeln, Kommentare, Validierungsregeln, Hyperlinks, benannte Bereiche, verbundene Zellen und Eigenschaften der Arbeitsmappe.

## Optional: Wenn Code-Ausführung verfügbar ist — angehängte Tabellen auswerten

Für Berechnungen, Filter, Gruppierungen, Pivots, Statistik oder Diagramme auf einer angehängten CSV/XLSX ist Code-Ausführung zuverlässiger, als Werte zu lesen und im Kopf zu rechnen.

1. Der Anhang liegt in der Sandbox unter `/mnt/data/<dateiname>` (prüfen mit `os.listdir("/mnt/data")`).
2. Zuerst `import pandas`; fehlt es, nimm die Alternative. Laden mit `pd.read_excel(pfad, sheet_name=None)` (alle Blätter) oder `pd.read_csv(pfad, sep=None, engine="python")`; deutsche Exporte brauchen oft `decimal=","` und `thousands="."`.
3. Sieh dir Form, Spalten und Datentypen an, bevor du rechnest. Berichte die Zahlen aus der Code-Ausgabe, keine Schätzungen.
4. Ergebnis als Datei: Für eine formatierte Arbeitsmappe im Corporate Design übergib die Ergebnistabelle an `create_excel_advanced` / `create_excel_from_json`. Eine in der Sandbox geschriebene Datei (unter neuem Namen in `/mnt/data/` speichern, nie die Eingabe überschreiben) kommt als Chat-Anhang zurück, aber ohne die companyFILES-CI – gestaltest du sie in der Sandbox selbst (openpyxl), rufe vorher `get_corporate_ci` auf und übernimm Schrift, Farben und Seitenformat.

**Ohne Code-Ausführung:** `read_excel { "librechat_file_id": "<file_id>" }` (bei großen Arbeitsmappen je Blatt mit `sheet_name`), aus den gelieferten Werten Schritt für Schritt rechnen und die Zwischenergebnisse zeigen. Für ein Diagramm `show_interactive_chart` / `create_chart_document` (**charts-diagram-skill**). Ist die Datei zu groß, um sie vollständig zu lesen, sag das und werte ein benanntes Blatt oder einen Bereich aus.

### Die Arbeitsmappe selbst in der Sandbox bauen

Die companyFILES-Tools decken Titelbereich, Formate, Diagramme und Druckeinstellungen ab, nimm also bevorzugt
`create_excel_advanced`. Baust du trotzdem eine Arbeitsmappe mit openpyxl (z. B. für einen Diagrammtyp, den das Tool
nicht kennt), gelten dieselben Gestaltungsregeln und:

1. Rufe zuerst `get_corporate_ci` auf und nimm Schrift und Farben daraus; was unter `notConfigured` steht, bleibt
   neutral (Schwarz, Grautöne).
2. Setz `number_format` selbst auf **jede** Zahlenzelle, auch Formel- und Summenzellen (openpyxl übernimmt keine
   Formate, ein Datum erscheint sonst als `45337`, 30 % als `0.3`).
3. `ws.sheet_view.showGridLines = False`; bei breiten Blättern `ws.page_setup.orientation = "landscape"`,
   `ws.page_setup.fitToWidth = 1`, `ws.page_setup.fitToHeight = 0`, `ws.sheet_properties.pageSetUpPr.fitToPage = True`;
   unter der Kopfzeile fixieren (`ws.freeze_panes = "A5"`, Spalten nur nach der Regel oben).
4. Diagramme: `chart.roundedCorners = False`, `chart.legend.overlay = False` und bei jedem gesetzten Titel
   `.overlay = False` (`chart.title`, `chart.x_axis.title` …); bei Diagrammen mit Achsen (nicht Kreis/Ring)
   `chart.x_axis.delete = False` und `chart.y_axis.delete = False`. Sonst legt Excel Titel oder Legende über die
   Fläche, rundet den Rahmen ab oder blendet die Achsen aus. Datenbeschriftungen (nur bei wenigen Balken, siehe oben)
   immer vollständig angeben, denn fehlende Schalter liest Excel als „an“ und schreibt dann Reihe, Kategorie und
   Legendensymbol an jeden Balken:
   `DataLabelList(showVal=True, showSerName=False, showCatName=False, showLegendKey=False, showPercent=False,
   dLblPos="outEnd")` (bei Kreis/Ring ohne `dLblPos`), dazu `chart.dataLabels.numFmt = '#,##0 "€"'` ohne
   Nachkommastellen.
5. Stolperfallen: Bei verbundenen Zellen nur die Zelle oben links beschreiben. Eine mit `data_only=True` geladene
   Mappe nie speichern, das ersetzt alle Formeln durch feste Werte; zum Lesen von Formeln *und* Werten zweimal laden.
   `.xlsm` mit `keep_vba=True` laden, sonst gehen die Makros verloren.
6. Ist LibreOffice verfügbar (`soffice`), rechne vor der Übergabe neu, damit die Formelergebnisse gespeichert sind,
   und such im Ergebnis nach Fehlerwerten (`#REF!`, `#DIV/0!`, `#NAME?`, `#VALUE!`); gib keine Datei mit Fehlerwerten
   heraus. Ohne LibreOffice sag, dass die Werte erst nach dem Öffnen in Excel erscheinen.

## Wichtige Hinweise

- Alle Erstell-Tools liefern `{id, filename, downloadUrl, markdownLink}` (plus `librechat_file_id`, wenn das Dokument zusätzlich als Chat-Datei gespeichert wird) – gib in der Antwort immer `markdownLink` aus.
- `modify_excel` benötigt eine `document_id` oder `librechat_file_id`, die auf eine `.xlsx`-Datei zeigt; ist der Dokumenttyp nicht Excel, gibt es einen Fehler. Ein Chat-Anhang (`librechat_file_id`) wird nach Möglichkeit direkt aktualisiert – die Antwort enthält dann `librechat_file_id`, `filename`, `modifications` und `message`, aber keinen Download-Link. Andernfalls wird die geänderte Kopie als neues Dokument mit neuer `id` und `markdownLink` gespeichert.
- Blattnamen müssen zur Arbeitsmappe passen – rufe zuerst `read_excel` auf, um sie zu sehen; ein unbekannter Name führt zu einem Fehler, der die vorhandenen Blätter auflistet.
- Zelladressen unterstützen ein Blatt-Präfix: `"Sheet2!B3"`.
- Bereiche in `number_formats`, `cell_styles`, `merge_cells` und `row_heights` nutzen Blattzeilen. Mit `title` ist die Kopfzeile Zeile 4; sieh im `layout` der Antwort nach.
- Die CI der Organisation bzw. des Benutzers wird automatisch angewendet, wenn sie in den Einstellungen konfiguriert ist: Farben, Schrift, Seitenformat und -ausrichtung, Kopf-/Fußzeile mit Seitenzahlen und der Firmenname in den Dateieigenschaften. Ein Logo setzt Excel nicht.
- Um eine Vorlage mit `{{placeholder}}`-Syntax auszufüllen, verwende stattdessen `fill_excel_template` aus dem **templates-skill**.
