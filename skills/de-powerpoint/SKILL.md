---
name: de-powerpoint
description: 'Erstellt und überarbeitet PowerPoint-Präsentationen (.pptx) mit companyFILES MCP-Tools. Verwenden, wenn eine Präsentation erstellt, Folien ergänzt oder korrigiert, ein Corporate-Folienmaster verwendet oder mit einer im Chat angehängten .pptx gearbeitet werden soll („mach einen Foliensatz in diesem Design“, „ergänze Folien“). Deckt alle Wege ab: von Grund auf (create_powerpoint), aus einer {{placeholder}}-Vorlage (create_powerpoint_from_template), aus einem Corporate-Master ohne Platzhalter über seine Folienlayouts (describe_pptx_template, create_powerpoint_from_layouts, add_slides_from_layouts, set_powerpoint_slide_fields) und aus einem Design-Deck, dessen Musterfolien nur Textfelder mit Blindtext haben („Text“, „XXX“, „TITEL“; per Code-Ausführung). Dazu iteratives Bearbeiten (append_slides_to_powerpoint, update_powerpoint_slide, read_powerpoint_slides), Klonen von Vorlagenfolien, Tabellen, Sprechernotizen, Bilder und Diagramme.'
---

# PowerPoint Skill

Alles, was du brauchst, um `.pptx`-Foliensätze zu erstellen, zu erweitern und zu reparieren.

## Tool-Übersicht

| Tool                              | Zweck                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| `create_powerpoint`               | Neuer Foliensatz aus Markdown oder einem typisierten `slides`-Array (eigenes Design) |
| `create_powerpoint_from_template` | Neuer Foliensatz aus einer POTX/PPTX-Vorlage mit `{{placeholders}}`                  |
| `describe_pptx_template`          | Liest die **nativen Folienlayouts** eines Foliensatzes – kein `{{}}` nötig           |
| `create_powerpoint_from_layouts`  | Neuer Foliensatz durch Instanziieren dieser nativen Layouts (Corporate Design)       |
| `add_slides_from_layouts`         | Hängt layout-native Folien an einen bestehenden Foliensatz an, **direkt in der Datei** |
| `set_powerpoint_slide_fields`     | Ändert die nativen Platzhalter einer Folie (Text + Bilder) direkt in der Datei       |
| `append_slides_to_powerpoint`     | Hängt Folien an einen bestehenden Foliensatz an, direkt in der Datei                 |
| `update_powerpoint_slide`         | Ersetzt eine Folie eines bestehenden Foliensatzes, direkt in der Datei               |
| `read_powerpoint_slides`          | Liest Foliennummern, Titel, Text **sowie Layout/Slots jeder Folie**                  |
| `list_my_files`                   | Findet einen Foliensatz, den der Nutzer im Chat angehängt hat (`file_id`)            |
| `list_templates`                  | Findet verfügbare Vorlagen (`type: "potx"`) vor dem Erstellen                        |
| `list_image_templates`            | Findet Bilder in der Bildbibliothek (`img:<name>`)                                   |
| `embed_chart_in_document`         | Chart.js-Diagramm als neuer Foliensatz; `title` fügt eine Titelfolie hinzu           |

---

## 1. Iterativ arbeiten – keinen Foliensatz in einem Rutsch erzeugen

**Ein Foliensatz mit mehr als ~6 Folien muss in mehreren Tool-Aufrufen entstehen.** Ein einziger
riesiger `create_powerpoint`-Aufruf ist der häufigste Fehler: Die Argumente werden abgeschnitten,
Layout-Entscheidungen lassen sich nicht korrigieren, und eine einzige fehlerhafte Folie bedeutet,
dass alles neu generiert werden muss.

Der Ablauf:

```
PLAN   → zuerst die Gliederung in deiner Antwort schreiben (Foliennummer, Rolle/Layout, Überschrift, Inhaltsskizze)
PROBE  → describe_pptx_template / list_templates / read_powerpoint_slides – herausfinden, was vorhanden ist
SEED   → create_powerpoint* nur mit den ERSTEN 3–5 Folien → die zurückgegebene id (document_id) merken
EXTEND → append_slides_to_powerpoint (Weg A/B) oder add_slides_from_layouts (Weg C)
         in Paketen von 3–5 Folien, wiederholt
REFINE → set_powerpoint_slide_fields oder update_powerpoint_slide für einzelne Korrekturen
VERIFY → read_powerpoint_slides, um Folienanzahl, Reihenfolge, Titel und übrig gebliebenen Blindtext zu prüfen
```

**Melde einen Foliensatz nie als fertig, bevor du ihn zurückgelesen hast.** Folien, die noch den
Blindtext der Vorlage zeigen („Text“, „XXX“, „TITEL“, „Lorem ipsum“) oder leer herauskommen, sind ein
Fehler, kein Ergebnis. Korrigiere sie oder sag dem Nutzer genau, welche Folien nicht befüllt sind und
warum.

### PLAN vor dem ersten Tool-Aufruf

Zeige dem Nutzer bei allem, was über ein paar Folien hinausgeht, einen Plan und lass ihn reagieren.
Das kostet eine Nachricht und erspart den Neuaufbau eines 20-Folien-Foliensatzes.

```
Plan — "Digitalstrategie 2027" (12 Folien, Corporate-Master `folienmaster`)

 #  Layout / Rolle     Überschrift                   Inhalt
 1  title              Digitalisierungsstrategie 2027 Autor + Datum
 2  section            1. Ausgangslage
 3  content            Kernbefunde                   3 Aufzählungspunkte, 1 eingerückt
 4  two-content        Handlungsoptionen             Option A | Option B
 5  section            2. Zielbild
 …
12  closing            —                             Kontaktblock

Ich erstelle zuerst 1–5 und hänge dann 6–12 in zwei Paketen an. Sag Bescheid, wenn sich die Struktur ändern soll.
```

### Faustregeln

- **Paketgröße 3–5 Folien** pro Aufruf. Bei langen Aufzählungstexten oder `htmlTable`-Inhalten → 2–3.
- **Behalte die `document_id`.** Der erste Erstellungsaufruf gibt die `id` des Foliensatzes zurück;
  jeder Append-/Update-/Patch-Aufruf auf diesen Foliensatz behält _dieselbe_ id. Verwende sie weiter;
  erstelle nie einen zweiten Foliensatz, um den ersten zu reparieren.
- **Eine fehlerhafte Folie → nur diese Folie ändern.** `set_powerpoint_slide_fields` (layout-nativ)
  oder `update_powerpoint_slide` (eigenes Design / Klonmodus). Beide erhalten Folienanzahl und Position.
- **`read_powerpoint_slides` zwischen den Paketen**, wenn du mehrfach angehängt hast, um sicherzugehen,
  dass du die Folien von der richtigen Basis aus nummerierst.
- **Melde den Fortschritt**, z. B. „Folien 1–5 fertig, als Nächstes hänge ich 6–9 an“, und gib den
  zurückgegebenen `markdownLink` aus, damit der Nutzer den Zwischenstand öffnen kann.
- **Nie neu erstellen, um anzuhängen.** `add_slides_from_layouts` / `append_slides_to_powerpoint`
  gibt es genau dafür, dass ein Foliensatz über mehrere Runden wachsen kann.

Jede Folie in einem **typisierten** `slides`-Array (`create_powerpoint`, `append_slides_to_powerpoint`,
`update_powerpoint_slide`) **benötigt einen `title`** (Pflichtfeld, auch bei `section`-Folien) – eine
Folie ohne `title` scheitert an der Validierung. Die `slides` der Layout-Tools haben eine andere
Struktur – `layout`, `fields`, `images`, `notes` – und kein `title`-Feld; ein Titel gehört in
`fields.title`.

---

## 2. Den Erstellungsweg wählen

Entscheide einmal, ganz am Anfang. Werden Wege in einem Foliensatz gemischt, entsteht ein
uneinheitliches Design.

| Situation                                                     | Weg                                     |
| ------------------------------------------------------------- | --------------------------------------- |
| Keine Vorlage erwähnt, companyFILES-Design passt              | **A** `create_powerpoint`               |
| Eine Vorlage existiert **und** enthält `{{key}}`-Markup       | **B** `create_powerpoint_from_template` |
| Ein Corporate-Master / Folienmaster **ohne** `{{}}`-Markup    | **C** `create_powerpoint_from_layouts`  |
| Ein Design-Deck, dessen **Musterfolien** das Design als einfache Textfelder mit Blindtext tragen und dessen Layouts (fast) keine Text-Slots haben | **D** Musterfolien klonen und befüllen (Code-Ausführung, §4a) |

