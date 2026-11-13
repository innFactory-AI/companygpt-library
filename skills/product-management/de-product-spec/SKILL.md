---
name: de-product-spec
description: Erstellt aus vagen Ideen Feature-Spezifikationen oder PRDs über strukturierte Rückfragen und Scope-Management. Verwende ihn, wenn du ein neues Feature definierst, ein Briefing für das Engineering schreibst oder Stakeholder-Wünsche in umsetzbare Specs überführst. Auslösen mit "Spec erstellen für", "hilf mir, das auszuspezifizieren", "PRD für [Feature]".
---

# Produkt-Spec-Skill

Mach aus mehrdeutigen Produktideen klare, engineering-fertige Spezifikationen. Der Skill deckt Klärungs-Workflows, Scope-Management, das Strukturieren von Anforderungen und das Erkennen von Risiken ab, damit verlässliche PRDs entstehen. Die nötigen Eingaben kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear, Asana, Shortcut) | Bestehende Tickets, Epics oder OKRs als Kontext; finalisierte Stories zurückschreiben |
| **Design-Tool über MCP** (z. B. Figma, Miro) | Wireframes, User Flows, Constraints des Design-Systems |
| **companyRAG-Sammlungen** | Bestehende Specs, frühere Recherchen, Wettbewerbskontext, Architektur-Dokumente |
| **companyRAG / Datei-Upload** | Confluence-Seiten, Discovery-Notizen, technische Assessments |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Spezifikations-Workflow

Führe diese fünf Phasen der Reihe nach aus. Jede Phase hat ein Gate — gehe nicht weiter, bevor die Gate-Bedingung erfüllt ist.

### Phase 1: Das Problem klären

Bevor du eine einzige Anforderung schreibst, kläre, welches Problem dieses Feature für wen löst. Die meisten Spec-Fehler lassen sich darauf zurückführen, dass diese Phase übersprungen wurde.

**Reihenfolge der Klärungsfragen** (in dieser Reihenfolge stellen, Formulierung an den Kontext anpassen):

1. Problembeschreibung: "Welches Problem löst das, und woher weißt du, dass es ein echtes Problem ist?" — Achte auf Belege: Nutzerforschung, Support-Tickets, Churn-Daten, Sales-Feedback. Lautet die Antwort "Stakeholder X will das", frage nach dem dahinterliegenden Problem.
2. Betroffene Nutzer: "Wer erlebt dieses Problem, und wie oft?" — Bestimme das Nutzersegment, die Häufigkeit und die Schwere. Ein Problem, das 5 % der Nutzer täglich betrifft, kann wichtiger sein als eines, das 50 % einmal im Jahr betrifft.
3. Aktueller Workaround: "Wie lösen Nutzer das heute ohne das Feature?" — Workarounds offenbaren den tatsächlichen Workflow, die Erwartungen und die Intensität des Schmerzes. Kein Workaround kann auf geringe Dringlichkeit hindeuten.
4. Geschäftskontext: "Warum genau jetzt lösen? Was ändert sich, wenn wir es nicht tun?" — Verknüpft mit OKRs, Umsatzzielen, Wettbewerbsdruck oder regulatorischen Fristen. Bleibt die Antwort vage, ist die Priorität unsicher.
5. Frühere Versuche: "Wurde das schon einmal versucht? Was ist passiert?" — Verhindert das Wiederholen gescheiterter Ansätze und legt organisatorische Constraints offen.

**Gate**: Es existiert eine Problembeschreibung, die den Nutzer, den Schmerz und den Beleg benennt. Kann der Nutzer das Problem nicht artikulieren, hilf ihm, eines zu formulieren, bevor du weitermachst — springe NICHT zum Lösungsdesign.

### Phase 2: Scope definieren

Scope Creep ist die häufigste Ursache für gescheiterte Specs. Nutze explizite In/Out-Grenzen und ein Phasen-Framework.

**Schritte zur Scope-Definition**:

1. Lösungsskizze: Bitte den Nutzer, seine ideale Lösung in 2–3 Sätzen zu beschreiben — maximal. Das erzwingt Priorisierung vor dem Detail.
2. In-Scope-/Out-of-Scope-Tabelle: Klassifiziere jede genannte Fähigkeit explizit:

| Fähigkeit | In Scope (v1) | Später (v2+) | Out of Scope | Begründung |
| --- | --- | --- | --- | --- |
| [Fähigkeit] | ✓ / — | — / ✓ | — / ✓ | [warum diese Klassifizierung] |

1. **MoSCoW-Klassifizierung** für In-Scope-Punkte:   - Must have: Ohne dieses Feature ist es kaputt. Ship-blockierend.   - Should have: Deutlicher Mehrwert, starke Erwartung, aber es gibt einen Workaround.   - Could have: Schön zu haben, wenn Kapazität da ist. Wird zuerst gestrichen.   - Won't have (diesmal): Explizit zurückgestellt. "Won't" zu dokumentieren verhindert Scope-Drift.
2. **Scope-Verankerungsfrage**: "Wenn wir nur EINE Sache aus dieser Spec ausliefern könnten, welche wäre das?" — Die Antwort ist der nicht verhandelbare Kern. Alles andere ist relative Priorität darum herum.

**Gate**: Eine In/Out-Tabelle existiert, die MoSCoW-Klassifizierung ist angewendet, und der Nutzer hat die Scope-Grenze bestätigt.

### Phase 3: Spec-Abschnitte schreiben

Strukturiere das PRD anhand der untenstehenden Ausgabevorlage. Wende für jeden Abschnitt diese Schreibprinzipien an:

- Anforderungen statt Lösungen: Beschreibe das WAS und WARUM, nicht das WIE. "Nutzer müssen nach Datumsbereich filtern können", nicht "Füge eine Datepicker-Komponente hinzu."
- Testbare Akzeptanzkriterien (acceptance criteria): Jede Anforderung braucht eine überprüfbare Bedingung. "Die Seite lädt" ist nicht testbar. "Die Seite rendert die ersten 20 Ergebnisse innerhalb von 2 Sekunden über eine 3G-Verbindung" schon.
- Edge Cases vorab: Frage bei jeder Anforderung "Was passiert, wenn …?" — Leerzustände, Fehlerzustände, Berechtigungsgrenzen, Datenlimits, gleichzeitiger Zugriff.
- Eine Anforderung, eine Aussage: Zusammengesetzte Anforderungen ("das System sollte X und Y") verbergen Komplexität und erzeugen mehrdeutige Akzeptanzkriterien. Teile sie auf.

**Muster zur Anforderungszerlegung**:

```
ANFORDERUNG: [Klare Aussage mit einem einzigen Zweck]
  User Story:        Als [Rolle] möchte ich [Fähigkeit], damit [Ergebnis]
  Akzeptanzkriterien:
    GIVEN [Kontext]
    WHEN  [Aktion]
    THEN  [beobachtbares Ergebnis]
  Edge Cases:
    - [Was, wenn die Eingabe leer/fehlerhaft/am Limit ist?]
    - [Was, wenn dem Nutzer die Berechtigung fehlt?]
    - [Was, wenn ein abhängiger Dienst nicht verfügbar ist?]
  Abhängigkeiten:    [Andere Anforderungen oder Systeme, von denen dies abhängt]
  Offene Fragen:     [Ungeklärte Entscheidungen — Verantwortlicher und Frist zur Klärung]
```

### Phase 4: Risiken identifizieren

Decke Risiken systematisch auf, bevor das Engineering beginnt. Kategorisiere nach:

| Risikokategorie | Worauf zu achten ist | Muster zur Gegenmaßnahme |
| --- | --- | --- |
| **Technisch** | Neue Technologie, Integrationskomplexität, Performance-Anforderungen, Datenmigration | Erst Spike/Prototyp, Fallback-Ansatz definieren |
| **Scope** | Mehrdeutige Anforderungen, undefinierte Edge Cases, implizite Annahmen | Akzeptanzkriterien schärfen, explizite Constraints ergänzen |
| **Abhängigkeit** | Externe Teams, Drittanbieter-APIs, Plattform-Freigaben, geteilte Infrastruktur | Kritischen Pfad identifizieren, SLAs oder Fristen mit Verantwortlichen festlegen |
| **Nutzerakzeptanz** | Workflow-Störung, Lernkurve, Migration von bestehendem Verhalten | Rollout-Strategie planen, Adoption-Kennzahlen definieren |
| **Timeline** | Konkurrierende Prioritäten, Team-Verfügbarkeit, sequenzielle Abhängigkeiten | Parallelisierbare Arbeit identifizieren, Ressourcenkonflikte früh markieren |

