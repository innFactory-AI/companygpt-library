---
name: de-tech-debt
description: Technical debt inventory with severity scoring, business impact assessment, and remediation prioritisation. Use when auditing tech debt, making a case for refactoring, or planning tech debt sprints. Trigger with "assess tech debt in", "tech debt inventory", "should we refactor".
---

# Tech-Debt-Skill

Verwandle vage "wir sollten das refactoren"-Gespräche in datenbasierte Investitionsentscheidungen. Der Skill führt dich durch Identifikation, Klassifikation, Schweregrad-Bewertung, Business-Impact-Einschätzung und Remediation-Priorisierung — alles auf Basis des Kontexts, den du bereitstellst.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **companyRAG-Sammlungen** | Architektur-Dokumentation, frühere Assessments, Quality-Reports |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear) | Erstellung und Tracking von Remediation-Tickets; Verknüpfung von Debt mit betroffenen Features |
| **Git-Provider über MCP** (z. B. GitHub, GitLab) | Code-Historie, Änderungshäufigkeit, Contributor-Muster |
| **Code-Quality über MCP** (z. B. SonarQube) | Coverage, Komplexitätsmetriken, gemeldete Code-Smells |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Assessment-Workflow

### Schritt 1: Debt identifizieren

Tech-Debt ist nicht einfach "Code, den ich nicht mag". Es ist eine Design- oder Implementierungsentscheidung, die laufende Kosten verursacht — langsamere Entwicklung, höhere Fehlerquoten, operativen Aufwand oder Skalierungsgrenzen.

**Identifikationsquellen:**

| Quelle | Was sie offenbart |
| --- | --- |
| **Entwickler-Interviews** | Schmerzpunkte, gefürchtete oder gemiedene Bereiche, "here be dragons"-Zonen |
| **Incident-Historie** | Wiederkehrende Ausfälle, Systeme, die unter Last brechen, Bereiche mit häufigen Rollbacks |
| **Änderungshäufigkeit + Defect-Korrelation** | Dateien, die oft geändert werden UND Bugs produzieren, deuten auf strukturelle Probleme hin |
| **Code-Review-Reibung** | Bereiche, in denen Reviews konstant Probleme aufzeigen, länger dauern oder Debatten auslösen |
| **Onboarding-Schwierigkeit** | Systeme, die neue Teammitglieder in einer angemessenen Einarbeitungszeit nicht verstehen können |
| **Build-/Test-Pipeline** | Langsame Builds, flaky Tests, Tests, die routinemäßig übersprungen oder ignoriert werden |
| **Dependency-Alter** | Bibliotheken mehrere Major-Versionen zurück, deprecated APIs, nicht unterstützte Runtimes |

**Identifikationsfragen an das Team:**

1. "Welchen Teil der Codebase fürchtest du am meisten? Warum?"
2. "Was dauert länger als es sollte? Was wäre schneller, wenn der Code anders wäre?"
3. "Wo kommen Bugs immer wieder her? Gibt es ein Muster?"
4. "Was bricht, wenn wir skalieren wollen?"
5. "Was lässt sich nicht ändern, ohne das Risiko, etwas anderes zu zerstören?"

### Schritt 2: Debt-Typ klassifizieren

Nicht jede Debt ist gleich. Die Klassifikation bestimmt den Remediation-Ansatz.

**Tech-Debt-Taxonomie:**

| Debt-Typ | Definition | Beispiele | Typische Remediation |
| --- | --- | --- | --- |
| **Architektur-Debt** | Systemstruktur, die nicht zu den aktuellen oder absehbaren Anforderungen passt | Monolith, der unabhängige Skalierung braucht; synchrone Calls, die async werden müssen; fehlende Service-Grenzen | Inkrementelle Restrukturierung, Strangler-Fig-Pattern, Extraktion von Domain-Grenzen |
| **Code-Debt** | Implementierung, die korrekt, aber teuer zu warten oder zu erweitern ist | Lange Funktionen, tiefe Verschachtelung, duplizierte Logik, unklare Benennung, fehlende Abstraktionen | Refactoring während der Feature-Arbeit, dedizierte Refactoring-Sprints |
| **Test-Debt** | Unzureichende, unzuverlässige oder schlecht strukturierte Tests | Niedrige Coverage auf kritischen Pfaden, flaky Tests, an Implementierungsdetails gekoppelte Tests, fehlende Integrationstests | Test-Verbesserungskampagnen, Coverage-Ratcheting, Beseitigung flaky Tests |
| **Dependency-Debt** | Veraltete oder problematische externe Abhängigkeiten | Bibliotheken mehrere Major-Versionen zurück, deprecated APIs, nicht gewartete Pakete, bekannte Schwachstellen | Dependency-Update-Sprints, Migration auf unterstützte Alternativen |
| **Infrastruktur-Debt** | Deployment-, Build- oder Betriebssysteme, die Reibung erzeugen | Langsame CI-Pipelines, manuelle Deployment-Schritte, fehlendes Monitoring, unzureichendes Alerting | DevOps-Investition, Pipeline-Modernisierung, Observability-Verbesserungen |
| **Dokumentations-Debt** | Fehlende oder veraltete Dokumentation, die die Entwicklung bremst | Keine Architektur-Docs, veraltete API-Referenzen, Tribal Knowledge, fehlende Runbooks | Dokumentations-Sprints, Docs-as-Code-Praktiken, ADR-Einführung |
| **Design-Debt** | Unter Zeitdruck getroffene Entscheidungen, die bekannte suboptimale Strukturen erzeugt haben | Abkürzungen in Datenmodellen, temporäre Workarounds, die permanent wurden, leaky Abstractions | Geplantes Rework, Expand-Contract-Migrationen |

