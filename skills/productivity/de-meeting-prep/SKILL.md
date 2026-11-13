---
name: de-meeting-prep
description: Erstellt Agenda-Entwürfe und Pre-Read-Briefings aus Kalenderkontext, früheren Meeting-Notizen und angebundenen Quellen. Verwende ihn, wenn du dich auf ein Meeting vorbereitest, Agenden erstellst oder Pre-Reads zusammenstellst. Auslösen mit "bereite mein Meeting mit … vor", "Agenda erstellen für", "Meeting-Brief für".
---

# Meeting-Vorbereitung-Skill

Sammle Kontext aus Kalendern, E-Mail, Chat und Notizen, um Agenden zu entwerfen, Pre-Read-Briefings zusammenzustellen und Gesprächspunkte für jedes Meeting vorzuschlagen. Die Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Kalender über MCP** (z. B. Google Calendar, Outlook) | Meeting-Titel, Zeit, Teilnehmende, Ort, angehängte Agenda |
| **E-Mail über MCP** (z. B. Gmail, Outlook) | Aktueller Schriftverkehr mit Teilnehmenden, geteilte Dokumente |
| **Chat über MCP** (z. B. Slack, Microsoft Teams) | Aktuelle Konversationen mit Teilnehmenden, Channel-Kontext |
| **Dokumente über MCP** (z. B. Notion, Confluence, Google Docs) | Frühere Meeting-Notizen, geteilte Dokumente, Projektseiten |
| **CRM über MCP** (z. B. Salesforce, HubSpot) | Account-Historie, Deal-Status, Kontaktdetails (für externe Meetings) |
| **Issue-Tracker über MCP** (z. B. Jira, Linear, Asana) | Offene Punkte zum Meeting-Thema |
| **companyM365** (falls aktiviert) | Outlook-Kalender und -Mails, Teams-Nachrichten und OneDrive-/SharePoint-Dokumente aus deinem Microsoft-365-Konto |
| **companyRAG / Datei-Upload** | Wiederkehrende Meeting-Vorlagen, Hintergrunddokumente |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Vorbereitungs-Workflow

Führe diese Schritte für jede Meeting-Vorbereitung aus. Die Vorbereitungstiefe skaliert mit der Wichtigkeit des Meetings — ein kurzes 1:1 braucht weniger als eine Vorstandspräsentation.

### Schritt 1: Das Meeting identifizieren

Kläre die Grundlagen:

- Meeting-Typ: 1:1, Team-Standup, Projektreview, Kundencall, Vorstandssitzung, Interview, Brainstorming, Entscheidungsmeeting, Informationsmeeting, Retrospektive
- Teilnehmende: Wer nimmt teil? Welche Rollen haben sie? Sind externe Personen dabei (Kunden, Partner, Lieferanten)?
- Dauer: Wie lang ist das Meeting? Das begrenzt die Agenda.
- Ziel: Was soll nach dem Meeting wahr sein, das vorher nicht wahr war? Wenn der Nutzer das nicht formulieren kann, hilf ihm dabei — ein Meeting ohne Ziel ist ein Meeting ohne Wert.
- Wiederholung: Einmalig oder wiederkehrend? Bei wiederkehrenden Meetings frühere Notizen heranziehen, falls verfügbar.

### Schritt 2: Kontext sammeln

Ziehe relevante Informationen aus angebundenen Quellen:

**Frühere Meetings mit diesen Teilnehmenden:**

- Letzte Meeting-Notizen, Action Items, getroffene Entscheidungen
- Offene Action Items aus vorherigen Sitzungen
- Vertagte oder geparkte Themen

**Aktueller Schriftverkehr:**

- E-Mail-Threads mit Teilnehmenden aus den letzten 1–2 Wochen
- Chat-Nachrichten in relevanten Channels
- Kürzlich bearbeitete geteilte Dokumente

**Relevanter Projekt-/Account-Status:**

- Offene Aufgaben oder Issues zum Meeting-Thema
- Bei externen Meetings: Account-Status, Deal-Phase, jüngste Interaktionen aus dem CRM
- Bei Projektmeetings: Meilenstein-Status, Blocker, jüngste Änderungen

