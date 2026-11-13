---
name: de-sprint-planning
description: Plant Sprints, indem er den Arbeitsumfang abgrenzt, die Kapazität schätzt, Ziele setzt und Abhängigkeiten kartiert. Verwende ihn beim Start eines neuen Sprints, beim Umpriorisieren mitten im Sprint oder beim Prüfen der Kapazität für anstehende Arbeit. Auslösen mit "nächsten Sprint planen", "Sprint-Planung für", "was passt in diesen Sprint".
---

# Sprint-Planung-Skill

Plane Iterationszyklen mit fester Länge — grenze den Arbeitsumfang an die Kapazität an, setze ergebnisorientierte Sprint-Ziele, kartiere Abhängigkeiten und unterscheide feste Zusagen von Stretch-Zielen. Team-Metriken und Backlog-Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear, GitHub) | Backlog-Items, Story-Schätzungen, historische Velocity, Sprint-Status, Verantwortlichkeiten |
| **companyRAG-Sammlungen** | Roadmap, OKRs, technische Spezifikationen, Team-Vereinbarungen, Retrospektiven-Notizen |
| **Datei-Upload** | Kapazitäts-Tabellen, Velocity-Historie, exportierte Backlog-Listen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Kapazitätsschätzung

### Schritt 1: Rohkapazität berechnen

Die Rohkapazität ist das theoretische Maximum vor allen Anpassungen.

```
ROHKAPAZITÄT = Teammitglieder × Sprint-Länge (Tage) × Stunden pro Tag
```

Verwende die regulären Arbeitsstunden des Teams — gehe NICHT von 8 Stunden/Tag produktiver Engineering-Zeit aus. Die meisten Teams arbeiten nach Meetings, Kontextwechseln und Overhead mit 5–6 produktiven Stunden/Tag.

### Schritt 2: Verfügbarkeitsanpassungen anwenden

Reduziere die Rohkapazität um bekannte Abwesenheiten:

| Anpassung | Wie anwenden |
| --- | --- |
| **Urlaub / Feiertage** | Volle Tage pro Person abziehen |
| **On-Call-Rotation** | Kapazität dieser Person um 30–50 % reduzieren (basierend auf der historischen Interrupt-Rate) |
| **Wiederkehrende Meetings** | Gesamte Meeting-Stunden über den Sprint pro Person abziehen |
| **Onboarding / Einarbeitung** | Neue Teammitglieder mit 25–50 % Kapazität in den ersten 2–4 Sprints |
| **Support-Rotation** | Den historischen Durchschnitt des Teams für Support-Arbeit abziehen |

```
ANGEPASSTE KAPAZITÄT = ROHKAPAZITÄT − (Urlaubsstunden + On-Call-Reduktion + Meetings + Support)
```

### Schritt 3: Focus Factor anwenden

Der Focus Factor berücksichtigt ungeplante Arbeit, Bugfixes, Code-Review und sonstigen Overhead, der oben nicht erfasst ist. Leite ihn aus der eigenen Historie des Teams ab:

```
FOCUS FACTOR = (tatsächlich abgeschlossene Story Points) / (angepasste Kapazität in Stunden) — gemittelt über die letzten 3–5 Sprints
```

Sind keine historischen Daten vorhanden, starte mit 0,7 (70 %) und kalibriere nach 2–3 Sprints. Schreibe niemals einen universellen Focus Factor vor — er variiert je nach Team-Reife, Codebasis-Gesundheit und Interrupt-Mustern.

```
EFFEKTIVE KAPAZITÄT = ANGEPASSTE KAPAZITÄT × FOCUS FACTOR
```

### Schritt 4: Als Story Points oder Stunden ausdrücken

Wandle die effektive Kapazität in die Schätzeinheit des Teams um. Nutzt das Team Story Points, mappe über die historische Velocity:

```
SPRINT-KAPAZITÄT (Punkte) = durchschnittliche Velocity der letzten 3–5 Sprints, angepasst an Kapazitätsunterschiede
```

Hat dieser Sprint 80 % der normalen Kapazität, plane mit etwa 80 % der durchschnittlichen Velocity. Velocity ist ein empirisches Maß, kein Ziel — blähe sie weder auf noch "strecke" sie.

## Definition des Sprint-Ziels

Ein Sprint-Ziel ist eine Ergebnisaussage, keine Liste von Tickets. Es beantwortet: "Wenn wir diesen Sprint erfolgreich abschließen, was wird dann wahr sein, das es heute noch nicht ist?"

### Checkliste zur Zielqualität

