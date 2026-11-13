---
name: de-tech-docs
description: Erstellt technische Dokumentation — API-Referenzen, Runbooks, ADRs und Onboarding-Guides — aus Code-Kontext oder informellen Beschreibungen. Verwende ihn, wenn du ein System dokumentierst, Onboarding-Material erstellst oder einen ADR schreibst. Auslösen mit "Doku schreiben für", "diese API dokumentieren", "einen ADR erstellen für".
---

# Technische-Doku-Skill

Erstelle technische Dokumentation — API-Referenzen, Runbooks, ADRs, Onboarding-Guides und READMEs — aus Code, informellen Beschreibungen oder System-Kontext. Der Skill leitet zur passenden Vorlage weiter und sorgt für Doku, die am ersten Tag nützlich und langfristig wartbar ist.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **companyRAG-Sammlung** | Bestehende Doku, Architektur-Kontext, Code-Konventionen |
| **Git-Provider über MCP** (z. B. GitHub, GitLab) | Quellcode, Commit-Historie, vorhandene Dokumentation |
| **Datei-Upload / companyFILES** | Export im bevorzugten Format des Teams (DOCX, PDF) |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Dokumenttyp-Router

Beginne hier. Der Dokumenttyp bestimmt die Vorlage, die Zielgruppe und den Detailgrad.

| Dokumenttyp | Verwenden, wenn | Primäre Zielgruppe | Schlüsselmerkmal |
| --- | --- | --- | --- |
| **API-Referenz** | Du eine REST-, GraphQL- oder RPC-API dokumentierst | Entwickler, die die API nutzen | Vollständig, maschinenlesbar, beispielgetrieben |
| **Runbook** | Du eine operative Prozedur dokumentierst | On-Call-Engineers, SREs | Schritt für Schritt, unter Druck ausführbar |
| **ADR** | Du eine Architektur- oder Designentscheidung festhältst | Aktuelle und künftige Engineers | Kontext-bewahrend, entscheidungsfokussiert |
| **Onboarding-Guide** | Du neuen Teammitgliedern hilfst, produktiv zu werden | Neue Engineers im Team | Schrittweise, ohne Vorannahmen, praxisnah |
| **README** | Du ein Projekt, einen Service oder eine Library vorstellst | Alle, die dem Code zum ersten Mal begegnen | Knapp, eigenständig, Quick-Start-orientiert |

Passt das Dokument nicht zu diesen Typen, bitte den Nutzer, Zielgruppe und Zweck zu beschreiben — und passe dann die nächstliegende Vorlage an.

## Dokumentationsprinzipien

Gilt für jeden Dokumenttyp:

1. Schreibe für den Leser, nicht für den Autor. Der Leser weiß nicht, was du weißt. Setze keinen Kontext voraus, der nicht auf der Seite steht.
2. Beginne mit dem Warum. Bevor du erklärst, wie etwas funktioniert, erkläre, warum jemand das wissen muss.
3. Zeigen, dann erklären. Beginne mit einem konkreten Beispiel, erkläre dann das allgemeine Muster. Beispiele sind der meistgelesene Teil jeder technischen Doku.
4. Aktuell halten oder löschen. Veraltete Doku ist schlimmer als keine Doku — sie führt aktiv in die Irre. Lässt sich ein Dokument nicht pflegen, kennzeichne es mit einer Veralterungswarnung oder entferne es.
5. Eine Single Source of Truth. Dupliziere Informationen nicht über Dokumente hinweg. Verweise stattdessen auf die maßgebliche Quelle. Duplizierte Doku driftet auseinander.

## API-Referenz-Vorlage

