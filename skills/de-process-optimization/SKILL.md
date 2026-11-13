---
name: de-process-optimization
description: Analysiert Prozesse auf Engpässe, Verschwendung und Verbesserungspotenziale mit Durchsatzmessung und priorisierten Empfehlungen. Verwende ihn, wenn sich ein Prozess langsam anfühlt, du Ineffizienzen untersuchst oder eine Prozessverbesserung vorbereitest. Auslösen mit "diesen Prozess optimieren", "Engpässe finden in", "wie können wir verbessern".
---

# Prozessoptimierung-Skill

Analysiere Prozesse auf Engpässe und Verschwendung und empfiehl anschließend messbare Verbesserungen mit priorisierten Roadmaps. Prozessdaten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-/Issue-Tracker über MCP** (z. B. Jira, Asana, Monday) | Bearbeitungs- und Durchlaufzeiten, Status-Verweildauern, Volumina, Rückläufer |
| **Workflow-/CRM-System über MCP** (z. B. HubSpot, Salesforce, ServiceNow) | Genehmigungsketten, Übergaben, SLA-Daten, Fehler- und Nacharbeitsraten |
| **companyRAG-Sammlungen / Datei-Upload** | Prozessdokumentation, Runbooks, Audit-Protokolle, Zeit- und Kostenexporte |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Methodik der Prozessanalyse

### Kartierung des Ist-Zustands

Kartiere den Prozess vor jeder Optimierung so, wie er tatsächlich abläuft — nicht so, wie er dokumentiert oder gedacht ist:

1. Prozess End-to-End begehen: Dokumentiere jeden Schritt, Entscheidungspunkt, jede Übergabe, Wartezeit und Nacharbeitsschleife so, wie sie real auftreten.
2. Beteiligte identifizieren: Wer berührt den Prozess in welcher Phase — Rollen, nicht nur Abteilungen.
3. Zeiten erfassen: Erfasse je Schritt die Bearbeitungszeit (aktive Arbeit) und die Durchlaufzeit (Kalenderzeit inklusive Wartezeiten). Die Lücke zwischen beiden offenbart Liege- und Wartezeiten.
4. Volumina notieren: Wie viele Vorgänge durchlaufen den Prozess pro Periode — insgesamt und je Variante.
5. Schmerzpunkte markieren: Wo berichten Beteiligte von Frust, Fehlern oder Workarounds? Das sind Optimierungssignale.

### Durchsatzmessung

Lege Baseline-Kennzahlen fest, bevor du Änderungen empfiehlst:

```
PROZESS-BASELINE:
  Prozess:            [Name]
  Messzeitraum:       [Datumsbereich]
  Volumen:            [bearbeitete Vorgänge pro Periode]
  Zykluszeit:         [durchschnittliche End-to-End-Durchlaufzeit]
  Bearbeitungszeit:   [durchschnittliche aktive Arbeitszeit pro Vorgang]
  Prozesseffizienz:   [Bearbeitungszeit ÷ Zykluszeit × 100]%
  Fehler-/Nacharbeitsrate: [% der Vorgänge, die Nacharbeit oder Korrektur erfordern]
  First-Pass-Yield:   [% der Vorgänge, die im ersten Durchlauf korrekt abschließen]
  Kosten pro Vorgang: [Gesamtprozesskosten ÷ Volumen, falls Daten verfügbar]
```

Das Verhältnis der Prozesseffizienz zeigt, wie viel Zeit auf wertschöpfende Arbeit gegenüber Warten entfällt. Ein Prozess mit 2 Stunden aktiver Arbeitszeit und 5 Tagen Zykluszeit hat eine Prozesseffizienz von rund 5 % — die meiste Zeit wird gewartet, nicht gearbeitet.

## Identifikation von Verschwendung

### Acht-Verschwendungsarten-Framework

Aus der Lean-Methodik für Wissensarbeit und Geschäftsprozesse adaptiert:

| Verschwendungsart | Definition | Prozessindikatoren |
| --- | --- | --- |
| **Warten** | Leerzeit zwischen Schritten — Warteschlangen, Genehmigungen, Informationsanfragen | Vorgänge in Postfächern, Genehmigungsstau, Status "warte auf [Person]" |
| **Überbearbeitung** | Mehr tun als nötig — unnötige Details, redundante Prüfungen, Gold-Plating | Berichte, die niemand liest; Genehmigungen, die nie ablehnen; ungenutzte Daten |
| **Nacharbeit** | Korrektur von Fehlern aus vorherigen Schritten | Hohe Ablehnungsquoten, häufige Überarbeitungszyklen, "Zurück-an"-Muster |
| **Übergabe-Reibung** | Bei Übergaben zwischen Personen/Teams gehen Informationen verloren oder verschlechtern sich | Wiederholte Rückfragen, erneutes Sammeln von Kontext, "Das wusste ich nicht"-Momente |
| **Bewegung** | Unnötiges Wechseln zwischen Tools, Systemen oder Formaten | Copy-Paste zwischen Systemen, manuelle Dateneingabe, Formatkonvertierungen |
| **Überproduktion** | Mehr Output oder häufiger produzieren, als der nachgelagerte Abnehmer braucht | Zu große Losgrößen, häufiger erzeugte Berichte als konsumiert |
| **Bestand** | Vorgänge stauen sich zwischen Schritten — Aufbau von Work-in-Progress | Wachsende Backlogs, alternde Vorgänge, begonnene aber nicht abgeschlossene Vorgänge |
| **Ungenutztes Talent** | Personen arbeiten unter ihrer Qualifikation, oder Expertise wird nicht genutzt | Senior-Mitarbeitende an Routineaufgaben, Spezialwissen nicht konsultiert |

