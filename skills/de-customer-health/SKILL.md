---
name: de-customer-health
description: Bewerte die Account-Gesundheit über Produktnutzung, Support-Historie und Stimmung — kennzeichne Churn-Risiken mit empfohlenen nächsten Schritten. Verwende diesen Skill, wenn du Accounts durchsiehst, dich auf ein CS-Team-Meeting vorbereitest oder gefährdete Kunden identifizierst. Auslösen mit "diesen Kunden bewerten", "Account-Gesundheitscheck", "Churn-Risiko für [Account]".
---

# Kundengesundheit-Skill

Bewerte die Account-Gesundheit über mehrere Dimensionen, klassifiziere das Churn-Risiko und erstelle priorisierte Maßnahmenpläne. Die Account-Daten stammen von dir, aus einer verbundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten stammen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM via MCP** (z. B. HubSpot, Salesforce) | Account-Metadaten, Vertragsdaten, ARR, Verantwortlicher, Lifecycle-Phase |
| **Support-Plattform via MCP** (z. B. Zendesk, Intercom, Freshdesk) | Ticket-Volumen, Lösungszeit, CSAT-Werte, Eskalationen |
| **Produktanalyse via MCP** (z. B. Amplitude, Mixpanel, Pendo oder intern) | Login-Häufigkeit, Feature-Adoption, Nutzungstrends |
| **companyRAG / Datei-Upload** | CSM-Notizen, QBR-Protokolle, Umfrageergebnisse, hochgeladene Exporte |

> **Keine verbundene Quelle?** Stelle die Daten im Chat bereit oder lade Exporte hoch — und kennzeichne jede Dimension, in der Daten fehlen. Bewerte niemals ohne Belege.

## Workflow zur Gesundheitsbewertung

Führe diese Schritte für jede Gesundheitsbewertung in dieser Reihenfolge aus.

### Schritt 1: Account-Signale sammeln

Sammle Daten über sechs Signalkategorien hinweg. Erfasse für jedes Signal die Quelle und die Aktualität des Datenpunkts.

| Signalkategorie | Schlüsselindikatoren | Quelle |
| --- | --- | --- |
| **Produktnutzung** | Trend der Login-Häufigkeit (30/60/90 Tage), Breite der Feature-Adoption, Nutzungstiefe vs. Lizenzkapazität | Produktanalyse, CRM |
| **Support** | Trend des Ticket-Volumens, durchschnittliche Lösungszeit, Anzahl der Eskalationen, CSAT-/Zufriedenheitswerte | Support-Plattform |
| **Beziehung** | Engagement des Executive Sponsors, Reaktionsfreude des Champions, Stakeholder-Abdeckung, Meeting-Frequenz | CRM, CSM-Notizen |
| **Kommerziell** | Trend des Vertragswerts, Expansionshistorie, pünktliche Zahlungen, Nähe des Verlängerungstermins | CRM, Abrechnung |
| **Stimmung** | NPS-/CSAT-Trend, qualitative Feedback-Themen, Social Mentions falls verfügbar | Umfragen, CRM |
| **Ergebnisse** | Vom Kunden berichteter ROI, Zielerreichung vs. Erfolgsplan, Belege für Geschäftsauswirkung | CSM-Notizen, QBR-Protokolle |

Wenn für eine Signalkategorie keine Daten verfügbar sind, kennzeichne sie als NO DATA (keine Daten) und schließe sie aus dem Gesamtscore aus. Weise prominent auf die Lücke hin — fehlende Daten sind selbst ein Risikosignal.

### Schritt 2: Jede Dimension bewerten

Bewerte jede Dimension auf einer Skala von 1–5 anhand der untenstehenden Verhaltensanker.

| Score | Label | Definition |
| --- | --- | --- |
| **1** | Kritisch | Aktive Abwendung oder schwerwiegender negativer Trend. Sofortige Intervention erforderlich. |
| **2** | Gefährdet | Rückläufiger Trend oder wiederholte negative Signale. Proaktive Kontaktaufnahme innerhalb weniger Tage nötig. |
| **3** | Neutral | Stabil, aber unauffällig. Keine klare positive oder negative Entwicklung. Engmaschig beobachten. |
| **4** | Gesund | Positiver Trend über die meisten Indikatoren hinweg. Aktuelle Engagement-Frequenz beibehalten. |
| **5** | Florierend | Starke positive Signale, wachsende Nutzung, aktive Fürsprache. Expansionsmöglichkeiten ausloten. |

