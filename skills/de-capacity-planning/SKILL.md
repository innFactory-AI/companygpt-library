---
name: de-capacity-planning
description: Plant Ressourcen- und Personalkapazität mit Nachfrageprognose und Auslastungsanalyse. Verwende ihn, wenn du Personalbedarf planst, Arbeitslasten über Teams hinweg ausbalancierst oder den Ressourcenbedarf für anstehende Projekte prognostizierst. Auslösen mit "Kapazität planen für", "haben wir genug Leute", "Ressourcenprognose für".
---

# Kapazitätsplanung-Skill

Bewerte Personal- und Ressourcenkapazität gegenüber der prognostizierten Nachfrage — mit Auslastungsanalyse, Lückenidentifikation und Szenariomodellierung. Die zugrunde liegenden Zahlen kommen von dir, aus einer angebundenen Quelle oder aus hochgeladenen Dateien.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt- / Ressourcen-Tools über MCP** (z. B. Jira, Asana, Monday) | Aktuelle Allokationen, Projektpläne, Meilensteine, offene Arbeit |
| **HRIS über MCP** (z. B. Personio, Workday) | Headcount, FTE-Äquivalente, Abwesenheiten, Skill-Profile |
| **companyRAG-Sammlungen** | Historische Auslastungsdaten, frühere Kapazitätspläne, Planungsleitlinien |
| **Datei-Upload (CSV/XLSX)** | Auslastungstabellen, Demand-Pipelines, Headcount-Listen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Framework zur Kapazitätsbewertung

### Bestandsaufnahme der Kapazität (Supply)

Bevor du die Nachfrage prognostizierst, halte fest, welche Kapazität aktuell vorhanden ist. Erfasse für jedes Team oder jeden Ressourcenpool:

1. Headcount: Anzahl der Personen, FTE-Äquivalente (berücksichtige Teilzeit, externe Kräfte, geteilte Ressourcen)
2. Verfügbare Stunden: Gesamtarbeitsstunden minus geplante Abwesenheiten, Feiertage, Schulungstage, administrativer Overhead
3. Skill-Profil: Fähigkeiten pro Person oder Rolle — welche Art von Arbeit jede Ressource erbringen kann
4. Aktuelle Allokation: Bestehende Verpflichtungen nach Projekt, BAU (Business-as-usual) und Support
5. Auslastungsgrad: (Allozierte Stunden ÷ Verfügbare Stunden) × 100 — berechnet aus den eigenen Daten der Organisation

### Auslastungsklassifizierung

| Band | Auslastung | Interpretation | Maßnahme |
| --- | --- | --- | --- |
| **Unterausgelastet** | Unter dem Zielband | Kapazität für neue Arbeit oder Umverteilung verfügbar | Passende Arbeit identifizieren; auf Skill-Mismatches prüfen |
| **Zielband** | Von der Organisation definierter Optimalbereich | Gesunder Betriebszustand mit Puffer für ungeplante Arbeit | Beibehalten; auf Abweichungen überwachen |
| **Überausgelastet** | Über dem Zielband | Anhaltendes Überlastungsrisiko — Gefahr für Qualität, Moral und Fluktuation | Umverteilen, verschieben oder aufstocken |

Das Zielband ist organisationsspezifisch. Nimm keinen Standardwert an. Bitte die Nutzerin oder den Nutzer, das Zielband für die Auslastung zu definieren. Ist es nicht definiert, fordere zur Festlegung auf — basierend auf den historischen Daten und der Toleranz gegenüber ungeplanter Arbeit.

### Kapazitätsberechnung

Für jedes Team oder jeden Ressourcenpool:

```
KAPAZITÄTSÜBERSICHT:
  Team/Pool:               [Name]
  Headcount (FTE):         [aus Org-Daten]
  Verfügbare Stunden/Periode: [Gesamtarbeitsstunden - Abwesenheiten - Overhead]
  Aktuell alloziert:       [für bestehende Arbeit gebundene Stunden]
  Verbleibende Kapazität:  [verfügbar - alloziert]
  Auslastungsgrad:         [alloziert ÷ verfügbar × 100]%
  Auslastungsband:         [Unter / Ziel / Über]
```

Aggregiere über die Teams hinweg zu einer organisationsweiten Kapazitätssicht. Markiere Teams, deren Auslastungsbänder stark voneinander abweichen — ein Team unterausgelastet, während ein anderes überausgelastet ist, signalisiert eine Umverteilungschance.

## Nachfrageprognose

### Identifikation der Nachfragequellen

Katalogisiere alle Quellen, die Nachfrage auf den Ressourcenpool ausüben:

| Quellentyp | Beispiele | Vorhersagbarkeit |
| --- | --- | --- |
| **Zugesagte Projekte** | Freigegebene Roadmap-Punkte, unterschriebene Verträge, regulatorische Fristen | Hoch — bekannter Umfang und Zeitplan |
| **Pipeline-Projekte** | Angebote in Arbeit, ausstehende Budgetfreigaben | Mittel — nach Freigabewahrscheinlichkeit gewichten |
| **BAU / Run-the-Business** | Support, Wartung, operative Aufgaben, wiederkehrendes Reporting | Hoch — historischen Durchschnitt mit saisonaler Anpassung nutzen |
| **Ungeplant / reaktiv** | Incidents, Ad-hoc-Anfragen, Prioritäten der Führung | Niedrig — Kapazität auf Basis historischer Häufigkeit reservieren |
| **Strategische Initiativen** | Transformationsprogramme, Markteintritt, M&A-Integration | Variabel — szenarioabhängig |

### Quantifizierung der Nachfrage

Für jede Nachfragequelle:

1. Aufwand schätzen: Stunden oder FTEs pro Periode. Nutze bei unsicheren Posten eine Drei-Punkt-Schätzung (optimistisch, wahrscheinlich, pessimistisch).
2. Nach Wahrscheinlichkeit gewichten: Multipliziere bei Pipeline-Posten den Aufwand mit der Materialisierungswahrscheinlichkeit. Zugesagt = 100 %, Pipeline = historische Conversion-Rate der Organisation.
3. Timing zuordnen: Wann trifft die Nachfrage ein? Verteile sie nach Projektplänen über die Perioden.
4. Skill-Anforderungen identifizieren: Welche Fähigkeiten erfordert jede Nachfragequelle? Gleiche sie mit dem Skill-Profil der Supply-Seite ab.

### Drei-Punkt-Schätzung

Nutze für unsichere Nachfrageposten:

```
Erwarteter Aufwand = (Optimistisch + 4 × Wahrscheinlich + Pessimistisch) ÷ 6
Standardabweichung  = (Pessimistisch - Optimistisch) ÷ 6
```

Das ergibt einen gewichteten Durchschnitt, der die Schätzunsicherheit berücksichtigt. Die Standardabweichung zeigt die Konfidenz an — große Spannen zwischen optimistisch und pessimistisch signalisieren hohe Unsicherheit, die über Szenariomodellierung statt über Einzelpunkt-Planung adressiert werden sollte. Führe diese Rechnungen anhand der bereitgestellten Zahlen durch und zeige deinen Rechenweg, damit er überprüfbar bleibt.

## Lückenanalyse

### Supply-Demand-Vergleich

Für jede Periode und Skill-Kategorie:

```
LÜCKENANALYSE:
  Periode:             [Zeitfenster]
  Skill-Kategorie:     [Rollentyp oder Fähigkeit]
  Supply (FTE):        [verfügbare Kapazität aus der Bestandsaufnahme]
  Demand (FTE):        [prognostizierte, wahrscheinlichkeitsgewichtete Nachfrage]
  Lücke:               [Supply - Demand; positiv = Überschuss, negativ = Unterdeckung]
  Konfidenz:           [Hoch / Mittel / Niedrig je nach Schätzspanne]
  Lückenklassifizierung: [Überschuss / Ausgeglichen / Moderate Unterdeckung / Kritische Unterdeckung]
```

### Lückenklassifizierung

| Klassifizierung | Bedingung | Risikoniveau |
| --- | --- | --- |
| **Überschuss** | Supply übersteigt Demand um mehr als den Puffer für ungeplante Arbeit | Niedrig — aber auf Kosteneffizienz achten |
| **Ausgeglichen** | Supply deckt Demand innerhalb des Puffers für ungeplante Arbeit | Niedrig — gesunder Betriebszustand |
| **Moderate Unterdeckung** | Demand übersteigt Supply bis zur von der Organisation definierten Schwelle | Mittel — adressierbar durch Priorisierung oder temporäre Aufstockung |
| **Kritische Unterdeckung** | Demand übersteigt Supply über die Schwelle hinaus | Hoch — erfordert sofortiges Handeln: Scope-Reduktion, Fristverlängerung oder Ressourcenbeschaffung |

Die Schwelle zwischen moderat und kritisch ist organisationsspezifisch. Fordere zur Definition auf, falls sie nicht festgelegt ist.

## Szenariomodellierung

Baue mindestens drei Szenarien, um den Kapazitätsplan zu stresstesten:

### Szenariostruktur

| Szenario | Demand-Annahme | Supply-Annahme | Zweck |
| --- | --- | --- | --- |
| **Base Case** | Zugesagt + wahrscheinlichkeitsgewichtete Pipeline | Aktueller Headcount + freigegebene Einstellungen | Wahrscheinlichstes Ergebnis |
| **Hohe Nachfrage** | Zugesagt + gesamte Pipeline bei 100 % + Aufschlag für ungeplante Nachfrage | Aktueller Headcount + freigegebene Einstellungen | Stresstest für Nachfragespitze |
| **Eingeschränkte Supply** | Demand des Base Case | Aktueller Headcount minus Fluktuationsschätzung, keine Neueinstellungen | Auswirkung von Einstellungsstopp oder Fluktuationsspitze |

Führe für jedes Szenario die Lückenanalyse durch und dokumentiere:

- Welche Teams oder Skill-Kategorien zuerst in die kritische Unterdeckung geraten
- An welchem Punkt der Timeline die Lücke unkontrollierbar wird
- Welche Hebel verfügbar sind (siehe Empfehlungs-Framework unten)

Ergänze nach Bedarf organisationsspezifische Szenarien (z. B. M&A-Integration, Marktexpansion, Technologiemigration).

## Empfehlungs-Framework

Wenn Lücken identifiziert sind, bewerte Gegenmaßnahmen in dieser Prioritätsreihenfolge:

| Priorität | Hebel | Vorlaufzeit | Kostenwirkung | Reversibilität |
| --- | --- | --- | --- | --- |
| 1 | **Nachfrage neu priorisieren** | Sofort | Keine | Hoch |
| 2 | **Über Teams umverteilen** | Tage–Wochen | Niedrig | Hoch |
| 3 | **Effizienz verbessern** | Wochen–Monate | Niedrig–Mittel | Hoch |
| 4 | **Temporäre Aufstockung** (externe Kräfte, Dienstleister) | Wochen | Mittel–Hoch | Hoch |
| 5 | **Feste Einstellung** | Monate | Hoch | Niedrig |
| 6 | **Arbeit verschieben oder descopen** | Sofort | Variabel | Mittel |

Für jede Empfehlung:

```
EMPFEHLUNG:
  Adressierte Lücke:    [welche Unterdeckung dies abmildert]
  Hebel:                [aus der Prioritätstabelle]
  Konkrete Maßnahme:    [konkreter Schritt — nicht "mehr Leute einstellen", sondern "2 Senior-Backend-Engineers bis Q3 einstellen"]
  Umsetzungsaufwand:    [Zeit und Ressourcen zur Umsetzung des Hebels]
  Erwartete Wirkung:    [FTE-Äquivalent oder zurückgewonnene Stunden]
  Timeline:             [wann die Kapazität verfügbar wird]
  Risiko:               [was das Gelingen verhindern könnte]
  Abhängigkeiten:       [Freigaben, Budget, Marktverfügbarkeit]
```

## Ausgabevorlage

Strukturiere den finalen Kapazitätsplan wie folgt:

```
# Kapazitätsplan — [Team/Organisation] — [Periode]

## Executive Summary
- Aktuelle Auslastung: [aggregierter Wert und Band]
- Prognostizierte Nachfrage: [gesamte FTE-Nachfrage für den Planungszeitraum]
- Lückenbewertung: [Anzahl Teams/Skills in Unterdeckung]
- Hauptrisiko: [größtes Kapazitätsrisiko]
- Primäre Empfehlung: [wirkungsstärkste Maßnahme]

## Bestandsaufnahme (Supply)
[Kapazitätsübersichten je Team]

## Nachfrageprognose
[Quantifizierung je Quelle mit Timing]

## Lückenanalyse
[Lückenklassifizierung je Periode, je Skill]

## Szenarioanalyse
[Ergebnisse von Base Case, hoher Nachfrage, eingeschränkter Supply]

## Empfehlungen
[Priorisierte Maßnahmen mit erwarteter Wirkung]

## Annahmen und Einschränkungen
[Alle während der Analyse getroffenen Annahmen dokumentieren]

## Review-Kadenz
[Wann dieser Plan aktualisiert werden sollte — typischerweise quartalsweise oder bei wesentlichen Änderungen]
```

## An dein Geschäft anpassen

Passe diesen Skill an deine Organisation an, indem du Folgendes definierst:

- Ziel-Auslastungsband: Dein Optimalbereich (z. B. 75–85 %) und die Begründung dahinter
- Planungshorizont: Wie weit du vorausplanst (quartalsweise, halbjährlich, jährlich)
- Nachfrage-Wahrscheinlichkeitsschwellen: Deine Conversion-Raten von Pipeline zu zugesagter Arbeit
- Schwelle für kritische Unterdeckung: Die Lückengröße, die eine Eskalation auslöst
- Puffer für ungeplante Arbeit: Anteil der Kapazität, der für reaktive Arbeit reserviert wird (auf Basis historischer Daten)
- Fluktuationsannahmen: Erwartete Fluktuationsrate für die Supply-Modellierung
- Freigabe-Workflows: Wer welchen Gegenmaßnahmen-Hebel autorisiert

## Leitplanken

- Erzeuge niemals Headcount-Benchmarks, Staffing-Ratios oder Auslastungsziele aus Trainingsdaten. Alle Zahlen müssen aus den Organisationsdaten der Nutzerin oder des Nutzers stammen.
- Nimm niemals ein "Standard"-Auslastungsziel an. Bitte um die Definition des Zielbands.
- Erfinde niemals Pipeline-Daten oder Nachfrageprognosen. Alle Demand-Eingaben kommen vom Nutzer. Sind die Daten unzureichend, gib "unzureichende Daten zur Prognose" an, statt zu extrapolieren.
- Kennzeichne erzeugte Inhalte: `[Aus Org-Daten]`, `[Framework-Methodik]`, `[KI-Schätzung — überprüfen]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Kapazitätsplan zu erhalten.
