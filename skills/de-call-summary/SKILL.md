---
name: de-call-summary
description: Extrahiert Action Items, Kernthemen und Einwände aus Gesprächsnotizen oder Transkripten und entwirft eine kundengerichtete Follow-up-E-Mail. Verwende ihn nach einem Sales-Call, einer Demo oder einem Discovery-Termin. Auslösen mit "fasse dieses Gespräch zusammen", "Gesprächsnotizen von", "schreibe ein Follow-up für dieses Meeting".
---

# Gesprächszusammenfassung-Skill

Wandle Gesprächsnotizen oder Transkripte in verwertbare Erkenntnisse um und entwirf kundengerichtete Follow-up-E-Mails. Der Skill liefert Gesprächszusammenfassungen, Action-Item-Register, Einwand-Protokolle und Follow-up-Entwürfe. Alle Gesprächsinhalte gibst du vor oder sie kommen aus einer angebundenen Quelle.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Account-Kontext, Opportunity-Stage, bekannte Stakeholder, frühere Gesprächsnotizen |
| **Gesprächsaufzeichnung / Transkription über MCP** (z. B. Gong) | Roh-Transkripte, Teilnehmerlisten, Zeitstempel wichtiger Momente |
| **companyTRANSCRIBE** (falls aktiviert) | Transkribiert eine im Chat angehängte Gesprächsaufzeichnung (Audio oder Video) mit Sprecherzuordnung oder ruft deine vorhandenen Transkripte ab |
| **companyM365** (falls aktiviert) | Transkripte von Teams-Meetings |
| **companyRAG-Sammlungen** | Discovery-Zusammenfassungen, Wettbewerbsprofile, Produktinformationen für kontextgerechte Follow-ups |
| **Datei-Upload (Transkripte)** | Transkript- oder Notizdateien, die du direkt in den Chat lädst |

> **Keine angebundene Quelle?** Gib das Transkript oder die Notizen im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Gesprächsverarbeitungs-Workflow

```
1. INGEST Gesprächsinhalt
   |
   +--> Roh-Transkript, strukturierte Notizen oder Stichpunkt-Recap akzeptieren
   +--> Gesprächstyp bestimmen: Discovery / Demo / Verhandlung / Check-in / Sonstiges
   +--> Teilnehmende identifizieren (aus Transkript-Headern, Notizen oder Nutzereingabe)
   |
2. EXTRACT Kernthemen
   |
   +--> Diskussionspunkte kategorisieren (siehe Themen-Kategorisierung unten)
   +--> Wörtliche Zitate mit Gewicht erfassen (Entscheidungen, Zusagen, Einwände)
   +--> Angesprochene, aber ungeklärte Themen festhalten — sie werden zu offenen Punkten
   |
3. IDENTIFY Action Items
   |
   +--> Für jede genannte Zusage oder jeden nächsten Schritt:
   |      Verantwortlich (unsere Seite / ihre Seite / gemeinsam)
   |      Aktion (konkret und überprüfbar)
   |      Frist (genannt oder aus dem Kontext abgeleitet)
   |      Priorität (blockiert Deal-Fortschritt / wichtig / nice-to-have)
   |
4. FLAG Einwände und Bedenken
   |
   +--> Einwand wie geäußert erfassen (nicht weginterpretieren)
   +--> Festhalten, ob er adressiert, teilweise adressiert oder offen geblieben ist
   +--> Die gegebene Antwort (falls vorhanden) für Konsistenz in künftigen Gesprächen festhalten
   +--> Nach Typ klassifizieren (siehe Einwand-Klassifizierung unten)
   |
5. ASSESS Deal-Impact
   |
   +--> Hat das Gespräch den Deal vorangebracht, ins Stocken gebracht oder zurückgeworfen?
   +--> Was hat sich an unserem Verständnis der Opportunity geändert?
   +--> Gibt es neue Stakeholder, Risiken oder Timeline-Verschiebungen?
   |
6. DRAFT Follow-up (siehe Follow-up-E-Mail-Framework unten)
   |
7. COMPILE Ausgabe (siehe Ausgabevorlagen unten)
```