Dokumentiere zu jedem Risiko: Beschreibung, Eintrittswahrscheinlichkeit (Hoch/Mittel/Niedrig), Auswirkung (Hoch/Mittel/Niedrig), Plan zur Gegenmaßnahme und Verantwortlicher.

**Gate**: Mindestens drei Risiken sind identifiziert und dokumentiert. Eine Spec mit null Risiken wurde nicht kritisch geprüft.

### Phase 5: Erfolgskennzahlen festlegen

Definiere, woran das Team erkennt, dass das Feature erfolgreich war. Nutze die Metrik-Hierarchie:

1. Primärkennzahl (nur 1): Die eine Zahl, die am direktesten misst, ob das Problem aus Phase 1 gelöst ist. An die Problembeschreibung gebunden, nicht an die Lösung.
2. Frühindikatoren (2–3): Kennzahlen, die sich VOR der Primärkennzahl bewegen und ein frühes Signal liefern. Beispiel: Ist die Primärkennzahl die Retention, könnten Frühindikatoren die Feature-Adoptionsrate oder die Task-Completion-Rate sein.
3. Guardrail-Kennzahlen (1–2): Kennzahlen, die sich NICHT verschlechtern dürfen. Verhindern, dass ein Problem gelöst wird, indem ein neues entsteht. Beispiel: Die Ladezeit der Seite darf nicht steigen; das Support-Ticket-Volumen darf nicht hochschnellen.

Für jede Kennzahl:

```
KENNZAHL: [Name]
  Typ:        Primär / Frühindikator / Guardrail
  Definition: [Präzise Berechnung — Zähler, Nenner, Zeitfenster]
  Baseline:   [Aktueller Wert oder "in den ersten 2 Wochen zu ermitteln"]
  Ziel:       [Konkreter Schwellenwert mit Zeitrahmen]
  Quelle:     [Woher die Daten kommen — Analytics-Tool, Datenbankabfrage, Umfrage]
```

**Gate**: Mindestens eine Primärkennzahl, ein Frühindikator und ein Guardrail sind mit messbaren Zielen definiert.

## PRD-Ausgabevorlage

Verwende diese Struktur für das finale Dokument. Passe die Detailtiefe der Abschnitte an die Feature-Komplexität an — ein zweiwöchiges Feature braucht weniger Detail als eine quartalslange Initiative.

```
# [Feature-Name] — Product Requirements Document

## 1. Problembeschreibung
[Aus Phase 1 — das Problem, wer es erlebt, der Beleg, dass es zählt]

## 2. Lösungsüberblick
[2–3 Sätze zur Beschreibung des vorgeschlagenen Lösungsansatzes]

## 3. Ziele & Erfolgskennzahlen
[Aus Phase 5 — Primärkennzahl, Frühindikatoren, Guardrails mit Zielen]

## 4. Scope
### 4a. In Scope (v1)
[MoSCoW-klassifizierte Fähigkeiten für dieses Release]

### 4b. Out of Scope
[Explizit zurückgestellte Punkte mit Begründung]

## 5. User Stories & Anforderungen
[Aus Phase 3 — zerlegte Anforderungen mit Akzeptanzkriterien]

### 5a. Must Have
[Ship-blockierende Anforderungen]

### 5b. Should Have
[Anforderungen mit hohem Mehrwert und Workarounds]

### 5c. Could Have
[Wenn Kapazität da ist]

## 6. User Flows
[Wichtige Workflows — auf Design-Dateien verweisen, falls vorhanden]

## 7. Edge Cases & Fehlerbehandlung
[Konsolidiert aus der Anforderungszerlegung in Phase 3]

## 8. Technische Überlegungen
[Bekannte Constraints, API-Abhängigkeiten, Performance-Anforderungen, Änderungen am Datenmodell]

## 9. Risiken & Gegenmaßnahmen
[Aus Phase 4 — kategorisierte Risiken mit Verantwortlichen]

## 10. Abhängigkeiten
[Erforderliche externe Teams, Dienste, Freigaben]

## 11. Offene Fragen
[Ungeklärte Entscheidungen — Verantwortlicher und Frist je Punkt]

## 12. Release-Plan
[Rollout-Strategie, Feature Flags, Kriterien für den phasenweisen Launch]

## 13. Anhang
[Unterstützende Recherche, Wettbewerbskontext, Verweise auf Vorarbeiten]
```