### Verschwendungsbewertung

Für jede identifizierte Verschwendung:

```
VERSCHWENDUNGSPOSTEN:
  Art:           [aus den acht Verschwendungsarten]
  Ort:           [welcher Schritt oder zwischen welchen Schritten]
  Beschreibung:  [was konkret passiert]
  Häufigkeit:    [wie oft — jeder Vorgang, gelegentlich, bestimmte Bedingungen]
  Auswirkung:    [Zeit-, Kosten- oder Qualitätseffekt pro Vorkommen]
  Grundursache:  [warum diese Verschwendung existiert — nicht nur was, sondern warum]
  Beleg:         [Daten, die die Bewertung stützen — Zeiten, Volumina, Fehlerraten]
```

## Engpasserkennung

### Identifikationsmethoden

Ein Engpass ist der Schritt, der den Durchsatz des gesamten Prozesses begrenzt. Der Prozess kann nur so schnell sein wie sein langsamster Schritt.

**Methode 1 — Warteschlangenbeobachtung**: Der Schritt mit der längsten vorgelagerten Warteschlange ist wahrscheinlich der Engpass. Arbeit staut sich vor der Restriktion.

**Methode 2 — Auslastungsanalyse**: Der Schritt, an dem Ressourcen am stärksten ausgelastet sind (nahe 100 %), ist die Restriktion. Andere Schritte haben ungenutzte Kapazität.

**Methode 3 — Vergleich der Flussraten**: Miss den Durchsatz jedes Schritts unabhängig. Der Schritt mit der niedrigsten Durchsatzrate begrenzt den Prozess.

### Engpassklassifizierung

| Typ | Ursache | Beispiel | Lösungsansatz |
| --- | --- | --- | --- |
| **Ressourcen-Engpass** | Nicht genug Personen, Tools oder Kapazität am Schritt | Einzelner Genehmiger für alle Anfragen | Kapazität ergänzen, umverteilen oder Nachfrage reduzieren |
| **Policy-Engpass** | Regeln oder Anforderungen, die den Fluss unnötig einschränken | Genehmigung für Vorgänge unterhalb einer sinnvollen Schwelle | Die Regel hinterfragen — erfüllt sie noch ihren Zweck? |
| **Abhängigkeits-Engpass** | Schritt durch externe Eingabe oder vorgelagerte Lieferung blockiert | Warten auf Drittanbieterdaten vor dem Fortfahren | Entkoppeln, parallelisieren oder Abhängigkeit vorab beschaffen |
| **Batching-Engpass** | Arbeit wird gehalten, bis sich ein Batch ansammelt | Monatliche Rechnungsverarbeitung, wo wöchentlich besser flösse | Losgröße reduzieren oder kontinuierlich verarbeiten |
| **Wissens-Engpass** | Nur bestimmte Personen haben die Expertise für den Schritt | Einzelner Fachexperte für jede Prüfung erforderlich | Cross-Training, dokumentieren oder Spezialisierungsbedarf neu gestalten |

## Identifikation von Verbesserungen

### Verbesserungskategorien

| Kategorie | Beschreibung | Typische Auswirkung | Typischer Aufwand |
| --- | --- | --- | --- |
| **Eliminieren** | Den Schritt ganz entfernen — er schafft keinen Mehrwert | Hoch | Gering (oft nur eine Entscheidung) |
| **Automatisieren** | Manuelle Arbeit durch systemgesteuerte Ausführung ersetzen | Hoch | Mittel–Hoch |
| **Vereinfachen** | Komplexität reduzieren — weniger Felder, einfachere Regeln, kürzere Formulare | Mittel | Gering–Mittel |
| **Parallelisieren** | Sequenzielle Schritte gleichzeitig ausführen, wo keine echte Abhängigkeit besteht | Mittel | Gering–Mittel |
| **Losgröße reduzieren** | Kleinere Batches häufiger verarbeiten für schnelleren Fluss | Mittel | Gering |
| **Standardisieren** | Varianten zu einem einheitlichen Vorgehen zusammenführen | Mittel | Mittel |
| **Verlagern** | Den Schritt früher oder später im Prozess platzieren für besseren Fluss | Gering–Mittel | Gering |

### Five-Whys-Grundursachenanalyse

Wende für jede signifikante Verschwendung oder jeden Engpass eine Grundursachenanalyse an, bevor du Lösungen empfiehlst:

```
PROBLEM: [beobachtetes Symptom]
  Warum 1: [Ursache erster Ebene]
  Warum 2: [Ursache der Ursache erster Ebene]
  Warum 3: [tiefere Ursache]
  Warum 4: [noch tiefere Ursache]
  Warum 5: [Grundursache — das systemische Thema, das angegangen werden muss]
  Grundursache: [Zusammenfassung — das muss sich ändern]
```

Höre auf, sobald du eine Ursache erreichst, die umsetzbar und systemisch ist. Nicht jede Kette geht bis fünf Ebenen; stoppe bei der umsetzbaren Wurzel.

## Wirkungsabschätzung

### Vorher-/Nachher-Prognose

Schätze für jede empfohlene Verbesserung die Wirkung ab:

```
VERBESSERUNGSPROGNOSE:
  Verbesserung:        [konkrete Änderung]
  Adressiert:          [welche Verschwendung/welchen Engpass]
  Aktuelle Kennzahl:   [Baseline aus der Durchsatzmessung]
  Prognostizierte Kennzahl: [erwarteter Wert nach der Verbesserung]
  Verbesserung:        [Delta und prozentuale Veränderung]
  Konfidenz:           [Hoch / Mittel / Gering — basierend auf Datenqualität]
  Annahmen:            [was zutreffen muss, damit die Prognose hält]
  Messmethode:         [wie du die Verbesserung nach der Umsetzung verifizierst]
```

Kennzeichne alle Prognosen als [KI-Prognose — mit Prozessdaten verifizieren]. Stelle Prognosen nie als Gewissheiten dar.

### Priorisierungsmatrix

Priorisiere Verbesserungen nach Wirkung gegen Aufwand:

|  | Hohe Wirkung | Mittlere Wirkung | Geringe Wirkung |
| --- | --- | --- | --- |
| **Geringer Aufwand** | **Zuerst tun** — Quick Wins | **Als Zweites** — leichter Mehrwert | **Erwägen** — marginale Gewinne |
| **Mittlerer Aufwand** | **Planen** — bedeutende Projekte | **Bewerten** — Kosten/Nutzen abwägen | **Zurückstellen** — begrenzter Ertrag |
| **Hoher Aufwand** | **Strategisch angehen** — große Investition | **Niedriger priorisieren** — schlechtes Verhältnis | **Vermeiden** — minimaler Ertrag bei hohen Kosten |

## Ausgabevorlage

```
# Prozessoptimierungs-Report — [Prozessname]

## Executive Summary
- Aktuelle Performance: [zentrale Baseline-Kennzahlen]
- Primärer Engpass: [die wesentliche Restriktion]
- Größte Verschwendungskategorie: [größte Verschwendungsquelle]
- Empfohlene Verbesserungen: [Anzahl und prognostizierte Gesamtwirkung]
- Quick Wins: [Verbesserungen, die innerhalb von 2 Wochen erreichbar sind]

## Ist-Zustand-Analyse
- Prozessmap: [Schritt-für-Schritt-Ist-Zustand mit Zeiten]
- Baseline-Kennzahlen: [Ergebnisse der Durchsatzmessung]
- Prozesseffizienz: [Verhältnis]

## Verschwendungsbewertung
[Verschwendungsposten mit Art, Ort, Häufigkeit, Auswirkung, Grundursache]

## Engpassanalyse
[Identifizierte Engpässe mit Klassifizierung und Beleg]

## Verbesserungsempfehlungen
[Priorisierte Liste mit Wirkungsprognosen]

## Umsetzungs-Roadmap
- Phase 1 (Quick Wins): [Verbesserungen mit geringem Aufwand, sofort umsetzbar]
- Phase 2 (Geplant): [Verbesserungen mit mittlerem Aufwand und Zeitrahmen]
- Phase 3 (Strategisch): [Verbesserungen mit hohem Aufwand, die eine Investitionsentscheidung erfordern]

## Erfolgskennzahlen
[Wie sich messen lässt, ob die Optimierung ihre Ziele erreicht hat — Baseline-Kennzahlen nach der Umsetzung erneut messen]

## Annahmen und Einschränkungen
[Welche Daten verfügbar waren, was geschätzt wurde, was validiert werden muss]
```

## Leitplanken

- Erzeuge niemals Zykluszeiten, Durchsatzraten oder Kostenwerte aus Trainingsdaten. Alle Kennzahlen stammen aus den Prozessdaten des Nutzers.
- Behaupte niemals Benchmarks. "Branchen-Benchmark" und "Best-in-Class" sind ohne den spezifischen Kontext des Nutzers bedeutungslos.
- Stelle Prognosen niemals als garantierte Ergebnisse dar. Alle Prognosen sind Schätzungen, die eine Messung nach der Umsetzung erfordern.
- Kennzeichne generierte Inhalte: `[Aus Prozessdaten]`, `[Framework-Methodik]`, `[KI-Prognose — mit Prozessdaten verifizieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX-, XLSX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Optimierungs-Report zu erhalten.
