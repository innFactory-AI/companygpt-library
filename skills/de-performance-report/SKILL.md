---
name: de-performance-report
description: Erstellt Marketing-Performance-Reports mit Trendanalyse, Wins/Misses, Attributionshinweisen und priorisierten Optimierungsempfehlungen. Verwende ihn, wenn du ein wöchentliches oder monatliches Marketing-Review vorbereitest, den Kampagnen-ROI analysierst oder einen Funnel-Einbruch diagnostizierst. Auslösen mit "Marketing-Performance-Report", "Kampagnenanalyse", "was funktioniert im Marketing".
---

# Performance-Report-Skill

Erstelle Messpläne, wähle Attributionsmodelle aus, analysiere Kampagnenergebnisse und entwirf Marketing-Experimente. Alle Performance-Daten kommen aus deinen Quellen — der Skill liefert Prozess und Struktur, keine Benchmarks.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Analytics & Ad-Plattformen über MCP** (z. B. GA4, Ad-Plattformen) | Traffic, Impressions, Klicks, Spend, Conversions, Kampagnen-Performance |
| **CRM über MCP** (z. B. HubSpot) | Leads, Pipeline-Einfluss, Deals, CAC-Inputs, Closed-Won-Daten |
| **companyRAG-Sammlungen** | Historische Reports, Messpläne, Kampagnen-Briefings, frühere Lernerkenntnisse |
| **Datei-Upload (CSV/XLSX-Exporte)** | Manuell exportierte Kampagnendaten, Funnel-Auswertungen, Spend-Tabellen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Auswahl des Attributionsmodells

Dies ist das zentrale Entscheidungsframework des Skills. Verwende es, wenn ein Kunde einen Attributionsansatz wählen, bewerten oder migrieren muss.

### Entscheidungsbaum

Vorfilter: Wenn mehr als die Hälfte der Kunden-Touchpoints offline stattfinden (Events, Telefonate, Direct Mail, Field Sales), beginne mit Marketing Mix Modeling (siehe Abschnitt MMM vs. MTA weiter unten) statt mit diesem digital orientierten Attributions-Entscheidungsbaum.

Bewerte jeden Faktor, um den richtigen Modelltyp zu bestimmen. Die Mehrheitsspalte gewinnt; bei Gleichstand mit Multi-Touch starten.

| Faktor | Single-Touch | Multi-Touch | Hybrid |
| --- | --- | --- | --- |
| Länge des Sales-Cycles | Kurz (< 30 Tage typisch) | Mittel (30–180 Tage typisch) | Lang (> 180 Tage typisch) oder gemischt |
| Durchschnittliche Touchpoints pro Conversion | Wenige (1–3 typisch) | Moderat (4–10 typisch) | Viele (> 10 typisch) oder unbekannt |
| Datenreife | Basic (Last-Click verfügbar) | Mittel (Multi-Touch-Tracking) | Fortgeschritten (Cross-Device, offline) |
| Marketing-Kanäle | 1–2 dominant | 3–5 aktiv | 6+ mit Offline-Mix |
| Analytics-Investment | Minimal | Moderat | Erheblich |

Diese Schwellenwerte sind Startpunkte — kalibriere sie auf dein Geschäft. Ein "kurzer" Cycle für Enterprise-Software unterscheidet sich von einem "kurzen" Cycle für Consumer Goods.

**Auswahlprozess**:

1. Bewerte jeden Faktor anhand der Tabelle oben
2. Zeigt die Mehrheit auf eine Spalte, verwende diesen Modelltyp
3. Bei Gleichstand mit Multi-Touch starten (am vielseitigsten) und Komplexität ergänzen, sobald die Daten reifen
4. Dokumentiere die Auswahlbegründung vor der Implementierung — quartalsweise überprüfen

### Single-Touch-Modelle

| Modell | Verwenden wenn | Limitierung |
| --- | --- | --- |
| First-Click | Awareness ist der primäre Engpass | Ignoriert Conversion-Optimierung |
| Last-Click | Conversion-Optimierung steht im Fokus | Ignoriert Awareness-Generierung |

Wähle Single-Touch nur, wenn der Entscheidungsbaum klar dorthin zeigt. Im Zweifel Multi-Touch verwenden.

