---
name: de-job-description
description: Schreibt klare, inklusive Stellenbeschreibungen mit Levelling-Logik und Konformität zur EU-Entgelttransparenzrichtlinie. Verwende ihn, wenn du eine neue Rolle erstellst, eine bestehende Stellenbeschreibung auffrischst oder Ausschreibungen auf Verzerrungen und Compliance prüfst. Auslösen mit "Stellenbeschreibung schreiben für", "Stellenausschreibung erstellen", "diese Ausschreibung aktualisieren".
---

# Stellenbeschreibung-Skill

Schreibe, prüfe und auditiere Stellenbeschreibungen — Rollendefinition, Anforderungskalibrierung, inklusive Sprache, Job-Levelling und Konformität zur EU-Entgelttransparenzrichtlinie. Organisationsspezifische Details kommen aus deinen HR-Systemen, companyRAG-Sammlungen oder hochgeladenen Dateien.

> **Hinweis:** Dieser Skill unterstützt HR-Workflows, stellt jedoch keine arbeitsrechtliche Beratung dar. Lass alle Ergebnisse von qualifizierten HR-Fachleuten und arbeitsrechtlichem Beistand in der jeweiligen Jurisdiktion prüfen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **ATS über MCP** (z. B. Greenhouse, Lever) | Bestehende Ausschreibungen, Rollenvorlagen, Pipeline-Status, Hiring-Manager-Notizen |
| **HRIS über MCP** | Job-Architektur, Levelling-Framework, Vergütungsbänder, Org-Struktur |
| **companyRAG-Sammlungen / Datei-Upload** | Job-Architektur-Dokumente, Werte-Statements, bestehende Stellenbeschreibungen, Hiring-Manager-Briefings |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## EU-AI-Act-Compliance-Grenze

KI-gestützte Rekrutierung, einschließlich KI-generierter Stellenbeschreibungen, die in Recruiting-Pipelines verwendet werden, kann je nach Einsatz in automatisierten Screening- oder Matching-Systemen Pflichten des EU AI Act (Anhang III, Kategorie 4) berühren. Dieser Skill erzeugt Stellenbeschreibungs-TEXT zur menschlichen Prüfung und Veröffentlichung — er screent, matcht oder bewertet keine Kandidat:innen. Alle Ergebnisse müssen vor der Veröffentlichung von einem Menschen geprüft und freigegeben werden.

## Stellenbeschreibungs-Workflow

### Schritt 1: Rollendefinition

Sammle und bestätige vor dem Schreiben diese Eingaben:

```
ROLLENDEFINITION
================
Stellentitel:         [Arbeitstitel — wird noch verfeinert]
Abteilung / Team:     [organisatorische Einheit]
Berichtet an:         [Titel der direkten Führungskraft]
Standort:             [Büro / Hybrid / Remote — bei Remote-Rollen Jurisdiktionen angeben]
Beschäftigungsart:    [unbefristet / befristet / freiberuflich / Praktikum]
Job-Level:            [aus der Job-Architektur, falls vorhanden]
Headcount-Kontext:    [neue Rolle / Nachbesetzung / Erweiterung]
Geschäftsbedarf:      [warum diese Rolle existiert — das Problem, das sie löst, oder das Ergebnis, das sie ermöglicht]
Zusammenarbeit:       [wichtige interne und externe Stakeholder, mit denen die Rolle arbeitet]
```

Wenn die Organisation eine Job-Architektur oder ein Levelling-Framework hat, verankere die Rolle darin, bevor du schreibst. Existiert kein Framework, ziehe den design-learning-plan-Skill für die Gestaltung eines Karriere-Frameworks heran oder lege die Level-Erwartungen mit der Hiring-Manager:in fest.

### Schritt 2: Anforderungskalibrierung

Die wirkungsvollste Qualitätsentscheidung in einer Stellenbeschreibung ist die Unterscheidung zwischen Anforderungen und Präferenzen. Überhöhte Anforderungen verringern systematisch die Vielfalt der Bewerbenden und schließen qualifizierte Kandidat:innen aus.

