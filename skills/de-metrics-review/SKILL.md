---
name: de-metrics-review
description: Prüft Produktmetriken mit Trendanalyse, Anomalieerkennung und umsetzbaren Empfehlungen. Verwende ihn, wenn du ein Produkt-Review vorbereitest, eine Metrik-Veränderung untersuchst oder das KPI-Tracking für ein neues Feature aufsetzt. Auslösen mit "Produktmetriken prüfen", "warum hat sich [Metrik] verändert", "Metriken-Dashboard reviewen".
---

# Metriken-Review-Skill

Prüfe Produktmetriken, erkenne Anomalien, diagnostiziere Ursachen und übersetze Metrik-Bewegungen in umsetzbare Produktentscheidungen. Alle Metrikdaten stammen von dir, aus angebundenen Analyse-Tools oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Analyse-Tools über MCP** (z. B. Amplitude, Mixpanel, GA4) | Aktuelle und historische Metrikwerte, Funnel-Daten, Segment-Aufschlüsselungen, Event-Streams |
| **companyRAG-Sammlungen** | Metrik-Definitionen, frühere Review-Dokumente, Launch- und Incident-Notizen, KPI-Zielwerte |
| **Datei-Upload (CSV-/XLSX-Exporte)** | Dashboard-Exporte, Kohorten-Tabellen, Roh-Auswertungen aus deinem Analyse-Stack |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Metrik-Hierarchie-Framework

Produktmetriken existieren in einer Hierarchie. Sie zu verstehen verhindert, dass du auf Symptome reagierst und dabei die eigentlichen Ursachen übersiehst.

### Hierarchie-Struktur

```
NORTH STAR METRIC
  Die eine Metrik, die den Kernwert deines Produkts für die Nutzer am besten erfasst.
  Verändert sich langsam. Spiegelt die kumulierte Produktgesundheit wider.
  │
  ├── INPUT-METRIKEN (3-5)
  │     Beeinflussen die North Star direkt. Vom Produktteam beeinflussbar.
  │     Verändern sich wöchentlich/monatlich. Jede entspricht einem Produkt-Hebel.
  │     │
  │     ├── FEATURE-METRIKEN
  │     │     Messen Adoption, Nutzungstiefe und Zufriedenheit eines konkreten Features.
  │     │     Verändern sich täglich/wöchentlich.
  │     │
  │     └── FUNNEL-METRIKEN
  │           Messen die Conversion zwischen wichtigen Produktstufen.
  │           Verändern sich täglich/wöchentlich.
  │
  └── HEALTH-METRIKEN (2-4)
        Dürfen NICHT verfallen, während Input-Metriken optimiert werden.
        Performance, Zuverlässigkeit, Support-Last, Nutzer-Sentiment.
```

### Vorgehen zum Aufbau der Hierarchie

1. North Star identifizieren : Welche einzelne Metrik misst am direktesten, ob dein Produkt seinen Kernwert liefert? Nicht der Umsatz (das ist eine Business-Metrik) — die Aktion oder das Ergebnis, das ZUM Umsatz führt.
2. Input-Metriken zuordnen : Welche Nutzerverhalten treiben die North Star direkt? Jede Input-Metrik sollte umsetzbar sein — das Produktteam kann Interventionen entwerfen, die sie bewegen.
3. Feature-Metriken ergänzen : Was misst für jedes wichtige Feature oder jeden Produktbereich Adoption (probieren Nutzer es aus?), Engagement (nutzen sie es sinnvoll?) und Retention (kommen sie wieder?).
4. Health-Metriken definieren : Was darf NICHT kaputtgehen? Ladezeit, Fehlerraten, Support-Ticket-Volumen, NPS/CSAT. Das sind Leitplanken, keine Ziele.

### Validierung der Hierarchie

Eine gut konstruierte Hierarchie erfüllt diese Checks:

| Check | Bestanden | Nicht bestanden |
| --- | --- | --- |
| **Kausaler Zusammenhang** | Eine Input-Metrik zu bewegen bewegt plausibel die North Star | Input-Metrik korreliert, ist aber nicht kausal |
| **Umsetzbar** | Das Produktteam kann Features/Änderungen entwerfen, die die Input-Metrik bewegen | Metrik wird primär von externen Faktoren beeinflusst |
| **Redundanzfrei** | Jede Input-Metrik erfasst einen eigenen Produkt-Hebel | Zwei Input-Metriken messen dasselbe zugrunde liegende Verhalten |
| **Vollständig** | Zusammen decken die Input-Metriken die wichtigsten Pfade zur North Star ab | Wichtige Treiber sind nicht repräsentiert |
| **Messbar** | Die Metrik lässt sich mit der aktuellen Infrastruktur zuverlässig tracken | Datenquelle nicht verfügbar, unzuverlässig oder unverhältnismäßig teuer |

## Metriken-Review-Workflow

### Schritt 1: Review-Kontext festlegen

Bevor du Zahlen betrachtest, kläre:

- Review-Typ : Routine-Kadenz (wöchentlich/monatlich), Ad-hoc-Untersuchung oder Review eines neuen Feature-Launches?
- Zeitfenster : Welcher Zeitraum wird betrachtet? Vergleichszeitraum einbeziehen (Vorperiode, Jahresvergleich oder Baseline).
- Scope : Gesamtes Produkt, ein bestimmtes Feature, ein bestimmtes Segment oder eine bestimmte Metrik?
- Bekannter Kontext : Gab es im Zeitraum Launches, Incidents, Marketing-Kampagnen, Saisonalität oder externe Ereignisse?

### Schritt 2: Top-Down-Metrik-Scan

Beginne bei der North Star und arbeite dich die Hierarchie hinunter:

```
METRIK-SCAN — [Periode]

North Star: [Metrik-Name]
  Aktuell:   [Wert aus Nutzerdaten]
  Vorher:    [Vergleichswert]
  Änderung:  [absolut und prozentual]
  Trend:     [Richtung über die letzten 3+ Perioden]
  Status:    Auf Kurs / Unter Ziel / Über Ziel / Kein Ziel gesetzt

Input-Metriken:
  [Metrik 1]: [aktuell] vs [vorher] → [Änderung] — [Status]
  [Metrik 2]: [aktuell] vs [vorher] → [Änderung] — [Status]
  ...

Health-Metriken:
  [Metrik 1]: [aktuell] vs [vorher] → [Änderung] — [Status]
  ...
```

**Scan-Disziplin**: Berichte die Zahlen, bevor du sie interpretierst. Menschen verankern sich an der ersten Erzählung, die sie hören — präsentiere zuerst die Daten, dann die Analyse.

### Schritt 3: Anomalieerkennung

Eine Anomalie ist eine Metrik-Bewegung, die merklich vom erwarteten Muster abweicht. "Merklich" wird durch die historische Varianz der Metrik selbst definiert, nicht durch einen universellen Schwellenwert.

**Erkennungskriterien**:

| Anomalie-Typ | Wie erkennen | Bedeutung |
| --- | --- | --- |
| **Plötzlicher Sprung** | Wert springt/fällt um mehr als 2 Standardabweichungen vom gleitenden Mittel | Wahrscheinlich durch ein diskretes Ereignis verursacht — suche danach |
| **Trendbruch** | Richtungsumkehr, die nach einem konsistenten Trend 2+ Perioden anhält | Kann auf eine strukturelle Veränderung hindeuten — Ursache untersuchen |
| **Divergenz** | Input-Metrik bewegt sich, North Star aber nicht (oder umgekehrt) | Deutet darauf hin, dass der Hierarchie-Link schwächer ist als angenommen — Kausalmodell prüfen |
| **Segment-Anomalie** | Gesamtmetrik ist stabil, aber ein bestimmtes Segment zeigt deutliche Veränderung | Verstecktes Problem oder verstecktes Potenzial — in Segmentdaten eintauchen |
| **Saisonale Abweichung** | Metrik weicht von ihrem historischen Saisonmuster ab | Entweder eine echte Veränderung oder ein Kalender-Artefakt — Jahresvergleich heranziehen |

