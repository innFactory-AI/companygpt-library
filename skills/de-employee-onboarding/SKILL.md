---
name: de-employee-onboarding
description: Erstellt personalisierte Onboarding-Checklisten und 30/60/90-Tage-Pläne für neue Mitarbeitende, zugeschnitten auf Rolle und Standort. Verwende ihn beim Onboarding einer neuen Person, beim Neugestalten des Onboarding-Erlebnisses oder beim Skalieren von Onboarding über Teams hinweg. Auslösen mit "Onboarding-Plan für", "Checkliste für neue Mitarbeitende", "30/60/90 für [Rolle]".
---

# Mitarbeiter-Onboarding-Skill

> **Hinweis:** Dieser Skill unterstützt bei HR-Workflows, stellt aber keine arbeitsrechtliche Beratung dar. Lass alle Ergebnisse von qualifizierten HR-Fachleuten und arbeitsrechtlicher Beratung in der jeweiligen Rechtsordnung prüfen.

Gestalte personalisierte Onboarding-Programme — Pre-Boarding, Logistik am ersten Tag, 30/60/90-Tage-Meilensteine, Buddy-Zuweisung und Wirksamkeitsmessung. Organisationsspezifische Details kommen von dir, aus angebundenen HR-Systemen, companyRAG-Sammlungen oder hochgeladenen Dateien.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **HRIS über MCP** (z. B. Workday, BambooHR, Personio) | Stammdaten der Person, Rolle und Level, Abteilung, Manager, Startdatum, Beschäftigungsart |
| **Aufgaben-Tracker über MCP** (z. B. Asana, Monday, Jira, Notion) | Onboarding-Aufgaben, Verantwortlichkeiten, Status der Checklisten-Punkte |
| **companyRAG-Sammlungen / Datei-Upload** | Rollenbeschreibungen, Team-Playbooks, Compliance-Vorgaben, bestehende Onboarding-Vorlagen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Onboarding-Design-Workflow

### Schritt 1: Rollenkontext sammeln

Sammle vor dem Erstellen von Onboarding-Inhalten diese Eingaben:

```
ONBOARDING-KONTEXT
==================
Name neue Person:     [Name]
Rolle:                [Titel und Level]
Abteilung / Team:     [organisatorische Einheit]
Manager:              [Name]
Startdatum:           [Datum]
Standort:             [Büro / hybrid / remote — Stadt, Land]
Beschäftigungsart:    [unbefristet / befristet / freiberuflich]
Interner Wechsel:     [ja / nein — interne Wechsel erfordern angepasstes Onboarding]
Vorheriger Kontext:   [relevanter Hintergrund — Branche, ähnliche Rollen, interne Erfahrung]
Teamgröße:            [wie viele Personen im unmittelbaren Team]
Wichtige Stakeholder: [bereichsübergreifende Kontakte, mit denen die Person regelmäßig arbeitet]
```

### Schritt 2: Pre-Boarding-Checkliste (vor Tag 1)

Pre-Boarding umfasst alles, was zwischen der Vertragsannahme und dem ersten Tag passieren sollte. Dieser Zeitraum prägt das Erlebnis am ersten Tag und das frühe Engagement maßgeblich.

#### Administratives Pre-Boarding

| Punkt | Verantwortlich | Zeitpunkt | Status |
| --- | --- | --- | --- |
| **Arbeitsvertrag unterschrieben** | HR | Vor dem Startdatum | ☐ |
| **IT-Equipment bestellt und konfiguriert** | IT / HR | 5+ Werktage vor Start | ☐ |
| **Systemkonten angelegt** | IT | 2–3 Werktage vor Start | ☐ |
| **E-Mail und Kalender eingerichtet** | IT | 1–2 Werktage vor Start | ☐ |
| **Gebäudezugang / Sicherheitsausweis** | Facilities | Vor dem Startdatum | ☐ |
| **Lohnabrechnung und Benefits-Anmeldung gestartet** | HR / Payroll | Vor dem Startdatum | ☐ |
| **Arbeitsplatz vorbereitet** | Team / Facilities | Vor dem Startdatum | ☐ |
| **Willkommenspaket versendet** | HR / Team | 3–5 Tage vor Start | ☐ |

#### Manager-Pre-Boarding

| Punkt | Verantwortlich | Zeitpunkt | Status |
| --- | --- | --- | --- |
| **Onboarding-Buddy zugewiesen** | Manager | 1+ Woche vor Start | ☐ |
| **Kalender der ersten Woche befüllt** | Manager + Buddy | 2–3 Tage vor Start | ☐ |
| **Team über neue Person informiert** | Manager | 1 Woche vor Start | ☐ |
| **30/60/90-Tage-Plan entworfen** | Manager | Vor dem Startdatum | ☐ |
| **Vorstellungen bei wichtigen Stakeholdern geplant** | Manager | Vor oder während der ersten Woche | ☐ |