#### Framework: Anforderungen vs. Präferenzen

| Kategorie | Definition | Test |
| --- | --- | --- |
| **Must-Have (Anforderungen)** | Fähigkeiten, ohne die die Person die Rolle ab Tag eins nicht ausüben kann — auch mit Onboarding-Unterstützung | Würdest du eine ansonsten herausragende Person ablehnen, der dies fehlt? Wenn nein, ist es keine Anforderung. |
| **Nice-to-Have (Präferenzen)** | Fähigkeiten, die das Einarbeiten beschleunigen oder Mehrwert bringen, aber im Job erlernbar sind | Könnte eine starke Person dies innerhalb von 6–12 Monaten in der Rolle lernen? Wenn ja, ist es eine Präferenz. |
| **Bonus (Differenzierer)** | Fähigkeiten, die außergewöhnlich wären, aber nicht erwartet werden | Würdest du aktiv danach suchen, oder schätzt du es nur, wenn es zufällig vorhanden ist? |

#### Kalibrierungsprozess

1. Liste alles auf, was die Hiring-Manager:in zunächst als „erforderlich" benennt
2. Wende den Must-Have-Test auf jeden Punkt an
3. Verschiebe Punkte, die den Test nicht bestehen, zu Nice-to-Have oder Bonus
4. Begrenze Must-Haves auf 5–7 Punkte — Forschung zeigt konsistent, dass längere Anforderungslisten unterrepräsentierte Bewerbende überproportional abschrecken
5. Formuliere Must-Haves als Ergebnisse oder Fähigkeiten, nicht als Qualifikationen — „Erfahrung im Design verteilter Systeme" statt „5+ Jahre Backend-Engineering"

#### Anti-Pattern: Jahre an Erfahrung

Vermeide es, Erfahrungsjahre als Anforderung anzugeben. Erfahrungsjahre sind ein Proxy, keine Kompetenz. Probleme mit jahresbasierten Anforderungen:

- Sie benachteiligen Quereinsteigende, Autodidakt:innen und Personen, die schneller als der Durchschnitt vorangekommen sind
- Sie erzeugen rechtliches Risiko in Jurisdiktionen mit Altersdiskriminierungsschutz (was die EU unter Richtlinie 2000/78/EG einschließt)
- Sie korrelieren jenseits der ersten Jahre in einem Bereich nicht gut mit Fähigkeit

Stattdessen: Beschreibe das erwartete FÄHIGKEITSNIVEAU. „Fähig, eigenständig Microservice-Architekturen zu entwerfen und umzusetzen" ist informativer und inklusiver als „7+ Jahre Backend-Entwicklung".

Besteht die Hiring-Manager:in auf Erfahrungsjahren, formuliere es als Richtwert: „Typischerweise sind X+ Jahre einschlägiger Erfahrung erforderlich" statt als harte Anforderung.

### Schritt 3: Prüfung auf inklusive Sprache

Wende diese Prüfungen vor der Veröffentlichung auf den gesamten Text der Stellenbeschreibung an.

#### Sprach-Audit-Checkliste