**Berechnung der Standardabweichung**: Nutze die letzten 8-12 Periodenwerte der Metrik selbst, um Mittelwert und Standardabweichung zu bestimmen. Das ist metrikspezifisch — wende niemals einen universellen Schwellenwert an. Reichen die historischen Daten nicht aus (< 8 Perioden), weise darauf hin, dass die Anomalieerkennung unzuverlässig ist, und urteile nach Richtung.

### Schritt 4: Ursachenanalyse

Wende für jede markierte Anomalie das Diagnose-Framework an:

#### 5-Why-Zerlegung

Beginne mit der beobachteten Anomalie und frage iterativ "warum", indem du die Metrik-Hierarchie hinabgehst:

```
ANOMALIE: [Metrik] hat sich in [Periode] um [Betrag] verändert

Warum 1: [Erklärung erster Ebene — welche Input-Metrik hat sich bewegt?]
Warum 2: [Was hat diese Veränderung der Input-Metrik ausgelöst?]
Warum 3: [Welches Nutzerverhalten oder welche Systemänderung hat das verursacht?]
Warum 4: [Was hat dieses Verhalten oder diese Systemänderung ausgelöst?]
Warum 5: [Ursache — das umsetzbare Ereignis, das passiert ist]

Konfidenz: [Hoch / Mittel / Niedrig]
Belege:    [Welche Daten stützen diese Ursache?]
```

**Höre auf zu zerlegen, wenn** du einen umsetzbaren Faktor erreichst, den das Produktteam beeinflussen kann. Ist die Ursache "Wettbewerber hat ein besseres Feature gelauncht", ist der nächste Schritt Reaktionsplanung, nicht weitere Zerlegung.

#### Checkliste der Ursachenkategorien

Prüfe bei der Diagnose systematisch diese Kategorien:

| Kategorie | Check | Häufige Signale |
| --- | --- | --- |
| **Produktänderung** | Wurde in dieser Periode etwas ausgeliefert? | Zeitliche Korrelation mit einem Deployment |
| **Bug / Incident** | Gab es Fehler, Ausfälle oder verschlechterte Performance? | Anstieg der Fehlerrate, Zunahme von Support-Tickets |
| **Traffic-Änderung** | Hat sich Traffic-Volumen oder Quellen-Mix verändert? | Marketing-Kampagne, Presse-Erwähnung, SEO-Verschiebung |
| **Segment-Verschiebung** | Hat sich der Nutzer-Mix verändert? | Neue Kundenkohorte, geografische Expansion, Churn in einem bestimmten Segment |
| **Saisonalität** | Ist das ein bekanntes Saisonmuster? | Jahresvergleich stimmt überein |
| **Externes Ereignis** | Marktereignis, Wettbewerber-Aktion, regulatorische Änderung? | Zeitliche Korrelation mit einem externen Ereignis |
| **Messänderung** | Haben sich Tracking, Definitionen oder Tooling verändert? | Plötzlicher klarer Bruch in den Daten (nicht graduell) |

**Kritischer Check**: Prüfe immer, ob eine Messänderung die Anomalie erklärt, BEVOR du eine echte Produktänderung annimmst. Tracking-Bugs, Definitionsänderungen und Updates von Analyse-Tools sind häufige Quellen für Fehlalarme.

### Schritt 5: Reaktion formulieren

Bestimme für jede bestätigte Anomalie mit diagnostizierter Ursache die Reaktion:

| Ursachen-Typ | Reaktionsmuster |
| --- | --- |
| **Bug / Incident** | Bug beheben. Auswirkungs-Zeitfenster quantifizieren. Monitoring ergänzen, um Wiederholung zu verhindern. |
| **Produktänderung verursachte Regression** | Schweregrad bewerten. Rollback oder Fast-Follow-Fix. Feature-Metriken aktualisieren. |
| **Produktänderung wirkte wie beabsichtigt** | Feiern. Das erfolgreiche Muster dokumentieren. Verstärkung erwägen. |
| **Segment-Verschiebung** | Bewerten, ob die Verschiebung erwünscht ist. Targeting oder Produktprioritäten anpassen. |
| **Wettbewerb / extern** | Auf den Brief-Competitor-Skill verweisen. Strategische Reaktion bewerten. |
| **Saisonalität** | Für künftige Planung notieren. Keine Produktreaktion nötig. |
| **Messproblem** | Tracking korrigieren. Historische Daten neu darstellen. Korrektur an Stakeholder kommunizieren. |