### Multi-Touch-Modelle

| Modell | Credit-Verteilung | Am besten für |
| --- | --- | --- |
| Linear | Gleichmäßig auf alle Touchpoints | Kein klar dominanter Touchpoint, explorative Phase |
| Time-Decay | Mehr Credit für jüngere Touchpoints | Kurze Consideration-Cycles, Recency zählt |
| Position-based (U-shaped) | Üblicher Default: 40/40/20 First/Last/Middle — an deine Daten anpassen | Awareness und Conversion sind gleich wichtig |
| W-shaped | Üblicher Default: 30/30/30/10 First/Lead-Creation/Last/Middle — an deine Daten anpassen | B2B mit eindeutigem Lead-Creation-Moment |
| Algorithmisch/datengetrieben | ML-basiert, variiert nach Daten | Große Datenmengen, reifes Analytics-Team |

**Multi-Touch-Auswahl innerhalb der Kategorie**:

```
Hast du ein eindeutiges Lead-Creation-Event (z. B. Formular-Ausfüllung, Trial-Start)?
  JA   --> W-shaped (bei B2B) oder Position-based (bei B2C)
  NEIN --> Ist Recency ein starkes Signal in deinen Conversion-Daten?
            JA   --> Time-Decay
            NEIN --> Hast du genug Daten für algorithmisches Modeling?
                      JA   --> Algorithmisch/datengetrieben
                      NEIN --> Linear (sicherster Default)
```

### MMM-vs.-MTA-Entscheidungsframework

Diese sind komplementär, nicht konkurrierend. Nutze dieses Framework, um zu bestimmen, was priorisiert oder wie beides kombiniert wird.

| Faktor | Marketing Mix Modeling (MMM) | Multi-Touch Attribution (MTA) |
| --- | --- | --- |
| Datenanforderung | Aggregiert (Spend, Umsatz, externe Faktoren) | Individuell (User Journeys) |
| Zeithorizont | Langfristig (12–24 Monate Historie nötig) | Kurzfristig (Echtzeit oder nahe) |
| Offline-Kanäle | Gut abbildbar (TV, Radio, Print, Events) | Ohne Workarounds nicht trackbar |
| Digitale Kanäle | Grob (Kanal-Ebene) | Granular (Kampagne, Ad, Keyword) |
| Datenschutz-Auswirkung | Gering (kein individuelles Tracking) | Hoch (erfordert User-Level-Daten) |
| Am besten für | Budget-Allokation über Kanäle | Optimierung innerhalb digitaler Kanäle |
| Update-Frequenz | Quartalsweise oder seltener | Kontinuierlich |

**Komplementäres Nutzungsmuster**: MMM für die Budget-Allokation auf Kanalebene, MTA für die Optimierung innerhalb der Kanäle. Wenn beide verfügbar sind, setzt MMM den Budgetrahmen pro Kanal; MTA optimiert den Spend innerhalb jedes Rahmens.

**Auswahl, wenn nur eines machbar ist**:

```
Hast du signifikanten Offline-Media-Spend (TV, Radio, Print, Events)?
  JA   --> Mit MMM starten (MTA kann Offline-Impact nicht erfassen)
  NEIN --> Ist User-Level-Tracking über deine digitalen Kanäle verfügbar?
            JA   --> Mit MTA starten (schnellere Feedback-Loops)
            NEIN --> Mit MMM starten (funktioniert mit aggregierten Daten)
```

### Migrationspfad für Attributionsmodelle

Beim Wechsel von einem einfacheren zu einem komplexeren Modell:

1. Lasse das neue Modell 1–2 volle Sales-Cycles parallel laufen, bevor du umstellst
2. Vergleiche die Outputs: Wo stimmen die Modelle überein? Wo weichen sie ab?
3. Untersuche Abweichungen — sie zeigen, welche Kanäle über-/unterbewertet werden
4. Stelle das primäre Reporting erst um, nachdem die Stakeholder über die Implikationen des neuen Modells abgestimmt sind
5. Halte das alte Modell im ersten Quartal nach der Umstellung zum Vergleich verfügbar

