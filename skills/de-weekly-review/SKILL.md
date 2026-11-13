---
name: de-weekly-review
description: Fasst offene Aufgaben, Fristen, Fortschritt und Übertrag in einen strukturierten Wochen-Reset zusammen. Verwende ihn zu Wochenbeginn oder -ende, beim Review des Erledigten oder bei der Planung der kommenden Woche. Auslösen mit "Wochenrückblick", "was steht an", "Woche im Rückblick".
---

# Wochenrückblick-Skill

Sammle offene Arbeit, bewerte den Fortschritt, mache Blocker sichtbar und erstelle einen klaren Plan für die kommende Woche — alles in einem strukturierten Durchgang. Die Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Aufgaben-Manager über MCP** (z. B. Jira, Linear, Asana, Todoist, Monday.com, Notion) | Offene Aufgaben, Fälligkeiten, Status, Verantwortliche |
| **Kalender über MCP** (z. B. Google Calendar, Outlook Calendar) | Anstehende Meetings, Zeitblöcke, Fristen |
| **E-Mail & Chat über MCP** (z. B. Gmail, Outlook, Slack, Microsoft Teams) | Action Items aus Korrespondenz, Zusagen aus Gesprächen, Erwähnungen |
| **companyM365** (falls aktiviert) | Outlook-Kalender und -Mails, Teams-Nachrichten, Aufgaben aus Microsoft To Do und Planner aus deinem Microsoft-365-Konto |
| **companyRAG / Datei-Upload** | Review-Vorlagen, Projekt-Briefs, Meeting-Notizen mit Action Items |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Review-Workflow

Führe diese Schritte der Reihe nach aus. Der Rückblick wirkt am besten, wenn er zu einem festen Zeitpunkt erfolgt — entweder Freitagnachmittag (Woche abschließen) oder Montagmorgen (Woche eröffnen).

### Schritt 1: Offene Punkte sammeln

Sammle alles, was in Arbeit, überfällig oder anstehend ist:

**Aus Aufgaben-Managern** (falls angebunden):

- Alle dem Nutzer zugewiesenen Aufgaben mit Status ≠ Erledigt/Geschlossen
- Diese Woche abgeschlossene Aufgaben (für die Retrospektive)
- In den nächsten 7 Tagen fällige Aufgaben
- Überfällige Aufgaben

**Aus dem Kalender** (falls angebunden):

- Meetings und Termine für die kommende Woche
- Fristen oder Meilensteine, die als Kalendereinträge erscheinen
- Wiederkehrende Verpflichtungen (Standups, 1:1s, Reviews)

**Aus E-Mail und Chat** (falls angebunden):

- Action Items aus der Korrespondenz der vergangenen Woche
- Ausstehende Antworten oder Zusagen
- Erwähnungen, die ein Follow-up erfordern

**Aus Nutzereingaben**:

- Aufgaben, Projekte oder Verpflichtungen, die in keinem Tool erfasst sind
- Persönliche Ziele oder Entwicklungspunkte
- Punkte, die dir während des Review-Prozesses einfallen

### Schritt 2: Kategorisieren und bewerten

Ordne die gesammelten Punkte in diese Kategorien ein:

| Kategorie | Definition | Aktion |
| --- | --- | --- |
| **Diese Woche abgeschlossen** | Seit dem letzten Review fertiggestellte Aufgaben | Anerkennen und archivieren. Notiere, was deutlich länger oder kürzer gedauert hat als erwartet. |
| **In Arbeit** | Begonnen, aber nicht abgeschlossen | Bewerten: im Plan, gefährdet oder blockiert? Restaufwand schätzen. |
| **Übertrag** | Für diese Woche geplant, aber nicht begonnen | Warum ist es nicht passiert? Für nächste Woche neu priorisieren oder bewusst verschieben. |
| **Überfällig** | Über dem Fälligkeitsdatum und nicht abgeschlossen | Eskalieren, Frist neu verhandeln oder neu priorisieren. Überfällige Punkte brauchen eine Entscheidung, nicht nur eine Notiz. |
| **Anstehend (nächste 7 Tage)** | In der kommenden Woche fällig oder geplant | Aufwand schätzen und nach Möglichkeit bestimmten Tagen zuordnen. |
| **Warten auf andere** | Durch die Aktion einer anderen Person blockiert | Notiere wer, was und wann du zuletzt nachgehakt hast. Plane ein Follow-up, wenn es alt ist. |
| **Irgendwann / Backlog** | Punkte ohne Frist, aber weiterhin relevant | Quartalsweise prüfen. Steht ein Punkt 4+ Wochen ohne Fortschritt auf dieser Liste, entscheide: einplanen oder verwerfen. |

### Schritt 3: Muster und Blocker erkennen

Schau über die kategorisierten Punkte hinweg nach systemischen Problemen:

- Wiederkehrender Übertrag : Erscheint dieselbe Aufgabe 2+ Wochen als Übertrag, deutet das auf Überlastung, unklare Anforderungen oder Vermeidung hin. Benenne es.
- Zeit-Missverhältnis : Ist der Kalender voller Meetings, die Aufgabenliste erwartet aber 20 Stunden Fokusarbeit, gibt es ein Rechenproblem. Markiere es.
- Blocker-Häufung : Sind mehrere Punkte durch dieselbe Person, dasselbe Team oder dieselbe Abhängigkeit blockiert? Das ist ein einzelner Blocker zum Eskalieren, nicht viele separate.
- Prioritätsdrift : Verdrängen dringend-aber-unwichtige Aufgaben wichtig-aber-nicht-dringende Arbeit? Notiere die Drift.

