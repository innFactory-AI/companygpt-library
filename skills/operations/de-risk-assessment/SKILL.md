---
name: de-risk-assessment
description: Operative Risikobewertung mit Schweregrad-x-Eintrittswahrscheinlichkeit-Matrix, Maßnahmenplanung und Pflege des Risikoregisters. Verwende ihn, wenn du Risiken für ein Projekt bewertest, eine periodische Risikoprüfung durchführst oder ein Risikoregister aufbaust. Auslösen mit "Risiko bewerten für", "Risikoanalyse", "was könnte schiefgehen bei".
---

# Risikobewertung-Skill

Identifiziere, bewerte und entschärfe operative Risiken. Der Skill erzeugt Risikoregister, Risikomatrizen, Maßnahmenpläne und periodische Review-Berichte. Die zu bewertenden Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt- / Issue-Tracker über MCP** (z. B. Jira, Asana, Monday) | Projektumfang, Abhängigkeiten, offene Issues, historische Incidents |
| **Incident- / Monitoring-Tools über MCP** (z. B. PagerDuty, Sentry) | Vergangene Incidents, Near-Misses, Post-Mortems für die historische Auswertung |
| **companyRAG-Sammlungen / Datei-Upload** | Prozessbeschreibungen, Verträge, Pre-Mortem-Notizen, bestehende Risikoregister |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Risikoidentifikation

### Identifikationstechniken

Nutze mehrere Ansätze, um ein umfassendes Risikoinventar aufzubauen — keine einzelne Technik erfasst alle Risiken:

| Technik | Funktionsweise | Am besten geeignet für |
| --- | --- | --- |
| **Strukturiertes Brainstorming** | Gehe jeden Prozessschritt, jeden Entscheidungspunkt, jede Abhängigkeit und jeden externen Faktor durch und frage "was könnte hier schiefgehen?" | Bekannte Prozesse mit identifizierbaren Fehlerquellen |
| **Pre-Mortem** | Nimm an, das Projekt/die Initiative sei gescheitert; arbeite rückwärts, um die Ursachen zu identifizieren | Projekte und Initiativen — bringt Risiken zutage, die Menschen ungern ansprechen |
| **Historische Auswertung** | Untersuche vergangene Incidents, Near-Misses und Post-Mortems auf wiederkehrende Muster | Operative Prozesse mit Incident-Historie |
| **Abhängigkeits-Mapping** | Verfolge alle Abhängigkeiten (Personen, Systeme, Lieferanten, Daten, Freigaben) und bewerte jede auf ihr Ausfallpotenzial | Komplexe Prozesse mit vielen externen Abhängigkeiten |
| **Annahmen-Test** | Liste alle dem Plan zugrunde liegenden Annahmen auf; jede Annahme, die sich als falsch erweisen könnte, ist ein Risiko | Strategische Initiativen und Business Cases |
| **PESTLE-Scan** | Prüfe politische, ökonomische, soziale, technologische, rechtliche und ökologische Faktoren | Bewertung der externen Risikolandschaft |

### Standard für Risikobeschreibungen

Jedes Risiko muss als spezifisches Ereignis mit Ursache und Folge beschrieben werden — nicht als vage Sorge:

**Muster**: "Aufgrund von [Ursache] kann [Ereignis] eintreten, was zu [Folge] führt."

| Qualität | Schlechtes Beispiel | Gutes Beispiel |
| --- | --- | --- |
| **Spezifisch** | "Technologierisiko" | "Aufgrund des Single-Region-Hostings des Anbieters kann ein regionaler Cloud-Ausfall eintreten, was zu 4–8 Stunden Nichtverfügbarkeit des Dienstes führt" |
| **Ursachenbezogen** | "Wir könnten Daten verlieren" | "Aufgrund fehlender automatisierter Backup-Verifikation kann ein unbemerktes Backup-Versagen eintreten, was zu Datenverlust von bis zu 24 Stunden führt" |
| **Folgenbezogen** | "Lieferkettenprobleme" | "Aufgrund der Single-Source-Abhängigkeit bei Komponente X kann ein Produktionsstopp beim Lieferanten eintreten, was zu 6 Wochen Lieferverzug bei Kundenaufträgen führt" |

## Risiko-Scoring

### Schweregrad-Skala

