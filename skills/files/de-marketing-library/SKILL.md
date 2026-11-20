---
name: de-marketing-library
description: 'Findet und nutzt die Marketing-Bibliothek (Bilder, Icons und freigegebene Folien) von companyFILES mit search_library. Verwenden, wenn eine Präsentation, ein Dokument oder PDF Bilder, Icons, eine Feature- oder Prozessfolie mit Icons oder eine fertige Firmenfolie (Referenzen, Über uns, Team, Preise) braucht, wenn der Nutzer nach Markenmaterial, Icons oder „unseren Folien“ fragt oder Icons selbst auswählen möchte. Deckt search_library, img:-/icon:-/slide:-Verweise, das Icon-Raster (slides[].iconGrid), Bibliotheksfolien (librarySlide, insert_library_slides, replace für Namen), die Icon-Auswahl (show_icon_picker) und die Nutzungsrechte (nur intern, Bildnachweis, abgelaufen) ab.'
---

# Marketing-Bibliothek Skill

Die Bilder, Icons und freigegebenen Folien der Organisation (und des Nutzers), nach Bedeutung durchsuchbar und in
jedem Dokument-Tool nutzbar. Schau zuerst hier nach, bevor du ein externes Bild nimmst oder selbst etwas zeichnest.

## Tool-Übersicht

| Tool                      | Zweck                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------- |
| `search_library`          | Bilder, Icons und Folien nach Bedeutung suchen (Deutsch oder Englisch)                |
| `list_image_templates`    | Nur Bilder auflisten/filtern (gleicher Index, gleiche Felder)                         |
| `view_image`              | Ein Bild der Bibliothek ansehen: `{ "image_template": "<name>" }`                     |
| `show_icon_picker`        | Der Nutzer wählt Icons in einem Widget; die Auswahl kommt als seine nächste Nachricht |
| `insert_library_slides`   | Bibliotheksfolien unverändert in ein Deck oder ein neues Deck einfügen                |
| `update_powerpoint_slide` | Mit `replace`: Namen oder Datum auf einer Folie ändern, Design bleibt                 |

Das Deck oder Dokument selbst baust du mit **de-powerpoint**, **de-word-odt**, **de-pdf**.

## 1. Ablauf

1. **Zuerst suchen.** `search_library` für jedes Bild, Icon und jede Folie, die du brauchst. Bevorzuge Assets der
   Organisation vor allem Externen oder Generierten.
2. **Nimm den `ref` genau wie geliefert**: `img:<name>`, `icon:<set>/<name>`, `slide:<collection>/<id>`. Erfinde nie
   einen Verweis; ein falscher scheitert mit `unknown_ref`, und es entsteht kein Dokument.
3. **Prüfe `rights`** jedes Treffers, den du nutzt (Abschnitt 5), und sag dem Nutzer, was gilt.
4. **Baue** mit den Verweisen (Abschnitte 3 und 4) und gib den `markdownLink` des Ergebnisses aus.
5. Will der Nutzer **Icons selbst wählen**, ruf `show_icon_picker` auf (Abschnitt 6), statt zu raten.

## 2. `search_library`

```json
{ "query": "Sicherheit Baustelle", "kind": "icon", "style": "outline", "limit": 10 }
{ "query": "team meeting office", "kind": "image", "aspect_ratio": "16:9", "language": "en" }
{ "query": "Referenzen Kunden", "kind": "slide", "collection": "vertrieb" }
```

| Parameter      | Bedeutung                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------ |
| `query`        | Freitext; alle Wörter müssen treffen; Umlaute gefaltet, Wortanfänge ab 3 Buchstaben        |
| `kind`         | `image`, `icon` oder `slide` (weglassen = alle)                                            |
| `set`, `style` | Icon-Set und Stil (`outline`, `filled`, `duotone`, `other`), nur Icons                     |
| `collection`   | Folien-Sammlung, nur Folien                                                                |
| `orientation`  | `landscape`, `portrait`, `square` (Bilder)                                                 |
| `aspect_ratio` | Zahl oder `"16:9"` (±10 %, Nächstes zuerst): Zielfläche angeben, damit wenig beschnitten wird |
| `language`     | Sprache der gelieferten Texte: `de` (Standard) oder `en`; die Suche deckt beide ab         |
| `limit`        | Bis 100, Standard 20                                                                       |

Jeder Treffer hat `ref`, `kind`, `scope` (`org` oder `user`), `displayName`, `description`, `tags`, `aspectRatio`,
`orientation`; Icons zusätzlich `set`, `style`, `recolorable`; Folien `collection`, `collectionDisplayName`, `index`;
dazu `rights` (Abschnitt 5). Ein persönliches und ein Organisations-Asset mit gleichem Verweis erscheinen beide: der
Verweis löst auf das persönliche auf, der Organisations-Eintrag hat `shadowed: true`. Ausgeblendete und abgelaufene
Assets werden nie gelistet.

