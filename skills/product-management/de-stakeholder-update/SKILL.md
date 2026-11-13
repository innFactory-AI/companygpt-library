---
name: de-stakeholder-update
description: Erstellt maßgeschneiderte Produkt-Status-Updates für unterschiedliche Zielgruppen und Kadenzen — Exec-Summary, Engineering-Detail, kundenorientiert. Verwende ihn beim Schreiben wöchentlicher Updates, bei der Vorbereitung eines Leadership-Reviews oder beim Kommunizieren des Launch-Status. Auslösen mit "Produkt-Update schreiben", "Status-Update für [Zielgruppe]", "wöchentliche Produktzusammenfassung".
---

# Stakeholder-Update-Skill

Schreibe Produkt-Status-Updates, die zu Zielgruppe, Kadenz und Zweck passen. Der Skill macht Updates handlungsorientiert statt zeremoniell — mit zielgruppenspezifischen Vorlagen, Tonkalibrierung und einer klaren Informationshierarchie.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Asana, Linear) | Story-Status, Sprint-Fortschritt, Blocker, Meilenstein-Tracking |
| **Analytics über MCP** (z. B. Amplitude, Mixpanel, GA) | KPI-Werte, Aktivierungs- und Nutzungskennzahlen, Trends |
| **companyRAG-Sammlungen / Datei-Upload** | Roadmaps, OKRs, Feature-Specs, vorherige Updates, Sales-Handover-Notizen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Zielgruppen-Framework

Jedes Update bedient eine bestimmte Zielgruppe. Derselbe Produktstatus ist — je nach Aufbereitung — für die Leserin nützlich oder nutzlos.

| Zielgruppe | Was sie braucht | Was sie NICHT braucht |
| --- | --- | --- |
| **Executive / C-Level** | Business-Impact, strategische Ausrichtung, nötige Entscheidungen, Risiko-Eskalation | Implementierungsdetails, einzelne Ticket-Status, technischer Jargon |
| **Engineering / Design** | Scope-Klarheit, Abhängigkeitsstatus, technische Entscheidungen, Blocker | Business-Begründung für jedes Element, übergeordnetes Strategie-Narrativ |
| **Cross-funktionale Peers** (Marketing, Sales, CS) | Timeline, Feature-Beschreibungen in Nutzersprache, Launch-Bereitschaft, Enablement-Bedarf | Technische Architektur, Sprint-Detail, interne Priorisierungsdebatten |
| **Kunden / Extern** | Gelieferter Mehrwert, was kommt (in Zeiträumen, nicht Daten), wie man Feedback gibt | Interne Roadmap, Priorisierungslogik, ungelieferte Features, Wettbewerbskontext |
| **Board / Investoren** | Traction-Kennzahlen, strategischer Fortschritt, Ressourcenallokation, Wettbewerbsposition | Operatives Detail, Sprint-Planung, einzelner Feature-Status |

## Update-Vorlagen

### Executive-Update

Kadenz: Wöchentlich oder zweiwöchentlich. Länge: maximal 5–10 Bullet Points.

Das Executive-Update beantwortet drei Fragen: Sind wir im Plan? Was musst du wissen? Was musst du entscheiden?

```
PRODUKT-UPDATE — [Zeitraum]
An: [Zielgruppe]    |    Von: [PM-Name]    |    Datum: [Datum]

📊 STATUS: [On Track / At Risk / Off Track]

HEADLINE: [Ein Satz — das Wichtigste, das man in diesem Zeitraum wissen muss]

FORTSCHRITT:
• [Erreichter Meilenstein] — Impact: [warum es in Business-Begriffen zählt]
• [Erreichter Meilenstein] — Impact: [warum es zählt]

ALS NÄCHSTES:
• [Nächster Meilenstein] — Erwartet: [Zeitrahmen]
• [Nächster Meilenstein] — Erwartet: [Zeitrahmen]

RISIKEN & BLOCKER:
• [Risiko] — Gegenmaßnahme: [was wir tun] — Entscheidung nötig: [Ja/Nein]
  [Wenn ja: konkrete Entscheidung mit Optionen und Empfehlung]

KENNZAHLEN:
• [Wichtige Kennzahl]: [aktueller Wert] → [Ziel] ([on track / hinterher / voraus])

NÖTIGE ENTSCHEIDUNGEN:
• [Beschreibung der Entscheidung] — Optionen: [A / B] — Empfehlung: [welche und warum]
  Frist für die Entscheidung: [Datum]
```

**Prinzipien des Executive-Updates**:

