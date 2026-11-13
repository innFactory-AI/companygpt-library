---
name: de-runbook
description: Erstellt Standard Operating Procedures und betriebliche Runbooks mit Schritt-für-Schritt-Anleitungen und Eskalationspfaden. Verwende ihn, wenn du eine wiederholbare betriebliche Prozedur dokumentierst, On-Call-Leitfäden erstellst oder Team-Workflows standardisierst. Auslösen mit "Runbook erstellen für", "SOP erstellen für", "diese Prozedur dokumentieren".
---

# Runbook-Skill

Erstelle betriebliche Runbooks und SOPs mit Schritt-für-Schritt-Anleitungen, Entscheidungsbäumen, Eskalationspfaden und Prüfschritten. Alle technischen Details kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Monitoring / Alerting über MCP** (z. B. PagerDuty, Datadog, Grafana) | Alert-Definitionen, Trigger-Bedingungen, Severity-Stufen, On-Call-Rotationen |
| **Ticketing / Tracker über MCP** (z. B. Jira, ServiceNow, Notion) | Bestehende Prozeduren, Eskalationsverläufe, Verantwortlichkeiten |
| **companyRAG / Datei-Upload** | Architektur-Notizen, frühere Incident-Reports, technische Dokumentation, Konfigurationsexporte |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Runbook vs. SOP

Wähle den passenden Dokumenttyp für den Kontext:

| Attribut | Runbook | SOP |
| --- | --- | --- |
| **Zweck** | Eine spezifische betriebliche Prozedur als Reaktion auf einen Auslöser ausführen | Einen wiederkehrenden Geschäftsprozess standardisieren |
| **Zielgruppe** | Operator, der die Prozedur ausführt (oft unter Zeitdruck) | Jede Person, die den Prozess ausführt (Routineausführung) |
| **Auslöser** | Spezifisches Ereignis, Alert oder Anfrage | Wiederkehrender Zeitplan oder Geschäftsereignis |
| **Tonfall** | Direkt, imperativ, knapp — "tu dies, dann prüfe das" | Beschreibend, gründlich — "dieser Schritt sichert die Qualität, indem ..." |
| **Entscheidungsbäume** | Essenziell — mehrere Pfade je nach Beobachtung | Wenige — meist linear mit dokumentierten Ausnahmen |
| **Verifikation** | Nach jedem kritischen Schritt — "X bestätigen, bevor du fortfährst" | An Quality-Gates und Übergabepunkten |

Beide Typen folgen der gleichen strukturellen Methodik; passe Tonfall und Detailtiefe an den Dokumenttyp an.

## Runbook-Struktur

### Metadaten-Header

Jedes Runbook beginnt mit den wesentlichen Metadaten zur schnellen Orientierung:

    RUNBOOK: [Name der Prozedur]
      Version:          [Dokumentversion]
      Letzte Aktualisierung: [Datum]
      Owner:            [Rolle, die für die Pflege dieses Runbooks verantwortlich ist]
      Geprüft von:      [wer die Prozedur validiert hat]
      Prüfintervall:    [wie oft dieses Runbook erneut validiert wird]
      Auslöser:         [welches Ereignis oder welche Bedingung diese Prozedur aktiviert]
      Zielgruppe:       [wer dies ausführen soll — Rolle und erforderliches Zugriffslevel]
      Geschätzte Dauer: [typische Dauer bis zum Abschluss]
      Severity:         [falls zutreffend — Impact-Level des auslösenden Ereignisses]

### Voraussetzungen-Abschnitt

Liste alles auf, was der Operator vor dem Start benötigt — das verhindert Verzögerungen mitten in der Prozedur:

    VORAUSSETZUNGEN:
      Erforderliche Zugriffe:
        - [System/Tool] — [benötigtes Berechtigungslevel]
        - [System/Tool] — [benötigtes Berechtigungslevel]

      Benötigte Informationen:
        - [Datenpunkt] — [wo zu finden]
        - [Datenpunkt] — [wo zu finden]

      Tools/Ressourcen:
        - [Tool] — [Zweck in dieser Prozedur]

      Vorbedingungen:
        - [Bedingung, die vor dem Start zutreffen muss]

### Schritt-für-Schritt-Prozedur

Jeder Schritt folgt einer konsistenten Struktur, die auf Ausführung unter Druck optimiert ist:

    SCHRITT [Nummer]: [Aktionsverb + was]
      Aktion:          [präzise Anweisung — was tun, wo tun, wie tun]
      Erwartet:        [was du beobachten solltest, wenn der Schritt gelingt]
      Bei Abweichung:  [was tun, wenn das Ergebnis abweicht — zu Entscheidungsbaum verzweigen oder eskalieren]
      Verifizieren:    [wie bestätigen, dass der Schritt korrekt abgeschlossen wurde, bevor es weitergeht]
      Vorsicht:        [Warnungen vor häufigen Fehlern oder destruktiven Aktionen, falls zutreffend]
      Rollback:        [wie diesen Schritt rückgängig machen, falls nötig]

### Schreibprinzipien für Runbook-Schritte

