---
name: de-templates
description: 'Erstelle Dokumente aus Vorlagen mit companyFILES MCP-Tools. Verwende diesen Skill, wenn eine Vorlage ausgefüllt, eine Firmenvorlage oder ein Briefkopf verwendet, ein Dokument aus einem vordefinierten Layout erstellt, Platzhalter befüllt, eine Rechnungsvorlage ausgefüllt oder aus einer DOCX-/XLSX-/POTX-/ODT-Vorlage erstellt werden soll. Deckt Word-, Excel-, ODT- und PowerPoint-Vorlagen ab, inklusive Bildplatzhaltern, der Bildbibliothek (Stockfotos, Key Visuals, Icons als `img:<name>`) und Schleifen-/Wiederholungssyntax, sowie die Übergabe einer Vorlage an den Code-Interpreter für Änderungen, die die Vorlagen-Tools nicht können.'
---

# Vorlagen-Skill

Tools zum Auflisten und Ausfüllen von Dokumentvorlagen (Word, Excel, ODT, PowerPoint).

## Tools in diesem Skill

| Tool                                    | Zweck                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `list_templates`                        | Alle verfügbaren Vorlagen (persönlich + global) mit Platzhalter-Infos auflisten                   |
| `create_word_from_template`             | DOCX-Vorlage mit `{placeholder}`-Syntax ausfüllen                                                 |
| `create_word_from_template_with_images` | DOCX-Vorlage mit Text- und Bildplatzhaltern ausfüllen                                             |
| `create_excel_from_template`            | XLSX-Vorlage per Zelladresse **oder** `{{placeholder}}`-Name ausfüllen (automatisches Routing)    |
| `fill_excel_template`                   | XLSX-Vorlage mit `{{placeholder}}`-Syntax ausfüllen                                               |
| `create_odt_from_template`              | ODT-Vorlage mit `{{placeholder}}`-Syntax ausfüllen                                                |
| `create_powerpoint_from_template`       | POTX/PPTX-Vorlage mit Text, Bildern, Diagrammen, Sprechernotizen und Folienwiederholung ausfüllen |
| `attach_template_to_chat`               | Kopie einer Vorlage für den Code-Interpreter an den Chat hängen                                   |
| `list_image_templates`                  | Bildbibliothek (Bildvorlagen) nach `img:<name>`-Verweisen durchsuchen                             |

## Ablauf

1. **Vorlagen ermitteln:** Rufe `list_templates` auf (optional nach `type` filtern: `docx`, `xlsx`, `potx`, `odt`, `pdf`, `image`)
2. **Platzhalternamen** aus der Antwort notieren
3. **Vorlage ausfüllen** mit dem passenden `create_*_from_template`-Tool
4. **Nur wenn die Vorlagen-Tools es nicht können** (Massen- oder freie Änderungen im Layout der Vorlage) und Code-Ausführung verfügbar ist: `attach_template_to_chat`, dann per Code bearbeiten (siehe unten)

## Verwendung der Tools

### list_templates

```json
{
  "type": "potx"
}
```

Liefert pro Vorlage: `name`, `displayName`, `description`, `category`, `tags`, Platzhalterlisten, `loopSources`, `fields` (bei PDF-Formularvorlagen), `size`, `isDefault`, Upload-Daten und den Geltungsbereich (`"user"` persönlich oder `"global"`).

Bei **POTX/PPTX**-Vorlagen enthält die Antwort eine Aufschlüsselung pro Folie (`slideInfo`):

- `slideNumber` — Folienindex, beginnend bei 1
- `layoutName` — Name des PowerPoint-Layouts (z. B. `"Title Slide"`, `"Two Content"`)
- `layoutType` — Wert aus einem `{{slide_type:xxx}}`-Marker auf dieser Folie (z. B. `"section"`, `"default"`, `"text-image"`)
- `textPlaceholders` — `{{key}}`-Platzhalter auf dieser Folie
- `imagePlaceholders` — `{%name}`-Platzhalter auf dieser Folie
- `chartPlaceholders` — `{{name}}`-Platzhalter für Diagrammcontainer auf dieser Folie

