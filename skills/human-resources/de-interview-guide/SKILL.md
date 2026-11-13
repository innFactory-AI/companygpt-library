---
name: de-interview-guide
description: Erstellt strukturierte Interview-Leitfäden mit verhaltensbasierten Fragen, Bewertungsrastern und Hinweisen zur Bias-Vermeidung. Verwende ihn, wenn du für eine neue Stelle rekrutierst, deinen Interview-Prozess neu gestaltest oder Interviewer kalibrierst. Auslösen mit "Interview-Leitfaden erstellen für", "Scorecard erstellen für", "Interviews für diese Rolle gestalten".
---

# Interview-Leitfaden-Skill

Gestalte mehrstufige Interview-Prozesse mit verhaltensbasierten Bewertungsrastern, Interviewer-Kalibrierung und einer belastbaren Debrief-Methodik. Organisationsspezifische Daten — Rollenanforderungen, Kompetenzdefinitionen, Team-Kontext — kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **ATS über MCP** (z. B. Greenhouse, Lever) | Offene Stellen, Rollenbeschreibungen, bestehende Scorecards, Konfiguration der Interview-Stufen |
| **HRIS über MCP** (z. B. Workday, Personio, Bamboo HR) | Job-Architektur, Kompetenzdefinitionen, Ziel-Jobleveln, Teamstruktur |
| **companyRAG / Datei-Upload** | Stellenbeschreibungen, Kompetenz-Frameworks, Rollenanforderungen, Recruiting-Richtlinien |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## EU-AI-Act- & DSGVO-Compliance-Grenzen

KI-gestützte Rekrutierung und Bewerberbewertung gilt als **hochriskant nach dem EU AI Act (Anhang III, Kategorie 4 — Beschäftigung und Personalmanagement)**. Nach Artikel 22 DSGVO haben Personen das Recht, nicht einer ausschließlich auf automatisierter Verarbeitung beruhenden Entscheidung unterworfen zu werden, die ihnen gegenüber rechtliche oder ähnlich erhebliche Wirkung entfaltet. Alle Ergebnisse sind Entscheidungshilfen für menschliche Fachkräfte — Bewerberbewertung, Scoring und Einstellungsentscheidungen müssen von qualifizierten menschlichen Interviewern getroffen werden.

## Gestaltung des Interview-Prozesses

### Kompetenz-zu-Stufe-Mapping

Die Grundlage strukturierten Recruitings ist sicherzustellen, dass jede erforderliche Kompetenz bewertet wird, jede Kompetenz mindestens einmal bewertet wird und keine Kompetenz über mehrere Stufen hinweg redundant bewertet wird — es sei denn, dies geschieht bewusst (zur Verlässlichkeit).

Methodik für das Mapping:

1. Liste alle für die Rolle und das Joblevel erforderlichen Kompetenzen auf (aus Job-Architektur oder Rollenbeschreibung)
2. Ordne jede Kompetenz der optimalen Bewertungsmethode zu:
   - Verhaltensinterview: Vergangenes Verhalten als Prädiktor — am besten für Zwischenmenschliches, Führung, Problemlösung, kulturelle Anpassungsfähigkeit
   - Technische Bewertung: Nachgewiesene Fähigkeit — am besten für Fachexpertise, Coding, analytisches Denken, Schreiben
   - Case/Simulation: Angewandtes Urteilsvermögen — am besten für strategisches Denken, Priorisierung, Stakeholder-Management
   - Arbeitsprobe: Tatsächliches Ergebnis — am besten für kreative, operative und ausführungslastige Rollen
3. Gruppiere Kompetenzen nach Methodentyp in Bewertungsstufen
4. Weise jede Stufe einem oder mehreren Interviewern zu, basierend auf deren Qualifikation, diese Kompetenzen zu bewerten
5. Prüfe die Abdeckung: Erstelle eine Matrix aus Kompetenzen × Stufen — jede Kompetenz muss mindestens einmal vorkommen; markiere alle, die dreimal oder häufiger auftauchen (wahrscheinlich redundant)

