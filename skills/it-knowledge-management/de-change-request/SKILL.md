---
name: de-change-request
description: Erstellt strukturierte IT-Change-Requests mit Risikoanalyse, Rollback-Plänen und Freigabe-Routing. Verwende ihn, wenn du Infrastrukturänderungen planst, in die Produktion deployst oder Zugriffsänderungen beantragst. Auslösen mit "Change-Request erstellen für", "CR für [Änderung]", "diese Änderung einplanen".
---

# Change-Request-Skill

Erstelle IT-Change-Requests entlang von ITIL 4 Change Enablement — Klassifizierung, Risikoanalyse, Implementierungspläne, Rollback-Prozeduren, Testpläne und Kommunikationspläne. Änderungsspezifische Details kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **ITSM über MCP** (z. B. ServiceNow, Jira Service Management) | Change-Records, verknüpfte Incidents, CAB-Termine, betroffene Configuration Items |
| **Monitoring / CMDB über MCP** | Service-Abhängigkeiten, Blast-Radius, aktive Alarme, Configuration-Management-Daten |
| **companyRAG / Datei-Upload** | Runbooks, freigegebene Standard-Change-Prozeduren, Architektur- und Referenzdokumentation |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Change-Klassifizierung

Klassifiziere die Änderung, bevor du den Request schreibst. Die Klassifizierung bestimmt den Freigabepfad, die Dokumentationstiefe und die Vorlaufzeit.

### Change-Typen

| Typ | Definition | Freigabepfad | Vorlaufzeit | Dokumentationstiefe |
| --- | --- | --- | --- | --- |
| **Standard** | Vorab genehmigte, risikoarme, wiederholbare Änderung mit dokumentierter Prozedur. Wurde bereits erfolgreich durchgeführt. | Vorab genehmigt — keine CAB-Prüfung | Gemäß Prozedur-SLA | Verweis auf bestehende Prozedur |
| **Normal** | Geplante Änderung, die Bewertung und Freigabe erfordert. Kann routinemäßig sein, ist aber nicht vorab genehmigt. | CAB oder delegierter Genehmiger | Organisationsabhängig (typischerweise 5+ Arbeitstage) | Vollständiger Change-Request |
| **Emergency** | Ungeplante Änderung zur Wiederherstellung eines Service oder zur Vermeidung eines unmittelbaren Ausfalls. Kann nicht auf den normalen Freigabezyklus warten. | Emergency CAB (ECAB) oder benannte Instanz — nachträgliche vollständige Prüfung | Sofort — Freigabe während oder nach der Implementierung | Verkürzter Request, vollständiges Post-Implementation-Review |

### Klassifizierungs-Entscheidungsbaum

1. Ist dies eine Reaktion auf einen aktiven P1/P2-Incident? → Emergency
2. Existiert eine genehmigte Standard-Change-Prozedur für genau diese Änderung? → Standard
3. Ist dies eine routinemäßige, risikoarme Änderung, die mit derselben Prozedur bereits 3+ Mal erfolgreich durchgeführt wurde? → Kandidat für Standard (zur Vorab-Genehmigung einreichen)
4. Alles andere → Normal

### Kriterien für Standard-Changes

Eine Änderung qualifiziert sich nur dann als Standard, wenn ALLE der folgenden Punkte zutreffen:

- Eine dokumentierte, getestete und aktuelle Prozedur existiert
- Das Risiko ist gut verstanden und durchgängig niedrig
- Die Änderung wurde mindestens 3 Mal erfolgreich durchgeführt
- Die Rollback-Prozedur ist dokumentiert und getestet
- Der Change-Umfang hat sich seit der Genehmigung der Prozedur nicht geändert
- Die Änderung wurde vom CAB oder der Change-Authority als Standard-Change genehmigt

Wenn auch nur ein Kriterium nicht erfüllt ist, klassifiziere als Normal — unabhängig davon, wie "einfach" die Änderung erscheint.

---

## Change-Request-Vorlage

### Standard-Change-Request

```
# Standard-Change-Request

**Change-ID**: [automatisch generiert oder zugewiesen]
**Datum**: [Datum]
**Antragsteller**: [Name, Team]

## Änderungsbeschreibung
**Standard-Change-Prozedur**: [Verweis auf genehmigte Prozedur-ID/-Name]
**Was geändert wird**: [konkrete Instanz — welcher Server, Service oder welche Umgebung]
**Geplantes Zeitfenster**: [Datum und Uhrzeit]
**Geschätzte Dauer**: [Zeit]

## Vorbedingungen
- [ ] Prozedur [ID] ist aktuell (zuletzt geprüft: [Datum])
- [ ] Alle Voraussetzungen der Prozedur sind erfüllt
- [ ] Rollback-Prozedur ist bereit
- [ ] Betroffene Parteien benachrichtigt (falls von der Prozedur gefordert)

## Implementierung
Gemäß Prozedur [ID]. Keine Abweichungen.

## Verifizierung nach der Implementierung
Verifizierungsschritte gemäß Prozedur [ID].
```