| Prüfung | Worauf zu achten ist | Maßnahme |
| --- | --- | --- |
| **Geschlechtsspezifische Sprache** | „Er/sie", geschlechtsspezifische Nomen („Vorsitzender", „Mannstärke"), Pronomen, die auf ein Geschlecht festgelegt sind | Geschlechtsneutrale Alternativen verwenden („sie", „Vorsitz", „Belegschaft") |
| **Aggressive/kompetitive Formulierungen** | „Ziele zerschmettern", „den Markt dominieren", „Rockstar", „Ninja", „Killerinstinkt" | Durch leistungsorientierte Sprache ersetzen („Ergebnisse liefern", „Wachstum vorantreiben", „leistungsstark") |
| **Unnötige Superlative** | „Weltklasse", „Best-in-Class", „Top-Tier" ohne Definition | Entfernen oder durch konkrete Erwartungen ersetzen |
| **Ausschließender Jargon** | Interne Akronyme, nicht erklärte Nischenbegriffe, kulturspezifische Bezüge | Begriffe definieren oder einfache Sprache verwenden |
| **Annahmen über Fähigkeiten** | „Muss 50 kg heben können", wenn nicht wirklich erforderlich; „sauberer Führerschein", wenn für die Rolle nicht nötig | Entfernen, außer es ist für die Funktion echt erforderlich und als wesentliche Aufgabe dokumentiert |
| **Qualifikations-Inflation** | Verlangen eines Abschlusses, wenn die Rolle auch ohne ausführbar ist; Verlangen bestimmter Institutionen oder Zertifikate | Qualifikationen nur verlangen, wenn rechtlich notwendig (z. B. reglementierte Berufe) oder echt wesentlich; sonst gleichwertige Erfahrung akzeptieren |

#### Inklusive Formulierungsmuster

| Statt | Verwende |
| --- | --- |
| „Muss X Jahre in Y haben" | „Nachgewiesene Fähigkeit, [Ergebnis] in [Bereich] zu erzielen" |
| „Selbststarter, der im Chaos aufblüht" | „Komfortabel im autonomen Arbeiten und im Anpassen an sich wandelnde Prioritäten" |
| „Culture Fit" | „Im Einklang mit [konkret benannten Werten]" |
| „Muttersprachliches Englisch" | „Verhandlungssicheres Englisch" (oder das tatsächlich erforderliche Sprachniveau) |
| „Junges, dynamisches Team" | „Kollaboratives Team" (Altersbezüge erzeugen Diskriminierungsrisiko) |
| „Wettbewerbsfähiges Gehalt" | Konkrete Gehaltsspanne (siehe Abschnitt Entgelttransparenz) |

### Schritt 4: Struktur der Stellenbeschreibung

#### Standard-Vorlage Stellenbeschreibung

```
[STELLENTITEL]
[Abteilung] · [Standort] · [Beschäftigungsart]

ÜBER DIE ROLLE
[2–3 Sätze: was diese Rolle tut, warum sie wichtig ist und welche Wirkung die Person hat.
Mit Ergebnissen beginnen, nicht mit Tätigkeiten. Beantworte: „Warum würde eine talentierte Person diesen Job wollen?"]

WAS DU TUN WIRST
[5–8 Kernaufgaben. Jede mit einem Aktionsverb beginnen.
Nach Wichtigkeit für die Rolle ordnen, nicht nach Häufigkeit.
Wo möglich als Ergebnisse formulieren: „X vorantreiben" statt „An Meetings über X teilnehmen".]

- [Aufgabe 1 — wirkungsvollste Tätigkeit]
- [Aufgabe 2]
- [Aufgabe 3]
- [Aufgabe 4]
- [Aufgabe 5]

WAS WIR SUCHEN
[Must-Haves — maximal 5–7 Punkte. Als Fähigkeiten formulieren, nicht als Qualifikationen.]

- [Anforderung 1 — fähigkeitsbasiert]
- [Anforderung 2]
- [Anforderung 3]

NICE TO HAVE
[Präferenzen — klar von den Anforderungen getrennt]

- [Präferenz 1]
- [Präferenz 2]

WAS WIR BIETEN
[Vergütungsspanne, Benefits, Entwicklungsmöglichkeiten, Arbeitsmodell.
Sei konkret — vage Versprechen („attraktives Paket") signalisieren fehlende Transparenz.]

- Gehaltsspanne: [Spanne in lokaler Währung, gemäß Entgelttransparenzanforderungen]
- [Benefit 1]
- [Benefit 2]
- [Arbeitsmodell: Details zu Büro/Hybrid/Remote]

CHANCENGLEICHHEIT
[Statement der Organisation zur Chancengleichheit.
Sollte konkret und echt sein, nicht Standardfloskel.]

WIE DU DICH BEWIRBST
[Bewerbungsprozess, was einzureichen ist, Erwartungen zum Zeitplan]
```