## Themen-Kategorisierung

Klassifiziere jedes Diskussionsthema, damit die Zusammenfassung schnell erfassbar bleibt:

| Kategorie | Was sie abdeckt | CRM-Relevanz |
| --- | --- | --- |
| **Requirements** | Genannte Bedürfnisse, Use Cases, Bewertungskriterien | Opportunity-Anforderungen aktualisieren |
| **Decision Process** | Timeline, beteiligte Stakeholder, Freigabeschritte | Close-Date, Entscheider-Map aktualisieren |
| **Budget / Commercial** | Preisdiskussion, Budgetgrenzen, ROI-Erwartungen | Deal-Wert, Stage aktualisieren |
| **Technical** | Integrationsbedarf, Security, Compliance, Architektur | Als technische Anforderungen erfassen |
| **Competitive** | Erwähnung von Alternativen, Bestandsanbieter, Vergleich | Wettbewerbsfeld im CRM aktualisieren |
| **Relationship** | Rapport-Signale, interne Politik, Stärke des Champions | Stakeholder-Notizen aktualisieren |
| **Next Steps** | Vereinbarte Aktionen, Folgetermine, zugesagte Deliverables | CRM-Aufgaben anlegen |

## Einwand-Klassifizierung

| Typ | Definition | Follow-up-Priorität |
| --- | --- | --- |
| **Deal-blocking** | Einwand, der den Abschluss verhindert, wenn er ungelöst bleibt | Sofort |
| **Stage-blocking** | Verhindert den Übergang in die nächste Stage, ist aber nicht zwingend ein Deal-Killer | Hoch |
| **Concern** | Geäußerte Sorge, die adressiert werden muss, aber den Fortschritt nicht blockiert | Mittel |
| **Skepticism** | Allgemeiner Zweifel an Mehrwert oder Vorgehen — braucht Belege | Mittel |
| **Clarification** | Missverständnis oder Informationslücke — leicht mit Daten zu klären | Niedrig |

Halte zu jedem Einwand fest: geäußerter Einwand (wörtlich oder nahezu wörtlich), Klassifizierung, im Gespräch gegebene Antwort, Lösungsstatus (gelöst / teilweise adressiert / offen) und empfohlene Follow-up-Aktion.

## Follow-up-E-Mail-Framework

Die Follow-up-E-Mail sollte mit minimalen Anpassungen versandfertig sein. Aufbau:

### Tonkalibrierung

| Beziehungsstand | Ton | Förmlichkeit |
| --- | --- | --- |
| **Erster Kontakt** | Professionell, wertschätzend für die Zeit | Formell |
| **Aktive Evaluierung** | Kollaborativ, auf Momentum ausgerichtet | Halbformell |
| **Etablierter Rapport** | Direkt, effizient, partnerschaftlich | Locker |
| **Executive-Publikum** | Knapp, ergebnisorientiert | Formell |

### E-Mail-Struktur

```
Betreff: [beschreibend, handlungsorientiert — niemals generisch wie "Meeting-Follow-up"]

[Einstieg: 1 Satz — Dank + Bezug auf einen konkreten Moment aus dem Gespräch]

[Zusammenfassung: 3-5 Stichpunkte des Besprochenen — formuliert aus Sicht
 ihrer Prioritäten und ihrer Sprache, nicht deiner Produktfeatures]

[Action Items: klare Tabelle oder Liste]
  - Was wir zugesagt haben → bis wann
  - Worum wir sie bitten → bis wann

[Nächster Schritt: konkret — Datum, Uhrzeit, Agenda für den nächsten Kontakt]

[Abschluss: 1 Satz — Begeisterung über das konkret besprochene Ergebnis,
 keine generische Vorfreude]
```

### Follow-up-Qualitätscheck