## Aufbau des Messplans

Strukturierte Methodik, um einen Messplan von Grund auf zu erstellen. Folge allen vier Schritten in der Reihenfolge; das Überspringen von Schritten erzeugt unvollständige Pläne.

### Schritt 1: KPI-Hierarchie nach Funnel-Stufe

| Funnel-Stufe | Metrik-Typen | Beispiele für Metrik-Namen (niemals WERTE generieren) |
| --- | --- | --- |
| Awareness | Reichweite, Sichtbarkeit | Impressions, Reach, Share-of-Voice, Brand Recall |
| Consideration | Engagement, Interesse | Click-Through-Rate, Time on Page, Content-Downloads, E-Mail-Öffnungen |
| Conversion | Aktion, Akquise | Conversion Rate, CAC, Cost per Lead, beeinflusste Pipeline, erstellte Deals |
| Retention | Loyalität, Expansion | Customer Lifetime Value, Churn Rate, NPS, Expansion Revenue |

HINWEIS: Diese Tabelle benennt Metrik-TYPEN als Methodik. Sie generiert niemals konkrete Ziel-WERTE oder Benchmarks. Der Kunde legt seine eigenen Baselines aus seinen eigenen historischen Daten fest.

**KPI-Auswahlprozess**:

1. Identifiziere 1–2 primäre Metriken pro Funnel-Stufe, die zum Kampagnenziel passen
2. Definiere Leading Indicators (prädiktiv) und Lagging Indicators (Ergebnis) für jede
3. Lege fest, welche Metriken der Kunde mit der aktuellen Infrastruktur tatsächlich tracken kann
4. Entferne jede Metrik, die nicht zuverlässig messbar ist — ein nicht messbarer KPI ist schlimmer als keiner

### Schritt 2: Auswahl des Attributionsfensters

| Sales-Cycle | Empfohlenes Fenster | Begründung |
| --- | --- | --- |
| < 7 Tage | 7–14 Tage | Kurze Consideration, jüngste Touchpoints zählen |
| 7–30 Tage | 30–60 Tage | Trial-Phase + Vor-Trial-Recherche |
| 30–90 Tage | 60–90 Tage | Mehrere Stakeholder, längere Evaluierung |
| 90+ Tage | 90–180 Tage | Komplexe Buying-Committees, lange Evaluierungs-Cycles |

Setze das Fenster, BEVOR du die Kampagne startest. Ein Wechsel des Attributionsfensters mitten in der Kampagne entwertet Vergleiche.

### Schritt 3: Design der Reporting-Kadenz

| Report-Typ | Häufigkeit | Zielgruppe | Fokus |
| --- | --- | --- | --- |
| Kampagnen-Puls | Wöchentlich | Kampagnen-Manager | Leading Indicators, Spend-Pacing, Anomalie-Erkennung |
| Performance-Review | Monatlich | Marketing-Leitung | KPI-Trends, Kanaleffektivität, Budget-Umverteilung |
| Strategie-Review | Quartalsweise | CMO / Exec-Team | ROI, Attributions-Insights, Budget-Empfehlungen |
| Jahresanalyse | Jährlich | Board / C-Suite | Year-over-Year-Trends, strategische Investitionsempfehlungen |

Jeder Report-Typ sollte ein definiertes Template, einen Verantwortlichen und einen Verteiler haben, bevor die Kampagne startet.

### Schritt 4: Methodik zum Setzen von Baselines

Wie du Baselines aus DEINEN Daten festlegst (nicht aus Branchendurchschnitten):

1. Sammle 3–6 Monate historische Daten pro Metrik
2. Berechne Mittelwert und Standardabweichung für jede Metrik
3. Setze Ziele: Baseline + Verbesserungsziel basierend auf Investitionsniveau und historischer Varianz
4. Tracke die Abweichung von DEINER Baseline, nicht von externen Benchmarks
5. Setze die Baseline jährlich neu oder nach signifikanten Änderungen des Geschäftsmodells

Wenn keine historischen Daten verfügbar sind: Führe eine reine Messphase (keine Optimierungsänderungen) über 4–8 Wochen durch, um Baselines festzulegen, bevor du Ziele setzt.

