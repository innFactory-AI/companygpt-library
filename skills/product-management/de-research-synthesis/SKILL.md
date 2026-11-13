---
name: de-research-synthesis
description: Wandelt rohe User-Research in strukturierte Insights um — Themen, Opportunity-Bereiche und priorisierte Empfehlungen. Verwende ihn, wenn du Interview-Notizen konsolidierst, Umfrageergebnisse auswertest oder Research-Readouts für das Team vorbereitest. Auslösen mit "synthetisiere diese Research", "was sind die Themen", "Research-Zusammenfassung für [Projekt]".
---

# Research-Synthese-Skill

Verwandle rohe qualitative und quantitative Research-Daten in handlungsleitende Produkt-Insights. Der Skill deckt thematische Analyse, Bewertung der Evidenzstärke, das Mapping von Insights auf Opportunities und die Strukturierung von Readouts ab. Alle Research-Daten müssen von dir, aus einer angebundenen Quelle oder aus companyRAG-Sammlungen kommen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **MCP-Server** (z. B. Notion, Confluence, Jira, ein angebundenes Research-Repository) | Research-Datenbanken, Studienseiten, Tickets mit User-Feedback |
| **companyRAG-Sammlungen** | Interview-Notizen, Transkripte, Umfrage-Exporte, Usability-Test-Protokolle |
| **Datei-Upload** | Einzelne Transkripte, CSV-Exporte von Umfragen, Readout-Entwürfe |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Research-Synthese-Workflow

Führe diese fünf Phasen der Reihe nach aus. Wer ohne sauberes Codieren (Phase 2) und Theming (Phase 3) direkt zu Empfehlungen (Phase 5) springt, erzeugt unzuverlässige Insights.

### Phase 1: Quelldaten inventarisieren & klassifizieren

Katalogisiere vor der Analyse, welche Daten verfügbar sind, und beurteile ihre Eigenschaften.

```
RESEARCH-INVENTAR
  Projekt:          [Name des Research-Projekts]
  Research-Frage:   [die Frage, die diese Research beantworten sollte]

  Datenquellen:
  | Quellentyp | Anzahl | Methode | Teilnehmende | Zeitraum |
  |---|---|---|---|---|
  | [z. B. User-Interviews] | [Anzahl] | [1:1 / Gruppe / unmoderiert] | [Segmentbeschreibung] | [Daten] |
  | [z. B. Umfrageantworten] | [Anzahl] | [offen / strukturiert / gemischt] | [Segmentbeschreibung] | [Daten] |

  Teilnehmer-Abdeckung:
  | Segment | Ziel | Tatsächlich | Lücke |
  |---|---|---|---|
  | [Segment] | [Ziel-n] | [tatsächliches n] | [über/unter/erreicht] |

  Bekannte Einschränkungen:
  - [z. B. nur Power-User interviewt — Perspektive neuer Nutzer fehlt]
  - [z. B. Umfrage mit 15 % Rücklaufquote — Self-Selection-Bias wahrscheinlich]
```

**Datensuffizienz-Check**: Beurteile vor dem Weitermachen, ob die Daten die Research-Frage glaubwürdig beantworten können. Wenn wichtige Teilnehmer-Segmente fehlen oder Stichproben sehr klein sind, markiere diese Einschränkung prominent — sie begrenzt jeden folgenden Befund.

### Phase 2: Die Daten codieren

Codieren verwandelt Rohdaten in strukturierte, analysierbare Einheiten. Dies ist die arbeitsintensivste Phase und die, die am ehesten übersprungen wird.

**Codier-Prozess**:

1. Beobachtungen extrahieren : Gehe jede Datenquelle durch und ziehe einzelne Beobachtungen heraus — konkrete Dinge, die Teilnehmende gesagt, getan oder erlebt haben. Eine Beobachtung pro Einheit.

```
BEOBACHTUNG:
  Teilnehmer: [ID — anonymisiert]
  Quelle:      [Interview / Umfrage / Usability-Test / Support-Ticket]
  Wortlaut:    [exaktes Zitat oder Beschreibung des beobachteten Verhaltens]
  Kontext:     [was dies ausgelöst hat — gestellte Frage, versuchte Aufgabe, Szenario]
```

1. Codes zuweisen : Versieh jede Beobachtung mit einem beschreibenden Code. Codes sind kurze Labels, die das Konzept erfassen.

**Codier-Disziplin**:

- Verwende wo möglich die Sprache der Teilnehmenden — vermeide es, dein eigenes Framework vorschnell aufzuzwingen
- Eine Beobachtung kann mehrere Codes haben (Verhalten bezieht sich oft auf mehrere Themen)
- Beginne mit offenem Codieren (bottom-up aus den Daten), bevor du vordefinierte Kategorien anwendest
- Wenn dasselbe Konzept bei verschiedenen Teilnehmenden unterschiedlich formuliert auftaucht, verwende einen konsistenten Code
- Erfasse die Code-Häufigkeit, setze Häufigkeit aber NICHT mit Wichtigkeit gleich — ein seltener, aber gravierender Pain Point kann wichtiger sein als ein häufiger, milder

