---
name: de-process-doc
description: Dokumentiert Geschäftsprozesse mit Schritt-für-Schritt-Workflows, RACI-Matrizen, Ausnahmebehandlung und wartbarer Struktur. Verwende ihn, wenn du einen Prozess formalisierst, jemanden in einen Workflow einarbeitest oder eine Prozessdokumentation verbesserst. Auslösen mit "dokumentiere diesen Prozess", "erstelle eine Prozess-Doku für", "RACI für".
---

# Prozess-Doku-Skill

Halte Geschäftsprozesse als Schritt-für-Schritt-Workflows fest — mit RACI-Matrizen, Ausnahmebehandlung und einer wartbaren Struktur. Alle Prozessinhalte stammen aus deiner Beschreibung, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Wissensplattform über MCP** (z. B. Confluence, SharePoint) | Bestehende Prozessbeschreibungen, Richtlinien, frühere SOPs, Rollen- und Systemreferenzen |
| **companyRAG-Sammlungen** | Interne Handbücher, Onboarding-Material, abgelegte Verfahrensdokumente |
| **Datei-Upload** | Notizen aus Prozess-Interviews, Workshop-Mitschriften, Tabellen mit Rollen und SLAs |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Prozess-Mapping

### Informationen sammeln

Erfasse vor dem Schreiben der Dokumentation die Prozessinformationen systematisch:

| Element | Frage | Warum es wichtig ist |
| --- | --- | --- |
| **Trigger** | Welches Ereignis oder welche Bedingung startet diesen Prozess? | Legt fest, wann der Prozess greift — ohne klaren Trigger wissen die Leute nicht, wann sie ihn anwenden sollen |
| **Input** | Welche Informationen, Materialien oder Voraussetzungen sind nötig? | Verhindert Prozessfehler durch fehlende Eingaben |
| **Schritte** | Was passiert, in welcher Reihenfolge? | Der Kern der Dokumentation |
| **Entscheidungspunkte** | Wo verzweigen sich die Pfade abhängig von Bedingungen? | Stellt sicher, dass das Dokument alle Szenarien abdeckt, nicht nur den Idealfall |
| **Rollen** | Wer führt welchen Schritt aus? | Schafft Verantwortlichkeit — verwende Rollenbezeichnungen, keine Personennamen |
| **Systeme** | Welche Tools oder Systeme werden in welchem Schritt genutzt? | Praktische Umsetzungshinweise |
| **Output** | Was wird produziert, wenn der Prozess abgeschlossen ist? | Definiert "fertig" — messbare Abschlusskriterien |
| **Übergaben** | Wo wechselt die Arbeit von einer Person/einem Team zur/zum nächsten? | Übergaben sind die Bruchstellen von Prozessen — dokumentiere sie explizit |
| **Ausnahmen** | Was passiert, wenn etwas schiefgeht oder vom Normalfall abweicht? | Verhindert Improvisation bei Ausnahmen |
| **SLAs/Timing** | Wie lange sollte jeder Schritt oder der Gesamtprozess dauern? | Schafft Erwartungen und ermöglicht Monitoring |

### Prozessgrenzen definieren

Lege klar fest, was IN und was AUSSERHALB des Geltungsbereichs dieses Prozessdokuments liegt:

```
PROZESSGRENZE:
  Prozessname:    [klarer, beschreibender Name]
  Zweck:          [ein Satz — was dieser Prozess erreicht]
  Trigger:        [Ereignis oder Bedingung, das/die den Prozess startet]
  Startet bei:    [erste Aktion]
  Endet bei:      [Abschlusskriterium]
  In Scope:       [was dieses Dokument abdeckt]
  Out of Scope:   [was dieses Dokument ausdrücklich NICHT abdeckt]
  Verwandte Prozesse: [vor- und nachgelagerte Prozesse mit Querverweisen]
```

## RACI-Matrix erstellen

### Methodik der Rollenzuweisung

Weise für jeden Schritt im Prozess jeder beteiligten Rolle genau eine von vier Verantwortlichkeitsstufen zu:

| Code | Rolle | Definition | Regel |
| --- | --- | --- | --- |
| **R** | Responsible (Durchführend) | Führt die Arbeit aus | Mindestens ein R pro Schritt; kann geteilt werden, wenn echt kollaborativ |
| **A** | Accountable (Rechenschaftspflichtig) | Genehmigt oder hat die letzte Entscheidung | Genau EIN A pro Schritt — niemals mehr; hier endet die Verantwortung |
| **C** | Consulted (Beratend) | Liefert Input, bevor der Schritt abgeschlossen wird | Zweiwegkommunikation — der Input wird eingeholt und berücksichtigt |
| **I** | Informed (Informiert) | Wird nach Abschluss des Schritts benachrichtigt | Einwegkommunikation — wird über das Ergebnis informiert |

