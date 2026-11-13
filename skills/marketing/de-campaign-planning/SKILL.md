---
name: de-campaign-planning
description: Erstellt Kampagnen-Briefings mit Zielen, Zielgruppensegmenten, Kanalstrategie, Content-Kalender und Erfolgskennzahlen. Verwende ihn, wenn du eine neue Kampagne startest, Quartals-Marketingaktivitäten planst oder eine Agentur briefst. Auslösen mit "Kampagne planen für", "Kampagnen-Briefing", "Marketingplan für [Launch]".
---

# Kampagnen-Planung-Skill

Plane Marketingkampagnen von der Zieldefinition über die Produktion des Content-Kalenders bis zur Erfolgsmessung. Alle Markenrichtlinien, Zielgruppendaten, historische Performance und Budgets kommen von dir oder aus angebundenen Quellen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Analytics über MCP** (z. B. Google Analytics, Adobe, Mixpanel) | Historische Performance, Zielgruppenverhalten, Conversions |
| **CRM über MCP** (z. B. Salesforce, HubSpot) | Kundensegmente, Deal-Stage-Daten, Kontaktlisten |
| **Ad-Plattformen über MCP** (z. B. Google Ads, Meta Ads, LinkedIn Ads) | Vergangene Kampagnen-Performance, Targeting-Daten, Spend-Historie |
| **CMS über MCP** (z. B. WordPress, Contentful, Webflow) | Content-Inventar, Veröffentlichungsplan, SEO-Daten |
| **E-Mail über MCP** (z. B. Mailchimp, HubSpot, Braze, Customer.io) | Listengröße, Engagement-Kennzahlen, Sequenz-Performance |
| **companyRAG-Sammlungen / Datei-Upload** | Markenrichtlinien, frühere Briefings, Kampagnenvorlagen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Kampagnen-Planungs-Workflow

Führe diese Schritte der Reihe nach aus. Jeder Schritt baut auf dem vorherigen auf — übersprungene Schritte führen zu unvollständigen Briefings, die nachgearbeitet werden müssen.

### Schritt 1: Kampagnenziele definieren

Jede Kampagne beginnt mit einem klaren, messbaren Ziel. Ohne ein solches lässt sich weder der Erfolg bestimmen noch lassen sich Ressourcen sinnvoll zuweisen.

**Ziel-Framework:**

```
KAMPAGNENZIEL:
  Geschäftsziel:     [Das übergeordnete Geschäftsergebnis, das diese Kampagne unterstützt]
  Kampagnenziel:     [Das spezifische Marketingergebnis — was verändert sich durch diese Kampagne?]
  Primäre Kennzahl:  [Die EINE Zahl, die Erfolg definiert]
  Zielwert:          [Spezifischer, messbarer Zielwert für die primäre Kennzahl]
  Zeitraum:          [Start- und Enddatum der Kampagne]
  Baseline:          [Aktueller Wert der primären Kennzahl, aus DEINEN Daten]
```

**Qualitätscheck für das Ziel:**

| Check | Frage | Wenn Nein |
| --- | --- | --- |
| Messbar | Lässt sich Erfolg in einer Zahl ausdrücken? | Neu definieren, bis quantifizierbar |
| Zeitlich begrenzt | Gibt es ein klares Enddatum? | Eines festlegen — offene Kampagnen verlaufen sich |
| Mit Baseline | Kennst du den Ausgangszustand? | Baseline vor der Zielsetzung ermitteln |
| Singulär | Gibt es EINE primäre Kennzahl? | Eine primäre wählen, andere als sekundär einordnen |
| Beeinflussbar | Kann Marketing diese Kennzahl spürbar bewegen? | Auf eine Kennzahl umschwenken, die Marketing steuert |

### Schritt 2: Zielgruppe segmentieren

Definiere, wen die Kampagne adressiert. Kampagnen, die "alle" adressieren, erreichen niemanden wirklich.

**Segmentierungsmethodik:**

1. Beginne mit dem Geschäftsziel — wer muss welche Handlung vornehmen, damit das Ziel erreicht wird?
2. Definiere primäre Segmente (maximal 2–4 pro Kampagne) anhand der verfügbaren Datendimensionen:

| Dimension | Beispiele | Am besten für |
| --- | --- | --- |
| Demografisch | Unternehmensgröße, Branche, Jobtitel, Region | B2B-Targeting, Account-based Campaigns |
| Verhaltensbasiert | Kaufhistorie, Engagement-Level, Produktnutzung | Retention, Upsell, Re-Engagement |
| Phasenbasiert | Funnel-Phase, Lifecycle-Phase, Position in der Buyer Journey | Nurture, Conversion, Onboarding |
| Bedürfnisbasiert | Pain Points, Use Cases, Jobs-to-be-done | Content-Marketing, Thought Leadership |

1. Vervollständige für jedes Segment:

```
SEGMENT: [Name]
  Größenschätzung:     [aus CRM-/Analytics-Daten oder Nutzereingabe]
  Schlüsselmerkmale:   [definierende Attribute]
  Primärer Pain Point: [welches Problem löst diese Kampagne für sie?]
  Gewünschte Handlung: [was sollen sie nach Kontakt mit der Kampagne TUN?]
  Aktuelles Bewusstsein: [unaware / problem-aware / solution-aware / product-aware]
  Kanäle:              [wo konsumiert dieses Segment Content? — aus Daten oder Nutzereingabe]
```