**So unterscheidest du B, C und D:** Führe `describe_pptx_template` auf der Vorlage aus und lies
`hasLegacyPlaceholders`.

- `true` → der Foliensatz verwendet `{{}}` → Weg **B** (siehe auch **de-templates**)
- `false` → sieh dir die `slots` der Layouts an:
  - die Layouts, die du brauchst, haben Text-Slots (`title`, `body:*`, …) → Weg **C**
  - die Layouts haben **keine oder fast keine Text-Slots**, aber `read_powerpoint_slides` (mit
    `include_layouts: false`) zeigt Text auf den eigenen Folien des Decks („Text“, „XXX“, „TITEL“,
    „UNTERTITEL“, „Text 1 … Text 4“, eine Agenda mit „01 XXX“) → Weg **D**. Das Design steckt in den
    Musterfolien, nicht in den Layouts. Eine Layout-Folie aus so einem Master kommt **leer** heraus
    (nur Hintergrund, Logo und Fußzeile), und `set_powerpoint_slide_fields` meldet jeden Key als
    `unknownFields`.
- Gemischte Decks sind häufig: ein Titellayout mit echten Slots, aber Inhaltsfolien als Musterfolien.
  Entscheide pro Folientyp; im Zweifel nimm Weg D für das ganze Deck, damit alle Folien aus derselben
  Quelle stammen.

`list_templates` (`type: "potx"`) listet Kandidaten auf und liefert für `{{}}`-Foliensätze eine
Aufschlüsselung der Platzhalter pro Folie. Den Layout-Katalog liefert es **nicht** – dafür nimmst du
`describe_pptx_template`.

Ein Foliensatz, den der Nutzer im Chat angehängt hat, muss für Weg C nicht als Vorlage hochgeladen
werden – siehe nächster Abschnitt. Weg B ist die Ausnahme: `create_powerpoint_from_template` nimmt
nur einen `template_name` entgegen.

---

## 2a. Der Nutzer hat eine `.pptx` im Chat angehängt

Das ist der Normalfall: Jemand legt seinen Folienmaster oder einen bestehenden Foliensatz in die
Unterhaltung und bittet um eine Präsentation „in diesem Design“ oder darum, den gerade geschickten
Foliensatz zu erweitern. Bei einem Corporate-Master (ohne `{{}}`) **bitte den Nutzer nicht, ihn als
Vorlage hochzuladen** – die Layout-Tools, `read_powerpoint_slides`, `append_slides_to_powerpoint` und
`update_powerpoint_slide` nehmen den Anhang direkt entgegen. `create_powerpoint_from_template` nicht:
Es hat nur `template_name`, kein `document_id` / `librechat_file_id`.

```
FIND    file_id aus dem Block "Attached files in this message:"
        (kein Block: list_my_files → die .pptx anhand des Dateinamens wählen; list_documents /
        search_documents funktionieren auch – die id des Eintrags übergeben)
PROBE   describe_pptx_template { "librechat_file_id": "<file_id>" }
        → hasLegacyPlaceholders entscheidet den Weg (B oder C)
        read_powerpoint_slides { "librechat_file_id": "<file_id>" }, wenn der Foliensatz Inhalte hat,
        die du sehen oder erweitern musst – es meldet Layout und Slot-Keys jeder Folie
        → Layouts ohne Text-Slots + Blindtext auf den Folien = Weg D (§4a)
BUILD   (Weg C)
        neuer Foliensatz → create_powerpoint_from_layouts { "librechat_file_id": ..., "slides": [...] }
        erweitern        → add_slides_from_layouts     { "librechat_file_id": ..., "slides": [...] }
        eine korrigieren → set_powerpoint_slide_fields { "librechat_file_id": ..., "slide_number": n, ... }
```

**Ein angehängter `{{}}`-Foliensatz (Weg B)** hat zwei Wege:

- Um ihn mit `create_powerpoint_from_template` zu befüllen (Bilder, Diagramme, `repeat`), muss er
  zuerst als Vorlage hochgeladen werden (Web-UI, `open_companyfiles_ui page="upload"`); danach rufst du
  das Tool mit diesem `template_name` auf.
- Oder du bearbeitest den Anhang selbst im Klonmodus (§5): `update_powerpoint_slide` mit
  `reference_slide` gleich `slide_number` plus `placeholders` befüllt eine Folie direkt in der Datei;
  `append_slides_to_powerpoint` mit `reference_slide` plus `placeholders` fügt eine befüllte Kopie hinzu.

**`librechat_file_id` und `document_id` sind austauschbare Eingaben.** Der Server löst beide auf,
zuerst über das PVC. Übergib die id, die dir die Auflistung geliefert hat.

**Neuer Foliensatz oder bearbeiteter Foliensatz?** Zwei verschiedene Absichten, zwei verschiedene Tools:

| Der Nutzer möchte                                         | Tool                             | Ergebnis                                                 |
| --------------------------------------------------------- | -------------------------------- | -------------------------------------------------------- |
| Eine Präsentation **im Design** dieses Foliensatzes       | `create_powerpoint_from_layouts` | Ein **neues** Dokument; der Anhang bleibt unverändert    |
| Weitere Folien **in** diesem Foliensatz                   | `add_slides_from_layouts`        | **Derselbe** Foliensatz, direkt in der Datei erweitert   |
| Eine Folie dieses Foliensatzes geändert                   | `set_powerpoint_slide_fields`    | **Derselbe** Foliensatz, eine Folie geändert             |

Bei einem Anhang bedeutet „direkt in der Datei“: Die Datei wird auf dem gemeinsamen LibreChat-Volume
überschrieben, wenn dieses Volume eingebunden ist (gleiche `file_id`); andernfalls wird die geänderte
Kopie als neues companyFILES-Dokument gespeichert. Die `message` in der Antwort sagt, was passiert
ist – gib das weiter, statt dem Nutzer zu versprechen, dass seine Originaldatei geändert wurde.

**Ein aus Markdown erstellter Foliensatz hat keine befüllbaren Layouts.** `add_slides_from_layouts`
lehnt ihn ab und nennt stattdessen `append_slides_to_powerpoint`; diese Ablehnung ist korrekt, umgehe
sie nicht.

---

## 3. Weg A – von Grund auf (`create_powerpoint`)

### Markdown-Modus (schnell, textlastige Foliensätze)

`#` oder `##` beginnt eine neue Folie. Alle Folien erhalten das Layout `default`. Eine Zeile, die
genau `???` enthält, beginnt Sprechernotizen, die bis zur nächsten `#`/`##`-Überschrift reichen.

> **`title` fügt eine Folie hinzu.** Das Top-Level-Argument `title` von `create_powerpoint` stellt
> eine generierte dunkle Titelfolie (Titel, Autor, heutiges Datum) voran. `n` Inhaltsfolien plus
> `title` ergeben also `n + 1` Folien, und jede spätere `slide_number` verschiebt sich um eins. Lass
> `title` weg, wenn du die Eröffnungsfolie selbst gestalten willst. `append_slides_to_powerpoint`
> fügt nie eine hinzu.

```json
{
  "markdown": "# Quarterly Results\n\n- Revenue: €1.2M\n- Growth: 15%\n\n???\nOpen with the revenue number.\n\n## Key Highlights\n\n- Launched new product\n- Expanded to 3 markets",
  "filename": "q4_results",
  "title": "Q4 2025 Results",
  "author": "Strategy Team"
}
```

Inline-Bilder im Markdown von `create_powerpoint` verwenden `doc:<documentId>`, `lc:<file_id>` oder
`img:<name>` (Bildbibliothek, siehe §6):

```markdown
![Chart](doc:abc12345-...)
![Attachment](lc:xyz-librechat-file-id)
![Team](img:office-team)
```

### Modus mit typisierten Folien (Layout-Kontrolle)

Übergib `slides` statt `markdown`. Sind beide angegeben, gewinnt `slides`.

| `type`         | Darstellung                                                  | Felder                                                               |
| -------------- | ------------------------------------------------------------ | -------------------------------------------------------------------- |
| `"default"`    | Akzentbalken + Titel + gestapelter Inhalt                    | `title`, `content`, `bullets`, `code`, `table`, `htmlTable`, `image` |
| `"section"`    | Dunkler Hintergrund, großer zentrierter Titel – Kapiteltrenner | `title`, `subtitle`                                                |
| `"text-image"` | Titel oben, Text/Aufzählung links, Bild rechts               | `title`, `content`, `bullets`, `htmlTable`, `image`, `imageAlt`      |

