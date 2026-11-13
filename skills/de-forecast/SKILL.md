---
name: de-forecast
description: Erstellt einen gewichteten Umsatz-Forecast mit Risikoflags, Commit-Empfehlungen und Gap-to-Quota-Analyse. Verwende ihn zur Vorbereitung eines Forecast-Calls, zur Bewertung der Projektion zum Quartalsende oder zur Einschätzung der Pipeline-Coverage. Auslösen mit "Forecast erstellen", "Forecast für dieses Quartal", "wo stehe ich gegen mein Quota".
---

# Forecast-Skill

Wandle Pipeline-Daten in gewichtete Projektionen mit Risikobewertung, Commit-Kategorie-Empfehlungen und Gap-to-Quota-Aktionsplänen um. Alle Pipeline-Daten, Quota-Ziele und historischen Werte kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. HubSpot, Salesforce, Dynamics) | Pipeline-Deals, Stages, Werte, Close-Dates, Aktivitätshistorie |
| **companyRAG-Sammlungen** | Frühere Forecast-Genauigkeit, saisonale Muster, Win-Rate-Daten |
| **Datei-Upload (CSV/XLSX)** | Pipeline-Export, Quota-Ziele, deal-spezifische Confidence, Kontext, der nicht im CRM steht |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Forecasting-Workflow

```
1. PIPELINE-DATEN heranziehen
   |
   +--> Alle offenen Opportunities für den Forecast-Zeitraum
   +--> Enthält: Deal-Name, Wert, Stage, Close-Date, Alter, letzte Aktivität, Owner
   +--> Markiere Deals mit Close-Date in der Vergangenheit (geslippte Deals)
   +--> Markiere Deals ohne Aktivität in den letzten 14 Tagen
   |
2. JEDEN DEAL KATEGORISIEREN
   |
   +--> Wende die Forecast-Kategorien an (siehe Kategorie-Framework unten)
   +--> Dokumentiere für jeden Deal die Begründung der Kategoriezuordnung
   +--> Markiere Abweichungen zwischen CRM-Stage und eingeschätzter Confidence
   |
3. NACH WAHRSCHEINLICHKEIT GEWICHTEN
   |
   +--> Wende stage-basierte oder eingeschätzte Wahrscheinlichkeit an (siehe Gewichtungs-Methodik unten)
   +--> Berechne den gewichteten Wert je Deal
   +--> Summiere nach Kategorie für die Kategorie-Totale
   |
4. RISIKEN MARKIEREN
   |
   +--> Wende die Risikokriterien auf jeden Deal an (siehe Risiko-Flagging unten)
   +--> Klassifiziere die Risikoschwere: Hoch / Mittel / Niedrig
   +--> Deals mit hohem Risiko werden eine Kategorie heruntergestuft oder zur Prüfung markiert
   |
5. GAP-TO-QUOTA BERECHNEN
   |
   +--> Vergleiche den gewichteten Forecast mit dem Quota-Ziel
   +--> Identifiziere die Lücke (oder den Überschuss) auf Commit- und Best-Case-Ebene
   +--> Bewerte die Pipeline-Coverage (siehe Coverage-Analyse unten)
   |
6. MASSNAHMEN EMPFEHLEN
   |
   +--> Bei Forecast-Lücken: identifiziere die beweglichsten Deals zum Schließen der Lücke
   +--> Bei gefährdeten Deals: empfiehl konkrete Maßnahmen zur Risikoreduktion
   +--> Bei Coverage-Defiziten: markiere den Bedarf an Pipeline-Generierung mit Dringlichkeit
   |
7. FORECAST-OUTPUT ERSTELLEN (siehe Ausgabevorlage unten)
```

## Forecast-Kategorie-Framework

Ordne jeden Deal genau einer Kategorie zu — auf Basis von Evidenz, nicht von Optimismus:

| Kategorie | Definition | Erforderliche Evidenz |
| --- | --- | --- |
| **Closed Won** | Unterschrieben, gebucht oder verbal mit schriftlicher Bestätigung zugesagt | Vertrag unterzeichnet oder Bestellung (PO) erhalten |
| **Commit** | Hohe Abschluss-Wahrscheinlichkeit in diesem Zeitraum — konkrete Evidenz für Käufer-Commitment | Verbale Zusage + definierter Vertragsprozess + abgestimmte Timeline innerhalb des Zeitraums |
| **Best Case** | Realistische Abschluss-Chance in diesem Zeitraum — Deal entwickelt sich, aber Zusagen sind weich | Aktives Engagement + Budget bestätigt + Entscheider eingebunden + Timeline plausibel |
| **Pipeline** | Im aktiven Sales-Prozess, aber unwahrscheinlich für diesen Zeitraum | Qualifizierte Opportunity mit Aktivität, aber ohne Commitment-Signale |
| **Omit** | Veraltete, disqualifizierte oder Platzhalter-Deals, die nicht im Forecast erscheinen sollten | Keine Aktivität >30 Tage oder fehlende grundlegende Qualifizierungskriterien |

### Entscheidungsbaum für die Kategoriezuordnung

```
Deal im CRM für diesen Zeitraum
  |
  +--> Vertrag unterschrieben oder PO erhalten?
  |      JA --> CLOSED WON
  |
  +--> Käufer hat verbal zugesagt + Vertragsprozess definiert + Timeline im Zeitraum?
  |      ALLE JA --> COMMIT
  |      EINIGE JA --> Prüfen: welche Elemente fehlen?
  |                   +--> Verbale Zusage fehlt --> höchstens BEST CASE
  |                   +--> Vertragsprozess fehlt --> BEST CASE (Risiko: Procurement-Verzögerung)
  |                   +--> Timeline rutscht aus dem Zeitraum --> PIPELINE oder BEST CASE
  |
  +--> Aktives Engagement + Budget bestätigt + Entscheider eingebunden?
  |      ALLE JA + Timeline plausibel --> BEST CASE
  |      EINIGE JA --> PIPELINE
  |
  +--> Qualifiziert, aber frühphasig oder Timeline im nächsten Zeitraum+?
  |      JA --> PIPELINE
  |
  +--> Keine nennenswerte Aktivität in >30 Tagen oder grundlegende Qualifizierungslücken?
         JA --> OMIT (zur Pipeline-Bereinigung markieren)
```

## Gewichtungs-Methodik

Zwei Ansätze — verwende den, den die Datenlage des Kunden hergibt:

### Stage-basierte Gewichtung

Leite die Wahrscheinlichkeiten aus den eigenen historischen Abschlussraten je Stage ab. Schreibe niemals Wahrscheinlichkeiten vor.

| Schritt | Aktion |
| --- | --- |
| 1 | Ziehe Closed-Won- und Closed-Lost-Deals der letzten 4+ Quartale heran |
| 2 | Berechne die Win Rate je Stage: Deals, die Stage X erreichten und letztlich Closed Won wurden / alle, die Stage X erreichten |
| 3 | Wende die abgeleitete Rate auf die aktuelle Pipeline an: gewichteter Wert = Deal-Wert × Stage-Wahrscheinlichkeit |
| 4 | Korrigiere bekannte Verzerrungen: wenn aus einer bestimmten Stage konsistent zu optimistisch geforecastet wird, wende einen aus den jüngsten Genauigkeitsdaten abgeleiteten Abschlagsfaktor an |

### Gewichtung nach eingeschätzter Confidence

Wenn historische Daten nicht ausreichen oder die Deal-Eigenschaften zu stark variieren:

| Schritt | Aktion |
| --- | --- |
| 1 | Für jeden Deal vergibt der Rep (oder die KI auf Basis von CRM-Signalen) eine Confidence-Prozentzahl |
| 2 | Die Confidence muss mit konkreter Evidenz begründet sein, nicht mit Bauchgefühl |
| 3 | Gewichteter Wert = Deal-Wert × eingeschätzte Confidence |
| 4 | Vergleiche rep-eingeschätzte vs. stage-basierte Wahrscheinlichkeit — eine große Abweichung weist auf Datenqualität oder deal-spezifische Erkenntnisse hin |

**Schreibe niemals Conversion-Raten, Stage-Wahrscheinlichkeiten oder Benchmark-Prozente vor.** Leite immer aus den eigenen Daten des Kunden ab oder kennzeichne als "[Angenommen — anhand historischer Daten kalibrieren]".