Dokumentiere den Messplan anhand der vier Schritte oben (KPI-Hierarchie, Attributionsfenster, Reporting-Kadenz, Baselines) in einem strukturierten Ausfüllformat, das deine Organisation bevorzugt.

## Methodik der Kampagnenanalyse

Strukturierter Prozess zur Post-Campaign-Analyse. Folge allen vier Schritten der Reihe nach.

### Schritt 1: Hypothesen-Dokumentation

Dokumentiere vor der Analyse:

```
HYPOTHESE KAMPAGNENANALYSE:
  Ziel:               [Was wollte die Kampagne erreichen?]
  Erwartetes Ergebnis: [Was haben wir quantifiziert erwartet?]
  Erfolgsmetriken:    [Welche konkreten Metriken definieren Erfolg?]
  Erfolgsschwelle:    [Welcher Wert je Metrik = Erfolg?]
  Zeitraum:           [Kampagnendaten + Attributionsfenster]
```

Fülle dies aus, BEVOR du die Ergebnisse betrachtest, um nachträgliche Rationalisierung zu vermeiden.

### Schritt 2: Checkliste zur Datenerhebung

| Element | Angabe |
| --- | --- |
| Zeitraum | Kampagnenstart/-ende + Verlängerung um das Attributionsfenster |
| Datenquellen | Analytics-Plattform, CRM, Ad-Plattformen, Call-Tracking etc. |
| Segmente | Geografisch, Audience, Kanal, Creative-Varianten |
| Baseline | Vor-Kampagnen-Zeitraum gleicher Länge zum Vergleich |
| Kontrollgruppe | Falls verfügbar, nicht exponierte Gruppe für kausale Inferenz |

Markiere alle Lücken in Datenquellen: "Daten zu Kanal X nicht verfügbar — Analyse schließt diesen Kanal aus."

### Schritt 3: Performance-Dekomposition

Systematischer Drilldown vom Gesamtbild ins Granulare. Vergleiche auf jeder Ebene gegen die in Schritt 1 dokumentierte Hypothese.

**Gesamt**: Hat die Kampagne ihre erklärten Ziele erreicht? Ja / Nein / Teilweise — mit Daten.

**Nach Kanal**: Welche Kanäle haben Ergebnisse erzielt? Welche haben relativ zum Spend underperformt?

```
KANAL-DEKOMPOSITION:
  Kanal:           [Name]
  Spend:           [aus Kundendaten]
  Primäre Metrik:  [Wert aus Kundendaten]
  Cost per Result: [berechnet]
  vs. Baseline:    [% Veränderung gegenüber Vor-Kampagnen-Zeitraum]
  Bewertung:       [Über/Unter/An der erwarteten Performance]
```

**Nach Audience**: Welche Segmente haben reagiert? Welche nicht? Unerwartete Segmente?

**Nach Creative**: Welche Messaging- oder Creative-Varianten haben performt? Dokumentiere die konkreten Unterschiede zwischen Varianten — nicht nur "Creative A hat gewonnen", sondern was sich unterschied (Headline, CTA, Bildsprache, Angebot).

**Nach Timing**: Wann erreichte die Performance ihren Höhepunkt? Wochentags-Muster, Tageszeit-Muster, Fatigue-Kurven.

### Schritt 4: Insight-Extraktion

Dokumentiere für jeden Befund:

| Element | Inhalt |
| --- | --- |
| Befund | Was passiert ist (datengestützt, Quelle und Zeitraum nennen) |
| Konfidenz | Hoch / Mittel / Niedrig (basierend auf Stichprobengröße und Datenqualität) |
| Warum es wichtig ist | Business-Impact, wo möglich quantifiziert |
| Empfohlene Maßnahme | Konkreter, testbarer nächster Schritt |
| Nötige Daten zur Validierung | Was diesen Befund bestätigen oder widerlegen würde |

Teile Befunde auf in: bestätigt (hohe Konfidenz, ausreichende Daten), direktional (mittlere Konfidenz, handlungswürdig mit Monitoring) und Hypothesen (niedrige Konfidenz, weiteres Testen nötig).

