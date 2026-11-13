---
name: de-escalation-brief
description: Verpacke ein Kundenproblem in einen strukturierten Eskalations-Brief für Engineering oder Leadership mit quantifizierter geschäftlicher Auswirkung. Verwende ihn, wenn ein Kundenproblem Aufmerksamkeit auf Führungsebene, eine Priorisierung im Engineering oder eine bereichsübergreifende Abstimmung braucht. Auslösen mit "diese Eskalation aufbereiten", "Eskalation verpacken für", "das braucht Aufmerksamkeit vom Engineering".
---

# Eskalations-Brief-Skill

Verwandle Kundenprobleme in strukturierte Eskalations-Briefe, die die geschäftliche Auswirkung beziffern und konkrete Maßnahmen empfehlen. Die Details zum Problem kommen von dir, aus einer verbundenen MCP-Quelle oder aus companyRAG-Collections.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Support-Plattform via MCP** (z. B. Zendesk, Intercom, Freshdesk) | Ticket-Historie, Lösungsversuche, Kommunikationsprotokoll mit dem Kunden |
| **CRM via MCP** (z. B. HubSpot, Salesforce) | Account-Wert, Verlängerungsdatum, strategische Bedeutung, Ansprechpartner der Stakeholder |
| **companyRAG / Datei-Upload** | Interne Notizen, frühere Eskalationen, technischer Kontext |

> **Keine verbundene Quelle?** Stelle die Daten im Chat bereit oder lade die relevanten Dateien hoch — der Skill funktioniert auf dieselbe Weise.

## Workflow zur Aufbereitung einer Eskalation

Führe diese Schritte für jede Eskalation der Reihe nach aus.

### Schritt 1: Schweregrad bewerten

Klassifiziere das Problem anhand zweier Dimensionen: Kundenauswirkung und Geschäftsrisiko.

**Kundenauswirkung:**

| Stufe | Definition | Beispiele |
| --- | --- | --- |
| **Critical** (kritisch) | Der zentrale Workflow des Kunden ist ohne Workaround blockiert | Plattform-Ausfall, Datenverlust, Sicherheitsvorfall, vollständiger Funktionsausfall |
| **High** (hoch) | Erhebliche Beeinträchtigung mehrerer Benutzer oder zentraler Workflows | Performance-Probleme, teilweiser Funktionsausfall, Ausfall einer Integration |
| **Medium** (mittel) | Spürbares Problem mit verfügbarem, tragfähigem Workaround | UI-Fehler, kleinere Funktionslücken, unkritische Integrationsprobleme |
| **Low** (niedrig) | Kosmetisches oder geringfügiges Problem, das keinen Workflow blockiert | Anzeigefehler, Lücken in der Dokumentation, Verbesserungswünsche |

**Geschäftsrisiko:**

| Stufe | Definition | Indikatoren |
| --- | --- | --- |
| **Critical** (kritisch) | Unmittelbares Churn- oder Rechtsrisiko | Kunde hat mit Nichtverlängerung, rechtlichen Schritten oder öffentlicher Offenlegung gedroht |
| **High** (hoch) | Verlängerung oder Expansion gefährdet | Kunde nähert sich der Verlängerung mit ungelösten Problemen, Expansionsdeal stockt |
| **Medium** (mittel) | Beziehungsschaden, aber kein unmittelbares kommerzielles Risiko | Frustration des Kunden wächst, NPS sinkt, Champion verliert intern an Glaubwürdigkeit |
| **Low** (niedrig) | Isoliertes Problem, Beziehung stabil | Einmaliges Problem, Kunde zeigt Verständnis, kein Muster |

**Kombinierter Schweregrad** = der höhere Wert der beiden Dimensionen. Eine mittlere Kundenauswirkung mit kritischem Geschäftsrisiko ist eine kritische Eskalation.

### Schritt 2: Kontext sammeln

Verschaffe dir ein vollständiges Bild, bevor du den Brief verfasst. Unvollständige Eskalationen werden deprioritisiert.