```
# [API-Name] Referenz

## Überblick
[Ein Absatz: was diese API tut, wer sie nutzt und wie man startet.]

## Authentifizierung
[Authentifizierungsmethode, Token-Format, wo man Credentials erhält.]

## Base-URL
[Base-URL für jede Umgebung — Production, Staging, Sandbox.]

## Endpunkte

### [HTTP-Methode] [Pfad]
[Einzeiler, was dieser Endpunkt tut.]

**Request**

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| [Name] | [path/query/header/body] | [Typ] | [ja/nein] | [was es ist] |

**Request-Beispiel**
[Vollständiger, kopierbarer Request mit realistischen (aber nicht echten) Daten.]

**Response**

| Feld | Typ | Beschreibung |
|---|---|---|
| [Name] | [Typ] | [was es bedeutet] |

**Response-Beispiel**
[Vollständiger Response-Body mit realistischen Daten.]

**Fehler-Responses**

| Status-Code | Error-Code | Beschreibung | Behebung |
|---|---|---|---|
| [Code] | [error_code] | [was schiefging] | [wie man es behebt] |

[Für jeden Endpunkt wiederholen.]

## Rate Limits
[Limits pro Endpunkt oder global. Was bei Überschreitung passiert.]

## Pagination
[Pagination-Mechanismus (Cursor, Offset), Parameter, Standard-Seitengröße.]

## Versionierung
[Wie API-Versionen angegeben werden. Deprecation-Policy.]

## Changelog
[Aktuelle Änderungen mit Datum. Breaking Changes hervorgehoben.]
```

## Runbook-Vorlage

```
# Runbook: [Prozedurname]

## Zweck
[Welches Problem löst dieses Runbook? Wann sollte es eingesetzt werden?]

## Voraussetzungen
- [ ] [Erforderliche Zugänge/Berechtigungen]
- [ ] [Tools, die installiert sein müssen]
- [ ] [Kontext, der vor dem Start verstanden sein muss]

## Schweregrad / Dringlichkeit
[Wann wird dieses Runbook ausgelöst? Welcher Zeitdruck besteht?]

## Schritte

### Schritt 1: [Aktion]
**Befehl/Aktion:**
[Exakter Befehl oder UI-Schritte. Kopierbar.]

**Erwartete Ausgabe:**
[Was du sehen solltest, wenn es funktioniert hat.]

**Wenn es fehlschlägt:**
[Was zu tun ist, wenn dieser Schritt nicht die erwartete Ausgabe liefert.]

### Schritt 2: [Aktion]
[Muster für jeden Schritt wiederholen.]

## Verifikation
[Wie man bestätigt, dass die Prozedur erfolgreich war. Konkrete Checks.]

## Rollback
[Wie man die Prozedur rückgängig macht, falls etwas schiefgeht.]

## Eskalation
[Wen man kontaktiert, wenn das Runbook das Problem nicht löst.]

## Historie
| Datum | Autor | Änderung |
|---|---|---|
| [Datum] | [Name] | [was sich änderte] |
```

## Architecture Decision Record (ADR) — Vorlage

```
# ADR-[NNN]: [Titel der Entscheidung]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-NNN]

## Datum
[YYYY-MM-DD]

## Kontext
[Welche technische oder geschäftliche Situation hat diese Entscheidung ausgelöst? Welche Kräfte wirken? Welche Constraints bestehen? Schreibe genug, dass jemand, der dies in zwei Jahren liest, die Situation ohne Rückfragen versteht.]

## Entscheidung
[Die Entscheidung, klar formuliert. "Wir werden [X tun] für [Zweck Y]."]

## Betrachtete Optionen

### Option A: [Name]
- Pro: [Liste]
- Contra: [Liste]

### Option B: [Name]
- Pro: [Liste]
- Contra: [Liste]

## Konsequenzen
- [Was dadurch einfacher wird]
- [Was schwieriger wird]
- [Welche neuen Constraints entstehen]
- [Welche Folgeentscheidungen nötig sind]

## Review-Trigger
[Wann sollte diese Entscheidung überprüft werden? Konkrete Bedingungen, kein vages "regelmäßig".]
```

## Onboarding-Guide-Vorlage