Strukturiere die Post-Campaign-Analyse anhand der Schritte oben (Hypothesen-Dokumentation, Daten-Checkliste, Performance-Dekomposition, Insight-Extraktion).

## A/B-Test-Framework

Methodik zum Experiment-Design für Marketing. Verwende sie immer dann, wenn du Tests von Messaging, Creatives, Kanälen, Audiences oder Angeboten entwirfst.

### Hypothesen-Struktur

"Wenn wir [Änderung] machen, dann wird [Metrik] um [Größenordnung] [Richtung] gehen, weil [Begründung]."

Alle fünf Elemente sind erforderlich. Eine Hypothese ohne Begründung ist nur eine Vermutung; eine Hypothese ohne Größenordnung macht es unmöglich, die nötige Stichprobengröße zu bestimmen.

### Design-Checkliste

| Element | Anforderung |
| --- | --- |
| Einzelvariable | Nur eine Sache unterscheidet A und B |
| Erfolgsmetrik | Primäre Metrik vor dem Start definiert |
| Guardrail-Metriken | Sekundäre Metriken, die sich nicht verschlechtern dürfen |
| Stichprobengröße | Für statistische Signifikanz berechnet (Tools nutzen, nicht raten) |
| Dauer | Lang genug für volle Geschäftszyklen (Wochenmuster, Zahltage, Saisonalität) |
| Segmentierung | Segmente für Post-hoc-Analyse vordefinieren (auf Simpson-Paradoxon in Segmentergebnissen prüfen) |
| Minimum Detectable Effect | Kleinste bedeutsame Differenz, die eine Umsetzung wert ist |
| Kein vorzeitiges Stoppen | Test nicht stoppen oder Gewinner erklären, bevor die geplante Stichprobengröße erreicht ist |

Für regulierte Branchen: Prüfe, ob die Testvarianten den branchenspezifischen Content-Anforderungen entsprechen (Pharma-MLR-Freigabe, Financial-FINRA-Review, Healthcare-HIPAA-Überlegungen), bevor du Experimente startest.

### Interpretation der Ergebnisse

| Ergebnis | Maßnahme |
| --- | --- |
| Statistisch signifikant + bedeutsame Effektgröße | Gewinner umsetzen, Learning dokumentieren |
| Statistisch signifikant + triviale Effektgröße | Operativen Aufwand der Änderung gegen Gewinn abwägen |
| Nicht signifikant + ausreichende Stichprobe | Kein erkennbarer Unterschied — eine größere Änderung testen |
| Nicht signifikant + unzureichende Stichprobe | Test verlängern oder Traffic-Allokation erhöhen |

### Test-Priorisierung

Wenn mehrere Tests möglich sind, priorisiere mit:

```
PRIORISIERUNGS-SCORE:
  Impact:     [Hoch/Mittel/Niedrig] -- Wie stark könnte dies die primäre Metrik bewegen?
  Konfidenz:  [Hoch/Mittel/Niedrig] -- Wie stark ist die Begründung?
  Aufwand:    [Hoch/Mittel/Niedrig] -- Wie schnell lässt sich dies umsetzen und messen?

  Priorität = Impact x Konfidenz x Aufwand (Hoch=3, Mittel=2, Niedrig=1)
  Höchstbewertete Tests zuerst durchführen.
```

## Funnel-Diagnose

Systematischer Ansatz zur Diagnose von Funnel-Performance-Problemen. Verwende ihn, wenn Conversion Rates unter den Erwartungen liegen oder zurückgehen.

### Diagnoseprozess

**1. Funnel-Stufen abbilden**

Definiere den tatsächlichen Funnel des Kunden (kein generisches Template). Übliche Stufen: Awareness, Consideration, Conversion, Retention — aber nutze die Terminologie und Stufendefinitionen des Kunden.

**2. Stufenweise Conversion Rates aus DEINEN Daten berechnen**

Verwende niemals angenommene oder "typische" Raten. Sind für eine Stufe keine Daten verfügbar, kennzeichne sie als blinden Fleck.

**3. Den größten absoluten Drop-off identifizieren**

Fokussiere auf die Stufe mit dem größten absoluten Volumenverlust, nicht nur auf den niedrigsten Prozentsatz. Ein 50%-Drop von 10.000 auf 5.000 wiegt schwerer als ein 70%-Drop von 100 auf 30.