### Schritt 3: Kanäle und Taktiken auswählen

Ordne Kanäle den Segmenten und Zielen zu. Die Kanalauswahl ist eine strategische Entscheidung, keine Checkliste.

**Kanalauswahl-Matrix:**

Bewerte für jeden Kandidaten-Kanal:

| Faktor | Bewertung |
| --- | --- |
| Zielgruppenpräsenz | Ist das Zielsegment auf diesem Kanal aktiv? (aus Daten, nicht aus Annahme) |
| Zielpassung | Kann dieser Kanal die gewünschte Handlung auslösen (Awareness, Consideration, Conversion)? |
| Historische Performance | Wie hat dieser Kanal bei ähnlichen Kampagnen abgeschnitten? (aus deinen Daten) |
| Budgeteffizienz | Wie hoch sind die erwarteten Kosten pro Ergebnis im Vergleich zu anderen Kanälen? |
| Content-Passung | Funktioniert die Kampagnenbotschaft im Format dieses Kanals? |
| Kapazität | Hat das Team die Fähigkeiten und Bandbreite, um auf diesem Kanal gut zu liefern? |

**Zuweisung der Kanalrolle:**

Weise jedem ausgewählten Kanal eine konkrete Rolle in der Kampagne zu:

| Rolle | Zweck | Beispiel |
| --- | --- | --- |
| **Reach** | Awareness in der Zielgruppe erzeugen | Paid Social, Display, PR, SEO-Content |
| **Engage** | Interesse vertiefen und Richtung Consideration bewegen | Blogposts, Webinare, E-Mail-Nurture, Retargeting |
| **Convert** | Die konkrete gewünschte Handlung auslösen | Landingpages, Paid Search, Direkt-E-Mail, Sales Enablement |
| **Retain** | Verstärkung nach der Conversion | Onboarding-E-Mails, Community, Kunden-Content |

Nicht jede Kampagne braucht alle vier Rollen. Richte sie nach deinem Funnel-Ziel aus.

### Schritt 4: Content-Kalender planen

Übersetze die Kanalstrategie in einen Produktions- und Veröffentlichungsplan.

**Prozess zur Erstellung des Kalenders:**

1. Arbeite vom Launch-Datum rückwärts — identifiziere alle benötigten Content-Assets, ihre Abhängigkeiten und Produktionszeiten
2. Ordne den Content der Kampagnen-Timeline zu:

```
CONTENT-KALENDER:

Woche 1: [Kampagnenphase — z. B. Pre-Launch / Teaser]
  [Datum] — [Kanal] — [Content-Stück] — [Segment] — [Verantwortlich] — [Status]
  [Datum] — [Kanal] — [Content-Stück] — [Segment] — [Verantwortlich] — [Status]

Woche 2: [Kampagnenphase — z. B. Launch]
  ...

Woche 3–4: [Kampagnenphase — z. B. Sustain / Nurture]
  ...

Woche N: [Kampagnenphase — z. B. Close / Wrap-up]
  ...
```

1. Produktions-Timeline — definiere für jedes Content-Stück:

| Element | Detail |
| --- | --- |
| Content-Stück | Name und Format |
| Briefing fällig | Datum, zu dem das Briefing bereitstehen muss |
| Erster Entwurf fällig | Datum für die erste Erstellung |
| Review/Freigabe | Datum für die Stakeholder-Review |
| Finales Asset fällig | Datum, zu dem das fertige Asset benötigt wird |
| Veröffentlichungsdatum | Datum, an dem es live geht |

1. Kapazität validieren: Gesamtzahl der Content-Stücke × durchschnittliche Produktionszeit ≤ verfügbare Team-Stunden. Wenn die Rechnung nicht aufgeht, kürze den Umfang vor dem Start — nicht mitten in der Kampagne.

### Schritt 5: KPIs und Messplan festlegen

Definiere, wie der Erfolg gemessen wird. Verweise auf den report-performance-Skill für eine detaillierte Messmethodik.

**KPI-Framework für die Kampagne:**

```
PRIMÄRER KPI:
  Kennzahl:  [aus dem Kampagnenziel]
  Zielwert:  [konkrete Zahl]
  Baseline:  [aktueller Wert]
  Messquelle: [welches Tool/welche Plattform]

SEKUNDÄRE KPIs:
  [Kennzahl 1]: [Zielwert] — Misst: [welchen Aspekt der Kampagnengesundheit]
  [Kennzahl 2]: [Zielwert] — Misst: [...]

GUARDRAIL-KENNZAHLEN (dürfen sich nicht verschlechtern):
  [Kennzahl]: [Schwellenwert] — z. B. Abmelderate muss unter X % bleiben
```

### Schritt 6: Budgetzuteilung

Verteile das Budget über die Kanäle nach dem erwarteten Beitrag zum Kampagnenziel.

**Zuteilungsmethodik:**

