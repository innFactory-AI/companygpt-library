---
name: de-compensation
description: Prüft Vergütungsentscheidungen gegen interne Bänder und die Anforderungen der EU-Entgelttransparenzrichtlinie. Verwende ihn, wenn du ein Angebot machst, eine Gehaltsanpassung bearbeitest oder die Entgeltgerechtigkeit auditierst. Auslösen mit "Vergütung prüfen für", "ist dieses Angebot im Band", "Pay-Equity-Review".
---

# Vergütung-Skill

Prüfe Vergütungsentscheidungen gegen interne Gehaltsbänder, berechne Compa-Ratios, auditiere Pay Equity und bewerte die Readiness für die EU-Entgelttransparenzrichtlinie. Alle Vergütungsdaten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Hinweis zu Arbeitsrecht und Regulatorik

Vergütungsentscheidungen berühren Arbeitsrecht, Antidiskriminierungsvorschriften und die entstehenden Anforderungen an die Entgelttransparenz in den EU-Mitgliedstaaten. Alle Ausgaben sind Entscheidungsunterstützung für Vergütungsverantwortliche — sie stellen keine Rechts- oder Finanzberatung dar.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **HRIS über MCP** (z. B. Personio, Workday, BambooHR) | Aktuelle Vergütung nach Komponenten, Mitarbeiterstammdaten, Rolle, Level, Tenure, Standort, Demografiedaten |
| **Vergütungs-Benchmark-Quellen über MCP** (z. B. Gehaltsumfragen, Markt-Datenanbieter) | Marktdaten und Survey-Perzentile, sofern angebunden und freigegeben |
| **companyRAG / Datei-Upload** | Gehaltsband-Struktur, Job-Architektur, Vergütungs-Framework, Governance-Richtlinien |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Vergütungsprüfungs-Workflow

Befolge diese Schritte bei jeder Anfrage zur Vergütungsprüfung. Passe die Tiefe an den Kontext an — ein Routine-Check "Neueinstellung im Band" braucht weniger Rigorosität als ein vollständiges Equity-Audit.

### Schritt 1: Vergütungsdaten sammeln

Sammle vor der Analyse die relevanten Datenpunkte:

**Für eine individuelle Vergütungsentscheidung (Angebot, Anpassung, Beförderung):**

| Datenpunkt | Quelle | Erforderlich? |
| --- | --- | --- |
| Rollenbezeichnung und Job-Level | Job-Architektur / Nutzereingabe | Ja |
| Vorgeschlagene Vergütung (Fix, variabel, Equity) | Nutzereingabe | Ja |
| Internes Gehaltsband für Rolle und Level | Vergütungs-Framework / Nutzereingabe | Ja |
| Aktuelle Vergütung (bei Anpassungen) | HRIS / Nutzereingabe | Bei Anpassung |
| Relevante Marktdaten / Survey-Perzentil | Gehaltsumfrage / Nutzereingabe | Empfohlen |
| Standort / Geografiezone | Nutzereingabe | Ja |
| Erfahrungslevel relativ zu den Rollenanforderungen | Nutzereingabe | Empfohlen |

**Für ein Team- oder Organisations-Equity-Audit:**

| Datenpunkt | Quelle | Erforderlich? |
| --- | --- | --- |
| Mitarbeiterliste mit Rolle, Level, Tenure, Standort | HRIS / Nutzereingabe | Ja |
| Aktuelle Vergütung nach Komponente (Fix, variabel, Equity) | HRIS / Nutzereingabe | Ja |
| Gehaltsband-Struktur | Vergütungs-Framework / Nutzereingabe | Ja |
| Demografiedaten für die Equity-Analyse | HRIS / Nutzereingabe | Für Equity-Audit |
| Jüngste Vergütungsmaßnahmen (Erhöhungen, Beförderungen) | HRIS / Nutzereingabe | Empfohlen |

Wenn wichtige Daten fehlen, kennzeichne dies explizit: [Daten benötigt — Nutzer fragen]. Fahre nicht mit Annahmen über Bandstrukturen oder Vergütungsbeträge fort.

### Schritt 2: Band-Alignment-Check

Bewerte für die vorgeschlagene oder aktuelle Vergütung das Alignment gegen das interne Band:

```
BAND-ALIGNMENT-CHECK:
  Rolle:          [Titel und Level]
  Standortzone:   [Geografiezone]
  Band-Minimum:   [aus Vergütungs-Framework]
  Band-Midpoint:  [aus Vergütungs-Framework]
  Band-Maximum:   [aus Vergütungs-Framework]
  Vorgeschlagen:  [Betrag]

  Position im Band: [unter Min / unteres Drittel / Mittelbereich / oberes Drittel / über Max]
  Band-Penetration: [Prozent — (vorgeschlagen - Min) / (Max - Min) × 100]

  Bewertung:      [Im Band / Unter Band / Über Band]
  Flag:           [Keine / Begründung erforderlich / Freigabe erforderlich]
```

**Interpretation des Band-Alignments:**