- Mit dem Status starten (das RAG-Signal) — schlechte Nachrichten nicht verstecken
- Business-Impact zuerst, Produktdetail danach
- Jedes Risiko braucht eine Gegenmaßnahme — nie ein Problem ohne Plan präsentieren
- Nötige Entscheidungen sind der wichtigste Abschnitt — sie treiben das Handeln an
- Wenn keine Entscheidungen nötig sind, muss das Update vielleicht gar nicht verschickt werden

### Engineering-Update

Kadenz: Wöchentlich (am Sprint-Rhythmus ausgerichtet). Länge: so viel, wie für Klarheit nötig.

```
ENGINEERING-STATUS — Sprint [Nummer] — [Daten]

SPRINT-ZIEL: [Ergebnis-Statement]
ZIEL-STATUS: [On Track / At Risk / Blocked]

IN DIESEM SPRINT ABGESCHLOSSEN:
• [Story/Feature] — [Akzeptanzkriterien erfüllt] — [Etwaiges Follow-up]
• [Story/Feature] — [Akzeptanzkriterien erfüllt]

IN ARBEIT:
• [Story/Feature] — [% fertig oder verbleibende Tage] — Verantwortlich: [Name]
  [Etwaige Blocker oder nötige Entscheidungen]

BLOCKIERT:
• [Story/Feature] — Blockiert durch: [Beschreibung] — Verantwortlich für Auflösung: [Name]
  Erwartete Auflösung: [Datum]

CARRY-OVER:
• [Story/Feature] — Grund: [warum nicht abgeschlossen] — Neue Schätzung: [Zeitrahmen]

ABHÄNGIGKEITEN:
• [Abhängigkeit] — Status: [Aufgelöst / On Track / At Risk] — Verantwortlich: [Name]

VORSCHAU NÄCHSTER SPRINT:
• [Geplanter Fokus oder Ziel für den nächsten Sprint]

TECH DEBT / WARTUNG:
• [Etwaige relevante Tech-Debt-Punkte, die adressiert oder markiert wurden]
```

### Cross-funktionales Update

Kadenz: Wöchentlich oder an Launch-Meilensteine gebunden. Länge: prägnant, handlungsorientiert.

```
PRODUKT-UPDATE FÜR [Marketing / Sales / CS] — [Zeitraum]

WAS AUSGELIEFERT WURDE:
• [Feature/Änderung] — Was es tut: [nutzerseitige Beschreibung in einfacher Sprache]
  Wen es betrifft: [Nutzersegment]
  Enablement-Bedarf: [Doku-Update / Schulung / FAQ / nichts]

WAS KOMMT:
• [Feature] — Erwartet: [Zeitraum, kein exaktes Datum]
  Early Access: [verfügbar / noch nicht]
  Enablement-Timeline: [wann Materialien bereit sind]

WAS SICH GEÄNDERT HAT:
• [Timeline-Verschiebung / Scope-Änderung / Prioritätsänderung]
  Warum: [kurze Erklärung]
  Auswirkung auf dein Team: [was anzupassen ist]

ACTION ITEMS FÜR DEIN TEAM:
• [Konkrete Bitte] — Bis: [Datum] — Verantwortlich: [Name]

KUNDENGERICHTETE MESSAGING:
• [Freigegebene Formulierungen für die Kundenkommunikation, falls zutreffend]
```

### Kundenorientiertes Update

Kadenz: Monatlich, quartalsweise oder an größere Releases gebunden. Länge: kurz, mehrwert-fokussiert.

```
PRODUKT-UPDATE — [Monat/Quartal Jahr]

WAS NEU IST:
• [Feature-Name]: [Ein-Satz-Beschreibung des Mehrwerts, den es bietet]
  So nutzt du es: [kurze Anleitung oder Doku-Link]

DEMNÄCHST:
• [Feature/Verbesserung]: [Welches Problem es löst — aus Nutzersicht beschrieben]
  Erwartet: [Dieses Quartal / Nächstes Quartal / Erstes Halbjahr]

VERBESSERUNGEN:
• [Performance-Verbesserung / Bugfix / UX-Optimierung]: [Was sich geändert hat und warum es zählt]

DEIN FEEDBACK ZÄHLT:
[Wie man Feedback gibt, Features anfragt oder an Research teilnimmt]
```

**Regeln für kundenorientierte Updates**:

- Mehrwert-orientierte Sprache: beschreibe, was Nutzer TUN können, nicht was du GEBAUT hast
- Nur Zeiträume — nie konkrete Daten ("Q3", nicht "15. August")
- Ungelieferte Features nie als zugesagt erwähnen — verwende "in Prüfung", "geplant" oder "demnächst"
- Nie interne Projektnamen, Priorisierungs-Scores oder Wettbewerbskontext offenlegen
- Nie Features besprechen, die gestrichen, depriorisiert oder gecancelt wurden — das stiftet Verwirrung