### Schritt 5: Integration des Job-Levelling

Wenn die Organisation eine Job-Architektur oder ein Levelling-Framework hat, richte die Stellenbeschreibung daran aus:

| Element der Stellenbeschreibung | Levelling-Ausrichtung |
| --- | --- |
| **Stellentitel** | Bildet ein konkretes Level in der Job-Architektur ab (z. B. IC3, M2, Senior Engineer) |
| **Aufgaben** | Spiegeln Umfang, Komplexität und Autonomie wider, die auf diesem Level erwartet werden |
| **Anforderungen** | Auf das Level kalibriert — nicht am Level darüber überindexiert |
| **Vergütung** | Innerhalb des für dieses Level definierten Bands (siehe Abschnitt Entgelttransparenz) |
| **Entwicklungspfad** | Wohin die Rolle führt — das nächste Level im Karriere-Framework |

Wenn keine Levelling-Information vorliegt, bitte die Hiring-Manager:in zu beschreiben:

- Den Spielraum für eigenständige Entscheidungen
- Die Komplexität der Probleme, die die Rolle lösen soll
- Ob die Rolle Personen, Projekte oder weder noch führt
- Wer die Peers der Rolle sind (zur Kalibrierung)

### Schritt 6: Konformität zur EU-Entgelttransparenzrichtlinie

Die EU-Entgelttransparenzrichtlinie (Richtlinie (EU) 2023/970) führt Anforderungen an die Entgelttransparenz in Stellenausschreibungen ein. Die Mitgliedstaaten müssen die Richtlinie bis zum 7. Juni 2026 umsetzen. Zentrale Anforderungen an Stellenbeschreibungen:

#### Entgelttransparenz vor der Bewerbung (Artikel 5)

- Bewerbende haben das Recht, Informationen über das anfängliche Entgeltniveau oder die Entgeltspanne der Stelle zu erhalten
- Diese Information muss in der Stellenausschreibung oder vor dem Vorstellungsgespräch bereitgestellt werden, ohne dass die Person sie anfragen muss
- Der Arbeitgeber darf Bewerbende nicht nach ihrer Entgelthistorie in aktuellen oder früheren Beschäftigungsverhältnissen fragen

#### Compliance-Checkliste für Stellenbeschreibungen

| Anforderung | So erfüllst du sie in der Stellenbeschreibung |
| --- | --- |
| **Offenlegung der Entgeltspanne** | Gehaltsspanne (oder Einstiegsgehalt) in die Ausschreibung aufnehmen. Aus der Vergütungsstruktur der Organisation für das Job-Level ableiten. |
| **Keine Abfrage der Entgelthistorie** | Keine Fragen zu aktuellem oder früherem Gehalt im Bewerbungsprozess aufnehmen. Solche Felder aus Bewerbungsformularen entfernen. |
| **Geschlechtsneutrale Stellenklassifizierung** | Sicherstellen, dass Titel und Klassifizierung geschlechtsneutral und an objektiven Kriterien orientiert sind |
| **Gleicher Lohn für gleiche Arbeit** | Prüfen, dass die angebotene Spanne mit dem konsistent ist, was bestehende Mitarbeitende auf gleichem Level und in vergleichbaren Rollen erhalten |

#### Umsetzungshinweise

- Die Richtlinie erfordert die Umsetzung durch die Mitgliedstaaten — konkrete Anforderungen können variieren. Beobachte die Umsetzung in den Jurisdiktionen, in denen die Rolle ausgeschrieben wird.
- Schon vor der vollständigen Umsetzung haben mehrere Mitgliedstaaten nationale Entgelttransparenzanforderungen (z. B. Deutschlands Entgelttransparenzgesetz, das individuelle Auskunftsrechte für Beschäftigte in Organisationen mit 200+ Mitarbeitenden vorsieht).
- Für die Analyse von Vergütungsbändern nutze den check-compensation-Skill.

