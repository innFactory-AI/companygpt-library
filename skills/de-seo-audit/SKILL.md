---
name: de-seo-audit
description: Prüft die SEO-Gesundheit einer Website, deckt Keyword-Chancen auf, identifiziert Content-Lücken und benchmarkt gegen Wettbewerber. Verwende ihn für ein vierteljährliches SEO-Review, zum Diagnostizieren von Traffic-Rückgängen oder zur Planung der Content-Strategie. Auslösen mit "SEO-Audit erstellen für", "Keyword-Chancen", "warum sinkt der Traffic".
---

# SEO-Audit-Skill

Prüfe die SEO-Gesundheit einer Website in fünf Phasen — technisches Audit, Content-Audit, Keyword-Analyse, Wettbewerbs-Benchmarking und priorisierte Empfehlungen. Alle Daten stammen aus deinen SEO-Tools, deiner Analytics und deiner Search Console; der Skill crawlt selbst keine Websites, sondern wertet die von dir bereitgestellten Daten aus.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Search Console über MCP** (z. B. Google Search Console) | Impressionen, Klicks, CTR, Position, Index-Abdeckung, Crawl-Daten |
| **Web-Analytics über MCP** (z. B. GA4) | Traffic-Daten, Nutzerverhalten, Conversions, Performance der Landingpages |
| **SEO-Tools über MCP** (z. B. Ahrefs, Semrush) | Keyword-Rankings, Backlinks, technische Crawl-Daten, Wettbewerbsanalyse |
| **companyRAG-Sammlungen** | Frühere Audits, Keyword-Recherchen, Content-Strategie-Dokumente |
| **Datei-Upload (Crawl-Exporte)** | Crawl-Exporte, CMS-Inventare, Metadaten-Tabellen, Screenshots aus deinen Tools |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## SEO-Audit-Workflow

Führe diese fünf Phasen der Reihe nach aus. Jede Phase baut auf der vorherigen auf und fließt in die priorisierten Empfehlungen ein.

### Phase 1: Technisches Audit

Bewerte die technischen Grundlagen, die Crawlbarkeit, Indexierbarkeit und Site-Performance beeinflussen.

**Checkliste technisches Audit:**

| Kategorie | Prüfung | Worauf achten | Datenquelle |
| --- | --- | --- | --- |
| **Crawlbarkeit** | Robots.txt | Unbeabsichtigte Blockierungen, fehlende Direktiven | Crawl-Export / manuelle Prüfung |
|  | XML-Sitemap | Vorhanden, eingereicht, aktuell, fehlerfrei | Search Console / manuelle Prüfung |
|  | Crawl-Fehler | 4xx, 5xx, Redirect-Ketten, verwaiste Seiten | Search Console / Crawl-Export |
|  | Interne Verlinkung | Defekte Links, tiefe Seiten ohne interne Links | Crawl-Export |
| **Indexierbarkeit** | Index-Abdeckung | Indexierte vs. eingereichte Seiten, Noindex-Fehler | Search Console |
|  | Canonical-Tags | Fehlend, selbstreferenzierend, im Konflikt mit anderen Signalen | Crawl-Export |
|  | Duplicate Content | Identische oder fast identische Seiten ohne Canonical-Auflösung | Crawl-Export |
| **Performance** | Core Web Vitals | LCP-, INP-, CLS-Werte | PageSpeed Insights / Search Console |
|  | Mobile-Usability | Mobile-Fehler, Probleme mit responsivem Design | Search Console / manuelle Prüfung |
|  | Seitengeschwindigkeit | Ladezeiten, render-blockierende Ressourcen, Bildoptimierung | PageSpeed Insights / Crawl-Export |
| **Strukturierte Daten** | Schema-Markup | Vorhanden, valide, relevante Typen (Organisation, Article, Product, FAQ usw.) | Rich-Results-Test / Crawl-Export |
| **Sicherheit** | HTTPS | Vollständige HTTPS-Migration, Mixed Content, Zertifikatsgültigkeit | Crawl-Export / manuelle Prüfung |
|  | Hreflang (bei mehrsprachig) | Korrekte Sprach-/Regionsausrichtung, reziproke Tags | Crawl-Export |

