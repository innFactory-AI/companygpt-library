---
name: de-call-prep
description: Erstellt aus CRM-, Kalender- und E-Mail-Kontext einen umfassenden Gesprächsbrief — Teilnehmende, Deal-Historie, offene Fragen, empfohlene Ansätze. Verwende ihn zur Vorbereitung eines Sales-Calls, einer Demo oder eines Kundenmeetings. Auslösen mit "Call vorbereiten mit [Person/Firma]", "Gesprächsbrief für", "was sollte ich vor diesem Meeting wissen".
---

# Gesprächsvorbereitung-Skill

Verbinde CRM-Kontext, Informationen zu den Teilnehmenden und die Deal-Historie zu einem kompakten, umsetzbaren Gesprächsbrief. Der Skill erzeugt Briefe, Teilnehmer-Profile, Zielsetzungs-Worksheets und Talking-Point-Sequenzen. Alle Deal-Daten und Kontaktinformationen kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. Salesforce, HubSpot, Dynamics) | Deal-Stage, Historie, Kontaktrollen, Notizen, vergangene Aktivitäten-Timeline |
| **Kalender über MCP** (z. B. Google Calendar, Outlook) | Meeting-Zeit, Teilnehmende, Agenda, wiederkehrendes Muster |
| **E-Mail über MCP** (z. B. Gmail, Outlook) | Aktueller Schriftverkehr, offene Threads, Tonalität des letzten Austauschs |
| **companyM365** (falls aktiviert) | Outlook-Kalender und -Mails sowie Personensuche aus deinem Microsoft-365-Konto |
| **companyRAG-Sammlungen** | Discovery-Frameworks, Einwand-Bibliotheken, relevante Proof Points |
| **Web-Recherche über MCP** (z. B. LinkedIn, Firmen-News) | Hintergrund der Teilnehmenden, aktuelle Signale rund um das Unternehmen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Workflow zur Gesprächsvorbereitung

```
1. KONTEXT zum Meeting sammeln
   |
   +--> Kalendereintrag ziehen: Zeit, Teilnehmende, Agenda
   +--> CRM auf Deal-Record prüfen: Stage, Wert, Historie, letzte Aktivität
   +--> Aktuelle E-Mails mit den Teilnehmenden auf offene Threads oder Tonalitätswechsel scannen
   |
2. TEILNEHMENDE recherchieren
   |
   +--> Für jede teilnehmende Person:
   |      +--> CRM-Kontaktdatensatz (Rolle, frühere Interaktionen, Notizen)
   |      +--> Klassifizierung der Buying-Center-Rolle (aus der Deal-Strategie, falls vorhanden)
   |      +--> Aktueller beruflicher Kontext (Beförderung, Rollenwechsel, öffentliche Posts)
   |      +--> Hinweise auf den Kommunikationsstil (formell/informell, detail- oder big-picture-orientiert)
   |
3. DEAL-HISTORIE durchsehen
   |
   +--> Timeline der wichtigsten Interaktionen (Meetings, Angebote, Follow-ups)
   +--> Zusagen beider Seiten (und ob sie eingehalten wurden)
   +--> Offene Einwände oder ungelöste Bedenken aus früheren Calls
   +--> Wettbewerbserwähnungen oder Signale einer Alternativen-Evaluierung
   |
4. GESPRÄCHSZIELE festlegen
   |
   +--> Primärziel: das eine Ergebnis, das diesen Call zum Erfolg macht
   +--> Sekundärziele: zusätzliche Themen, die du bei ausreichend Zeit abdeckst
   +--> Mindestergebnis: die Untergrenze — was du mindestens mitnehmen musst
   +--> Fortschrittsmarker: wie ein Vorankommen im Deal-Stage nach diesem Call aussieht
   |
5. TALKING-POINT-SEQUENZ aufbauen
   |
   +--> Talking Points den Zielen zuordnen (siehe Talking-Point-Sequenzierung unten)
   +--> Fragen je Teilnehmer-Rolle vorbereiten
   +--> Einwand-Antworten für bekannte Bedenken bereithalten
   +--> Proof Points und Referenzen identifizieren, die griffbereit sein sollten
   |
6. GESPRÄCHSBRIEF zusammenstellen (siehe Ausgabevorlage unten)
```