## Leitfaden zur Kadenzwahl

| Kadenz | Am besten für | Inhaltlicher Fokus |
| --- | --- | --- |
| **Täglich** (Stand-up-Notizen) | Engineering-Team im aktiven Sprint | Blocker und benötigte Hilfe — extrem knapp halten |
| **Wöchentlich** | Executive, Engineering, Cross-funktional in aktiver Entwicklung | Fortschritt, Risiken, nötige Entscheidungen |
| **Zweiwöchentlich** | Executive in stabilen Phasen | Meilenstein-Fortschritt, strategische Ausrichtung |
| **Monatlich** | Kundenorientiert, Board-Ebene | Kumulierter Fortschritt, kommende Themen |
| **Quartalsweise** | Board, Investoren, Company-All-Hands | Strategischer Fortschritt, Kennzahlentrends, Ausblick aufs nächste Quartal |

**Kadenz-Disziplin**: Verschicke ein Update nicht nur, weil der geplante Tag gekommen ist. Wenn es nichts Bedeutsames zu kommunizieren gibt, sag das in einem Satz und überspringe das volle Update. Zeremonielle Updates trainieren Leser darauf, sie zu ignorieren.

## Status-Framing

### RAG-Definitionen (Rot / Gelb / Grün)

Definiere diese einmal für deine Organisation und wende sie konsequent an:

| Status | Definition | Aktion der Leserin |
| --- | --- | --- |
| **Grün — On Track** | Lieferung nach Plan. Keine ungelösten Risiken. Kennzahlen im Zielbereich. | Keine Aktion nötig. Zur Kenntnis nehmen. |
| **Gelb — At Risk** | Ein Deliverable, eine Timeline oder eine Kennzahl ist gefährdet. Gegenmaßnahme läuft, Ausgang unsicher. | Awareness nötig. Eskalation kann folgen. |
| **Rot — Off Track** | Deliverable wird das Ziel ohne Eingreifen verfehlen. Gegenmaßnahme braucht Hilfe oder Entscheidung. | Entscheidung nötig. Eskalation aktiv. |

**Framing-Disziplin**:

- Nie Rot melden ohne Gegenmaßnahmen-Plan und konkrete Bitte
- Nie Grün melden, wenn du insgeheim Gelb für richtig hältst — Vertrauensverlust ist schlimmer als schlechte Nachrichten
- Gelb heißt nicht "ich bin unsicher" — es heißt, ein konkretes, benanntes Risiko existiert mit aktiver Gegenmaßnahme
- Der Status bezieht sich auf das ZIEL, nicht die Aktivität — "Wir haben 8 von 10 Stories geliefert" ist Aktivität; "Das Sprint-Ziel ist gefährdet, weil die Payment-Integration blockiert ist" ist Status

### Schlechte Nachrichten kommunizieren

Wenn der Status Gelb oder Rot ist:

1. Nenne die Fakten: Was passiert ist oder was gefährdet ist — ohne Beschönigung
2. Erkläre die Auswirkung: Was bedeutet das für Timeline, Kennzahl oder Deliverable?
3. Präsentiere die Gegenmaßnahme: Was wird bereits getan?
4. Stelle die Bitte: Welche Entscheidung oder Hilfe braucht es von der Leserin?
5. Gib ein nächstes Check-Datum: Wann gibst du ein Update zur Auflösung?

Verstecke schlechte Nachrichten nie in der Mitte eines Updates. Stelle sie an den Anfang oder hebe sie in einem klar markierten Abschnitt hervor.

## Leitplanken

- Erfinde NIEMALS Fortschritt, Kennzahlen, Timelines oder Status-Daten. Wenn Daten fehlen, kennzeichne das Feld als [Daten erforderlich], statt zu schätzen.
- Erzeuge NIEMALS kundengerichtete Feature-Beschreibungen ohne Informationen. Frage den Nutzer nach Feature-Details, statt sie zu erfinden.
- Vergib NIEMALS einen RAG-Status ohne Daten. Wenn der Status nicht bestimmbar ist, schreibe "Status nicht bewertbar — [angeben, welche Daten fehlen]".
- Versieh jedes Element mit einer Quellenkennzeichnung: [Aus Nutzer-/Projektdaten], [Kommunikations-Framework] oder [KI-Entwurf — vor dem Versand prüfen].

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort verteilbares Dokument zu erhalten.