- Bezieht sich auf etwas Konkretes aus dem Gespräch (beweist, dass du zugehört hast)
- Verwendet ihre Sprache und Terminologie, nicht internen Jargon
- Action Items haben Verantwortliche und Termine
- Der nächste Schritt ist konkret und terminiert
- Keine Markdown-Formatierung (Klartext oder minimales HTML für E-Mail-Clients)
- Die Betreffzeile ergibt in ihrem Posteingang auch ohne Zusatzkontext Sinn
- Angemessene Länge: 150-250 Wörter für Standard-Follow-ups

## Ausgabevorlage — Gesprächszusammenfassung

```
# Gesprächszusammenfassung: [Meeting-Titel / Firmenname]
**Datum**: [Gesprächsdatum]  |  **Dauer**: [tatsächliche Länge]
**Gesprächstyp**: [Discovery / Demo / Verhandlung / Check-in]
**Teilnehmende**: [Liste mit Rollen]

## Besprochene Kernthemen
| # | Thema   | Kategorie | Zusammenfassung        |
|---|---------|-----------|------------------------|
| 1 | [Thema] | [Kategorie] | [2-3 Sätze]          |
| 2 | [Thema] | [Kategorie] | [2-3 Sätze]          |

## Action Items
| #  | Aktion             | Verantwortlich | Frist  | Priorität        |
|----|--------------------|----------------|--------|------------------|
| 1  | [konkrete Aktion]  | [Wer]          | [Wann] | [Klassifizierung]|

## Einwände & Bedenken
| Einwand        | Typ              | Status            | Follow-up nötig      |
|----------------|------------------|-------------------|----------------------|
| [wie geäußert] | [Klassifizierung]| [Offen/Adressiert]| [empfohlene Aktion]  |

## Deal-Impact-Bewertung
- **Deal-Bewegung**: [Vorangebracht / Ins Stocken geraten / Zurückgeworfen / Neutral]
- **Stage-Empfehlung**: [Bleiben / Vorrücken zu X / Zur Prüfung markieren]
- **Neue Informationen**: [Was wir gelernt haben und unser Verständnis verändert]
- **Risikoänderungen**: [Neue Risiken aufgetaucht oder bestehende abgemildert]

## Follow-up-E-Mail-Entwurf
[versandfertige E-Mail nach dem obigen Framework]
```

## Verarbeitungshinweise zur Transkriptqualität

| Eingabequalität | Handhabung |
| --- | --- |
| **Vollständiges Transkript** | Wörtliche Zitate für Schlüsselmomente extrahieren; umfassende Zusammenfassung |
| **Strukturierte Notizen** | In das Framework überführen; mögliche Abdeckungslücken markieren |
| **Stichpunkt-Recap** | Zusammenfassung aus den Stichpunkten bauen; darauf hinweisen, dass Nuancen fehlen können |
| **Teilweise / fragmentarisch** | Zusammenfassen, was vorliegt; Abschnitte klar als "[Unvollständig — Rep um Ergänzung bitten]" kennzeichnen |

## Leitplanken

1. Erfinde niemals Gesprächsinhalte. Jedes Thema, jedes Zitat und jedes Action Item muss auf die gelieferten Notizen oder das Transkript zurückführbar sein. Mehrdeutiger Inhalt: "[Unklar aus den Notizen — mit Teilnehmenden verifizieren]".
2. Erfinde niemals Reaktionen der Teilnehmenden. Charakterisiere weder Stimmung noch Kaufbereitschaft, sofern sie nicht ausdrücklich in den Notizen steht.
3. Einwand-Genauigkeit. Erfasse Einwände so nah am Wortlaut, wie es die Quelle erlaubt. Beschönige, framen oder verkleinere geäußerte Bedenken nicht.
4. Quellenkennzeichnung. Markiere Aussagen — [Aus Transkript], [Aus Notizen], [Aus Nutzereingabe], [KI-Interpretation]. KI-Interpretationen müssen zur Verifizierung gekennzeichnet werden.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um eine formatierte, sofort teilbare Zusammenfassung zu erhalten.