## Risiko-Flagging

Wende diese Kriterien auf jeden Deal im Forecast an. Ein Deal kann mehrere Risikoflags tragen:

| Risikofaktor | Auslösebedingung | Schwere |
| --- | --- | --- |
| **Kein Next Step** | Kein definierter, abgestimmter nächster Schritt mit Datum | Hoch |
| **Single-Threaded** | Nur ein Kontakt eingebunden; kein Multi-Threading | Hoch |
| **Close-Date geslippt** | Close-Date in diesem Quartal ein- oder mehrmals nach hinten verschoben | Hoch |
| **Veraltetes Engagement** | Keine nennenswerte Aktivität (E-Mail, Call, Meeting) in >14 Tagen | Hoch |
| **Economic Buyer fehlt** | Keine Interaktion mit der Budget-Autorität | Mittel |
| **Wettbewerbsbedrohung** | Aktive Wettbewerber-Evaluierung ohne klaren Differenzierungsplan | Mittel |
| **Champion-Risiko** | Champion hat die Rolle gewechselt, ist verstummt oder hat das Unternehmen verlassen | Hoch |
| **Vertragsprozess undefiniert** | Keine Klarheit über Procurement-Schritte, Vertragsprüfung oder Legal-Timeline | Mittel |
| **Wert-Misalignment** | CRM-Deal-Wert wurde nicht mit dem Käufer validiert | Mittel |
| **Late-Stage-Qualifizierungslücke** | Deal in später Stage, aber MEDDPICC/BANT-Elemente niedrig bewertet | Hoch |

### Zuordnung Risiko → Maßnahme

| Schwere | Forecast-Auswirkung | Empfohlene Maßnahme |
| --- | --- | --- |
| **Hoch** | Eine Kategorie herunterstufen oder zur Override-Prüfung markieren | Sofortige Rep-Aktion erforderlich; in die Notizen zum Forecast-Call aufnehmen |
| **Mittel** | Gewichteten Wert um einen vom Kunden definierten Faktor abwerten | Auf die wöchentliche Deal-Review-Agenda setzen; konkrete Folgeaktion zuweisen |

## Gap-to-Quota-Analyse

```
QUOTA-ZIEL für den Zeitraum: [Q]

COMMIT-Total (gewichtet): [C]
BEST-CASE-Total (gewichtet): [B]
PIPELINE-Total (gewichtet): [P]

GAP auf Commit-Ebene: Q - C = [Lücke oder Überschuss]
GAP auf Best-Case-Ebene: Q - (C + B) = [Lücke oder Überschuss]

COVERAGE-RATIO:
  Gesamter aktiver Pipeline-Wert / Q = [X]x Coverage
  Gewichtete Pipeline / Q = [Y]x gewichtete Coverage

  Vergleich mit der historischen Coverage-to-Close-Ratio des Kunden:
    ÜBER der historischen Ratio --> Coverage ist ausreichend (Deal-Qualität dennoch prüfen)
    AUF der historischen Ratio --> Auf Kurs, minimaler Puffer für Slippage
    UNTER der historischen Ratio --> Coverage-Lücke — Dringlichkeit für Pipeline-Generierung
```

## Coverage-Analyse

Pipeline-Coverage im Kontext der Realität des Kunden:

| Faktor | Bewertung |
| --- | --- |
| **Rohe Coverage** | Gesamter Pipeline-Wert / Quota-Ziel |
| **Gewichtete Coverage** | Gewichteter Pipeline-Wert / Quota-Ziel |
| **Qualitätsbereinigte Coverage** | Omit-Kategorie und Hochrisiko-Deals entfernen, neu berechnen |
| **Zeitbereinigte Coverage** | Deals nach Übereinstimmung des Close-Dates mit dem Zeitraumende gewichten |
| **Source-Mix** | Aufschlüsselung der Pipeline nach Quelle (Inbound, Outbound, Expansion, Partner) — Übergewicht einer Quelle ist ein Coverage-Risiko |

## Ausgabevorlage: Forecast-Zusammenfassung