**4. Die Drop-off-Stufe diagnostizieren**

Untersuche für jede Drop-off-Stufe die passenden Ursachen:

- Awareness → Consideration-Drop: Targeting-Kriterien, Messaging-Resonanz, Kanal-Mix, Angebotsqualität, Geschwindigkeit des Sales-Follow-ups prüfen
- Consideration → Conversion-Drop: Landingpages, Preisdarstellung, Social Proof, CTA-Klarheit, Beschaffungs-Friction, Compliance-Hürden, Budget-Freigabeprozess prüfen
- Conversion → Retention-Drop: Onboarding-Flow, Time-to-First-Value, Churn-Surveys, Implementierungskomplexität, Servicequalität prüfen
- Zuvor stabile Stufe rückläufig: Mit Vorperioden vergleichen, Wettbewerbsumfeld prüfen, Audience-Frische prüfen

**5. Eine Hypothese zur Grundursache formulieren**

Verwende dieselbe Hypothesen-Struktur wie im A/B-Test-Framework: "Wenn [Grundursache], dann wird [ihre Behebung] [Metrik verbessern] um [Größenordnung], weil [Begründung]."

**6. Eine konkrete, testbare Intervention entwerfen**

Nicht "die Landingpage verbessern", sondern "die Headline von feature-orientiert auf ergebnisorientiert ändern" oder "Kundenstimmen above the fold ergänzen". Vage Interventionen erzeugen nicht interpretierbare Ergebnisse.

**7. Die Intervention testen**

Verwende das A/B-Test-Framework oben. Lässt sich die Intervention nicht per A/B-Test prüfen (z. B. eine Preisänderung), nutze ein Vorher/Nachher-Design mit passenden Kontrollen und Hinweisen auf Confounding-Faktoren.

### Funnel-Health-Monitoring

Laufendes Monitoring-Framework (nicht nur eine einmalige Diagnose):

| Check | Häufigkeit | Alert-Trigger |
| --- | --- | --- |
| Stufen-Conversion-Rates | Wöchentlich | Schwelle anhand deiner historischen Varianz definieren (z. B. 2+ Standardabweichungen) |
| Funnel-Velocity (Zeit zwischen Stufen) | Wöchentlich | Steigender Trend über 3+ Wochen |
| Stufen-Volumen | Wöchentlich | Signifikanter Rückgang gegenüber Vorperiode (Schwelle anhand deiner Daten definieren) |
| Drop-off-Konzentration | Monatlich | Einzelne Stufe verantwortet > 50 % des gesamten Funnel-Verlusts |

## Vorlagen

- Vorlage für Kampagnenanalyse — heranziehen, wenn du Kampagnen-Performance analysierst
- Vorlage für Messplan — heranziehen, wenn du einen Messplan erstellst

Diese Vorlagen kannst du als companyRAG-Sammlung hinterlegen oder als Datei hochladen, damit der Skill konsistent darauf aufbaut.

## Leitplanken

- Generiere niemals Benchmark-Daten, Conversion Rates oder Branchendurchschnitte. Metrik-Typen zu benennen (CAC, Pipeline-Velocity) ist Methodik; konkrete Werte zu generieren ist Erfindung.
- Nenne bei der Analyse von Kampagnen immer die konkrete Datenquelle und den Zeitraum. Verwende im Zweifel "unzureichende Daten zur Bestimmung" statt zu spekulieren.
- Menschliche Verifizierung ist erforderlich für Empfehlungen zur Budget-Allokation, Änderungen am Attributionsmodell und das Setzen von KPI-Zielen.
- Kennzeichne Outputs: [Aus Kundendaten] für gequellte Daten · [Framework-Methodik] für den Ansatz dieses Skills · [KI-Analyse] für Modell-Synthese. Verwende [Konfidenz hoch/mittel/niedrig]-Bewertungen.

> **Hinweis:** Der Skill rechnet selbst keine Queries — er analysiert die Daten, die du bereitstellst. Fordere über companyFILES eine XLSX-, PPTX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Report zu erhalten.