- Eine Aktion pro Schritt: Enthält ein Schritt ein "und", sind es vermutlich zwei Schritte
- Imperativ: "Starte den Service neu", nicht "Der Service sollte neu gestartet werden"
- Konkrete Referenzen: "Führe [Befehl] in [Ort] aus", nicht "Führe den relevanten Befehl aus"
- Erwartete Ergebnisse für jeden Schritt: Der Operator muss wissen, wie "Erfolg" aussieht, bevor er fortfährt
- Explizite Verifikation: Verlasse dich nie auf "sollte funktionieren" — füge eine Prüfaktion hinzu
- Kein vorausgesetztes Wissen: Schreibe für ein qualifiziertes Teammitglied, das genau diese Prozedur noch nie ausgeführt hat. Beschreibe, worauf zu achten ist, nicht nur, was zu tun ist.

## Entscheidungsbäume

Für Prozeduren mit mehreren Pfaden je nach Beobachtung oder Bedingung:

### Struktur eines Entscheidungspunkts

    ENTSCHEIDUNG: [Was beobachtest oder prüfst du?]
      WENN [Bedingung A]:
        → [Aktion oder weiter zu Schritt X]
      WENN [Bedingung B]:
        → [Aktion oder weiter zu Schritt Y]
      WENN [keine der obigen / unklar]:
        → Eskaliere an [Rolle] über [Kanal] mit [bereitzustellender Information]

### Designregeln für Entscheidungsbäume

- Jeder Zweig muss in einer Lösung, einer Fortsetzung zu einem anderen Schritt oder einer Eskalation enden
- Lass nie einen offenen Zweig stehen — "wenn etwas anderes, dann finde es heraus" verfehlt den Zweck
- Nimm den "unklar / keine der obigen"-Auffangzweig auf — die Realität liefert oft Bedingungen, die nicht im Baum stehen
- Halte Entscheidungsbäume flach (maximal 2–3 Ebenen). Tiefere Bäume sollten in Unterprozeduren aufgeteilt werden.

## Eskalations-Design

### Eskalationsmatrix

Lege fest, wen du wann und wie kontaktierst:

    ESKALATIONSMATRIX:
      Stufe 1 — [Rolle/Team]:
        Wann:        [Bedingungen, die eine L1-Eskalation auslösen]
        Kontakt:     [wie erreichbar — Kanal, keine privaten Telefonnummern im Dokument]
        SLA:         [erwartete Reaktionszeit]
        Bereitstellen: [Informationen, die sie von dir benötigen]

      Stufe 2 — [Rolle/Team]:
        Wann:        [Bedingungen für L2 — typischerweise zeit- oder severitybasiert]
        Kontakt:     [Kanal]
        SLA:         [erwartete Reaktionszeit]
        Bereitstellen: [benötigte Informationen]

      Stufe 3 — [Rolle/Team]:
        Wann:        [Bedingungen für L3 — kritischer Impact oder lange Dauer]
        Kontakt:     [Kanal]
        SLA:         [erwartete Reaktionszeit]
        Bereitstellen: [benötigte Informationen]

### Leitlinien für Eskalationsauslöser

| Auslösertyp | Beschreibung | Beispiel |
| --- | --- | --- |
| **Zeitbasiert** | Prozedur überschreitet die erwartete Dauer ohne Lösung | "Wenn nicht innerhalb von 30 Minuten gelöst, an L2 eskalieren" |
| **Severitybasiert** | Impact ist größer als ursprünglich eingeschätzt | "Wenn kundenseitiger Impact bestätigt, sofort an L2 eskalieren" |
| **Kompetenzbasiert** | Operator erreicht einen Schritt, der Expertise erfordert, die er nicht hat | "Wenn Datenbank-Recovery nötig ist, an DBA-On-Call eskalieren" |
| **Befugnisbasiert** | Aktion erfordert eine Freigabe, die der Operator nicht erteilen kann | "Wenn Verlängerung des Downtime-Fensters nötig ist, an [Rolle] eskalieren" |
| **Unsicherheitsbasiert** | Operator ist sich über den richtigen Pfad unsicher | "Wenn die Symptome zu keinem Zweig des Entscheidungsbaums passen, an L1 eskalieren" |

## Kommunikationsvorlagen

Füge vorformulierte Kommunikationsvorlagen für häufige Szenarien während der Ausführung ein:

    KOMMUNIKATIONSVORLAGE — [Szenario-Name]
      Zielgruppe: [wer diese Kommunikation erhält]
      Kanal:      [wohin sie gesendet wird]
      Wann:       [an welchem Punkt der Prozedur]
      Vorlage:
        Betreff:  [Vorlage mit Platzhaltern]
        Text:     [Vorlage mit Platzhaltern — kurz, faktisch und handlungsorientiert halten]

Platzhalter verwenden [KLAMMERN] für Werte, die der Operator ausfüllt. Beispiel: "Incident begann um [ZEIT]. Impact: [BESCHREIBUNG]. Aktueller Status: [STATUS]. Nächstes Update um [ZEIT]."

## Verifikation und Test

