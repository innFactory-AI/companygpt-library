---
name: de-roadmap-update
description: Aktualisiert oder priorisiert Roadmaps neu mit Now/Next/Later-, Quartals- oder OKR-Frameworks inklusive Abhängigkeits-Mapping. Verwende ihn nach einem Strategiewechsel, zur Vorbereitung eines Roadmap-Reviews oder zur Kommunikation der Produktrichtung. Auslösen mit "Roadmap aktualisieren", "Roadmap neu priorisieren", "Roadmap für Q[n]".
---

# Roadmap-Update-Skill

Baue, aktualisiere und kommuniziere Produkt-Roadmaps mit Framework-Auswahl, Priorisierungs-Scoring (RICE, MoSCoW, gewichtet), Abhängigkeits-Mapping und zielgruppengerechten Kommunikationsformaten. Roadmap-Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Productboard, Linear) | Backlog-Items, aktueller Roadmap-Stand, Status, Abhängigkeiten, Verantwortlichkeiten |
| **companyRAG-Sammlungen** | Strategiedokumente, OKRs, Customer-Feedback, Discovery-Notizen, Wettbewerbsanalysen |
| **Datei-Upload** | Aktuelle Roadmap-Exporte, Kapazitätspläne, Metrik-Reports |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Framework-Auswahl

Wähle das Roadmap-Framework, das zur Planungsreife des Teams, zu den Stakeholder-Bedürfnissen und zur Liefer-Kadenz passt. Verwende ein Framework konsistent — das Mischen von Frameworks stiftet Verwirrung.

| Framework | Am besten geeignet für | Trade-off |
| --- | --- | --- |
| **Now / Next / Later** | Teams mit hoher Unsicherheit, kontinuierlicher Auslieferung oder Stakeholdern, die zu stark auf Termine fixiert sind | Geringe Commitment-Spezifität — Cross-Team-Abhängigkeiten sind schwerer zu koordinieren |
| **Quartalsweise (Q1/Q2/Q3/Q4)** | Teams mit planbarer Liefer-Kadenz, Board-Reporting-Zyklen oder regulatorischen Fristen | Termingebunden — erzeugt implizite Commitments, die verfrüht sein können |
| **OKR-orientiert** | Teams mit reifer OKR-Praxis, bei denen Roadmap-Items direkt auf messbare Ziele abbilden | Erfordert klar definierte OKRs; schlecht formulierte OKRs erzeugen schlecht strukturierte Roadmaps |
| **Themenbasiert** | Portfolio-Roadmaps über mehrere Teams oder Produktlinien hinweg | Hochlevelig — erfordert Zerlegung für die Umsetzungsplanung |

### Entscheidungsbaum zur Auswahl

```
Hat das Team eine reife OKR-Praxis mit messbaren Key Results?
  JA   → OKR-orientiert (Initiativen unter Zielen gruppiert)
  NEIN → Verpflichtet sich das Team auf quartalsweise Liefertermine?
           JA   → Quartalsweise
           NEIN → Ist die Roadmap für ein einzelnes Team oder mehrere?
                    Einzelnes Team → Now / Next / Later
                    Mehrere Teams / Portfolio → Themenbasiert (mit Zerlegung auf Team-Ebene)
```

## Priorisierungsmethodik

### RICE-Scoring

Verwende RICE, wenn der Backlog viele konkurrierende Items enthält und das Team eine quantitative erste Rangfolge braucht. RICE trifft NICHT die Entscheidung — es schafft einen fundierten Ausgangspunkt für die Diskussion.

| Faktor | Definition | Scoring-Hinweis |
| --- | --- | --- |
| **Reach** | Wie viele Nutzer/Accounts betrifft das in einem definierten Zeitraum? | Verwende ein konsistentes Zeitfenster (z. B. pro Quartal). Zähle aus eigenen Daten, nicht aus Schätzungen. |
| **Impact** | Wie stark bewegt das die Zielmetrik pro erreichtem Nutzer? | 3 = massiv, 2 = hoch, 1 = mittel, 0,5 = gering, 0,25 = minimal |
| **Confidence** | Wie sicher bist du dir bei Reach- und Impact-Schätzungen? | 100 % = hohe Sicherheit mit Daten, 80 % = fundierte Schätzung, 50 % = Bauchgefühl |
| **Effort** | Wie viele Personen-Sprints (oder Personen-Wochen) erfordert das? | Design, Engineering, QA und Rollout einrechnen — nicht nur Coding |

```
RICE-SCORE = (Reach × Impact × Confidence) / Effort
```

**RICE-Kalibrierungsregeln**:

- Bewerte alle Items in derselben Session, um Drift zu vermeiden
- Bewerte neu, wenn neue Daten eintreffen (User Research, technische Discovery)
- Vergleiche RICE-Scores niemals über verschiedene Produktbereiche hinweg — die Skalen sind nicht kalibriert
- RICE ist ein Input für die Priorisierung, nicht das Ergebnis — überschreibe es bei strategischem Alignment, Abhängigkeiten oder Sequenzierungsvorgaben

### MoSCoW für Scope-Gates

Wenn die Roadmap eine feste Zeitgrenze hat (quartalsweise, release-basiert), wende MoSCoW an, um zu klassifizieren, was hineinpasst:

- Must have : Ohne dieses Item scheitert der Roadmap-Zeitraum. Nicht verhandelbare Commitments (regulatorisch, vertraglich, kritische Bugs).
- Should have : Hoher Wert, starke Stakeholder-Erwartung, aber um einen Zeitraum verschiebbar ohne kritische Auswirkung.
- Could have : Wertvoll, wenn Kapazität vorhanden ist. Wird als Erstes gestrichen, wenn die Kapazität knapp wird.
- Won't have (in diesem Zeitraum) : Explizit zurückgestellt. Dokumentiere das "Won't", um Scope-Drift zu verhindern und Erwartungen zu setzen.

### Gewichtetes Scoring für strategisches Alignment

Wenn RICE allein nicht ausreicht (z. B. strategische Wetten, die beim Reach schlecht abschneiden), ergänze strategische Dimensionen:

| Dimension | Gewicht (anpassen) | Score (1–5) |
| --- | --- | --- |
| Strategisches Alignment | [Gewicht] | Wie gut bringt das die Unternehmens-/Produktstrategie voran? |
| Kundennachfrage | [Gewicht] | Häufigkeit und Intensität der Kundenanfragen |
| Umsatzwirkung | [Gewicht] | Direkter oder indirekter Umsatzbeitrag |
| Abbau technischer Schulden | [Gewicht] | Reduziert das den Wartungsaufwand oder steigert die künftige Velocity? |
| Wettbewerbsnotwendigkeit | [Gewicht] | Entsteht ein Wettbewerbsnachteil, wenn das nicht gebaut wird? |

Die Gewichte müssen sich auf 1,0 summieren und VOR dem Scoring der Items festgelegt werden. Gewichte nach dem Scoring zu ändern, ist ein Priorisierungs-Smell — es deutet darauf hin, dass die Antwort rückwärts konstruiert wird.

## Roadmap-Update-Workflow

### Schritt 1: Eingaben sammeln

Sammle vor dem Neupriorisieren den aktuellen Stand:

1. Aktuelle Roadmap : Was war geplant? Was wurde ausgeliefert? Was ist verrutscht?
2. Neue Eingaben : Strategieänderungen, Kundenfeedback, Wettbewerbsbewegungen, technische Discoveries, regulatorische Anforderungen
3. Kapazitätsänderungen : Teamgrößen-Änderungen, einarbeitende Neueinstellungen, Abgänge, Reorgs
4. Abhängigkeits-Updates : Veränderte Cross-Team-Commitments, verschobene externe Timelines
5. Metrik-Performance : Bewegen aktuelle Initiativen die Zielmetriken? Nutze den review-metrics-Skill für die Analyse.

### Schritt 2: Neue Items triagieren

Für jedes neue Item, das in den Backlog eintritt:

1. Problemvalidierung : Löst das ein validiertes Problem? (Siehe write-spec Phase 1)
2. Strategischer Fit : Passt das zur aktuellen Strategie und zu den OKRs?
3. Größenschätzung : Grobe T-Shirt-Größe (S/M/L/XL) für die erste Priorisierung — die detaillierte Schätzung folgt später
4. Dringlichkeitsbewertung : Gibt es einen zeitgebundenen Auslöser (Wettbewerb, regulatorisch, vertraglich)?

### Schritt 3: Neu priorisieren

Wende die gewählte Priorisierungsmethodik (RICE, MoSCoW, gewichtetes Scoring) auf den kombinierten Backlog (bestehende + neue Items) an. Vergleiche die neue Rangfolge mit der aktuellen Roadmap:

| Änderungstyp | Aktion |
| --- | --- |
| **Neues Item rangiert über bestehender committeter Arbeit** | Bewerte: tauschen, zurückstellen oder Kapazität erhöhen? Dokumentiere den Trade-off explizit. |
| **Priorität eines bestehenden Items gesunken** | In den nächsten Zeitraum oder Backlog verschieben. Kommuniziere die Änderung an betroffene Stakeholder. |
| **Item abgeschlossen oder nicht mehr relevant** | Entferne es und dokumentiere warum. Feiere Abschlüsse; erkläre Streichungen. |
| **Item durch ungelöste Abhängigkeit blockiert** | In den Status "blockiert" verschieben. Verantwortliche/n für die Abhängigkeit benennen. Nicht ohne Lösungspfad auf der Roadmap halten. |