### RACI-Validierungsregeln

Prüfe die Matrix nach dem Erstellen auf diese häufigen Probleme:

| Problem | Symptom | Lösung |
| --- | --- | --- |
| **Keine Verantwortlichkeit** | Ein Schritt hat kein A | Genau eine rechenschaftspflichtige Rolle zuweisen |
| **Geteilte Verantwortlichkeit** | Ein Schritt hat mehrere As | Eine wählen; die anderen zu C oder R verschieben |
| **Keine Durchführung** | Ein Schritt hat kein R | Die Rolle zuweisen, die die Arbeit erledigt |
| **Alle beratend** | Ein Schritt hat viele Cs | Auf die wesentlichen Berater reduzieren — Überberatung verlangsamt den Prozess |
| **Rollenüberlastung** | Eine Rolle hat R oder A bei den meisten Schritten | Umverteilen oder als Single-Threaded-Abhängigkeitsrisiko anerkennen |
| **Verwaiste Rollen** | Eine Rolle steht in der Matrix, hat aber bei keinem Schritt R, A, C oder I | Aus der Matrix entfernen oder ihre Beteiligung klären |

### RACI-Ausgabeformat

```
| Schritt | [Rolle 1] | [Rolle 2] | [Rolle 3] | [Rolle 4] |
|---------|-----------|-----------|-----------|-----------|
| 1. [Schrittname] | R | A | C | I |
| 2. [Schrittname] | I | R/A | | C |
| ... | | | | |
```

## Schritte dokumentieren

### Schrittstruktur

Dokumentiere jeden Schritt mit einheitlicher Struktur:

```
SCHRITT [Nummer]: [Aktionsverb + Objekt — z. B. "Eingereichte Anfrage prüfen"]
  Verantwortlich:    [Rolle aus RACI]
  Input:             [was zum Start dieses Schritts benötigt wird]
  Aktion:            [detaillierte Beschreibung — präzise genug für jemanden, der den Prozess nicht kennt]
  System:            [genutztes Tool oder System, falls zutreffend]
  Entscheidungspunkt: [falls dieser Schritt eine Wahl beinhaltet, Bedingung und Pfad für jedes Ergebnis nennen]
  Output:            [was dieser Schritt produziert]
  Übergabe:          [wer den Output erhält und wie — E-Mail, Systembenachrichtigung, manuelle Übergabe]
  SLA:               [erwartete Bearbeitungszeit, falls definiert]
  Notizen:           [Sonderfälle, Tipps, häufige Fehler]
```

### Schreibprinzipien für Prozessschritte

- Beginne jeden Schritt mit einem Aktionsverb: "Prüfen", "Einreichen", "Genehmigen", "Benachrichtigen" — nicht "Die Anfrage wird geprüft"
- Sei konkret bei Aktionen: "Auf 'Absenden' in der Freigabe-Queue klicken" — nicht "Die Anfrage absenden"
- Nenne die Bedingung vor dem Pfad: "Wenn der Betrag 10.000 € übersteigt, an den Finance Director eskalieren. Andernfalls genehmigen und zu Schritt 5 weitergehen."
- Dokumentiere den Übergabemechanismus: "Das genehmigte Dokument an [Rolle] über [Kanal] senden" — Übergaben ohne expliziten Mechanismus sind Bruchstellen
- Nenne, was NICHT zu tun ist, wenn es ein häufiger Fehler ist: "NICHT genehmigen, wenn der Budgetcode fehlt — an den Antragsteller zurückgeben (Schritt 2)"

## Ausnahmebehandlung

### Klassifizierung von Ausnahmen

| Ausnahmetyp | Definition | Dokumentationsansatz |
| --- | --- | --- |
| **Bekannte Ausnahme** | Erwartete Abweichung mit definierter Reaktion | Den Ausnahmepfad direkt beim Schritt oder in einem eigenen Ausnahmenabschnitt dokumentieren |
| **Eskalationstrigger** | Bedingung, die eine höhere Instanz oder einen anderen Prozess erfordert | Eskalationskriterien, Pfad und erwartete Reaktion definieren |
| **Fehlerbehebung** | Ein Prozessschritt scheitert (Systemfehler, falsche Eingabe etc.) | Die Wiederherstellungsschritte dokumentieren — wie man wieder auf Kurs kommt |
| **Grenzfall-Ausnahme** | Anfrage oder Situation außerhalb des Prozess-Scopes | Definieren, wie man Out-of-Scope-Fälle erkennt und wohin man sie umleitet |

