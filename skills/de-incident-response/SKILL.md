---
name: de-incident-response
description: Strukturiert IT-Incidents mit Schweregrad-Klassifizierung, Eskalationspfaden, Kommunikationsvorlagen und Post-Mortem-Leitfäden. Verwende ihn, wenn ein Incident auftritt, du die Reaktion über Teams koordinierst oder ein Post-Incident-Review durchführst. Auslösen mit "Incident Response", "wir haben einen P1", "Production ist down".
---

# Incident-Response-Skill

Klassifiziere, steuere und löse IT-Incidents mit Schweregrad-Frameworks, Eskalationsmatrizen, Kommunikationsvorlagen, Timeline-Tracking und schuldfreier Post-Mortem-Moderation. Organisationsspezifische Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Incident-/On-Call-Tools über MCP** (z. B. PagerDuty, Opsgenie) | Alert-Daten, On-Call-Roster, Eskalationsketten, Incident-Status |
| **ITSM über MCP** (z. B. ServiceNow) | Ticket-Historie, Change Records, SLA-Bedingungen, Asset-Informationen |
| **Monitoring über MCP** (z. B. Datadog) | Metriken, Logs, Alert-Verläufe, betroffene Services |
| **companyRAG / Datei-Upload** | Runbooks, organisationsspezifische SLA-Vorgaben, On-Call-Roster, frühere Post-Mortems |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Schweregrad-Klassifizierungs-Framework

Klassifiziere jeden Incident vor jeder anderen Aktion gegen diese vier Stufen. Der Schweregrad bestimmt Reaktionsgeschwindigkeit, Kommunikationskadenz und Eskalationspfad.

### Schweregrad-Definitionen

| Schweregrad | Name | Impact-Kriterien | Beispielszenarien |
| --- | --- | --- | --- |
| **P1** | Kritisch | Vollständiger Service-Ausfall, der alle Nutzer betrifft, ODER bestätigte Datenpanne ODER Sicherheitsrisiko. Umsatzwirksam. SLA-Uhr läuft. | Produktionsdatenbank down, Authentifizierungsdienst nicht verfügbar, Ransomware erkannt, Ausfall der Zahlungsabwicklung |
| **P2** | Hoch | Wichtige Funktion für ein erhebliches Nutzersegment eingeschränkt. Workaround existiert evtl., ist aber nicht tragfähig. Drohende SLA-Verletzung. | Suchfunktion defekt, API-Antwortzeiten >10x normal, SSO bei einem Identity-Provider fehlerhaft, E-Mail-Zustellung >2h verzögert |
| **P3** | Moderat | Nicht-kritische Funktion beeinträchtigt. Begrenzter Nutzer-Impact. Workaround verfügbar und tragfähig. | Berichtserstellung langsam, einzelne Integration fehlerhaft, UI-Renderingproblem in einem Browser, Nicht-Produktionsumgebung down |
| **P4** | Niedrig | Kosmetisches Problem, kleinerer Bug oder informativer Alert. Kein Nutzer-Workflow blockiert. | Tippfehler in einer Fehlermeldung, Log-Rauschen von einem veralteten Endpoint, kleineres UI-Ausrichtungsproblem, Folgeaufgabe nach geplanter Wartung |

### Klassifizierungs-Entscheidungsbaum

Wende diese Fragen der Reihe nach an:

1. Ist der Service für alle Nutzer komplett nicht verfügbar? → P1
2. Gibt es eine bestätigte oder vermutete Sicherheitsverletzung? → P1
3. Ist der Umsatz gerade jetzt direkt betroffen? → P1
4. Ist eine wichtige Funktion für >25 % der Nutzer eingeschränkt? → P2
5. Steht eine SLA-Verletzung unmittelbar bevor (innerhalb der nächsten Reporting-Periode)? → P2
6. Ist eine nicht-kritische Funktion mit tragfähigem Workaround beeinträchtigt? → P3
7. Ist der Impact rein kosmetisch oder informativ? → P4

Bei Unsicherheit zwischen zwei Stufen: in den HÖHEREN Schweregrad einordnen. Herabstufen ist immer einfacher als aufzuholen, nachdem man zu niedrig eingestuft hat.

### Schweregrad-Eskalation und -Deeskalation

Der Schweregrad ist nicht statisch. Bewerte ihn bei jedem Status-Update neu:

- Eskaliere, wenn: sich der Impact auf mehr Nutzer ausbreitet, der Workaround fehlschlägt, sich das SLA-Fenster verengt, die Root Cause einen größeren Umfang offenbart
- Deeskaliere, wenn: der Workaround für alle betroffenen Nutzer bestätigt wirksam ist, der Impact eingedämmt ist und schrumpft, die Root Cause isoliert ist und ein Fix in Arbeit ist

Dokumentiere jede Schweregrad-Änderung mit Zeitstempel, Grund und der Person, die sie autorisiert hat.

---

## Incident-Rollen

Definiere diese Rollen bei der Incident-Deklaration. Eine Person pro Rolle (wobei Incident Commander und Communications Lead bei P3/P4 dieselbe Person sein können).

| Rolle | Verantwortung | Erforderlich für |
| --- | --- | --- |
| **Incident Commander (IC)** | Verantwortet den Incident-Lifecycle. Trifft Entscheidungen zu Schweregrad, Eskalation, Ressourcenzuteilung. Einziger Autoritätspunkt. | P1, P2 (empfohlen für P3) |
| **Technical Lead** | Treibt Diagnose und Lösung voran. Koordiniert die Engineering-Arbeit. Berichtet den Fortschritt an den IC. | P1, P2, P3 |
| **Communications Lead** | Verantwortet die gesamte Stakeholder-Kommunikation. Versendet Updates nach Kadenz. Verwaltet die Status-Page. | P1, P2 |
| **Scribe** | Pflegt die Incident-Timeline. Protokolliert jede Aktion, Entscheidung und jedes Finding mit Zeitstempeln. | P1, P2 (empfohlen für P3) |

Der IC muss NICHT der erfahrenste Engineer sein. Der IC muss jemand sein, der unter Druck koordinieren, delegieren und Entscheidungen treffen kann. Die technische Tiefe kommt vom Technical Lead.

---

## Eskalationsmatrix

### Reaktionszeit-Zielwerte

| Schweregrad | Acknowledge | Erstes Update | Lösungsziel | Update-Kadenz |
| --- | --- | --- | --- | --- |
| **P1** | 15 Min | 30 Min | 4 Std | Alle 30 Min |
| **P2** | 30 Min | 1 Std | 8 Std | Alle 1 Std |
| **P3** | 2 Std | 4 Std | 3 Arbeitstage | Alle 4 Std während der Geschäftszeiten |
| **P4** | 1 Arbeitstag | 2 Arbeitstage | Nächster Sprint/Zyklus | Bei Lösung |

Dies sind Startwerte. Ersetze sie durch die SLA-getriebenen Zielwerte deiner Organisation aus der companyRAG-Sammlung oder dem System-Prompt.

### Eskalations-Trigger

Eskaliere an die nächste Management-Ebene, wenn EINE dieser Bedingungen erfüllt ist:

| Trigger | Aktion |
| --- | --- |
| Lösungsziel zu 50 % verstrichen ohne identifizierte Root Cause | An das Engineering-Management eskalieren |
| Lösungsziel zu 75 % verstrichen ohne ausgerollten Fix | Auf VP-/Director-Ebene eskalieren |
| Kundenseitige SLA-Verletzung steht unmittelbar bevor | An Account Management + Engineering-Leitung eskalieren |
| Incident betrifft eine Datenpanne oder regulatorische Exposition | Unabhängig von der verstrichenen Zeit sofort an CISO/DPO + Legal eskalieren |
| IC fordert zusätzliche Ressourcen über seine Befugnis hinaus an | An die Management-Kette des IC eskalieren |
| Incident-Umfang weitet sich über mehrere Services/Teams aus | An die Platform-/Infrastructure-Leitung eskalieren |

### On-Call-Eskalationspfad

```
Primary On-Call (Team-Ebene)
  → Secondary On-Call (Team-Ebene)
    → Engineering Manager (Team)
      → Director of Engineering / VP
        → CTO (nur P1, falls nach 2 Std ungelöst)
```

Befülle dies mit dem tatsächlichen Roster deiner Organisation. Die obige Struktur ist die Standardkette. Parallele Pfade für Security (→ CISO) und Customer Impact (→ VP Customer Success) werden je nach Incident-Typ aktiviert.

---

## Kommunikationsvorlagen

### P1/P2: Erste Deklaration