| Kriterium | Bestanden | Durchgefallen |
| --- | --- | --- |
| **Ergebnisorientiert** | "Nutzer können den Checkout ohne Seiten-Reload abschließen" | "Tickets ENG-123, ENG-124, ENG-125 fertigstellen" |
| **Einzelner Fokus** | Ein zusammenhängendes Thema oder Ziel | Mehrere unzusammenhängende Ziele gebündelt |
| **Überprüfbar** | Eine Demo oder Kennzahl kann die Erreichung belegen | Keine Möglichkeit zu erkennen, ob das Ziel erreicht ist |
| **Erreichbar** | Passt nach der Schätzung in die Sprint-Kapazität | Erfordert optimistische Annahmen über die Kapazität |
| **Für Stakeholder bedeutsam** | Auch Nicht-Entwickler verstehen den gelieferten Mehrwert | In rein technischem Jargon ausgedrückt |

### Prozess der Zielsetzung

1. Produktprioritäten prüfen: Was ist die Arbeit mit dem höchsten Impact aus dem Backlog? Beziehe dich auf die Roadmap und die aktuellen OKRs.
2. 1–2 Kandidatenziele entwerfen: Als Ergebnisse formulieren, nicht als Aufgabenlisten.
3. Umfangs-Check: Kann das Team dieses Ziel realistisch innerhalb der effektiven Kapazität erreichen? Falls nicht, grenze den Umfang ein — reduziere das Ziel, nicht die Qualität.
4. Team-Alignment: Das Team muss das Ziel verstehen und sich dazu committen. Ein ohne Team-Buy-in auferlegtes Ziel erzeugt Compliance, kein Commitment.

## Abhängigkeiten kartieren

### Abhängigkeitskategorien

| Typ | Definition | Gegenmaßnahme |
| --- | --- | --- |
| **Internes Team** | Arbeit, die von einer anderen Story im selben Sprint abhängt | Stories sequenzieren; wenn möglich im Paar zuweisen |
| **Cross-Team** | Arbeit, die durch das Deliverable eines anderen Teams blockiert ist | Liefertermin vor der Sprint-Zusage bestätigen; Puffer einplanen |
| **Extern** | Drittanbieter-API, Lieferanten-Deliverable, Kundenfreigabe | Abhängige Arbeit niemals ohne bestätigten Termin zusagen |
| **Technisch** | Gemeinsame Infrastruktur, Datenbankmigration, Deployment-Pipeline | Früh im Sprint identifizieren und einplanen |

### Protokoll zur Auflösung von Abhängigkeiten

Für jede identifizierte Abhängigkeit:

1. Nach Typ klassifizieren (siehe oben)
2. Status bestätigen: Ist die Abhängigkeit bereits aufgelöst, in Arbeit oder noch nicht begonnen?
3. Risiko bewerten: Was passiert, wenn die Abhängigkeit zu spät kommt? Gibt es alternative Arbeit, die das Team ziehen kann?
4. Verantwortlichen zuweisen: Jemand im Team ist für das Tracking jeder externen Abhängigkeit verantwortlich
5. Check-in festlegen: Wann prüfst du, ob die Abhängigkeit im Plan liegt? (Nicht am letzten Tag des Sprints)

**Regel**: Hat eine Story eine ungelöste externe Abhängigkeit ohne bestätigten Liefertermin, geht sie in den Stretch — niemals ins Commitment.

## Commitment vs. Stretch

Teile den Sprint-Backlog in zwei explizite Kategorien:

### Commitment

Arbeit, von der das Team überzeugt ist, sie innerhalb des Sprints abzuschließen. Konfidenzschwelle: Das Team glaubt, dass eine Abschlusswahrscheinlichkeit von mindestens 80–90 % bei effektiver Kapazität besteht.

- Muss in die effektive Kapazität passen
- Abhängigkeiten müssen aufgelöst sein oder bestätigte Liefertermine haben
- Akzeptanzkriterien müssen klar sein — kann das Team "fertig" nicht beschreiben, ist die Story nicht bereit fürs Commitment

### Stretch

Arbeit, die das Team zieht, wenn die Commitment-Items früh fertig werden. Stretch-Items:

- Sind vollständig groomed und startbereit (keine blockierenden Fragen)
- Haben keine ungelösten Abhängigkeiten
- Sind unabhängig — das Ziehen eines Stretch-Items destabilisiert committete Arbeit nicht
- Sind nach Priorität geordnet, damit das Team weiß, was zuerst zu ziehen ist

**Richtwert zur Kapazitätsverteilung**: Committe 80–90 % der effektiven Kapazität; fülle die restlichen 10–20 % mit geordneten Stretch-Items. Das genaue Verhältnis hängt von der historischen Genauigkeit des Teams ab — Teams, die durchgängig zu wenig committen, können das Verhältnis straffen; Teams, die zu viel committen, sollten es lockern.

## Sprint-Planungs-Workflow

### Vor der Planung (Vorbereitung)

