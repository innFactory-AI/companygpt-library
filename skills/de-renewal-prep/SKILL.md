---
name: de-renewal-prep
description: Bereite eine Verlängerungsstrategie vor — erkenne Expansions- oder Abwanderungsrisiken und entwirf einen Gesprächsleitfaden mit empfohlenem Preisansatz. Verwende ihn, wenn eine Verlängerung 60–90 Tage bevorsteht, du deine Renewal-Pipeline durchgehst oder dich auf eine Verlängerungsverhandlung vorbereitest. Auslösen mit "Verlängerung vorbereiten für", "Verlängerungsstrategie für [Account]", "Verlängerungs-Risikobewertung".
---

# Vertragsverlängerung-Skill

Erstelle Renewal-Briefings, die eine Risikobewertung, einen Gesprächsleitfaden und einen empfohlenen Preisansatz kombinieren. Die Account-Daten stammen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM via MCP** (z. B. HubSpot, Salesforce) | Vertragskonditionen, ARR, Verlängerungsdatum, Expansionshistorie, Stakeholder-Kontakte |
| **Abrechnung via MCP** (z. B. Stripe, Chargebee) | Zahlungshistorie, aktuelle Preise, nutzungsbasierte Abrechnungsdaten |
| **companyRAG / Datei-Upload** | QBR-Notizen, Kennzahlen aus dem Success Plan, Support-Zusammenfassungen, frühere Verlängerungsunterlagen |

> **Keine angebundene Quelle?** Stelle die Daten im Chat bereit oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Workflow zur Verlängerungsvorbereitung

Beginne diesen Workflow 60–90 Tage vor dem Verlängerungsdatum. Bei strategischen Accounts früher; bei automatisch verlängernden Verträgen mit geringem Risiko ist auch später akzeptabel.

### Schritt 1: Account-Gesundheit prüfen

Rufe einen aktuellen Health Score über den **de-customer-health** ab oder erstelle ihn. Wenn ein aktueller Score vorliegt, prüfe ihn. Falls nicht, führe eine frische Bewertung durch.

Wichtige Gesundheitsdimensionen im Verlängerungskontext:

| Dimension | Relevanz für die Verlängerung |
| --- | --- |
| **Produktnutzung** | Rückläufige Nutzung ist der stärkste Indikator für eine Nicht-Verlängerung |
| **Support** | Ungelöste Eskalationen verschaffen dem Kunden Verhandlungshebel |
| **Beziehung** | Weggang des Champions oder Rückzug der Führungsebene signalisiert Risiko |
| **Stimmung** | Der NPS-Trend zeigt die Bereitschaft zu verlängern und zu expandieren |
| **Ergebnisse** | Dokumentierter ROI ist das stärkste Argument für Verlängerung und Expansion |

### Schritt 2: Risikofaktoren bewerten

Bewerte jede Risikokategorie und stufe sie als High / Medium / Low (hoch / mittel / niedrig) ein.

| Risikokategorie | Indikatoren für High Risk | Indikatoren für Medium Risk | Indikatoren für Low Risk |
| --- | --- | --- | --- |
| **Nutzung** | Rückläufige Nutzung, geringe Adoption im Verhältnis zur Lizenz, Kernfunktionen ungenutzt | Stabile, aber flache Nutzung, moderate Adoption | Wachsende Nutzung, hohe Adoption, sich erweiternde Anwendungsfälle |
| **Beziehung** | Champion weg, Führungsebene zurückgezogen, dünne Stakeholder-Landkarte | Champion stabil, aber ohne Ausbau, begrenztes Multi-Threading | Starkes Multi-Threading, eingebundener Executive Sponsor |
| **Support** | Offene Eskalationen, hohes Ticketaufkommen, sinkender CSAT | Moderates Ticketaufkommen, gelöste Eskalationen | Geringes Ticketaufkommen, hoher CSAT, Self-Service-Adoption |
| **Kommerziell** | Zahlungsverzögerungen, kommunizierte Budgetbeschränkungen, Wettbewerbsevaluierung | Flaches Budget, keine Expansionssignale, Preissensibilität erwähnt | Pünktliche Zahlungen, Expansionsinteresse, bestätigtes Budget |
| **Wert** | Kein dokumentierter ROI, Kunde kann den Wert nicht artikulieren | Einige ROI-Nachweise, aber nicht quantifiziert, teilweise Zielerreichung | Starker ROI dokumentiert, Ziele übertroffen, interne Fallstudie |
| **Markt** | Kunde im Zuge von M&A, Führungswechsel, Branchenabschwung | Gewisser organisatorischer Wandel, laufende Budgetprüfungen | Stabile Organisation, wachsendes Geschäft, strategische Ausrichtung |

**Gesamtrisiko der Verlängerung** = höchste einzelne Risikokategorie. Ein einziger High-Risk-Faktor kann eine Verlängerung unabhängig von den anderen Dimensionen zum Scheitern bringen.