Definiere den Schweregrad in Begriffen, die für die Organisation aussagekräftig sind:

| Stufe | Label | Definitionsvorlage |
| --- | --- | --- |
| 5 | **Kritisch** | Bedroht die Existenzfähigkeit der Organisation, schwere regulatorische Sanktion oder irreversibler Schaden |
| 4 | **Schwerwiegend** | Erheblicher finanzieller Verlust, Reputationsschaden mit Auswirkung auf Kundenbeziehungen oder langanhaltende Betriebsstörung |
| 3 | **Mittel** | Materielle Auswirkung mit Managementaufmerksamkeit, temporäre Betriebsbeeinträchtigung oder eingegrenzter finanzieller Verlust |
| 2 | **Gering** | Begrenzte Auswirkung, im Normalbetrieb beherrschbar, kleinere Verzögerungen oder geringe finanzielle Abweichung |
| 1 | **Vernachlässigbar** | Minimale Auswirkung, leicht aufzufangen, kein bleibender Effekt |

Diese Definitionen sind Vorlagen — die Organisation sollte sie mit konkreten Schwellenwerten kalibrieren (z. B. sollte "erheblicher finanzieller Verlust" in Geldbeträgen definiert werden, die zur Größenordnung der Organisation passen). Fordere den Nutzer auf, seine Schwellenwerte zu definieren, falls noch nicht festgelegt.

### Eintrittswahrscheinlichkeits-Skala

| Stufe | Label | Definition |
| --- | --- | --- |
| 5 | **Fast sicher** | Tritt voraussichtlich innerhalb des Bewertungszeitraums ein; ist zuvor wiederholt vorgekommen |
| 4 | **Wahrscheinlich** | Wird vermutlich eintreten; ist unter ähnlichen Bedingungen schon vorgekommen |
| 3 | **Möglich** | Könnte eintreten; Bedingungen existieren, aber zusätzliche Faktoren nötig |
| 2 | **Unwahrscheinlich** | Nicht erwartet, aber denkbar; würde ungewöhnliche Umstände erfordern |
| 1 | **Selten** | Höchst unwahrscheinlich; würde außergewöhnliche Umstände erfordern |

### Risikomatrix

Schweregrad × Eintrittswahrscheinlichkeit ergibt einen Risiko-Score:

|  | Selten (1) | Unwahrscheinlich (2) | Möglich (3) | Wahrscheinlich (4) | Fast sicher (5) |
| --- | --- | --- | --- | --- | --- |
| **Kritisch (5)** | 5 — Hoch | 10 — Hoch | 15 — Kritisch | 20 — Kritisch | 25 — Kritisch |
| **Schwerwiegend (4)** | 4 — Mittel | 8 — Hoch | 12 — Hoch | 16 — Kritisch | 20 — Kritisch |
| **Mittel (3)** | 3 — Niedrig | 6 — Mittel | 9 — Hoch | 12 — Hoch | 15 — Kritisch |
| **Gering (2)** | 2 — Niedrig | 4 — Mittel | 6 — Mittel | 8 — Hoch | 10 — Hoch |
| **Vernachlässigbar (1)** | 1 — Niedrig | 2 — Niedrig | 3 — Niedrig | 4 — Mittel | 5 — Mittel |

### Schwellenwerte für die Risikoeinstufung

| Einstufung | Score-Bereich | Erforderliche Maßnahme |
| --- | --- | --- |
| **Kritisch** | 15–25 | Sofortiges Handeln erforderlich; an die Geschäftsleitung eskalieren; ohne Maßnahmenplan kein Weitermachen möglich |
| **Hoch** | 8–14 | Maßnahmenplan erforderlich; Verantwortlichen benennen; mindestens monatlich prüfen |
| **Mittel** | 4–7 | Aktiv überwachen; Maßnahme wünschenswert; quartalsweise prüfen |
| **Niedrig** | 1–3 | Akzeptieren und überwachen; keine aktive Maßnahme nötig, außer mit geringem Aufwand |

Schwellenwerte und erforderliche Maßnahmen sollten auf die Risikobereitschaft der Organisation kalibriert werden. Die obigen Scores und Bereiche sind ein Ausgangsrahmen — passe sie an die Risikotoleranz der Organisation an.

## Risikoregister

### Format eines Registereintrags