### Validierungsprozess für Runbooks

Bevor ein Runbook als produktionsreif gilt:

1. Technisches Review: Ein Subject-Matter-Expert validiert, dass die Schritte korrekt und vollständig sind
2. Walk-Through-Test: Jemand anderes als der Autor führt die Prozedur in einer Nicht-Produktivumgebung aus (oder geht sie Schritt für Schritt durch, falls keine Testumgebung existiert)
3. Blindtest: Ein qualifiziertes Teammitglied, das NICHT am Schreiben des Runbooks beteiligt war, versucht die Ausführung allein anhand des Dokuments. Bleibt es stecken, muss das Runbook verbessert werden.
4. Edge-Case-Review: Identifiziere Szenarien, die der Hauptablauf nicht abdeckt — ergänze Entscheidungsbäume oder Eskalationspfade nach Bedarf

### Review nach der Ausführung

Nach jeder echten Ausführung des Runbooks:

    REVIEW NACH AUSFÜHRUNG:
      Datum:              [wann die Prozedur ausgeführt wurde]
      Ausgeführt von:     [Operator]
      Auslöser:           [was die Prozedur initiiert hat]
      Dauer:              [tatsächliche Dauer bis zum Abschluss]
      Befolgte Schritte:  [bestätigen, dass alle Schritte wie geschrieben ausgeführt wurden]
      Abweichungen:       [Schritte, bei denen die tatsächliche Prozedur vom Dokument abwich]
      Aufgetretene Probleme: [Probleme mit dem Runbook selbst — unklare Schritte, fehlende Informationen, falsche Reihenfolge]
      Ergebnis:           [Resultat der Prozedur]
      Notwendige Updates: [konkrete Änderungen am Runbook auf Basis dieser Ausführung]

## Runbook-Anti-Patterns

| Anti-Pattern | Problem | Besserer Ansatz |
| --- | --- | --- |
| **Textwand** | Unter Druck nicht zu befolgen | Nummerierte Schritte mit klarer Aktion/Verifikation-Struktur |
| **Vorausgesetzter Kontext** | Scheitert für alle außer dem ursprünglichen Autor | Explizite Voraussetzungen, erwartete Ergebnisse und Systemreferenzen |
| **Nur der Happy Path** | Keine Anleitung, wenn es nicht wie geplant läuft | Entscheidungsbäume und Eskalationspfade für Abweichungen |
| **Veraltete Kontakte** | Eskalation scheitert, weil sich Kontakte geändert haben | Rollen und Kanäle referenzieren, keine Einzelnamen; ein Pflegeintervall aufnehmen |
| **Keine Verifikationsschritte** | Operator fährt fort, ohne Erfolg zu bestätigen — Fehler kaskadieren | Nach jeder kritischen Aktion verifizieren |
| **Destruktive Schritte ohne Rollback** | Kein Wiederherstellungspfad, wenn die Aktion Schaden anrichtet | Rollback für jeden zustandsändernden Schritt dokumentieren |
| **Fehlende "Nicht tun"-Warnungen** | Häufige Fehler werden nicht markiert | Vorsichtshinweise dort einfügen, wo destruktive Fehler wahrscheinlich sind |

## Ausgabevorlage

    # [Runbook/SOP]: [Name der Prozedur]

    ## Metadaten
    [Header aus dem Metadaten-Abschnitt]

    ## Voraussetzungen
    [Zugriffe, Informationen, Tools und Vorbedingungen]

    ## Prozedur
    [Nummerierte Schritte mit Aktion/Erwartet/Verifizieren-Struktur]

    ## Entscheidungsbäume
    [Entscheidungspunkte mit verzweigenden Pfaden]

    ## Eskalationsmatrix
    [Gestufte Eskalation mit Auslösern, Kontakten und SLAs]

    ## Kommunikationsvorlagen
    [Vorformulierte Nachrichten für Stakeholder-Updates]

    ## Rollback-Prozedur
    [Wie die Prozedur rückgängig gemacht wird — umgekehrte Reihenfolge der kritischen Schritte]

    ## Checkliste nach der Ausführung
    [Schnelle Checkliste, die der Operator nach Abschluss durchgeht]

    ## Änderungshistorie
    | Version | Datum | Autor | Änderungen |
    |---------|-------|-------|------------|

## Leitplanken

- Erzeuge niemals Systembefehle, IPs, URLs oder Zugangsdaten aus Trainingsdaten. Alle technischen Details kommen vom Nutzer.
- Erfinde niemals Eskalationskontakte, SLA-Zeiten oder Schwellenwerte. Verwende `[vom Team zu definieren]`-Platzhalter. Wenn die Beschreibung unvollständig ist, benenne die Lücken und frage nach.
- Nimm niemals den Technologie-Stack oder die Kommunikationskanäle an. Frage den Nutzer nach Details.
- Kennzeichne erzeugte Inhalte: `[Aus Prozedurbeschreibung]`, `[Framework-Methodik]`, `[Platzhalter — mit Operations-Team definieren]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um ein formatiertes, sofort verteilbares Dokument zu erhalten.