#### Standortspezifisches Pre-Boarding

Passe das Pre-Boarding an den Standort der neuen Person an:

| Standorttyp | Zusätzliche Punkte |
| --- | --- |
| **Bürobasiert** | Schreibtischzuweisung, Parkplatz-/Nahverkehrsinfos, Bürorundgang geplant, Mittagessen für Tag 1 |
| **Hybrid** | Bürozeiten kommuniziert, Homeoffice-Equipment versandt, Videokonferenz getestet |
| **Remote** | Gesamtes Equipment versandt und erhalten, virtueller Onboarding-Plan bestätigt, Zeitzonen berücksichtigt |
| **International** | Arbeitserlaubnis geprüft, Anstellung bei lokaler Gesellschaft bestätigt, länderspezifische Pflichtschulungen identifiziert, lokale Feiertage geteilt |

### Schritt 3: Struktur der ersten Woche

Die erste Woche gibt den Ton für das gesamte Onboarding-Erlebnis vor. Strukturiere sie so, dass Informationsvermittlung und Beziehungsaufbau ausgewogen sind.

#### Agenda für Tag 1

| Zeitblock | Aktivität | Verantwortlich | Zweck |
| --- | --- | --- | --- |
| **Erste 30 Min.** | Willkommen durch Manager — 1:1-Check-in | Manager | Persönliches Willkommen, Erwartungen für den Tag setzen |
| **Vormittag** | HR-Orientierung — Richtlinien, Benefits, Compliance-Schulung | HR | Administrative Grundlagen |
| **Später Vormittag** | IT-Setup — alle Systeme, Zugänge und Tools prüfen | IT / Buddy | Technische Blocker beseitigen |
| **Mittag** | Team-Lunch oder virtueller Kaffee | Team / Buddy | Soziale Verbindung |
| **Nachmittag** | Team-Vorstellung — unmittelbare Teammitglieder kennenlernen | Manager / Team | Kontext und Beziehungen |
| **Tagesende** | Buddy-Check-in — Fragen, erste Eindrücke | Buddy | Unterstützung und Wohlbefinden |

#### Rahmen für Tage 2–5

| Fokusbereich | Aktivitäten | Ergebnis |
| --- | --- | --- |
| **Produkt-/Service-Verständnis** | Produktdemos, Dokumentation durchgehen, Customer Journey durchspielen | Person kann artikulieren, was die Organisation für wen tut |
| **Team-Kontext** | Teamziele, aktuelle Projekte, Arbeitsweisen, Kommunikationsnormen | Person versteht die Prioritäten des Teams und wie Arbeit fließt |
| **Stakeholder-Vorstellungen** | Geplante 1:1s mit wichtigen bereichsübergreifenden Partnern | Person kann Gesichter Namen zuordnen und versteht Kollaborationspunkte |
| **Rollenspezifisches Onboarding** | Fachschulungen, tool-spezifische Tutorials, Shadow-Sessions | Person beginnt, die tägliche Arbeit der Rolle zu verstehen |
| **Kultur und Werte** | Werte-Session, kulturspezifisches Onboarding, ERG-Vorstellungen (falls zutreffend) | Person versteht organisatorische Normen und Community |

### Schritt 4: 30/60/90-Tage-Plan

Der 30/60/90-Plan strukturiert das Einarbeiten der Person in drei Phasen. Jede Phase hat Lernziele, Schlüsselaktivitäten, erwartete Ergebnisse und Erfolgskriterien.

#### Phase 1: Lernen (Tage 1–30)

```
PHASE 1: LERNEN — Tage 1–30
===========================
Ziel: Fundiertes Grundwissen über Rolle, Team und Organisation aufbauen.

LERNZIELE:
  1. [Rollenspezifisches Wissensziel — z. B. "Produktarchitektur und Kernkomponenten verstehen"]
  2. [Prozesswissen-Ziel — z. B. "Alle Pflicht-Compliance-Schulungen abschließen"]
  3. [Beziehungsziel — z. B. "Alle wichtigen Stakeholder treffen und ihre Prioritäten verstehen"]

SCHLÜSSELAKTIVITÄTEN:
  - [Aktivität 1 mit Verantwortlichem und Zeitrahmen]
  - [Aktivität 2]
  - [Aktivität 3]

ERWARTETE ERGEBNISSE:
  - Kann Teamziele und aktuelle Prioritäten artikulieren
  - Hat alle Pflichtschulungen und Compliance-Anforderungen abgeschlossen
  - Hat alle wichtigen Stakeholder getroffen und versteht Kollaborationspunkte
  - Kann Kern-Tools und -Systeme selbstständig nutzen

ERFOLGSKRITERIEN (beim 30-Tage-Check-in bewertet):
  - [Spezifisches, beobachtbares Kriterium 1]
  - [Spezifisches, beobachtbares Kriterium 2]

UNTERSTÜTZUNG:
  - Wöchentliches 1:1 mit Manager (30 Min.)
  - Tägliches Check-in mit Buddy (15 Min., abnehmend bis nach Bedarf)
  - Zugang zu Onboarding-Dokumentation und Wissensdatenbank
```

