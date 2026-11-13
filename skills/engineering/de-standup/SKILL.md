---
name: de-standup
description: Generate standup summaries from task context, recent commits, and open PRs. Use when preparing for daily standup, writing async standup updates, or summarising team activity. Trigger with "standup update", "what did I work on", "team standup summary".
---

# Standup-Skill

Erstelle Standup-Updates aus Aktivitätsdaten der angebundenen Werkzeuge. Der Skill funktioniert sowohl für synchrone Standups (Gesprächspunkte) als auch für asynchrone Updates (geschriebene Posts). Die Aktivitätsdaten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Git-Provider über MCP** (z. B. GitHub, GitLab, Bitbucket) | Commits seit dem letzten Standup, offene/gemergte PRs |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear, Asana, Shortcut) | Aufgaben in Arbeit, abgeschlossen und blockiert |
| **Chat über MCP** (z. B. Slack, Teams) | Threads mit Blockern oder Entscheidungen |
| **companyM365** (falls aktiviert) | Teams-Nachrichten und Outlook-Kalender aus deinem Microsoft-365-Konto |
| **companyRAG / Datei-Upload** | Sprint-Ziele, bevorzugtes Standup-Format des Teams |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Standup-Workflow

### Schritt 1: Jüngste Aktivität sammeln

Sammle die Daten der angebundenen Werkzeuge für den Berichtszeitraum (Standard: seit dem letzten Werktag). Sind keine Werkzeuge angebunden, frage den Nutzer nach den Informationen.

**Zu sammelnde Daten:**

| Kategorie | Quelle | Worauf achten |
| --- | --- | --- |
| **Abgeschlossene Arbeit** | Projekt-Tracker (erledigt/geschlossen), Git (gemergte PRs) | Auf erledigt gesetzte Tickets, gemergte PRs, ausgelieferte Features |
| **Laufende Arbeit** | Projekt-Tracker (in Arbeit), Git (offene PRs, jüngste Commits) | In Bearbeitung befindliche Tickets, PRs im Review, aktive Branches |
| **Blockierte Arbeit** | Projekt-Tracker (blockiert/pausiert), Nutzereingabe | Als blockiert markierte Tickets, PRs, die seit über 24 h auf Review warten, Abhängigkeit von einem anderen Team |
| **Anstehende Arbeit** | Projekt-Tracker (zu erledigen/als Nächstes), Sprint-Board | Nächste Prioritäten nach Abschluss der aktuellen Aufgaben |

### Schritt 2: Kategorisieren und priorisieren

Ordne die gesammelten Daten in die Standup-Struktur ein. Wende diese Regeln an:

1. Beginne mit Blockern. Blocker sind der einzige Standup-Punkt, der Handeln durch andere erfordert. Stelle sie an den Anfang, damit das Team sie angehen kann.
2. Fasse zusammen, statt aufzuzählen. "Am Auth-Refactoring gearbeitet — 3 PRs gemergt, 1 im Review" ist besser als jeden einzelnen PR-Titel zu listen.
3. Verknüpfe mit Zielen. Wenn Sprint-Ziele vorliegen, ordne abgeschlossene und laufende Arbeit den Zielen zu, die sie voranbringen.
4. Markiere Risiken. Droht laufende Arbeit, eine Deadline zu verpassen, weise unter den Blockern oder als separaten Risikohinweis darauf hin.
5. Lass Rauschen weg. Triviale Commits (Tippfehler, Formatierung), bot-generierte PRs und administrative Aufgaben gehören nicht ins Standup, es sei denn, sie stehen für nennenswerten Aufwand.

### Schritt 3: Ausgabe formatieren

Verwende das passende Format je nach Kontext.

## Individuelles Standup-Update

```
## Standup — [Name] — [Datum]

### Blocker
- [Beschreibung des Blockers — wer/was zum Auflösen nötig ist — wie lange blockiert]
[oder: Keine Blocker]

### Gestern (Abgeschlossen)
- [Arbeitspunkt — Ergebnis oder Fortschritt — verlinktes Ticket/PR falls relevant]

### Heute (Geplant)
- [Arbeitspunkt — konkretes Ziel für heute — verlinktes Ticket falls relevant]

### Risiken / FYI
- [Was das Team wissen sollte — nahende Deadline, Scope-Änderung, Abhängigkeit]
[oder: Abschnitt weglassen, falls keine]
```

## Team-Standup-Zusammenfassung

Wenn du für das gesamte Team zusammenfasst:

```
## Team-Standup — [Teamname] — [Datum]

### Blocker (Handeln erforderlich)
- [Person]: [Blocker] — braucht [Aktion/Person]

### Fortschritt Sprint-Ziele
- Ziel 1: [Zielbeschreibung] — [im Plan / gefährdet / blockiert] — [kurzer Status]
- Ziel 2: [Zielbeschreibung] — [im Plan / gefährdet / blockiert] — [kurzer Status]

### Highlights
- [Bemerkenswerte Abschlüsse, Deployments oder Meilensteine]

### In Arbeit
- [Person]: [Hauptfokus heute]

### Risiken
- [Risiken für Sprint-Zusagen oder anstehende Deadlines]
```

## Asynchrones Standup-Format

Für Teams mit asynchronen Standups (Slack-/Teams-Posts):

```
**[Name] — [Datum]**
✅ Erledigt: [abgeschlossene Punkte, kurz]
🔄 In Arbeit: [laufende Punkte, kurz]
🚫 Blockiert: [Blocker mit benötigter Aktion]
```

Halte asynchrone Updates auf maximal 3–5 Zeilen. Wird mehr Detail benötigt, verlinke das Ticket oder den PR.

## Qualitäts-Checkliste fürs Standup

- Blocker sind konkret und nennen, was zum Auflösen nötig ist
- Abgeschlossene Punkte beschreiben Ergebnisse, nicht nur Aktivität ("Auth-Fix ausgeliefert" statt "am Code gearbeitet")
- Geplante Punkte sind konkret genug, dass das Team weiß, was du erledigen willst
- Keine Punkte, die älter als 2 Standups sind — wiederkehrende Punkte brauchen ein anderes Gespräch (Eskalation oder Re-Scoping)
- Das Update ist knapp genug, um es in unter 90 Sekunden vorzutragen (synchron) oder in unter 30 Sekunden zu lesen (asynchron)

## Leitplanken

- Erfinde niemals Aktivität. Liegen keine Daten vor, gib an: "Keine Aktivitätsdaten verfügbar — gib dein Update an oder binde [Werkzeugname] an."
- Rate niemals den Ticket-Status. Ist der Status aus dem Projekt-Tracker nicht verfügbar, frage den Nutzer, statt etwas anzunehmen.
- Erfinde niemals Blocker oder Risiken. Berichte nur, was durch Daten oder Nutzereingabe als blockiert oder gefährdet bestätigt ist.
- Versieh jeden Punkt mit einer Quellenkennzeichnung: `[Aus Projekt-Tracker]`, `[Aus Git]` oder `[Aus Nutzereingabe]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um ein sofort teilbares Update zu erhalten.