Nutze diese Aufschlüsselung, um vor dem Aufruf von `create_powerpoint_from_template` genau zu wissen, welcher Platzhalter auf welche Folie gehört. Filtere mit `type`, um die Ergebnisse einzugrenzen: `"docx"`, `"xlsx"`, `"potx"`, `"odt"`, `"pdf"`, `"image"`. Bildvorlagen (die Bildbibliothek) erscheinen nur mit `type: "image"`; ein passendes Bild findest du mit `list_image_templates` (siehe unten).

---

### Bildbibliothek (Bildvorlagen)

Admins laden Organisationsbilder (Stockfotos, Key Visuals, Icons) in der companyFILES-Oberfläche unter Vorlagen → Hochladen hoch, Nutzer ihre eigenen (PNG, JPEG, WebP, GIF, TIFF, BMP; kein SVG). Ein persönliches Bild verdeckt ein Organisationsbild mit demselben Namen. Finde sie mit `list_image_templates`:

```json
{ "search": "team büro", "orientation": "landscape", "aspect_ratio": 1.78, "limit": 10 }
```

Alle Argumente sind optional: `search` (alle Wörter müssen in Name, Beschreibung oder Schlagwörtern vorkommen), `tag`, `orientation` (`landscape`, `portrait`, `square`), `aspect_ratio` (Breite/Höhe; sortiert die nächsten zuerst), `limit`. Jedes Ergebnis hat `ref` (`"img:<name>"`), `description`, `tags`, `width`, `height`, `aspectRatio` und `orientation`. Einen Kandidaten siehst du dir mit `view_image { "image_template": "<name>" }` an.

Verwende das Bild als `img:<name>` überall, wo ein Bild angenommen wird (`slides[].image`, Layout-`images`, Markdown `![alt](img:<name>)`), oder als `image_template` in den `{%name}`-Bildobjekten von Word- und PowerPoint-Vorlagen. Wähle ein Bild, dessen `aspectRatio` nah am Seitenverhältnis des Zielbereichs liegt, damit wenig beschnitten wird. Ein unbekannter Name bricht den Aufruf mit einem Fehler ab, der den Verweis nennt.

---

### create_word_from_template

Platzhaltersyntax: `{placeholder}` (einfache geschweifte Klammern). Punktpfade: `{user.name}`.

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

**Tabellenschleifen-Syntax** (FOR/END-FOR jeweils in eine eigene Tabellenzeile setzen):

```
{FOR item IN items}
{= $item.name} | {= $item.qty} | {= $item.price}
{END-FOR item}
```

Übergib `items` als Array in `data`. Fehlende Schleifenquellen werden stillschweigend mit einer Warnung übersprungen.

**Vorlagenausdrücke sind kein JavaScript.** Innerhalb von `{…}`-Befehlen funktionieren nur Datenpfade (`$item.price`, `rows[0]`), Literale, Operatoren (`+ - * / %`, Vergleiche, `&& || ??`, `cond ? a : b`), die Befehle `FOR`, `IF` und `EXEC` sowie eine kurze Allowlist von Hilfsfunktionen — z. B. `toFixed`, `toUpperCase`, `join`, `toLocaleDateString`, `Math.round`, `parseFloat`, `new Date(…)`. Arrow Functions, `.map`/`.filter`, Schleifen und Template-Literale lassen das Ausfüllen fehlschlagen — berechne solche Werte vorab und übergib sie in `data`.

---

### create_word_from_template_with_images

Unterstützt Textplatzhalter `{name}` und Bildplatzhalter `{IMAGE logo}` oder die Kurzform `{%logo}` (in einem Zug tippen, sonst teilt Word ihn auf und er bleibt als Text stehen).

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

Bild aus einem gespeicherten Dokument oder aus der Bildbibliothek (kein erneuter Upload nötig):

```json
{
  "logo": { "document_id": "abc12345-...", "width": 4, "height": 2 },
  "hero": { "image_template": "office-team", "width": 16, "height": 9, "fit": "cover" }
}
```

