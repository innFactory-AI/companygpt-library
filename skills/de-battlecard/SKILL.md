---
name: de-battlecard
description: Erstellt Direktvergleiche mit Wettbewerbern inklusive Win/Loss-Mustern, Einwandbehandlung und Differenzierungs-Talk-Tracks. Verwende ihn, wenn du dich auf einen umkämpften Deal vorbereitest, einen neuen Vertriebler briefst oder Competitive Intelligence aktualisierst. Auslösen mit "Battlecard erstellen für", "Wettbewerbervergleich", "wie konkurrieren wir gegen".
---

# Battlecard-Skill

Erstelle Wettbewerbs-Battlecards mit FIA (Fact-Impact-Act), Positionierungsmatrizen und strukturierter Einwandbehandlung. Der Skill liefert die Struktur, nicht die Intelligence: Alle Wettbewerbsdaten kommen von dir, aus companyRAG-Sammlungen oder aus der Websuche.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Deal-Kontext, Wettbewerbssituation, Closed-Won/Closed-Lost-Notizen, Stakeholder |
| **Battlecard-Bibliothek / companyRAG-Sammlungen** | Bestehende Wettbewerbs-Intelligence, Proof Points, Referenzkunden |
| **Datei-Upload** | RFPs, Discovery-Call-Notizen, Wettbewerbsanalysen, Pricing-Unterlagen |
| **Websuche** | Aktuelle, öffentlich verfügbare Wettbewerberinformationen (nur belegbare Fakten) |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Komplexität und Tiefe

Die Frameworks dieses Skills (FIA, LAER, Win/Loss-Analyse, Positionierungsmatrix) gelten universell über alle Komplexitätsstufen des Sales Motion Complexity Assessment hinweg, das die Sales-Skills gemeinsam nutzen (Zykluslänge, Deal-Wert, Anzahl der Stakeholder, Lösungskomplexität — jeweils relativ zu den Normen des Kunden). Komplexere Deals rechtfertigen detailliertere Battlecards und eine tiefere Wettbewerbsanalyse, die grundlegende Methodik ändert sich jedoch nicht. Passe die Tiefe an die Bedeutung des Deals an: eine vollständige Battlecard mit Landmine-Fragen für einen High-Complexity-Deal; eine fokussierte FIA-Zusammenfassung für einen Low-Complexity-Deal.

## FIA-Battlecard-Methodik

Das Fact-Impact-Act-Framework (FIA) strukturiert Competitive Intelligence in handlungsfähige Battlecards.

### Struktur pro Wettbewerbspunkt

| Ebene | Definition | Beispielstruktur |
| --- | --- | --- |
| **Fact** | Spezifische, überprüfbare Intelligence über den Wettbewerber. Muss belegt und aktuell sein. Keine Spekulation, keine Behauptungen aus Trainingsdaten. | "Wettbewerber erfordert [spezifische technische Einschränkung]" -- [Quelle: Battlecard-Bibliothek / Nutzereingabe / Websuche] |
| **Impact** | Warum dieser Fakt für den Deal relevant ist. Verbindet ihn mit der konkreten Situation oder den Bewertungskriterien des Kunden. | "Das bedeutet, der Kunde müsste [konkrete Konsequenz], was seine [genannte Priorität] betrifft." |
| **Act** | Was der Vertriebler sagen oder tun sollte. Konkreter Talk-Track, Frage oder Proof Point. | "Frage: 'Wie wichtig ist [Fähigkeit] für euer Team?' Teile dann [Proof Point]." |

### Battlecard-Abschnitte (FIA angewendet)

1. Wettbewerber-Überblick : Unternehmenskontext, Marktposition, typisches Kundenprofil (alles belegt, nie generiert)
2. Stärken mit Neutralisierung : Wettbewerbsvorteile + FIA zur Neutralisierung jeder einzelnen
3. Schwächen mit Ausnutzung : Schwachstellen des Wettbewerbers + FIA, um jede zu nutzen
4. Pricing-Vergleichs-Framework : Struktur für den Vergleich von Preismodellen (nicht der tatsächlichen Preise). Dimensionen: Modelltyp, TCO-Faktoren, versteckte Kosten, Value-pro-Einheit-Methodik
5. Einwand-Antwort-Paare : Mit LAER auf Antworten abgebildet (siehe unten)
6. Landmine-Fragen : Discovery-Fragen pro Schwachstellenkategorie (siehe unten)
7. Kunden-Proof-Points : Vorlage zum Strukturieren von Evidenz -- aus companyRAG-Sammlungen befüllt, nie generiert

Nutze die Battlecard-Abschnitte und die FIA-Methodik oben als strukturelle Vorlage; erweitere jeden Abschnitt mit belegter Intelligence von dir oder aus companyRAG-Sammlungen.

## Wettbewerbs-Positionierungsmatrix

Framework für den Vergleich von Lösungen über Bewertungskriterien hinweg:

1. Bewertungskriterien des Kunden identifizieren : Aus RFP, genannten Anforderungen oder Discovery. Niemals Kriterien annehmen.
2. Kriterien klassifizieren : Must-win (Deal-Breaker bei Schwäche) vs. Nice-to-have (Differenzierer bei Stärke)
3. Pro Lösung bewerten : Strong / Neutral / Weak (stark / neutral / schwach) ausschließlich auf Basis von Evidenz.
4. Positionierungswinkel identifizieren :   - Must-win + du stark + Wettbewerber schwach = primäre Differenzierung   - Must-win + du schwach = Risikobereich, der Gegenmaßnahmen erfordert   - Nice-to-have + du stark = sekundäre Talking Points