### Normal-Change-Request

```
# Change-Request: [CR-Nummer]

**Datum**: [Datum]
**Antragsteller**: [Name, Team]
**Change-Typ**: Normal
**Priorität**: [Critical / High / Medium / Low]
**Zieltermin**: [gewünschtes Implementierungsdatum]

## 1. Änderungsbeschreibung

### Was geändert wird
[Präzise Beschreibung der Änderung. Konkret genug, dass auch jemand ohne Kontext versteht, was nach der Änderung anders ist.]

### Warum diese Änderung nötig ist
[Geschäftliche oder technische Begründung. Welches Problem löst sie? Was passiert, wenn wir die Änderung nicht durchführen?]

### Umfang
- **In Scope**: [was diese Änderung abdeckt]
- **Out of Scope**: [was diese Änderung NICHT abdeckt]
- **Betroffene Systeme**: [Liste von Systemen, Services oder Komponenten]
- **Umgebungen**: [Produktion, Staging usw.]
- **Betroffene Nutzer**: [wer diese Änderung wie bemerkt]

## 2. Risikobewertung

### Risikoklassifizierung

Bewerte jede Risikodimension:

| Dimension | Bewertung (H/M/L) | Begründung |
|-----------|-------------------|------------|
| **Service-Impact** | [H/M/L] | [Was bricht, wenn etwas schiefgeht?] |
| **Nutzer-Impact** | [H/M/L] | [Wie viele Nutzer sind betroffen? Gibt es einen Workaround?] |
| **Komplexität** | [H/M/L] | [Wie viele Komponenten, Abhängigkeiten oder manuelle Schritte?] |
| **Reversibilität** | [H/M/L] | [Wie leicht lässt sich das zurückrollen? Risiko von Datenverlust?] |
| **Change-Fenster** | [H/M/L] | [Ist das Fenster ausreichend? Was passiert bei Überschreitung?] |
| **Abhängigkeitsrisiko** | [H/M/L] | [Hängt dies von anderen Changes, Teams oder Anbietern ab?] |

### Gesamt-Risikowert

| Bewertungen | Gesamtrisiko | Freigabe-Ebene |
|-------------|--------------|----------------|
| Alle Low | Low | Team Lead + Change Manager |
| Mindestens ein Medium, kein High | Medium | CAB-Prüfung |
| Mindestens ein High | High | CAB-Prüfung + Senior Management |
| Mehrere High oder kritischer Service | Critical | CAB-Prüfung + VP/CTO-Freigabe |

### Identifizierte Risiken

| # | Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|--------|-----------------------------|------------|---------------|
| 1 | [was schiefgehen könnte] | [H/M/L] | [H/M/L] | [wie verhindern oder reduzieren] |
| 2 | [was schiefgehen könnte] | [H/M/L] | [H/M/L] | [wie verhindern oder reduzieren] |

## 3. Implementierungsplan

### Checkliste vor der Implementierung
- [ ] [Voraussetzung 1: z. B. Backup abgeschlossen und verifiziert]
- [ ] [Voraussetzung 2: z. B. Monitoring-Dashboards geöffnet]
- [ ] [Voraussetzung 3: z. B. Rollback-Prozedur vom Implementierenden geprüft]
- [ ] [Voraussetzung 4: z. B. Kommunikation an betroffene Parteien versendet]

### Implementierungsschritte

| Schritt | Aktion | Verantwortlich | Geschätzte Zeit | Verifizierung |
|---------|--------|----------------|-----------------|---------------|
| 1 | [konkrete Aktion] | [wer] | [Zeit] | [wie Erfolg verifiziert wird] |
| 2 | [konkrete Aktion] | [wer] | [Zeit] | [wie Erfolg verifiziert wird] |
| 3 | [konkrete Aktion] | [wer] | [Zeit] | [wie Erfolg verifiziert wird] |

### Change-Fenster
- **Start**: [Datum, Uhrzeit, Zeitzone]
- **Ende**: [Datum, Uhrzeit, Zeitzone]
- **Wartungsfenster erforderlich**: [Ja/Nein — erleben Nutzer eine Downtime?]
- **Ausweichfenster**: [Datum, Uhrzeit — falls das primäre Fenster verpasst wird]

## 4. Testplan

### Tests vor der Änderung
[Welche Tests wurden vor dem Antrag durchgeführt? Testumgebung, Testfälle, Ergebnisse.]

| Test | Umgebung | Ergebnis | Datum |
|------|----------|----------|-------|
| [Testbeschreibung] | [Umgebung] | [Pass/Fail] | [Datum] |

### Verifizierung nach der Änderung
[Wie der Erfolg der Änderung in der Produktion verifiziert wird.]

| Verifizierung | Erwartetes Ergebnis | Tatsächliches Ergebnis |
|---------------|---------------------|------------------------|
| [Prüfung] | [wie Erfolg aussieht] | [während der Implementierung ausgefüllt] |

### Smoke-Test-Prozedur
[Minimaler Satz an Prüfungen, um die Grundfunktionalität unmittelbar nach der Änderung zu bestätigen.]

1. [Prüfung 1 — Verifizierung des kritischen Pfades]
2. [Prüfung 2 — Verifizierung des Integrationspunkts]
3. [Prüfung 3 — Verifizierung der nutzerseitigen Funktionalität]

## 5. Rollback-Plan

### Entscheidungskriterien für Rollback
Leite einen Rollback ein, wenn EINE der folgenden Bedingungen erfüllt ist:
- [Kriterium 1: z. B. Verifizierung nach der Änderung schlägt bei einer kritischen Prüfung fehl]
- [Kriterium 2: z. B. Fehlerrate übersteigt X % innerhalb von 30 Minuten]
- [Kriterium 3: z. B. Change-Fenster wird um mehr als 30 Minuten überschritten]

### Rollback-Prozedur

| Schritt | Aktion | Verantwortlich | Geschätzte Zeit |
|---------|--------|----------------|-----------------|
| 1 | [Rollback-Aktion] | [wer] | [Zeit] |
| 2 | [Rollback-Aktion] | [wer] | [Zeit] |
| 3 | [erfolgreichen Rollback verifizieren] | [wer] | [Zeit] |

### Rollback-Einschränkungen
[Szenarien, in denen ein Rollback nicht möglich oder nur teilweise möglich ist. Was passiert mit Daten, die zwischen Deployment und Rollback entstehen? Gibt es irreversible Schritte?]

**Geschätzte Gesamt-Rollback-Zeit**: [Zeit]
**Datenauswirkung des Rollbacks**: [keine / Risiko von Datenverlust beschrieben / manueller Eingriff nötig]

## 6. Kommunikationsplan

### Kommunikation vor der Änderung

| Zielgruppe | Kanal | Zeitpunkt | Nachricht |
|------------|-------|-----------|-----------|
| [betroffene Nutzer] | [E-Mail/Slack/Teams] | [X Tage vorher] | [Ankündigung der geplanten Wartung] |
| [Support-Team] | [Kanal] | [X Tage vorher] | [Impact-Briefing, erwartete Tickets] |
| [Management] | [Kanal] | [bei Freigabe] | [Change-Zusammenfassung, Risiko, Zeitplan] |

### Kommunikation während der Änderung

| Ereignis | Zielgruppe | Kanal | Nachricht |
|----------|------------|-------|-----------|
| Change gestartet | [wer] | [wo] | [Change in Arbeit, ETA] |
| Change abgeschlossen | [wer] | [wo] | [Change fertig, Verifizierung läuft] |
| Probleme erkannt | [wer] | [wo] | [Problembeschreibung, in Untersuchung] |
| Rollback eingeleitet | [wer] | [wo] | [Rollback in Arbeit, ETA] |

### Kommunikation nach der Änderung

| Zielgruppe | Kanal | Zeitpunkt | Nachricht |
|------------|-------|-----------|-----------|
| [betroffene Nutzer] | [Kanal] | [innerhalb 1 Std. nach Abschluss] | [Change fertig, ggf. erforderliche Aktion] |
| [Management] | [Kanal] | [innerhalb 1 Std. nach Abschluss] | [Zusammenfassung des Change-Ergebnisses] |

## 7. Freigabe

| Genehmiger-Rolle | Name | Entscheidung | Datum |
|------------------|------|--------------|-------|
| Change Manager | [Name] | [Genehmigt / Abgelehnt / Zurückgestellt] | [Datum] |
| CAB (falls erforderlich) | [Mitglieder] | [Genehmigt / Abgelehnt / Zurückgestellt] | [Datum] |
| Senior Management (falls erforderlich) | [Name] | [Genehmigt / Abgelehnt / Zurückgestellt] | [Datum] |

**Freigabebedingungen**: [an die Freigabe geknüpfte Bedingungen]
```

