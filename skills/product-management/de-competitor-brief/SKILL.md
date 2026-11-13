---
name: de-competitor-brief
description: Erstellt Wettbewerbsanalysen für Produktstrategie-Entscheidungen, Feature-Priorisierung und Differenzierung. Verwende ihn, wenn ein Wettbewerber etwas Neues launcht, du in ein neues Marktsegment eintrittst oder dich auf ein Strategie-Review vorbereitest. Auslösen mit "Wettbewerber-Briefing zu", "was macht [Wettbewerber]", "vergleiche uns mit [Wettbewerber]".
---

# Wettbewerber-Briefing-Skill

Baue Wettbewerbs-Briefings, die Produktstrategie, Feature-Priorisierung und Marktpositionierung fundieren. Alle Wettbewerbsdaten müssen von dir, aus companyRAG-Sammlungen oder aus der Websuche stammen — niemals aus Trainingsdaten.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **MCP-Server** (z. B. CRM wie HubSpot/Salesforce, Analyst- oder Review-Plattformen) | Sales-Call-Notizen, Churn-Interviews, Einwände von Prospects, RFP-Antworten |
| **companyRAG-Sammlungen / Datei-Upload** | Analyst-Reports, Kundenbewertungen, technische Assessments, eigene Feature-Dokumentation |
| **Websuche** | Öffentliche Produktdokumentation, Pressemeldungen, Stellenanzeigen, Patentanmeldungen, Konferenzbeiträge |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Workflow für das Wettbewerber-Briefing

Führe diese vier Phasen der Reihe nach aus. Jede Phase liefert die Grundlage für die nächste.

### Phase 1: Intelligence sammeln

Lege vor der Analyse fest, was bekannt ist und was untersucht werden muss.

**Quellen-Inventar** — für jeden analysierten Wettbewerber:

| Quellentyp | Beispiele | Zuverlässigkeit |
| --- | --- | --- |
| **Primär** | Direkte Produktnutzung, kostenlose Trials, öffentliche Demos, veröffentlichte Dokumentation | Höchste — Beobachtung aus erster Hand |
| **Sekundär** | Analyst-Reports, Kundenbewertungen (G2, Capterra), Pressebeiträge, Blogposts | Hoch — aber möglicherweise veraltet oder verzerrt |
| **Field Intelligence** | Sales-Call-Notizen, Churn-Interviews, Einwände von Prospects, RFP-Antworten | Hoch für Absichtssignale — aber anekdotisch |
| **Öffentliche Unterlagen** | Geschäftsberichte, Stellenanzeigen, Patentanmeldungen, Konferenzbeiträge | Hoch für strategische Richtung — niedrig für Produktdetails |

**Lücken identifizieren**: Liste nach dem Inventarisieren explizit auf, was NICHT bekannt ist. Unbekannte Bereiche werden zu Recherche-Aufgaben, nicht zu Annahmen.

```
INTELLIGENCE-INVENTAR — [Name des Wettbewerbers]
  Bekannt (belegt):    [Liste mit Quelle und Aktualitätsdatum]
  Teilweise bekannt:   [Liste mit identifizierten Lücken]
  Unbekannt:           [Liste — das sind Recherche-Aufgaben, keine Bereiche zum Raten]
  Zuletzt aktualisiert: [Datum]
```

### Phase 2: Feature-Vergleichsmatrix

Baue einen strukturierten Vergleich der Fähigkeiten entlang von Bewertungsdimensionen, die für deine Produktkategorie relevant sind.

**Vorgehen zum Aufbau der Matrix**:

1. Dimensionen definieren: Verwende die Feature-Kategorien deines eigenen Produkts, nicht die Marketingsprache des Wettbewerbers. Dimensionen sollten widerspiegeln, wie Kunden die Kategorie bewerten.
2. Fähigkeiten bewerten: Beurteile für jede Dimension jeden Akteur (dein Produkt + Wettbewerber):   - Stark: Deckt den Bedarf vollständig ab; keine wesentlichen Lücken   - Ausreichend: Deckt den Kernbedarf ab; einige Einschränkungen   - Schwach: Deckt den Bedarf nur teilweise oder gar nicht ab   - Unbekannt: Unzureichende Daten — für Recherche markieren
3. Belege ergänzen: Jede Bewertung muss ihre Quelle nennen. Unbelegte Bewertungen sind Annahmen.