#### Phase 2: Beitragen (Tage 31–60)

```
PHASE 2: BEITRAGEN — Tage 31–60
===============================
Ziel: Erste sinnvolle Beiträge leisten und zugleich die Fachexpertise vertiefen.

BEITRAGSZIELE:
  1. [Erstes eigenständiges Ergebnis — z. B. "Ein Projekt mit kleinem Umfang end-to-end verantworten"]
  2. [Prozessverbesserung — z. B. "Eine Verbesserungsmöglichkeit aus der Frische-Perspektive identifizieren"]
  3. [Kollaborationsziel — z. B. "Eine bereichsübergreifende Initiative leiten oder mitleiten"]

SCHLÜSSELAKTIVITÄTEN:
  - [Aktivität 1 mit zunehmender Eigenständigkeit]
  - [Aktivität 2]

ERWARTETE ERGEBNISSE:
  - Hat mindestens ein bedeutsames Arbeitsergebnis eigenständig geliefert
  - Trägt mit fundierten Perspektiven zu Team-Diskussionen und -Planung bei
  - Hat Bereiche identifiziert, in denen weitere Entwicklung nötig ist

ERFOLGSKRITERIEN (beim 60-Tage-Check-in bewertet):
  - [Spezifisches Ergebnis oder Resultat 1]
  - [Spezifisches Ergebnis oder Resultat 2]

UNTERSTÜTZUNG:
  - Wöchentliches 1:1 mit Manager (30 Min.)
  - Buddy-Check-ins nach Bedarf (Übergang von geplant zu auf Abruf)
  - Vom Manager eingeholtes Feedback der Stakeholder
```

#### Phase 3: Verantworten (Tage 61–90)

```
PHASE 3: VERANTWORTEN — Tage 61–90
==================================
Ziel: Auf vollem Produktivitätsniveau der Rolle arbeiten und Verantwortungen eigenständig tragen.

VERANTWORTUNGSZIELE:
  1. [Voller Verantwortungsbereich — z. B. "[Bestimmte Verantwortung] end-to-end verantworten, Manager nur bei Eskalationen"]
  2. [Strategischer Beitrag — z. B. "Einen Plan oder eine Initiative vorschlagen, die auf den ersten 60 Tagen aufbaut"]
  3. [Team-Integration — z. B. "Aktiv zu Team-Ritualen, Code-Reviews, Planungssessions beitragen"]

SCHLÜSSELAKTIVITÄTEN:
  - [Aktivität 1 im vollen Rollenumfang]
  - [Aktivität 2]

ERWARTETE ERGEBNISSE:
  - Arbeitet eigenständig auf dem für die Rolle erwarteten Niveau
  - Hat einen klaren Entwicklungsplan für die nächsten 6–12 Monate (siehe Skill design-learning-plan)
  - Team und Stakeholder sehen die Person als beitragendes Teammitglied

ERFOLGSKRITERIEN (beim 90-Tage-Review bewertet):
  - [Spezifisches Ergebnis 1]
  - [Spezifisches Ergebnis 2]
  - Manager und Person stimmen ab: was gut läuft, was Entwicklung braucht, Ziele für das nächste Quartal

UNTERSTÜTZUNG:
  - Wöchentliches oder zweiwöchentliches 1:1 mit Manager
  - Buddy-Beziehung wird zur Peer-Beziehung
  - Formelle Feedback-Erhebung bei wichtigen Stakeholdern
```

### Schritt 5: Buddy-Zuweisung

Der Onboarding-Buddy unterscheidet sich vom Manager und erfüllt eine andere Funktion.

#### Auswahlkriterien für den Buddy

| Kriterium | Warum es wichtig ist |
| --- | --- |
| **Peer- oder Near-Peer-Level** | Die Person sollte sich wohlfühlen, "dumme Fragen" zu stellen — ein Buddy aus der Führungsebene erzeugt ein Machtgefälle, das dies hemmt |
| **Gleiches oder benachbartes Team** | Nähe zur täglichen Arbeit macht die Anleitung des Buddys unmittelbar relevant |
| **Betriebszugehörigkeit von 6+ Monaten** | Der Buddy muss genug wissen, um hilfreich zu sein; zu neu, und er lernt selbst noch |
| **Freiwillige Teilnahme** | Die Buddy-Zuweisung sollte nicht verpflichtend sein — unwillige Buddys bieten schlechte Unterstützung |
| **Kommunikationsstil** | Prüfe, ob der Stil des Buddys zur neuen Person passt (besonders bei Remote-Onboarding, wo schriftliche Kommunikation mehr Gewicht hat) |