Jeder Typ akzeptiert zusätzlich `notes` (Sprechernotizen). Unbekannte `type`-Werte fallen auf
`"default"` zurück. Fehlt `image` auf einer `text-image`-Folie, wird ein Skelett-Platzhalterkasten
gezeichnet – nützlich für Entwürfe.

**Titel bleiben einzeilig** (Inhalts-, Titel- und Abschnittsfolien): Ein langer Titel wird kleiner gesetzt (bis
16 pt), einer mit mehr als etwa 60 Zeichen mit „…“ gekürzt. Halte Folientitel kurz und stell Details in den Inhalt.

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

`bullets` ist hier ein flaches `string[]` – für eingerückte Aufzählungen nutzt du Weg C (`level`)
oder eine Vorlage. Das Feld `image` nimmt `lc:<file_id>` (Chat-Anhang oder erzeugtes Bild, siehe
`list_my_files`), `doc:<document_id>`, `img:<name>` (Bildbibliothek), eine base64-Data-URI oder eine
öffentliche http(s)-URL (siehe §6). `imageFit` legt fest, wie es seinen Bereich füllt: `"contain"`
(Standard, ganzes Bild, mittig), `"cover"` (füllt den Bereich, beschneidet) oder `"stretch"` (verzerrt –
nur auf Wunsch). Dasselbe gilt in `append_slides_to_powerpoint` und `update_powerpoint_slide`.

**Natives Diagramm auf einer Folie:** Ergänze `chart` auf einer `default`-Folie (unter dem Text) oder einer
`text-image`-Folie (ersetzt das Bild – nimm `image` **oder** `chart`, nicht beides). Es ist ein echtes,
bearbeitbares PowerPoint-Diagramm („Daten bearbeiten“ öffnet die Zahlen in Excel) in den Farben und der
Schrift der Corporate Identity. `section`-Folien zeigen keines. Die Daten haben dieselbe Form wie bei
`show_interactive_chart`:

```json
{
  "type": "default",
  "title": "Umsatz je Quartal",
  "bullets": ["Q3 ist das stärkste Quartal"],
  "chart": {
    "type": "bar",
    "labels": ["Q1", "Q2", "Q3"],
    "datasets": [{ "label": "2026", "data": [12, 15, 19] }],
    "showValues": true
  }
}
```

`chart.type`: `bar`, `horizontalBar`, `stackedBar`, `line`, `area`, `pie`, `doughnut`, `scatter`, `radar`
(`pie`/`doughnut` zeigen nur die erste Datenreihe). Optional: `title`, `showLegend`, `showValues`,
`numberFormat` (Excel-Format, z. B. `"#,##0"`), `xAxisTitle`, `yAxisTitle`. Grenzen: höchstens 20 Datenreihen
mit je 1000 Punkten; jede Datenreihe braucht genau eine Zahl je Label, sonst bricht das Tool ab und nennt die
Datenreihe. Funktioniert auch in `append_slides_to_powerpoint` und `update_powerpoint_slide`.

### Formatierte Tabellen – `htmlTable`

Verwende `htmlTable` statt `table`, wenn Zellen Farbe, Fettdruck oder Ausrichtung brauchen.
Unterstützt auf `default` und `text-image`; hat Vorrang vor `table`.

| Inline-CSS                        | Wirkung       |
| --------------------------------- | ------------- |
| `background-color: #hex`          | Zellfüllung   |
| `color: #hex`                     | Textfarbe     |
| `font-weight: bold`               | Fett          |
| `font-style: italic`              | Kursiv        |
| `text-align: left\|center\|right` | Ausrichtung   |

`<th>`-Zellen erhalten automatisch Kopfzeilenfüllung/-text des Themes, sofern nicht überschrieben.

```json
{
  "type": "default",
  "title": "Revenue by Region",
  "htmlTable": "<table><tr><th>Region</th><th>Q1</th><th>vs PY</th></tr><tr><td style=\"font-weight:bold\">DACH</td><td>€1.2M</td><td style=\"color:#16A34A\">+18%</td></tr><tr><td style=\"font-weight:bold\">US</td><td>€0.8M</td><td style=\"color:#DC2626\">-3%</td></tr></table>"
}
```

Für ein einfaches Raster reicht `table: string[][]` (erste Zeile = Kopfzeile).

---

## 4. Weg C – Corporate-Master ohne `{{}}` (layout-nativ)

Das ist der Weg für einen Foliensatz, den das Design-Team geliefert hat, z. B. eine
`Corporate-Master.pptx`. Solche Foliensätze enthalten **kein `{{}}`-Markup**, sondern nur benannte
Folienlayouts mit den eigenen Platzhaltern von OOXML. Inhalte werden an diese Platzhalter gebunden
und es wird **keine Formatierung geschrieben**, sodass Schriften, Farben, Logos und Geometrie aus dem
Master stammen. („Folie zurücksetzen“ in PowerPoint ändert nichts – das ist der Beweis.)

Lade einen solchen Master als Vorlage hoch (eine `.pptx` wird als Typ `potx` gespeichert) – oder,
wenn der Nutzer ihn im Chat angehängt hat, verwende direkt seine `librechat_file_id` (Abschnitt 2a).

### Schritt 1 – `describe_pptx_template`

```json
{ "template_name": "folienmaster" }
```

Liefert:

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

So liest du das:

- **`layoutId` ist der stabile Bezeichner.** Layout-**Namen wiederholen sich** über Folienmaster
  hinweg (ein echter Foliensatz hatte `Präsentationstitel` 3× verteilt auf 5 Master). Bevorzuge `layoutId`.
- **Slot-Keys lauten `type` oder `type:idx`.** Der `idx` zählt: `body:12` + `body:13` im selben
  Layout bedeutet ein zweispaltiges Layout – befülle beide, um beide Spalten zu nutzen. Die Nummer
  sagt **nicht**, welcher Kasten links oder oben steht: `body:13` kann die rechte Spalte sein. Prüfe
  die Position (der `at`-Wert von `--lists`, siehe „Listen kommen aus der Vorlage“ unten) oder
  befülle die Spalten mit Texten, deren Reihenfolge egal ist.
- **`role`** wird aus dem Layoutnamen (deutsche + englische Schlüsselwörter) und der Zusammensetzung
  seiner Slots abgeleitet. Rollen: `title`, `title-image`, `section`, `content`, `two-content`,
  `title-only`, `closing`, `reference`. `roleMap` wählt pro Rolle ein Layout.
- **`hint`** ist der eigene Aufforderungstext des Layouts und nur ein Hinweis – echte Master sagen oft
  „Mastertextformat bearbeiten“ oder Lorem ipsum. Urteile nach Name + Slot-Struktur, nicht nach dem Hinweis.
- **`isImage`-Slots (`pic:*`) erhalten ein Bild über das separate Argument `images`**, nicht über
  `fields`. `aspectRatio` (Breite ÷ Höhe des Slot-Rahmens) zeigt dir, was sich gut zuschneiden lässt –
  das Bild wird mittig auf dieses Verhältnis zugeschnitten, nie verzerrt. Aus der Bildbibliothek wählst
  du ein Bild mit ähnlichem `aspectRatio` (`list_image_templates` mit `aspect_ratio`). Ein Slot, für den du kein
  Bild übergibst, bleibt leer und erscheint in `imageSlotsNotFilled`; versprich dem Nutzer dann kein Bild.
- **`acceptsChart`-Slots** (Platzhaltertypen `chart`, `obj`, `body`) erhalten ein natives Diagramm über das
  separate Argument `charts` (siehe „Diagramme“ unten). `read_powerpoint_slides` meldet `acceptsChart` ebenfalls.

### Schritt 2 – `create_powerpoint_from_layouts`

Jede Folie wählt ihr Layout über `layoutId`, Layoutnamen oder Rolle – frei kombinierbar.

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

**Bilder** gehören in ein `images`-Objekt pro Folie, mit Keys wie bei `fields` (exakter Slot-Key, der
bloße Typ `pic` oder die Synonyme `image`/`picture`/`photo`). Als Quellen dienen die üblichen drei:

```json
{
  "layout": "title-image",
  "fields": { "title": "Standort München" },
  "images": { "pic:14": { "librechat_file_id": "abc-attachment-id" } }
}
```

`{ "document_id": "..." }` (ein PVC-Upload), `{ "image_template": "..." }` (Bildbibliothek) und
`{ "base64": "..." }` funktionieren genauso. Das Bild übernimmt Position und Größe aus dem Layout und wird
auf das Seitenverhältnis des Slots zugeschnitten (`cover`). Soll das ganze Bild zu sehen sein, nutze die
Objektform mit `"fit": "contain"` (ein Rahmen im Seitenverhältnis des Bildes, mittig im Slot); `"stretch"`
nur auf Wunsch. Auch einfache Strings gehen: `"images": { "pic:14": "lc:abc-attachment-id" }` (ebenso
`doc:<document_id>`, `img:<name>` oder eine `data:image/…`-URI). Eine nicht auflösbare
`lc:`/`doc:`/`img:`-Referenz bricht den Aufruf ab, der Fehler nennt sie.