### Ausgabeformat der Reaktion

```
METRIK-REVIEW-ZUSAMMENFASSUNG — [Periode]

HEADLINE: [Ein-Satz-Zusammenfassung des Reviews — der einzelne wichtigste Befund]

METRIKEN-ÜBERSICHT:
  [Top-Down-Scan aus Schritt 2]

ERKANNTE ANOMALIEN: [Anzahl]
  1. [Metrik]: [Änderung] — Ursache: [Erklärung] — Konfidenz: [H/M/N]
     Empfohlene Maßnahme: [konkrete Maßnahme mit Verantwortlichem]
  2. ...

POSITIVE TRENDS:
  [Metriken, die sich in die richtige Richtung bewegen — Erfolge anerkennen]

ZU BEOBACHTEN:
  [Metriken, die noch nicht anomal sind, aber Richtung Problem tendieren]

EMPFEHLUNGEN:
  1. [Maßnahme] — Verantwortlich: [Name] — Priorität: [Hoch/Mittel/Niedrig] — Zeitrahmen: [wann]
  2. ...

OFFENE FRAGEN:
  [Anomalien ohne klare Ursache — zur weiteren Untersuchung zugewiesen]
```

## Metrik-Setup für neue Features

Definiere beim Launch eines neuen Features die Metriken VOR dem Launch mit diesem Framework:

1. Adoption-Metrik : Wie viel Prozent der berechtigten Nutzer probieren das Feature aus? (Misst Awareness und Erst-Nutzungs-Reibung)
2. Activation-Metrik : Wie viel Prozent der Nutzer, die das Feature ausprobieren, schließen die Kernaktion ab? (Misst, ob das Feature sein Versprechen einlöst)
3. Engagement-Metrik : Wie häufig oder wie tief nutzen aktivierte Nutzer das Feature? (Misst den fortlaufenden Mehrwert)
4. Retention-Metrik : Kommen Nutzer, die das Feature adoptieren, wieder? In welcher Kadenz? (Misst nachhaltigen Mehrwert)
5. Impact-Metrik : Korreliert die Feature-Nutzung mit einer Verbesserung der relevanten Input-Metrik? (Validiert die Produkthypothese)

```
FEATURE-METRIK-PLAN — [Feature-Name]
  Adoption:    [Metrik-Definition, Messquelle]
  Activation:  [Metrik-Definition, Messquelle]
  Engagement:  [Metrik-Definition, Messquelle]
  Retention:   [Metrik-Definition, Messquelle]
  Impact:      [Metrik-Definition, Messquelle]
  Baseline:    [in den ersten 2 Wochen nach Launch zu etablieren]
  Review-Datum: [wann erstmals bewerten — typischerweise 2-4 Wochen nach Launch]
```

## Leitplanken

- Erzeuge NIEMALS Metrikwerte, Benchmarks oder Branchendurchschnitte. Alle Zahlen müssen vom Nutzer, aus Analyse-Tools oder aus einer companyRAG-Sammlung stammen.
- Erfinde NIEMALS Ursachen. Ist die Ursache unbekannt, schreibe "Ursache nicht ermittelt — erfordert weitere Untersuchung" und weise eine Recherche-Aufgabe zu.
- Behaupte NIEMALS kausale Zusammenhänge ohne Belege. Korrelation ist eine Hypothese, bis sie durch ein Experiment oder einen klaren Mechanismus bestätigt ist. Prüfe immer, ob eine Mess-/Tracking-Änderung eine Anomalie erklärt, bevor du sie echtem Produktverhalten zuschreibst.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Nutzer-/Analysedaten]`, `[Metrik-Framework]` oder `[KI-Analyse — prüfen]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Review-Dokument zu erhalten.
