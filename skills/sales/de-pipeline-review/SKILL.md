---
name: de-pipeline-review
description: Analysiere die Deal-Gesundheit, decke veraltete oder gefährdete Opportunities auf und erstelle einen priorisierten wöchentlichen Aktionsplan. Verwende ihn zur Vorbereitung auf ein Pipeline-Review-Meeting, zur Bewertung der Forecast-Genauigkeit oder zum Aufspüren festgefahrener Deals. Auslösen mit "Pipeline reviewen", "Pipeline-Gesundheitscheck", "Deal-Risikoanalyse".
---

# Pipeline-Review-Skill

Diagnostiziere die Gesundheit von Pipeline und Deals, qualifiziere Opportunities und erstelle Forecasts mit komplexitätsbasierten Frameworks (von BANT bis zum vollständigen MEDDPICC). Alle Deal- und Pipeline-Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Deal-Stages, Werte, Verantwortliche, Days-in-Stage, Abschlusshistorie, Kontakt-Engagement |
| **Analytics- / Forecasting-Tools über MCP** | Conversion Rates, historische Abschlussdaten, Pipeline-Snapshots im Zeitverlauf |
| **companyRAG / Datei-Upload (CSV/XLSX)** | Exportierte Pipeline-Reports, Deal-Notizen, Qualifizierungs-Frameworks, Analysen verlorener Deals |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Bewertung der Sales-Motion-Komplexität

Bewerte die Komplexität des Deals entlang von vier Dimensionen. Alle Schwellenwerte sind relativ zu den eigenen Normen des Kunden -- niemals absolute Werte.

| Dimension | Niedrig | Mittel | Hoch |
| --- | --- | --- | --- |
| **Länge des Sales-Cycle** | Deutlich unter dem Kundendurchschnitt | Etwa im Kundendurchschnitt | Deutlich über dem Kundendurchschnitt |
| **Deal-Wert** | Unter dem Kundendurchschnitt | Etwa im Kundendurchschnitt | Deutlich über dem typischen Bereich des Kunden |
| **Anzahl Stakeholder** | Einzelkontakt oder kleine Gruppe | Definiertes Buying Center | Funktionsübergreifendes Buying Committee |
| **Lösungskomplexität** | Einzelprodukt/-service, Standard | Etwas Customizing, Multi-Produkt | Individuelle Lösung, abteilungsübergreifend |

### Komplexitäts-Routing

```
Bewerte die 4 Dimensionen für diesen Deal (relativ zu den eigenen Normen des Kunden):

  Überwiegend LOW (niedrig) über die Dimensionen hinweg
    --> BANT-Qualifizierung + Status-basiertes Forecasting
    --> 3-Punkte-Scoring (Weak / Adequate / Strong)
    --> Historische Conversion Rates je Status bestimmen den Forecast

  Mischung aus LOW und MEDIUM, oder überwiegend MEDIUM (mittel)
    --> BANT+ oder vereinfachtes MEDDPICC + Meilenstein-basiertes Forecasting
    --> 0-3-Scoring je ausgewähltem Element
    --> Forecast-Wahrscheinlichkeit an Meilenstein-Erreichung gekoppelt

  Mehrere HIGH-Dimensionen, oder HIGH (hoch) bei Stakeholder/Wert/Lösung (Cycle-Länge allein eskaliert nicht), oder MEDIUM über alle vier
    --> Vollständiges MEDDPICC (alle 8 Elemente) + Wahrscheinlichkeitsbasiertes Forecasting
    --> 0-3-Scoring mit Verhaltensankern
    --> Stage-Wahrscheinlichkeits-Framework mit Szenarioanalyse
```

Gemischte Sales Motions: Wenn ein Kunde über verschiedene Komplexitätsstufen hinweg verkauft, segmentiere die Pipeline und wende je Segment die passende Methodik an. Nutzer können jederzeit auf ein detaillierteres oder weniger detailliertes Framework wechseln.

## BANT-Qualifizierungs-Framework

Für Deals mit niedriger Komplexität. Bewerte jedes Element auf einer 3-Punkte-Skala:

| Element | Weak (1) | Adequate (2) | Strong (3) |
| --- | --- | --- | --- |
| **Budget** | Keine Budget-Diskussion | Budget-Rahmen anerkannt | Budget bestätigt und zugewiesen |
| **Authority** | Entscheider unbekannt | Entscheider identifiziert | Entscheider eingebunden und unterstützend |
| **Need** | Pain vage benannt | Bedarf mit Business Impact formuliert | Bedarf quantifiziert mit Dringlichkeitstreiber |
| **Timeline** | Kein Zeitrahmen besprochen | Grober Zeitrahmen genannt | Konkrete Frist mit auslösendem Ereignis |

**Advancement-Schwelle**: Alle Elemente Adequate (2) oder höher. Jedes Element mit Weak (1) löst eine Gap-Analyse aus (siehe unten).

Nutze für mittlere Komplexität das BANT+ / vereinfachte MEDDPICC-Routing aus dem Komplexitätsabschnitt oben; ausführliche Rubriken und Fragenkataloge sollten denselben Evidenzstandards folgen wie die Tabellen in diesem Skill.

## MEDDPICC-Scoring-Framework

Für Deals mit hoher Komplexität. Bewerte jedes der 8 Elemente auf einer 0-3-Skala:

| Score | Definition |
| --- | --- |
| **0** | Nicht identifiziert -- keine Informationen verfügbar |
| **1** | Identifiziert, aber unbestätigt -- erwähnt, aber nicht mit Belegen bestätigt |
| **2** | Bestätigt und eingebunden -- über direkte Interaktion oder Dokumentation bestätigt |
| **3** | Vollständig validiert und mobilisiert -- unterstützt den Deal aktiv mit nachweisbaren Handlungen |

Anwenden auf: **M**etrics, **E**conomic Buyer, **D**ecision Criteria, **D**ecision Process, **P**aper Process, **I**mplicate the Pain, **C**hampion, **C**ompetition.

Nutze die 0-3-Definitionen oben als Verhaltensanker; entwirf für jedes niedrig bewertete Element gezielte Discovery-Fragen, die nach belegbaren Nachweisen suchen (wer hat wann bestätigt, welches Artefakt oder Meeting).

### Vereinfachtes MEDDPICC für mittlere Komplexität

Wähle eine Teilmenge der Elemente basierend auf historischen Fehlerursachen:

1. Historische Fehlerursachen identifizieren : Was hat die letzten 3-5 verlorenen Deals des Kunden verursacht?
2. Fehler auf MEDDPICC-Elemente mappen : Jeder Fehler verweist auf das Element, das ihn aufgefangen hätte
3. Diese Elemente priorisieren : Die richtige Teilmenge hängt von der Deal-Dynamik des Kunden ab
4. Mit der 0-3-Skala oben bewerten

Wenn keine Fehlerdaten verfügbar sind, beginne mit: Metrics, Economic Buyer, Champion, Decision Process.

## SPIN als Discovery-Werkzeug

SPIN (Situation, Problem, Implication, Need-payoff) SPEIST IN die Qualifizierung EIN -- es ist kein eigenständiges Framework. Jeder Fragetyp ist bestimmten Qualifizierungslücken zugeordnet:

| SPIN-Typ | Speist ein (BANT) | Speist ein (MEDDPICC) |
| --- | --- | --- |
| **Situation** | Authority, Timeline | Economic Buyer, Decision Process |
| **Problem** | Need | Implicate the Pain, Metrics |
| **Implication** | Need (Dringlichkeit), Budget | Metrics, Champion |
| **Need-payoff** | Budget (Wertbegründung) | Decision Criteria, Metrics |

Nutze SPIN, um Lücken bei Elementen mit Score 0-1 (MEDDPICC) oder Weak (BANT) zu schließen, indem du die Fragetypen den Qualifizierungslücken aus der SPIN-Tabelle oben zuordnest.

## Entscheidungsbaum für die Gap-Analyse

Für jedes Element, das unter dem Schwellenwert bewertet wurde:

```
Element unter Schwellenwert bewertet
  |
  +--> Erste Bewertung?
  |      JA --> Gezielte SPIN-Discovery-Fragen generieren
  |             Touchpoint planen, nach der Discovery neu bewerten
  |
  +--> Discovery versucht, aber Element bleibt niedrig?
  |      JA --> Eskalations-Check:
  |             - Lücke blockiert den Deal-Fortschritt? (Stage-Gate-Verletzung)
  |             - Besteht seit >1 Review-Zyklus?
  |             - 3+ Elemente gleichzeitig niedrig?
  |             |
  |             IRGENDEIN JA --> Als gefährdet markieren. Empfehlen: Einbindung
  |                              des Executive Sponsors, Champion-Aufbau oder
  |                              Disqualifikations-Review
  |             ALLE NEIN --> Discovery fortsetzen, Vorgehen anpassen
  |
  +--> Niedrig über 3+ Review-Zyklen?
         JA --> Festgefahrener Deal. Expliziter Disqualifikations-Review:
                "Was müsste sich ändern?"
                Falls unklar --> starkes Disqualifikationssignal
```