## Teilnehmer-Analyse

Erstelle für jede teilnehmende Person ein kompaktes Profil:

| Feld | Beschreibung |
| --- | --- |
| **Name & Titel** | Aktuelle Rolle — gegen CRM und LinkedIn abgleichen |
| **Buying-Center-Rolle** | Economic Buyer, Champion, Technical Evaluator, End User, Blocker, Sonstige |
| **Beziehungshistorie** | Frühere Meetings, Zusammenfassung des Schriftverkehrs, Beziehungsqualität |
| **Bekannte Prioritäten** | Was ihnen wichtig ist — genannte Ziele, Evaluierungskriterien, Pain Points |
| **Kommunikationsstil** | Formell / locker, detail- oder big-picture-orientiert, konsensorientiert / entscheidungsfreudig |
| **Watch-Outs** | Ungelöste Einwände, frühere Reibungspunkte, konkurrierende Prioritäten |

Wenn die Datenlage zu einer teilnehmenden Person dünn ist, kennzeichne die Lücke: "Begrenzter Hintergrund — Discovery-Fragen für diesen Kontakt einplanen."

## Zielsetzungs-Framework

Jeder Call braucht eine gestaffelte Zielstruktur:

| Stufe | Definition | Beispiel |
| --- | --- | --- |
| **Primärziel** | Das ideale Ergebnis — den Deal zu einem definierten nächsten Meilenstein bringen | "Zusage zu einem technischen Proof-of-Concept bis [Datum] sichern" |
| **Sekundärziele** | Wertvolle Nebenergebnisse, die sich bei ausreichend Zeit lohnen | "Budget-Timeline bestätigen; Procurement-Kontakt identifizieren" |
| **Mindestergebnis** | Die Untergrenze — das Wenigste, mit dem du herausgehen musst | "Folgetermin mit anwesendem Technik-Team vereinbaren" |
| **Fortschrittsmarker** | Wie der Nachweis von Fortschritt nach diesem Call aussieht | "Mutual Action Plan geteilt und akzeptiert" |

Wenn der Nutzer keine Ziele angibt, leite sie aus dem Deal-Stage und der Zusammensetzung der Teilnehmenden ab, kennzeichne sie aber als "[KI-Vorschlag — vor dem Call bestätigen]".

## Talking-Point-Sequenzierung

Strukturiere den Gesprächsverlauf je nach Call-Typ:

### Discovery Call

1. Kontext setzen (2 Min.): Bestätigen, was du weißt, und Vorbereitung zeigen
2. Situations-Exploration (10–15 Min.): Offene Fragen zum aktuellen Stand
3. Problemaufdeckung (10–15 Min.): Pain Points und ihre Auswirkungen vertiefen
4. Wert-Verknüpfung (5 Min.): Pain mit deiner Fähigkeit verbinden — Fragen, kein Pitch
5. Next-Step-Commitment (3 Min.): Konkrete nächste Aktion mit Datum vorschlagen

### Demo- / Präsentations-Call

1. Recap und Agenda bestätigen (3 Min.): Wiederholen, was sie sehen wollten und warum
2. Maßgeschneiderte Demonstration (15–20 Min.): Funktionen auf ihre genannten Prioritäten abbilden
3. Reaktions-Check (5 Min.): Nach jedem größeren Abschnitt für Feedback pausieren
4. Einwand-Aufdeckung (5–10 Min.): Proaktiv fragen, welche Bedenken bleiben
5. Next-Step-Commitment (3 Min.): Evaluierungskriterien oder nächstes Meeting vorschlagen

### Verhandlungs- / Abschluss-Call

1. Alignment-Check (5 Min.): Gemeinsames Verständnis von Umfang und Wert bestätigen
2. Konditionen-Besprechung (15–20 Min.): Offene Punkte durchgehen
3. Bedenken-Auflösung (10 Min.): Blocker mit vorbereiteten Antworten adressieren
4. Vereinbarungs-Framing (5 Min.): Zusammenfassen, was vereinbart wurde
5. Prozess-Next-Steps (5 Min.): Genaue Schritte bis zur Unterschrift definieren