1. Backlog groomen: Top-Kandidaten müssen klare Beschreibungen, Akzeptanzkriterien und Schätzungen haben. Ungroomte Items können nicht in den Sprint.
2. Kapazität berechnen: Führe die Schritte 1–4 aus der Kapazitätsschätzung mit den aktuellen Sprint-Daten aus.
3. Abhängigkeiten aufdecken: Identifiziere Cross-Team- und externe Abhängigkeiten der Kandidaten-Stories.
4. Vorherigen Sprint prüfen: Was wurde übertragen? Was wurde gelernt? Carry-over-Items werden vorrangig betrachtet, aber nicht automatisch übernommen — bewerte die Priorität neu.

### Während der Planung

1. Das Sprint-Ziel präsentieren (aus der Zieldefinition oben)
2. Die Kandidaten-Stories durchgehen: Für jede Scope, Schätzung, Abhängigkeiten und Akzeptanzkriterien bestätigen
3. Commitment laden: Stories ins Commitment aufnehmen, bis die effektive Kapazität erreicht ist
4. Nach Abhängigkeiten sequenzieren: Committete Stories so ordnen, dass abhängige Arbeit erst nach ihren Voraussetzungen startet
5. Stretch ergänzen: Den Stretch-Backlog in Prioritätsreihenfolge füllen
6. Team-Bestätigung: Jedes Teammitglied bestätigt, dass es seine Arbeit versteht und das Commitment für erreichbar hält

### Ausgabe des Sprint-Plans

```
SPRINT: [Name / Nummer]
DATEN:  [Start] — [Ende]
ZIEL:   [Ergebnisaussage]

KAPAZITÄT:
  Teammitglieder:      [Anzahl]
  Rohkapazität:        [Stunden oder Punkte]
  Anpassungen:         [Urlaub, On-Call usw.]
  Effektive Kapazität: [finale Zahl]
  Velocity-Referenz:   [Durchschnitt der letzten 3–5 Sprints]

COMMITMENT: [Gesamt-Punkte/Stunden] ([X] % der effektiven Kapazität)
  | # | Story | Schätzung | Verantwortlich | Abhängigkeiten | Status |
  |---|-------|-----------|----------------|----------------|--------|
  | 1 | [Titel] | [Schätzung] | [Name] | [Abh.] | Ready |

STRETCH: [Gesamt-Punkte/Stunden]
  | # | Story | Schätzung | Ziehpriorität | Abhängigkeiten |
  |---|-------|-----------|---------------|----------------|
  | 1 | [Titel] | [Schätzung] | 1 (zuerst ziehen) | [Abh.] |

ABHÄNGIGKEITEN:
  | Abhängigkeit | Typ | Verantwortlich | Erwartete Auflösung | Check-in-Datum |
  |--------------|-----|----------------|---------------------|----------------|

RISIKEN:
  [Wesentliche Risiken für die Erreichung des Sprint-Ziels — aus der Abhängigkeitsanalyse und Kapazitätsprüfung]

CARRY-OVER AUS DEM VORHERIGEN SPRINT:
  [Items, Grund für Carry-over, aktualisierte Prioritätsbewertung]
```

## Umpriorisieren mitten im Sprint

Wenn die Sprint-Gesundheit nachlässt (blockierte Items, Scope-Änderungen, unerwartete Abwesenheiten), nutze diese Triage:

1. Verbleibende Kapazität bewerten: Berechne die effektive Kapazität für die restlichen Sprint-Tage neu
2. Commitment neu bewerten: Welche committeten Items sind gefährdet? Welche liegen im Plan?
3. Das Sprint-Ziel schützen: Ist das Ziel mit einer Teilmenge der committeten Arbeit erreichbar, schiebe Nicht-Ziel-Items in den Stretch
4. Blocker eskalieren: Ungelöste Abhängigkeiten, die das Sprint-Ziel bedrohen, erfordern sofortige Eskalation — warte nicht bis zum nächsten Stand-up
5. Kommunizieren: Ändert sich das Commitment, informiere die Stakeholder — nutze den write-stakeholder-update-Skill

## Leitplanken

- Erzeuge NIEMALS Velocity-Daten, Schätzungen oder Kapazitätszahlen. Alle Team-Metriken müssen vom Nutzer, aus dem Projekt-Tracker oder aus einer companyRAG-Sammlung stammen.
- Schreibe NIEMALS universelle Focus Factors, Velocity-Ziele oder Kapazitätsverhältnisse vor. Lehre die Berechnung; das Team leitet seine eigenen Zahlen ab.
- Befülle Sprint-Pläne NIEMALS mit erfundenen Stories oder Schätzungen. Erzeuge leere Vorlagen, wenn keine Daten vorliegen.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Nutzer-/Tracker-Daten]`, `[Aus Sprint-Planungs-Framework]` oder `[KI-Vorschlag — mit dem Team verifizieren]`.

> **Tipp:** Fordere über companyFILES eine Markdown-, DOCX- oder XLSX-Ausgabe an, um einen formatierten, sofort teilbaren Sprint-Plan zu erhalten.
