---
name: de-it-docs
description: Schreibt technische Dokumentation, Runbooks, Architecture Decision Records und Prozessleitfäden aus informellen Beschreibungen. Verwende ihn, wenn du ein neues System dokumentierst, Runbooks für den Betrieb erstellst oder implizites Wissen in strukturierte Dokumente überführst. Auslösen mit "Doku schreiben für", "Runbook erstellen", "diesen Prozess dokumentieren".
---

# IT-Doku-Skill

Verwandle informelle Beschreibungen, Meeting-Notizen oder implizites Team-Wissen in saubere technische Dokumentation — Runbooks, ADRs, Prozessleitfäden und Referenzdokumente. Der Skill ordnet deine Eingabe dem richtigen Dokumenttyp zu und wendet die passende Vorlage an. Die technischen Inhalte kommen von dir oder aus deinen angebundenen Quellen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Dokumentation & Wiki über MCP** (z. B. Confluence, SharePoint) | Bestehende Seiten, frühere Runbooks, Umgebungsnotizen, Prozessbeschreibungen |
| **Code & Infrastruktur über MCP** (z. B. GitHub) | Repository-Details, Konfigurationsdateien, Deployment-Definitionen, READMEs |
| **companyRAG / Datei-Upload** | Meeting-Notizen, Incident-Berichte, Architektur-Skizzen, implizites Wissen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Dokumenttyp-Router

Klassifiziere die Doku-Anfrage, bevor du schreibst. Der Dokumenttyp bestimmt Struktur, Zielgruppe und Detailtiefe.

| Typ | Zweck | Zielgruppe | Wann verwenden |
| --- | --- | --- | --- |
| **Runbook** | Schritt-für-Schritt-Betriebsanleitungen zum Ausführen einer Aufgabe oder zum Reagieren auf ein Szenario | On-Call-Engineers, SREs, Betriebspersonal | Deployen, Neustarten, Failover, Skalieren, Wiederherstellen oder Diagnostizieren eines konkreten Systems |
| **ADR** | Festhalten einer Architektur- oder Technologieentscheidung mit Kontext und Begründung | Engineering-Team, künftige Maintainer | Auswahl einer Technologie, Architekturänderung, Einführung eines Patterns, Abkündigung einer Komponente |
| **Prozessleitfaden** | Dokumentierter Workflow für einen wiederkehrenden Geschäfts- oder IT-Prozess | IT-Personal, bereichsübergreifende Teams | Onboarding, Offboarding, Zugriffsvergabe, Change-Management, Incident-Management |
| **Referenzdokument** | Faktische Beschreibung eines Systems, Dienstes oder einer Umgebung | Alle, die das System verstehen müssen | Architekturüberblick, Netzwerk-Topologie, Service-Catalog-Eintrag, Umgebungskonfiguration |

Wenn die Anfrage zu mehreren Typen passt, frage den Nutzer, welchen Typ er braucht, oder empfiehl einen anhand des Kontexts. Ein "Dokument zum Deployment" kann ein Runbook sein (wie man deployt), ein ADR (warum wir diese Deployment-Strategie gewählt haben) oder ein Referenzdokument (wie die Deployment-Pipeline funktioniert).

---

## Runbook-Vorlage

Runbooks sind für die Ausführung unter Stress gedacht. Sie müssen von jemandem nutzbar sein, der dieses System nie angefasst hat — um 3 Uhr nachts, mit einem auslösenden Alert.

