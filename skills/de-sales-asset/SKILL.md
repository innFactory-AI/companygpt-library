---
name: de-sales-asset
description: Erstellt maßgeschneiderte One-Pager, Landingpages, Case-Study-Entwürfe und Demo-Narrative, personalisiert auf einen konkreten Deal und eine Buyer-Persona. Verwende ihn, wenn du Collateral für einen bestimmten Deal vorbereitest, Leave-behind-Material baust oder Standard-Assets für einen Interessenten anpasst. Auslösen mit "One-Pager erstellen für", "Sales-Deck für [Deal]", "dieses Asset anpassen für".
---

# Sales-Asset-Skill

Erstelle dealspezifische Sales-Collateral — One-Pager, Case-Study-Entwürfe, Executive Summaries, Demo-Narrative und Proposal-Einschübe —, personalisiert auf die Branche, die Rolle und die genannten Prioritäten des Buyers. Alle Produktinformationen, Case Studies, Preise und der Deal-Kontext kommen von dir, aus companyRAG-Sammlungen oder aus einem angebundenen CRM.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Deal-Phase, Deal-Wert, Stakeholder, Wettbewerbssituation, Closed-Won-Notizen |
| **companyRAG-Sammlungen** | Produktspezifikationen, Case Studies, Proof Points, Branchen-Referenzen |
| **Datei-Upload** | Discovery-Notizen, Battlecards, Account-Research, Call-Zusammenfassungen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Asset-Typ-Routing

Bestimme das passende Asset-Format anhand der Sales-Situation:

| Situation | Empfohlenes Asset | Zweck |
| --- | --- | --- |
| Erstes Meeting — Leave-behind für den Champion | **One-Pager** | Kompakter Überblick, den der Champion intern weiterleiten kann |
| Engagement mit Executive Sponsor | **Executive Summary** | Auf Geschäftsergebnisse fokussiert, minimaler technischer Detailgrad |
| Technische Evaluierung läuft | **Solution Brief** | Fokus auf Architektur, Integration, Security, Compliance |
| Interessent fragt "Wer nutzt das noch?" | **Case-Study-Entwurf** | Social Proof, abgebildet auf seine Branche / seinen Use Case |
| Demo terminiert — Narrativ nötig | **Demo-Narrativ** | Storyline, die den Demo-Ablauf an seinen konkreten Pain knüpft |
| Abschnitt für Proposal oder RFP-Antwort | **Proposal-Einschub** | Zugeschnittener Abschnitt zu bestimmten Bewertungskriterien |
| Multi-Stakeholder-Deal — unterschiedliche Bedürfnisse | **Messaging-Matrix** | Stakeholder-spezifische Value Props in einem Referenzdokument |

Lässt sich die Anfrage des Nutzers nicht eindeutig einem Typ zuordnen, stelle vor dem Entwurf klärende Fragen zu Zielgruppe, Timing und Verwendungszweck.

## Asset-Erstellungs-Workflow

```
1. ASSET-TYP und Zielgruppe IDENTIFIZIEREN
   |
   +--> Auf Asset-Typ routen (Tabelle oben)
   +--> Primäre Zielgruppe bestimmen: Rolle, Seniorität, technische Tiefe
   +--> Sekundäre Zielgruppe bestimmen: Wer sieht das noch?
   +--> Kontext klären: Wo im Deal-Zyklus, was hat die Anfrage ausgelöst
   |
2. DEAL-KONTEXT SAMMELN
   |
   +--> Aus dem CRM: Deal-Phase, Wert, Stakeholder, Wettbewerbssituation
   +--> Vom Nutzer: konkrete Pain Points, Bewertungskriterien, Buyer-Sprache
   +--> Aus companyRAG-Sammlungen: Produktspezifikationen, Case Studies, Proof Points
   +--> Aus vorherigen Skills: Account-Research, Call-Zusammenfassungen, Battlecard-Infos
   |
3. MESSAGING auf die Persona ABBILDEN
   |
   +--> Persona-Message-Matrix anwenden (siehe unten)
   +--> Value Propositions nach Relevanz für diesen Buyer priorisieren
   +--> Proof Points wählen, die zu seiner Branche und Unternehmensgröße passen
   +--> Sprachregister an Seniorität und Funktion der Zielgruppe anpassen
   |
4. ENTWURF GENERIEREN
   |
   +--> Asset-spezifische Vorlage anwenden (siehe Asset-Vorlagen unten)
   +--> Sicherstellen, dass jede Aussage durch eine Quelle gestützt oder als ungestützt markiert ist
   +--> Vor der Präsentation gegen die Qualitätskriterien prüfen
   |
5. PRÜFEN und VERFEINERN
   |
   +--> Asset-Review-Checkliste durchgehen (siehe unten)
   +--> Abschnitte markieren, die Input oder Freigabe des Nutzers brauchen
   +--> Alternative Framings für zentrale Botschaften vorschlagen
```