```
INCIDENT DEKLARIERT — [P1/P2]

Betroffener Service: [Servicename]
Impact: [wer betroffen ist, was nicht möglich ist]
Erkannt: [Zeitstempel, wie erkannt — Alert / Kundenmeldung / intern]
Aktueller Status: Investigating
Incident Commander: [Name]
War Room: [Link zu Call/Channel]

Nächstes Update: [Zeitstempel, gemäß Kadenz]
```

### P1/P2: Status-Update

```
INCIDENT UPDATE — [P1/P2] — [Investigating / Identified / Mitigated]

Service: [Servicename]
Dauer: [Zeit seit Erkennung]
Aktueller Impact: [aktualisierter Impact-Umfang]
Was wir wissen: [nur faktische Findings — keine Spekulation]
Was wir tun: [aktuelle Aktion und wer sie verantwortet]
ETA bis zum nächsten Meilenstein: [falls bekannt, sonst "investigating"]

Nächstes Update: [Zeitstempel]
```

### P1/P2: Lösung

```
INCIDENT GELÖST — [P1/P2]

Service: [Servicename]
Gesamtdauer: [Erkennung bis Lösung]
Root Cause: [einzeilige Zusammenfassung]
Lösung: [was es behoben hat]
Erforderliche Nutzeraktion: [falls vorhanden — z. B. "Cache leeren", "neu authentifizieren"]
Daten-Impact: [bestätigt: keiner / wird untersucht / Details]

Post-Mortem geplant für: [Datum/Uhrzeit]
```

### P3/P4: Leichtgewichtige Benachrichtigung

```
INCIDENT — [P3/P4]

Service: [Servicename]
Impact: [kurze Beschreibung]
Workaround: [falls verfügbar]
Status: [Investigating / Fix in progress / Resolved]
ETA: [falls bekannt]
Verantwortlich: [Name/Team]
```

### Externe Kundenkommunikation (P1/P2)

```
Betreff: Service-Störung — [Servicename]

Wir sind uns eines Problems bewusst, das [Beschreibung des Impacts in einfacher Sprache] betrifft.

Unser Engineering-Team arbeitet aktiv an einer Lösung. Wir geben alle [Kadenz] ein Update.

Aktueller Status: [Investigating / Identified / Fix in progress]
Geschätzte Lösung: [falls bekannt, sonst "Wir arbeiten daran, dies so schnell wie möglich zu lösen."]

Wir entschuldigen uns für die Unannehmlichkeiten und halten dich auf dem Laufenden.

[Support-Kontakt oder Status-Page-Link]
```

Halte externe Kommunikation faktisch und frei von technischem Jargon. Spekuliere in externer Kommunikation niemals über die Root Cause, bevor das Post-Mortem abgeschlossen ist.

---

## Incident-Timeline-Tracking

Pflege ab dem Moment der Incident-Deklaration eine laufende Timeline. Der Scribe verantwortet dieses Dokument. Jeder Eintrag folgt diesem Format:

```
[YYYY-MM-DD HH:MM UTC] [ROLLE] — [AKTION/FINDING/ENTSCHEIDUNG]
```

### Erforderliche Timeline-Einträge

Erfasse mindestens:

| Ereignis | Wann protokollieren |
| --- | --- |
| Incident erkannt (Alert ausgelöst, Kunde gemeldet usw.) | Erster Eintrag |
| Incident deklariert und Schweregrad zugewiesen | Bei Deklaration |
| Rollen zugewiesen (IC, Tech Lead, Comms, Scribe) | Bei Deklaration |
| Jedes versendete Status-Update | Beim Versand |
| Root-Cause-Hypothese gebildet | Bei Identifikation |
| Root Cause bestätigt | Bei Bestätigung |
| Mitigation durchgeführt (Failover, Rollback, Hotfix) | Bei Ausführung |
| Schweregrad-Änderung (hoch oder runter) | Bei Änderung |
| Eskalation ausgelöst | Bei Eskalation |
| Service wiederhergestellt | Bei Bestätigung |
| Incident geschlossen | Wenn alle Follow-up-Punkte protokolliert sind |

### Timeline-Vorlage