### Format der Ausnahmedokumentation

Für jede bekannte Ausnahme:

```
AUSNAHME: [beschreibender Name]
  Tritt auf bei:  [welcher Schritt]
  Bedingung:      [was die Ausnahme auslöst]
  Reaktion:       [was zu tun ist — Schritt für Schritt]
  Eskalation:     [wen kontaktieren, falls die Reaktion die Ausnahme nicht löst]
  Rückkehrpunkt:  [wo der Prozess fortgesetzt wird, nachdem die Ausnahme behandelt wurde]
```

## Prozessdokument-Vorlage

Strukturiere das fertige Dokument wie folgt:

```
# [Prozessname]

## Überblick
- Zweck: [was dieser Prozess erreicht]
- Owner: [Rolle, die für den Prozess rechenschaftspflichtig ist]
- Zuletzt geprüft: [Datum]
- Prüffrequenz: [wie oft dieses Dokument auf Aktualität geprüft wird]
- Version: [Dokumentversion]

## Scope
- Trigger: [was den Prozess startet]
- In Scope: [abgedeckt]
- Out of Scope: [nicht abgedeckt]
- Verwandte Prozesse: [Links zu vor-/nachgelagerten Prozessdokumenten]

## Rollen
[Kurze Beschreibung jeder beteiligten Rolle — Rollenbezeichnung, kein Personenname]

## RACI-Matrix
[Matrix aus der RACI-Erstellung]

## Prozessschritte
[Nummerierte Schritte nach der obigen Schrittstruktur]

## Ausnahmen
[Ausnahmeeinträge nach dem obigen Ausnahmeformat]

## Definitionen
[Glossar prozessspezifischer Begriffe — nur Begriffe, die mehrdeutig oder organisationsspezifisch sind]

## Änderungshistorie
| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| [Ver] | [Datum] | [Rolle] | [was sich geändert hat] |
```

## Dokumentations-Anti-Patterns

| Anti-Pattern | Problem | Besserer Ansatz |
| --- | --- | --- |
| **Textwüste** | Unstrukturierte Prosa ist während der Ausführung schwer zu folgen | Nummerierte Schritte, Tabellen und einheitliche Formatierung nutzen |
| **Zu kleinteilig** | Jeden Mausklick zu dokumentieren macht das Dokument unbrauchbar | Auf Entscheidungs-/Aktionsebene dokumentieren, nicht auf Klickebene |
| **Zu abstrakt** | "Die Anfrage angemessen bearbeiten" gibt keine Orientierung | Konkret werden, was "angemessen" im jeweiligen Kontext bedeutet |
| **Nur der Idealfall** | Ignoriert Ausnahmen, Fehler und Grenzfälle | Die wichtigsten 3–5 Ausnahmen explizit dokumentieren |
| **Personennamen** | Bricht, wenn Personen die Rolle wechseln | Rollenbezeichnungen nutzen; eine separate Rollen-zu-Person-Zuordnung pflegen |
| **Schreiben und vergessen** | Der Prozess entwickelt sich, die Doku nicht | Prüfkadenz und Owner festlegen; das Dokument versionieren |
| **Vorausgesetztes Wissen** | "Wie du weißt ..." schließt neue Teammitglieder aus | Für jemanden schreiben, der neu in der Rolle ist; allen nötigen Kontext mitgeben |

## Leitplanken

- Erzeuge niemals Prozessschritte aus Trainingsdaten. Alle Prozessinhalte stammen aus der Beschreibung des Nutzers, wie die Arbeit tatsächlich abläuft.
- Nimm niemals Rollen, Systeme oder Schwellenwerte an. Frage den Nutzer nach Details. Verwende `[vom Process Owner zu definieren]` für Unbekanntes.
- Trage niemals SLAs, Budgetgrenzen oder Systemnamen ohne Eingabe des Nutzers ein. Wenn die Beschreibung unvollständig ist, frage nach, statt plausible Schritte zu erfinden.
- Kennzeichne generierte Inhalte: `[Aus Prozessbeschreibung]`, `[Framework-Methodik]`, `[Platzhalter — mit Process Owner definieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX-, Markdown- oder PDF-Ausgabe an, um ein formatiertes, sofort verteilbares Dokument zu erhalten. Enthält das Dokument ein Flussdiagramm, kann companyFILES Mermaid-Diagramme rendern.
