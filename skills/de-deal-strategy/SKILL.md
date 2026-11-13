---
name: de-deal-strategy
description: Kartiert die Machtverhältnisse der Stakeholder, deckt Deal-Risiken auf und empfiehlt eine schrittweise Engagement-Strategie. Verwende ihn, wenn du in einen komplexen Deal einsteigst, ein Meeting mit dem Executive Sponsor vorbereitest oder eine festgefahrene Opportunity diagnostizierst. Auslösen mit "Deal-Strategie planen für", "Stakeholder-Map", "wie bringe ich diesen Deal voran".
---

# Deal-Strategie-Skill

Kartiere Stakeholder, bewerte ihren Einfluss, plane Multi-Threading und erkenne organisatorische Veränderungssignale. Der Skill liefert Stakeholder-Maps, Engagement-Strategien und Mutual Action Plans. Alle Kontaktdaten, Org-Charts und Beziehungskontexte kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Account-Details, Kontakte, Org-Charts, Opportunity-Stadium, Aktivitätsverlauf |
| **Kommunikations-Tools über MCP** (z. B. E-Mail, Kalender, Slack) | Interaktionshistorie, letzte Touchpoints, Engagement-Trends je Stakeholder |
| **companyRAG / Datei-Upload** | Discovery-Call-Notizen, Beziehungs-Mapping, Account-Pläne, Wettbewerbskontext |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Bewertung der Beziehungskomplexität

Bewerte die Beziehungskomplexität des Accounts. Die primäre Routing-Dimension ist die Anzahl der Stakeholder, ergänzt durch die Sales-Motion-Komplexitätsbewertung, die alle Sales-Skills teilen (Zykluslänge, Deal-Wert, Anzahl Stakeholder, Lösungskomplexität — jeweils relativ zu den eigenen Normen des Kunden).

```
  WENIGE Stakeholder (Einzelkontakt oder kleines Buying Center)
    --> LEICHTGEWICHTIGES Stakeholder-Tracking
    --> Einfache Kontaktliste (Rolle, Einflussgrad, letzte Interaktion)
    --> Tracking der nächsten Schritte
    --> Grundlegende Engagement-Kadenz

  MITTLERE Stakeholder-Gruppe (mehrere Kontakte, definiertes Buying Center)
    --> STANDARD-Stakeholder-Mapping
    --> Stakeholder-Map mit Rollenklassifizierung und Einfluss-Scoring
    --> Meilensteinbasiertes Action-Tracking
    --> Strukturierter Engagement-Plan

  GROSSE Stakeholder-Gruppe (komplexe Org, mehrere Abteilungen/Divisionen)
    --> VOLLSTÄNDIGE Stakeholder-Strategie
    --> Komplette Macht-/Einfluss-Matrix mit Org-Chart-Navigation
    --> Mutual Action Plans mit Buyer-/Seller-Meilensteinen
    --> Multi-Threading-Plan über Abteilungen hinweg
    --> Monitoring organisatorischer Veränderungen
```

## Methodik des Stakeholder-Mappings

### Rollenklassifizierung

Klassifiziere jeden Stakeholder nach Rolle und definiere die Engagement-Strategie. Dies sind Archetypen, keine starren Kategorien — eine Person kann mehrere Rollen ausfüllen, und nicht jede Rolle existiert in jedem Deal oder Account:

| Rolle | Engagement-Strategie |
| --- | --- |
| **Champion** | Mit Argumenten ausstatten (Business Case, Proof Points). Die Beziehung schützen. Regelmäßige Check-ins. |
| **Coach** | Vertrauen aufbauen. Nach organisatorischem Insider-Wissen fragen. Sie niemals politisch exponieren. |
| **Economic Buyer** | In Geschäftsergebnissen kommunizieren, nicht in Features. Zu strategischen Momenten ansprechen (Budgetzyklen, Renewals, Expansionen). |
| **Technical Evaluator** | Technische Tiefe bieten. Bedenken direkt adressieren. In Proof-of-Concept oder Pilot-Design einbinden. |
| **Blocker** | Bedenken verstehen (oft berechtigt). Grundlegende Einwände adressieren. Über den Champion ansprechen, falls der direkte Weg scheitert. |
| **End User** | Adoption-Erfolg sicherstellen. Nutzungs-Feedback sammeln. Zufriedenheit als Expansion-Hebel nutzen. |