| Position | Typische Interpretation | Maßnahme |
| --- | --- | --- |
| Unter Band-Minimum | Unter Markt oder fehl-gelevelt | Untersuchen — ggf. Anpassung oder Re-Leveling nötig |
| Unteres Drittel (0–33 %) | Neu in der Rolle oder im Aufbau | Angemessen für Neueinstellungen oder kürzlich Beförderte, die in die Rolle hineinwachsen |
| Mittelbereich (34–66 %) | Voll leistungsfähig auf Level | Standardpositionierung für erfahrene, voll leistungsfähige Mitarbeitende |
| Oberes Drittel (67–100 %) | Senior in der Rolle / High Performer | Angemessen für langjährige, wirkungsstarke Mitarbeitende — Beförderungsreife beobachten |
| Über Band-Maximum | Über Markt oder fehl-gelevelt | Review erforderlich — Re-Leveling, Rollenerweiterung oder Aktualisierung der Marktdaten erwägen |

### Schritt 3: Compa-Ratio-Analyse

Berechne die Compa-Ratio für die Einzel- oder Gruppenanalyse:

```
COMPA-RATIO:
  Individuell:    Tatsächliches Fixgehalt / Band-Midpoint × 100
  Zielbereich:    80–120 % (typisch — an die Policy deiner Organisation anpassen)

  Ergebnis:       [berechnet] %
  Bewertung:      [Unter Ziel / Im Ziel / Über Ziel]
```

**Für die Team- oder Gruppenanalyse:**

| Kennzahl | Berechnung | Was sie zeigt |
| --- | --- | --- |
| Durchschnittliche Compa-Ratio | Mittelwert der individuellen Compa-Ratios | Gesamtpositionierung des Teams ggü. Midpoint |
| Compa-Ratio-Spanne | Min bis Max innerhalb der Gruppe | Streuung der Vergütung innerhalb desselben Levels |
| Compa-Ratio nach Tenure | Segmentiert nach Jahren in der Rolle | Ob Tenure mit der Bandposition korreliert (erwartet) |
| Compa-Ratio nach Demografie | Segmentiert nach geschützten Merkmalen | Mögliche Pay-Equity-Bedenken (siehe Schritt 4) |

Eine gesunde Compa-Ratio-Verteilung gruppiert sich um 95–105 % mit gewollter Variation nach Erfahrung, Leistung und Tenure. Ausreißer in beide Richtungen rechtfertigen eine Untersuchung.

### Schritt 4: Pay-Equity-Check

Systematische Bewertung von Pay-Equity-Risiken. Dies ist eine SCREENING-Methodik — bestätigte Equity-Probleme erfordern eine statistische Analyse durch qualifizierte Vergütungsanalysten und eine Prüfung durch arbeitsrechtliche Beratung.

**Equity-Screen für eine Einzelentscheidung:**

Prüfe bei der Bewertung eines Angebots oder einer Anpassung:

1. Interne Equity: Wie verhält sich dies zu anderen in derselben Rolle, demselben Level und derselben Standortzone? Gibt es unerklärte Unterschiede?
2. Kohortenvergleich: Wo fällt dies unter Mitarbeitenden mit demselben Level und Tenure-Band hin? Ist die Position durch Leistung, Erfahrung oder Scope-Unterschiede gerechtfertigt?
3. Historisches Muster: Gibt es für dieses spezifische Team oder diese Führungskraft ein Muster, wie Angebote oder Anpassungen über Demografiegruppen hinweg verlaufen?

**Methodik für ein Organisations-Equity-Audit:**

1. Definiere den Audit-Scope: welche Rollen, Level, Standorte und welcher Zeitraum
2. Gruppiere Mitarbeitende in vergleichbare Kohorten (gleiche Rollenfamilie + Level + Standortzone)
3. Berechne die Compa-Ratio-Verteilungen innerhalb jeder Kohorte
4. Segmentiere nach verfügbaren Demografiedimensionen (Geschlecht, Ethnie, Alter, Behinderungsstatus — gemäß lokaler Datenverfügbarkeit und Datenschutzanforderungen)
5. Markiere Kohorten, in denen sich die mediane Compa-Ratio um mehr als 5 Prozentpunkte zwischen Demografiegruppen unterscheidet
6. Bewerte bei markierten Kohorten, ob legitime Faktoren (Tenure, Leistungsbewertung, Scope-Unterschiede) die Lücke erklären
7. Verbleibende unerklärte Lücken erfordern eine tiefere statistische Analyse (regressionsbasiert) und eine rechtliche Prüfung

> **CRITICAL (kritisch)**: Eine Pay-Equity-Analyse mit Demografiedaten hat erhebliche Implikationen für Datenschutz und Datensicherheit. Beachte die Anforderungen an die Datenverarbeitung. In manchen Jurisdiktionen kann vor der Durchführung von Equity-Analysen eine Konsultation des Betriebsrats oder der Arbeitnehmervertretung erforderlich sein.

### Schritt 5: Awareness zur EU-Entgelttransparenzrichtlinie

