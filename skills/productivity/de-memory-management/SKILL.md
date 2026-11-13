---
name: de-memory-management
description: Pflegt personalisierten Nutzerkontext über Sitzungen hinweg — Terminologie, Präferenzen, Projektkürzel und Arbeitsstil — für schnellere und präzisere Unterstützung. Verwende ihn, wenn du dem Assistenten deinen Arbeitskontext beibringst, Präferenzen aktualisierst oder gespeicherten Kontext durchsiehst. Auslösen mit "merke dir", "aktualisiere meinen Kontext", "was weißt du über mich".
---

# Memory-Management-Skill

Nimm personalisierten Nutzerkontext über Sitzungen hinweg auf, kategorisiere, speichere, rufe ihn ab und bereinige ihn — Projekte, Präferenzen, Terminologie und Arbeitsmuster — sodass jede künftige Konversation mit dem richtigen Wissen beginnt. Der Kontext wird über die CompanyGPT-Memory-Funktion und companyRAG-Sammlungen dauerhaft gehalten.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CompanyGPT Memory** | Dauerhafter Speicher für personalisierten Nutzerkontext über Sitzungen hinweg |
| **companyRAG-Sammlungen** | Umfangreichere Kontextdokumente, Notizsammlungen, durchsuchbares Wissen |
| **MCP-Server** (Notiz-Tools, z. B. Notion, Obsidian) | Bestehende Notizen und Kontext aus angebundenen Systemen |
| **Datei-Upload** | Kontextdokumente, Glossare, Projektnotizen, die du direkt hochlädst |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Kontext-Management-Workflow

### Kontext aufnehmen

Wenn du Kontext zum Merken bereitstellst, erfasse ihn präzise.

**Aufnahmeprozess:**

1. Kontext empfangen — du nennst etwas zum Merken ("merke dir, dass die Q3-Planung das PACE-Framework nutzt" oder "mein Team nennt das Onboarding-Projekt 'Lighthouse'")
2. Verständnis bestätigen — paraphrasiere zur Verifizierung der Richtigkeit zurück an dich. Missverstandenen Kontext nicht speichern.
3. Kategorisieren — der passenden Kontextkategorie zuordnen (siehe Taxonomie unten)
4. Speicherung bestätigen — bestätigen, was in welcher Kategorie in CompanyGPT Memory abgelegt wurde

**Aufnahmeformat:**

```
GESPEICHERTER KONTEXT:
  Kategorie:  [Kategorie aus Taxonomie]
  Schlüssel:  [kurzer Bezeichner — z. B. "Q3-Planungs-Framework"]
  Wert:       [der Kontext selbst — wörtlich oder akkurat paraphrasiert]
  Hinzugefügt:[Datum]
  Quelle:     [vom Nutzer bereitgestellt]
```

### Kategorisieren

Organisiere gespeicherten Kontext in diese Kategorien für effizienten Abruf.

| Kategorie | Was hierhin gehört | Beispiele |
| --- | --- | --- |
| **Projekte** | Aktive Projekte, Codenamen, Zeitpläne, Stakeholder, Status | "Projekt Lighthouse = Onboarding-Redesign, Launch Q3, geleitet von Sarah" |
| **Präferenzen** | Arbeitsstil, Präferenzen beim Ausgabeformat, Kommunikationsstil | "Bevorzugt Stichpunkte gegenüber Fließtext", "Nutzt britische Schreibweise" |
| **Terminologie** | Unternehmensspezifische Begriffe, Akronyme, Jargon, Namenskonventionen | "PACE = Plan, Align, Create, Evaluate — unser Planungs-Framework" |
| **Team** | Teammitglieder, Rollen, Berichtslinien, wichtige Kontakte | "Direct Reports: Alex (Engineering), Maria (Design), Tom (Daten)" |
| **Prozesse** | Wiederkehrende Workflows, Freigabeketten, Standardvorgehen | "Budgetanfragen laufen über Finance → VP → CFO bei Beträgen über 50.000 €" |
| **Tools & Systeme** | Bevorzugte Tools, Systemnamen, Zugriffsmuster | "Nutzt Linear für Aufgaben-Tracking, Notion für Dokumentation" |
| **Einschränkungen** | Grenzen, Limitierungen, zu vermeidende Dinge | "Niemals den Begriff 'Synergie' in Deliverables verwenden — Unternehmenskultur" |

### Speichern

Speicherprinzipien:

- Atomare Einträge: Speichere jeden Kontextbaustein als separaten, in sich geschlossenen Eintrag. "Mein Team nutzt Linear und bevorzugt asynchrone Kommunikation" wird zu zwei Einträgen — einer unter Tools & Systeme, einer unter Präferenzen.
- Wörtlich, wenn möglich: Verwende deine eigenen Worte. Wird zur Klarheit paraphrasiert, bestätige es mit dir.
- Keine Interpretation: Speichere Fakten, keine Schlussfolgerungen. Wenn du sagst "ich arbeite in Berlin", speichere das. Leite keine Zeitzone, Sprachpräferenz oder arbeitsrechtlichen Kontext ab.
- Mit Zeitstempel: Jeder Eintrag enthält das Hinzufügedatum, um Veralten zu verwalten.