| Kontextelement | Quelle | Details |
| --- | --- | --- |
| **Problembeschreibung** | Support-Ticket, CSM-Notizen | Was passiert, wann es begann, wer betroffen ist |
| **Zeitverlauf** | Support-Plattform | Wann gemeldet, unternommene Lösungsversuche, aktueller Status |
| **Betroffener Umfang** | Kunde, Support-Daten | Anzahl betroffener Benutzer, welche Funktionen/Workflows, Häufigkeit |
| **Workaround-Status** | Support-Team | Gibt es einen Workaround? Nutzt der Kunde ihn? Ist er nachhaltig? |
| **Lösungsversuche** | Ticket-Historie im Support | Was wurde versucht, von wem, mit welchem Ergebnis |
| **Kundenerwartung** | CSM, Kundenkommunikation | Was der Kunde hinsichtlich Zeitrahmen und Lösung erwartet |
| **Verwandte Probleme** | Support-Plattform, Engineering | Ist dies ein bekannter Bug? Sind andere Kunden betroffen? Gibt es ein bestehendes Ticket? |

### Schritt 3: Geschäftliche Auswirkung quantifizieren

Übersetze das Problem in Begriffe, die die interne Priorisierung vorantreiben. Engineering und Leadership reagieren auf geschäftliche Auswirkung, nicht auf Frustrationsgrade.

| Auswirkungsdimension | Quantifizierungsansatz |
| --- | --- |
| **Gefährdeter Umsatz** | ARR der betroffenen Accounts. Wenn die Verlängerung innerhalb von 90 Tagen ansteht, ausdrücklich kennzeichnen. |
| **Benutzerauswirkung** | Anzahl betroffener Benutzer × Häufigkeit der Auswirkung. Tägliche Blocker wiegen schwerer als wöchentliche Unannehmlichkeiten. |
| **Strategischer Wert** | Ist dies ein Logo-Account, ein Referenzkunde, ein Expansionsziel oder ein strategisches Segment? |
| **Ausstrahlungsrisiko** | Sind andere Kunden betroffen oder werden es voraussichtlich sein? Handelt es sich um ein systemisches Problem? |
| **Vertragliche Exposition** | Werden SLA-Zusagen verletzt? Bestehen Risiken durch Vertragsstrafen? |
| **Beziehungskapital** | Wie viel Goodwill wurde bereits aufgewendet? Hat der CSM oder eine Führungskraft bereits Zusagen gemacht? |

Verwende tatsächliche Zahlen aus CRM- und Support-Daten. Schätze Umsätze oder Vertragswerte niemals aus dem Gedächtnis.

### Schritt 4: Eskalations-Brief verfassen

Verwende die untenstehende Output-Vorlage. Jedes Feld muss ausgefüllt oder ausdrücklich als unbekannt gekennzeichnet werden.

### Schritt 5: Maßnahme empfehlen

Empfiehl auf Basis von Schweregrad und Kontext eine konkrete Reaktion.

| Schweregrad | Empfohlene Reaktion | Interne Weiterleitung |
| --- | --- | --- |
| **Critical** (kritisch) | War Room / sofortige Aufmerksamkeit vom Engineering + Benachrichtigung des Executive Sponsors | Engineering Lead + CS-Leadership + Account Executive |
| **High** (hoch) | Priorisiertes Engineering-Ticket + CSM-geführter Kommunikationsplan mit dem Kunden | Engineering Manager + CS Manager |
| **Medium** (mittel) | Engineering-Ticket mit geschäftlichem Kontext + CSM-Follow-up-Rhythmus | Engineering-Team über Standard-Queue mit Prioritätskennzeichnung |
| **Low** (niedrig) | Standard-Support-/Engineering-Queue mit angehängtem Kontext | Support-Team oder Produkt-Backlog |

## Output-Vorlage — Eskalations-Brief

