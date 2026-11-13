---
name: de-account-research
description: Recherchiert ein Unternehmen oder einen Prospect zu verwertbaren Sales-Insights — Überblick, aktuelle Signale, Schlüsselpersonen und Gesprächsaufhänger. Verwende ihn, wenn du dich auf ein Erstgespräch vorbereitest, einen neuen Account übernimmst oder veraltetes Account-Wissen auffrischst. Auslösen mit "Recherchiere [Unternehmen]", "Was muss ich über [Account] wissen", "Account-Briefing für".
---

# Account-Research-Skill

Verwandle Rohdaten zu einem Unternehmen in verwertbare Sales-Intelligence — Account-Briefings, Signal-Zusammenfassungen, Profile von Schlüsselpersonen und Gesprächsaufhänger. Alle Unternehmensdaten kommen von dir, aus einer angebundenen MCP-Quelle, aus der Websuche oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CRM über MCP** (z. B. Salesforce, HubSpot, Dynamics) | Deal-Historie, vergangene Interaktionen, bestehende Kontakte, Notizen des Account-Owners |
| **Websuche** (Unternehmenswebsite, News, Pressemitteilungen) | Aktuelle Ankündigungen, Führungswechsel, Produkt-Launches, Finanzkennzahlen |
| **Enrichment-Daten über MCP** (z. B. LinkedIn, Crunchbase, Owler) | Firmografische Daten, Finanzierungsrunden, Headcount-Trends, Tech-Stack |
| **companyRAG / Datei-Upload** | Historischer Kontext, Wettbewerbspositionierung, Persona-Definitionen, Geschäftsberichte (z. B. Annual Report, 10-K, Earnings Call) |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

Wenn eine Datenquelle nicht verfügbar ist, weise die Lücke im Output explizit aus, statt sie mit Annahmen zu füllen.

## Recherche-Workflow

```
1. ZIEL identifizieren
   |
   +--> Unternehmensname + Kontext vom Nutzer
   +--> CRM auf bestehenden Account-Datensatz prüfen
   |      GEFUNDEN --> Deal-Historie, Kontaktliste, Notizen ziehen
   |      NICHT GEFUNDEN --> Als Net-New-Account markieren
   |
2. Firmografische Basis ZUSAMMENTRAGEN
   |
   +--> Unternehmensüberblick: Branche, HQ, Mitarbeiterzahl, Umsatzrange
   +--> Geschäftsmodell: an wen sie verkaufen, wie sie Mehrwert liefern
   +--> Wachstumsentwicklung: Hiring-Trends, Finanzierung, Expansionssignale
   +--> Tech-Stack: bekannte Tools und Plattformen (nur aus Enrichment oder Nutzereingabe)
   |
3. Aktuelle SIGNALE finden (letzte 90 Tage priorisiert)
   |
   +--> Führungswechsel (C-Level, VP-Level: Neueinstellungen/Abgänge)
   +--> Earnings- oder Finanzierungsereignisse
   +--> Produkt-Launches oder Pivots
   +--> Partnerschaften oder Übernahmen
   +--> Regulatorische oder Compliance-Entwicklungen
   +--> Entlassungen, Restrukturierungen oder strategische Verschiebungen
   |
4. Schlüsselpersonen ABBILDEN
   |
   +--> Wahrscheinliche Rollen im Buying Center identifizieren (siehe Mapping unten)
   +--> CRM-Kontakte mit der aktuellen Org abgleichen
   +--> Veraltete Kontakte markieren (Rolle gewechselt, Unternehmen verlassen)
   +--> Warm Paths identifizieren (gemeinsame Kontakte, vergangene Interaktionen)
   |
5. Gesprächsaufhänger HERAUSARBEITEN
   |
   +--> Signale mit deinem Value Proposition matchen (siehe Hook-Generierung unten)
   +--> Durch Signale implizierte Pain Points identifizieren
   +--> 2–3 Einstiegswinkel entwerfen, nach Relevanz gerankt
   |
6. Account-Briefing ZUSAMMENSTELLEN (siehe Ausgabevorlage unten)
```

## Signal-Kategorisierung

Klassifiziere jedes Signal nach Typ und Sales-Relevanz:

| Signaltyp | Beispiele | Sales-Relevanz |
| --- | --- | --- |
| **Growth** | Finanzierungsrunde, IPO-Filing, Marktexpansion | Budgetverfügbarkeit, Skalierungsdruck, Spend für neue Initiativen |
| **Leadership Change** | Neuer CxO, VP-Einstellung in der Zielfunktion | Frisches Mandat, Bereitschaft, neue Anbieter zu evaluieren |
| **Strategic Shift** | Digitale Transformation, Eintritt in neuen Markt, M&A | Neubewertung bestehender Tools, erweitertes Buying Center |
| **Pain Indicator** | Entlassungen, verfehlte Earnings, Produktrückruf, Churn-News | Kostendruck, Effizienzbedarf, Druck, Ergebnisse zu liefern |
| **Regulatory** | Neue Compliance-Anforderungen, Audit-Befunde | Compliance-getriebener Kauf, verbindlicher Zeitrahmen |
| **Technology** | Plattformmigration, Tool-Konsolidierung, ausgeschriebener RFP | Aktiver Evaluierungszyklus, definierter Beschaffungszeitrahmen |
| **Competitive** | Wettbewerber in News erwähnt, Anbieterwechsel | Displacement-Chance, Unzufriedenheitssignal |

Recency-Gewichtung: Signale der letzten 30 Tage haben höchste Relevanz, 30–90 Tage moderate, jenseits von 90 Tagen als potenziell veraltet markieren.

## Mapping von Schlüsselpersonen

Erfasse für jeden identifizierten Kontakt:

| Feld | Beschreibung |
| --- | --- |
| **Name & Titel** | Aktuelle Rolle im Unternehmen (Aktualität verifizieren) |
| **Rolle im Buying Center** | Economic Buyer, Champion, Technical Evaluator, End User, Blocker |
| **Relevanz** | Warum diese Person für deinen Deal wichtig ist (funktionale Verantwortung) |
| **Warm Path** | Gemeinsame Kontakte, frühere Interaktionen, gemeinsame Events |
| **Engagement-Status** | Neuer Kontakt / Bestehende Beziehung / Veraltet (kein Kontakt seit >6 Monaten) |

Wenn keine Enrichment-Daten verfügbar sind, liste den benötigten Rollen-Archetyp (z. B. "VP Engineering — noch nicht identifiziert"), damit der Rep weiß, wonach zu suchen ist.

### Heuristiken zur Org-Navigation

Nutze bei unbekannten Organisationen diese Muster, um wahrscheinliche Entscheider zu identifizieren:

- Top-down-Signal: Führungseinstellung in der Zielfunktion → diese Person verantwortet wahrscheinlich die Initiative
- Bottom-up-Signal: Stellenausschreibungen für Rollen nahe deiner Lösung → der einstellende Manager ist ein potenzieller Champion
- Laterales Signal: Bestehender Kundenkontakt ist zu diesem Unternehmen gewechselt → Pfad für eine warme Vorstellung
- Beschaffungssignal: Erwähnungen von RFP oder Anbieter-Review → die Beschaffungsleitung ist ein Gatekeeper, den man früh mappen sollte

## Hook-Generierung

Ein Gesprächsaufhänger verbindet ein Signal mit einem Pain Point, den deine Lösung adressiert. Jeder Hook folgt dieser Struktur:

```
SIGNAL: [Was passiert ist — belegter Fakt]
  |
  +--> IMPLIKATION: [Was das für ihr Geschäft wahrscheinlich bedeutet]
  |
  +--> VERBINDUNG: [Wie deine Lösung für diese Implikation relevant ist]
  |
  +--> OPENER: [Eine konkrete Frage oder Aussage, um das Gespräch zu starten]
```

### Qualitätskriterien für Hooks

| Kriterium | Starker Hook | Schwacher Hook |
| --- | --- | --- |
| **Spezifität** | Verweist auf ein konkretes Signal mit Datum/Quelle | Allgemeine Branchenbeobachtung |
| **Relevanz** | Verbindet direkt mit den genannten Prioritäten des Prospects | Tangential zum Geschäft |
| **Aktualität** | Basiert auf einem aktuellen Ereignis (idealerweise <30 Tage) | Basiert auf veralteter oder undatierter Information |
| **Value Framing** | Rahmt um das Ergebnis des Kunden, nicht um deine Produktfeatures | Beginnt mit dem Produkt-Pitch |
| **Dialogorientiert** | Lädt zum Dialog ein ("Wie denkst du über …") | Deklarativ ("Du brauchst …") |

Generiere 2–3 Hooks pro Account-Briefing, gerankt nach Signalstärke und Relevanz.