**Kultureller Kontext**: Die Engagement-Strategien gehen von Normen mit direktem Zugang aus. In hierarchischen Kulturen (z. B. Japan, Korea, Naher Osten) anpassen für: protokollgesteuerten Zugang (Vorstellung über die richtigen Kanäle), Senioritäts-orientiertes Engagement und Präferenz für indirekte Kommunikation. Hole dir bei kultureller Orientierung Rat beim Account-Owner oder lokalen Team.

### Einfluss-Scoring (1–5)

Bewerte den organisatorischen Einfluss jedes Stakeholders von 1 (minimal — nur informativ) bis 5 (Entscheidungsbefugnis — kann eigenständig freigeben oder ablehnen).

### Beziehungsstärke (1–5)

Bewerte die aktuelle Beziehung von 1 (keine Beziehung) bis 5 (aktiver Fürsprecher, der intern als Champion auftritt).

**Für leichtgewichtige Accounts**: Erfasse nur Rolle, Einflussgrad (Hoch/Mittel/Niedrig) und Datum der letzten Interaktion. Überspringe die vollständige Matrix.

**Macht-/Einfluss-Matrix** (Standard/Vollständig): Zeilen je Stakeholder mit Spalten für Rolle, Einfluss (1–5), Beziehungsstärke (1–5), Haltung (Support/Neutral/Block), letzter Touchpoint und nächste geplante Aktion. **Multi-Threading**: Sorge für parallele Abdeckung über Champion, Economic Buyer und Technical Evaluator (und Procurement beim Renewal); kartiere Abhängigkeiten zwischen Meilensteinen. **Organisatorische Veränderungssignale**: Rollenwechsel, M&A, Reorgs, neue Procurement-Beteiligung, Abgang des Champions oder plötzliches Schweigen eines Stakeholders — behandle sie als Auslöser, um die Map zu aktualisieren und das Risiko neu zu bewerten.

## Methodik des Action-Trackings

Skaliert nach Beziehungskomplexität:

**Leichtgewichtig (wenige Stakeholder)**:

- Liste der nächsten Schritte: Aktion, Verantwortlicher, Fälligkeitsdatum
- Tracking im Gespräch oder im CRM-Task

**Standard (mittlere Stakeholder-Gruppe)**:

- Meilensteinbasiertes Tracking: zentrale Meilensteine mit Abhängigkeiten
- Informell mit dem Kunden geteilt
- Stillstands-Erkennung: Meilensteine markieren, die über eine zur Deal-Zykluslänge proportionale Schwelle hinaus überfällig sind (z. B. 5–10 % des typischen Zyklus)

**Vollständig (große Stakeholder-Gruppe)**:

- Mutual Action Plan (MAP): gemeinsamer Plan mit Buyer- und Seller-Meilensteinen
- Mit dem Kunden vereinbarte gemeinsame Erfolgskriterien
- Timeline mit Abhängigkeiten und kritischem Pfad
- Auslöser der Stillstands-Erkennung: überfälliger Meilenstein, nicht reagierender Stakeholder, sich ändernde Anforderungen ohne MAP-Aktualisierung

## Stakeholder-Dynamik bei Renewal/Retention

Stakeholder-Maps verschieben sich bei Renewal- und Retention-Meilensteinen:

- Procurement gewinnt an Einfluss: Beim Renewal tritt Procurement oft hinzu oder gewinnt an Gewicht. Kartiere sie früh im Renewal-Zyklus.
- Champion-Kontinuitätsrisiko: Der ursprüngliche Champion hat möglicherweise die Rolle gewechselt oder das Unternehmen verlassen. Prüfe den Champion-Status vor dem Renewal.
- Neue Stakeholder: Nutzungs-Expansion kann neue Abteilungen oder Nutzer eingeführt haben, die nicht in der ursprünglichen Map sind. Aktualisiere die Map vor den Renewal-Gesprächen.
- Mehrwert-Validierung: Beim Renewal braucht der Economic Buyer Belege für den gelieferten Mehrwert. Bereite Kennzahlen und Geschäftsergebnisse für das Renewal-Gespräch vor.