```
# Onboarding: [Team-/Systemname]

## Willkommen
[Ein Absatz: was dieses Team oder System tut und warum es existiert.]

## Vor deinem ersten Tag
- [ ] [Account-/Zugangs-Setup]
- [ ] [Zu installierende Software]
- [ ] [Zu lesende Dokumente]

## Tag 1: Zum Laufen bringen
[Schritt-für-Schritt-Anleitung zum Einrichten der Entwicklungsumgebung. Setze nichts über ein Standard-Laptop hinaus voraus.]

### Klonen und Bauen
[Exakte Befehle. Erwartete Ausgabe bei jedem Schritt.]

### Lokal ausführen
[Wie man das System startet. Wie man verifiziert, dass es läuft.]

### Tests ausführen
[Wie man die Test-Suite ausführt. Wie man die Ausgabe interpretiert.]

## Woche 1: Das System verstehen
[Architektur-Überblick. Wichtige Komponenten und ihr Zusammenspiel. Links zu tieferer Doku.]

### Architektur-Überblick
[Beschreibung eines High-Level-Diagramms. Hauptkomponenten und ihre Verantwortlichkeiten.]

### Schlüsselkonzepte
[Domänenspezifische Begriffe und Konzepte, die ein neuer Engineer kennen muss.]

### Wo die Dinge liegen
[Verzeichnisstruktur, wichtige Dateien, Konfigurationsorte.]

## Woche 2–4: Beitragen
[Wie man eine Aufgabe übernimmt, eine Änderung vornimmt, einen PR einreicht, ihn reviewen und deployen lässt.]

### Entwicklungs-Workflow
[Branch-Benennung, Commit-Konventionen, PR-Prozess, CI/CD-Pipeline.]

### Häufige Aufgaben
[Schritt-für-Schritt-Anleitungen für die häufigsten Änderungsarten — neuer Endpunkt, neue UI-Komponente, Datenbankmigration usw.]

## Wen man fragt
[Teammitglieder und ihre Fachgebiete. Kommunikationskanäle.]

## Glossar
[Domänenbegriffe, Akronyme und internes Jargon mit Definitionen.]
```

## README-Vorlage

```
# [Projektname]

[Ein Satz: was dieses Projekt tut.]

## Quick Start

[Minimale Schritte, um das Projekt zum Laufen zu bringen. Ziel: unter 5 Minuten für einen Entwickler mit installierten Voraussetzungen.]

## Voraussetzungen

- [Runtime und Version]
- [Paketmanager]
- [Externe Services]

## Installation

[Exakte Befehle.]

## Verwendung

[Der häufigste Use Case mit einem konkreten Beispiel.]

## Konfiguration

[Umgebungsvariablen, Konfigurationsdateien und ihr Zweck. Defaults vermerkt.]

## Entwicklung

[Wie man die Entwicklungsumgebung einrichtet, Tests ausführt und Änderungen einreicht.]

## Architektur

[Kurzer Überblick über die Projektstruktur. Was wo liegt und warum.]

## Troubleshooting

[Häufige Probleme und ihre Lösungen.]

## Mitwirken

[Wie man beiträgt. Link zu einem ausführlicheren Contributing-Guide, falls vorhanden.]
```

## Leitplanken

- Erfinde niemals API-Endpunkte, Parameter oder Response-Formate. Wenn API-Details fehlen, erzeuge die Vorlage mit `[NOCH AUSZUFÜLLEN]`-Platzhaltern.
- Erfinde niemals Systemarchitektur oder operative Prozeduren. Kennzeichne Lücken explizit: `[Fehlt: Authentifizierungsmechanismus dieses Service beschreiben]`.
- Erzeuge niemals unverifizierte Code-Beispiele. Kennzeichne die Quelle: `[Aus nutzerbereitgestelltem Code]`, `[Aus API-Dokumentation]` oder `[Illustratives Beispiel — gegen die tatsächliche API verifizieren]`.
- Lieber unvollständig und korrekt als vollständig und erfunden. Ein Dokument mit gekennzeichneten Lücken ist vertrauenswürdiger als eines voller plausibler, aber unverifizierter Details.

> **Tipp:** Fordere über companyFILES eine Markdown-, DOCX- oder PDF-Ausgabe an, um eine formatierte, sofort teilbare Doku zu erhalten.