### Emergency-Change-Request

```
# Emergency-Change-Request: [ECR-Nummer]

**Datum**: [Datum, Uhrzeit]
**Antragsteller**: [Name, Team]
**Verknüpfter Incident**: [Incident-ID — Link zum aktiven Incident]
**Freigegeben von**: [ECAB-Mitglied oder benannte Instanz]

## Was
[Ein Absatz: was geändert wird und warum es nicht auf den normalen Prozess warten kann.]

## Risiko
[Kurze Risikobewertung — was bei dieser Änderung schiefgehen könnte. Emergency bedeutet nicht unbewertet.]

## Implementierung
[Schritte, in Reihenfolge. Knapp, aber vollständig.]

## Rollback
[Wie man rückgängig macht, falls die Änderung die Lage verschlechtert.]

## Nach der Implementierung
- [ ] Nachträglicher Change-Request innerhalb von [24/48 Std.] für die vollständige CAB-Prüfung eingereicht
- [ ] Post-Implementation-Review abgeschlossen
- [ ] Incident-Post-Mortem berücksichtigt den Emergency-Change
```

---

## Risikobewertung im Detail

### Analyse der Service-Abhängigkeiten

Bevor du das Risiko bewertest, kartiere den Blast-Radius der Änderung:

1. Direkte Abhängigkeiten: Systeme, die die geänderte Komponente direkt konsumieren oder von ihr konsumiert werden
2. Indirekte Abhängigkeiten: Systeme, die einen Schritt entfernt sind — sie hängen von einem System ab, das von der geänderten Komponente abhängt
3. Geteilte Infrastruktur: Load Balancer, DNS, Authentifizierungsdienste, Datenbanken, die die geänderte Komponente mit anderen Services teilt