### Schritt 4: Abhängigkeiten validieren

Baue oder aktualisiere für die aktualisierte Roadmap die Abhängigkeitskarte:

```
ABHÄNGIGKEITSKARTE:
  Initiative: [Name]
  Hängt ab von: [Initiative / Team / extern]
  Abhängigkeitstyp: Sequenziell (muss zuerst fertig sein) / Parallel (kann überlappen) / Informativ (braucht Input, nicht blockierend)
  Status: Gelöst / In Arbeit / Gefährdet / Ungelöst
  Verantwortlich: [Name]
  Erwartete Auflösung: [Datum]
```

**Identifikation des kritischen Pfads**: Verfolge die längste Kette sequenzieller Abhängigkeiten. Das ist die Mindest-Timeline der Roadmap, unabhängig von der Team-Kapazität. Übersteigt der kritische Pfad den Planungszeitraum, muss der Scope reduziert werden.

### Schritt 5: Änderungen kommunizieren

Schneide das Roadmap-Update auf jede Zielgruppe zu. Siehe den Abschnitt Stakeholder-Kommunikationsformat unten.

## Stakeholder-Kommunikationsformat

Verschiedene Zielgruppen brauchen verschiedene Sichten auf dieselbe Roadmap.

### Executive- / Board-Sicht

Fokus: Strategie-Alignment, Geschäftsergebnisse, Ressourcenzuteilung.

```
ROADMAP-ZUSAMMENFASSUNG — [Zeitraum]
Strategische Prioritäten:  [2–3 Themen, an Unternehmens-OKRs gekoppelt]
Wichtige Deliverables:     [3–5 Headline-Items mit erwarteten Ergebnissen]
Ressourcenzuteilung:       [% der Kapazität pro Thema]
Wichtige Risiken:          [Top 2–3 Risiken für die Roadmap-Lieferung]
Änderungen seit letztem Review:  [Was hinein-/herauskam und warum]
```

### Engineering- / Design-Sicht

Fokus: Scope, Abhängigkeiten, Sequenzierung, technische Anforderungen.

```
ROADMAP — [Zeitraum]
Sprint-Level-Aufschlüsselung:  [Initiativen in sprintgroße Arbeit zerlegt]
Abhängigkeiten:                [Vollständige Abhängigkeitskarte mit Verantwortlichen und Terminen]
Technische Risiken:            [Architekturentscheidungen, nötige Spikes, Unbekannte]
Kapazitätszuteilung:           [Team-für-Team-Kapazität vs. geplante Arbeit]
```

### Kundengerichtete Sicht

Fokus: gelieferter Mehrwert, Timeline-Bereiche (keine exakten Termine), keine internen Details.

```
PRODUKT-UPDATE — [Zeitraum]
Demnächst:        [Features in aktiver Entwicklung — Mehrwert beschreiben, nicht Implementierung]
Auf dem Radar:    [Geplante Features — als gelöste Probleme formulieren, nicht als Lösungen]
Kürzlich ausgeliefert: [Abgeschlossene Features mit Adoption-/Impact-Daten, falls verfügbar]
```

**Regel**: Kundengerichtete Roadmaps verwenden Zeitbereiche ("dieses Quartal", "erste Jahreshälfte"), niemals konkrete Termine. Lege niemals interne Priorisierungs-Scores, interne Projektnamen oder technische Implementierungsdetails offen.

## Leitplanken

- Erfinde niemals Initiativ-Daten, Timelines oder Kapazitätszahlen. Alle Roadmap-Inhalte müssen vom Nutzer, aus dem Projekt-Tracker oder aus einer companyRAG-Sammlung stammen.
- Erzeuge niemals RICE-Scores, Effort-Schätzungen oder Reach-Zahlen. Stelle das Scoring-Framework bereit; das Team füllt es mit seinen Daten.
- Behaupte niemals "Branchenstandard"-Priorisierungsgewichte oder Roadmap-Strukturen. Frameworks sind Methodik; konkrete Gewichte und Prioritäten sind organisationsspezifisch.
- Roadmap-Items sind keine verbindlichen Zusagen, solange sie nicht ausdrücklich als Commitment ausgewiesen sind. Halte diese Unterscheidung in jeder Ausgabe aufrecht.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Nutzer-/Roadmap-Daten]`, `[Roadmap-Framework]` oder `[KI-Vorschlag — prüfen]`.

> **Tipp:** Fordere über companyFILES eine Markdown-, DOCX- oder XLSX-Ausgabe an, um eine formatierte, sofort teilbare Roadmap zu erhalten.
