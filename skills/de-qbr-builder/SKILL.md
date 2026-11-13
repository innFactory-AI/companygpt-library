---
name: de-qbr-builder
description: Erstelle Inhalte für Quarterly Business Reviews mit Nutzungstrends, ROI-Highlights, gemeinsamen Erfolgsmetriken und vereinbarten nächsten Schritten. Verwende ihn bei der Vorbereitung eines Kunden-QBR, beim Erstellen von Account-Zusammenfassungen auf Executive-Ebene oder beim Belegen des Produktnutzens. Auslösen mit "QBR erstellen für", "Quarterly Review für [Kunde]", "Business Review vorbereiten".
---

# QBR-Builder-Skill

Erstelle QBR-Dokumente, die Nutzungsanalysen, eine ROI-Erzählung, Erfolgsmetriken und vereinbarte nächste Schritte kombinieren. Die Account-Daten stammen von dir, aus einer verbundenen MCP-Quelle oder aus companyRAG-Collections.

## Woher die Daten stammen

| Quelle | Was sie beisteuert |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Account-Metadaten, Vertragsdetails, Expansionshistorie, Stakeholder-Kontakte |
| **Produktanalyse über MCP** (z. B. Amplitude, Mixpanel, Pendo oder intern) | Nutzungsmetriken, Feature-Adoption, Trenddaten |
| **companyRAG / Datei-Upload** | Success-Pläne, CSM-Notizen, Support-Exporte, vom Kunden gemeldete Daten |

> **Keine verbundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch – der Skill funktioniert auf dieselbe Weise.

## QBR-Erstellungs-Workflow

Beginne die Vorbereitung 2–3 Wochen vor dem QBR-Termin, um Zeit für Datensammlung, Aufbau der Erzählung und interne Review zu haben.

### Schritt 1: Metriken sammeln

Sammle Daten in vier Metrik-Kategorien. Erfasse für jede Metrik den aktuellen Wert, den Wert der Vorperiode und die Trendrichtung.

| Metrik-Kategorie | Schlüsselmetriken | Quelle |
| --- | --- | --- |
| **Nutzung & Adoption** | Aktive Nutzer vs. lizenzierte, Trend der Login-Häufigkeit, Breite der Feature-Adoption, Nutzungstiefe, Verweildauer in der Plattform | Produktanalyse |
| **Wert & Ergebnisse** | Fortschritt bei vom Kunden genannten Zielen, ROI-Metriken (sofern quantifizierbar), Effizienzgewinne, Belege für Geschäftswirkung | Success-Plan, CSM-Notizen, vom Kunden gemeldete Daten |
| **Support & Zufriedenheit** | Trend des Ticketvolumens, Lösungszeit, CSAT-/NPS-Werte, Eskalationshistorie | Support-Plattform |
| **Partnerschaft** | Erreichte Meilensteine, abgeschlossene Schulungen, bearbeitete Feature-Requests, Roadmap-Alignment | CSM-Notizen, CRM |

Notiere für jede Metrik die Quelle und den Datumsbereich. Veraltete oder unvollständige Daten sollten gekennzeichnet, nicht weggelassen werden.

### Schritt 2: Die Werterzählung aufbauen

Der QBR ist kein Daten-Dump – er ist eine Geschichte über den Wert, den der Kunde erhalten hat, und darüber, wohin sich die Partnerschaft entwickelt.

**Erzählstruktur:**

1. **Wo wir gestartet sind** – Erinnere das Publikum an die ursprünglichen Ziele des Kunden und die Ausgangsbasis. Das verankert das Gespräch in dem, was für den Kunden zählt.
2. **Was wir erreicht haben** – Präsentiere Erfolge in der Sprache und mit den Metriken des Kunden, nicht mit den Feature-Namen deines Produkts. „Euer Team hat die Vertragsprüfungszeit um 40 % reduziert" ist stärker als „Nutzer haben das KI-Prüf-Feature übernommen".
3. **Erfolge und Highlights** – Hebe 2–3 konkrete Erfolge hervor, die der Führungsebene des Kunden wichtig wären. Verbinde jeden mit einem Geschäftsergebnis.
4. **Herausforderungen und wie wir sie angegangen sind** – Sei transparent über aufgetretene Probleme. Zeige, dass sie bewältigt wurden und was gelernt wurde. Probleme zu verbergen untergräbt das Vertrauen.
5. **Was als Nächstes kommt** – Vorausschauende Ziele für das nächste Quartal, abgestimmt auf die sich wandelnden Geschäftsprioritäten des Kunden.