```
# Umsatz-Forecast: [Zeitraum]
**Erstellt**: [Datum]  |  **Quota**: [Ziel]
**Forecast-Methode**: [Stage-basiert / Eingeschätzte Confidence / Gemischt]

## Forecast nach Kategorie
| Kategorie    | Anzahl Deals | Gesamtwert    | Gewichteter Wert | % vom Quota |
| ------------ | ------------ | ------------- | ---------------- | ----------- |
| Closed Won   | [N]          | [Wert]        | [Wert]           | [%]         |
| Commit       | [N]          | [Wert]        | [Gewichtet]      | [%]         |
| Best Case    | [N]          | [Wert]        | [Gewichtet]      | [%]         |
| Pipeline     | [N]          | [Wert]        | [Gewichtet]      | [%]         |
| **Total**    | [N]          | [Wert]        | [Gewichtet]      | [%]         |

## Gap-Analyse
- **Commit-Gap**: [Quota] - [Commit gewichtet] = [Lücke/Überschuss]
- **Best-Case-Gap**: [Quota] - [Commit + Best Case gewichtet] = [Lücke/Überschuss]
- **Coverage-Ratio**: [X]x roh | [Y]x gewichtet | [Z]x qualitätsbereinigt

## Risiko-Report
| Deal          | Wert    | Kategorie  | Risikoflags    | Schwere  | Empfohlene Maßnahme |
| ------------- | ------- | ---------- | -------------- | -------- | ------------------- |
| [Deal-Name]   | [Wert]  | [Kategorie]| [Flags]        | [H/M]    | [Konkrete Aktion]   |

## Deals mit höchster Beweglichkeit (Gap-schließende Opportunities)
| Deal          | Wert    | Aktuelle Kategorie | Was zum Vorankommen nötig ist | Wahrscheinlichkeit des Vorankommens |
| ------------- | ------- | ------------------ | ----------------------------- | ----------------------------------- |
| [Deal-Name]   | [Wert]  | [Kategorie]        | [Konkreter Blocker]           | [Auf Basis von Evidenz]             |

## Bedarf an Pipeline-Generierung
- **Coverage-Status**: [Ausreichend / Dünn / Kritisch]
- **Empfohlene neue Pipeline**: [Auf Basis von Coverage-Lücke und historischer Conversion benötigter Betrag]
- **Dringlichkeit**: [Auf Basis der verbleibenden Tage im Zeitraum und typischer Cycle-Länge]

## Annahmen & Vorbehalte
- [Liste jede Annahme auf, die in diesen Forecast eingeflossen ist]
- [Markiere Datenqualitätsprobleme, fehlende historische Baselines oder Deals mit unzureichenden Informationen]
```

## Leitplanken

1. Erzeuge niemals Pipeline-Daten. Alle Deal-Namen, Werte, Stages und Close-Dates müssen vom Nutzer oder aus dem CRM kommen. Wenn keine Pipeline-Daten vorliegen, erzeuge die Forecast-Vorlage mit "[Pipeline-Daten erforderlich]" in jedem Feld.
2. Schreibe niemals Conversion-Raten oder Wahrscheinlichkeiten vor. Alle Stage-Wahrscheinlichkeiten, Coverage-Ratios und Win Rates müssen aus den eigenen historischen Daten des Kunden abgeleitet werden. Falls nicht verfügbar, kennzeichne als "[Historische Baseline erforderlich — Platzhalter verwendet]".
3. Quellenkennzeichnung. Versieh jede Aussage mit einem Tag — [Aus CRM], [Aus Nutzereingabe], [Aus historischen Daten], [KI-Einschätzung]. KI-Kategorieempfehlungen müssen zur Rep-Validierung markiert werden.
4. Menschliches Urteil erforderlich. Füge auf allen Ausgaben hinzu: "Dieser Forecast ist ein Entscheidungs-Hilfsmittel. Kategoriezuordnungen und Risikobewertungen erfordern vor der Abgabe die Validierung durch Rep und Manager."

> **Tipp:** Fordere über companyFILES eine XLSX-Ausgabe an, um eine formatierte, sofort verteilbare Tabelle zu erhalten (auch DOCX oder Markdown möglich).