**Diagramme** gehören in ein `charts`-Objekt pro Folie, mit Keys wie bei `fields` (exakter Slot-Key wie
`chart:15` oder der bloße Typ; `content`/`chart` nehmen den ersten freien Chart-, Obj- oder Body-Slot).
Das Diagramm füllt den Rahmen des Slots (aus dem Layout, sonst aus dem Folienmaster; ohne Rahmen ein Fehler
mit dem Slot-Namen) in den Theme-Farben (Design → Farben) und der Theme-Schrift des Decks. Ein Slot nimmt ein
Feld **oder** ein Diagramm, nicht beides. Dasselbe Diagrammobjekt wie bei `slides[].chart` oben:

```json
{
  "layout": "Diagramm",
  "fields": { "title": "Umsatz je Quartal" },
  "charts": {
    "chart:15": {
      "type": "bar",
      "labels": ["Q1", "Q2", "Q3"],
      "datasets": [{ "label": "2026", "data": [12, 15, 19] }]
    }
  }
}
```

`charts` funktioniert genauso in `add_slides_from_layouts` und `set_powerpoint_slide_fields`.

**Slot-Werte** akzeptieren drei Formen:

| Wert                              | Ergebnis                                                   |
| --------------------------------- | ---------------------------------------------------------- |
| `"one line"`                      | Ein Absatz auf Ebene 0; `\n` teilt in mehrere Absätze      |
| `["a", "b"]`                      | Ein Absatz pro Element, alle auf Ebene 0                   |
| `[{ "text": "sub", "level": 1 }]` | Ein Absatz auf Ebene `level` 0–8                           |

Im Text werden `**fett**`, `*kursiv*` und `~~durchgestrichen~~` formatiert; Schrift, Größe und Farbe bleiben die des
Layouts. Links erscheinen als „Text (URL)“, nicht klickbar.

Weggelassene Slots bleiben leer und zeigen in PowerPoint den Aufforderungstext des Layouts.

**Listen kommen aus der Vorlage, nicht von dir.** Das Tool schreibt keine eigenen Aufzählungs- oder
Nummerierungseinstellungen. Jeder Absatz übernimmt das Zeichen seiner Ebene aus dem Listenformat des
Platzhalters im Master: einen Aufzählungspunkt, eine Nummer oder nichts. Ein String und ein Array
sehen **gleich** aus. Das Array teilt den Text nur in Absätze; es schaltet keine Aufzählung ein oder
aus. Das heißt:

- **Tippe nie selbst Listenzeichen.** Kein `•`, `-`, `–`, `*`, `1.`, `a)` oder `→` am Zeilenanfang.
  Auf einer Ebene mit Aufzählungszeichen entsteht sonst `• • Text` oder `• 1. Text`. Schreib den
  reinen Text, die Vorlage setzt das Zeichen.
- **Ein Absatz kann sein Aufzählungszeichen nicht abschalten.** In einem Platzhalter, dessen Ebene 0
  Aufzählungszeichen hat, bekommt jede Zeile auf Ebene 0 einen Punkt, auch eine Überschrift oder ein
  Einleitungssatz. Überschriften gehören in den `title`-/`ctrTitle`-Slot des Layouts oder in ein
  Layout mit eigenem Überschrift-Slot oder einer Ebene ohne Zeichen. Schreib „OPTION A“ nicht als
  ersten Punkt einer Spalte.
- **Nummerierte oder schlichte Zeilen brauchen eine Ebene oder einen Slot, der so formatiert ist.**
  Nummeriert die Vorlage eine Ebene, nutze sie; sonst ist die Liste eine Aufzählung, also setz keine
  eigenen Nummern dazu. Agendapunkte, Schritte und Kapitelnummern gehören in Slots ohne
  Aufzählungszeichen. Passt keiner, schreib die Punkte ohne Nummern.
- **Viele Firmen-Master nutzen Ebene 0 für Fließtext und Ebene 1 für Aufzählungen** (Beispieltext
  „Mastertextformat bearbeiten / Zweite Ebene …“). Bei so einem Master schreibst du Einleitungstext
  auf Ebene 0 und die Listenpunkte mit `"level": 1`.

Welche Ebene Aufzählungszeichen hat, zeigt `describe_pptx_template` nicht. Mit Code-Ausführung liest
du es aus der Vorlage (siehe unten), ohne Code hältst du dich an die Regeln oben. Lies das Deck nach
dem Erstellen mit `read_powerpoint_slides` zurück: Zeilen, die mit einem selbst getippten `•`, `-`
oder einer Nummer beginnen, sind ein Fehler. Sag dem Nutzer, dass die Aufzählungszeichen aus der
Vorlage kommen, und bitte ihn, eine Inhaltsfolie zu prüfen.

**Wenn Code-Ausführung verfügbar ist**, lies Listenformat und Position jedes Slots aus, bevor du
planst. Hänge die Vorlage an (`attach_template_to_chat`, siehe **de-templates**) und führe das
mitgelieferte Skript aus. Es ist nur da, wenn der Skill als Paket installiert wurde (Zip / Sync):

```bash
python3 /mnt/data/skills/de-powerpoint/scripts/pptx_inventory.py "/mnt/data/<vorlage>.pptx" --lists
```

```text
== slideLayout9.xml "Text_Box_OB"
  body:13      at 52%,30%  L0=bullet '•'  L1=bullet '–'  L2=none …
  body:14      at  5%,30%  L0=bullet '•'  L1=bullet '–'  L2=none …
```

`L0=bullet` = Zeilen auf Ebene 0 bekommen einen Aufzählungspunkt, `L0=number arabicPeriod` =
nummeriert, `L0=none` = schlichter Text. Ein Zeichen wie `'§'` oder `'n'` stammt aus einer
Symbolschrift (Quadrat, Strich, …) und ist trotzdem ein Aufzählungszeichen. `at x%,y%` ist die linke
obere Ecke des Slots: Hier ist `body:14` die **linke** Spalte, obwohl die Nummer höher ist. Fehlt das
Skript, gelten die Regeln oben ohne es.

**Optionen für den Basis-Foliensatz:**

- `drop_template_slides` (Standard `true`) entfernt die eigenen Folien des Quell-Foliensatzes.
  Folienmaster, Layouts, Themes und Medien bleiben **immer** erhalten.
- `drop_template_slides: false` behält sie und hängt danach an – das Ergebnis wird jedoch als **neues**
  Dokument gespeichert. Um einen Foliensatz direkt in der Datei wachsen zu lassen, verwende
  `add_slides_from_layouts` (Schritt 3).
- Statt `template_name` kannst du `document_id` (eine gespeicherte `.pptx`) oder `librechat_file_id`
  (einen Anhang) übergeben, um diesen Foliensatz als Basis zu verwenden. Da die Layouts erhalten
  bleiben, lässt sich ein so erstellter Foliensatz später erweitern – das ist der iterative Weg für Weg C.
- `role_map` überschreibt die Ableitung: `{ "content": "slideLayout4.xml" }`.

Die **Antwort** meldet pro Folie: `layoutId`, `layoutName`, `filledSlots`, `filledImageSlots`,
`unknownFields`, `emptySlots`. Prüfe immer `unknownFields` – ein vertippter Slot-Key wird gemeldet,
nicht stillschweigend verworfen. Bild-Slots, die kein Bild erhalten haben, stehen in
`imageSlotsNotFilled` (mit einer `note`).

### Schritt 3 – `add_slides_from_layouts` (Foliensatz direkt in der Datei erweitern)

Das In-place-Gegenstück zu Schritt 2: dasselbe `slides`-Array, aber es zielt über `document_id` /
`librechat_file_id` auf einen bestehenden Foliensatz und **behält dasselbe Dokument**. So wächst ein
Weg-C-Foliensatz über mehrere Runden – erstelle den Foliensatz nie neu, um Folien hinzuzufügen.

```json
{
  "document_id": "<id>",
  "slides": [
    { "layout": "Kapiteltrenner", "fields": { "title": "2. Zielbild" } },
    { "layout": "slideLayout11.xml", "fields": { "title": "Roadmap", "body:10": ["Q1", "Q2"] } }
  ]
}
```