**Hintergrunddokumente:**

- Bereits vom Organisator geteilte Pre-Reads
- Relevante Richtlinien, Spezifikationen oder Referenzmaterialien aus companyRAG-Sammlungen

Wenn keine angebundenen Quellen verfügbar sind, bitte den Nutzer um den vorhandenen Kontext. Schon eine Zwei-Satz-Zusammenfassung von "worum es in diesem Meeting geht und was letztes Mal passiert ist" verbessert die Vorbereitungsqualität deutlich.

### Schritt 3: Agenda entwerfen

Baue die Agenda nach diesem Schema auf:

**Agenda-Struktur:**

```
# [Meeting-Titel]
Datum: [Datum und Uhrzeit]
Dauer: [Länge]
Teilnehmende: [Liste]
Ziel: [was nach dem Meeting wahr sein soll]

## Agenda

1. [Eröffnung / Check-in]                         [X Min]
   - [Kurzer Kontext-Einstieg oder Warm-up]

2. [Thema A — höchste Priorität]                  [X Min]
   - Kontext: [1–2 Sätze Hintergrund]
   - Entscheidung nötig: [ja/nein — falls ja, welche Entscheidung]
   - Pre-Read: [Link oder Referenz, falls vorhanden]

3. [Thema B]                                      [X Min]
   - Kontext: [...]
   - Entscheidung nötig: [...]

4. [Thema C]                                      [X Min]
   - Kontext: [...]

5. [Action Items und nächste Schritte]            [5 Min]
   - Getroffene Entscheidungen durchgehen
   - Action Items mit Verantwortlichen und Fristen zuweisen

## Offene Punkte aus dem letzten Meeting
  - [Punkt 1] — Verantwortlich: [Name] — Status: [erledigt / in Arbeit / nicht begonnen]
  - [Punkt 2] — ...
```

**Agenda-Prinzipien:**

- Timeboxe jeden Punkt. Die gesamte Zeitzuteilung darf die Meeting-Dauer minus 5 Minuten nicht überschreiten (Puffer für Überziehen und Abschluss).
- Priorisiere rigoros. Setze das wichtigste oder zeitkritischste Thema nach vorne. Falls das Meeting überzieht, wurde zumindest der kritische Punkt behandelt.
- Unterscheide Entscheidungen von Diskussionen. Markiere Themen, die eine Entscheidung erfordern — dafür braucht es den Entscheider und genug Kontext für eine fundierte Wahl.
- Begrenze auf 3–5 substanzielle Punkte für ein 30-Minuten-Meeting, 5–7 für ein 60-Minuten-Meeting. Mehr Punkte garantieren, dass nichts ausreichend Aufmerksamkeit bekommt.
- Nimm offene Punkte aus dem letzten Meeting auf. Verbindlichkeit braucht Sichtbarkeit.

### Schritt 4: Pre-Read-Briefing zusammenstellen

Für Meetings, bei denen Teilnehmende Hintergrund brauchen (Projektreviews, Kundencalls, Vorstandssitzungen), erstelle ein Briefing-Dokument:

```
# Meeting-Brief: [Titel]
Erstellt: [Datum]
Meeting: [Datum und Uhrzeit]

## TL;DR
  [2–3 Sätze: warum wir uns treffen, was am wichtigsten ist, was wir entscheiden müssen]

## Kontext
  [Hintergrund, den die Teilnehmenden brauchen — maximal 1 Seite. Verlinke detaillierte Quellen, statt sie zu reproduzieren.]

## Wichtige Datenpunkte
  - [Kennzahl oder Fakt 1] — Quelle: [woher das stammt]
  - [Kennzahl oder Fakt 2] — Quelle: [...]
  - [Kennzahl oder Fakt 3] — Quelle: [...]

## Offene Fragen
  1. [Frage, die in diesem Meeting geklärt werden muss]
  2. [Frage 2]

## Relevante Historie
  - [Datum]: [Was passiert ist — Entscheidung, Meilenstein oder Änderung]
  - [Datum]: [...]

## Vorgeschlagene Gesprächspunkte
  - [Punkt 1 — was anzusprechen ist und warum]
  - [Punkt 2]
  - [Punkt 3]
```