```
# Runbook: [Aktion] [System/Dienst]

**Owner**: [Team]
**Zuletzt getestet**: [Datum — Runbooks müssen regelmäßig getestet werden]
**Zuletzt aktualisiert**: [Datum]
**Geschätzte Dauer**: [wie lange diese Prozedur unter Normalbedingungen dauert]

## Zweck
[Ein Satz: wann und warum du diese Prozedur ausführst.]

## Voraussetzungen
- [ ] Zugriff auf [System/Umgebung] mit [Rolle/Berechtigungen]
- [ ] [Tool] installiert und konfiguriert (Version [X]+)
- [ ] [Credential/Token] verfügbar aus [Ort]

## Pre-Flight-Checks
[Verifizierungsschritte VOR der Ausführung. Fange Falsche-Umgebung-Fehler hier ab.]

1. Prüfe, ob du mit [korrekter Umgebung] verbunden bist: `[Befehl zur Prüfung]`
2. Bestätige den aktuellen Zustand: `[Befehl zur Prüfung]`
   Erwartete Ausgabe: [was du sehen solltest]
3. [Weitere Verifizierung]

## Prozedur

### Schritt 1: [Verb] [Objekt]
    [exakter Befehl oder exakte Aktion]
**Erwartete Ausgabe**: [was du sehen solltest]
**Wenn das fehlschlägt**: [was prüfen, was tun]

### Schritt 2: [Verb] [Objekt]
    [exakter Befehl oder exakte Aktion]
**Erwartete Ausgabe**: [was du sehen solltest]
**Wenn das fehlschlägt**: [was prüfen, was tun]

### Schritt 3: [Verb] [Objekt]
    [exakter Befehl oder exakte Aktion]
**Erwartete Ausgabe**: [was du sehen solltest]
**Wenn das fehlschlägt**: [was prüfen, was tun]

## Verifizierung
[Wie du bestätigst, dass die Prozedur erfolgreich war.]

1. [Prüf-Befehl oder URL]
   Erwartet: [konkretes Ergebnis]
2. [X Minuten beobachten]
   Erwartet: [stabile Metriken]

## Rollback
[Wie du diese Prozedur rückgängig machst, falls etwas schiefläuft.]

1. [Rollback-Schritt]
2. [Rollback-Schritt]
3. [Erfolgreichen Rollback verifizieren]

## Troubleshooting

| Symptom | Wahrscheinliche Ursache | Lösung |
|---------|-------------------------|--------|
| [was du siehst] | [warum] | [was tun] |
| [was du siehst] | [warum] | [was tun] |

## Eskalation
Wenn die Prozedur fehlschlägt und das Troubleshooting nicht hilft:
- **Während der Geschäftszeiten**: Kontaktiere [Team/Person] über [Kanal]
- **Außerhalb der Geschäftszeiten**: Alarmiere [On-Call-Rotation] über [Tool]
```

### Regeln für das Schreiben von Runbooks

- Befehle müssen kopierbar sein. Keine Platzhalter, die unter Druck interpretiert werden müssen. Verwende <VARIABLEN_NAME> für variable Werte und liste sie in den Voraussetzungen samt Fundort auf.
- Jeder Schritt hat einen Fehlerpfad. "Wenn das fehlschlägt" ist für jeden Schritt Pflicht. Ein On-Call-Engineer, der um 3 Uhr nachts auf einen unerwarteten Fehler trifft, braucht den nächsten Schritt, keine leere Wand.
- Erwartete Ausgabe angeben. Ohne erwartete Ausgabe weiß die ausführende Person nicht, ob der Schritt funktioniert hat.
- Teste das Runbook. Ein ungetestetes Runbook ist Fiktion. Füge ein "Zuletzt getestet"-Datum hinzu und mach das Testen zum Teil des Review-Zyklus.
- Zeitschätzungen sind ehrlich. Wenn es 45 Minuten dauert, schreib nicht 15. Genaue Zeitschätzungen helfen Incident Commandern bei der Planung.

---

## Architecture Decision Record (ADR)-Vorlage

ADRs halten das WARUM hinter Entscheidungen fest, damit künftige Engineers den Kontext verstehen, nicht nur das Ergebnis.

```
# ADR-[Nummer]: [Titel der Entscheidung]

**Datum**: [Datum der Entscheidung]
**Status**: [Vorgeschlagen / Angenommen / Abgekündigt / Ersetzt durch ADR-XXX]
**Entscheider**: [wer diese Entscheidung getroffen oder freigegeben hat]

## Kontext
[Welche Situation oder welches Problem hat diese Entscheidung ausgelöst? Welche
Rahmenbedingungen gibt es? Beschreibe den technischen und geschäftlichen Kontext.
Ein Leser in 2 Jahren sollte verstehen, warum diese Entscheidung getroffen wurde.]

## Entscheidungstreiber
- [Treiber 1: z. B. "Muss innerhalb von 6 Monaten den 10-fachen Durchsatz unterstützen"]
- [Treiber 2: z. B. "Team hat keine Erfahrung mit Technologie X"]
- [Treiber 3: z. B. "Budget-Grenze von EUR X/Monat für Infrastruktur"]

## Betrachtete Optionen

### Option A: [Name]
[Beschreibung des Ansatzes.]
- **Pro**: [Vorteile]
- **Contra**: [Nachteile]
- **Geschätzter Aufwand**: [Zeit/Kosten]

### Option B: [Name]
[Beschreibung des Ansatzes.]
- **Pro**: [Vorteile]
- **Contra**: [Nachteile]
- **Geschätzter Aufwand**: [Zeit/Kosten]

### Option C: [Name]
[Beschreibung des Ansatzes.]
- **Pro**: [Vorteile]
- **Contra**: [Nachteile]
- **Geschätzter Aufwand**: [Zeit/Kosten]

## Entscheidung
[Welche Option gewählt wurde und eine knappe Begründung, warum.]

## Konsequenzen
- **Positiv**: [erwartete Vorteile]
- **Negativ**: [akzeptierte Trade-offs und Risiken]
- **Neutral**: [Implikationen, die weder positiv noch negativ sind]

## Folgeaktionen
- [ ] [Konkrete Aktion zur Umsetzung der Entscheidung]
- [ ] [Konkrete Aktion zur Minderung bekannter Risiken]

## Referenzen
- [Links zu relevanten Dokumenten, RFCs oder früheren ADRs]
```