### Schritt 3: Expansionschancen erkennen

Achte auf Signale, die darauf hindeuten, dass der Kunde bereit für eine Expansion sein könnte.

| Expansionssignal | Erforderlicher Nachweis | Expansionstyp |
| --- | --- | --- |
| Nutzung nähert sich Lizenzgrenzen oder überschreitet sie | Nutzungsdaten vs. Vertragskapazität | Lizenz-Uplift |
| Neue Abteilungen oder Teams zeigen Interesse | Kundenanfrage, CSM-Beobachtung | Seat-Erweiterung |
| Kunde fragt Funktionen aus höheren Tiers nach | Support-Tickets, Feature-Anfragen | Tier-Upgrade |
| Neue Anwendungsfälle jenseits des ursprünglichen Umfangs entstehen | Nutzungsmuster, Kundengespräche | Produkt-Cross-Sell |
| Das Geschäft des Kunden wächst (Mitarbeiterzahl, Umsatz) | Öffentliche Daten, Kundenkommunikation | Organische Expansion |
| Positiver ROI ermöglicht Budgetrechtfertigung | QBR-Daten, Kennzahlen aus dem Success Plan | Wertbasiertes Upsell |

### Schritt 4: Verlängerungsstrategie entwerfen

Wähle auf Basis der Risiko- und Chancenbewertung eine strategische Haltung.

| Szenario | Strategische Haltung | Fokus |
| --- | --- | --- |
| Low Risk + Expansionssignale | **Expand** (Ausbauen) | Mit geliefertem Wert beginnen, erweiterten Umfang vorschlagen, am ROI verankern |
| Low Risk + keine Expansionssignale | **Secure** (Sichern) | Wert bestätigen, bei Eignung Mehrjahresvertrag festschreiben, Momentum erhalten |
| Medium Risk + beliebige Expansion | **Stabilise then expand** (Stabilisieren, dann ausbauen) | Zuerst Risikofaktoren lösen, Wert demonstrieren, dann Expansion einbringen |
| Medium Risk + keine Expansion | **Defend** (Verteidigen) | Fokus auf Retention, Bedenken adressieren, Recovery-Plan aufbauen |
| High Risk + beliebig | **Recover** (Zurückgewinnen) | Volle Aufmerksamkeit auf Risikominderung, Einbindung der Führungsebene, Wertbekräftigung |

### Schritt 5: Gesprächsleitfaden vorbereiten

Strukturiere das Verlängerungsgespräch anhand der strategischen Haltung.

**Gesprächsrahmen:**

1. **Mit Wert beginnen** — Starte mit konkreten Ergebnissen, die der Kunde erreicht hat. Verweise auf QBR-Daten, Kennzahlen aus dem Success Plan oder ROI-Nachweise. Beginne nie mit dem Preis.
2. **Die Beziehung würdigen** — Verweise auf konkrete Meilensteine, gemeistert Herausforderungen und Partnerschaftsmomente. Zeige, dass du diesen Account kennst.
3. **Bekannte Bedenken ansprechen** — Sprich Themen, die du kennst, proaktiv an, anstatt zu warten, bis der Kunde sie aufbringt. Das schafft Vertrauen und steuert die Erzählung.
4. **Das Verlängerungsangebot präsentieren** — Basierend auf deiner strategischen Haltung:   - Expand: „Basierend auf dem, was Sie erreicht haben, können wir Ihnen so helfen, noch mehr zu erreichen ..."   - Secure: „Wir würden diese Partnerschaft gern fortsetzen. So sieht die Verlängerung aus ..."   - Defend: „Wir wissen, dass es Herausforderungen gab. Hier ist unser Plan, sie zu adressieren, und das ist unsere Zusage ..."   - Recover: „Wir hören Ihre Bedenken. Bevor wir über die Verlängerung sprechen, lassen Sie uns abstimmen, was sich ändern muss ..."
5. **Einwände behandeln** — Bereite Antworten auf die wahrscheinlichsten Einwände auf Basis deiner Risikobewertung vor.
6. **Nächste Schritte vereinbaren** — Beende ein Verlängerungsgespräch nie ohne einen klaren, terminierten nächsten Schritt.

**Häufige Einwände und Vorbereitung:**

| Einwandtyp | Erforderliche Vorbereitung |
| --- | --- |
| „Wir sehen nicht genug Wert" | ROI-Nachweise, Nutzungsdaten, Ergebniskennzahlen — vor dem Gespräch vorbereiten |
| „Das Budget ist knapp / wir müssen kürzen" | Wechselkostenanalyse, Effizienzgewinne, Abgrenzung essenziell vs. nice-to-have |
| „Wir evaluieren Alternativen" | Wettbewerbspositionierung (nutze einen Battlecard-Skill aus dem Sales-Pack, falls verfügbar), Wechselkostenanalyse, einzigartige Wert-Differenzierungsmerkmale |
| „Wir brauchen einen Rabatt" | Wertbegründung, Mehrjahres-Anreizoptionen, Optionen zur Umfangsanpassung |
| „Unser Champion ist gegangen" | Frühzeitig neue Stakeholder erneut einbinden, die Wert-Erzählung für die neue Zielgruppe neu aufbauen |

