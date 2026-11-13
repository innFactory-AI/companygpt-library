---
name: de-compliance-tracking
description: Operatives Compliance-Monitoring, Gap-Analyse und Remediation-Tracking gegen Frameworks und Richtlinien. Verwende ihn bei der Audit-Vorbereitung, beim laufenden Compliance-Monitoring oder beim Bewerten von Lücken gegenüber einem Framework. Auslösen mit "Compliance tracken für", "Compliance-Gap-Analyse", "Audit-Readiness-Check".
---

# Compliance-Tracking-Skill

Überwache Compliance gegen Frameworks, Richtlinien und Standards — Gap-Analyse, Remediation-Tracking und Bewertung der Audit-Bereitschaft. Für rechtliche Auslegung verwende stattdessen die Skills check-compliance oder handle-gdpr. Compliance-Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **GRC-Tools über MCP** (z. B. Vanta, Drata, OneTrust) | Control-Register, Evidence-Status, Framework-Mappings, Maturity-Bewertungen |
| **Ticketing über MCP** (z. B. Jira, ServiceNow, Asana) | Remediation-Items, Status, Verantwortlichkeiten, Fälligkeitstermine |
| **companyRAG / Datei-Upload** | Richtliniendokumente, Audit-Berichte, Evidence-Dateien, Framework-Dokumentation |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Anforderungserfassung

### Framework-Mapping

Identifiziere alle Compliance-Pflichten, die für den Geltungsbereich relevant sind:

| Quellentyp | Beispiele | Wie zu identifizieren |
| --- | --- | --- |
| **Regulatorisch** | DSGVO, SOX, HIPAA, DORA, NIS2, branchenspezifische Regulierungen | Legal-/Compliance-Team, Regulierungsregister |
| **Vertraglich** | Kunden-AVVs, SLAs, Lieferantenverträge, Partnerschaftskonditionen | Vertragsablage, Beschaffungsunterlagen |
| **Interne Richtlinie** | Informationssicherheitsrichtlinie, Acceptable Use, Datenklassifizierung | Richtlinienmanagementsystem, Governance-Dokumente |
| **Industriestandards** | ISO 27001, SOC 2, PCI DSS, NIST CSF | Zertifizierungsumfang, Kundenanforderungen |
| **Freiwillige Selbstverpflichtungen** | ESG-Frameworks, Branchen-Codes-of-Conduct, Pledges | Unternehmenskommunikation, Nachhaltigkeitsberichte |

### Control-Zerlegung

Zerlege für jedes Framework bzw. jede Richtlinie die Anforderungen in einzelne, bewertbare Controls:

```
CONTROL-REGISTER-EINTRAG:
  Control-ID:        [eindeutige Kennung — nutze das Nummernschema der Organisation, falls vorhanden]
  Framework:         [Quell-Framework oder Richtlinie]
  Anforderung:       [konkreter Klausel- oder Abschnittsverweis]
  Control-Beschreibung: [was vorhanden sein oder getan werden muss — konkret und beobachtbar]
  Control-Typ:       [Preventive / Detective / Corrective]
  Control-Art:       [Technical / Administrative / Physical]
  Frequenz:          [Continuous / Periodic (angeben) / Event-driven]
  Verantwortlicher:  [zuständige Person oder Rolle]
  Evidence-Typ:      [was Compliance belegt — Logs, Richtlinien, Screenshots, Attestierungen]
```

## Ist-Aufnahme

### Bewertung der Control-Wirksamkeit

Bewerte jedes Control anhand einer Maturity-Skala:

| Rating | Definition | Evidence-Merkmale |
| --- | --- | --- |
| **Not implemented** | Control existiert nicht oder ist nicht operativ | Keine Evidence verfügbar |
| **Ad hoc** | Control existiert, ist aber informell, inkonsistent oder personenabhängig | Nur anekdotische Evidence; keine Dokumentation |
| **Defined** | Control ist mit klaren Verfahren dokumentiert | Schriftliches Verfahren vorhanden; Ausführung kann variieren |
| **Managed** | Control wird konsistent ausgeführt und überwacht | Konsistente Evidence; periodische Reviews finden statt |
| **Optimised** | Control wird auf Basis von Metriken und Feedback kontinuierlich verbessert | Metrikgetrieben; proaktiver Verbesserungszyklus |

### Bewertungsprozess

Für jedes Control im Register:

1. Evidence sammeln: Erfasse den im Control-Register angegebenen Evidence-Typ.
2. Vollständigkeit prüfen: Deckt die Evidence den gesamten Umfang und Zeitraum ab?
3. Wirksamkeit bewerten: Erfüllt das Control seinen vorgesehenen Zweck?
4. Maturity bewerten: Wende die obige Rating-Skala anhand von Evidence-Qualität und -Konsistenz an.
5. Lücken dokumentieren: Beschreibe dort, wo das Control hinter der Anforderung zurückbleibt, die konkrete Lücke.
6. Abhängigkeiten notieren: Identifiziere Controls, die von der Wirksamkeit anderer Controls abhängen.

### Format der Bewertungsausgabe

```
CONTROL-BEWERTUNG:
  Control-ID:           [aus Register]
  Control-Beschreibung: [aus Register]
  Aktuelles Rating:     [Not implemented / Ad hoc / Defined / Managed / Optimised]
  Ziel-Rating:          [von der Organisation geforderte Maturity-Stufe]
  Lücke:                [konkretes Defizit, falls aktuell < Ziel]
  Geprüfte Evidence:    [Liste der geprüften Evidence-Elemente]
  Evidence-Lücken:      [fehlende oder unvollständige Evidence]
  Risiko bei Nichtbehebung: [Konsequenz, falls die Lücke fortbesteht]
  Bewertender:          [wer die Bewertung durchgeführt hat]
  Bewertungsdatum:      [wann]
```

## Gap-Analyse

### Gap-Klassifizierung

| Gap-Typ | Definition | Beispiel |
| --- | --- | --- |
| **Design-Gap** | Control fehlt oder das Design adressiert die Anforderung nicht | Es existiert kein Access-Review-Prozess für ein System, das vierteljährliche Reviews erfordert |
| **Operating-Gap** | Control existiert, wird aber nicht konsistent oder wirksam ausgeführt | Access-Review-Prozess existiert, wurde aber im letzten Jahr nur einmal durchgeführt |
| **Evidence-Gap** | Control funktioniert korrekt, aber die Evidence reicht nicht aus, um Compliance zu belegen | Access-Reviews werden vierteljährlich durchgeführt, aber die Ergebnisse werden nicht dokumentiert |
| **Scope-Gap** | Control deckt einige, aber nicht alle in-scope Systeme, Prozesse oder Standorte ab | Access-Reviews decken Produktionssysteme ab, aber keine Staging-Umgebungen |

### Gap-Priorisierungsmatrix

Priorisiere die Remediation auf Basis von regulatorischem Risiko und Aufwand:

|  | Hohes regulatorisches Risiko | Mittleres regulatorisches Risiko | Geringes regulatorisches Risiko |
| --- | --- | --- | --- |
| **Geringer Aufwand** | Sofort — Quick Win mit hohem Wert | Hoch — leicht zu beheben, lohnenswert | Mittel — im normalen Zyklus angehen |
| **Mittlerer Aufwand** | Hoch — angesichts des Risikos Ressourcen einsetzen | Mittel — planen und terminieren | Gering — im nächsten Zyklus berücksichtigen |
| **Hoher Aufwand** | Hoch — muss angegangen, aber sorgfältig geplant werden | Mittel — für künftigen Zyklus planen | Gering — deprioritisieren, sofern nicht strategisch |

Das regulatorische Risiko sollte vom Compliance-Team bewertet und nicht angenommen werden. Im Zweifel als höheres Risiko einstufen, bis eine fachkundige Prüfung erfolgt ist.

## Remediation-Planung

### Remediation-Tracker

Für jede identifizierte Lücke:

```
REMEDIATION-ITEM:
  Gap-ID:            [eindeutige Referenz, verknüpft mit der Control-Bewertung]
  Control-ID:        [aus Register]
  Gap-Typ:           [Design / Operating / Evidence / Scope]
  Gap-Beschreibung:  [konkretes Defizit]
  Priorität:         [aus Priorisierungsmatrix]
  Remediation-Maßnahme: [konkreter Schritt zur Schließung der Lücke — nicht "Prozess verbessern", sondern "vierteljährlichen Access-Review mit [Tool] über [Scope] einführen"]
  Verantwortlicher:  [für die Remediation zuständige Person]
  Zieltermin:        [Frist zum Abschluss]
  Status:            [Not started / In progress / Blocked / Complete / Verified]
  Abhängigkeiten:    [weitere Maßnahmen, Freigaben oder benötigte Ressourcen]
  Verifizierungsmethode: [wie der Abschluss bestätigt wird — erforderliche Evidence]
  Verifizierungsdatum: [wann die Compliance nach der Remediation neu bewertet wird]
```

### Status-Tracking

Aggregiere die Remediation-Items zu einer programmweiten Sicht:

```
REMEDIATION-DASHBOARD — [Datum]

Gesamtzahl Lücken:    [Anzahl]
Not started:          [Anzahl] — [% des Gesamten]
In progress:          [Anzahl] — [% des Gesamten]
Blocked:              [Anzahl] — [% des Gesamten] — [Blocker auflisten]
Complete:             [Anzahl] — [% des Gesamten]
Verified:             [Anzahl] — [% des Gesamten]

Überfällige Items:    [Anzahl mit Verantwortlichen und ursprünglichen Zielterminen]
Gefährdete Items:     [Items, die den Zieltermin voraussichtlich verfehlen]
Nächster Meilenstein: [anstehender Audit-Termin oder Reporting-Deadline]
```

## Audit-Readiness-Bewertung

### Pre-Audit-Checkliste

Bei der Vorbereitung auf ein internes oder externes Audit:

1. Scope bestätigen: Bestätige, welche Controls, Systeme und Zeiträume für das Audit in scope sind.
2. Evidence-Vollständigkeit: Prüfe für jedes in-scope Control, dass Evidence existiert, aktuell ist und den vollen Audit-Zeitraum abdeckt.
3. Vorbereitung der Verantwortlichen: Briefe Control-Owner zu ihren Aufgaben während des Audits — was sie gefragt werden könnten und welche Evidence sie bereithalten sollten.
4. Status der Gap-Remediation: Identifiziere offene Lücken im Audit-Scope — entscheide, ob sie vor dem Audit geschlossen werden können oder offengelegt werden müssen.
5. Frühere Findings: Prüfe Findings aus dem letzten Audit — bestätige, dass alle Remediation-Maßnahmen abgeschlossen und verifiziert sind.
6. Zugriffsvorbereitung: Stelle sicher, dass Auditoren Zugriff auf die benötigten Systeme, Dokumentationen und Personen haben.

### Readiness-Score

Erstelle eine Readiness-Bewertung pro Control-Bereich:

| Control-Bereich | Controls in Scope | Vollständig konform | Lücken mit Remediation | Offene Lücken | Readiness |
| --- | --- | --- | --- | --- | --- |
| [Bereichsname] | [Anzahl] | [Anzahl] | [Anzahl] | [Anzahl] | Green / Amber / Red |

**Scoring**: Green = alle Controls konform oder Lücken behoben; Amber = Lücken bestehen, Remediation läuft und ist voraussichtlich vor dem Audit abgeschlossen; Red = offene Lücken, die vor dem Audit voraussichtlich nicht gelöst werden.

## Referenz gängiger Frameworks

Dieser Skill unterstützt das Tracking gegen jedes Compliance-Framework. Häufig anzutreffende Frameworks sind:

| Framework | Typischer Scope | Beispiele für Control-Domänen |
| --- | --- | --- |
| **ISO 27001** | Informationssicherheits-Management | Access Control, Kryptografie, Operations Security, Lieferantenbeziehungen |
| **SOC 2** | Controls von Dienstleistungsorganisationen | Security, Availability, Processing Integrity, Confidentiality, Privacy |
| **DSGVO** | Schutz personenbezogener Daten | Rechtsgrundlage, Betroffenenrechte, Meldung von Verletzungen, DSFAs |
| **DORA** | Digitale operationale Resilienz (Finanzdienstleistungen) | IKT-Risikomanagement, Incident-Reporting, Resilienz-Tests |
| **NIS2** | Netz- und Informationssicherheit | Risikomanagement-Maßnahmen, Incident-Handling, Lieferkettensicherheit |
| **PCI DSS** | Sicherheit von Zahlungskartendaten | Netzwerksicherheit, Access Control, Monitoring, Verschlüsselung |

Wenn der Nutzer ein bestimmtes Framework nennt, ordne dessen Anforderungen der obigen Control-Register-Struktur zu. Erzeuge keine framework-spezifischen Control-Listen aus Trainingsdaten — verwende das eigene Control-Mapping des Nutzers oder die offizielle Framework-Dokumentation.

## Leitplanken

- Erzeuge niemals regulatorische Anforderungen oder Compliance-Auslegungen aus Trainingsdaten. Alle Anforderungen stammen vom Compliance-Team des Nutzers, aus Richtlinien oder aus der Framework-Dokumentation.
- Gib niemals rechtliche Einschätzungen zum Compliance-Status ab. Nenne das Bewertungsergebnis und empfiehl eine Verifizierung durch qualifizierte Compliance-Fachleute.
- Erfinde niemals Audit-Findings, Remediation-Status oder Evidence. Alle Compliance-Daten kommen vom Nutzer; ohne Evidence keine Aussage zum Compliance-Status.
- Kennzeichne generierte Inhalte: `[Aus Compliance-Daten]`, `[Framework-Methodik]`, `[KI-Bewertung — mit Compliance-Team verifizieren]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Dokument zu erhalten.