## Bewertung der Stakeholder-Gesundheit

**Vollständige Methodik** (Standard- und Vollkomplexität):

| Faktor | Bewertung |
| --- | --- |
| **Beziehungsabdeckung** | Sind die Schlüsselrollen besetzt? Lücken bei Champion, Economic Buyer oder Technical Evaluator = Risiko. |
| **Einfluss-Balance** | Liegen deine stärksten Beziehungen bei einflussreichen Stakeholdern? Oder nur bei Kontakten mit geringem Einfluss? |
| **Engagement-Trend** | Richtung von Häufigkeit und Tiefe der Interaktionen über die Stakeholder hinweg (verbessernd, stabil, abnehmend). |
| **Champion-Stärke** | Ist der Champion ausgestattet, aktiv und politisch sicher? Champion-Verlust = Ereignis mit höchstem Risiko. |
| **Blocker-Status** | Sind die Bedenken der Blocker adressiert oder eskalieren sie? |

**Vereinfacht (leichtgewichtig)**: Ist der Hauptkontakt engagiert und reaktionsschnell? Grün / Gelb / Rot.

## Ausgabevorlage — Stakeholder-Strategie

```
STAKEHOLDER-STRATEGIE
Account: [Name]
Opportunity: [Name / Stadium]
Komplexität: [Leichtgewichtig / Standard / Vollständig]

STAKEHOLDER-MAP:
  Stakeholder 1: [Name — Rolle]
    Einfluss: [1–5] | Beziehungsstärke: [1–5] | Haltung: [Support/Neutral/Block]
    Letzter Touchpoint: [Datum] | Nächste Aktion: [Beschreibung]
  Stakeholder 2: [Name — Rolle]
    ...

MULTI-THREADING-ABDECKUNG:
  Champion:            [Name oder "Keine Daten verfügbar — erfordert Eingabe"]
  Economic Buyer:      [Name oder "Keine Daten verfügbar — erfordert Eingabe"]
  Technical Evaluator: [Name oder "Keine Daten verfügbar — erfordert Eingabe"]

ENGAGEMENT-STRATEGIE:
  [pro Stakeholder: empfohlener nächster Schritt, Quellenkennzeichnung]

RISIKEN & SIGNALE:
  1. [Risiko/Signal] → [Empfehlung] → Verantwortlich: [Name]
  2. ...

MUTUAL ACTION PLAN (falls Standard/Vollständig):
  [Buyer-/Seller-Meilensteine mit Terminen und Abhängigkeiten]
```

## Referenzmaterial

- Beziehungs-Mapping-Leitfaden — beim Kartieren der Deal-Stakeholder heranziehen. Lade ihn als Datei hoch oder hinterlege ihn in einer companyRAG-Sammlung, damit der Skill darauf zugreifen kann.

## Leitplanken

1. Erzeuge niemals Stakeholder-Daten. Alle Kontaktinformationen, Org-Charts und Beziehungsdetails müssen von dir, aus dem CRM oder aus einer companyRAG-Sammlung stammen.
2. "Keine Daten verfügbar"-Standard. Für jedes Feld ohne Daten "Keine Daten verfügbar — erfordert Eingabe" anzeigen.
3. Quellenkennzeichnung. Versieh Aussagen mit Tags — `[Aus Account-Daten]`, `[Aus Mapping-Framework]`, `[KI-Empfehlung]`.
4. Verifizierungs-Disclaimer. Füge auf allen Maps "Stakeholder-Informationen mit dem Account-Owner verifizieren" hinzu. Org-Strukturen ändern sich.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um eine formatierte, sofort teilbare Stakeholder-Strategie zu erhalten.
