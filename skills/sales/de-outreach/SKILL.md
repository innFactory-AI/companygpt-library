---
name: de-outreach
description: Recherchiert einen Prospect und entwirft anschließend personalisierte Outreach mit recherchegestützten Aufhängern, Betreffzeilen-Varianten und Follow-up-Sequenzen. Verwende ihn für Cold-E-Mails an einen Prospect, LinkedIn-Outreach oder den Aufbau einer Multi-Touch-Sequenz. Auslösen mit "Outreach entwerfen an [Person/Unternehmen]", "Cold-E-Mail schreiben an", "Outreach-Sequenz für".
---

# Outreach-Skill

Verbinde Prospect-Wissen mit dem Verfassen von Nachrichten, um personalisierte, kanalübergreifende Outreach zu erstellen — Erstnachrichten, Betreffzeilen-Varianten, Follow-up-Sequenzen und LinkedIn-Kontaktanfragen. Prospect-Daten kommen von dir, aus einer angebundenen MCP-Quelle, aus companyRAG-Sammlungen oder per Datei-Upload.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. Salesforce, HubSpot, Dynamics) | Frühere Interaktionen, Deal-Historie, Kontaktstatus, Do-not-contact-Flags |
| **Sales-Engagement- / Enrichment-Tools über MCP** (z. B. LinkedIn, Unternehmenswebseite, News) | Rollenkontext, jüngste Aktivität, Unternehmenssignale, gemeinsame Kontakte |
| **companyRAG-Sammlungen** | ICP-Definitionen, Messaging-Frameworks, relevante Proof Points |
| **companyRAG / Datei-Upload** | Trigger-Events, öffentliche Statements, gemeinsame Interessen, Kontextmaterial |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Outreach-Workflow

```
1. BESTEHENDE Beziehung prüfen
   |
   +--> Im CRM nach Prospect und Account suchen
   |      BESTEHENDER KONTAKT --> Historie, letzte Interaktion, Opt-out-Status prüfen
   |      FRÜHERER DEAL --> Tonalität anpassen: Re-Engagement, keine Cold-Outreach
   |      KEIN EINTRAG --> Als Net-new-Outreach fortfahren
   |
2. PROSPECT recherchieren (Personenebene)
   |
   +--> Aktuelle Rolle, Betriebszugehörigkeit und Verantwortungsbereich
   +--> Jüngste berufliche Aktivität (Posts, Vorträge, Jobwechsel, Beförderung)
   +--> Genannte Prioritäten oder Herausforderungen (Interviews, Panel-Zitate, Blogposts)
   +--> Gemeinsame Kontakte oder geteilter Kontext (Events, Gruppen, Alma Mater)
   |
3. ACCOUNT recherchieren (Unternehmensebene)
   |
   +--> Jüngste Signale: Funding, Produktlaunch, Führungswechsel, Hiring-Welle
   +--> Branchenkontext: regulatorische Veränderungen, Wettbewerbsbewegungen, Markttrends
   +--> Hinweise auf den Technologie-Stack (sofern für deine Lösung relevant)
   |
4. PERSONALISIERUNGS-Aufhänger identifizieren
   |
   +--> Prospect-/Account-Signale auf Value Propositions abbilden
   +--> Aufhänger nach Spezifität und Aktualität ranken (siehe Hook-Ranking unten)
   +--> 1–2 primäre Aufhänger pro Nachricht auswählen
   |
5. NACHRICHT(EN) entwerfen
   |
   +--> Kanal und Format wählen (siehe Channel-Routing unten)
   +--> Nachrichtenstruktur anwenden (siehe Message-Architektur unten)
   +--> Betreffzeilen-Varianten erzeugen (nur E-Mail)
   +--> Gegen die Qualitätskriterien prüfen
   |
6. FOLLOW-UP-Sequenz aufbauen (bei Multi-Touch)
   |
   +--> 3–5-Touch-Sequenz mit variierenden Blickwinkeln gestalten
   +--> Touches angemessen takten (siehe Sequenz-Architektur unten)
   +--> Jeder Touch bringt neuen Mehrwert oder Blickwinkel — niemals nur ein "Nachfassen"
   |
7. OUTPUT zusammenstellen (siehe Ausgabevorlage unten)
```

## Hook-Ranking

Nicht jede Personalisierung ist gleich stark. Ranke Aufhänger nach Wirkung:

| Rang | Hook-Typ | Beispiel | Warum es funktioniert |
| --- | --- | --- | --- |
| 1 | **Trigger-Event + Rollen-Match** | "Habe gesehen, dass du gerade EMEA-Ops übernommen hast — genau dann evaluieren Teams oft..." | Zeitnah + relevant für ihr neues Mandat |
| 2 | **Genannte Priorität + dein Mehrwert** | "Du hast [Priorität] bei [Event] erwähnt — wir helfen Teams..." | Belegt Recherche + direkte Relevanz |
| 3 | **Empfehlung über gemeinsamen Kontakt** | "[Name] hat vorgeschlagen, dass ich mich melde, weil..." | Warmer Intro über vertrauenswürdigen Kontakt |
| 4 | **Unternehmenssignal + Implikation** | "Mit der Expansion von [Unternehmen] in [Markt] stehen Teams oft vor..." | Zeigt Verständnis für ihren Geschäftskontext |
| 5 | **Geteilter Kontext** | "Als [Gruppe]-Mitglied ist mir dein Post über... aufgefallen" | Echte gemeinsame Basis |
| 6 | **Branchentrend + Spezifität** | "Teams in [ihrem spezifischen Sub-Segment] kämpfen mit..." | Relevant, aber weniger persönlich |

Aufhänger mit Rang 1–3 sind stark genug, um eine Nachricht zu eröffnen. Aufhänger mit Rang 4–6 sind unterstützender Kontext und eignen sich besser als Verstärkung im zweiten Satz.

## Channel-Routing

| Kanal | Am besten für | Längenrichtwert | Tonalität |
| --- | --- | --- | --- |
| **E-Mail** | Detaillierte Value Prop, mehrere Stakeholder, formelle Branchen | 80–150 Wörter Body | Professionell |
| **LinkedIn-Nachricht** | Peer-to-Peer, Tech/Startup, nach akzeptierter Verbindung | 50–80 Wörter | Gesprächig |
| **LinkedIn-InMail** | Cold-Outreach ohne E-Mail, Senior-Prospects | 60–100 Wörter | Professionell-locker |
| **LinkedIn-Kontaktanfrage** | Erster Touch, Netzwerkaufbau | Unter 300 Zeichen | Kurz, spezifisch |

## Message-Architektur

Jede Outreach-Nachricht folgt unabhängig vom Kanal dieser Struktur:

### Zeile-für-Zeile-Framework

| Abschnitt | Zweck | Länge |
| --- | --- | --- |
| **Eröffnungszeile** | Personalisierter Aufhänger — warum du genau diese Person anschreibst | 1 Satz |
| **Kontext-Brücke** | Verbinde den Aufhänger mit einem Problem oder einer Chance, die sie wahrscheinlich haben | 1–2 Sätze |
| **Value Statement** | Welches Ergebnis du erreichen hilfst — nicht, was dein Produkt tut | 1 Satz |
| **Proof Point** | Glaubwürdigkeitssignal — konkretes Ergebnis, genannter Kunde, Kennzahl | 1 Satz (optional in Kurzformaten) |
| **Call to Action** | Spezifischer, reibungsarmer Ask | 1 Satz |

### Eröffnungszeilen-Muster (passend zum Hook wählen)

- Trigger: "Mir ist [konkretes Event] aufgefallen — wenn Teams [Veränderung] durchlaufen, tun sie oft..."
- Empfehlung: "[Name] hat erwähnt, dass du die richtige Ansprechperson für [Thema] bist..."
- Content: "Dein [Post/Vortrag] zu [Thema] hat mich angesprochen — besonders der Punkt über..."
- Beobachtung: "Beim Blick darauf, wie [Unternehmen] [Initiative] angeht, hatte ich einen Gedanken zu..."

### Call-to-Action-Muster

| CTA-Typ | Wann einsetzen | Beispiel |
| --- | --- | --- |
| **Frage-CTA** | Discovery-Phase, geringe Verbindlichkeit | "Ist [konkretes Problem] dieses Quartal auf deinem Radar?" |
| **Meeting-CTA** | Wenn Intent-Signale vorliegen | "20 Minuten Gespräch nächste Woche wert?" |
| **Ressourcen-CTA** | Nurture-Phase, Glaubwürdigkeit aufbauen | "Ich habe ein [Brief/Analyse] erstellt — soll ich es schicken?" |
| **Intro-CTA** | Multi-threaded, anderer Stakeholder nötig | "Wer in deinem Team verantwortet [Funktion]?" |

## Betreffzeilen-Methodik (nur E-Mail)

Erzeuge pro E-Mail 3 Betreffzeilen-Varianten, die unterschiedliche Blickwinkel testen:

| Varianten-Typ | Muster | Beispiel |
| --- | --- | --- |
| **Trigger-basiert** | Verweist auf das konkrete Signal | "[Unternehmen]s EMEA-Expansion + [Thema]" |
| **Frage-basiert** | Formuliert das Problem als Frage | "Wie geht [Unternehmen] mit [Herausforderung] um?" |
| **Ergebnis-basiert** | Führt mit dem Resultat | "[Kennzahl-Verbesserung] für Teams in [ihrer Branche]" |

Betreffzeilen-Regeln: unter 50 Zeichen bevorzugt, kein ALL CAPS, keine Spam-Trigger-Wörter, keine falsche Dringlichkeit, keine irreführenden Re:- oder Fwd:-Präfixe.

## Sequenz-Architektur

Variiere bei Multi-Touch-Sequenzen mit jedem Touch den Blickwinkel:

| Touch | Timing | Blickwinkel | Kanal |
| --- | --- | --- | --- |
| 1 | Tag 0 | Primärer Hook + Value Statement | E-Mail oder LinkedIn |
| 2 | Tag 3–4 | Neuer Proof Point oder Case-Study-Blickwinkel | Gleicher oder alternativer Kanal |
| 3 | Tag 7–8 | Branchen-Insight oder Ressourcen-Angebot | Alternativer Kanal |
| 4 | Tag 14 | Anderer Stakeholder-Blickwinkel oder Empfehlungs-Ask | E-Mail |
| 5 | Tag 21–28 | Break-up: direkter Ask zu Fit/Timing | E-Mail |

### Sequenz-Regeln

- Jeder Touch muss neuen Mehrwert oder einen neuen Blickwinkel bringen — niemals "melde mich nur nochmal" oder "schiebe das hoch".
- Antwortet der Prospect zu irgendeinem Zeitpunkt, verlasse die Sequenz und antworte gesprächig.
- Respektiere Opt-out-Signale: explizite Anfragen, Auto-Replies (Abwesenheit) oder Do-not-contact auf Unternehmensebene.
- Passe das Timing an die Seniorität an: C-Level bekommt längere Abstände zwischen den Touches.
- Maximale Sequenzlänge: 5 Touches über 4 Wochen bei Cold-Outreach.

## Ausgabevorlage — Outreach-Paket

```
# Outreach: [Prospect-Name] bei [Unternehmen]
**Kanal**: [E-Mail / LinkedIn / Multi-Channel]
**Sequenzlänge**: [Einzelnachricht / X-Touch-Sequenz]
**Prospect-Kontext**: [1–2 Sätze Recherche-Zusammenfassung]

## Recherche-Zusammenfassung
- **Rolle**: [Titel, Verantwortungsbereich, Betriebszugehörigkeit]
- **Signale**: [zentrale identifizierte Trigger — mit Datum und Quelle]
- **Gewählte Aufhänger**: [für diese Outreach gewählte, gerankte Aufhänger]

## Nachricht 1: Erst-Outreach
**Betreffzeilen-Optionen** (nur E-Mail):
1. [Variante A]
2. [Variante B]
3. [Variante C]

**Body**:
[Vollständiger Nachrichtentext — Klartext, keine Markdown-Formatierung]

---

## Nachricht 2: Follow-up 1
**Timing**: [Tage nach Nachricht 1]
**Blickwinkel**: [was in diesem Touch neu ist]

**Betreff**: [Reply im Thread oder neuer Betreff]

**Body**:
[Vollständiger Nachrichtentext]

---

[Für jeden Sequenz-Touch fortsetzen]

## Personalisierungs-Notizen
- [Warum die jeweiligen Aufhänger gewählt wurden]
- [Alternative Blickwinkel, falls diese nicht zünden]
- [Kontakte zum CC oder Verweis, wenn der Thread aufgewärmt wird]
```

## Leitplanken

1. Erfinde niemals Prospect-Details. Alle Namen, Titel, Unternehmensfakten und Aktivitäten müssen aus CRM, Enrichment, Websuche oder Nutzereingabe stammen. Ist die Recherche dünn, verwende Platzhalter in eckigen Klammern: "[konkretes Signal einfügen]."
2. Erfinde niemals gemeinsame Kontakte. Verweise nur dann auf einen gemeinsamen Kontakt, wenn er vom Nutzer oder durch CRM-Daten bestätigt ist.
3. Opt-out-Bewusstsein. Zeigt das CRM Opt-out, Do-not-contact oder einen abgemeldeten Status, lehne das Verfassen der Outreach ab und weise auf die Einschränkung hin.
4. Quellenkennzeichnung. Tagge die Recherche — [Aus CRM], [Aus LinkedIn], [Aus Websuche], [Aus Nutzereingabe], [KI-Entwurf].

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Outreach-Paket zu erhalten.