- `insert_after: n` setzt die neuen Folien hinter Folie `n` (`0` = vor Folie 1). Weglassen, um anzuhängen.
- Liefert `slides_before` / `slides_after` / `slides_added` plus denselben Bericht pro Folie.
- Lehnt einen Foliensatz ab, dessen Layouts keine nativen Platzhalter haben (einen aus Markdown
  erstellten Foliensatz), und nennt stattdessen `append_slides_to_powerpoint` – in diesem Fall wird
  nichts geschrieben. Ebenfalls ohne zu schreiben lehnt es ab, wenn überhaupt kein Slot befüllt wird
  (typischerweise: keiner der übergebenen Keys passt zu einem Slot).

### Schritt 4 – `set_powerpoint_slide_fields` (eine Folie ändern)

Ändert **eine** Folie direkt in der Datei. Nur die übergebenen Slots ändern sich; alle anderen Slots,
Formen, Bilder und die Position der Folie bleiben unberührt. Slots, die das Layout anbietet, die Folie
aber noch nicht enthält, werden hinzugefügt – auch Bild-Slots.

```json
{
  "document_id": "<id>",
  "slide_number": 3,
  "fields": { "title": "Kernbefunde (überarbeitet)", "body:10": ["Neuer Punkt 1", "Neuer Punkt 2"] },
  "images": { "pic:14": { "librechat_file_id": "abc-attachment-id" } }
}
```

`fields` oder `images` allein genügt – übergib beides nur, wenn du beides ändern willst. Das ist das
Tool, das du über mehrere Runden immer wieder aufrufst, während der Nutzer den Foliensatz prüft.
Akzeptiert auch `librechat_file_id` (der Anhang wird auf dem gemeinsamen Volume aktualisiert, sofern
verfügbar).

### Wie eine `layout`-Referenz aufgelöst wird

Das `layout` einer Folie wird in dieser Reihenfolge abgeglichen: eine `layoutId` → eine Rolle (ein
expliziter `role_map`-Eintrag überschreibt die abgeleitete `roleMap`) → ein Layoutname.
`{{slide_type:x}}`-Marker spielen hier keine Rolle; sie steuern nur `repeat`-Datensätze in
`create_powerpoint_from_template` (siehe **de-templates**). **Bitte den Nutzer nie, `{{}}`-Marker
in einen Corporate-Master einzutippen** – genau das macht Weg C überflüssig.

---

## 4a. Weg D – Design-Deck mit Blindtext auf den Musterfolien

Viele Firmenvorlagen sind nicht so gebaut, wie PowerPoint es vorsieht. Die Designer haben die
Inhaltsbereiche als **einfache Textfelder auf Musterfolien** angelegt (Titelfolie, Agenda,
Kapiteltrenner, Inhaltsfolie, Abschlussfolie) und mit Blindtext gefüllt: „Text“, „XXX“, „TITEL“,
„UNTERTITEL“, „Text 1 … Text 4“, „01 XXX“. Die Layouts hinter diesen Folien tragen nur Hintergrund,
Logo, Fußzeile und Foliennummer. Deshalb finden die Layout-Tools aus Weg C nichts zum Befüllen.

So ein Deck nutzt du so, wie es ein Mensch tun würde: **die passende Musterfolie duplizieren, ihre
Textfelder überschreiben, die nicht genutzten Musterfolien löschen.** companyFILES hat kein Tool, das
einfache Textfelder bearbeitet, deshalb braucht dieser Weg Code-Ausführung.

**Erst planen, wie in §1:** Nenne für jede Folie des neuen Decks die Musterfolie, die sie kopiert
(„Folie 5 = Inhaltsfolie mit drei Bullets“), und den Text für jedes ihrer Textfelder. Eine Musterfolie
kannst du beliebig oft verwenden; nicht benötigte Musterfolien fallen weg. Halte die Texte ungefähr so
lang wie den Blindtext. Die Felder haben eine feste Größe, und niemand sieht die Folie, bevor der
Nutzer sie öffnet.

### Wenn Code-Ausführung verfügbar ist

Das angehängte Deck liegt in der Sandbox unter `/mnt/data/<dateiname>.pptx` (eine companyFILES-Vorlage:
erst `attach_template_to_chat`, siehe **de-templates**). Dieser Skill bringt zwei Skripte mit, unter
`/mnt/data/skills/de-powerpoint/scripts/`, wenn er als Paket installiert wurde:

1. **Inventur**: listet jedes Shape mit ID und Absätzen auf:

   ```bash
   python3 /mnt/data/skills/de-powerpoint/scripts/pptx_inventory.py "/mnt/data/<deck>.pptx"
   ```

   Jede Zeile lautet `id=<shape id> <art> "<name>"  [0] 'Absatz 0'  [1] 'Absatz 1' …`.
   `box` = einfaches Textfeld (Inhalt für Weg D), `ph:*` = echter Platzhalter, `tbl` = Tabelle
   (Zellen als `r<zeile>c<spalte>`), `in=<id>` = in einer Gruppe. `!DUMMY` markiert Blindtext. Große
   Decks: `--slides 1-10` anhängen (die Ausgabe eines Aufrufs ist auf etwa 64 KB begrenzt).
   - `fit≈22ch×3 lines` = ungefähr so viel Text fasst das Feld laut Design. Die farbige Kachel oder
     der abgerundete Kasten hinter einem Textfeld ist für seinen Blindtext bemessen. Plane deine
     Texte innerhalb dieser Grenze: Eine Überschrift mit 6 Zeichen braucht einen kurzen Ersatz, keinen
     Satz.
   - `<r>` in einem Absatz markiert einen Formatwechsel, z. B. `'01 <r>TITEL'` = fette Nummer + normaler
     Titel. Behalte das `<r>` in deinem Text (`"02 <r>PORTFOLIO"`), dann bleiben beide Formate.

2. **Befüllen**: Plan schreiben und das Deck in einem Aufruf bauen:

   ```bash
   cat > /tmp/plan.json <<'EOF'
   {"slides": [
     {"from": 1, "texts": {"8": "Jahresbericht 2026", "18": "Berlin, 28.10.2026"}, "notes": "Begrüßung"},
     {"from": 2, "texts": {"3": ["Markt", "Produkte", "Team", "Ausblick"]}},
     {"from": 5, "texts": {"4": ["Stärke eins", "Stärke zwei", "Stärke drei"], "6": "01 UNTERNEHMEN"}},
     {"from": 5, "texts": {"4": ["Zweite Folie", "im selben Design"], "6": "02 PRODUKTE"}},
     {"from": 8, "replace": {"Musterfirma": "Acme GmbH"}}
   ]}
   EOF
   python3 /mnt/data/skills/de-powerpoint/scripts/pptx_fill.py "/mnt/data/<deck>.pptx" /tmp/plan.json "/mnt/data/<ergebnis>.pptx"
   ```

   - `from` = Nummer der Musterfolie, `texts` = Shape-ID → neuer Text. Die Shape-IDs bleiben auf
     jeder Kopie einer Musterfolie gleich.
   - Ein Text ist ein String (`\n` = neuer Absatz, `<br>` = Zeilenumbruch), eine Liste von Absätzen
     (einer pro Bullet; `null` behält einen Absatz) oder `{"<absatz-index>": "text"}`, um einzelne
     Zeilen eines Felds zu ändern (ein Feld mit `'XXX'  ''  'XXX'` = Überschrift, Leerzeile,
     Beschreibung).
   - Außerdem: `tables` (Shape-ID → Zeilen × Zellen), `images` (Shape-ID → `/mnt/data/<bild>`, tauscht
     ein Bild und behält seinen Rahmen), `delete` (Shape-IDs, z. B. ein „ABBILDUNG“-Feld, für das du kein
     Bild hast), `replace` (Teilstring auf der ganzen Folie), `notes`.
   - Schreib den Plan im **selben** Aufruf nach `/tmp`. Dateien in `/mnt/data` werden zu Chat-Anhängen,
     und `/tmp` wird nach jedem Aufruf geleert.
   - Das Skript behält die Formatierung jedes Absatzes (Schrift, Größe, Farbe, Bullet), kopiert Diagramme
     und Bilder mit der Folie und überschreibt die Quelle nie.

3. **Prüfen**: Das Befüll-Skript endet mit einer Prüfung und beendet sich mit Code 2, wenn Blindtext
   übrig ist (`CHECK FAILED` mit Folie, Shape-ID und Text). Korrigiere den Plan und führe ihn erneut aus.
   Eine `FIT WARNING` heißt: Ein Text ist zu lang für sein Feld oder die Form dahinter und läuft über das
   Design hinaus. Kürze genau diese Texte und führe den Plan erneut aus, bis keine Warnung mehr kommt.
   Einzeln prüfen geht auch: `pptx_inventory.py "/mnt/data/<ergebnis>.pptx" --check`. Lass die Inventur
   noch einmal über das Ergebnis laufen und vergleiche sie mit deinem Plan, bevor du antwortest.