Wende diese Anker je Dimension an:

**Produktnutzung:**

- 1 = Nutzung um >50 % gegenüber Vorperiode gesunken oder nahezu keine aktiven Nutzer
- 3 = Stabile Nutzung, moderate Feature-Adoption, kein signifikanter Trend
- 5 = Wachsende Nutzung, breite Feature-Adoption, Nutzung übersteigt Lizenzbasis

**Support:**

- 1 = Hohes Ticket-Volumen mit ungelösten Eskalationen, sinkender CSAT
- 3 = Normales Ticket-Volumen, akzeptable Lösungszeiten, stabile Zufriedenheit
- 5 = Geringes Ticket-Volumen, schnelle Lösung, hoher CSAT, Self-Service-Nutzung

**Beziehung:**

- 1 = Champion abgewandert oder nicht erreichbar, kein Executive-Engagement, Meetings abgesagt
- 3 = Regelmäßiger Kontakt gepflegt, stabile Stakeholder-Map, ausreichende Meeting-Frequenz
- 5 = Beziehungen auf mehreren Ebenen (Multi-Threading), Executive Sponsor aktiv eingebunden, proaktive Kommunikation

**Kommerziell:**

- 1 = Anzeichen für Schrumpfung, Zahlungsprobleme oder Kunde hat Absicht zur Nicht-Verlängerung signalisiert
- 3 = Konstanter Vertrag, pünktliche Zahlungen, Verlängerung noch nicht besprochen
- 5 = Expansionshistorie, frühe Verlängerungssignale, Kunde initiiert Wachstumsgespräche

**Stimmung:**

- 1 = NPS auf Detraktor-Niveau, negatives qualitatives Feedback, ungelöste Beschwerden
- 3 = NPS auf Passiv-Niveau, neutrales Feedback, keine starken Signale in eine Richtung
- 5 = NPS auf Promoter-Niveau, positive Testimonials, Bereitschaft als Referenz zu dienen

**Ergebnisse:**

- 1 = Keine Belege für Wertrealisierung, Kunde kann den ROI nicht artikulieren
- 3 = Einige Ziele erreicht, teilweise ROI-Belege, Wertgeschichte vorhanden, aber nicht quantifiziert
- 5 = Vom Kunden berichteter ROI übertrifft Erwartungen, Geschäftsziele erreicht, Material für interne Fallstudie

### Schritt 3: Gesamtgesundheit klassifizieren

Berechne einen gewichteten Gesamtscore. Standardgewichte siehe unten — passe sie danach an, was in deinem Kundenstamm Churn vorhersagt.

| Dimension | Standardgewicht | Begründung |
| --- | --- | --- |
| Produktnutzung | 25 % | Stärkster vorlaufender Indikator für Retention |
| Support | 15 % | Nachlaufend, aber signalstark im Negativfall |
| Beziehung | 20 % | Multi-Threading ist ein bewährter Churn-Puffer |
| Kommerziell | 15 % | Direktes Umsatzsignal |
| Stimmung | 10 % | Subjektiv, aber in der Tendenz wertvoll |
| Ergebnisse | 15 % | Verknüpft die Gesundheit mit den eigenen Zielen des Kunden |

**Gesamtscore** = Σ (Dimensionsscore × Gewicht)

Ordne den Gesamtscore einer Gesundheitsklassifikation zu:

| Gesamtscore-Bereich | Klassifikation | Farbe | Bedeutung |
| --- | --- | --- | --- |
| 4.0–5.0 | Florierend | GREEN | Geringes Churn-Risiko. Fokus auf Expansion und Fürsprache. |
| 3.0–3.9 | Stabil | YELLOW | Mäßiges Risiko. Trends beobachten und jede rückläufige Dimension adressieren. |
| 2.0–2.9 | Gefährdet | ORANGE | Erhöhtes Churn-Risiko. Proaktiver Maßnahmenplan erforderlich. |
| 1.0–1.9 | Kritisch | RED | Hohes Churn-Risiko. Intern eskalieren und sofort eingreifen. |