```
## Incident: [ID] — [Titel]
Schweregrad: [P1/P2/P3/P4]
Service: [Name]
Commander: [Name]

### Timeline

[2025-01-15 14:02 UTC] ALERT — PagerDuty-Alert: API-Antwortzeit >5000ms für 3 Min
[2025-01-15 14:05 UTC] IC — Incident deklariert als P2. War Room geöffnet. Rollen zugewiesen.
[2025-01-15 14:08 UTC] TECH LEAD — Bestätigt: Datenbank-Connection-Pool auf primärer Replica erschöpft.
[2025-01-15 14:12 UTC] IC — Schweregrad auf P1 eskaliert: Impact breiter als zunächst eingeschätzt, alle API-Calls schlagen fehl.
[2025-01-15 14:15 UTC] COMMS — Erstes Status-Update versendet (intern + Status-Page).
[2025-01-15 14:22 UTC] TECH LEAD — Failover auf sekundäre Replica eingeleitet.
[2025-01-15 14:28 UTC] TECH LEAD — Sekundäre Replica bedient Traffic. API-Antwortzeiten normalisieren sich.
[2025-01-15 14:30 UTC] IC — Service wiederhergestellt. Überwachung auf Stabilität.
[2025-01-15 14:45 UTC] COMMS — Lösungs-Benachrichtigung versendet. Post-Mortem für 2025-01-16 10:00 UTC geplant.
[2025-01-15 15:00 UTC] IC — Incident geschlossen. Dauer: 58 Min (Erkennung bis Lösung).
```

---

## Schuldfreies Post-Mortem

Führe für jeden P1- und P2-Incident ein Post-Mortem durch. P3-Incidents bekommen ein Post-Mortem, wenn sie wiederkehren oder das Team eines anfordert. Das Ziel ist systemische Verbesserung, nicht individuelle Schuldzuweisung.

### Post-Mortem-Prinzipien

- Schuldfrei: Fokus auf Systeme, Prozesse und Informationsfluss — nicht auf Einzelpersonen. Menschen trafen die bestmöglichen Entscheidungen mit den damals verfügbaren Informationen.
- Gründlich: Bilde die vollständige Ursachenkette ab, nicht nur den unmittelbaren Auslöser.
- Handlungsorientiert: Jedes Finding erzeugt eine konkrete, zugewiesene, terminierte Maßnahme — oder wird ausdrücklich als akzeptiertes Risiko vermerkt.
- Zeitlich begrenzt: 60–90 Minuten für P1, 30–45 Minuten für P2. Wenn du mehr Zeit brauchst, braucht das Dokument mehr Vorarbeit.

### Post-Mortem-Dokumentvorlage

```
# Post-Mortem: [Incident-ID] — [Titel]

**Datum**: [Datum des Post-Mortem-Meetings]
**Incident-Datum**: [Datum]
**Dauer**: [Erkennung bis Lösung]
**Schweregrad**: [P1/P2/P3]
**Incident Commander**: [Name]
**Post-Mortem-Moderation**: [Name — idealerweise NICHT der IC]
**Teilnehmende**: [Namen]

## Zusammenfassung

[2–3 Sätze: was passiert ist, wer betroffen war, wie es gelöst wurde.]

## Impact

- **Betroffene Nutzer**: [Anzahl oder Prozentsatz]
- **Dauer des nutzerseitigen Impacts**: [Zeit]
- **Umsatz-Impact**: [falls messbar, sonst "nicht quantifiziert"]
- **SLA-Impact**: [etwaige SLA-Verletzungen, Gutschriftsverpflichtungen]
- **Daten-Impact**: [etwaiger Datenverlust, Korruption oder unbefugter Zugriff — bestätigt oder ausgeschlossen]

## Root Cause

[Detaillierte technische Erklärung der Root Cause. Gehe über den unmittelbaren Auslöser hinaus zu den systemischen Faktoren. Nutze die "5 Whys" oder eine Ursachenketten-Analyse.]

Why 1: [unmittelbare Ursache]
Why 2: [warum ist das passiert?]
Why 3: [warum ist das passiert?]
Why 4: [warum ist das passiert?]
Why 5: [systemische Root Cause]

## Timeline

[Aus der Incident-Timeline übernehmen, mit Hindsight-Notizen versehen, wo das Team anders handeln würde.]

## Was gut lief

- [Dinge, die funktioniert haben: schnelle Erkennung, effektive Kommunikation, gute Teamarbeit, korrektes Runbook]

## Was schlecht lief

- [Dinge, die nicht funktioniert haben: langsame Erkennung, fehlendes Runbook, unklare Eskalation, Monitoring-Lücke]

## Wo wir Glück hatten

- [Dinge, die schlimmer hätten ausgehen können: passierte während der Geschäftszeiten, die richtige Person war on-call, die sekundäre Replica war gesund]

## Maßnahmen

| ID | Maßnahme | Verantwortlich | Priorität | Fällig | Status |
|----|----------|----------------|-----------|--------|--------|
| 1 | [spezifische, messbare Maßnahme] | [Name] | [P1/P2/P3] | [Datum] | Open |
| 2 | [spezifische, messbare Maßnahme] | [Name] | [P1/P2/P3] | [Datum] | Open |

Maßnahmen MÜSSEN:
- Spezifisch sein (nicht "Monitoring verbessern" — stattdessen "Alert für Connection-Pool-Auslastung >80 % hinzufügen")
- Einem benannten Verantwortlichen zugewiesen sein
- Mit einem Fälligkeitsdatum terminiert sein
- Bis zum Abschluss im Issue-Tracker des Teams verfolgt werden
```