## Persona-Message-Matrix

Stimme den Messaging-Schwerpunkt auf Rolle und Prioritäten des Buyers ab:

| Persona | Hauptanliegen | Messaging-Schwerpunkt | Art des Proof Points |
| --- | --- | --- | --- |
| **C-Level / Executive** | Umsatzwirkung, Risiko, strategisches Alignment | Geschäftsergebnisse, ROI, Wettbewerbsvorteil | Umsatzkennzahlen, Marktposition |
| **VP / Director** | Team-Produktivität, Budget-Rechtfertigung | Operative Effizienz, Time-to-Value, TCO | Produktivitätsgewinne, Kosteneinsparungen |
| **Manager / Team Lead** | Auswirkung im Alltag, Adoption, Workflow-Fit | Bedienbarkeit, Integration, Support-Qualität | Nutzerzufriedenheit, Adoptionsraten |
| **Technischer Evaluator** | Architektur, Security, Skalierbarkeit | Technische Spezifikationen, Compliance, API-Abdeckung | Technische Benchmarks, Zertifizierungen |
| **Einkauf** | Kosten, Vertragsbedingungen, Lieferantenrisiko | Preistransparenz, Lieferantenstabilität, SLAs | Finanzielle Stabilität, Kundenanzahl |
| **Endnutzer / Practitioner** | Tägliche Arbeit, Lernkurve, Zuverlässigkeit | Usability, Geschwindigkeit, Zuverlässigkeit, Support | Nutzer-Testimonials, Usability-Kennzahlen |

### Sprachregister nach Seniorität

| Zielgruppen-Ebene | Register | Vermeiden |
| --- | --- | --- |
| **Executive** | Knapp, ergebnisorientiert, strategisches Framing, minimaler Jargon | Feature-Listen, technische Spezifikationen, Akronyme |
| **Management** | Ausgewogen — Ergebnisse mit stützenden Details, kennzahlengetrieben | Vage Aussagen ohne Zahlen, übermäßige Länge |
| **Practitioner** | Konkret, praktisch, workflow-orientiert, technisch präzise | Abstrakte Plattitüden, Marketing-Superlative |

## Asset-Vorlagen

### One-Pager-Vorlage

```
# [Lösungsname] für [Branche / Use Case]

## Die Herausforderung
[1-2 Sätze, die das konkrete Problem dieses Interessenten beschreiben — in seiner Sprache, nicht in deiner]

## Wie [Lösung] hilft
[3-4 Bullet Points — jeweils strukturiert als: Ergebnis → Wie es funktioniert → Proof]
- **[Ergebnis]**: [Kurzer Mechanismus] — [Proof Point mit Kennzahl]
- **[Ergebnis]**: [Kurzer Mechanismus] — [Proof Point mit Kennzahl]
- **[Ergebnis]**: [Kurzer Mechanismus] — [Proof Point mit Kennzahl]

## Warum [Unternehmensname] im Speziellen
[2-3 Sätze, die deine Differenzierung mit den genannten Bewertungskriterien oder der Wettbewerbssituation verknüpfen]

## Kunden-Proof
"[Zitat eines Referenzkunden aus seiner Branche oder mit ähnlichem Use Case]"
— [Name, Titel, Unternehmen]   |   [erreichte Schlüsselkennzahl]

## Nächster Schritt
[Konkreter CTA passend zur Phase im Deal-Zyklus]
```