1. Das Codebook aufbauen : Während sich Codes ansammeln, organisiere sie:

```
CODEBOOK
| Code | Definition | Beispiel-Beobachtung | Häufigkeit |
|---|---|---|---|
| [Code-Name] | [was dieser Code bedeutet] | [repräsentatives Zitat] | [n Teilnehmende] |
```

### Phase 3: Thematische Analyse

Themen sind Muster, die durch das Gruppieren verwandter Codes entstehen. Ein Thema ist KEINE Zusammenfassung einzelner Beobachtungen — es ist eine interpretierende Aussage darüber, was die Beobachtungen gemeinsam bedeuten.

**Prozess der Themenbildung**:

1. **Codes clustern**: Gruppiere verwandte Codes, die auf dasselbe zugrunde liegende Muster verweisen. Achte auf:   - Codes, die häufig gemeinsam auftreten (dieselben Teilnehmenden zeigen beide)   - Codes, die verschiedene Facetten derselben Erfahrung beschreiben   - Codes, die eine Kausalkette bilden (eines führt zum anderen)
2. **Das Thema benennen**: Ein guter Themenname ist eine interpretierende Aussage, kein Themen-Label.   - Themen-Label (schwach): "Onboarding"   - Interpretierendes Thema (stark): "Nutzer brechen das Onboarding ab, wenn sie es nicht mit ihrer unmittelbaren Aufgabe verbinden können"
3. **Themenstärke beurteilen**:

| Evidenzniveau | Kriterien | Konfidenz |
| --- | --- | --- |
| **Stark** | Thema von 5+ Teilnehmenden über mehrere Segmente gestützt; konsistentes Muster mit spezifischer, detaillierter Evidenz | Hoch — verlässliche Basis für Produktentscheidungen |
| **Moderat** | Thema von 3–4 Teilnehmenden gestützt oder auf ein Segment konzentriert; Muster klar, aber Abdeckung begrenzt | Mittel — handlungswert mit Bewusstsein für die Grenzen |
| **Aufkommend** | Thema von 1–2 Teilnehmenden gestützt; die Beobachtung ist auffällig, aber noch kein Muster | Niedrig — Hypothese für weitere Research, keine Entscheidungsbasis |

1. Jedes Thema dokumentieren :

```
THEMA: [Interpretierende Aussage]
  Stärke:        [Stark / Moderat / Aufkommend]
  Enthaltene Codes: [Liste der Codes, die dieses Thema bilden]
  Stützende Evidenz:
    - P[id]: "[wörtliches Zitat]" — [Kontext]
    - P[id]: "[wörtliches Zitat]" — [Kontext]
    - P[id]: "[beobachtetes Verhalten]" — [Kontext]
  Gegenevidenz: [Beobachtungen, die diesem Thema widersprechen]
  Betroffene Segmente: [welche Teilnehmer-Segmente dieses Muster zeigen]
  Beziehung zu anderen Themen: [interagiert dieses Thema mit anderen?]
```

**Rigorositäts-Checks**:

- Jedes Thema braucht direkte Evidenz (Zitate oder beobachtetes Verhalten) — keine Schlussfolgerungen
- Suche aktiv nach Gegenevidenz — Beobachtungen, die dem Thema widersprechen. Ein Thema ganz ohne Gegenevidenz wurde womöglich nicht kritisch genug geprüft.
- Wenn sich zwei Themen stark überschneiden, führe sie zusammen oder schärfe die Abgrenzung

### Phase 4: Insight-to-Opportunity-Mapping

Übersetze Themen in Produkt-Opportunities. Ein Insight beschreibt, was passiert und warum; eine Opportunity beschreibt, was man dagegen tun könnte.

**Mapping-Framework**:

```
INSIGHT → OPPORTUNITY

Insight:       [Was passiert und warum — abgeleitet aus einem Thema]
Evidenz:       [Themenstärke: Stark / Moderat / Aufkommend]
User-Impact:   [Wie dies den Nutzer betrifft — Schwere × Häufigkeit]
Opportunity:   [Was könnte das Produktteam dagegen tun?]
Opportunity-Typ:
  - Pain Relief:     Eine Reibungsquelle beseitigen oder reduzieren
  - Unmet Need:      Eine Fähigkeit liefern, die Nutzern heute fehlt
  - Delight:         Erwartungen auf unerwartete Weise übertreffen
  - Efficiency Gain: Einen bestehenden Workflow spürbar schneller machen
Konfidenz:     [Wie sicher sind wir, dass diese Opportunity real ist? Basierend auf Evidenzstärke + User-Impact-Bewertung]
```

**Priorisierung von Opportunities** (kein Ersatz für RICE — ein research-informierter Input dafür):

| Faktor | Bewertung |
| --- | --- |
| **Evidenzstärke** | Starke Themen erzeugen Opportunities mit höherer Konfidenz |
| **User-Impact** | Schwere (wie schmerzhaft?) × Breite (wie viele Nutzer betroffen?) |
| **Strategisches Alignment** | Verbindet sich diese Opportunity mit aktuellen OKRs oder der Produktstrategie? |
| **Feasibility-Signal** | Haben Nutzer Workarounds vorgeschlagen oder beschrieben, die auf Lösungsansätze hindeuten? |