### Abrufen

Nutze gespeicherten Kontext proaktiv, um die Qualität der Unterstützung zu verbessern.

**Abruf-Trigger:**

| Trigger | Aktion |
| --- | --- |
| Du verweist auf ein gespeichertes Projekt per Name oder Codename | Gespeicherten Projektkontext automatisch anwenden |
| Aufgabe betrifft eine Domäne, zu der Präferenzen gespeichert sind | Formatierungs-, Stil- und Kommunikationspräferenzen anwenden |
| Du erwähnst ein Teammitglied per Name | Dessen Rolle und Beziehungskontext abrufen |
| Du verwendest unternehmensspezifische Terminologie | Die gespeicherten Definitionen für korrektes Verständnis nutzen |
| Du fragst "was weißt du über mich" oder "was steht in meinem Kontext" | Eine strukturierte Zusammenfassung des gesamten gespeicherten Kontexts nach Kategorie präsentieren |

**Abrufformat bei der Präsentation von gespeichertem Kontext:**

```
# Dein gespeicherter Kontext

## Projekte
  - [Schlüssel]: [Wert] — hinzugefügt [Datum]
  - ...

## Präferenzen
  - [Schlüssel]: [Wert] — hinzugefügt [Datum]
  - ...

## Terminologie
  - [Schlüssel]: [Wert] — hinzugefügt [Datum]
  - ...

[...für jede Kategorie mit Einträgen fortsetzen]
```

### Veraltete Einträge bereinigen

Kontext veraltet. Überprüfe und bereinige gespeicherte Einträge regelmäßig.

**Veraltungsindikatoren:**

| Signal | Aktion |
| --- | --- |
| Projekt als abgeschlossen oder abgebrochen markiert | Archivieren — als inaktiv ablegen, aber für historische Referenz behalten |
| Kontext durch neuere Informationen widerlegt | Auf aktuellen Stand aktualisieren; Änderung vermerken |
| Eintrag älter als 6 Monate ohne kürzlichen Abruf | Zur Nutzerprüfung markieren — "Ist das noch relevant?" |
| Du sagst ausdrücklich, etwas zu vergessen | Sofort entfernen |

**Bereinigungsprozess:**

1. Wenn Kontext abgerufen wird und potenziell veraltet wirkt, frage: "Ich habe [Kontext] vom [Datum] gespeichert — ist das noch aktuell?"
2. Periodisch (während Wochenreviews oder wenn du um eine Kontextprüfung bittest) Einträge präsentieren, die älter als 3 Monate sind, zur Bestätigung
3. Wenn du aktualisierten Kontext lieferst, der gespeichertem Kontext widerspricht, ersetze den alten Eintrag und bestätige: "[Schlüssel] von [alter Wert] auf [neuer Wert] aktualisiert"

## Anti-Patterns

| Anti-Pattern | Problem | Regel |
| --- | --- | --- |
| **Sensible PII speichern** | Datenschutzrisiko — Passwörter, persönliche Finanzdaten, Gesundheitsinformationen, Ausweisdokumente | VERWEIGERE das Speichern von Passwörtern, Finanzkontodetails, Gesundheitsakten, amtlichen Ausweisnummern oder anderen sensiblen personenbezogenen Daten. Informiere den Nutzer: "Ich kann diese Art sensibler Informationen nicht speichern." |
| **Kontext ableiten** | Genauigkeitsrisiko — Annahmen können falsch sein | Speichere nur Kontext, den du ausdrücklich bereitstellst. Leite niemals Präferenzen, Beziehungen oder Fakten aus Konversationsmustern ab. |
| **Drittdaten speichern** | Datenschutz- und Genauigkeitsrisiko | Speichere keine detaillierten persönlichen Informationen über andere Personen außer grundlegendem beruflichem Kontext (Name, Rolle, Team). Speichere niemals Bewertungen, Leistungsmeinungen oder persönliche Details über Dritte. |
| **Überspeichern** | Rauschen überlagert Signal | Halte Einträge knapp und atomar. Übersteigt die Kontextzusammenfassung 30–40 Einträge, ermutige den Nutzer zum Durchsehen und Bereinigen. |
| **Niemals bereinigen** | Veralteter Kontext führt zu falschen Annahmen | Markiere veraltete Einträge proaktiv zur Prüfung, statt überholten Kontext stillschweigend anzuwenden. |

## Leitplanken

- Erfinde oder leite NIEMALS Nutzerkontext ab — aller gespeicherte Kontext muss ausdrücklich vom Nutzer bereitgestellt werden.
- Speichere NIEMALS sensible personenbezogene Daten (Passwörter, Finanzkonten, Gesundheitsinformationen, amtliche Ausweise).
- Präsentiere abgerufenen Kontext NIEMALS als aktuelles Faktum, ohne das Speicherdatum zu nennen; fordere Bestätigung für Einträge an, die älter als 90 Tage sind.
- Kennzeichne Ausgaben: `[Aus gespeichertem Kontext]`, `[In dieser Sitzung vom Nutzer bereitgestellt]`, `[Vorschlag]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe deiner Kontextzusammenfassung an, um einen formatierten, teilbaren Überblick zu erhalten.