Bildwerte: `{data, extension}` oder `{document_id | librechat_file_id | image_template}`. `width`/`height` (cm) sind optional und bilden einen Rahmen: Das Bild behält darin sein Seitenverhältnis (`fit: "contain"`, Standard), `"cover"` schneidet es auf den Rahmen zu, `"stretch"` verzerrt (nur auf Wunsch). Nur eine der beiden Angaben skaliert die andere mit; keine Angabe = natürliche Größe, höchstens 16 cm breit. `create_word_from_template` nimmt dieselben Bildobjekte.

Das Organisations-/Benutzerlogo wird **automatisch eingefügt**, aber nur in einen Platzhalter, der exakt `logo` heißt (also `{%logo}`) — und nur, wenn es in den Einstellungen konfiguriert ist und kein `logo`-Wert übergeben wird. Anders benannte Bildplatzhalter (z. B. `{%companyLogo}`) werden **nicht** automatisch befüllt. Das Logo behält sein Seitenverhältnis (im Rahmen 4 × 2 cm).

---

### create_excel_from_template

Akzeptiert in `cell_values` **entweder** Zelladressen (z. B. `"A1"`, `"Sheet2!B3"`) **oder** `{{placeholder}}`-Namen (den reinen Namen ohne `{{ }}` übergeben) — das Tool routet automatisch anhand der übergebenen Schlüssel; bei gemischten Schlüsseln gilt der Platzhaltermodus. Mit `list_templates` siehst du die verfügbaren XLSX-Vorlagen.

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

Befüllt Zellen per `{{placeholder}}`-Syntax — Formatierung, Stile, Formeln und Diagramme bleiben erhalten.

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

Befüllt `{{placeholder}}`-Syntax in ODT-Vorlagen.

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

Platzhaltersyntax:

- **Text:** `{{key}}` an beliebiger Stelle in einem Textfeld
- **Bild:** `{%name}` im **Alternativtext** (`descr`-Attribut) einer Bildform
- **Diagramm:** `{{name}}` im **Alternativtext** einer Diagrammcontainer-Form
- **Layout-Marker:** `{{slide_type:default}}`, `{{slide_type:section}}`, `{{slide_type:text-image}}` — unsichtbarer Metadaten-Marker; legt den Layouttyp der Folie für das `repeat`-Routing (Multi-Source) fest. Wird in der Ausgabe automatisch entfernt. Die Layout-nativen Tools (`create_powerpoint_from_layouts`, `add_slides_from_layouts`) ignorieren ihn.

Führe immer zuerst `list_templates` aus — bei POTX/PPTX liefert es eine Aufschlüsselung pro Folie mit `layoutName`, `layoutType` (aus dem `{{slide_type:xxx}}`-Marker) und den Text-/Bild-/Diagrammplatzhaltern, die zu jeder Folie gehören.

> **Enthält die POTX/PPTX-Vorlage KEINE `{{}}`-Platzhalter** und übergibt der Aufruf keine `images`, `charts` oder `speaker_notes`, lehnt dieses Tool den Aufruf ab und nennt stattdessen die Layout-Tools — `list_templates` kennzeichnet solche Vorlagen mit `hasLegacyPlaceholders: false` und einem `nextStep`-Hinweis. Corporate-Design-Folienmaster von Designteams enthalten meist überhaupt kein `{{}}`-Markup — sie bringen stattdessen benannte Folienlayouts mit. Führe `describe_pptx_template { "template_name": "..." }` aus: Ist `hasLegacyPlaceholders` `false`, wechsle zu `create_powerpoint_from_layouts` (siehe **de-powerpoint**, "corporate master without `{{}}`"). Bitte den Nutzer nie, `{{}}`-Marker in einen Corporate-Master einzutippen. Haben auch seine Layouts keine Text-Slots und liegen die Inhaltsbereiche als einfache Textfelder mit Blindtext auf Musterfolien („Text“, „XXX“, „TITEL“), ist das Weg D im **de-powerpoint** (Code-Ausführung). Dasselbe gilt für eine Word-Vorlage ohne `{{}}` (Blindtext, Textfelder, Inhaltssteuerelemente): siehe **de-word-odt**, „Firmendokument ohne `{{Platzhalter}}` befüllen“.