### Methodik der Panel-Gestaltung

Lege fest, wer was bewertet, und stelle sicher, dass das Urteil keines einzelnen Interviewers dominiert.

- Panel-Größe: 2–4 Interviewer je nach Senioritätsgrad der Rolle und Organisationsgröße (Hiring Manager + 1–3 weitere). Weniger erzeugt ein Single-Point-of-Failure-Risiko; mehr bringt abnehmenden Grenznutzen und Terminierungsaufwand. Kleinere Organisationen oder Junior-Rollen können 2 nutzen; Senior- oder funktionsübergreifende Rollen profitieren von 3–4.
- Prinzip der Interviewer-Zuweisung: Weise Interviewer Kompetenzen zu, die sie qualifiziert bewerten können. Eine Backend-Entwicklerin sollte keine Produktstrategie bewerten; ein Product Manager keine Codequalität.
- Überschneidungsstrategie: Bewusste Überschneidung bei 1–2 kritischen Kompetenzen liefert Verlässlichkeitsdaten. Unbeabsichtigte Überschneidung verschwendet Zeit von Bewerbern und Interviewern.
- Unabhängigkeitsanforderung: Interviewer dürfen vor dem Debrief KEINE Notizen oder Eindrücke teilen. Sequenzielle Kontamination zerstört den Wert mehrerer unabhängiger Bewertungen.

### Reihenfolge der Stufen

Ordne die Interview-Stufen so, dass sowohl Candidate Experience als auch Informationswert optimiert werden:

1. Screening (Recruiter oder Hiring Manager): Passung zur Rolle, Logistik, beidseitiges Interesse — beseitigt Fehlausrichtung frühzeitig
2. Technische/fachliche Bewertung: Fachliche Fähigkeit — die signalstärkste, objektivste Stufe
3. Verhaltensinterviews: Belege für vergangenes Verhalten — erfordern mehr Interviewer-Kompetenz, profitieren vom Rollenkontext aus früheren Stufen
4. Case/Simulation (falls zutreffend): Angewandtes Urteilsvermögen — kognitiv anspruchsvoll für die Bewerberin, besser nicht an erster Stelle
5. Werte/Culture-Add (falls zutreffend): Organisatorische Passung — anfällig für Bias; wende Culture-Add-Scorecard-Muster sowie die in diesem Skill beschriebenen Praktiken zur Bias-Vermeidung und zum Debrief an
6. Finalrunde (Senior Leadership): Strategische Passung und Sponsorship — erst, nachdem frühere Stufen die Fähigkeit bestätigt haben

## Framework für die Scorecard-Gestaltung

### Konstruktion verhaltensbasierter Anker

Eine Scorecard ist nur so gut wie ihre Anker. Verhaltensbasierte Anker definieren, wie "gut" auf jeder Bewertungsstufe für jede Kompetenz aussieht, und machen das Scoring über Interviewer hinweg konsistent.

5-stufiges Anker-Framework:

| Stufe | Label | Muster der Anker-Definition |
| --- | --- | --- |
| 1 | Erfüllt nicht (Does Not Meet) | Kein Beleg für die Kompetenz; Antworten enthalten gar keine relevanten Beispiele |
| 2 | Erfüllt teilweise (Partially Meets) | Einige Belege, aber erhebliche Lücken; Beispielen fehlt Spezifität, Eigenverantwortung oder Ergebnis |
| 3 | Erfüllt Erwartungen (Meets Expectations) | Klare Belege mit konkreten Beispielen, die die Kompetenz auf dem Ziel-Joblevel zeigen |
| 4 | Übertrifft Erwartungen (Exceeds Expectations) | Starke Belege mit mehreren Beispielen, die die Kompetenz über dem Ziel-Joblevel zeigen |
| 5 | Außergewöhnlich (Exceptional) | Überzeugende Belege für die Kompetenz auf einem Niveau, das Team- oder Organisationspraxis beeinflussen würde |