1. Beginne mit dem Gesamtbudget — falls undefiniert, soll der Plan das Budget benennen, das zur Zielerreichung nötig ist
2. Zuteilung nach Kanalrolle: Gewichte die Investition zugunsten der Funnel-Phasen, die für das Ziel am kritischsten sind
3. Innerhalb jedes Kanals: Zuteilung nach historischen Kosten pro Ergebnis (aus deinen Daten) oder Testbudget für unerprobte Kanäle

```
BUDGETZUTEILUNG:
  Gesamtbudget: [Betrag]

  Kanal:       [Name]
  Rolle:       [reach / engage / convert / retain]
  Zuteilung:   [Betrag oder %]
  Erwartetes Ergebnis: [Volumen der primären Kennzahl]
  Kosten pro Ergebnis: [aus historischen Daten oder Schätzung]
  Konfidenz:   [hoch — historische Daten / mittel — geschätzt / niedrig — neuer Kanal]

  [Für jeden Kanal wiederholen]

  Reserve:     [10–15 % empfohlen für opportunistische Ausgaben oder Umverteilung von unterperformenden Kanälen]
```

**Trigger für Budgetumverteilung:**

| Signal | Maßnahme |
| --- | --- |
| Kanal überschreitet das Kosten-pro-Ergebnis-Ziel um >25 % nach 2 Wochen | Zuteilung reduzieren, untersuchen |
| Kanal übertrifft die Erwartung um >25 % | Erhöhung der Zuteilung aus der Reserve erwägen |
| Neuer Kanal mit unzureichenden Daten nach der Testphase | Entscheiden: Test verlängern oder umverteilen |
| Gesamte Kampagne liegt am 50-%-Punkt hinter dem Ziel | Alle Kanalzuteilungen prüfen und anpassen |

## Ausgabevorlage: Kampagnen-Briefing

```
# Kampagnen-Briefing — [Kampagnenname]
Datum: [Datum]
Verantwortlich: [Kampagnenmanager]
Status: [Entwurf / In Review / Freigegeben]

## Ziel
  [Aus Schritt 1 — Geschäftsziel, Kampagnenziel, primäre Kennzahl, Zielwert, Zeitraum, Baseline]

## Zielgruppe
  [Aus Schritt 2 — Segmentprofile mit Größe, Merkmalen, Pain Points, gewünschten Handlungen]

## Kanalstrategie
  [Aus Schritt 3 — ausgewählte Kanäle mit Rollen, Begründung und Kapazitätsbewertung]

## Content-Kalender
  [Aus Schritt 4 — phasenbasierter Kalender mit Content-Stücken, Verantwortlichen und Produktions-Timeline]

## KPIs und Messung
  [Aus Schritt 5 — primäre, sekundäre und Guardrail-Kennzahlen mit Zielwerten und Quellen]

## Budget
  [Aus Schritt 6 — Zuteilung nach Kanal mit erwarteten Ergebnissen und Konfidenzniveaus]

## Risiken und Abhängigkeiten
  - [Risiko 1]: [Gegenmaßnahme]
  - [Abhängigkeit 1]: [Verantwortlich und Zeitplan]

## Freigaben
  - [ ] Kampagnenziel freigegeben von [Stakeholder]
  - [ ] Budget freigegeben von [Stakeholder]
  - [ ] Kreativ-Briefing freigegeben von [Stakeholder]
  - [ ] Legal-/Compliance-Review (falls zutreffend)
```

## An dein Geschäft anpassen

1. Lade deine Markenrichtlinien in eine companyRAG-Sammlung — der Skill berücksichtigt sie bei der Bewertung von Kanal- und Content-Passung
2. Hinterlege Kampagnenvorlagen aus erfolgreichen vergangenen Kampagnen — nutze sie als Ausgangs-Frameworks
3. Binde deine Analytics- und Ad-Plattformen für historische Performance-Daten an, um Kanalauswahl und Budgetzuteilung zu fundieren
4. Definiere deinen Standard-Freigabeprozess, damit Briefings von Anfang an die richtigen Stakeholder enthalten
5. Gib deine Content-Produktionskapazität an, damit die Kalenderplanung die reale Team-Bandbreite berücksichtigt

## Leitplanken

- Erzeuge niemals Performance-Benchmarks, Conversion-Raten, CPM-/CPC-Schätzungen oder Zielgruppengrößen. Alle Performance-Daten müssen aus den Analytics oder angebundenen Quellen des Nutzers stammen.
- Behaupte niemals "Best-Practice"-Kanalmixe oder Budgetaufteilungen. Die optimale Zuteilung hängt vom konkreten Geschäft, der Zielgruppe und dem Markt ab.
- Nimm niemals Zielgruppenmerkmale oder Kanalpräferenzen ohne Daten an. Frage den Nutzer oder kennzeichne als `[Daten erforderlich]`.
- Kennzeichne Ausgaben: `[Aus Kundendaten]` für belegte Daten · `[Framework-Methodik]` für den Ansatz dieses Skills · `[KI-Vorschlag]` für Modellempfehlungen · `[Daten erforderlich]` für Platzhalter.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Briefing zu erhalten.