### Schritt 3: ROI hervorheben

ROI ist das Kernstück jedes QBR auf Executive-Ebene. Strukturiere ihn anhand von Belegen, die der Kunde validieren kann.

**ROI-Framework:**

| ROI-Typ | Berechnungsansatz | Belegquelle |
| --- | --- | --- |
| **Zeitersparnis** | Eingesparte Stunden pro Woche × Anzahl der Nutzer × Stundenkosten (vom Kunden angegeben oder vereinbarter Satz) | Nutzungsdaten, Workflow-Vergleich |
| **Kostenvermeidung** | Kosten, die ohne das Produkt angefallen wären (z. B. zusätzliche Stellen, Tool-Lizenzen) | Schätzung des Kunden, Branchenreferenz |
| **Umsatzwirkung** | Beeinflusste Pipeline, beschleunigte Deals, dem Produkt zurechenbare Conversion-Verbesserungen | CRM-Daten, Zuordnung durch den Kunden |
| **Risikominderung** | Vermiedene Compliance-Vorfälle, Sicherheitsverbesserungen, Audit-Bereitschaft | Einschätzung des Kunden, Support-Daten |
| **Effizienzgewinne** | Prozessverbesserungen, Fehlerreduktion, Automatisierung manueller Aufgaben | Vorher/Nachher-Workflow-Vergleich |

**Kritische Regel**: Behaupte nur ROI, den der Kunde bestätigt hat oder validieren kann. Erfinde niemals ROI-Zahlen. Wenn der ROI nicht quantifizierbar ist, nutze qualitative Belege – „euer Team berichtet, dass..." oder „basierend auf eurem Feedback in unserem letzten Check-in...".

### Schritt 4: Die Agenda vorbereiten

Ein QBR sollte ein Gespräch sein, keine Präsentation. Strukturiere die Agenda so, dass das Engagement der Führungsebene sichergestellt ist.

| Agenda-Abschnitt | Dauer (Vorschlag) | Zweck |
| --- | --- | --- |
| **Geschäftskontext** | 5–10 Min. | Kunde teilt seine aktuellen Prioritäten und etwaige Änderungen seit dem letzten Quartal |
| **Gelieferter Wert** | 10–15 Min. | CSM präsentiert die Werterzählung (Schritt 2) mit Metriken |
| **ROI-Review** | 5–10 Min. | ROI-Belege durchgehen; den Kunden um Validierung bitten |
| **Herausforderungen & Feedback** | 5–10 Min. | Offene Diskussion darüber, was besser sein könnte; Probleme proaktiv ansprechen |
| **Produkt-Roadmap-Alignment** | 5–10 Min. | Relevante kommende Funktionen teilen; Input des Kunden einholen |
| **Vorausplan** | 10–15 Min. | Ziele für das nächste Quartal, Erfolgsmetriken und Action Items vereinbaren |

**Gesamt**: 40–70 Minuten, je nach Account-Komplexität.

Passe das Timing an das Publikum an. Executive-Sponsoren wollen die Zusammenfassung und das „Was bedeutet das" – überspringe granulare Nutzungsdaten, sofern nicht danach gefragt wird. Operative Stakeholder wollen die Details.

### Schritt 5: Das QBR-Dokument entwerfen

Verwende die untenstehende Output-Vorlage. Das Dokument dient sowohl als Präsentationsrahmen als auch als Protokoll nach dem Meeting.

## Output-Vorlage — QBR-Dokument