**Grundlegende Verwendung (Befüllung mit einem Datensatz):**

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

Die Schlüssel von `speaker_notes` sind Foliennummern, **beginnend bei 1**.

`charts` benennt nur die Datenreihen des Diagramms um (`datasets[].label`). `labels` und `values` werden **noch nicht** übernommen — der Server protokolliert sie als "not yet implemented", und das Diagramm behält die Daten der Vorlage. Versprich dem Nutzer keine aktualisierten Diagrammwerte.

Bildquellen je `images`-Eintrag: `base64`, `document_id`, `librechat_file_id` oder `image_template` (Bildbibliothek, z. B. `{ "image_template": "office-team" }`). Das Bild wird in den Rahmen des Platzhalterbildes eingepasst, nie verzerrt: `fit` je Bild, Standard `"cover"` (füllt den Rahmen, mittiger Beschnitt), `"contain"` für Namen mit „logo“ (ganzes Bild, mittig); `"stretch"` nur auf Wunsch.

In PowerPoint-Vorlagen wird kein Logo automatisch platziert: Nur `{{company_name}}` wird automatisch aus den Einstellungen befüllt. Um ein Logo anzuzeigen, übergib es explizit in `images` (z. B. `"logo"` für `{%logo}`).

Das Tool akzeptiert nur `template_name` — kein `document_id` / `librechat_file_id`. Ein im Chat angehängtes `{{}}`-Deck muss zuerst als Vorlage hochgeladen oder im Klonmodus bearbeitet werden (siehe **de-powerpoint** §2a).

**Single-Source-Wiederholung** (eine Folie pro Datensatz duplizieren):

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

`repeat.slide` ist die zu duplizierende Foliennummer (beginnend bei 1); die Folie wird durch N Kopien ersetzt, eine pro Datensatz. Standardmäßig werden Folien, die **nicht** wiederholt werden, aus der Ausgabe entfernt — setze `repeat.keep_unused_slides: true`, um sie zu behalten. `create_powerpoint_from_template` akzeptiert außerdem `title` und `author` auf oberster Ebene.

**Multi-Source-Wiederholung** (jeden Datensatz an die Folie mit passendem `slide_type` leiten):

Verwende dies, wenn die Vorlage mehrere mit `{{slide_type:xxx}}` markierte Layoutfolien enthält und jeder Datensatz ein anderes Layout nutzen soll.

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

Lass `repeat.slide` beim `slide_type`-Routing weg — die passende Vorlagenfolie wird automatisch über ihren `{{slide_type:xxx}}`-Marker gefunden. Die `slide_type`-Werte (`default`, `section`, `text-image`) entsprechen denselben Layoutnamen wie in `create_powerpoint`.

---

### attach_template_to_chat

Hängt eine Kopie einer Vorlage (persönlich oder global) als Datei an den aktuellen Chat, damit der Code-Interpreter sie mit Python öffnen und bearbeiten kann — für Änderungen, die die `create_*_from_template`-Tools nicht können (z. B. einen Begriff im ganzen Dokument inklusive Tabellen und Fußzeilen ersetzen, viele Tabellenzeilen im Stil der Vorlage anfügen, ein Tabellenblatt neu aufbauen, Folien aus den Layouts des Masters anlegen).

| Parameter | Typ | Pflicht | Beschreibung |
| --- | --- | --- | --- |
| `name` | string (max. 100) | ja | Vorlagenname genau wie von `list_templates` geliefert |
| `type` | `docx` \| `xlsx` \| `potx` \| `odt` | ja | Vorlagentyp wie von `list_templates` geliefert (kein `pdf`) |

```json
{ "name": "invoice", "type": "docx" }
```