### Regeln für das Schreiben von ADRs

- Der Kontext ist der wichtigste Abschnitt. Die Entscheidung selbst ist im Nachhinein oft offensichtlich. Nicht offensichtlich ist das WARUM — die Rahmenbedingungen, der Druck und die Trade-offs, die damals galten.
- Verworfene Optionen aufnehmen. Künftige Engineers werden fragen "Warum haben wir nicht einfach X genommen?" Das ADR sollte das vorab beantworten.
- ADRs unveränderlich halten. Bearbeite kein angenommenes ADR. Ändert sich die Entscheidung, schreibe ein neues ADR, das es ersetzt, und aktualisiere den Status des alten.
- Fortlaufend nummerieren. ADR-001, ADR-002 usw. So entsteht ein Entscheidungs-Log, das chronologisch durchblätterbar ist.

---

## Prozessleitfaden-Vorlage

Prozessleitfäden dokumentieren wiederkehrende Workflows, die Team- oder Systemgrenzen überschreiten.

```
# Prozess: [Prozessname]

**Owner**: [Team/Rolle, die für diesen Prozess verantwortlich ist]
**Zuletzt geprüft**: [Datum]
**Review-Zyklus**: [quartalsweise / halbjährlich / jährlich]

## Zweck
[Was dieser Prozess erreicht und wann er ausgelöst wird.]

## Geltungsbereich
- **Im Geltungsbereich**: [was dieser Prozess abdeckt]
- **Außerhalb**: [was dieser Prozess NICHT abdeckt — auf andere Prozesse verlinken]

## Rollen

| Rolle | Verantwortlichkeit |
|-------|--------------------|
| [Anfragender] | [was er tut] |
| [Genehmiger] | [was er tut] |
| [Ausführender] | [was er tut] |

## Eingaben
- [Was den Prozess auslöst: Anfrageformular, Ticket, Event, geplantes Datum]
- [Benötigte Informationen oder Artefakte]

## Workflow

### 1. [Phasenname]
**Wer**: [Rolle]
**Aktion**: [was er tut]
**Output**: [was diese Phase produziert]
**SLA**: [Zeiterwartung, falls vorhanden]

### 2. [Phasenname]
**Wer**: [Rolle]
**Aktion**: [was er tut]
**Output**: [was diese Phase produziert]
**SLA**: [Zeiterwartung, falls vorhanden]

### 3. [Phasenname]
**Wer**: [Rolle]
**Aktion**: [was er tut]
**Output**: [was diese Phase produziert]
**SLA**: [Zeiterwartung, falls vorhanden]

## Ausnahmebehandlung
[Was passiert, wenn der Prozess auf einen Sonderfall trifft oder an einem Schritt fehlschlägt.]

| Ausnahme | Aktion | Eskalation |
|----------|--------|------------|
| [Szenario] | [was tun] | [wen kontaktieren] |

## Metriken
| Metrik | Definition | Ziel |
|--------|------------|------|
| [z. B. Durchlaufzeit] | [Ende-zu-Ende-Zeit von Auslösung bis Abschluss] | [Ziel] |

## Audit-Trail
[Welche Aufzeichnungen wo und wie lange aufbewahrt werden.]
```

---

## Referenzdokument-Vorlage

Referenzdokumente beschreiben, was existiert. Sie sind die "Ist-Zustand"-Dokumentation, die jeder braucht, aber niemand schreibt.