Kein Treffer? Probiere ein Synonym oder die andere Sprache, lass `style`/`set` weg, dann eine weitere Suche. Sag es,
wenn die Bibliothek nichts Passendes hat; wechsle nicht stillschweigend zu einer anderen Quelle.

## 3. Icons

Verweis: `icon:<set>/<name>`, optional `?color=brand` (die CI-Primärfarbe) oder `?color=RRGGBB`.

- Gilt in **jedem Bildeingang** von PowerPoint, Word, PDF und ODT: `slides[].image`, Markdown `![Alt](icon:…)`,
  HTML `<img src="icon:…">`, Layout-`images`, `{%name}`-Bilder. PowerPoint und Word bekommen einen scharfen Vektor mit
  PNG-Fallback; der Alt-Text kommt vom Icon.
- **Umfärben geht nur bei einfarbigen Icons** (`recolorable: true`). Mehrfarbige und Raster-Icons bleiben, wie sie
  sind; das Ergebnis meldet das unter `notes`.
- **Word-Vorlagen** (`create_word_from_template`, `{%logo}` / `{IMAGE logo}`) brauchen die Objektform
  `{ "logo": { "icon": "icon:brand-line/lock", "width": 3 } }`. Ein bloßer String schlägt dort fehl.
- PowerPoint-Layout-Slots und `{%name}` nehmen `"icon:…"` oder `{ "icon": "icon:…", "fit": "contain" }`.

### Icon-Raster für Feature- und Prozessfolien

`slides[].iconGrid` (in `create_powerpoint`, `append_slides_to_powerpoint`, `update_powerpoint_slide`) setzt 3–6
Punkte gleichmäßig unter den Folientitel im Deck-Design. **`type` ist weiterhin Pflicht** an der Folie, nimm
`"default"`.

```json
{
  "type": "default",
  "title": "So arbeiten wir",
  "iconGrid": {
    "items": [
      { "icon": "icon:brand/search", "title": "Analyse", "text": "Wir verstehen Ziele und Ausgangslage." },
      { "icon": "icon:brand/pencil", "title": "Konzept", "text": "Wir entwerfen die Lösung mit Ihnen." },
      { "icon": "icon:brand/rocket", "title": "Umsetzung", "text": "Wir liefern in kurzen Iterationen." }
    ],
    "color": "brand"
  }
}
```

- 3 Punkte → 3 × 1, 4 → 2 × 2, 5 → 3 + 2, 6 → 3 × 2; `columns: 2|3` überschreibt das.
- Weniger als 3 oder mehr als 6 Punkte ist ein Fehler: auf mehrere Folien verteilen. `title` eine kurze Zeile,
  `text` höchstens 300 Zeichen.
- Icons nur als `icon:<set>/<name>` (kein `img:`, `lc:`, `doc:`). `color` (`"brand"` oder eine Hex-Farbe) färbt alle
  einfarbigen Icons um; ein eigenes `?color=` eines Punkts gewinnt.
- Andere Inhaltsfelder (`bullets`, `image`, …) an dieser Folie werden ignoriert (eine Warnung sagt es).
- Nimm Icons aus einem Set und einem Stil, damit das Raster einheitlich wirkt.

## 4. Bibliotheksfolien

Freigegebene Folien der Firma (eigener Master, Layout, Notizen, Diagramme, Bilder). **Füge sie unverändert ein**:
baue sie nicht mit `create_powerpoint` nach, das verliert das freigegebene Design.

| Ziel                                | Aufruf                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Neues Deck nur aus Bibliotheksfolien | `insert_library_slides { "slides": [{ "ref": "slide:vertrieb/257" }, { "ref": "slide:vertrieb/258" }], "filename": "Kundentermin" }` |
| In ein vorhandenes Deck             | `insert_library_slides { "document_id": "<id>", "slides": [{ "ref": "slide:vertrieb/257", "position": 2 }] }` |
| In einen Chat-Anhang                | `insert_library_slides { "librechat_file_id": "<id>", "slides": [{ "ref": "slide:vertrieb/257" }] }`    |
| Gemischt mit generierten Folien     | `create_powerpoint` → `slides: [{ "type": "default", "title": "Agenda", "bullets": [...] }, { "librarySlide": "slide:vertrieb/257" }]` |