## Ausgabevorlage — Renewal-Briefing

```
RENEWAL-BRIEFING
Account: [Name]
ARR: [aktueller Wert]
Verlängerungsdatum: [Datum]
Tage bis zur Verlängerung: [Anzahl]
Erstellt von: [CSM-Name]
Datum: [Datum]

ZUSAMMENFASSUNG ACCOUNT-GESUNDHEIT:
  Gesamtgesundheit: [GRÜN / GELB / ORANGE / ROT]
  Schlüsselscores: Produkt [X/5], Support [X/5], Beziehung [X/5],
                   Kommerziell [X/5], Stimmung [X/5], Ergebnisse [X/5]

RISIKOBEWERTUNG:
  Gesamtrisiko: [High / Medium / Low]
  Nutzungsrisiko:    [H/M/L] — [kurzer Nachweis]
  Beziehungsrisiko:  [H/M/L] — [kurzer Nachweis]
  Support-Risiko:    [H/M/L] — [kurzer Nachweis]
  Kommerz. Risiko:   [H/M/L] — [kurzer Nachweis]
  Wert-Risiko:       [H/M/L] — [kurzer Nachweis]
  Markt-Risiko:      [H/M/L] — [kurzer Nachweis]

EXPANSIONSCHANCEN:
  1. [Chance] — [Nachweis] — [geschätzter Wert]
  2. ...
  (oder: Aktuell keine Expansionssignale erkannt)

STRATEGIE: [Expand / Secure / Stabilise then Expand / Defend / Recover]
  Begründung: [warum diese Haltung]

WERT-NACHWEISE:
  - [konkretes Ergebnis oder Kennzahl, die der Kunde erreicht hat]
  - [konkretes Ergebnis oder Kennzahl]
  - ...

GESPRÄCHSLEITFADEN:
  Einstieg: [wertorientierter Einstieg, zugeschnitten auf diesen Account]
  Zu adressierende Bedenken: [Liste bekannter Bedenken mit vorbereiteten Antworten]
  Angebot: [vorzuschlagende Verlängerungskonditionen — gleichbleibend, Expansion, Mehrjahres usw.]
  Wahrscheinliche Einwände: [Top 2–3 mit vorbereiteten Antworten]
  Ask: [konkreter nächster Schritt, der am Gesprächsende vorgeschlagen wird]

INTERNE ABSTIMMUNG:
  CSM: [Name]
  Account Executive: [Name, falls an der Verlängerung beteiligt]
  Executive Sponsor: [Name, falls Einbindung der Führungsebene nötig]
  Aktionen vor der Verlängerung: [interne Schritte vor dem Kundengespräch]
```

## CUSTOMIZE — An deine Renewal-Motion anpassen

- Automatisch verlängernde Verträge : Richte den Workflow auf Risikoerkennung und Expansionschancen aus — die Verlängerung selbst läuft automatisch, doch das Abwanderungsrisiko bleibt bestehen.
- Nutzungsbasierte Preise : Ersetze die feste ARR-Analyse durch eine Nutzungstrend-Analyse und prognostizierte Abrechnung.
- Mehrjahres-Verlängerungen : Starte den Workflow 120–180 Tage vorher statt 60–90.
- Channel-/Partner-Verlängerungen : Füge zwischen Schritt 4 und 5 einen Schritt zur Partnerabstimmung ein.
- Verlängerungen mit hohem Volumen / Tech-Touch : Stütze das Risk-Scoring (Schritt 2) auf Health-Score-Daten und konzentriere den manuellen Aufwand nur auf Accounts mit High und Medium Risk.

## Leitplanken

- Erfinde niemals Vertragswerte, Verlängerungsdaten, Preise oder Nutzungsdaten. Alle kommerziellen Daten müssen vom Nutzer, aus dem CRM oder aus dem Abrechnungssystem stammen.
- Generiere niemals konkrete Rabattempfehlungen oder Preiszahlen. Dieser Skill strukturiert den Ansatz; die Zahlen liefert dein Pricing-Team.
- Nimm niemals die Budgetsituation oder das Wettbewerbsumfeld des Kunden an. Frage nach; schließe nicht darauf.
- Kennzeichne jede Aussage mit ihrer Quelle : [Aus Account-Daten] , [Aus Renewal-Framework] oder [CSM-Einschätzung] .

> **Tipp:** Fordere eine DOCX-Ausgabe über companyFILES an, um ein formatiertes Renewal-Briefing zu erhalten, das du direkt teilen kannst.
