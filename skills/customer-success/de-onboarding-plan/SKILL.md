---
name: de-onboarding-plan
description: Erstellt einen strukturierten Kunden-Onboarding-Plan mit Meilensteinen, Verantwortlichkeitszuweisungen und 30/60/90-Tage-Erfolgs-Checkpoints. Verwende ihn, wenn du einen neuen Kunden startest, einen Onboarding-Prozess neu gestaltest oder die CSM-Kapazität skalierst. Auslösen mit "Onboarding-Plan erstellen für", "neuer Kunden-Setup", "30/60/90-Plan für [Kunde]".
---

# Onboarding-Plan-Skill

Erstelle meilensteinbasierte Onboarding-Pläne, die einen neuen Kunden vom unterschriebenen Vertrag bis zum ersten realisierten Mehrwert führen. Kundenspezifische Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Account-Details, Vertragsumfang, ARR, wichtige Kontakte, Closed-Won-Notizen |
| **Projekt-Tracker über MCP** (z. B. Asana, Monday, Jira, Notion) | Aufgabenverfolgung, Meilenstein-Status, Verantwortlichkeitszuweisungen |
| **companyRAG / Datei-Upload** | Sales-Handover-Notizen, Discovery-Call-Zusammenfassungen, technische Assessments |

> **Keine angebundene Quelle?** Gib die Eingaben im Chat an oder lade die relevanten Dateien hoch — der Plan funktioniert als eigenständiges Dokument.

## Onboarding-Planungs-Workflow

Führe diese Schritte für jeden neuen Onboarding-Plan der Reihe nach aus.

### Schritt 1: Anforderungen sammeln

Sammle vor dem Erstellen des Plans diese Eingaben. Kennzeichne Lücken — unvollständige Anforderungen führen später zu Nacharbeit.

| Eingabe | Quelle | Warum sie wichtig ist |
| --- | --- | --- |
| **Vertragsumfang** | CRM / Sales-Handover | Legt fest, was der Kunde gekauft hat und was geliefert werden muss |
| **Geschäftsziele des Kunden** | Sales-Notizen, Discovery-Calls | Verankert Meilensteine an Ergebnissen, die dem Kunden wirklich wichtig sind |
| **Technische Umgebung** | Technisches Pre-Sales-Assessment | Bestimmt die Integrationskomplexität und die technischen Meilensteine |
| **Kunden-Team** | Sales-Handover, CRM-Kontakte | Identifiziert Stakeholder, Entscheider und tägliche Ansprechpartner |
| **Zeitliche Rahmenbedingungen** | Vertrag, Kundenwunsch | Harte Fristen (z. B. Go-live vor Geschäftsjahresende) prägen den Plan |
| **Bekannte Risiken** | Sales-Handover-Notizen | Während des Sales-Prozesses markierte Bedenken (z. B. begrenzte IT-Ressourcen) |
| **Erfolgskriterien** | Vom Kunden genannt oder gemeinsam definiert | Wie "fertig" aus Sicht des Kunden aussieht |

### Schritt 2: Onboarding-Phasen definieren

Strukturiere den Plan in drei Phasen mit klaren Eintritts- und Austrittskriterien.

**Phase 1 — Foundation (Tage 1–30)**

| Element | Detail |
| --- | --- |
| **Ziel** | Technisches Setup abgeschlossen, wichtige Stakeholder onboarded, erster Mehrwert demonstriert |
| **Eintrittskriterien** | Vertrag unterschrieben, Handover von Sales an CS abgeschlossen |
| **Wichtige Meilensteine** | Kickoff-Call, technisches Setup, Admin-Schulung, Erstkonfiguration, erster Use Case live |
| **Austrittskriterien** | Kernplattform konfiguriert, Admin-Nutzer geschult, mindestens ein Use Case in Betrieb |

**Phase 2 — Adoption (Tage 31–60)**

| Element | Detail |
| --- | --- |
| **Ziel** | Breitere Team-Adoption, Workflows etabliert, erste ROI-Belege |
| **Eintrittskriterien** | Austrittskriterien von Phase 1 erfüllt |
| **Wichtige Meilensteine** | Endnutzer-Schulung, Workflow-Konfiguration, Adoption-Check-in, Nutzungsreview |
| **Austrittskriterien** | Ziel-Aktivierungsrate erreicht, Kern-Workflows laufen, erste Erfolgskennzahlen erfasst |