- `position` ist 1-basiert im entstehenden Deck; ohne Angabe wird in der angegebenen Reihenfolge angehängt.
- `librarySlide` ist ein Feld des Folienobjekts und nimmt kein weiteres Feld. Die Layout-Tools
  (`create_powerpoint_from_layouts`, `add_slides_from_layouts`) nehmen dieselben Einträge in ihrer `slides`-Liste.
- Das Ergebnis hat `slides_before`, `slides_after`, `inserted [{ref, position, title}]` und `notes` (Abschnitt 5).
- Ein langsames Einfügen antwortet „läuft noch“: ruf mit **denselben Angaben** erneut auf, die Folien werden nicht
  doppelt eingefügt.
- Die eingefügte Folie bringt ihr eigenes Theme mit; sie übernimmt nicht die Farben des Ziel-Decks. Sag das, wenn
  die Decks sich unterscheiden.

### Namen oder Datum ändern: `replace`

Bearbeite die eingefügte Folie an Ort und Stelle, sonst ändert sich nichts (Design, Formatierung, Bilder, Diagramme,
Notizen):

```json
{
  "document_id": "<id>",
  "slide_number": 3,
  "replace": [{ "find": "Kunde X", "replace_with": "ACME" }]
}
```

Wörtlich und mit Groß-/Kleinschreibung, jedes Vorkommen auf der Folie, Paare der Reihe nach, nur innerhalb eines
Absatzes (nicht über Absätze oder Zeilenumbrüche). Das Ergebnis nennt `replaced: [{find, count}]`; trifft kein Paar,
scheitert der Aufruf mit `no_match` und schreibt nichts: lies die Folie mit `read_powerpoint_slides` und nimm den
genauen Text. `replace` lässt sich nicht mit `markdown`, `slides` oder `reference_slide` kombinieren.

Verbessere Folientexte darüber hinaus nicht. Bei größeren Änderungen sag dem Nutzer, dass die Folie freigegebener
Inhalt ist.

## 5. Nutzungsrechte: immer beachten

Jedes Asset kann Rechte tragen. Suchtreffer zeigen sie als `rights { usable, internalOnly, credit?, expiresAt? }`; die
Dokument-Tools setzen sie durch.

| Signal                                       | Was zu tun ist                                                                               |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Fehler `asset_expired` (mit dem Verweis)     | Die Rechte sind abgelaufen. Nichts wurde geschrieben. **Anderes Asset wählen** (neu suchen). |
| `notes`: „…nur intern verwenden“             | Dem Nutzer sagen, dass das Asset nur für interne Dokumente gilt; nicht in externem Material nutzen. |
| `notes`: Bildnachweis (`Bildnachweis „© …“`) | Dem Nutzer sagen und den **Nachweis ins Dokument setzen** (Bildunterschrift, Fußzeile oder letzte Folie). |
| `unknown_ref`                                | Der Verweis existiert nicht (Tippfehler, ausgeblendet oder gelöscht). Neu suchen, nie raten. |
| `rights.expiresAt` nah                       | Bei der Übergabe erwähnen („Lizenz gültig bis …“).                                           |

Die `notes` eines Ergebnisses gehören zur Antwort: lies sie jedes Mal und gib Bildnachweise und Intern-Hinweise in
deiner Antwort weiter.

## 6. Nutzer wählt Icons selbst: `show_icon_picker`

```json
{ "query": "Sicherheit", "set": "brand-line", "multiple": true }
```

Alle Argumente sind optional; `multiple` ist standardmäßig true (false = genau ein Icon). Das Widget bietet nur
nutzbare Icons an. Der Aufruf liefert die Wahl **nicht** zurück: sie kommt als **nächste Chat-Nachricht** des Nutzers,
z. B. `Ausgewählte Icons: icon:brand-line/lock, icon:brand-line/shield` (englische Oberfläche: `Selected icons: …`).
Höre nach dem Aufruf auf, warte auf diese Nachricht und nutze die Verweise dann unverändert. Willst du Icons selbst
auswählen, nimm `search_library`.

## 7. Stolperfallen

- `type` bleibt an einer Folie mit `iconGrid` Pflicht (`"default"`).
- Bilder in Word-Vorlagen: Objektform `{ "icon": "icon:…" }`, nie ein bloßer String.
- Eine Umfärbung bei einem mehrfarbigen Icon bewirkt nichts; prüfe `recolorable`, bevor du eine Farbe versprichst.
- `kind: "slide"` findet nur freigegebene Folien; ausgeblendete und abgelaufene erscheinen nie.
- Externe http(s)-Bilder sind der letzte Ausweg, nur wenn die Bibliothek nichts hat, und der Nutzer soll es wissen.