4. **Antworten**: Das Ergebnis kommt als Chat-Anhang zurück. Sag, aus welcher Musterfolie jede Folie
   stammt und dass du nur den Text prüfen konntest, nicht das Aussehen. Bitte den Nutzer, auf Text zu
   achten, der zu lang für sein Feld ist.

**Schreib keinen eigenen Befüll-Code, wenn die Skripte da sind.** Prüfe zuerst:
`ls /mnt/data/skills/de-powerpoint/scripts/`. Code, der allen Text ins größte Shape schreibt oder
`text_frame.clear()` aufruft bzw. `paragraph.text` setzt, löscht Schriften und Bullets der Vorlage,
legt Text über Bilder und lässt den Blindtext in den anderen Feldern stehen.

**Ohne die Skripte** (der Skill wurde als einzelne `SKILL.md` eingefügt): Führe dieselben Schritte
selbst mit python-pptx aus (zuerst `import pptx`; schlägt das fehl, siehe „Ohne Code-Ausführung“).

- Geh alle Shapes durch, auch Gruppen (`shape.shapes`) und Tabellenzellen.
- Ersetze Text **pro Absatz**: Schreib den Text in den ersten Run des Absatzes, leere die anderen Runs
  und entferne oder kopiere ganze Absätze. `shape.text` oder `text_frame.text` zu setzen löscht die
  Formatierung.
- Zum Duplizieren einer Folie legst du eine Folie mit demselben Layout an, kopierst die Kinder des
  `spTree` der Quellfolie und kopierst ihre Beziehungen (Bilder, Diagramme) mit neuen
  Beziehungs-IDs.
- Entferne nicht genutzte Folien aus `prs.slides._sldIdLst` und lösche ihre Beziehung.
- Durchsuche das Ergebnis nach übrig gebliebenem Blindtext, bevor du antwortest.

**Grenzen der Sandbox:**

- Die Sandbox hat kein LibreOffice, also rendert nichts eine Folie zum Anschauen als Bild.
- Jeder Aufruf endet nach etwa 15 Sekunden. Die Skripte brauchen etwa eine Sekunde, auch bei großen
  Decks.
- Eine einzelne Datei darf höchstens etwa 25 MB groß sein.

### Ohne Code-Ausführung

Es gibt keinen Tool-Weg, der diese Textfelder befüllt. Baue **keine** Layout-Folien, die leer
herauskommen, und wechsle nicht zu `create_powerpoint`, um das Ergebnis dann Vorlage zu nennen. Sag dem
Nutzer klar:

- Die Vorlage hat ihre Inhaltsbereiche als einfache Textfelder auf Musterfolien. companyGPT kann sie nur
  mit Code-Ausführung befüllen. Der Nutzer kann Code-Ausführung für den Chat oder Agenten einschalten
  oder einen Admin um die Berechtigung `RUN_CODE` bitten.
- Alternativ lässt sich der Folienmaster einmal mit echten Platzhaltern in seinen Layouts neu bauen
  (PowerPoint: Ansicht → Folienmaster → Platzhalter einfügen). Danach funktioniert Weg C ohne Code.
- Biete an, was jetzt geht: die Folientexte als strukturierte Gliederung zum Einfügen in die Vorlage
  oder ein Deck im companyFILES-Design (Weg A), klar als **nicht** die Firmenvorlage gekennzeichnet.

---

## 5. Iteratives Bearbeiten beliebiger Foliensätze

Alle drei folgenden Tools adressieren den Foliensatz über `document_id` **oder** `librechat_file_id`
(ein LibreChat-Anhang, der direkt auf dem gemeinsamen Volume aktualisiert wird, wenn es eingebunden ist).

### `append_slides_to_powerpoint`

Zwei sich gegenseitig ausschließende Modi.

**(1) Generieren** – `markdown` oder `slides`, dasselbe Schema wie bei `create_powerpoint`:

```json
{
  "document_id": "<id>",
  "slides": [
    { "type": "section", "title": "Part 2: Deep Dive" },
    { "type": "default", "title": "Technical Details", "bullets": ["Detail A", "Detail B"] }
  ]
}
```

**(2) Klonen und neu befüllen** – `reference_slide` kopiert eine **bestehende Folie desselben
Foliensatzes** (Design, Layout, Schriften, Hintergrund) und befüllt ihre `{{placeholders}}` neu. So
wird ein `{{}}`-Vorlagen-Foliensatz erweitert, damit die neue Folie genau wie die Vorlage aussieht:

```json
{
  "document_id": "<id>",
  "reference_slide": 4,
  "placeholders": { "region": "APAC", "revenue": "€0.9M" },
  "notes": "APAC is the newest market — numbers are 2 quarters old."
}
```

`reference_slide` lässt sich nicht mit `markdown`/`slides` kombinieren. Im Klonmodus verwendest du
das Top-Level-Feld `notes`, im Generierungsmodus `slides[].notes`.

Einschränkungen des Klonmodus:

- Strukturierte Felder (`bullets`, `code`, `table`) werden **nicht** gerendert – die geklonte Folie
  hat nur die Formen, die die Vorlage definiert. Inhalte fließen über `{{placeholders}}` ein.
- Nur `{{text placeholders}}` werden neu befüllt; das Neubefüllen von Bildern (`{%name}`) wird hier
  nicht unterstützt – dafür nimmst du `create_powerpoint_from_template`.

### `update_powerpoint_slide`

Ersetzt eine Folie und behält ihre Position sowie die Gesamtzahl der Folien. Dieselben zwei Modi:

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

Oder schnell nur Text: `{ "document_id": "<id>", "slide_number": 2, "markdown": "## New Title\n\n- Bullet" }`
(`##` setzt den Titel, `???` fügt Notizen hinzu).

Ist `reference_slide` gleich `slide_number`, wird die Folie direkt neu befüllt – so reparierst du eine
Folie, die noch rohe `{{placeholders}}` zeigt.

### `read_powerpoint_slides`

```json
{ "document_id": "<id>" }
```

Liefert `{ slide_count, hasLegacyPlaceholders, layoutsAvailable, slides: [...] }`, jede Folie mit
`{ slideNumber, title, textLines, layoutId, layoutName, role, slots, emptySlots }`. Verwende es, bevor
du einen Foliensatz bearbeitest, den du nicht gerade selbst erstellt hast, und nach mehreren
Anhängevorgängen, um die Nummerierung zu prüfen.

`slideNumber` ist die Position, **die PowerPoint anzeigt** (Reihenfolge in `sldIdLst`), keine interne
Dateinummer – es ist also die Nummer, die du an `set_powerpoint_slide_fields` /
`update_powerpoint_slide` übergibst, auch bei einem Foliensatz, dessen Folien umsortiert wurden, bevor
er bei uns ankam.

Die Layout-Felder machen einen unbekannten Foliensatz bearbeitbar: `layoutId` speist
`add_slides_from_layouts`, `slots` zeigt, was jede Folie aktuell enthält, und `emptySlots` listet die
noch freien Keys. Übergib `include_layouts: false` für ein reines Textlesen eines sehr großen
Foliensatzes (nur `slideNumber`, `title`, `textLines`).

---

## 6. Diagramme und Bilder in Folien

- **Diagramm als eigene Folie:** `embed_chart_in_document` mit `document_type: "powerpoint"` rendert
  das Diagramm auf eine eigene Folie; ist `title` gesetzt, kommt zuerst eine generierte Titelfolie,
  sodass der Foliensatz **zwei** Folien hat. Das Ergebnis ist ein Foliensatz – hänge mit
  `append_slides_to_powerpoint` weiter daran an. Seine `id` ist eine `.pptx`, **kein Bild**: Als
  `doc:<id>` oder als Bild-`document_id` übergeben, wird sie als „not an image“ abgelehnt.
- **Diagramm auf einer Inhaltsfolie:** Nimm das native Diagramm – `slides[].chart` (generierte Decks, §3)
  oder `charts` je Slot (Corporate-Decks, Weg C). Es bleibt in PowerPoint bearbeitbar. Nur wenn ein Bild
  gewünscht ist (oder das Deck eine `{{}}`-Vorlage ist, in der `charts` nur Datenreihen umbenennt),
  referenziere ein gespeichertes Diagrammbild als `![chart](doc:<id>)` im Markdown, über einen
  `{%name}`-Bildplatzhalter in einer `{{}}`-Vorlage oder über einen Layout-Bild-Slot (`images`, Weg C).