### Check-In- / Beziehungs-Call

1. Persönlicher Rapport (3–5 Min.): Echte Verbindung, kein einstudierter Small Talk
2. Gelieferter Mehrwert (5–10 Min.): Ergebnisse seit der letzten Interaktion durchgehen
3. Feedback-Schleife (5–10 Min.): Was funktioniert, was nicht
4. Expansion-Signale (5 Min.): Neue Use Cases, Abteilungen oder Pain Points
5. Vorausplan (3 Min.): Nächster Touchpoint und etwaige Action Items

## Ausgabevorlage — Gesprächsbrief

```
# Gesprächsbrief: [Meeting-Titel]
**Datum/Zeit**: [Datum und Uhrzeit des Meetings]
**Dauer**: [Geplante Länge]
**Call-Typ**: [Discovery / Demo / Verhandlung / Check-In / Sonstige]

## Deal-Kontext
- **Account**: [Firmenname]
- **Deal-Stage**: [Aktuelle Stage] | **Wert**: [Betrag oder Spanne]
- **Tage in Stage**: [Anzahl] | **Erwarteter Abschluss**: [Datum oder "TBD"]
- **Letzte Interaktion**: [Datum — Zusammenfassung des letzten relevanten Kontakts]

## Teilnehmende
| Name | Titel | Rolle | Beziehung | Wichtigste Priorität |
| --- | --- | --- | --- | --- |
| [Name] | [Titel] | [Buying-Rolle] | [Historie] | [Was ihnen wichtig ist] |

## Offene Punkte aus früheren Calls
- [ ] [Zusage oder Frage, die noch ungelöst ist — Verantwortlicher und Datum]
- [ ] [Einwand, der angesprochen, aber nicht vollständig adressiert wurde]

## Gesprächsziele
- **Primär**: [Ideales Ergebnis]
- **Sekundär**: [Zusätzliche Ziele]
- **Mindestergebnis**: [Untergrenze]

## Empfohlene Talking Points
1. [Thema] — [Warum es zählt] — [Vorgeschlagenes Framing oder Frage]
2. [Thema] — [Warum es zählt] — [Vorgeschlagenes Framing oder Frage]
3. [Thema] — [Warum es zählt] — [Vorgeschlagenes Framing oder Frage]

## Einwände, auf die du dich vorbereiten solltest
| Wahrscheinlicher Einwand | Vorbereitete Antwort | Beleg / Proof Point |
| --- | --- | --- |
| [Erwartetes Bedenken] | [Antwort-Framework] | [Bereitzuhaltende Referenz] |

## Bereitzuhaltende Materialien
- [ ] [Dokument, Case Study oder Demo-Umgebung]
- [ ] [Pricing oder Angebot, falls zutreffend]

## Post-Call-Checkliste
- [ ] Recap-E-Mail innerhalb von [Zeitrahmen] senden
- [ ] CRM mit Gesprächsnotizen und nächsten Schritten aktualisieren
- [ ] Neue Kontakte oder Änderungen an der Stakeholder-Map erfassen
```

## Leitplanken

1. Erfinde niemals Informationen zu den Teilnehmenden. Alle Namen, Titel und die Beziehungshistorie müssen aus CRM, Kalender, E-Mail oder Nutzereingabe stammen. Unbekannte Teilnehmende: "[Name aus Kalender — kein CRM-Datensatz, Discovery einplanen]".
2. Erfinde niemals Deal-Historie. Existiert kein CRM-Datensatz, schreibe "Kein früherer Deal-Datensatz gefunden", statt von einem Erstkontakt auszugehen.
3. Quellenkennzeichnung. Versieh jede Aussage mit einem Tag — [Aus CRM], [Aus Kalender], [Aus E-Mail], [Aus Nutzereingabe], [KI-Empfehlung].
4. Verifizierungs-Hinweis. Ergänze auf allen Ausgaben "Brief vor dem Call gegen dein eigenes Account-Wissen prüfen".

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Gesprächsbrief zu erhalten.