```
ESKALATIONS-BRIEF
Datum: [Datum]
Erstellt von: [CSM-Name]
Schweregrad: [CRITICAL / HIGH / MEDIUM / LOW]

ACCOUNT-KONTEXT:
  Account: [Name]
  ARR: [Wert]
  Verlängerungsdatum: [Datum]
  Strategische Stufe: [Enterprise / Mid-Market / SMB]
  Account-Gesundheit: [aus Health Score, falls verfügbar]
  Account-Owner: [CSM-Name]
  Executive Sponsor: [Name, falls zugewiesen]

PROBLEMZUSAMMENFASSUNG:
  [Beschreibung des Problems in 2-3 Sätzen in einfacher Sprache]

KUNDENAUSWIRKUNG:
  Auswirkungsstufe: [Critical / High / Medium / Low]
  Betroffene Benutzer: [Anzahl]
  Blockierte Workflows: [Liste]
  Workaround verfügbar: [Ja — beschreiben / Nein]
  Dauer: [wie lange das Problem bereits besteht]

GESCHÄFTSRISIKO:
  Risikostufe: [Critical / High / Medium / Low]
  Gefährdeter Umsatz: [ARR-Betrag]
  Nähe zur Verlängerung: [X Tage bis zur Verlängerung]
  Strategische Faktoren: [Referenzkunde, Expansionsmöglichkeit usw.]
  Vertragliche Exposition: [SLA-Verletzungen, Risiko von Vertragsstrafen]

ZEITVERLAUF:
  [Datum] — Problem erstmals gemeldet
  [Datum] — [Lösungsversuch und Ergebnis]
  [Datum] — [Eskalationsauslöser / was sich geändert hat]
  [Datum] — Aktueller Status

LÖSUNGSVERSUCHE:
  1. [was versucht wurde] → [Ergebnis]
  2. [was versucht wurde] → [Ergebnis]

KUNDENERWARTUNG:
  [Was der Kunde erwartet und bis wann]

ANGEFORDERTE MASSNAHME:
  [Konkrete Anfrage — z. B. "Root-Cause-Analyse durch das Engineering innerhalb von 48 Stunden"
   oder "Executive Call zur Neujustierung der Erwartungen bis Freitag"]

EMPFOHLENE INTERNE WEITERLEITUNG:
  Engineering: [Team/Person]
  CS-Leadership: [Person]
  Account Executive: [Person, bei kommerziellem Risiko]
  Executive: [Person, bei kritischem Schweregrad]

UNTERSTÜTZENDE MATERIALIEN:
  - [Link zum Support-Ticket]
  - [Link zum CRM-Account]
  - [Screenshots, Logs oder andere Nachweise]
```

## Anti-Patterns — Häufige Fehler bei Eskalationen

| Anti-Pattern | Warum es scheitert | Stattdessen |
| --- | --- | --- |
| Emotionen statt Fakten eskalieren | "Der Kunde ist wirklich verärgert" liefert keine handlungsrelevante Information | Quantifiziere die Auswirkung: betroffene Benutzer, gefährdeter Umsatz, Dauer |
| Lösungshistorie überspringen | Das Engineering verschwendet Zeit damit, bekannte Sackgassen erneut zu untersuchen | Dokumentiere jeden Versuch und sein Ergebnis |
| Vage Auswirkungsaussagen | "Das ist ein großer Account" vermittelt keine Dringlichkeit | Nenne ARR, Verlängerungsdatum und strategische Stufe ausdrücklich |
| Eskalieren ohne konkrete Anfrage | Empfänger wissen nicht, welche Maßnahme sie ergreifen sollen | Nenne genau, was du benötigst und bis wann |
| Geringfügige Probleme übermäßig eskalieren | Untergräbt die Glaubwürdigkeit künftiger Eskalationen | Nutze die Schweregradmatrix ehrlich; nicht jedes Problem ist kritisch |

## Leitplanken

- Erfinde niemals Account-Werte, Umsatzzahlen, Verlängerungsdaten oder Ticket-Details. Alle Daten müssen vom Benutzer, aus dem CRM oder von der Support-Plattform stammen. Gib bei fehlenden Daten "unbekannt — Untersuchung erforderlich" an.
- Nimm niemals den emotionalen Zustand des Kunden an. Berichte beobachtbare Signale (was er gesagt hat, Ticket-Volumen, abgesagte Meetings) statt abgeleiteter Gefühle.
- Eskalations-Briefe müssen vor dem Versand vom CSM geprüft werden. Niemals automatisch versenden.
- Kennzeichne jede Aussage mit ihrer Quelle: `[Aus Account-Daten]`, `[Aus Eskalations-Framework]` oder `[CSM-Einschätzung]`.

> **Tipp:** Fordere eine DOCX-Ausgabe über companyFILES an, um einen formatierten, versandfertigen Eskalations-Brief zu erhalten.