## Audit-Modus für Stellenbeschreibungen

Wenn du eine bestehende Stellenbeschreibung prüfst, statt eine neue zu schreiben:

### Audit-Bewertungsframework

Bewerte jede Dimension auf einer Skala von 1–5:

| Dimension | 1 (Schlecht) | 3 (Ausreichend) | 5 (Exzellent) |
| --- | --- | --- | --- |
| **Klarheit** | Vage Aufgaben, unklare Erwartungen | Aufgaben gelistet, aber generisch | Konkrete Ergebnisse, klarer Umfang, wo sinnvoll messbar |
| **Anforderungskalibrierung** | Überhöhte Anforderungen, keine Must/Nice-Unterscheidung | Etwas Unterscheidung, aber weiterhin überindexiert | Klare Must/Nice-Trennung, fähigkeitsbasiert, 5–7 Must-Haves |
| **Inklusivität** | Geschlechtsspezifische Sprache, Qualifikations-Inflation, ausschließende Formulierungen | Überwiegend neutral, aber einige Probleme | Bewusst inklusiv, fähigkeitsbasiert, keine unnötigen Hürden |
| **Levelling-Genauigkeit** | Unpassende Level-Signale (zu senior oder zu junior für den tatsächlichen Umfang) | Generell ausgerichtet, aber einige Inkonsistenzen | Präzise auf das Job-Level kalibriert |
| **Entgelttransparenz** | Keine Entgeltinformation | Vage („wettbewerbsfähig") | Konkrete Spanne enthalten, konform mit geltenden Anforderungen |
| **Arbeitgeberwert** | Keine Information über den Wert der Rolle oder den Team-Kontext | Generische Unternehmensbeschreibung | Konkrete, überzeugende Darstellung, warum diese Rolle zählt und was das Team attraktiv macht |

### Audit-Ausgabevorlage

```
AUDIT-BERICHT STELLENBESCHREIBUNG
=================================
Rolle:           [Titel]
Auditiert von:   [KI-Audit — erfordert HR-Prüfung]
Datum:           [Datum]

BEWERTUNGEN:
  Klarheit:               [1-5] — [kurze Begründung]
  Anforderungen:          [1-5] — [kurze Begründung]
  Inklusivität:           [1-5] — [kurze Begründung]
  Levelling:              [1-5] — [kurze Begründung]
  Entgelttransparenz:     [1-5] — [kurze Begründung]
  Arbeitgeberwert:        [1-5] — [kurze Begründung]
  Gesamt:                 [Durchschnitt]

GEFUNDENE PROBLEME:
  [Priorität: Hoch/Mittel/Niedrig] [Problembeschreibung] — [konkret zitierter Text] — [empfohlene Korrektur]

ÜBERARBEITETER TEXT (wo zutreffend):
  [Vorher]: "[Originaltext]"
  [Nachher]: "[verbesserter Text]"
```

## Leitplanken

- Erzeuge niemals Vergütungsdaten, Gehaltsspannen oder Markt-Benchmarks. Liegt keine Entgeltinformation vor, kennzeichne sie als erforderliche Eingabe.
- Erzeuge niemals organisationsspezifische Kultur-Statements, Werte oder Employer-Brand-Botschaften. Diese müssen von der Organisation kommen.
- Zitiere im Audit-Modus den konkret bewerteten Text, bevor du Änderungen vorschlägst. Kennzeichne Jurisdiktionsabhängigkeiten bei Entgelttransparenz- und Antidiskriminierungsanforderungen.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Rollenanforderungen]`, `[Aus Job-Architektur]`, `[Stellenbeschreibungs-Methodik]` oder `[KI-Vorschlag — mit HR prüfen]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, verteilfertiges Dokument zu erhalten.
