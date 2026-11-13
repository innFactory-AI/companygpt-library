---
name: de-status-report
description: Erstellt funktionsübergreifende Statusberichte mit Risiko-Highlights, Abhängigkeits-Tracking und Executive-Summary-Formatierung. Verwende ihn, wenn du wöchentliche Projekt-Updates, Reports auf Programmebene oder Executive-Briefings vorbereitest. Auslösen mit "Statusbericht für", "Projekt-Update", "Wochenbericht".
---

# Statusbericht-Skill

Erstelle funktionsübergreifende Statusberichte, die Fortschritt, Risiken, Abhängigkeiten und benötigte Entscheidungen sichtbar machen — zugeschnitten auf die jeweilige Zielgruppe. Die Daten dafür kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Asana, Linear, Monday) | Sprint-Fortschritt, Ticket-Status, Blocker, Velocity |
| **Kalender / Meeting-Notizen über MCP** | Aktuelle Entscheidungen, Action Items, anstehende Meilensteine |
| **Risikoregister** | Offene Risiken, Status der Gegenmaßnahmen, neu aufgekommene Risiken |
| **Kommunikationskanäle über MCP** (z. B. Slack, Teams) | Eskalationen, teamübergreifende Anfragen, gemeldete Blocker |
| **companyM365** (falls aktiviert) | Outlook-Kalender und -Mails, Teams-Nachrichten, OneNote-Seiten und Transkripte von Teams-Meetings |
| **companyRAG-Sammlungen / Datei-Upload** | Frühere Statusberichte, Programmpläne, OKRs |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Workflow

### 1. Updates je Workstream sammeln

Sammle für jeden Workstream oder Projekt-Track:

```
WORKSTREAM-UPDATE:
  Workstream:            [Name]
  Verantwortlich:        [Person oder zuständiges Team]
  Zeitraum:              [Berichtszeitraum — z. B. Woche vom 2025-04-01]
  Wichtige Ergebnisse:   [was abgeschlossen oder geliefert wurde]
  In Arbeit:             [woran aktiv gearbeitet wird]
  Als Nächstes geplant:  [was für den nächsten Zeitraum vorgesehen ist]
  Blocker:               [alles, was den Fortschritt verhindert — mit Verantwortlichem und Alter]
  Entscheidungen nötig:  [Entscheidungen, die die Zielgruppe treffen oder kennen muss]
```

Hole Updates aus jedem Workstream ein, bevor du den Status bewertest. Bewerte den RAG-Status niemals auf Basis von Annahmen — nutze Daten der Workstream-Verantwortlichen.

### 2. RAG-Status bewerten

Wende RAG (Red / Amber / Green) über alle Workstreams hinweg konsistent anhand eines definierten Rasters an:

| Status | Kriterien | Erforderliche Maßnahme |
| --- | --- | --- |
| **🟢 Green** | Auf Kurs — Meilensteine im Zeitplan, keine ungeminderten Risiken, Abhängigkeiten geklärt | Wie geplant fortfahren; keine Eskalation nötig |
| **🟡 Amber** | Gefährdet — Verzögerung möglich, Risiken identifiziert aber Gegenmaßnahmen laufen, Abhängigkeiten noch nicht bestätigt | Eng beobachten; Maßnahmenplan erforderlich; bei ausbleibender Besserung bis zum nächsten Zeitraum an Sponsor melden |
| **🔴 Red** | Vom Kurs abgekommen — Meilenstein verfehlt oder wird verfehlt, ungemindertes kritisches Risiko, Blocker ohne Lösungsweg | Sofortige Eskalation; Recovery-Plan erforderlich; Sponsor-Entscheidung nötig |

### RAG-Bewertungsdisziplin

- RAG basiert auf objektiven Kriterien, nicht auf Optimismus. Ein Workstream mit einem ungelösten Blocker ist nicht Green, nur weil das Team "erwartet, dass es bald behoben ist".
- Verfolge den RAG-Trend: ↑ Verbessert sich , → Stabil , ↓ Verschlechtert sich — die Richtung zählt genauso wie die aktuelle Farbe.
- War ein Workstream im letzten Zeitraum Amber und ist immer noch Amber ohne Fortschritt bei der Gegenmaßnahme, eskaliere — dauerhaftes Amber ist oft ein nicht eingestandenes Red.

### 3. Risiken und Abhängigkeiten identifizieren

Extrahiere übergreifende Risiken und Abhängigkeiten zwischen Workstreams:

```
RISIKO- / ABHÄNGIGKEITS-LOG:
  Element:              [Beschreibung]
  Typ:                  [Risiko / Abhängigkeit / Blocker]
  Betrifft:             [welche(n) Workstream(s)]
  Verantwortlich:       [wer für die Lösung zuständig ist]
  Status:               [Offen / In Arbeit / Gelöst]
  Fälligkeit:           [bis wann eine Lösung nötig ist]
  Auswirkung ohne Lösung: [was passiert, wenn es nicht adressiert wird]
```

Abhängigkeiten zwischen Workstreams sind die häufigste Ursache für Risiken auf Programmebene. Mache sie explizit sichtbar — Teams nehmen oft an, das andere Team wisse Bescheid.

### 4. Für die Zielgruppe formatieren