### Post-Mortem-Moderationsleitfaden

1. Vor dem Meeting (Moderation): Verteile die Incident-Timeline 24 Std vorher an alle Teilnehmenden. Bitte jede Person, sie zu prüfen und ihre Perspektive zu ergänzen.
2. Eröffnung (5 Min): Nenne das Schuldfreiheits-Prinzip. Erinnere alle: Wir sind hier, um das System zu verbessern, nicht um Schuld zuzuweisen.
3. Timeline-Durchgang (15–20 Min): Gehe die Ereignisse chronologisch durch. Teilnehmende ergänzen Kontext. Die Moderation hinterfragt Entscheidungspunkte und Informationslücken.
4. Root-Cause-Analyse (15–20 Min): Wende 5 Whys oder eine Ursachenkette an. Dringe über den unmittelbaren Auslöser hinaus zu den systemischen Faktoren vor.
5. Was gut lief / schlecht lief / Glück hatten (10–15 Min): Strukturierte Runde oder offene Diskussion. Die Kategorie "Glück gehabt" deckt verborgene Risiken auf.
6. Maßnahmen (10–15 Min): Für jeden "schlecht gelaufen"- und "Glück gehabt"-Punkt eine konkrete Maßnahme definieren oder das Risiko ausdrücklich akzeptieren.
7. Abschluss (5 Min): Maßnahmen durchgehen, Verantwortliche und Fälligkeitsdaten bestätigen, Follow-up-Review-Termin festlegen.

---

## Incident-Kennzahlen

Verfolge diese Kennzahlen über die Zeit, um die Reife des Incident-Managements zu messen:

| Kennzahl | Definition | Zielrichtung |
| --- | --- | --- |
| **MTTD** (Mean Time to Detect) | Zeit vom Incident-Beginn bis zur Erkennung | Sinkend |
| **MTTA** (Mean Time to Acknowledge) | Zeit von der Erkennung bis zur IC-Zuweisung | Sinkend |
| **MTTR** (Mean Time to Resolve) | Zeit von der Erkennung bis zur Service-Wiederherstellung | Sinkend |
| **MTTF** (Mean Time Between Failures) | Zeit zwischen Incidents für einen bestimmten Service | Steigend |
| **Eskalationsrate** | Anteil der Incidents, die eine Management-Eskalation erfordern | Sinkend |
| **Post-Mortem-Abschlussrate** | Anteil der P1/P2-Incidents mit abgeschlossenen Post-Mortems | 100 % |
| **Maßnahmen-Abschlussrate** | Anteil der Post-Mortem-Maßnahmen, die fristgerecht abgeschlossen werden | Steigend |
| **Wiederholungsrate** | Anteil der Incidents mit derselben Root Cause wie ein früherer Incident | Sinkend (0 % = keine wiederkehrenden Root Causes) |

---

## Leitplanken

- Diagnostiziere die Root Cause niemals allein aus der Beschreibung. Antworte mit Diagnoseschritten und Fragen, nicht mit spekulativen Root Causes. Unterscheide "bestätigte" von "vermuteten" Findings.
- Erfinde niemals SLA-Bedingungen oder On-Call-Roster. Nutze die Defaults in diesem Skill nur, wenn die Organisation keine eigenen bereitgestellt hat.
- Priorisiere während aktiver Incidents umsetzbare Anleitung statt umfassender Analyse. Ein P1 braucht nächste Schritte, keine Abhandlung.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Framework-Vorlage]`, `[Aus Incident-Daten]` oder `[KI-generierter Vorschlag — verifizieren]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um die Timeline oder das Post-Mortem als formatiertes, sofort teilbares Dokument zu erhalten.