**Briefing-Prinzipien:**

- Kürze vor Vollständigkeit. Ein einseitiges Brief, das gelesen wird, schlägt ein 10-seitiges Dokument, das es nicht wird.
- Belege alles mit Quellen. Jeder Datenpunkt, jede Aussage und jede historische Referenz muss ihre Quelle nennen, damit Teilnehmende bei Bedarf tiefer gehen können.
- Führe mit der Entscheidung oder der Bitte. Braucht das Meeting eine Entscheidung, setze Frage und Optionen nach vorne — den Kontext danach.

### Schritt 5: Gesprächspunkte vorschlagen

Schlage auf Basis des gesammelten Kontexts konkrete Gesprächspunkte vor, die der Nutzer ansprechen sollte:

| Typ | Wann vorschlagen | Format |
| --- | --- | --- |
| **Follow-up aus früherem Meeting** | Ein Action Item wurde vergeben oder ein Thema vertagt | "Letztes Mal haben wir [X] vereinbart. Status-Update?" |
| **Proaktives Update** | Der Nutzer hat Fortschritte oder Neuigkeiten für die Teilnehmenden | "Teile, dass [Meilenstein] erreicht / [Blocker] gelöst wurde" |
| **Frage stellen** | Eine Information wird von einer teilnehmenden Person benötigt | "Frage [Person] zu [Thema] — nötig für [Grund]" |
| **Risiko markieren** | Ein Risiko oder eine Sorge sollte früh angesprochen werden | "Markiere, dass [Risiko] [Timeline/Ergebnis] beeinflussen könnte" |
| **Entscheidung treiben** | Eine offene Entscheidung braucht Aufmerksamkeit | "Wir müssen über [Thema] entscheiden — Optionen sind [A] oder [B]" |

## Schnellanleitungen je Meeting-Typ

Passe die Workflow-Tiefe an den Meeting-Typ an:

| Meeting-Typ | Vorbereitungstiefe | Schwerpunkt |
| --- | --- | --- |
| **1:1 (Führungskraft/Mitarbeitende)** | Leicht — 5–10 Min Vorbereitung | Offene Action Items, Blocker, Karriere-/Entwicklungsthemen |
| **Team-Standup** | Minimal — 2 Min Vorbereitung | Eigener Status, Blocker, benötigte Hilfe |
| **Projektreview** | Mittel — 15–20 Min Vorbereitung | Meilenstein-Status, Risiken, nötige Entscheidungen, Timeline |
| **Kunden-/Externer Call** | Voll — 20–30 Min Vorbereitung | Account-Historie, Beziehungskontext, Ziele, Pre-Read |
| **Vorstand/Executive** | Voll — 30+ Min Vorbereitung | Narrative Struktur, Kernkennzahlen, Entscheidungen, Pre-Read-Paket |
| **Interview** | Mittel — 15 Min Vorbereitung | Rollenanforderungen, Kandidaten-Hintergrund, vorbereitete Fragen |
| **Brainstorming** | Leicht — 10 Min Vorbereitung | Problemdefinition, Rahmenbedingungen, Seed-Ideen, kreative Prompts |

## Leitplanken

- Erfinde niemals Meeting-Historie oder Hintergründe zu Teilnehmenden — wenn frühere Notizen oder Org-Daten nicht verfügbar sind, frage den Nutzer.
- Erzeuge niemals erfundene Kennzahlen oder Datenpunkte für Briefings — verwende `[Daten nötig — Nutzer fragen]` als Platzhalter.
- Nimm niemals das Meeting-Ziel an — frage nach, bevor du die Agenda entwirfst.
- Kennzeichne Ausgaben: `[Aus angebundener Quelle]`, `[Aus Nutzereingabe]`, `[Vorschlag]`, `[Daten nötig]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um eine formatierte, sofort teilbare Agenda oder ein Briefing zu erhalten.