Für jedes identifizierte Risiko:

```
RISIKOREGISTER-EINTRAG:
  Risiko-ID:         [eindeutige Kennung]
  Beschreibung:      [Format Ursache-Ereignis-Folge]
  Kategorie:         [Strategisch / Operativ / Finanziell / Compliance / Technologie / Personal / Extern]
  Schweregrad:       [1-5 mit Label]
  Eintrittswkt.:     [1-5 mit Label]
  Risiko-Score:      [Schweregrad × Eintrittswahrscheinlichkeit]
  Einstufung:        [Kritisch / Hoch / Mittel / Niedrig]
  Bestehende Controls: [was bereits vorhanden ist, um dem Risiko zu begegnen]
  Restrisiko:        [Risikoniveau nach bestehenden Controls — Schweregrad und Eintrittswahrscheinlichkeit neu bewerten]
  Maßnahmenplan:     [zusätzliche Maßnahmen zur Risikoreduktion — siehe Maßnahmenplanung]
  Verantwortlich:    [für das Management des Risikos zuständige Person]
  Review-Datum:      [nächste geplante Prüfung]
  Status:            [Offen / In Bearbeitung / Akzeptiert / Geschlossen]
  Trend:             [↑ Steigend / → Stabil / ↓ Sinkend — verglichen mit dem letzten Review]
```

### Restrisiko-Bewertung

Nach der Dokumentation bestehender Controls das Risiko neu bewerten:

1. Bereits vorhandene Controls identifizieren (präventiv, detektivisch oder korrektiv)
2. Wirksamkeit der Controls bewerten — werden sie konsistent angewandt? Werden sie getestet?
3. Schweregrad und Eintrittswahrscheinlichkeit unter Berücksichtigung der Controls neu bewerten
4. Der Restrisiko-Score bestimmt den erforderlichen Maßnahmenaufwand

Liegt das Restrisiko nach den bestehenden Controls über der Toleranz der Organisation, sind zusätzliche Maßnahmen erforderlich.

## Maßnahmenplanung

### Auswahl der Maßnahmenstrategie

Für jedes Risiko, das eine Maßnahme erfordert, eine oder mehrere Strategien wählen:

| Strategie | Aktion | Wann einzusetzen |
| --- | --- | --- |
| **Vermeiden** | Das Risiko durch Beseitigung der Ursache oder Änderung des Plans eliminieren | Wenn das Risiko inakzeptabel ist und ein alternativer Weg existiert |
| **Reduzieren** | Schweregrad oder Eintrittswahrscheinlichkeit durch Controls oder Designänderungen senken | Wenn das Risiko mit vertretbarem Aufwand in die Toleranz gebracht werden kann |
| **Übertragen** | Das Risiko auf eine andere Partei verlagern (Versicherung, Outsourcing, Vertragsklauseln) | Wenn eine andere Partei das Risiko wirksamer managen kann |
| **Akzeptieren** | Das Risiko anerkennen und überwachen, ohne aktive Maßnahme | Wenn das Risiko in der Toleranz liegt oder die Maßnahmenkosten die erwartete Auswirkung übersteigen |
| **Notfallplan** | Einen Reaktionsplan vorbereiten, der bei Eintritt des Risikos ausgeführt wird | Wenn das Risiko nicht verhindert, die Reaktion aber vorab geplant werden kann |

### Format eines Maßnahmenplans

Für jede Maßnahme:

```
MASSNAHME:
  Risiko-ID:         [verknüpft mit dem Registereintrag]
  Strategie:         [Vermeiden / Reduzieren / Übertragen / Akzeptieren / Notfallplan]
  Aktion:            [spezifischer, konkreter Schritt — nicht "Risiko reduzieren", sondern "automatisierte Backup-Verifikation implementieren, täglich laufend mit Alarm bei Fehler"]
  Verantwortlich:    [für die Umsetzung zuständige Person]
  Frist:             [bis wann die Maßnahme abgeschlossen sein muss]
  Kosten/Aufwand:    [für die Umsetzung benötigte Ressourcen]
  Erwartete Wirkung: [wie dies den Schweregrad- oder Eintrittswahrscheinlichkeits-Score verändert]
  Verifikation:      [wie Abschluss und Wirksamkeit bestätigt werden]
  Status:            [Nicht begonnen / In Arbeit / Abgeschlossen / Verifiziert]
```