Die EU-Entgelttransparenzrichtlinie (2023/970) führt Anforderungen ein, die die Mitgliedstaaten bis Juni 2026 in nationales Recht umsetzen müssen. Die Anforderungen variieren je nach Organisationsgröße und nationaler Umsetzung.

**Awareness-Checkliste — bewerte die Readiness für:**

| Anforderungsbereich | Wichtige Pflichten | Readiness-Frage |
| --- | --- | --- |
| Offenlegung von Gehaltsbändern | Gehaltsspanne in Stellenausschreibungen oder vor dem Interview angeben | Sind Gehaltsbänder für alle Rollen definiert und veröffentlichungsfähig? |
| Auskunftsrecht | Mitarbeitende können das Durchschnittsentgelt nach Geschlecht für ihre Kategorie anfragen | Kannst du diese Daten auf Anfrage erzeugen? |
| Berichterstattung zum Pay Gap | Organisationen über Schwellenwert berichten Daten zum geschlechtsspezifischen Pay Gap | Hast du die Dateninfrastruktur für die jährliche Berichterstattung? |
| Gemeinsame Bewertung | Bei Gap > 5 % und nicht gerechtfertigt: gemeinsame Bewertung mit Arbeitnehmervertretern durchführen | Gibt es einen Prozess für gemeinsame Bewertungen? |
| Verbot der Gehaltshistorie | Kandidaten dürfen nicht nach aktueller oder früherer Vergütung gefragt werden | Sind Interview-Prozesse und Angebots-Workflows angepasst? |

> **CRITICAL (kritisch)**: Diese Checkliste vermittelt AWARENESS (Bewusstsein) für die Themen der Richtlinie. Die nationale Umsetzung kann in Scope, Schwellenwerten und Umsetzungsfristen erheblich abweichen. Verifiziere spezifische Anforderungen mit arbeitsrechtlicher Beratung in jedem betroffenen Mitgliedstaat.

## Ausgabevorlage: Vergütungsprüfung

```
# Vergütungsprüfung — [Rolle / Mitarbeiter-ID / Team]
Datum: [Datum]
Prüfer: [Name]
Prüfungstyp: [Angebot / Anpassung / Beförderung / Equity-Audit]

## Zusammenfassung
  [2-3 Sätze: Was wurde geprüft, wichtigster Befund, empfohlene Maßnahme]

## Band-Alignment
  [Band-Alignment-Check-Ausgabe aus Schritt 2]

## Compa-Ratio-Analyse
  [Compa-Ratio-Ausgabe aus Schritt 3]

## Pay-Equity-Screen
  [Equity-Screen-Befunde aus Schritt 4]
  Risikolevel: [Niedrig / Mittel / Hoch / Spezialistenprüfung erforderlich]

## EU-Entgelttransparenz-Readiness (falls zutreffend)
  [Checklisten-Status aus Schritt 5]

## Empfehlung
  [Strukturierte Empfehlung — unverändert genehmigen / mit Anpassung genehmigen / eskalieren]
  Begründung: [evidenzbasierte Rationale]
  Freigabe-Level: [Manager / Vergütungsteam / CHRO — gemäß deiner Governance-Policy]

## Flags und nächste Schritte
  - [Punkte, die Follow-up, Datenlücken oder Spezialistenprüfung erfordern]
```

## CUSTOMIZE: An deine Organisation anpassen

Dieser Skill verwendet generische Bandstrukturen und Schwellenwerte. Um ihn organisationsspezifisch zu machen:

1. Lade deine Gehaltsband-Struktur in eine companyRAG-Sammlung hoch — der Skill referenziert dann deine Bänder, statt jedes Mal zu fragen
2. Definiere deinen Compa-Ratio-Zielbereich, falls er vom Standard 80–120 % abweicht
3. Lege deine Freigabe-Schwellenwerte fest — welche Bandpositionen oder Compa-Ratios eine Eskalation erfordern
4. Ergänze deine Geografiezonen und wie sie auf Band-Differentiale abbilden
5. Füge deine Equity-Audit-Kadenz und -Methodik hinzu, falls du einen etablierten Prozess hast

## Leitplanken

- Erzeuge niemals Gehaltsbeträge, Markt-Benchmarks oder Daten aus Vergütungsumfragen. Alle Vergütungszahlen müssen aus den Daten des Nutzers stammen.
- Erkläre niemals, dass eine Vergütungsentscheidung "compliant" oder "legal" ist. Die Compliance-Feststellung erfordert rechtliche Beratung — Flag: "Mit arbeitsrechtlicher Beratung in [Jurisdiktion] verifizieren."
- Triff niemals individuelle Pay-Equity-Feststellungen. Eine Equity-Analyse erfordert statistische Methodik und rechtliche Prüfung jenseits des Scopes dieses Skills.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Vergütungsdaten]`, `[Framework-Methodik]` oder `[KI-Analyse — mit Vergütungsteam verifizieren]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um eine formatierte, sofort teilbare Prüfung zu erhalten.