**Übersteuerungsregeln:**

- Jede einzelne Dimension mit Score 1 → Gesamtklassifikation kann unabhängig vom Gesamtscore nicht höher als YELLOW sein
- Produktnutzung mit Score 1 oder 2 UND Beziehung mit Score 1 oder 2 → automatisch RED
- Fehlende Daten bei 3+ Dimensionen → als ORANGE klassifizieren mit dem Hinweis, dass der Score unzuverlässig ist

### Schritt 4: Risikofaktoren identifizieren

Dokumentiere für jede Dimension mit Score 3 oder darunter:

| Element | Inhalt |
| --- | --- |
| **Signal** | Der/die konkrete(n) Datenpunkt(e), der/die den niedrigen Score verursacht/verursachen |
| **Trend** | Verbessernd, stabil oder rückläufig über die letzten 30/60/90 Tage |
| **Ursachenhypothese** | Was dieses Signal antreiben könnte (keine Gewissheit — eine zu untersuchende Hypothese) |
| **Auswirkung bei Untätigkeit** | Was mit dem Account passiert, wenn sich dieser Trend fortsetzt |
| **Konfidenz** | Hoch / Mittel / Niedrig basierend auf Datenqualität und Aktualität |

### Schritt 5: Nächste Schritte empfehlen

Empfehle für jedes identifizierte Risiko eine konkrete, terminierte Intervention.

| Risikostufe | Reaktionszeitraum | Aktionstyp | Beispiel |
| --- | --- | --- | --- |
| RED-Dimension | Innerhalb von 48 Stunden | Executive-Kontaktaufnahme, interne Eskalation | Gemeinsames Gespräch von CSM + Manager mit dem Champion; Eskalations-Briefing an die Führungsebene |
| ORANGE-Dimension | Innerhalb von 1 Woche | Proaktives Engagement, Ursachenermittlung | Check-in mit Fokus auf den konkreten Risikobereich planen; Wertzusammenfassung vorbereiten |
| YELLOW-Dimension | Innerhalb von 2 Wochen | Beobachtung mit leichter Berührung | Auf Watchlist setzen; Touchpoint planen; im nächsten Team-Meeting prüfen |
| GREEN-Dimension | Standard-Frequenz | Beibehalten und Expansion ausloten | Regelmäßiges Engagement fortsetzen; Expansionssignale erkennen |

Gib für jede empfohlene Aktion an: die Aktion, den Verantwortlichen (CSM, Manager, Executive), die Frist und den Erfolgsindikator.

## Ausgabevorlage — Gesundheits-Scorecard

```
KUNDENGESUNDHEIT-SCORECARD
Account: [Name]
Bewertungsdatum: [Datum]
Bewertet von: [CSM-Name]
Datenquellen: [verwendete MCP-Quellen, companyRAG-Sammlungen und manuelle Eingaben auflisten]

GESAMTGESUNDHEIT: [GREEN / YELLOW / ORANGE / RED] — Gesamtscore: [X.X / 5.0]

DIMENSIONS-SCORES:
  Produktnutzung:      [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Support:             [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Beziehung:           [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Kommerziell:         [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Stimmung:            [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Ergebnisse:          [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]

  [▲ = sich verbessernder Trend | ▼ = rückläufiger Trend | — = stabil]

ZENTRALE RISIKEN:
  1. [Risikobeschreibung] — [Dimension] — [Trend] — [Konfidenz]
     → Aktion: [konkrete Intervention]
     → Verantwortlicher: [Name/Rolle]
     → Frist: [Datum]

  2. [Risikobeschreibung] ...

EXPANSIONSSIGNALE:
  - [positive Signale, die auf eine Wachstumschance hindeuten]

DATENLÜCKEN:
  - [Dimensionen mit fehlenden oder veralteten Daten]

NÄCHSTES ÜBERPRÜFUNGSDATUM: [Datum]
```

## Referenzrahmen zur Gesundheitsbewertung