## Deal-Gesundheit vs. Deal-Risiko

Zwei eigenständige Bewertungen, die zusammenwirken:

**Deal-Gesundheit** (Vollständigkeit der Qualifizierung): Wissen wir genug über diesen Deal?

- BANT: Summe der Scores / 12. Jedes Weak = Gelb, 2+ Weak = Rot.
- MEDDPICC: Summe der Scores / 24. Kritische Elemente gewichten, falls der Kunde dies vorgibt.

**Deal-Risiko** (Pipeline-Risiko): Wird dieser Deal pünktlich und zum erwarteten Wert abschließen?

| Faktor | Bewertungsmethode |
| --- | --- |
| **Days-in-Stage** | Vergleich mit dem historischen Durchschnitt des Kunden für diese Stage |
| **Vollständigkeit der Qualifizierung** | Der Deal-Gesundheits-Score fließt hier ein |
| **Aktualität des Engagements** | Zeit seit der letzten substanziellen Kundeninteraktion |
| **Stakeholder-Abdeckung** | Eingebundene Stakeholder vs. typisch für diese Deal-Größe |
| **Wettbewerbspräsenz** | Aktiver Wettbewerb ohne Differenzierungsstrategie = Risiko |
| **Klarheit der nächsten Schritte** | Kein definierter, vereinbarter nächster Schritt mit Datum = Risikomarker |

Zusammengesetztes Risiko: Gewichte die Faktoren nach dem, was in den historischen Daten des Kunden am aussagekräftigsten ist. Klassifiziere als niedriges / mittleres / hohes Risiko.

**Stage-Alignment**: Vergleiche die Deal-Gesundheit mit den Erwartungen der Pipeline-Stage. Definiere je Stage: "Was muss zutreffen, um voranzukommen?" Abweichung = Risikomarker.

## Pipeline-Coverage-Analyse

Coverage Ratio -- ABGELEITET aus den eigenen Daten des Kunden, niemals vorgegeben.

1. Historische Conversion Rate : Closed-Won-Deals / Gesamtzahl der in die Pipeline eintretenden Deals (vom Kunden festgelegter Zeitraum)
2. Coverage ableiten : Coverage = 1 / Conversion Rate
3. Segmentieren, falls Raten variieren : Nach Deal-Typ, Quelle, Rep-Erfahrung oder Produktlinie
4. Altersbereinigen : Veraltete Pipeline konvertiert mit niedrigeren Raten -- separate Raten berechnen
5. Aktuelle Coverage : Aktiver Pipeline-Wert / Ziel

**Niemals konkrete Ratios vorgeben.** Vermittle die Berechnung; der Kunde leitet seine eigene Zahl ab.

## Forecast-Kategorien

Abgestimmt auf die Forecasting-Methodik aus dem Komplexitäts-Routing:

**Status-basiert (transaktional)**: Ordne jedem Deal-Status eine historische Close Rate zu. Forecast = Summe von (Wert x Rate). Aus aktuellen Daten neu kalibrieren.

**Meilenstein-basiert (Projekt)**: Meilensteine treiben die Abschlusswahrscheinlichkeit (angepasst an die Meilenstein-Schwierigkeit). Die Umsatzverteilung folgt den Vertragsbedingungen (anteilig, jährlich, bei Lieferung), nicht der Meilenstein-Erreichung selbst.

**Wahrscheinlichkeitsbasiert (komplex)**: Leite Stage-Wahrscheinlichkeiten aus historischen Daten ab. Lege Kategorie-Schwellen (Commit/Best Case/Pipeline) anhand der Konfidenzniveaus des Kunden fest. Führe eine Szenarioanalyse durch: Best Case, Most Likely, Worst Case.

Wende die Status-, Meilenstein- und wahrscheinlichkeitsbasierten Definitionen oben beim Erstellen von Forecast-Modellen an; dokumentiere die Annahmen und kalibriere anhand der historischen Abschlussdaten des Kunden.