## Einwandbehandlung (Carew LAER Bonding Process)

Wende Listen-Acknowledge-Explore-Respond auf jeden Wettbewerbseinwand in der Battlecard an. Die zentrale Disziplin: Erkunde das eigentliche Anliegen, bevor du antwortest -- der genannte Einwand ist oft nur ein Stellvertreter.

**Wichtige Abgrenzung**: Dies ist der Carew International LAER Bonding Process, NICHT das TSIA-Modell Land-Adopt-Expand-Renew, das sich das Akronym teilt.

Ordne Einwand-Antwort-Paare nach Kategorie (Pricing, Funktionslücken, Compliance/Security, Referenzen, Reife des Anbieters) und ordne jeder die Evidenz aus den companyRAG-Sammlungen zu.

## Landmine-Fragen-Methodik

Fragen, die Schwächen des Wettbewerbers während der Discovery aufdecken:

| Schwachstellenkategorie | Fragemuster | Was sie aufdeckt |
| --- | --- | --- |
| **Liefer-/Erfüllungsrisiko** | "Wie wichtig ist [zuverlässige Lieferung / Planbarkeit der Implementierung]?" | Inkonsistente Lieferung, Verzögerungen |
| **Gesamtbetriebskosten (TCO)** | "Welche weiteren Kosten neben dem genannten Preis fließen in eure Bewertung ein?" | Versteckte Kosten (Services, Integrationen, Schulung) |
| **Integration/Interoperabilität** | "Wie muss [die Lösung] mit euren bestehenden [Systemen/Tools] zusammenarbeiten?" | Ökosystem-Lock-in, Kompatibilitätsprobleme |
| **Implementierungskomplexität** | "Wie sieht ein typischer Rollout aus? Welche Ressourcen plant ihr ein?" | Aufwändige Implementierung, lange Time-to-Value |
| **Abhängigkeit/Wechsel** | "Was, wenn ihr die Richtung ändern müsstet? Wie portabel ist eure [Daten-/Investition]?" | Vendor-Lock-in, Wechselkosten |
| **Servicekontinuität** | "Wie wichtig sind Teamstabilität und kontinuierlicher Service für eure Organisation?" | Personalwechsel, Key-Person-Abhängigkeit, schwankende Servicequalität |
| **Fachexpertise** | "Welches Maß an [Branchen-/Fach-]Expertise erwartet ihr von eurem Anbieter?" | Oberflächliches Fachwissen, generische Ansätze, fehlende Referenzen |
| **Erfüllungs-Track-Record** | "Wie bewertet ihr die Fähigkeit eines Anbieters, dauerhaft in der benötigten Qualität zu liefern?" | Inkonsistente Lieferung, Qualitätsschwankungen, gebrochene Zusagen |

Wähle 2-3 pro Deal auf Basis bekannter Schwachstellen des Wettbewerbers aus der Battlecard aus.

## Win/Loss-Analyse-Framework

Strukturierte Post-Mortem-Methodik:

1. Datenerhebung : Erfasse für jeden abgeschlossenen Deal das Ergebnis, die entscheidenden Faktoren (in den Worten des Kunden), den Bewertungsprozess, die Stakeholder-Dynamik, die Timeline, die Preisdiskussion sowie genannte Stärken/Schwächen.
2. Root-Cause-Kategorisierung : Klassifiziere nach primärer Ursache (Produkt, Preis, Beziehung, Timing, Wettbewerb). Mehrere Verluste mit derselben Ursache = systemisches Problem.
3. Mustererkennung : Suche nach wiederkehrenden Mustern nach Ursache, Wettbewerber, Segment und Win-Korrelationen. Wenn Verluste auf dasselbe Muster einen erheblichen Anteil aller Ergebnisse ausmachen (relativ zur Portfoliogröße), rechtfertigt das eine strategische Reaktion und ein Update der Battlecard.

## Wettbewerbs-Deal-Strategie

Wende die passende Strategie je nach Szenario an (Head-to-Head, Displacement, Greenfield, Multi-Vendor). Jedes erfordert eine andere Gewichtung aus Battlecard und Positionierungsmatrix -- nutze die FIA-Punkte und Landmine-Fragen, die für das Szenario am relevantesten sind.

## Referenzvorlage

Wenn du eine Battlecard erstellst, folge der Struktur der sieben Battlecard-Abschnitte (FIA angewendet) oben. Verlange für jeden Abschnitt belegte Intelligence und kennzeichne jede Behauptung mit ihrer Quelle.

## Leitplanken

1. Erfinde niemals Wettbewerbsbehauptungen. Alle Features, Preise und Positionierungen des Wettbewerbers müssen von dir, aus companyRAG-Sammlungen oder aus der Websuche stammen.
2. Standardverhalten "Wettbewerbsdaten erforderlich". Wenn keine Daten vorliegen, gib dies aus, statt eine Analyse zu generieren.
3. Quellenkennzeichnung. Versieh jede Behauptung mit einem Tag — [ Aus Battlecard/companyRAG-Sammlung ] , [ Aus Nutzereingabe ] , [ Aus Websuche ] , [ KI-Framework-Anwendung ] .
4. Verifizierungs-Disclaimer. Füge auf allen Battlecard-Inhalten den Hinweis "Wettbewerbsbehauptungen vor dem kundenseitigen Einsatz verifizieren" hinzu.

> **Tipp:** Fordere über companyFILES eine DOCX-, Markdown- oder PPTX-Ausgabe an, um ein formatiertes, sofort verteilbares Dokument zu erhalten.