**Phase 3 — Optimierung (Tage 61–90)**

| Element | Detail |
| --- | --- |
| **Ziel** | Vollständiger Rollout, Mehrwert bestätigt, Übergang in eine stabile Dauerbeziehung |
| **Eintrittskriterien** | Austrittskriterien von Phase 2 erfüllt |
| **Wichtige Meilensteine** | Aktivierung erweiterter Funktionen, Review der Erfolgskennzahlen, Check-in mit Executive Sponsor, formelle Übergabe an das laufende CS |
| **Austrittskriterien** | Erfolgskriterien aus Schritt 1 erreicht, laufende Kadenz etabliert, Success-Plan entworfen |

### Schritt 3: Verantwortlichkeiten zuweisen

Jeder Meilenstein braucht einen klaren Verantwortlichen auf beiden Seiten — in deinem Team und im Team des Kunden.

| Rolle | Verantwortlichkeiten | Typischer Verantwortlicher |
| --- | --- | --- |
| **CSM** | Gesamtverantwortung für den Plan, Beziehungsmanagement, Meilenstein-Tracking, Eskalation | Dein Team |
| **Implementation / Solutions** | Technisches Setup, Konfiguration, Integrationen, Datenmigration | Dein Team |
| **Trainer** | Durchführung von Admin- und Endnutzer-Schulungen | Dein Team |
| **Projektleitung Kunde** | Interne Koordination, Verfügbarkeit von Ressourcen, Entscheidungsfindung | Kunden-Team |
| **Kunden-IT / Admin** | Technische Zugänge, Einrichtung der Umgebung, Security-Review | Kunden-Team |
| **Executive Sponsor** (beide Seiten) | Strategisches Alignment, Auflösen von Eskalationen, Erfolgsvalidierung | Beide Teams |

Bei kleineren Accounts kann eine Person mehrere Rollen übernehmen. Bei Enterprise-Accounts erweitere die Rollen nach Bedarf (z. B. eine eigene Leitung für Datenmigration oder Change-Management).

### Schritt 4: Erfolgs-Checkpoints festlegen

Plane formelle Checkpoints an jeder Phasengrenze und zum 90-Tage-Zeitpunkt.

| Checkpoint | Zeitpunkt | Teilnehmende | Agenda |
| --- | --- | --- | --- |
| **Kickoff** | Tag 1–5 | Alle Stakeholder | Vorstellung, Planreview, Zielbestätigung, Timeline-Abstimmung |
| **30-Tage-Review** | Tag 28–32 | CSM, Projektleitung Kunde, Sponsoren (optional) | Review der Phase-1-Meilensteine, Lösung von Problemen, Bereitschaft für Phase 2 |
| **60-Tage-Review** | Tag 58–62 | CSM, Projektleitung Kunde | Review der Adoption-Kennzahlen, Wirksamkeit der Workflows, Planung von Phase 3 |
| **90-Tage-Review** | Tag 88–92 | CSM, Projektleitung Kunde, Executive Sponsoren | Bewertung der Erfolgskriterien, Mehrwert-Zusammenfassung, Übergang in die laufende Kadenz |

Jeder Checkpoint erzeugt ein dokumentiertes Ergebnis: erreichte Meilensteine, verzögerte Meilensteine (mit neuen Terminen), offene Punkte und vereinbarte nächste Schritte.

### Schritt 5: Eine Kommunikationskadenz schaffen

Lege fest, wie und wann du während des Onboardings kommunizierst.

| Kommunikation | Häufigkeit | Kanal | Verantwortlicher |
| --- | --- | --- | --- |
| **Status-Update** | Wöchentlich | E-Mail oder gemeinsames Dokument | CSM |
| **Working Sessions** | Nach Bedarf je Meilenstein | Videocall | Implementation-Lead |
| **Eskalation** | Nach Bedarf | Direktnachricht + E-Mail | CSM oder Projektleitung Kunde |
| **Checkpoint-Review** | An Phasengrenzen | Videocall mit Agenda | CSM |

Passe die Kadenz an den Kunden an — manche bevorzugen asynchrone Updates, andere wollen wöchentliche Syncs. Frage beim Kickoff nach.

## Ausgabevorlage — Onboarding-Plan