### Vorlaufende vs. nachlaufende Indikatoren

Nicht alle Signale sagen Churn gleich gut voraus. Priorisiere vorlaufende Indikatoren für eine frühzeitige Intervention.

| Indikatortyp | Beispiele | Vorhersagewert |
| --- | --- | --- |
| **Vorlaufend** (Verhaltensänderungen vor dem Churn) | Rückgang der Login-Häufigkeit, sinkende Feature-Adoption, Abwendung des Champions, abgesagte Meetings | Hoch — frühzeitig darauf reagieren |
| **Gleichlaufend** (ändern sich parallel zum Churn-Risiko) | Spitzen im Support-Ticket-Volumen, NPS-Rückgang, Zahlungsverzögerungen | Mittel — mit vorlaufenden Indikatoren bestätigen |
| **Nachlaufend** (treten auf, nachdem das Risiko besteht) | Kündigungsmitteilung, explizites Churn-Signal, Wettbewerbsevaluierung | Geringer Vorhersagewert — reaktives Terrain |

### Trendanalyse

Bewerte stets die Richtung der Veränderung, nicht nur den aktuellen Zustand. Ein Score von 3, der im letzten Quartal noch 5 war, ist bedenklicher als ein stabiler Score von 3.

| Trendmuster | Interpretation | Handlungsdringlichkeit |
| --- | --- | --- |
| Rascher Rückgang (2+ Punkte in einer Periode) | Akutes Problem — etwas hat sich verändert | Sofortige Untersuchung |
| Allmählicher Rückgang (1 Punkt über 2+ Perioden) | Langsame Abwendung — möglicherweise strukturell | Proaktiv innerhalb von 1-2 Wochen |
| Stabil niedrig (durchgängig 1-2) | Chronisches Problem — möglicherweise normalisiert | Strategische Überprüfung, Eskalation erwägen |
| Erholung (verbessert sich aus niedrigem Niveau) | Intervention wirkt möglicherweise | Aktuellen Ansatz fortsetzen, validieren |

## Leitplanken

- Erfinde niemals Nutzungsdaten, Ticket-Zahlen, NPS-Werte oder andere Account-Metriken. Wenn für eine Dimension keine Daten verfügbar sind, kennzeichne sie als NO DATA (keine Daten) — schätze nicht.
- Behaupte niemals eine konkrete Churn-Wahrscheinlichkeit. Gesundheitsscores geben das Risikoniveau an, nicht die statistische Wahrscheinlichkeit. "RED" bedeutet "hohes Risiko, das eine Intervention erfordert", nicht "80 % Churn-Wahrscheinlichkeit".
- Gesundheitsscores sind entscheidungsunterstützende Eingaben, keine Entscheidungen. Füge stets hinzu: "Validiere die Scores mit dem Account-Team, bevor du auf Basis der Risikoklassifikationen handelst."
- Versiehe jede Aussage mit einem Quellen-Label: `[Aus Account-Daten]`, `[Aus Bewertungsrahmen]` oder `[CSM-Hypothese]`. Kennzeichne die Konfidenz je Dimension (Hoch / Mittel / Niedrig).

## Gewichte an dein Geschäft anpassen

Die obigen Standardgewichte der Dimensionen sind Ausgangspunkte. So kalibrierst du sie für deinen Kundenstamm:

1. Historische Churn-Daten überprüfen — welche Dimensionen waren 90 Tage vor Churn-Ereignissen am niedrigsten?
2. Nach Korrelationen suchen — welche Dimensionen sagen Verlängerungsergebnisse am stärksten voraus?
3. Gewichte anpassen — Gewicht der Dimensionen erhöhen, die in deinen Daten am aussagekräftigsten sind
4. Vierteljährlich validieren — die Korrelation erneut prüfen, während sich dein Produkt und dein Kundenstamm entwickeln
5. Bei Bedarf segmentieren — Enterprise vs. Mid-Market vs. SMB können unterschiedliche prädiktive Signale aufweisen

> **Tipp:** Fordere eine XLSX-Ausgabe über companyFILES an, um eine formatierte, verteilbare Tabelle zu erhalten.