### Executive-Summary-Vorlage

```
# Executive Summary: [Lösung] für [Unternehmen des Interessenten]

**Erstellt für**: [Name, Titel]
**Datum**: [Datum]

## Strategischer Kontext
[2-3 Sätze zur geschäftlichen Herausforderung, gerahmt durch die strategischen Prioritäten — referenziere Geschäftsbericht, Earnings Call oder genannte Ziele, falls verfügbar]

## Empfohlener Ansatz
[Kurze Beschreibung der vorgeschlagenen Lösung — Ergebnisse zuerst, dann das Wie — nie Feature-first]

## Erwartete Geschäftswirkung
| Ergebnisbereich       | Ist-Zustand          | Prognostizierte Verbesserung | Grundlage           |
| --------------------- | -------------------- | ---------------------------- | ------------------- |
| [Bereich]             | [Kennzahl, falls bekannt] | [Prognostizierte Änderung] | [Quelle/Vergleichswerte] |

## Risikominderung
[Adressiere die 2-3 größten Bedenken, die dieser Executive wahrscheinlich hat — Security, Integration, Change Management, Lieferantenstabilität]

## Investitionsüberblick
[Übergeordnetes Framing — keine detaillierten Preise. Positioniere als Investition mit erwarteter Rendite, nicht als Kostenfaktor]

## Empfohlener nächster Schritt
[Konkreter, für Executives angemessener Call-to-Action]
```

### Case-Study-Entwurf-Vorlage

```
# [Kundenname]: [Schlagzeilen-Ergebnis]

## Unternehmensprofil
- **Branche**: [Sektor]  |  **Größe**: [Mitarbeitende / Umsatz]
- **Use Case**: [Was sie erreichen wollten]

## Die Herausforderung
[3-4 Sätze — das konkrete Problem, seine geschäftliche Auswirkung und warum frühere Ansätze scheiterten]

## Die Lösung
[Wie sie deine Lösung eingeführt haben — Timeline, Umfang, Vorgehen. Fokus auf Entscheidungen, nicht auf Features]

## Ergebnisse
| Kennzahl            | Vorher           | Nachher          | Verbesserung        |
| ------------------- | ---------------- | ---------------- | ------------------- |
| [KPI]               | [Wert]           | [Wert]           | [% oder absolut]    |

## Schlüsselzitat
"[Kundenzitat, das die Transformation einfängt]"
— [Name, Titel]

## Relevanz für [Interessent]
[2-3 Sätze, die erklären, warum diese Case Study für die Situation des Interessenten besonders relevant ist]
```

### Demo-Narrativ-Vorlage

```
# Demo-Narrativ: [Unternehmen des Interessenten]

**Zielgruppe**: [Namen, Rollen]
**Dauer**: [geplante Zeit]
**Ziel**: [Wie Erfolg für diese Demo aussieht]

## Eröffnungskontext (2 Min.)
[Verknüpfe die genannte Herausforderung mit dem, was sie gleich sehen. Referenziere ein konkretes Gespräch oder einen Discovery-Befund.]

## Szene 1: [Pain Point → Capability] (X Min.)
- **Setup**: "[Beschreibe das Szenario in ihren Worten]"
- **Zeigen**: [Konkretes Feature/Workflow zum Demonstrieren]
- **Ergebnis**: "[Was das für ihr Team bedeutet]"
- **Check-in-Frage**: "[Reaktion und Relevanz abklopfen]"

## Szene 2: [Pain Point → Capability] (X Min.)
[Gleiche Struktur]

## Szene 3: [Differenzierungs-Moment] (X Min.)
- **Setup**: "[Hier unterscheiden wir uns von Alternativen]"
- **Zeigen**: [Einzigartige Capability, abgebildet auf ihre Bewertungskriterien]
- **Brücke**: "[Zurück zu ihren Entscheidungskriterien]"

## Abschluss (3 Min.)
- Recap: [3 zentrale Takeaways, abgebildet auf ihre Prioritäten]
- Ask: "[Vorschlag für den nächsten Schritt]"
- Leave-behind: [Was du danach schickst — One-Pager, Trial, Proposal]

## Backup-Szenen
[2-3 zusätzliche Features bereit, falls konkrete Fragen aufkommen oder die Zeit reicht — nur auf Nachfrage zeigen]
```