### Schritt 3: Schweregrad und Impact bewerten

Bewerte jedes Debt-Item auf zwei Dimensionen: technischer Schweregrad und Business-Impact. Die Kombination bestimmt die Priorität.

**Technischer Schweregrad (wie schlimm ist es technisch?):**

| Score | Stufe | Kriterien |
| --- | --- | --- |
| **4** | Kritisch | Verursacht aktiv Produktions-Incidents, Datenintegritätsprobleme oder Sicherheitslücken. Kann nicht sicher umgangen werden. |
| **3** | Hoch | Verlangsamt die Feature-Entwicklung deutlich (2x+ Aufwand), produziert häufige Bugs oder verhindert die Skalierung auf bekannte kurzfristige Anforderungen. |
| **2** | Mittel | Verursacht Reibung und gelegentliche Bugs. Workarounds existieren, fügen aber Komplexität hinzu. Die Entwicklung ist langsamer als sie sein sollte. |
| **1** | Niedrig | Kosmetisch oder geringfügig. Für Entwickler spürbar, beeinflusst aber Velocity, Zuverlässigkeit oder Skalierbarkeit nicht messbar. |

**Business-Impact (wie stark beeinflusst es die Ergebnisse?):**

| Score | Stufe | Kriterien |
| --- | --- | --- |
| **4** | Kritisch | Blockiert umsatzgenerierende Features, verursacht kundensichtbare Incidents oder erzeugt Compliance-/Security-Risiken. |
| **3** | Hoch | Verlangsamt die Auslieferung hochpriorisierter Roadmap-Items. Die Team-Velocity ist in einem geschäftskritischen Bereich messbar reduziert. |
| **2** | Mittel | Beeinträchtigt die Entwicklungseffizienz, liegt aber nicht auf dem kritischen Pfad. Der Impact ist real, aber das Team kann ihn umgehen. |
| **1** | Niedrig | Aktuell minimaler Business-Impact. Kann relevant werden, wenn System oder Team wachsen. |

**Prioritäts-Matrix:**

|  | Business-Impact 4 | Business-Impact 3 | Business-Impact 2 | Business-Impact 1 |
| --- | --- | --- | --- | --- |
| **Schweregrad 4** | P0 — Jetzt fixen | P0 — Jetzt fixen | P1 — Nächster Sprint | P2 — Dieses Quartal planen |
| **Schweregrad 3** | P0 — Jetzt fixen | P1 — Nächster Sprint | P2 — Dieses Quartal planen | P3 — Backlog |
| **Schweregrad 2** | P1 — Nächster Sprint | P2 — Dieses Quartal planen | P3 — Backlog | P4 — Beobachten |
| **Schweregrad 1** | P2 — Dieses Quartal planen | P3 — Backlog | P4 — Beobachten | P4 — Beobachten |

### Schritt 4: Remediation-Kosten schätzen

Schätze für jedes Debt-Item die Remediation-Kosten, um eine ROI-basierte Priorisierung zu ermöglichen.

**Kostenschätzungs-Framework:**

| Faktor | Schätzungsansatz |
| --- | --- |
| **Aufwand** | Engineering-Zeit in Personentagen oder Story Points. Aufteilen in Discovery (Problem verstehen), Implementierung (fixen) und Verifikation (beweisen, dass es gefixt ist). |
| **Risiko** | Wahrscheinlichkeit, dass die Remediation Regressionen einführt. Höher bei architektonischen Änderungen, niedriger bei isoliertem Refactoring. |
| **Disruption** | Blockiert die Remediation andere Arbeit? Erfordert sie Feature-Freezes? Braucht sie teamübergreifende Koordination? |
| **Opportunitätskosten** | Welche Feature-Arbeit wird durch diese Remediation verdrängt? Ist der Trade-off gerechtfertigt? |

**Kostenklassifikation:**

| Kostenstufe | Definition |
| --- | --- |
| **Niedrig** (< 1 Woche) | Begrenztes Refactoring, Dependency-Update, Dokumentation |
| **Mittel** (1–4 Wochen) | Querschnittliches Refactoring, Verbesserung der Test-Infrastruktur, Migration einer Komponente |
| **Hoch** (1–3 Monate) | Architektonische Restrukturierung, größere Migration, Plattformwechsel |
| **Sehr hoch** (> 3 Monate) | System-Rewrite, Multi-Service-Zerlegung, grundlegende Infrastruktur-Überholung |