Schneide den Bericht auf die Lesenden zu. Dieselben zugrunde liegenden Daten werden je nach Entscheidungsbefugnis und Detailbedürfnis der Zielgruppe unterschiedlich dargestellt.

## Zuschnitt auf die Zielgruppe

| Zielgruppe | Fokus | Detailtiefe | RAG-Tiefe | Empfohlene Länge |
| --- | --- | --- | --- | --- |
| **Executive / C-Level** | Strategischer Fortschritt, Top-Risiken, nötige Entscheidungen | Nur Headlines und Zahlen — keine Umsetzungsdetails | Gesamt-Programm-RAG + Top-3-Workstream-RAGs | 1 Seite / 5-Minuten-Lesezeit |
| **Steering Committee** | Workstream-übergreifende Abhängigkeiten, Risikominderung, Ressourcenfragen | Moderat — genug Kontext für fundierte Entscheidungen | RAG je Workstream mit Trendpfeilen | 2–3 Seiten / 10-Minuten-Lesezeit |
| **Programm- / Projektteam** | Detaillierter Fortschritt, Blocker, nächste Schritte, Action Items | Hoch — operative Details für die Umsetzung | RAG je Workstream mit belegenden Daten | 3–5 Seiten / 15-Minuten-Lesezeit |
| **Stakeholder-Gruppe** | Auswirkung auf ihren Bereich, anstehende Änderungen, was sie tun müssen | Selektiv — nur was ihren Bereich betrifft | RAG nur für relevante Workstreams | 1–2 Seiten / 5-Minuten-Lesezeit |

### Regeln für Executive-Berichte

- Beginne mit dem wichtigsten Punkt: "Programm ist auf Kurs für den Q3-Launch" oder "Programm ist gefährdet — Entscheidung zum Scope bis Freitag nötig"
- Kein Jargon, keine Akronyme ohne Erläuterung, keine technischen Umsetzungsdetails
- Jedes genannte Risiko braucht ein "Was bedeutet das" — die Konsequenz und die Anforderung
- Schließe mit den explizit von der Zielgruppe erbetenen Entscheidungen oder Maßnahmen

### Regeln für Team-Berichte

- Liefere genug operative Details, damit Teammitglieder auf Basis der Informationen handeln können
- Blocker müssen einen Verantwortlichen und ein erwartetes Lösungsdatum nennen
- Action Items werden mit Status-Updates aus früheren Berichten übernommen — lass nie Punkte stillschweigend verschwinden
- Feiere Abschlüsse — die Anerkennung gelieferter Arbeit erhält die Team-Dynamik

## Ausgabevorlage

```
# Statusbericht — [Programm-/Projektname]
# Zeitraum: [Berichtszeitraum]
# Gesamtstatus: [🟢/🟡/🔴] [Trendpfeil]

## Executive Summary
- Gesamt: [einsatziger Programmstatus]
- Wichtigster Erfolg: [bedeutendste Leistung in diesem Zeitraum]
- Top-Risiko: [Risiko mit höchster Priorität samt Auswirkungsaussage]
- Entscheidung nötig: [falls vorhanden — was, von wem, bis wann]

## Workstream-Status

| Workstream | Verantwortlich | Status | Trend | Wichtigstes Update |
|---|---|---|---|---|
| [Name] | [Verantwortlich] | [🟢/🟡/🔴] | [↑/→/↓] | [einzeilige Zusammenfassung] |

## Workstream-Detail
[Abschnitte je Workstream mit Ergebnissen, In Arbeit, Geplant, Blockern]

## Risiken und Abhängigkeiten

| # | Typ | Beschreibung | Betrifft | Verantwortlich | Status | Fällig |
|---|---|---|---|---|---|---|
| 1 | [Risiko/Abh./Blocker] | [Beschreibung] | [Workstreams] | [Verantwortlich] | [Status] | [Datum] |

## Benötigte Entscheidungen
[Von der Zielgruppe erforderliche Entscheidungen — was, Kontext, Optionen, Empfehlung, Frist]

## Maßnahmen und Follow-ups

| # | Maßnahme | Verantwortlich | Fällig | Status |
|---|---|---|---|---|
| [aus letztem Bericht übernommene + neue Punkte] |

## Ausblick auf den nächsten Zeitraum
- Anstehende wichtige Meilensteine: [Liste]
- Erwartete Statusänderungen: [Workstreams, die voraussichtlich den RAG wechseln]
```

## Leitplanken

- Erfinde niemals Fortschritts-Prozentsätze, Termine oder Meilenstein-Status. Alle Fortschrittsdaten stammen aus den Projekt-Tracking-Daten des Nutzers.
- Erfinde niemals Risiken oder Blocker. Frage nach Risikodaten, statt plausibel klingende Risiken zu generieren.
- Vergib niemals einen RAG-Status ohne Beleg. Sind die Daten unzureichend, kennzeichne als `[Daten nicht verfügbar — Status ausstehend vom Verantwortlichen]`.
- Kennzeichne generierte Inhalte: `[Aus Projektdaten]`, `[Framework-Methodik]`, `[KI-Entwurf — mit Workstream-Verantwortlichem prüfen]`.

> **Tipp:** Fordere über companyFILES eine DOCX-, Markdown- oder PPTX-Ausgabe an, um einen formatierten, sofort verteilbaren Bericht zu erhalten.