Eine "einfache" Änderung an einem geteilten Authentifizierungsdienst hat einen viel größeren Blast-Radius als eine Änderung an einem isolierten Microservice. Die Risikoklassifizierung muss dies widerspiegeln.

### Erkennung von Change-Konflikten

Prüfe auf Konflikte mit:

- Anderen Changes, die im selben Fenster geplant sind
- Laufenden Incidents, die dieselben Systeme betreffen
- Freeze-Phasen (Code Freezes, Release-Moratorien, regulatorische Audit-Fenster)
- Wichtigen Geschäftsereignissen (Quartalsende, Produkt-Launches, Spitzenlast-Zeiträume)

---

## Post-Implementation-Review

Jede Änderung (auch Standard-Changes) sollte eine schlanke Prüfung nach der Implementierung erhalten. Normal- und Emergency-Changes erfordern ein dokumentiertes Review.

### Review-Checkliste

- Alle Verifizierungen nach der Änderung bestanden
- Keine unerwarteten Alarme innerhalb des Monitoring-Zeitraums ausgelöst
- Kein Anstieg von Fehlerraten oder Support-Tickets
- Change in der Configuration Management Database (CMDB) oder Äquivalent dokumentiert
- Zugehörige Dokumentation aktualisiert (Runbooks, Architektur-Dokumente, Referenzdokumentation)
- Lessons Learned festgehalten (bei nicht-trivialen Changes)

### Zu verfolgende Kennzahlen

| Kennzahl | Definition | Zweck |
| --- | --- | --- |
| **Change Success Rate** | Anteil der Changes, die ohne Rollback oder Incident umgesetzt wurden | Misst die Change-Qualität |
| **Change Lead Time** | Zeit von der Antragstellung bis zur Implementierung | Misst die Prozesseffizienz |
| **Emergency Change Ratio** | Anteil der als Emergency klassifizierten Changes | Hoher Anteil deutet auf Prozesslücken oder chronische Unterinvestition hin |
| **Failed Change Rate** | Anteil der Changes, die einen Rollback erforderten | Identifiziert systemische Implementierungsprobleme |
| **Change-bezogene Incidents** | Incidents, die innerhalb von 48 Std. nach der Implementierung durch Changes verursacht wurden | Misst die Wirksamkeit des Change-Risikomanagements |

---

## Leitplanken

- Erzeuge niemals systemspezifische Implementierungsschritte aus Trainingsdaten. Alle technischen Details kommen vom Nutzer oder aus referenzierten Runbooks. Wenn kritische Schritte fehlen, frage nach.
- Erfinde niemals Rollback-Prozeduren. Kennzeichne fehlende Rollback-Pläne als `[ROLLBACK-PLAN ERFORDERLICH]`, anstatt plausibel klingende Schritte zu generieren.
- Erfinde niemals Freigabe-Routing, CAB-Mitgliedschaften oder Change-Fenster. Diese sind organisationsspezifisch. Kennzeichne unvollständige Abschnitte explizit als Blocker.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Änderungsbeschreibung]`, `[Change-Request-Vorlage]` oder `[KI-strukturiert — mit Change-Authority verifizieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Change-Request zu erhalten.