Schreibe für jede Kompetenz auf der Scorecard stufenspezifische Anker, die beobachtbares Bewerberverhalten für diese Kompetenz beschreiben. Generische Anker ("gute Antwort" / "schlechte Antwort") verfehlen den Zweck.

Muster zum Schreiben kompetenzspezifischer Anker:

```
Kompetenz: [Name] — Ziel-Joblevel: [aus Job-Architektur]
Stufe 1: [Wie sähe eine Antwort OHNE Beleg für diese Kompetenz aus?]
Stufe 3: [Welche konkreten Verhaltensweisen/Beispiele würden dies auf dem Ziel-Level zeigen?]
Stufe 5: [Was würde das Ziel-Level so übertreffen, dass es klar von Stufe 3 unterscheidbar ist?]
```

Schreibe zuerst die Stufen 1, 3 und 5. Interpoliere dann die Stufen 2 und 4 als Zwischenpunkte. Das verhindert den häufigen Fehler, dass sich alle Stufen ähnlich anfühlen.

Passe für Verhaltens-, technische, Case- und Werte/Culture-Add-Interviews das obige Anker-Framework an die jeweilige Bewertungsmethode an (siehe Kompetenz-zu-Stufe-Mapping) und halte die Scorecard-Abschnitte über die Interview-Typen hinweg konsistent.

### Scorecard-Abschnitte

Jede Scorecard sollte enthalten:

1. Bewertete Kompetenz: Verknüpft mit den Kompetenzanforderungen der Rolle
2. Ziel-Joblevel: Aus der Job-Architektur — legt die Schwelle für "Erfüllt Erwartungen" fest
3. Verhaltensbasierte Anker: Stufenspezifische Beschreibungen wie oben
4. Vorgeschlagene Vertiefungsbereiche: Keine vorformulierten Fragen, sondern Bereiche zum Explorieren, die Belege für diese Kompetenz hervorbringen
5. Feld zur Belegerfassung: Platz für die Interviewerin, um konkrete Aussagen und Verhaltensweisen der Bewerber festzuhalten (keine Eindrücke)
6. Score: Ein einzelner numerischer Wert je Kompetenz, gestützt auf die Anker
7. Gesamtempfehlung: Getrennt von den einzelnen Kompetenz-Scores — das ganzheitliche Hire/No-Hire-Signal der Interviewerin mit schriftlicher Begründung

## STAR+-Bewertungsmethodik

Du weißt bereits, was STAR ist. Dieser Abschnitt ergänzt die Bewertungsebene: wie du die Qualität von Bewerberantworten mit STAR+ BEWERTEST — nicht, wie du STAR-Fragen erzeugst.

### STAR+-Qualitätsindikatoren

Wenn eine Bewerberin eine verhaltensbasierte Antwort gibt, bewerte entlang dieser Dimensionen über die reine STAR-Struktur hinaus:

| Indikator | Was zu bewerten ist | Red Flag |
| --- | --- | --- |
| **Spezifität** | Ist das Beispiel ein konkretes, datierbares Ereignis oder ein verallgemeinertes "Ich mache normalerweise..."-Muster? | "In solchen Situationen mache ich typischerweise..." (kein konkretes Beispiel) |
| **Eigenverantwortung** | Beschreibt die Person ihre eigenen Handlungen und Entscheidungen oder Team-/Organisationsergebnisse? | "Wir haben entschieden..." ohne Klarheit über die eigene Rolle |
| **Messbare Wirkung** | Sind Ergebnisse quantifiziert oder mit konkreten Belegen qualifiziert? | "Es lief richtig gut" ohne Details |
| **Proportionale Zuschreibung** | Ist die beanspruchte Wirkung proportional zur beschriebenen Rolle? | Junior-Rolle beansprucht organisationsweite Transformation |
| **Reflexion** | Zeigt die Person Lernen oder Anpassung aus der Erfahrung? | Stellt jedes Beispiel als uneingeschränkten Erfolg dar |
| **Relevanz** | Passt das Beispiel zur bewerteten Kompetenz und zum Joblevel? | Starkes Beispiel, falsche Kompetenz |