- **Voraussetzungen:** Code-Ausführung muss für den Chat oder Agenten aktiviert (und für die Rolle des Nutzers erlaubt) sein, und die Umgebung muss companyFILES-Dokumente als LibreChat-Dateien speichern. Sonst antwortet das Tool mit einem Fehler — bleib dann bei den Vorlagen-Tools.
- **Nächster Zug:** Die Datei erreicht den Code-Interpreter erst ab der **nächsten** Nachricht des Nutzers (meist unter `/mnt/data/<name>.<type>`), nicht in derselben Antwort. Sag dem Nutzer, dass die Vorlage angehängt ist, und bitte ihn um seine nächste Nachricht (z. B. „weiter“).
- Eine `potx`-Vorlage wird als `<name>.pptx` angehängt, damit python-pptx sie direkt öffnet.
- Ein erneuter Aufruf ist günstig: Eine unveränderte Vorlage hängt dieselbe Datei wieder an, eine geänderte ersetzt die alte Kopie. Die Vorlage selbst bleibt unverändert.
- Meldet das Tool, dass die Übergabe noch läuft, rufe es nach etwa 30 Sekunden mit denselben Angaben erneut auf — es entsteht keine zweite Kopie.

#### Wenn Code-Ausführung verfügbar ist: Vorlage mit Python bearbeiten

1. Prüfe, ob die Datei da ist (`/mnt/data/`) und die Bibliothek lädt (`import docx` / `openpyxl` / `pptx`).
2. Fügst du neue Inhalte hinzu (Abschnitte, Tabellen, Folien), die die Vorlage nicht gestaltet, rufe vorher `get_corporate_ci` auf und übernimm Farben, Schriften und Größen der CI; wo die Vorlage Stile vorgibt, bleibt die Vorlage maßgeblich.
3. Ändere Text innerhalb der vorhandenen Runs/Zellen, damit das Layout bleibt; überschreibe nie die Eingabe — speichere das Ergebnis unter neuem Namen in `/mnt/data/`, es kommt als Chat-Anhang zurück.
4. Öffne das Ergebnis erneut und prüfe auf übrig gebliebene Platzhalter, bevor du Erfolg meldest.

Das ausführliche Rezept (Code für Word, Excel, PowerPoint, Stolperfallen wie verlorene Diagramme bei openpyxl) steht in der mitgelieferten Datei `references/code-template-editing.md` — lies sie mit dem eingebauten `read_file`-Tool, Pfad `de-templates/references/code-template-editing.md` (nicht das gleichnamige companyFILES-Tool). Sie ist nur vorhanden, wenn dieser Skill als Paket (zip) installiert wurde; wurde nur `SKILL.md` eingefügt, nutze die vier Schritte oben.

**Ohne Code-Ausführung** (oder wenn Datei oder Bibliothek fehlen): Fülle die Vorlage mit den `create_*_from_template`-Tools oben aus und verfeinere das Ergebnis mit den iterativen Tools unten (`append_to_word`, `replace_word_content`, `append_slides_to_powerpoint` mit `reference_slide`, `modify_excel`). Für ODT gibt es in der Standard-Sandbox keine Python-Bibliothek: nimm `create_odt_from_template`.

## Bearbeitung nach dem Ausfüllen (iterative Aktualisierungen)

Jedes Vorlagen-Tool liefert die `id` des neuen Dokuments. Übergib sie als `document_id` an die iterativen Bearbeitungstools aus **de-word-odt** und **de-powerpoint**, um das ausgefüllte Dokument weiter anzupassen, ohne es neu zu erzeugen.

### Nach `create_word_from_template` / `create_word_from_template_with_images`

| Ziel                               | Tool                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------ |
| Aktuellen Inhalt prüfen            | `read_word_content { "document_id": "<id>" }`                                        |
| Weitere Abschnitte am Ende anfügen | `append_to_word { "document_id": "<id>", "content": "...", "add_page_break": true }` |
| Dokument komplett neu schreiben    | `replace_word_content { "document_id": "<id>", "content": "..." }`                   |

Beispiel — Vorlage ausfüllen und anschließend einen eigenen Anhang anfügen:

```json
// Step 1: fill the template
{ "template_name": "report", "data": { "title": "Annual Report" } }
// → returns id "abc123" (use it as document_id)

// Step 2: append extra content
{ "document_id": "abc123", "content": "## Appendix A\n\nAdditional data...", "add_page_break": true }
```

### Nach `create_powerpoint_from_template`

| Ziel                                          | Tool                                                                                                                |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Vorhandene Folien prüfen                      | `read_powerpoint_slides { "document_id": "<id>" }`                                                                  |
| Neue Folien am Ende anfügen                   | `append_slides_to_powerpoint { "document_id": "<id>", "slides": [...] }`                                            |
| Eine bestimmte Folie ersetzen                 | `update_powerpoint_slide { "document_id": "<id>", "slide_number": 3, "slides": [...] }`                             |
| **Folie im Stil der Vorlage anfügen**         | `append_slides_to_powerpoint { "document_id": "<id>", "reference_slide": 2, "placeholders": {...} }`                |
| **Folie ersetzen, Erscheinungsbild behalten** | `update_powerpoint_slide { "document_id": "<id>", "slide_number": 3, "reference_slide": 2, "placeholders": {...} }` |

> **Erscheinungsbild der Vorlage behalten:** Anfügen/Aktualisieren mit `slides`/`markdown` rendert das generische Theme, das **nicht** zu einem Vorlagen-Deck passt. Verwende stattdessen `reference_slide` + `placeholders` (Klonen und Neubefüllen) — damit wird das Design einer vorhandenen Folie kopiert und ihre `{{placeholders}}` neu befüllt. Details siehe **de-powerpoint**. (Der Klonmodus befüllt nur Textplatzhalter neu; für Bildplatzhalter führe `create_powerpoint_from_template` erneut aus.)

Beispiel — Vorlage ausfüllen und anschließend eine eigene Abschlussfolie anfügen:

```json
// Step 1: fill the template
{ "template_name": "corporate_deck", "placeholders": { "title": "Q4 Results" } }
// → returns id "def456" (use it as document_id)

// Step 2a: add a generic (non-template-styled) closing slide
{ "document_id": "def456", "slides": [{ "type": "section", "title": "Thank You", "subtitle": "Questions?" }] }

// Step 2b: OR add a slide that matches the template by cloning slide 2 and refilling it
{ "document_id": "def456", "reference_slide": 2, "placeholders": { "title": "Next Steps", "owner": "PMO" } }
```

## Wichtige Hinweise

- Alle Erstellungstools liefern `{id, filename, downloadUrl, markdownLink}` — gib `markdownLink` immer in der Antwort aus.
- Wird `filename` weggelassen, erhält das ausgefüllte Dokument den Namen von `template_name` (`create_word_from_template_with_images`: `document`).
- `create_word_from_template_with_images` greift auf eine globale `default.docx` zurück, wenn die angegebene Vorlage fehlt, `create_word_from_template` dagegen nicht — prüfe mit `list_templates` vorab, ob die Vorlage existiert.
- Vorlagennamen unterscheiden **Groß- und Kleinschreibung** — prüfe sie immer zuerst mit `list_templates`.
- Benutzervorlagen haben Vorrang vor globalen Vorlagen mit demselben Namen.
- `replace_missing: false` (Standard) lässt nicht befüllte `{{placeholder}}`-Tokens unverändert; `true` ersetzt sie durch einen leeren String.
- Warnungen zu fehlenden Platzhaltern sind gegebenenfalls in der Antwort enthalten.
- Nutze nach dem Ausfüllen die iterativen Tools (`append_to_word`, `append_slides_to_powerpoint` usw.), um Inhalte hinzuzufügen oder zu aktualisieren — die `document_id` bleibt dabei durchgehend gleich.
- `attach_template_to_chat` ist der Ausnahmeweg für Änderungen, die die Vorlagen-Tools nicht können; er braucht Code-Ausführung und wirkt ab der nächsten Nachricht des Nutzers.