### Schritt 5: Priorisieren und planen

Kombiniere Schweregrad, Business-Impact und Remediation-Kosten zu einem priorisierten Backlog.

**Priorisierungsstrategien:**

| Strategie | Am besten, wenn |
| --- | --- |
| **Fix on contact** | Debt wird während der Feature-Arbeit angetroffen. Refactore den Bereich, den du ohnehin gerade anfasst. Geringer Overhead, stetige Verbesserung. |
| **Dedizierte Debt-Sprints** | Aufgelaufene Debt bremst die Velocity flächendeckend. Allokiere einen festen Kapazitätsanteil (üblich 15–20 %) für Debt-Remediation. |
| **Strategische Investition** | Architektur-Debt erfordert fokussierten Aufwand über mehrere Sprints. Behandle sie als Projekt mit Planung, Meilensteinen und Erfolgsmetriken. |
| **Containment** | Debt existiert, aber die Remediation-Kosten übersteigen den Nutzen. Ziehe eine Grenze: lass sie sich nicht weiter ausbreiten, investiere aber nicht in die Behebung. |
| **Geplante Stilllegung** | Das System wird ersetzt. Investiere nur, um es betriebsfähig zu halten, bis der Ersatz bereit ist. |

**Remediation-Plan-Vorlage pro Item:**

```
TECH-DEBT-ITEM: [ID] — [Kurzname]
  Typ:              [Architektur / Code / Test / Dependency / Infra / Docs / Design]
  Schweregrad:      [1–4] — [Begründung]
  Business-Impact:  [1–4] — [Begründung]
  Priorität:        [P0–P4]
  Remediation-Kosten: [Niedrig / Mittel / Hoch / Sehr hoch]
  Strategie:        [Fix on contact / Dedizierter Sprint / Strategische Investition / Containment / Geplante Stilllegung]
  Beschreibung:     [Was die Debt ist und warum sie relevant ist]
  Root Cause:       [Wie diese Debt entstand — Zeitdruck, geänderte Anforderungen, Wissenslücke]
  Remediation-Plan: [High-Level-Ansatz — kein vollständiges Design-Dokument]
  Erfolgsmetrik:    [Woran erkennen wir, dass es gefixt ist? — reduzierte Incident-Rate, bessere Velocity, Coverage-Ziel]
  Verantwortlich:   [Team oder Person]
  Zieltermin:       [Wann die Remediation abgeschlossen sein soll]
```

## Tech-Debt-Report-Vorlage

```
# Technical-Debt-Assessment: [System-/Bereichsname]

## Executive Summary
- Identifizierte Debt-Items gesamt: [N]
- Prioritätsverteilung: [N] P0, [N] P1, [N] P2, [N] P3, [N] P4
- Geschätzter Gesamtaufwand für Remediation: [Personenwochen]
- Top-3-Empfehlungen: [kurz]

## Debt nach Typ
| Typ | Anzahl | Ø Schweregrad | Ø Business-Impact |
|---|---|---|---|
| Architektur | [N] | [X] | [X] |
| Code | [N] | [X] | [X] |
| Test | [N] | [X] | [X] |
| Dependency | [N] | [X] | [X] |
| Infrastruktur | [N] | [X] | [X] |
| Dokumentation | [N] | [X] | [X] |
| Design | [N] | [X] | [X] |

## Prioritäts-Items (P0–P1)
[Detaillierte Einträge gemäß Vorlage aus Schritt 5]

## Remediation-Roadmap
| Quartal | Fokusbereich | Erwartetes Ergebnis | Aufwand |
|---|---|---|---|
| [Q] | [Bereich] | [messbare Verbesserung] | [Personenwochen] |

## Zu trackende Metriken
- Trend der Entwicklungs-Velocity (Story Points / Sprint)
- Defect-Escape-Rate (in Produktion gefundene Bugs)
- Incident-Häufigkeit pro Systembereich
- Mittlere Zeit zur Umsetzung eines Features im betroffenen Bereich
- Dauer der CI-Pipeline
```

## Leitplanken

- Erfinde niemals Code-Quality-Metriken. Behaupte keine Coverage-Prozentsätze oder Komplexitäts-Scores ohne Daten vom Nutzer. Gib an, welche Tools auszuführen sind und worauf zu achten ist.
- Bewerte Debt niemals ohne Begründung. Jeder Schweregrad- und Business-Impact-Score muss eine kurze Begründung enthalten — Scores ohne Begründung kann das Team nicht validieren.
- Nimm niemals Geschäftsprioritäten an. Frage den Nutzer nach seinen Prioritäten, statt anzunehmen, was die Organisation am meisten wertschätzt.
- Versieh Ausgaben mit Quellenkennzeichnung: `[Aus Nutzer-Kontext]`, `[Assessment-Methodik]` oder `[KI-Einschätzung — mit dem Team verifizieren]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, Markdown- oder DOCX-Ausgabe an, um ein formatiertes, sofort teilbares Inventar zu erhalten.