## Ausgabevorlage: Account-Briefing

```
# Account-Briefing: [Unternehmensname]
**Erstellt**: [Datum]  |  **Aktualität der Quellen**: [Datum des jüngsten Signals]

## Unternehmensüberblick
- **Branche**: [Sektor / Subsektor]
- **Hauptsitz**: [Standort]
- **Größe**: [Mitarbeiterzahl-Range] | [Umsatzrange, falls öffentlich/verfügbar]
- **Geschäftsmodell**: [Kurzbeschreibung: was sie tun und für wen]
- **Wachstumsphase**: [Early / Growth / Mature / Turnaround — mit Beleg]

## CRM-Kontext
- **Account-Status**: [Net-New / Bestehend / Churned / Dormant]
- **Frühere Interaktionen**: [Zusammenfassung relevanter CRM-Historie oder "Kein früherer Datensatz"]
- **Bestehende Kontakte**: [Liste oder "Keine erfasst"]

## Aktuelle Signale (letzte 90 Tage)
| Datum  | Signal             | Typ        | Sales-Relevanz                | Quelle      |
| ------ | ------------------ | ---------- | ----------------------------- | ----------- |
| [Datum]| [Konkretes Ereignis]| [Kategorie]| [Warum es für diesen Deal zählt]| [Quellen-Tag]|

## Schlüsselpersonen
| Name   | Titel          | Buying-Rolle      | Warm Path         | Status        |
| ------ | -------------- | ----------------- | ----------------- | ------------- |
| [Name] | [Aktuelle Rolle]| [Rollen-Archetyp]| [Verbindungspfad] | [Engagement]  |

## Gesprächsaufhänger
### Hook 1: [signalbasierter Titel]
- **Signal**: [Fakt + Quelle]
- **Implikation**: [Was es für sie bedeutet]
- **Opener**: "[Vorgeschlagene Frage oder Aussage]"

### Hook 2: [signalbasierter Titel]
...

## Lücken & nächste Schritte
- [ ] [Fehlende Daten, die ergänzt werden müssen — z. B. "VP Engineering identifizieren"]
- [ ] [Erforderliche Verifizierung — z. B. "Bestätigen, dass die Org-Umstrukturierung abgeschlossen ist"]
- [ ] [Empfohlene Aktion — z. B. "Vorstellung über [gemeinsamen Kontakt] anfragen"]
```

## Recherchetiefe je nach Kontext

| Kontext | Tiefe | Fokus |
| --- | --- | --- |
| **Vorbereitung Erstgespräch** | Vollständiges Briefing | Alle Abschnitte, Hooks und Schlüsselpersonen priorisieren |
| **Account-Auffrischung** | Signal- und Kontakt-Update | Neue Signale seit letztem Briefing, Audit veralteter Kontakte |
| **Territory-Planung** | Leichter Scan pro Account | Firmografie + Top-Signal + ICP-Fit-Bewertung |
| **Competitive Deal** | Vollständiges Briefing + Wettbewerbsebene | Abschnitt zur Wettbewerbsintelligenz aus dem Battlecard ergänzen |
| **Expansion Play** | Intern fokussiertes Briefing | Nutzungsdaten, Stakeholder-Wechsel, neue Abteilungen |

## Leitplanken

1. Erfinde niemals Kontakte oder Org-Strukturen. Alle Namen, Titel und Berichtswege müssen vom Nutzer, aus dem CRM, aus Enrichment-Daten oder aus der Websuche stammen. Unverifizierte Kontakte: liste den Rollen-Archetyp als "Noch nicht identifiziert".
2. Generiere niemals Finanzdaten. Umsatzzahlen, Finanzierungsbeträge und Wachstumsraten müssen belegt sein. Wenn nicht verfügbar, schreibe "Nicht öffentlich verfügbar" statt zu schätzen.
3. Quellenkennzeichnung. Versieh jede Aussage mit einem Tag — `[Aus CRM]`, `[Aus Websuche]`, `[Aus Enrichment]`, `[Aus Nutzereingabe]`, `[KI-Inferenz]`. KI-Inferenz muss als verifizierungsbedürftig markiert werden.
4. Verifizierungs-Hinweis. Setze auf jedes Account-Briefing den Hinweis "Schlüsselfakten vor dem kundenseitigen Einsatz verifizieren".

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Account-Briefing zu erhalten.