- **Bildbibliothek:** Stockfotos, Key Visuals und Icons der Organisation (und eigene des Nutzers).
  Finde sie mit `list_image_templates` (`search`, `tag`, `orientation`, `aspect_ratio` sortiert nach
  Nähe, `limit`); jedes Ergebnis hat `ref` (`"img:<name>"`), Beschreibung, Schlagwörter und
  `aspectRatio`. Übergib das `aspect_ratio` des Zielbereichs (das `aspectRatio` eines Slots aus
  `describe_pptx_template`, 16:9 = 1.78), damit wenig beschnitten wird; einen Kandidaten siehst du dir
  mit `view_image { "image_template": "<name>" }` an. Ein unbekannter `img:`-Name bricht den Aufruf mit
  einem Fehler ab, der ihn nennt.
- **Bildquellen** unterscheiden sich je nach Tool:
  - Markdown in `create_powerpoint`: `doc:<documentId>` (gespeichertes Bild), `lc:<file_id>`
    (LibreChat-Anhang – siehe `list_my_files`), `img:<name>` (Bildbibliothek), eine base64-Data-URI
    oder eine öffentliche http(s)-URL.
  - `image`-Felder in `slides[]` sowie Markdown in `append_slides_to_powerpoint` /
    `update_powerpoint_slide`: `lc:<file_id>`, `doc:<document_id>`, `img:<name>`, eine
    base64-Data-URI (`data:image/…`) oder eine öffentliche http(s)-URL. Bevorzuge `lc:`/`doc:`/`img:`
    statt base64. Eine nicht auflösbare Referenz in `slides[].image` ist ein Fehler, der sie nennt; im
    Markdown fällt die Folie auf den Alt-Text zurück.
  - http(s)-Bilder müssen von einem **öffentlich erreichbaren** Host stammen; interne oder private
    Adressen werden abgelehnt.
  - `{%name}`-Vorlagenbilder und Layout-Bild-Slots (`images`) nehmen
    `{ base64 | document_id | librechat_file_id | image_template }`; `images` der Layout-Tools nehmen
    auch die Strings `lc:…`, `doc:…`, `img:…` oder `data:image/…`.
- **Bilder werden nie verzerrt**, außer auf Wunsch (`stretch`):

  | Wo                       | Standard                                    | Option                          |
  | ------------------------ | ------------------------------------------- | ------------------------------- |
  | `slides[].image`         | `contain`: ganzes Bild, mittig im Bereich   | `imageFit: "cover"` beschneidet |
  | Layout-Bild-Slots        | `cover`: füllt den Slot, mittiger Beschnitt | `{ …, "fit": "contain" }`       |
  | `{%name}`-Vorlagenbilder | `cover`; `contain` für Namen mit „logo“     | `fit` je Bild                   |

- Siehe **de-charts-diagram** für das Erstellen von Diagrammen, **de-templates** für
  `{%image}`-Platzhalter, `charts` (benennt nur Datenreihen um – die Diagrammdaten der Vorlage bleiben)
  und `repeat`.

---

## 7. Stolperfallen

- **Weiche nie auf Weg A aus, wenn ein Corporate-Master gewünscht war.** Wird ein Layout-Aufruf
  abgelehnt, korrigiere den Aufruf – wechsle nicht zu `create_powerpoint`. Dessen Ausgabe nutzt das
  eigene Design, sodass genau das verloren geht, worum gebeten wurde (der Corporate-Master), und ein
  nach dem Master benannter Foliensatz, der ihn nicht verwendet, wirkt wie ein Erfolg, obwohl er ein
  Fehlschlag ist. Bekommst du den Aufruf nicht durch, sag das und hör auf; liefere nicht
  stillschweigend einen Ersatz.
- **Übergib `slides`, `fields` und `role_map` als echtes JSON, nicht als String.** Ein serialisiertes
  `"[{\"layout\":…}]"` toleriert der Server, aber nur als Sicherheitsnetz – sende strukturierte
  Argumente. Eine Schema-Ablehnung bedeutet, dass die _Struktur_ falsch ist: Lies das Beispiel in
  dieser Datei erneut, statt dieselbe Nutzlast noch einmal zu senden.
- **`slides` schlägt `markdown`**, wenn beide im selben Aufruf übergeben werden.
- **`title` bei `create_powerpoint` stellt eine zusätzliche generierte Titelfolie voran** – das
  verschiebt jede `slide_number`. Lass es weg, um Folie 1 selbst zu gestalten.
- **`reference_slide` + `markdown`/`slides` ist ein Fehler.** Wähle einen Modus.
- **`slide_number` beginnt bei 1**; ein Wert außerhalb des Bereichs ist ein Fehler, der die
  tatsächliche Folienanzahl meldet.
- **Ein Layout ohne Text-Slots ist keine leere Folie zum Befüllen.** Listet `describe_pptx_template`
  für die Layouts, die du brauchst, keine `title`/`body`-Slots, bleibt eine Layout-Folie leer: nur
  Hintergrund, Logo und Fußzeile. Das ist Weg D (§4a), kein Aufruf, den du mit anderen Feldnamen
  wiederholst.
- **„Fertig“ heißt: zurückgelesen und frei von Blindtext.** Ein Deck, das noch „Text“, „XXX“ oder
  „TITEL“ zeigt oder leere Inhaltsfolien hat, darf nicht als fertig gemeldet werden. Es als fertig zu
  melden und den Nutzer den Blindtext selbst finden zu lassen, ist das schlechteste Ergebnis.
- **`unknownFields` / `emptySlots`** in einer Layout-Antwort signalisieren, dass ein Slot-Key falsch
  war – lies `describe_pptx_template` erneut, statt zu raten. Gängige Synonyme werden akzeptiert
  (`title` für einen `ctrTitle`-Platzhalter, `subtitle` für `subTitle`, `content`/`bullets` für
  `body`), exakte Slot-Keys sind aber immer am sichersten.
- **Getippte Listenzeichen verdoppeln sich.** `"• Punkt"` oder `"1. Punkt"` in einem Layout-Slot
  erscheint als `• • Punkt` oder `• 1. Punkt`, weil das Listenformat der Vorlage ein eigenes Zeichen
  setzt. Aufzählungszeichen und Nummern kommen nur aus der Vorlage (siehe „Listen kommen aus der
  Vorlage“).
- **Ein Synonym befüllt einen Slot, nicht alle passenden.** Bei einem Layout mit zwei
  Body-Platzhaltern (`body:12`, `body:13`) befüllt ein einzelnes `bullets` den **ersten freien** und
  meldet den anderen in `emptySlots` – es wird nicht in beide dupliziert. Um beide Spalten zu befüllen,
  adressiere sie mit exaktem Key. Exakte Keys gewinnen gegen Synonyme, daher befüllt
  `{ "body:13": "right", "content": "left" }` beide korrekt.
- **`subtitle` bei einem Master ohne `subTitle`-Platzhalter** (häufig bei Corporate-Mastern: Die
  Untertitelzeile eines Titellayouts ist ein normaler `body`-Platzhalter) fällt auf den ersten freien
  `body`-Slot zurück, statt in `unknownFields` zu landen.
- **`create_powerpoint_from_template` lehnt eine Vorlage ohne `{{}}`-Platzhalter ab** – wenn auch
  `images`, `charts` und `speaker_notes` fehlen – und nennt in der Fehlermeldung die Layout-Tools. Das
  ist das Signal für Weg C, keine defekte Vorlage – versuche das Legacy-Tool nicht erneut und füge
  einem Corporate-Master keine `{{}}`-Marker hinzu.
- **`pic:*`-Slots erhalten Bilder über `images`, nicht über `fields`.** Ein `pic`-Key in `fields`
  befüllt nichts – der Slot bleibt leer.
- **Nur `add_slides_from_layouts` behält die Dokument-id**, wenn du einen Weg-C-Foliensatz
  erweiterst. `create_powerpoint_from_layouts` mit `drop_template_slides: false` erzeugt ein _neues_
  Dokument – nützlich, wenn der Nutzer eine Kopie will, falsch, wenn er das Vorhandene erweitern wollte.
- **`append_slides_to_powerpoint` auf einem Corporate-Foliensatz liefert Folien im
  companyFILES-Stil.** Die generierten Folien bringen ihr eigenes Design mit und werden auf das erste
  Layout des Foliensatzes umgemappt, sodass sie auf einem Design-Foliensatz unpassend aussehen. Die
  Antwort weist in `designNote` darauf hin; verwende `add_slides_from_layouts`.
- **Layoutnamen sind nicht eindeutig.** Mehrdeutige Namensreferenzen werden zum ersten Treffer
  aufgelöst und protokollieren eine Warnung; verwende `layoutId`.