```
KUNDEN-ONBOARDING-PLAN
Account: [Name]
CSM: [Name]
Startdatum: [Datum]
Ziel-Abschluss: [Datum — typischerweise 90 Tage ab Start]
Vertragsumfang: [kurze Zusammenfassung dessen, was gekauft wurde]
Erfolgskriterien: [vom Kunden genannte Definition von Erfolg]

PHASE 1 — FOUNDATION (Tage 1–30)
Ziel: [spezifisch für diesen Kunden]
  Meilenstein 1: [Beschreibung]
    Verantwortlich: [Name/Rolle] | Fällig: [Datum] | Status: [Nicht begonnen / In Arbeit / Abgeschlossen]
  Meilenstein 2: [Beschreibung]
    Verantwortlich: [Name/Rolle] | Fällig: [Datum] | Status: [...]
  ...
  Austrittskriterien: [was zutreffen muss, um zu Phase 2 überzugehen]
  30-Tage-Checkpoint: [Datum]

PHASE 2 — ADOPTION (Tage 31–60)
Ziel: [spezifisch für diesen Kunden]
  Meilenstein 1: [Beschreibung]
    Verantwortlich: [Name/Rolle] | Fällig: [Datum] | Status: [...]
  ...
  Austrittskriterien: [was zutreffen muss, um zu Phase 3 überzugehen]
  60-Tage-Checkpoint: [Datum]

PHASE 3 — OPTIMIERUNG (Tage 61–90)
Ziel: [spezifisch für diesen Kunden]
  Meilenstein 1: [Beschreibung]
    Verantwortlich: [Name/Rolle] | Fällig: [Datum] | Status: [...]
  ...
  Austrittskriterien: [was zutreffen muss, damit das Onboarding als abgeschlossen gilt]
  90-Tage-Checkpoint: [Datum]

RISIKEN & GEGENMASSNAHMEN:
  1. [Risiko] → [Plan zur Gegenmaßnahme] → Verantwortlich: [Name]
  2. ...

KOMMUNIKATIONSKADENZ:
  [wie in Schritt 5 definiert]

STAKEHOLDER-MAP:
  Dein Team:     [Name — Rolle, Name — Rolle, ...]
  Kunden-Team:   [Name — Rolle, Name — Rolle, ...]
```

## An dein Geschäft anpassen

Das 30/60/90-Framework ist eine Standardvorgabe. Passe es an dein Produkt und dein Kundenprofil an:

- **Einfaches Produkt, SMB-Kunde:** auf 14/30/45 Tage verkürzen, weniger Meilensteine, leichtere Checkpoints.
- **Komplexe Plattform, Enterprise-Kunde:** auf 30/60/90/120 Tage erweitern; eine Phase 0 (Vorbereitung vor dem Kickoff) und eine Phase 4 (erweiterte Aktivierung) ergänzen.
- **Nutzungsbasiertes Produkt:** zeitbasierte Phasengrenzen durch nutzungsbasierte Trigger ersetzen (z. B. Phase 2 startet bei X aktiven Nutzern, nicht an Tag 31).
- **Multi-Produkt-Rollout:** parallele Tracks je Produkt mit gemeinsamer Timeline und konsolidierten Checkpoints erstellen.
- **High-Touch vs. Tech-Touch:** beim gebündelten Onboarding einzelne Meilensteine durch automatisierte Trigger ersetzen (Willkommenssequenz, In-App-Guides, Self-Serve-Schulungen) sowie geplante Gruppen-Check-ins.

## Leitplanken

- Erfinde niemals Kundenanforderungen, technische Umgebungen oder Geschäftsziele. Alle kundenspezifischen Details müssen vom Nutzer oder aus angebundenen Daten stammen. Wenn Daten fehlen, erzeuge klar gekennzeichnete Platzhalterfelder.
- Nimm niemals die Teamstruktur oder die Ressourcenverfügbarkeit des Kunden an. Frage nach; leite nichts ab.
- Erzeuge niemals konkrete Adoption-Kennzahlen oder Nutzungsziele ohne Kundendaten.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Account-Daten]`, `[Aus Onboarding-Framework]` oder `[CSM-Eingabe erforderlich]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder XLSX-Ausgabe an, um einen formatierten, sofort teilbaren Plan zu erhalten.