Ordne Opportunities so: starke Evidenz + hoher Impact zuerst, dann moderate Evidenz + hoher Impact, dann starke Evidenz + moderater Impact. Opportunities mit aufkommender Evidenz gehen in "weitere Research nötig", nicht ins Produkt-Backlog.

### Phase 5: Research-Readout

Strukturiere die Synthese für die Nutzung durch das Team. Verschiedene Zielgruppen brauchen verschiedene Formate.

#### Vollständiges Research-Readout

Für das Produktteam, das Design-Team und Research-Stakeholder:

```
# Research-Synthese — [Projektname]
Datum: [Datum]    |    Researcher: [Name]

## 1. Research-Frage & Methode
[Was wir herausfinden wollten, wie wir untersucht haben, wer teilgenommen hat]

## 2. Teilnehmer-Überblick
[Vertretene Segmente, Stichprobengrößen, bekannte Lücken]

## 3. Wichtige Themen
[Nach Evidenzstärke geordnet — stärkstes zuerst]
  Thema 1: [interpretierende Aussage] — [Stark/Moderat/Aufkommend]
    [Zusammenfassung der stützenden Evidenz mit repräsentativen Zitaten]
  Thema 2: ...

## 4. Opportunities
[Aus Themen abgeleitet, nach Konfidenz × Impact geordnet]
  Opportunity 1: [Beschreibung] — Evidenz: [Stärke] — Impact: [Bewertung]
  Opportunity 2: ...

## 5. Empfehlungen
[Konkrete Produkt-Maßnahmen, je mit Evidenzbasis und Konfidenzniveau]

## 6. Einschränkungen & Vorbehalte
[Was diese Research nicht sagen kann — Stichprobenlücken, methodische Grenzen]

## 7. Weitere Research nötig
[Aufgeworfene, aber unbeantwortete Fragen — mit vorgeschlagenen Methoden]
```

#### Executive Summary

Für Stakeholder, die die Headline brauchen, nicht die Methodik:

```
RESEARCH-ZUSAMMENFASSUNG — [Projektname] — [Datum]

Kernbefund:     [Headline in einem Satz — der einzelne wichtigste Insight]
Evidenzbasis:   [n Teilnehmende, verwendete Methoden, abgedeckte Segmente]

Top-3-Insights:
1. [Insight] — [stützender Datenpunkt] — Konfidenz: [H/M/N]
2. [Insight] — [stützender Datenpunkt] — Konfidenz: [H/M/N]
3. [Insight] — [stützender Datenpunkt] — Konfidenz: [H/M/N]

Empfohlene Maßnahmen:
1. [Maßnahme] — Verantwortlich: [Name] — Priorität: [Hoch/Mittel/Niedrig]
2. [Maßnahme] — Verantwortlich: [Name] — Priorität: [Hoch/Mittel/Niedrig]

Einschränkungen: [zentrale Vorbehalte in einem Satz]
```

## Qualitative und quantitative Daten kombinieren

Wenn beide Datentypen vorliegen (z. B. Interview-Themen + Umfrage-Prozentwerte + Analytics-Daten):

1. Quantitativ zuerst für das "Was" : Nutze Metriken und Umfragedaten, um zu erkennen, WAS passiert — welche Features wenig genutzt werden, wo Nutzer abspringen, wie Zufriedenheitswerte aussehen
2. Qualitativ für das "Warum" : Nutze Interview- und Beobachtungsdaten, um zu erklären, WARUM die quantitativen Muster bestehen
3. Triangulation : Wenn Qual und Quant in dieselbe Richtung zeigen, steigt die Konfidenz. Wenn sie auseinandergehen, untersuche dies — die Divergenz selbst ist ein Insight.
4. Nutze Qual niemals, um Quant zu "validieren" (oder umgekehrt) — sie beantworten verschiedene Fragen. Qual erklärt Motivationen und Kontext; Quant misst Umfang und Häufigkeit.

## Leitplanken

- Erfinde NIEMALS Teilnehmer-Zitate, Beobachtungen oder Research-Daten. Jede Beobachtung, jeder Code und jedes Thema muss auf vom Nutzer bereitgestelltes Quellmaterial zurückführbar sein.
- Behaupte NIEMALS, Research-Befunde seien "statistisch signifikant", ohne quantitative Analyse. Qualitative Research erzeugt thematische Muster mit Evidenzstärke-Niveaus, keine statistische Signifikanz.
- Gegenevidenz ist Pflicht. Wenn du ein Thema präsentierst, benenne aktiv widersprechende Beobachtungen. Gegenevidenz wegzulassen ist eine Form von Fabrikation.
- Versieh jedes Element mit einer Quellenkennzeichnung: `[Aus Research-Daten]`, `[Synthese-Framework]` oder `[KI-Interpretation — mit Researcher verifizieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Readout zu erhalten.