### Messaging-Matrix-Vorlage

```
# Messaging-Matrix: [Deal-Name]

| Stakeholder         | Titel          | Hauptanliegen        | Value Prop                   | Proof Point               | Hauptein­wand           | Talk Track                    |
| ------------------- | -------------- | -------------------- | ---------------------------- | ------------------------- | ----------------------- | ----------------------------- |
| [Name]              | [Rolle]        | [sein Hauptanliegen] | [zugeschnittene Value-Aussage] | [relevante Case/Kennzahl] | [wahrscheinlicher Einwand] | [Wie das Gespräch zu rahmen ist] |
```

## Asset-Review-Checkliste

Prüfe vor der Auslieferung jedes Assets:

| Kriterium | Prüfung |
| --- | --- |
| **Zielgruppen-Alignment** | Passen Sprache, Tiefe und Schwerpunkt zur vorgesehenen Leserschaft? |
| **Aussagen-Belegbarkeit** | Ist jede Aussage durch einen belegten Proof Point gestützt oder markiert? |
| **Interessenten-Spezifität** | Gilt das Asset nur für diesen Interessenten oder ist es generisch? |
| **Wettbewerbsbewusstsein** | Adressiert es bekannte Alternativen, ohne Wettbewerber negativ zu nennen? |
| **CTA-Angemessenheit** | Passt der Call-to-Action zur Deal-Phase? |
| **Längenangemessenheit** | One-Pager: 1 Seite. Exec Summary: 1-2 Seiten. Case Study: 1-2 Seiten. |
| **Markenkonsistenz** | Entspricht es den Brand-Voice-Richtlinien des Kunden (falls vorhanden)? |
| **Formatierung** | Professionell, sauber, keine Markdown-Artefakte in kundenseitiger Copy |
| **Recht/Compliance** | Keine nicht freigegebenen Aussagen, korrekte Case-Study-Daten, keine NDA-Verstöße |

## Leitplanken

1. Erfinde niemals Case Studies oder Kundenzitate. Alle Kundennamen, Ergebnisse und Testimonials müssen vom Nutzer oder aus companyRAG-Sammlungen stammen. Verwende "[Kundenreferenz für diese Branche einfügen]", wenn keine vorliegen.
2. Erzeuge niemals Produktfähigkeiten, die nicht vom Nutzer bereitgestellt wurden. Wenn Produktdetails nicht in companyRAG-Sammlungen oder im Nutzer-Input vorliegen, markiere mit "[Mit Produktteam verifizieren]", statt Features anzunehmen.
3. Erfinde niemals Kennzahlen oder ROI-Werte. Prognosen zur Geschäftswirkung müssen auf bereitgestellten Case-Daten beruhen oder mit "[Platzhalter — Validierung durch Customer-Success-Team nötig]" markiert sein.
4. Quellenkennzeichnung. Tagge die Herkunft des Inhalts — [Aus companyRAG-Sammlung], [Aus Nutzer-Input], [Aus CRM], [Aus Deal-Kontext], [KI-Entwurf — verifizieren].

> **Tipp:** Fordere über companyFILES eine PPTX-Ausgabe an, um einen formatierten Slide-Deck zu erhalten, oder eine DOCX-Datei für einen sofort verteilbaren One-Pager. Für längere Unterlagen sind auch PDF und Markdown verfügbar.