- **`list_templates` enthält den Layout-Katalog nicht.** `describe_pptx_template` schon.
- **Schreibe in Weg C keine Formatierung.** Farben/Schriften zu übergeben ist weder möglich noch
  gewollt – der Master bestimmt das Design.
- **Downloads:** Jeder Erstellungsaufruf sowie jeder Append-/Update-/Patch-Aufruf auf einem
  companyFILES-Dokument liefert `{ id, filename, downloadUrl, markdownLink }` (plus
  `librechat_file_id`, wenn der Foliensatz auch als Chat-Datei gespeichert ist). Gib in der Antwort
  immer `markdownLink` aus. Bei einem direkt aktualisierten Chat-Anhang enthält die Antwort
  `librechat_file_id`, `filename` und `message`, aber **keinen** Download-Link – teile dem Nutzer mit,
  dass der angehängte Foliensatz aktualisiert wurde. Konnte der Anhang nicht direkt aktualisiert
  werden, wird ein neues Dokument mit eigener `id` und eigenem `markdownLink` zurückgegeben.
- **Theming (Weg A):** `create_powerpoint` übernimmt die CI automatisch aus den Einstellungen: Farben,
  Theme-Schriften, Linkfarbe, Firmenname in den Dateieigenschaften und – auf Inhaltsfolien – Fußzeilentext,
  Foliennummer und das Logo (wenn „Logo in Dokumenten“ an ist, an der Folienkante der eingestellten
  Logo-Position; Titel- und Abschnittsfolien bleiben ohne). Theme-Argumente sind nicht nötig.
- **Weg B (Vorlagen):** Nur `{{company_name}}` wird automatisch befüllt (aus dem Firmennamen in den
  Einstellungen); ein Logo braucht einen `{%logo}`-Bildplatzhalter und einen expliziten `images`-Eintrag.
  Weg C schreibt keine Formatierung, die Vorlage bestimmt das Aussehen.

---

## 8. End-to-End-Testlauf

Ein einziger Durchlauf, der alle Folienfunktionen abdeckt. Nützlich, um ein Deployment zu überprüfen.

**Weg A – Foliensatz von Grund auf, iterativ erstellt**

1. `create_powerpoint` – ohne `title`-Argument, 3 Folien: `section`, `default` (Aufzählung +
   `htmlTable` mit farbigen Zellen), `text-image` **ohne** `image` → Skelettkasten erwartet.
   → 3 Folien, `document_id` notieren. (Einmal **mit** `title` wiederholen, um zu bestätigen, dass die
   generierte Titelfolie erscheint und die Nummerierung auf 4 verschiebt.)
2. `append_slides_to_powerpoint` – `slides`: ein `default` mit `code`-Block und `table` sowie ein
   `text-image` **mit** `image` als base64-Data-URI. → dieselbe `document_id`, 5 Folien.
3. `append_slides_to_powerpoint` – `markdown` mit zwei `##`-Überschriften und einem `???`-Notizblock.
   → 7 Folien, Notizen in der Referentenansicht sichtbar.
4. `update_powerpoint_slide` – `slide_number: 2`, ein `slides`-Array mit einem Element vom Typ
   `section`. → weiterhin 7 Folien, Folie 2 ist jetzt ein Kapiteltrenner.
5. `read_powerpoint_slides` → `slide_count: 7`, Titel in der erwarteten Reihenfolge.

**Weg C – Corporate-Master, iterativ erstellt**

6. Master als `potx`-Vorlage hochladen → Logzeile
   `Auto-extracted N slide layout(s) from PPTX template …`, `placeholders` leer.
7. `describe_pptx_template` → `hasLegacyPlaceholders: false`, Layouts mit `layoutId`, `name`,
   `masterId`, `role`, Slot-Keys mit mindestens einem `body:idx`-Paar und einem `pic:*`.
8. `create_powerpoint_from_layouts` – 5 Folien, gemischt über **Rolle**, **Name** und **layoutId**
   adressiert; mit mehrstufiger Aufzählung, einem zweispaltigen Layout, das `body:12` + `body:13`
   befüllt, einem `\n` innerhalb eines Werts und `notes` auf Folie 1.
   → in PowerPoint öffnen: Corporate-Schriften/-Farben/-Logos, echte Master-Aufzählungszeichen, und
   **„Folie zurücksetzen“ ändert nichts**.
9. `set_powerpoint_slide_fields` – nur den `title` von Folie 2 ändern → dieselbe `document_id`,
   gleiche Folienanzahl, andere Slots unberührt.
10. `add_slides_from_layouts` mit dieser `document_id` → **dieselbe** `document_id`, 6 Folien, die neue
    im selben Corporate Design. Mit `insert_after: 1` wiederholen → die Folie landet an Position 2.
11. `set_powerpoint_slide_fields` mit `images: { "pic:14": { "librechat_file_id": "<png>" } }` auf
    einer Titel-Bild-Folie → das Bild füllt den Platzhalterrahmen, zugeschnitten statt verzerrt, und
    `slide.filledImageSlots` in der Antwort listet `pic:14`.

**Ein im Chat angehängter Foliensatz (§2a)**

12. Eine `.pptx` an eine Chat-Nachricht anhängen → `list_my_files` zeigt sie mit einer `file_id`.
13. `describe_pptx_template { "librechat_file_id": "<file_id>" }` → derselbe Katalog wie in Schritt 7,
    ohne Vorlagen-Upload.
14. `read_powerpoint_slides { "librechat_file_id": "<file_id>" }` → Folien in der Reihenfolge, in der
    PowerPoint sie anzeigt, jeweils mit `layoutId` und `slots`.
15. `add_slides_from_layouts` gegen diese `file_id` → die `message` in der Antwort sagt, dass der
    Anhang direkt aktualisiert wurde (gleiche `file_id`, `librechat_file_id` in der Antwort) oder dass
    die geänderte Kopie als neues Dokument gespeichert wurde (neue `id` und `markdownLink`).

**Weg D – Design-Deck mit Blindtext (Code-Ausführung)**

16. Ein Deck anhängen, dessen Inhaltsfolien einfache Textfelder sind („Text“, „XXX“) →
    `describe_pptx_template` zeigt Layouts ohne Text-Slots, `read_powerpoint_slides` zeigt den Blindtext.
17. `pptx_inventory.py` auf `/mnt/data/<deck>.pptx` → Zeilen mit `box` und `!DUMMY`.
18. `pptx_fill.py` mit einem Plan, der eine Musterfolie zweimal nutzt, eine Liste von Bullets, eine
    Absatz-Map `{"0": …, "2": …}` und ein `delete` → `saved … N slides`, `CHECK OK`, und das Ergebnis
    kommt als Chat-Anhang zurück; in PowerPoint sehen die Kopien aus wie die Musterfolie.
19. Derselbe Plan mit einer weggelassenen Shape-ID → `CHECK FAILED` mit dieser Folie und Shape,
    Exit-Code 2.

**Fehlerpfade**

20. `"layout": "GibtsNicht"` → Fehler, der alle Layouts **und** Rollen auflistet.
21. `fields: { "untertitel": "x" }` auf einem Layout ohne diesen Slot → `unknownFields: ["untertitel"]`.
22. `slide_number: 99` bei `set_powerpoint_slide_fields` → Fehler mit der tatsächlichen Folienanzahl.
23. `reference_slide` zusammen mit `slides` → Fehler.
24. Ein Foliensatz **mit** `{{}}`-Markup durch `describe_pptx_template` →
    `hasLegacyPlaceholders: true` → zu `create_powerpoint_from_template` wechseln.
25. `add_slides_from_layouts` auf einem mit `create_powerpoint` erstellten Foliensatz → Fehler, der
    `append_slides_to_powerpoint` nennt, und die Folienanzahl des Foliensatzes bleibt unverändert.
26. `add_slides_from_layouts` mit `insert_after` jenseits der Folienanzahl → Fehler mit der
    tatsächlichen Anzahl.
27. `pptx_inventory.py <Firmen-Master> --lists` → eine Zeile pro Text-Slot mit `at x%,y%` und
    `L0`…`L4`; ein Slot, dessen Master-Ebene 0 Aufzählungszeichen hat, zeigt `L0=bullet`. Befülle ihn
    mit `["Punkt A", "Punkt B"]` (ohne getipptes `•`) → PowerPoint zeigt genau einen Punkt pro Zeile.

`MANUAL_TESTS.md` §4.6 (Corporate-Master) und §4.9 (im Chat angehängter Foliensatz) enthalten diese
Szenarien als direkt ausführbare cURL-Befehle.