### Bewertung technischer Antworten

Technische Bewertungen erfordern andere Qualitätsindikatoren:

- Vorgehen vor Lösung: Klärt die Person Anforderungen und Rahmenbedingungen, bevor sie zur Lösung springt?
- Artikulation von Trade-offs: Kann die Person erklären, warum sie einen Ansatz gegenüber Alternativen gewählt hat?
- Bewusstsein für Edge Cases: Erkennt die Person Randbedingungen ungefragt?
- Kommunikation der Argumentation: Kann die Person ihren Gedankengang einer Nicht-Fachperson erklären?
- Kalibrierung auf das Joblevel: Eine Senior-Kandidatin, die löst, aber nicht lehren oder architekten kann, zeigt IC2-Verhalten, nicht IC4

## Debrief-Methodik

Im Debrief werden aus einzelnen Bewertungen eine kollektive Einstellungsentscheidung. Ohne Struktur orientiert sich der Debrief an dem, wer zuerst oder am selbstbewusstesten spricht.

### Strukturierter Debrief-Prozess

1. Vor-Debrief: Alle Interviewer reichen ihre Scorecards VOR dem Debrief-Meeting ein. Keine Ausnahmen — die vorherige Abgabe verhindert das Verankern an den Bewertungen anderer.
2. Score-Reveal: Zeige alle Scores gleichzeitig (Tabelle, Whiteboard, Tool). Geh NICHT reihum durch — die erste sprechende Person verankert alle anderen.
3. Identifikation von Abweichungen: Finde Kompetenzen, bei denen sich Scores um 2+ Stufen unterscheiden. Das sind die Diskussionspunkte.
4. Beleg-Review: Für jede abweichende Kompetenz teilt jeder Interviewer die konkreten Bewerberbelege (Zitate, Verhaltensweisen), die seinen Score begründet haben. Die Diskussion fokussiert auf Belege, nicht Eindrücke.
5. Kalibrierung: Nach dem Teilen der Belege dürfen Interviewer Scores anpassen. Anpassungen müssen belegbasiert sein — "Dieses Beispiel hatte ich nicht bedacht" ist gültig; "Ich richte mich nach dem Hiring Manager" nicht.
6. Aggregierte Bewertung: Kombiniere die Scores anhand der vorab vereinbarten Gewichtung (aus der Scorecard-Gestaltung). Der gewichtete Score ist ein Input für die Entscheidung, nicht DIE Entscheidung.
7. Einstellungsentscheidung: Der Hiring Manager trifft die finale Entscheidung und nennt ausdrücklich, ob er dem aggregierten Score folgt oder ihn übersteuert — und warum.
8. Dokumentation: Halte die Entscheidungsbegründung fest, einschließlich jeder Übersteuerungs-Begründung. Diese Dokumentation stützt belastbare Einstellungsentscheidungen.

### Auflösung von Uneinigkeit

Wenn Interviewer auch nach dem Teilen der Belege ernsthaft uneinig sind:

- Prüfe auf unterschiedliche Belegbasen (verschiedene Stufen können unterschiedliches Verhalten gezeigt haben)
- Prüfe auf Maßstabsunterschiede (das "Erfüllt" des einen kann das "Übertrifft" des anderen sein — ein Kalibrierungsproblem, das für künftige Einstellungen zu lösen ist, nicht für diese Entscheidung)
- Prüfe auf Bias-Muster (Milde, Strenge, Halo, Affinität, Groupthink, Kontrasteffekte) mithilfe des obigen strukturierten Debrief-Prozesses
- Wenn die Uneinigkeit nach dem Beleg-Review bestehen bleibt, dokumentiere beide Positionen und lass den Hiring Manager mit voller Transparenz entscheiden