**Ausgabeformat technisches Audit:**

```
TECHNISCHES AUDIT — BEFUND:
  Kategorie:    [Crawlbarkeit / Indexierbarkeit / Performance / strukturierte Daten / Sicherheit]
  Problem:      [konkrete Beschreibung]
  Schweregrad:  [CRITICAL (kritisch) / HIGH (hoch) / MEDIUM (mittel) / LOW (niedrig)]
  Betroffene Seiten: [Anzahl oder Umfang — aus Crawl-Daten]
  Beleg:        [konkreter Datenpunkt aus angebundener Quelle]
  Auswirkung:   [wie dies die Sichtbarkeit oder Nutzererfahrung beeinflusst]
  Empfehlung:   [konkrete Korrektur]
  Aufwand:      [Quick Fix / moderat / erheblich]
```

### Phase 2: Content-Audit

Bewerte Qualität, Relevanz und Performance der bestehenden Inhalte.

**Methodik Content-Audit:**

1. Inventarisiere bestehende Inhalte — erfasse alle indexierbaren Seiten mit ihren Metadaten (Title, Description, H1, Wortzahl, Veröffentlichungsdatum, letzte Aktualisierung)
2. Klassifiziere jede Seite nach Performance:

| Kategorie | Kriterien | Handlungsrichtung |
| --- | --- | --- |
| **Performend** | Rankings + Traffic + Conversions erreichen die Ziele | Halten und schrittweise optimieren |
| **Unterperformend** | Hat Impressionen, aber geringe CTR oder sinkenden Traffic | Optimieren — Title, Meta, Content-Qualität verbessern |
| **Thin** | Geringe Wortzahl, wenig Tiefe, kein einzigartiger Mehrwert | Ausbauen, zusammenführen oder entfernen |
| **Kannibalisierend** | Mehrere Seiten konkurrieren um dasselbe Keyword | Zu einer maßgeblichen Seite zusammenführen |
| **Verfallend** | Performte früher gut, jetzt rückläufig | Auffrischen — Daten aktualisieren, Abdeckung erweitern, erneut bewerben |
| **Verwaist** | Keine internen Links verweisen darauf | Interne Links ergänzen oder Erhalt prüfen |

1. Dokumentiere für jede unter- oder verfallende Seite:

```
CONTENT-AUDIT — SEITE:
  URL:              [Seiten-URL]
  Ziel-Keyword:     [primäres Keyword — aus SEO-Tools oder Nutzereingabe]
  Aktuelle Position: [Ranking — aus SEO-Tools]
  Impressionen:     [aus Search Console]
  Klicks:           [aus Search Console]
  CTR:              [aus Search Console]
  Traffic-Trend:    [wachsend / stabil / rückläufig — aus Analytics]
  Content-Qualität: [Bewertung nach Tiefe, Aktualität, Einzigartigkeit]
  Empfehlung:       [optimieren / auffrischen / zusammenführen / entfernen]
```

### Phase 3: Keyword-Analyse

Identifiziere Keyword-Chancen — Begriffe, bei denen die Website realistisch ihr Ranking verbessern oder neuen Traffic erschließen kann.

**Methodik Keyword-Chancen:**

1. Aktuelles Keyword-Portfolio — liste anhand der SEO-Tools alle Keywords auf, für die die Website aktuell rankt, mit Position, Suchvolumen und Traffic-Beitrag
2. Lückenidentifikation:

| Chancentyp | Definition | Wie finden |
| --- | --- | --- |
| **Quick Wins** | Rankings auf Position 4–20 mit relevantem Suchvolumen | Aktuelle Rankings nach Positionsbereich filtern |
| **Content-Lücken** | Keywords mit Suchvolumen, für die die Website keinen rankenden Content hat | Keyword-Gap-Analyse in SEO-Tools |
| **Long-Tail-Ausbau** | Spezifische Varianten von Keywords, deren Head-Term die Website bereits rankt | Verwandte-Keywords-Analyse, "Nutzer fragen auch"-Daten |
| **Aufkommende Themen** | Wachsende Suchtrends im Themenfeld der Website | Trendanalyse, aufsteigende Suchanfragen in der Search Console |
| **Wettbewerber-Keywords** | Begriffe, für die Wettbewerber ranken und diese Website nicht | Wettbewerber-Keyword-Gap-Analyse |

1. Dokumentiere für jede Chance:

```
KEYWORD-CHANCE:
  Keyword:           [Begriff]
  Suchvolumen:       [aus SEO-Tools — niemals selbst erzeugen]
  Aktuelles Ranking: [Position oder "rankt nicht"]
  Difficulty:        [aus SEO-Tools — niemals selbst erzeugen]
  Chancentyp:        [Quick Win / Content-Lücke / Long-Tail / aufkommend / Wettbewerber]
  Bestehender Content: [URL, falls relevanter Content vorhanden, sonst "keiner"]
  Empfohlene Aktion: [bestehende Seite optimieren / neuen Content erstellen / bestehenden Content erweitern]
  Geschäftsrelevanz: [hoch / mittel / niedrig — wie stark deckt sich dies mit den Geschäftszielen?]
  Priorität:         [aus dem Priorisierungs-Framework in Phase 5]
```

### Phase 4: Wettbewerbs-Benchmarking

Benchmarke die SEO-Performance der Website gegen zentrale Wettbewerber, um relative Stärken und Schwächen zu identifizieren.

**Wettbewerber-Auswahl:**

- Identifiziere 3–5 Wettbewerber: direkte Geschäftswettbewerber UND Such-Wettbewerber (Sites, die für dieselben Keywords ranken, aber keine direkten Geschäftswettbewerber sein müssen)
- Quelle: Nutzereingabe für Geschäftswettbewerber; SEO-Tools für Such-Wettbewerber

**Benchmarking-Dimensionen:**

| Dimension | Zu vergleichende Metriken | Datenquelle |
| --- | --- | --- |
| Domain-Autorität / -Stärke | Domain Rating, Domain Authority oder Äquivalent | SEO-Tools |
| Keyword-Überschneidung | % gemeinsamer Keywords, einzigartige Keywords je Wettbewerber | SEO-Tools |
| Content-Volumen | Anzahl indexierter Seiten, Publishing-Frequenz | SEO-Tools / manuelle Prüfung |
| Backlink-Profil | Gesamtzahl verweisender Domains, Qualitätsverteilung, Link-Velocity | SEO-Tools |
| SERP-Feature-Präsenz | Featured Snippets, Knowledge Panels, Bild-Ergebnisse, Video-Ergebnisse | SEO-Tools / manuelle Suche |
| Content-Tiefe | Durchschnittliche Content-Länge, Breite der Themenabdeckung | SEO-Tools / manuelle Bewertung |

**Ausgabeformat Benchmark:**

```
WETTBEWERBER-BENCHMARK:
  Wettbewerber:   [Name / Domain]
  Beziehung:      [direkter Wettbewerber / Such-Wettbewerber / beides]

  Wo sie uns übertreffen:
  - [Dimension]: [konkreter Beleg aus den Daten]
  - [Dimension]: [...]

  Wo wir sie übertreffen:
  - [Dimension]: [konkreter Beleg aus den Daten]
  - [Dimension]: [...]

  Wichtige Inhalte, die sie haben und wir nicht:
  - [Thema / Keyword]: [ihre URL, Ranking, geschätzter Traffic]

  Umsetzbare Erkenntnis:
  - [konkrete, datengestützte Aktion]
```

### Phase 5: Priorisierte Empfehlungen