```
QUARTERLY BUSINESS REVIEW
Account: [Name]
Zeitraum: [Q_ 20__]
QBR-Datum: [Datum]
Erstellt von: [CSM-Name]
Teilnehmer: [Liste]

EXECUTIVE SUMMARY:
  [Zusammenfassung in 3–5 Sätzen: was erreicht wurde, zentrales Highlight, Fokus für die Zukunft]

GESCHÄFTSKONTEXT:
  Kundenprioritäten in diesem Quartal: [aus dem Input des Kunden]
  Wesentliche Änderungen seit dem letzten QBR: [organisatorische, strategische oder Marktänderungen]

GELIEFERTER WERT:
  Ziel 1: [vom Kunden genanntes Ziel]
    Status: [Erreicht / Auf Kurs / Im Rückstand / Überarbeitet]
    Beleg: [konkrete Metriken oder Ergebnisse]
    Wirkung: [geschäftliche Bedeutung]

  Ziel 2: [vom Kunden genanntes Ziel]
    Status: [...]
    Beleg: [...]
    Wirkung: [...]

  [Für jedes Ziel wiederholen]

NUTZUNGS- & ADOPTIONS-HIGHLIGHTS:
  Aktive Nutzer: [aktuell] vs. [Vorquartal] ([Trend])
  Feature-Adoption: [zentrale Features und Adoptionsraten]
  Nutzungstrend: [Zusammenfassung mit Richtungsindikatoren]

ROI-ZUSAMMENFASSUNG:
  [ROI-Typ 1]: [quantifizierter oder qualitativer Beleg]
  [ROI-Typ 2]: [quantifizierter oder qualitativer Beleg]
  Geschätzter Gesamtwert: [sofern quantifizierbar, mit Methodikhinweis]
  Validierung durch Kunden: [bestätigt / Validierung ausstehend / nur qualitativ]

ERFOLGE IN DIESEM QUARTAL:
  1. [konkreter Erfolg mit Geschäftswirkung]
  2. [konkreter Erfolg mit Geschäftswirkung]
  3. [konkreter Erfolg mit Geschäftswirkung]

HERAUSFORDERUNGEN & LÖSUNG:
  1. [Herausforderung] → [wie sie angegangen wurde] → [aktueller Status]
  2. ...

PRODUKT-ROADMAP-ALIGNMENT:
  Kommende Funktionen relevant für [Account]:
  - [Feature/Funktion] — [erwarteter Zeitrahmen] — [Relevanz für den Kunden]
  Kundenfeedback / -anfragen:
  - [Anfrage] — [Status in der Roadmap]

VORAUSPLAN — NÄCHSTES QUARTAL:
  Ziel 1: [Beschreibung] — Erfolgsmetrik: [wie wir messen] — Verantwortlich: [Name]
  Ziel 2: [Beschreibung] — Erfolgsmetrik: [...] — Verantwortlich: [...]
  Ziel 3: [Beschreibung] — Erfolgsmetrik: [...] — Verantwortlich: [...]

ACTION ITEMS:
  | Aktion | Verantwortlich | Fällig am |
  |--------|----------------|-----------|
  | [Aktion] | [Name] | [Datum] |
  | [Aktion] | [Name] | [Datum] |

NÄCHSTES QBR: [vorgeschlagenes Datum]
```

## Leitplanken

- Erfinde niemals Metriken, Adoptionsraten oder ROI-Zahlen. Alle Account-Daten müssen vom Nutzer, aus einer verbundenen MCP-Quelle oder aus companyRAG-Collections stammen. Fehlen Daten, markiere die Felder als [DATEN BENÖTIGT].
- Generiere niemals ROI-Behauptungen ohne vom Kunden bestätigbare Belege. Verwende eine qualitative Formulierung, wenn keine quantitativen Daten verfügbar sind.
- Stelle Roadmap-Punkte niemals als Zusagen dar. Verwende „geplant" oder „auf unserer Roadmap" – niemals „wird geliefert bis".
- Versieh jede Aussage mit einem Quellen-Label: [Aus Account-Daten], [Aus QBR-Framework], [Vom Kunden gemeldet] oder [CSM-Beobachtung].

> **Tipp:** Frage über companyFILES nach einer PPTX-Ausgabe, um eine formatierte, verteilfertige Präsentation zu erhalten.