## Leitfaden zur Spec-Größe

Passe die Spec-Tiefe an den Feature-Umfang an:

| Feature-Umfang | Typische Dauer | Spec-Tiefe | Wichtige Abschnitte |
| --- | --- | --- | --- |
| **Klein** (Bugfix, Textänderung, Konfiguration) | < 1 Woche | Leichtgewichtig — Problem + Anforderungen + Akzeptanzkriterien | Abschnitte 1, 5, 7 |
| **Mittel** (neues Feature, Workflow-Änderung) | 1–6 Wochen | Standard — volles PRD ohne Anhang | Abschnitte 1–10 |
| **Groß** (neuer Produktbereich, Plattform-Änderung) | 1+ Quartal | Umfassend — volles PRD mit Anhang, phasenweiser Scope | Alle Abschnitte, phasenweiser Release-Plan |

## Anti-Patterns

Erkenne und markiere diese, sobald sie auftauchen:

1. Spec ohne Problembeschreibung: Eine Lösung auf der Suche nach einem Problem. Kann Phase 1 keine klare Problembeschreibung mit Beleg liefern, ist das Feature nicht spec-reif. Leite zurück zu Nutzerforschung oder Stakeholder-Alignment.
2. Unbegrenzter Scope: Kein expliziter Out-of-Scope-Abschnitt, keine MoSCoW-Klassifizierung oder jeder Punkt ist "Must have". Stell mit der Scope-Verankerungsfrage infrage und erzwinge Priorisierung.
3. Als Lösungen getarnte Anforderungen: "Füge ein Dropdown hinzu" statt "Nutzer müssen aus vordefinierten Optionen wählen können". Lösungsspezifik in Anforderungen schränkt das Engineering unnötig ein und vermischt die Rollen von PM und Engineering.
4. Akzeptanzkriterien, die nicht scheitern können: "Das Feature funktioniert korrekt" ist nicht testbar. Jedes Kriterium braucht eine klare Pass/Fail-Bedingung.
5. Null Risiken identifiziert: Signalisiert unzureichende kritische Prüfung. Wehre dich — jedes Feature hat Risiken. Die Frage ist, ob sie identifiziert und gemanagt werden.
6. Kennzahlen ohne Baselines: Ein Ziel von "Retention um 10 % steigern" ist ohne den aktuellen Wert bedeutungslos. Sind keine Baselines verfügbar, ist der erste Meilenstein, sie zu ermitteln.
7. Verwaiste offene Fragen: Fragen werden gelistet, aber ohne Verantwortlichen oder Frist zur Klärung. Jede offene Frage braucht einen Namen und ein Datum, sonst blockiert sie das Engineering.

## Nächste Schritte nach Fertigstellung der Spec

Sobald das PRD geprüft und freigegeben ist:

1. Engineering-Review: Plane ein technisches Review, um Implementierungsbedenken aufzudecken, Schätzungen zu verfeinern und Spikes zu identifizieren.
2. Design-Handover: Falls Design-Arbeit nötig ist, stelle sicher, dass Wireframes oder Prototypen alle User Flows und Edge Cases der Spec abdecken.
3. Spec als lebendes Dokument: Specs entwickeln sich während der Umsetzung weiter. Etabliere einen Change-Log-Abschnitt und einen leichtgewichtigen Freigabeprozess für Änderungen (wer Scope-Änderungen mitten in der Umsetzung freigeben darf).

## Leitplanken

- Erfinde NIEMALS Nutzerforschung, Kennzahlen oder Daten. Wenn keine Daten vorliegen, schreibe "Daten benötigt — [angeben, welche]" und lass das Feld für den Nutzer offen.
- Nimm NIEMALS technische Constraints an. Markiere sie als [Engineering-Input erforderlich], sofern der Nutzer oder eine companyRAG-Sammlung keine Details liefert.
- Erzeuge NIEMALS Wettbewerber-Features oder Marktdaten. Verweise auf den Wettbewerbsanalyse-Skill oder frage den Nutzer.
- Versieh jedes Element mit einer Quellenkennzeichnung: [Aus Nutzereingabe], [Spec-Framework] oder [KI-Vorschlag — prüfen].

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um ein formatiertes, sofort verteilbares Dokument zu erhalten.