```
# [System/Dienst/Komponente] — Referenz

**Owner**: [Team]
**Zuletzt aktualisiert**: [Datum]

## Überblick
[2–3 Sätze: was dieses System tut, wer es nutzt, warum es existiert.]

## Architektur

[Beschreibung der Komponenten und ihrer Beziehungen auf hoher Ebene. Verweise auf
ein Diagramm, falls vorhanden, aber erzeuge keine ASCII-Art, die veraltet.]

### Komponenten

| Komponente | Zweck | Technologie | Owner |
|------------|-------|-------------|-------|
| [Name] | [was sie tut] | [Stack] | [Team] |

### Abhängigkeiten

| Abhängigkeit | Typ | Auswirkung bei Ausfall |
|--------------|-----|------------------------|
| [Dienst/System] | [hart / weich] | [was bricht] |

## Konfiguration

| Parameter | Wert | Ort | Hinweise |
|-----------|------|-----|----------|
| [Name] | [aktueller Wert oder Referenz] | [wo konfiguriert] | [Einschränkungen] |

## Zugriff

| Rolle | Zugriffsebene | Wie anfordern |
|-------|---------------|---------------|
| [Rolle] | [lesen / schreiben / admin] | [Prozess oder Link] |

## Monitoring

| Alert | Bedingung | Reaktion |
|-------|-----------|----------|
| [Alert-Name] | [Auslösebedingung] | [Runbook-Link oder Aktion] |

## Verwandte Dokumente
- [Runbook: Link]
- [ADR: Link]
- [Prozessleitfaden: Link]
```

---

## Schreibrichtlinien für IT-Dokumentation

### Prinzipien

1. Schreibe für den Worst Case. Dokumentation ist am wertvollsten, wenn etwas kaputt ist und Menschen unter Stress stehen. Geh davon aus, dass die lesende Person unter Zeitdruck steht, das System nicht kennt und eindeutige Anweisungen braucht.
2. Befehle statt Beschreibungen. "Führe `kubectl get pods -n production` aus" ist besser als "Prüfe die Pods im Production-Namespace." Operatoren kopieren und fügen ein; sie interpretieren keine Prosa zu Befehlen.
3. Nur der Ist-Zustand. Dokumentiere, was heute existiert, nicht was nach einer geplanten Migration existieren wird. Aktualisiere die Doku, wenn die Migration abgeschlossen ist, nicht vorher.
4. Eine Single Source of Truth. Dupliziere niemals Inhalte über Dokumente hinweg. Verlinke auf die kanonische Quelle. Duplizierte Dokumentation driftet innerhalb von Wochen auseinander.
5. Testbar. Wenn jemand der Doku folgt und ein anderes Ergebnis erhält als beschrieben, ist die Doku falsch. Füge Verifizierungsschritte ein, damit die lesende Person bestätigen kann, auf dem richtigen Weg zu sein.

### Formatierungsstandards

- Überschriften: Halte die Überschriftenhierarchie strikt ein (H1 für den Titel, H2 für Hauptabschnitte, H3 für Unterabschnitte). Überspringe nie Ebenen.
- Befehle: Immer in Code-Blöcken mit angegebener Shell-Sprache. Gib den vollständigen Befehl an — kein "usw." oder "wie oben."
- Variablen: Verwende <SPITZE_KLAMMERN_GROSS> für Werte, die die lesende Person ersetzen muss. Liste alle Variablen im Abschnitt Voraussetzungen auf.
- Tabellen: Für strukturierte Daten (Konfigurationen, Rollen, Alerts). Nicht für Prosa.
- Links: Relative Links auf andere interne Dokumente. Absolute URLs für externe Referenzen.

---

## Leitplanken

- Erzeuge niemals systemspezifische Befehle, Konfigurationen oder Architektur aus Trainingsdaten. Wenn kritische Details fehlen, frage nach. Verwende [EINGABE ERFORDERLICH: ...]-Platzhalter statt plausibel klingender Annahmen.
- Erfinde niemals Monitoring-Schwellen, SLA-Werte oder Eskalationskontakte. Diese sind organisationsspezifisch — verwende [NOCH ZU DEFINIEREN]-Platzhalter.
- Erfinde niemals Tool-Versionen, API-Endpunkte oder Infrastrukturdetails. Trainingsdaten sind für Spezifika unzuverlässig.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: [Aus Nutzereingabe], [Dokumentvorlage] oder [KI-strukturiert — mit SME prüfen].

> **Tipp:** Fordere über companyFILES eine Markdown-, DOCX- oder PDF-Ausgabe an, um ein formatiertes, publikationsreifes Dokument zu erhalten.