Führe die Befunde aller Phasen zu einem priorisierten Aktionsplan zusammen.

**Priorisierungs-Framework:**

Bewerte jede Empfehlung auf drei Dimensionen:

| Dimension | Score 1 (niedrig) | Score 2 (mittel) | Score 3 (hoch) |
| --- | --- | --- | --- |
| **Impact** | Marginale Traffic- oder Ranking-Verbesserung | Moderate Verbesserung bei Ziel-Keywords | Erheblicher Traffic-, Ranking- oder Conversion-Impact |
| **Aufwand** | Erheblicher Entwicklungs- oder Content-Aufwand | Moderater Aufwand — Tage, nicht Wochen | Quick Fix — Stunden, nicht Tage |
| **Confidence** | Hypothese — wenig stützende Daten | Richtungsweisend — teils datengestützt | Starker Beleg aus den Daten |

**Priorität = Impact × Aufwand × Confidence** (max. 27). Führe die höchstbewerteten Aktionen zuerst aus.

**Ausgabeformat Empfehlung:**

```
EMPFEHLUNG [N]:
  Befund:        [Was das Audit ergeben hat]
  Phase:         [Technisch / Content / Keyword / Wettbewerber]
  Aktion:        [konkrete, umsetzbare Empfehlung]
  Impact:        [1–3] — [Begründung]
  Aufwand:       [1–3] — [Begründung]
  Confidence:    [1–3] — [Begründung]
  Prioritäts-Score: [berechnet]
  Verantwortlich: [wer ausführt — SEO, Content, Engineering]
  Zeitrahmen:    [vorgeschlagener Zeitraum]
```

## Ausgabevorlage: SEO-Audit-Report

```
# SEO-Audit-Report — [Domain]
Datum: [Datum]
Audit-Zeitraum: [Datumsbereich der analysierten Daten]
Auditor: [Name]

## Executive Summary
  [3–5 Sätze: Gesamtbewertung der SEO-Gesundheit, Top-3-Chancen, Top-3-Risiken]

## Technische Gesundheit
  Kritische Probleme: [Anzahl]
  Hochpriorisierte Probleme: [Anzahl]
  [Liste der technischen Befunde nach Schweregrad sortiert]

## Content-Bewertung
  Auditierte Seiten gesamt: [Anzahl]
  Performend: [Anzahl] | Unterperformend: [Anzahl] | Thin/entfernen: [Anzahl]
  [Top-Content-Befunde]

## Keyword-Chancen
  Quick Wins: [Anzahl]
  Content-Lücken: [Anzahl]
  [Top-Keyword-Chancen nach Priorität sortiert]

## Wettbewerbs-Landschaft
  [Wichtige Wettbewerber-Erkenntnisse und Lücken]

## Priorisierter Aktionsplan
  [Top 10–15 Empfehlungen nach Prioritäts-Score sortiert]

## Anhang
  [Detaillierte Datentabellen, vollständige Keyword-Listen, technische Crawl-Details]
```

## Leitplanken

- Erzeuge niemals SEO-Metrikwerte (Suchvolumen, Keyword-Difficulty, Domain-Autorität, Traffic-Schätzungen, CTR nach Position). Alle Daten müssen aus deinen Tools stammen.
- Garantiere niemals Ranking-Verbesserungen oder Traffic-Ergebnisse. SEO-Resultate hängen von vielen unkontrollierbaren Faktoren ab.
- Triff niemals qualitative Aussagen über Keywords ("hohes Volumen", "geringe Konkurrenz") ohne Daten aus deinen Tools.
- Kennzeichne Ausgaben: `[Aus SEO-Daten]` für tool-basierte Daten · `[Framework-Methodik]` für den Ansatz dieses Skills · `[KI-Analyse]` für Modell-Synthese · `[Daten erforderlich]` für Platzhalter, die echte Daten benötigen.

> **Tipp:** Fordere über companyFILES eine XLSX-, DOCX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Report zu erhalten.