### Schritt 4: Die kommende Woche planen

Übersetze die Bewertung in einen konkreten Plan:

1. 3–5 Prioritäten wählen : Keine vollständige Aufgabenliste — die 3–5 wichtigsten Ergebnisse für die kommende Woche. Das sind die Punkte, die die Woche zum Erfolg machen, wenn sie erledigt sind.
2. Zeitblock-Schätzungen : Schätze für jede Priorität die benötigte Fokuszeit. Vergleiche sie mit der verfügbaren Fokuszeit (Kalender minus Meetings, minus Puffer für reaktive Arbeit).
3. Tageszuordnung (optional, aber empfohlen): Ordne Prioritäten bestimmten Tagen zu — nach Fristen, Energie und Meeting-Mustern. Die wichtigste Arbeit nach vorne ziehen.
4. Follow-up-Liste : Punkte, bei denen du jemandem nachgehen, ein Update senden oder einen Status prüfen musst.
5. Bewusste Verschiebungen : Punkte, die du ausdrücklich in eine spätere Woche schiebst — nicht vergessen, sondern bewusst niedriger priorisiert. Notiere den Grund.

### Schritt 5: Das Review-Dokument erstellen

Erstelle die strukturierte Ausgabe mit der Vorlage unten.

## Ausgabevorlage: Wochenrückblick

```
# Wochenrückblick — [Woche vom DATUM]

## Letzte Woche: Was erledigt wurde
  ✓ [Abgeschlossener Punkt 1]
  ✓ [Abgeschlossener Punkt 2]
  ✓ [Abgeschlossener Punkt 3]
  ...

  Highlights: [1–2 Sätze zu dem, was gut lief, oder bemerkenswerten Erfolgen]

## Übertragen (nicht abgeschlossen)
  → [Punkt 1] — Grund: [warum es nicht passierte] — Entscheidung: [nächste Woche / verschieben / verwerfen]
  → [Punkt 2] — Grund: [...] — Entscheidung: [...]

## Aktuell in Arbeit
  ⟳ [Punkt 1] — Status: [im Plan / gefährdet / blockiert] — ETA: [Schätzung]
  ⟳ [Punkt 2] — Status: [...] — ETA: [...]

## Überfällig
  ⚠ [Punkt 1] — Fällig: [Datum] — Aktion: [neu verhandeln / eskalieren / bis X abschließen]

## Warten auf andere
  ⏳ [Punkt 1] — Warten auf: [Person] — Seit: [Datum] — Follow-up: [Plan]

## Diese Woche: Prioritäten
  1. [Priorität 1] — Geschätzte Zeit: [Stunden] — Fällig: [Datum oder "keine harte Frist"]
  2. [Priorität 2] — Geschätzte Zeit: [Stunden] — Fällig: [Datum]
  3. [Priorität 3] — Geschätzte Zeit: [Stunden] — Fällig: [Datum]

  Verfügbare Fokuszeit: ~[Stunden] (basierend auf [Gesamtstunden] minus [Meeting-Stunden] minus [Puffer])

## Zu sendende Follow-ups
  - [Follow-up 1] — An: [Person] — Bis: [Tag]
  - [Follow-up 2] — An: [Person] — Bis: [Tag]

## Bewusst verschoben
  ↓ [Punkt 1] — Verschoben auf: [Woche/Datum] — Grund: [warum]

## Beobachtete Muster
  [Systemische Beobachtungen aus Schritt 3]

## Notizen für das nächste Review
  [Was du dir merken oder nächste Woche prüfen solltest]
```

## Varianten der Review-Kadenz

Die Kernmethodik passt sich an verschiedene Kadenzen an:

| Kadenz | Wann verwenden | Anpassung |
| --- | --- | --- |
| **Wöchentlich** (Standard) | Standard-Wissensarbeit | Vollständiger Workflow wie oben beschrieben |
| **Zweiwöchentlich** | Geringeres Aufgabenvolumen oder längere Projektzyklen | Retrospektiven-Fenster verlängern; einen Pulse-Check in der Mitte ergänzen |
| **Daily-Standup-Vorbereitung** | High-Velocity-Umgebungen | Verkürzt: Schritte 3–4 überspringen; Fokus auf die 1–3 Punkte des Tages und Blocker |
| **Monatlich** | Strategisches/Leadership-Review | Ergänzen: Zielfortschritt, OKR-Check-in, Delegations-Bewertung, Team-Kapazität |

## Leitplanken

- Erfinde NIEMALS Aufgabenstatus oder Kalendereinträge — wenn Daten nicht verfügbar sind, frage den Nutzer.
- Priorisiere NIEMALS für den Nutzer ohne dessen Input — präsentiere die Punkte und eine empfohlene Reihenfolge, formuliert als Vorschlag.
- Schätze NIEMALS fachspezifische Arbeit ohne den Input des Nutzers — frage bei technischen oder spezialisierten Aufgaben nach Aufwandsschätzungen.
- Kennzeichne Ausgaben: `[Aus angebundener Quelle]`, `[Aus Nutzereingabe]`, `[Vorschlag]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um einen formatierten, sofort teilbaren Rückblick zu erhalten.