#### Verantwortlichkeiten des Buddys

| Verantwortlichkeit | Häufigkeit | Dauer |
| --- | --- | --- |
| Tägliches Check-in (informell) | Täglich in Woche 1–2, danach nach Bedarf | 10–15 Minuten |
| Fragen beantworten und Kontext geben | Laufend | Nach Bedarf |
| In Team-Normen und ungeschriebene Regeln einführen | Woche 1–4 | Organisch |
| Unterstützung bei sozialer Integration | Laufend | Vorstellungen über das unmittelbare Team hinaus |
| Bedenken an Manager oder HR eskalieren | Nach Bedarf | Wenn der Buddy bemerkt, dass die Person Schwierigkeiten hat oder sich zurückzieht |

## Anpassungs-Leitfaden

Passe den Standardrahmen an diese Rollen- und Kontextdimensionen an:

| Dimension | Anpassung |
| --- | --- |
| **Senior- / Führungskraft** | Lernphase verkürzen; Stakeholder-Listening-Tour ergänzen; Board-/Exec-Exposure einbauen; einen Senior-Peer-Buddy statt eines Junior-Buddys zuweisen |
| **Technische Rolle** | Codebase-Orientierung, Architektur-Walkthroughs, Dev-Environment-Setup ergänzen, erster PR/Commit als Meilenstein |
| **Kundenorientierte Rolle** | Produktzertifizierung, Kunden-Shadowing, CRM-Schulung ergänzen, erste Kundeninteraktion als Meilenstein |
| **Remote-Einstellung** | Virtuelle soziale Touchpoints intensivieren; alle Materialien asynchron zugänglich machen; Überschneidungszeiten mit dem Team einplanen |
| **Interner Wechsel** | Organisations-Onboarding überspringen; auf team- und rollenspezifische Elemente fokussieren; bestehende Beziehungen nutzen |
| **Internationale Einstellung** | Umzugsunterstützung, lokale Compliance-Schulung, kulturelle Orientierung, lokalen Feiertagskalender, ggf. Sprachunterstützung ergänzen |

## Wirksamkeitsmessung des Onboardings

### Messrahmen

| Kennzahl | Wann messen | Methode | Zielwert |
| --- | --- | --- | --- |
| **Zufriedenheit der neuen Person** | Tag 7, Tag 30, Tag 90 | Pulse-Umfrage (5–7 Fragen) | Schwellenwert anhand organisationsspezifischer Daten festlegen |
| **Time to Productivity** | Tag 30, Tag 60, Tag 90 | Manager-Bewertung gegen die Meilensteine des 30/60/90-Plans | Variiert je Rolle — Baselines etablieren |
| **30/60/90-Meilenstein-Erfüllung** | An jedem Meilenstein | Erfüllungsrate der Checkliste | 80 %+ der Meilensteine fristgerecht erreicht |
| **Buddy-Zufriedenheit** | Tag 30 | Buddy-Feedbackbogen | Qualitativ — empfinden Buddys das Programm als lohnend? |
| **Frühe Fluktuation** | 6- und 12-Monats-Marke | Fluktuationsdaten | Unter dem Organisationsdurchschnitt für das Rollenlevel |

### Kontinuierliche Verbesserung

Erfasse nach jedem Onboarding-Zyklus:

- Was gut lief (beibehalten)
- Was fehlte (ergänzen)
- Was unnötig war (entfernen)
- Was Anpassung braucht (ändern)

Speise die Verbesserungen in die Onboarding-Vorlagen für die nächste Person zurück.

## Leitplanken

- Erzeuge niemals organisationsspezifische Richtlinien, Systemnamen oder Verfahren. Fordere die Liste vom Nutzer an, statt Punkte zu erfinden.
- Nimm niemals standortspezifische Anforderungen an. Pflichtschulungen, Betriebsrats-Benachrichtigungen und Probezeit-Regeln variieren je Rechtsordnung — kennzeichne sie als "für [Rechtsordnung] prüfen".
- Erzeuge niemals konkrete Zeitpläne für administrative Aufgaben. Diese variieren je Organisation — nutze die Struktur und lass den Nutzer die tatsächlichen Zeitpläne füllen.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Rollenkontext]`, `[Aus Onboarding-Methodik]` oder `[KI-Vorschlag — mit HR prüfen]`.

> **Tipp:** Fordere über companyFILES eine DOCX-Ausgabe an, um ein formatiertes Word-Dokument zu erhalten, das verteilfertig ist. XLSX oder Markdown stehen ebenfalls zur Verfügung.