## Risiko-Review-Prozess

### Periodische Review-Kadenz

| Review-Typ | Häufigkeit | Umfang | Teilnehmende |
| --- | --- | --- | --- |
| **Risikoregister-Review** | Monatlich oder anlassbezogen | Alle offenen Risiken — Status prüfen, Scores aktualisieren, neue Risiken markieren | Risikoverantwortliche + Risiko-Koordinator |
| **Deep-Dive-Review** | Quartalsweise | Kritische und hoch eingestufte Risiken — detaillierter Maßnahmenfortschritt, Wirksamkeit der Controls | Risikoverantwortliche + Geschäftsleitung |
| **Scan für aufkommende Risiken** | Quartalsweise | Neue Risiken aus Umfeldveränderungen, Strategiewechseln, Incidents | Funktionsübergreifende Leitung |
| **Jährliche Risikobewertung** | Jährlich | Vollständige Neuidentifikation und Neubewertung aller Risiken | Vollständiges Risiko-Governance-Team |

### Format der Review-Ausgabe

```
RISIKO-REVIEW-ZUSAMMENFASSUNG — [Datum]

Register-Snapshot:
  Risiken gesamt:  [Anzahl]
  Kritisch:        [Anzahl] — [Liste der Risiko-IDs]
  Hoch:            [Anzahl]
  Mittel:          [Anzahl]
  Niedrig:         [Anzahl]

Änderungen seit dem letzten Review:
  Neue Risiken:          [Anzahl und Kurzbeschreibungen]
  Hochgestufte Risiken:  [Risiko-IDs, die in eine höhere Einstufung gewechselt sind]
  Herabgestufte Risiken: [Risiko-IDs, die in eine niedrigere Einstufung gewechselt sind]
  Geschlossene Risiken:  [Risiko-IDs und Begründung der Schließung]

Überfällige Maßnahmen:   [Maßnahmen über ihrer Frist]
Anstehende Fristen:      [Maßnahmen, die im nächsten Review-Zeitraum fällig sind]
Aufkommende Bedenken:    [neue oder sich entwickelnde Risikothemen, noch nicht im Register]
```

## Ausgabevorlage

Strukturiere die vollständige Risikobewertung wie folgt:

```
# Risikobewertung — [Gegenstand] — [Datum]

## Zusammenfassung
- Identifizierte Risiken gesamt: [Anzahl]
- Risikoprofil: [Kritisch: x, Hoch: x, Mittel: x, Niedrig: x]
- Top-Risiko: [am höchsten eingestuftes Risiko mit Kurzbeschreibung]
- Wichtigste Maßnahmenprioritäten: [Top 3 Aktionen]

## Risikoregister
[Vollständige Registereinträge]

## Visualisierung der Risikomatrix
[5×5-Matrix mit eingetragenen Risiko-IDs]

## Maßnahmenplan
[Priorisierte Aktionen mit Verantwortlichen und Fristen]

## Review-Zeitplan
[Nächste Review-Termine und Umfang]

## Methodik-Hinweise
- Scoring-Skalen kalibriert auf: [Definitionen der Organisation oder Skill-Defaults]
- Annahmen: [während der Bewertung getroffene Annahmen]
- Einschränkungen: [Datenlücken, nicht bewertete Bereiche, Konfidenz-Vorbehalte]
```

## Leitplanken

- Erzeuge niemals konkrete Risiken aus Trainingsdaten, als würden sie auf die Situation des Nutzers zutreffen. Alle Risiken müssen aus dem Nutzerkontext, der Prozessbeschreibung oder Domänenwissen stammen.
- Erfinde niemals Schweregrad- oder Eintrittswahrscheinlichkeits-Scores. Führe den Nutzer durch die Scoring-Methodik, statt Scores einseitig zu vergeben.
- Behaupte niemals ein "typisches Risikoprofil" oder "übliche Branchenrisiken". Risikoprofile sind organisationsspezifisch.
- Versieh erzeugte Inhalte mit einer Kennzeichnung: `[Aus Risikodaten]`, `[Framework-Methodik]`, `[KI-identifiziertes Risiko — mit Fachexperten verifizieren]`.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort verteilbares Risikoregister zu erhalten.