```
FEATURE-VERGLEICH — [Kategorie]
| Dimension | Dein Produkt | Wettbewerber A | Wettbewerber B | Notizen |
|---|---|---|---|---|
| [Dimension] | [Bewertung + Quelle] | [Bewertung + Quelle] | [Bewertung + Quelle] | [zentrale Unterschiede] |
```

**Bewertungsdisziplin**:

- Bewerte auf Basis des aktuell ausgelieferten Produkts, nicht der angekündigten Roadmap
- Gib deinem eigenen Produkt keine vorteilhaften Bewertungen ohne Belege — eine eigennützige Analyse ist schlimmer als gar keine
- "Unbekannt" ist eine gültige und ehrliche Bewertung — fülle Lücken niemals mit Annahmen
- Aktualisiere Bewertungen, wenn ein Akteur ein bedeutendes Update ausliefert

### Phase 3: Strategische Analyse

Bewege dich vom Feature-Vergleich zur strategischen Interpretation.

#### Positionierungsanalyse

Verorte die Positionierung jedes Wettbewerbers entlang der Dimensionen, die für deine Zielsegmente wichtig sind:

1. Value Proposition: Mit welchem Problem führen sie? Wer ist ihr idealer Kunde?
2. Go-to-Market-Motion: Self-Serve vs. Sales-led vs. Partner-led? SMB vs. Enterprise vs. beides?
3. Pricing-Modell: Per-Seat vs. nutzungsbasiert vs. Flatrate? Free-Tier? Premium-Positionierung?
4. Differenzierungsanspruch: Was macht sie ihrer Aussage nach anders? Ist der Anspruch belegt?

#### Bedrohungs- / Chancen-Bewertung

Klassifiziere für jeden Wettbewerber die strategische Situation:

| Signal | Klassifizierung | Implikation |
| --- | --- | --- |
| Wettbewerber stark, wo du schwach bist, in einer Dimension, die Kunden wichtig ist | **Bedrohung — Aktiv** | Erfordert Reaktion: bauen, partnern oder neu positionieren |
| Wettbewerber investiert in dein Stärkefeld (Hiring, Features, Marketing) | **Bedrohung — Aufkommend** | Genau beobachten; defensive Positionierung vorbereiten |
| Wettbewerber schwach, wo du stark bist, in einer Dimension, die Kunden wichtig ist | **Chance — Differenzierung** | In Positionierung und Sales-Enablement verstärken |
| Wettbewerber ignoriert ein Segment oder einen Use Case, den du gut bedienst | **Chance — White Space** | In das unterversorgte Segment hineingehen |
| Wettbewerber und du seid gleich stark | **Parität** | Auf anderen Dimensionen konkurrieren (Preis, Experience, Trust, Ökosystem) |

#### Indikatoren für Marktbewegung

Verfolge Signale, die auf strategische Richtungsänderungen hindeuten:

- Hiring-Muster: Für welche Rollen stellen sie ein? (Engineering in neuen Bereichen, Sales in neuen Regionen, spezifische Fachexpertise)
- Partnerschafts-Ankündigungen: Neue Integrationen, Channel-Partner, Plattform-Plays
- Preisänderungen: Preissenkung (Land-Grab), Preiserhöhung (Value-Extraction), neue Tiers (Segment-Expansion)
- Akquise-Aktivität: Welche Fähigkeiten kaufen sie ein?
- Verschiebungen im Kundensegment: Bewegen sie sich upmarket, downmarket oder in angrenzende Segmente?

### Phase 4: Empfohlene Reaktion

Strukturiere für jede aktive Bedrohung oder umsetzbare Chance eine Reaktionsempfehlung:

```
REAKTIONSEMPFEHLUNG:
  Auslöser:        [Welche Aktion des Wettbewerbers hat dies ausgelöst?]
  Klassifizierung: [Bedrohung — Aktiv / Bedrohung — Aufkommend / Chance]
  Auswirkung:      [Welche deiner Segmente, Kennzahlen oder Positionierung ist betroffen?]
  Reaktionsoptionen:
    1. [Bauen] — [Was bauen + grober Umfang + Auswirkung auf Timeline]
    2. [Partnern] — [Partnerschaft, die die Lücke schließen könnte]
    3. [Neu positionieren] — [Messaging-Änderung, um die Dimension neu zu rahmen]
    4. [Beobachten] — [Beobachten und beim nächsten Review-Zyklus neu bewerten]
  Empfohlene Option: [Nummer + Begründung]
  Entscheider:     [Wer sollte diese Reaktion genehmigen?]
  Dringlichkeit:   [Sofort / Dieses Quartal / Nächster Planungszyklus]
```

**Auswahlkriterien für die Reaktion**:

- Bauen, wenn die Lücke in einer Must-Win-Dimension liegt und du die Kapazität hast
- Partnern, wenn die Lücke real, aber nicht deine Kernkompetenz ist
- Neu positionieren, wenn der Vorteil des Wettbewerbers weniger zählt, als er behauptet, oder wenn du die Bewertungskriterien neu rahmen kannst
- Beobachten, wenn die Bedrohung aufkommt, aber noch keine Kunden oder Pipeline betrifft

## Ausgabevorlage — Wettbewerber-Briefing

```
# Wettbewerber-Briefing — [Name des Wettbewerbers]
Datum: [Datum]    |    Autor: [Name]    |    Einstufung: [Intern / Vertraulich]

## 1. Executive Summary
[2–3 Sätze Überblick: wer sie sind, was sich geändert hat, warum es für uns relevant ist]

## 2. Intelligence-Inventar
[Konsultierte Quellen, Aktualität, bekannte Lücken]

## 3. Feature-Vergleichsmatrix
[Strukturierter Vergleich — siehe Phase 2]

## 4. Positionierungsanalyse
[Value Proposition, GTM, Pricing, Differenzierung — siehe Phase 3]

## 5. Bedrohungs- & Chancen-Bewertung
[Klassifizierte Signale — siehe Phase 3]

## 6. Empfohlene Reaktion
[Handlungspunkte mit Verantwortlichen und Dringlichkeit — siehe Phase 4]

## 7. Offene Fragen
[Was wir noch lernen müssen, mit zugewiesenen Recherche-Aufgaben]

## 8. Review-Kadenz
[Wann das Briefing zu überarbeiten ist — typischerweise quartalsweise oder nach wichtigen Wettbewerber-Moves]
```

## Review-Kadenz für Wettbewerber

| Auslöser | Aktion |
| --- | --- |
| **Wettbewerber launcht großes Feature** | Betroffene Zeilen der Feature-Matrix aktualisieren; Bedrohungen neu bewerten |
| **Quartalsplanung** | Vollständiges Briefing-Refresh für die Top-2-3-Wettbewerber |
| **Deal an Wettbewerber verloren** | Post-Mortem, um Bedrohungsbewertung und Reaktion zu aktualisieren |
| **Eintritt in neues Marktsegment** | Neues Briefing für segmentspezifische Wettbewerber erstellen |
| **Finanzierung / Akquise eines Wettbewerbers** | Indikatoren für Marktbewegung und strategische Analyse aktualisieren |

## Leitplanken

- Erzeuge NIEMALS Features, Preise, Marktanteile oder Positionierung eines Wettbewerbers aus Trainingsdaten. Alle Wettbewerbsaussagen müssen von dir, aus companyRAG-Sammlungen oder aus der Websuche mit zitierten Quellen stammen.
- Behaupte NIEMALS "Marktstandard" oder "üblich" für eine Wettbewerbsdimension. Jede Aussage muss belegt sein.
- Wenn keine Wettbewerbsdaten vorliegen, erzeuge die leere Briefing-Vorlage und liste die konkret benötigten Daten auf — fülle Lücken nicht mit Annahmen.
- Versieh jede Aussage mit einer Quellenkennzeichnung: `[Aus Nutzereingabe / companyRAG]`, `[Aus Websuche — {Datum}]`, `[Analyse-Framework]` oder `[KI-Einschätzung — prüfen]`.

> **Tipp:** Fordere über companyFILES eine DOCX-, Markdown- oder PPTX-Ausgabe an, um ein formatiertes, sofort teilbares Briefing zu erhalten.