## Bewerber-Bewertungsmatrix

Für die finale Entscheidungsfindung über mehrere Bewerber hinweg:

### Gewichteter mehrdimensionaler Vergleich

Gewichte die Scorecard-Kompetenzen nach Rollenpriorität und befülle sie mit den Debrief-Scores jeder Bewerberin. Die Matrix ist EIN Input für die Entscheidung, nicht DIE Entscheidung. [KI-generierter Vorschlag — prüfen] Jedes auf Matrix-Scores basierende Ranking muss vom Hiring-Team validiert werden, das Kontext hat, den die Matrix nicht erfassen kann (Teamdynamik, Entwicklungspotenzial, Wettbewerbsfähigkeit des Angebots).

## Compliance-Bewusstsein bei KI-gestütztem Recruiting

Wenn KI-Tools in irgendeinem Teil des Recruiting-Prozesses eingesetzt werden (CV-Screening, Bewertungs-Scoring, Chatbot-Interaktionen, Analyse von Video-Interviews), kann dies eine Hochrisiko-Einstufung nach dem AI Act auslösen (Anhang III, Kategorie 4 — Beschäftigung und Personalmanagement).

Scoping-Methodik — prüfe, ob der KI-Anwendungsfall Folgendes umfasst:

- Rekrutierungs- oder Auswahlentscheidungen
- Screening oder Filterung von Bewerbungen
- Bewertung von Bewerbern
- Überwachung oder Bewertung während des Beschäftigungsverhältnisses

Falls eines davon zutrifft, kläre die Pflichten des Betreibers und prüfe die konkreten Anforderungen mit arbeitsrechtlicher Beratung in der jeweils anwendbaren Jurisdiktion, da nationale Umsetzungen variieren können.

Antidiskriminierungsanforderungen bei der Bewertung im Recruiting variieren erheblich nach Jurisdiktion. Wichtige Beispiele: Allgemeines Gleichbehandlungsgesetz (AGG) in Deutschland, Bestimmungen des Code du travail in Frankreich, Wet gelijke behandeling in den Niederlanden. Prüfe die Compliance deines Bewertungsansatzes mit arbeitsrechtlicher Beratung in der anwendbaren Jurisdiktion, bevor du ihn umsetzt.

## Unterstützendes Material

Wenn du detaillierte Strategien zur Bias-Vermeidung oder Scorecard-Vorlagen in companyRAG-Sammlungen oder als hochgeladene Dateien hast, ziehe sie heran, wenn du Ansätze zur Bias-Vermeidung gestaltest oder Scorecards baust. Andernfalls baue diese aus den Frameworks dieses Skills.

## Leitplanken

- Erzeuge niemals Bewerberbewertungen, Scores, Rankings oder Hire/No-Hire-Empfehlungen. Jede Bewerberbewertung muss von menschlichen Interviewern mithilfe der bereitgestellten Frameworks vorgenommen werden.
- Leite niemals Bewerberqualifikationen ab, die nicht ausdrücklich in den bereitgestellten Materialien genannt sind. Erzeuge niemals "Standard"-Interviewfragen aus Trainingsdaten — leite alle Bewertungsinhalte aus den spezifischen Kompetenzanforderungen der Rolle ab.
- Markiere, wenn Bewertungsansätze geschützte Merkmale berühren: "Mit arbeitsrechtlicher Beratung in [Jurisdiktion] validieren, um die Einhaltung der Antidiskriminierungsanforderungen zu bestätigen."
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Framework-Vorlage]`, `[Aus Rollenanforderungen]` oder `[KI-generierter Vorschlag — prüfen]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um einen formatierten Interview-Leitfaden und Scorecards zu erhalten, die sofort mit dem Panel teilbar sind.