**Pipelines mit geringem Volumen**: Wenn der Kunde weniger als 20 Deals pro Stage hat, ist die Standard-Wahrscheinlichkeitskalibrierung unzuverlässig. Optionen: angrenzende Stages zusammenfassen, um die Stichprobe zu vergrößern, Bayessche Glättung mit Priors aus den Gesamt-Pipeline-Raten verwenden oder auf Meilenstein-basiertes Forecasting zurückgreifen, das weniger historisches Volumen erfordert.

## Pipeline-Gesundheitsdiagnostik

Alle Benchmarks relativ zu den eigenen historischen Normen des Kunden. Analysiere vier Dimensionen:

1. Stage-Verteilung : Vergleiche die aktuelle Wertverteilung mit historischen Normen. Ungleichgewichte signalisieren spezifische Probleme (top-heavy = Qualifizierung/Advancement, bottom-heavy = Generierungsdefizit).
2. Velocity : Verfolge Days-per-Stage und Conversion Rates gegen Baselines. Trends zählen mehr als Momentaufnahmen.
3. Aging : Identifiziere Deals, die die typische Cycle-Länge überschreiten. Quantifiziere den Conversion-Abschlag aus den Daten des Kunden.
4. Creation-vs-Close-Balance : Vergleiche erstellte vs. abgeschlossene Deals über rollierende Zeiträume. Anhaltend negative Balance = künftige Lücke.

## Pipeline-Review-Kadenz

| Motion | Kadenz | Fokus | Aktions-Trigger |
| --- | --- | --- | --- |
| **Transaktional** | Tägliche/wöchentliche Snapshots | Conversion-Trends, Volumen, Verschiebungen in der Verteilung | Ratenrückgang vs. historisch, Volumendefizit |
| **Projektbasiert** | Bei Meilenstein-Übergängen | Abschlussraten, Lieferrisiko, Umsatztiming | Meilenstein-Verzögerungen, Scope-Änderungen |
| **Komplex** | Wöchentlich Deals + monatlich Pipeline-Form + quartalsweise Genauigkeit | Festgefahrene Deals, Stage-Verteilung, Forecast vs. Ist | Risikoeskalation, Formungleichgewicht, Forecast-Abweichung |

## Ausgabe der Qualifizierungsprüfung

Skaliere den Detailgrad nach Komplexität: Leichtgewichtig (BANT) liefert Scores + Advance/Hold/Disqualify. Standard ergänzt Belege, Gap-Analyse mit SPIN-Fragen und Stage-Alignment. Umfassend (vollständiges MEDDPICC) ergänzt Konfidenzniveaus je Element (Hoch/Mittel/Niedrig), gewichtetes Gesundheits-Scoring und Trigger zur Risikoeskalation.

Alle Reviews müssen Belegquellen-Tags enthalten: [Aus CRM/Nutzereingabe], [Aus Qualifizierungs-Framework], [KI-Einschätzung].

## Leitplanken

1. Erzeuge niemals Deal- oder Pipeline-Daten. Alle Prospect-Informationen, Deal-Werte, Stages und Conversion-Historien müssen vom Nutzer, aus einer angebundenen MCP-Quelle, aus companyRAG-Sammlungen oder aus hochgeladenen Dateien stammen.
2. Keine vorgegebenen Zahlen. Gib niemals Coverage Ratios, Conversion Rates, Stage-Wahrscheinlichkeiten oder Benchmarks vor. Vermittle die Berechnung; der Kunde leitet seine Zahl ab.
3. Quellenkennzeichnung. Versieh jede Aussage mit einem Tag — [Aus CRM/Nutzereingabe], [Aus Qualifizierungs-Framework], [KI-Einschätzung]. Bei Forecasts zusätzlich [Szenarioanalyse].
4. Menschliche Prüfung erforderlich. Füge auf allen Ausgaben "Vor dem Handeln auf Basis von Qualifizierungs-/Risikobewertungen mit der Vertriebsleitung verifizieren" hinzu.

> **Tipp:** Fordere über companyFILES eine XLSX-Ausgabe an, um eine formatierte, sofort verteilbare Tabelle zu erhalten; DOCX oder Markdown eignen sich gut für die schriftliche Review-Zusammenfassung.
