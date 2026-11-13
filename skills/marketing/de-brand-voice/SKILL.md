---
name: de-brand-voice
description: Prüft Inhalte gegen Brand-Voice- und Style-Richtlinien — markiert Abweichungen nach Schweregrad mit Vorher/Nachher-Verbesserungsvorschlägen. Verwende ihn, wenn du Marketing-Texte auditierst, eine:n neue:n Content-Ersteller:in einarbeitest oder eine Brand-Voice-Dokumentation aufbaust. Auslösen mit "prüfe das gegen unsere Brand Voice", "Markenkonsistenz checken", "diesen Text auditieren".
---

# Brand-Voice-Skill

Baue, auditiere und steuere Brand-Voice-Frameworks — Zerlegung der Stimme, Ton-Anpassung, Content-Scoring und Governance-Workflows. Alle Voice-Merkmale müssen aus der Markendokumentation des Kunden stammen oder gemeinsam mit dem Nutzer erarbeitet werden.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **CMS / Content-Tools über MCP** (z. B. Contentful, WordPress, Notion) | Bestehende Texte, veröffentlichte Inhalte je Kanal, Content-Inventar |
| **Analytics / Social-Tools über MCP** (z. B. GA4, LinkedIn, HubSpot) | Performance-Daten, hoch- und niedrigperformante Inhalte, Kanalkontext |
| **companyRAG-Sammlungen** (v. a. Brand- und Style-Guides) | Markenrichtlinien, Tonalitätsvorgaben, bestehende Voice-Frameworks |
| **Datei-Upload** | Style-Guides, einzelne Content-Stücke, Stakeholder-Notizen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Methodik zur Zerlegung der Stimme

Systematischer Prozess, um eine Brand Voice in messbare, bewertbare Komponenten zu zerlegen.

### Schritt 1: Kern-Voice-Merkmale identifizieren

Extrahiere 3–5 Kern-Voice-Merkmale aus den Markenrichtlinien oder aus Stakeholder-Input.

Regeln:

- Jedes Merkmal ist ein Spektrum, kein Binärwert (z. B. "formell <-> locker" mit Positionen 1–5)
- Merkmale müssen unabhängig sein -- die Anpassung eines Merkmals sollte logisch keine Anpassung eines anderen erzwingen
- Validierungstest: Verschiebt man ein Merkmal um 2 Punkte, sollte sich der Content spürbar anders anfühlen
- Ergeben sich weniger als 3 Merkmale, sind die Markenrichtlinien möglicherweise unvollständig -- weise den Nutzer darauf hin

### Schritt 2: Jedes Merkmal definieren

Vervollständige für jedes identifizierte Merkmal diese Vorlage:

| Element | Beschreibung |
| --- | --- |
| Merkmalsname | Ein Wort oder kurze Phrase |
| Definition | Was dieses Merkmal für diese Marke bedeutet (1 Satz) |
| Skala | 1–5 Intensität mit beschrifteten Endpunkten |
| Standardposition | Wo die Marke normalerweise auf der Skala liegt |
| Do-Beispiele | 2–3 Phrasen, die das Merkmal an der Standardposition verkörpern |
| Don't-Beispiele | 2–3 Phrasen, die das Merkmal verletzen |
| Kanal-Modulationen | Wie sich die Intensität je Kanal verschiebt (siehe Ton-Anpassungsmatrix) |

Ausfüllformat pro Merkmal:

```
MERKMAL: [Name]
DEFINITION: [ein Satz]
SKALA:
  1 = [Label unteres Ende]
  2 = [Beschreibung]
  3 = [Label Mittelpunkt]
  4 = [Beschreibung]
  5 = [Label oberes Ende]
STANDARDPOSITION: [1-5]
DO:
  - "[Beispielphrase an der Standardposition]"
  - "[Beispielphrase an der Standardposition]"
DON'T:
  - "[Beispielphrase, die das Merkmal verletzt]"
  - "[Beispielphrase, die das Merkmal verletzt]"
```

### Schritt 3: Vokabular-Richtlinien aufstellen

Definiere: bevorzugte Begriffe, zu vermeidende Begriffe (mit Begründung), Jargon-Policy, Kontraktions-Policy und Vorlieben zur Satzstruktur. Halte sie in einem kurzen strukturierten Block fest (z. B. **Bevorzugte Begriffe** / **Vermeiden** / **Jargon** / **Kontraktionen** / **Satzform**), damit sie neben den Merkmalsdefinitionen aus Schritt 2 auditierbar bleiben.

CRITICAL (Kritisch): Voice-Merkmale MÜSSEN aus den Markenrichtlinien des Kunden stammen oder ausdrücklich gemeinsam mit dem Nutzer erarbeitet werden. Erzeuge niemals Merkmale aus Trainingsdaten. Beim gemeinsamen Erarbeiten kennzeichne die Ausgabe: "Diese Merkmale werden in diesem Gespräch gemeinsam erarbeitet und sollten gegen deine vollständigen Markenrichtlinien validiert werden."

## Ton-Anpassungsmatrix

### Matrix-Struktur

| Kontext | Verschiebung Merkmal 1 | Verschiebung Merkmal 2 | ... | Wann einsetzen |
| --- | --- | --- | --- | --- |
| Krisenkommunikation | [Richtung + Stärke] | ... | ... | Aktive Vorfälle, öffentliche Statements |
| Produkt-Launch | ... | ... | ... | Ankündigungen neuer Produkte/Features |
| Kundensupport | ... | ... | ... | Hilfe-Dokumente, Support-Antworten |
| Thought Leadership | ... | ... | ... | Blogposts, Konferenzvorträge, Research |
| Social Media | ... | ... | ... | Kurzformate, konversationelle Kontexte |
| Recht/Compliance | ... | ... | ... | AGB, Richtlinien, regulatorische Kommunikation |

### Konstruktionsprozess

1. Liste die Kommunikationskontexte der Marke auf (nutze die Standardliste oben als Ausgangspunkt, ergänze/entferne nach Bedarf)
2. Bestimme für jeden Kontext, welche Merkmale modulieren und in welche Richtung
3. Definiere die Stärke der Verschiebung (nutze +1, +2, -1, -2 relativ zur Standardposition auf der 5-Punkte-Skala)
4. Validiere: Fühlt sich die modulierte Stimme noch wie dieselbe Marke an? Überschreitet eine Verschiebung +/-2, kann die Markenkohärenz brechen
5. Dokumentiere Ausnahmen -- Kontexte, in denen ein Merkmal bewusst ins Extrem geschoben wird (z. B. Rechtstexte bei maximaler Formalität)

### Verschiebungsnotation

```
KONTEXT: [Name]
MERKMALS-VERSCHIEBUNGEN:
  [Merkmal 1]: [Standard] -> [verschoben] ([+/-N], [Begründung])
  [Merkmal 2]: [Standard] -> [verschoben] ([+/-N], [Begründung])
  [Merkmal 3]: keine Verschiebung
WANN EINSETZEN: [konkrete Auslöser oder Content-Typen]
BEISPIEL: "[kurzer Beispielsatz, der die modulierte Stimme zeigt]"
```

### Matrix-Validierung

Validiere die Matrix nach der Konstruktion mit diesen Checks:

| Check | Frage | Falls Nein |
| --- | --- | --- |
| Kohärenz | Klingt jede Zeile noch nach der Marke? | Verschiebungsstärke reduzieren |
| Abdeckung | Sind alle wichtigen Kommunikationskontexte abgebildet? | Fehlende Zeilen ergänzen |
| Unterscheidbarkeit | Erzeugen unterschiedliche Kontexte tatsächlich unterschiedliche Modulationen? | Ähnliche Kontexte zusammenführen |
| Grenz-Sicherheit | Schieben Verschiebungen über die 1–5-Skala hinaus? | An den Endpunkten kappen |

## Content-Audit-Scoring

Systematischer Prozess zur Bewertung bestehender Inhalte gegen das Voice-Framework.

CRITICAL (Kritisch): ZITIERE immer den konkret bewerteten Text, bevor du eine Bewertung vergibst. Keine vagen Einschätzungen.

### Schritt 1: Content-Stichprobe auswählen

Wähle eine repräsentative Stichprobe, kein vollständiges Inventar:

- Alle aktiven Kanäle einbeziehen
- Sowohl aktuelle als auch ältere Inhalte einbeziehen
- Hoch- und niedrigperformante Stücke einbeziehen
- Minimum: 2–3 Stücke pro Kanal zur Mustererkennung

### Schritt 2: Bewertung pro Merkmal

Bewerte für jedes Content-Stück jedes Voice-Merkmal:

| Merkmal | Zielposition | Ist-Position (1–5) | Belege (Text zitieren) | Gap |
| --- | --- | --- | --- | --- |
| [Merkmalsname] | [aus Framework] | [bewertet] | "[zitierter Text]" | [Differenz] |

CRITICAL (Kritisch): ZITIERE immer den konkret bewerteten Text, bevor du eine Bewertung vergibst. Keine vagen Einschätzungen wie "der Content fühlt sich off-brand an" oder "der Ton passt nicht".

### Schritt 3: Bewertungen aggregieren

Drei Aggregationsebenen:

| Ebene | Berechnung | Zeigt |
| --- | --- | --- |
| Score pro Stück | Durchschnitt über die Merkmale (bei definierter Merkmals-Gewichtung gewichtet) | Qualität einzelner Inhalte |
| Gap-Analyse pro Merkmal | Durchschnittlicher Gap je Merkmal über alle Stücke | Welche Merkmale konsistent abweichen |
| Muster pro Kanal | Durchschnitts-Scores gruppiert nach Kanal | Ob Abweichungen mit Kanälen korrelieren |

### Schritt 4: Gap-Identifikation und Behebung

Prioritätsmatrix für Maßnahmen:

| Gap-Größe | Strategische Bedeutung | Maßnahme |
| --- | --- | --- |
| Groß (>2) | Hoch | Sofortiges Rewrite |
| Groß (>2) | Niedrig | Rewrite einplanen |
| Klein (<=1) | Hoch | Kleinere Anpassung |
| Klein (<=1) | Niedrig | Akzeptieren oder bündeln |

Zusätzliche Behebungs-Trigger:

- Dasselbe Merkmal in 3+ Stücken off-target -> systemisches Problem (Schulung, Prozess oder unklare Richtlinien)
- Derselbe Kanal konsistent off-target -> kanalspezifische Vorgaben in der Ton-Anpassungsmatrix nötig
- Vokabular-Verstöße -> Liste der bevorzugten/zu vermeidenden Begriffe aktualisieren oder Verbreitung verbessern

Nutze die obigen Scoring-Dimensionen, um für jedes Content-Stück ein detailliertes Bewertungs-Worksheet zu erstellen.

## Multi-Brand-Voice-Architektur

Methodik zur Steuerung von Voice-Frameworks über Markenhierarchien hinweg.

### Parent/Child-Modell

- Die Parent-Marke definiert die Kern-Merkmale und die nicht verhandelbaren Merkmalspositionen (Minimal- und Maximalgrenzen)
- Child-Marken erben die Kern-Merkmale, können aber:   - (a) 1–2 markenspezifische Merkmale für ihr Publikum ergänzen   - (b) Standardpositionen innerhalb definierter Grenzen verschieben   - (c) eigene Kanal-Modulationen innerhalb der Ton-Anpassungsmatrix definieren
- Governance-Regel: Der Content einer Child-Marke sollte auch ohne explizites Branding als Teil der Parent-Familie erkennbar sein

### Architektur-Entscheidungsbaum

| Szenario | Ansatz | Anzahl Voice-Frameworks |
| --- | --- | --- |
| Einzelmarke, mehrere Produkte | Ein Voice-Framework, produktspezifische Ton-Modulationen | 1 Framework + Produkt-Modulationszeilen |
| Brand House (Parent + benannte Sub-Brands) | Parent-Framework + Child-Variationsregeln | 1 Parent + N Child-Overlays |
| House of Brands (unabhängige Marken) | Separate Frameworks, gemeinsamer Governance-Prozess | N unabhängige Frameworks |
| Übergangsphase einer übernommenen Marke | Duales Framework mit Konvergenz-Roadmap | 2 Frameworks + Timeline |

### Dokumentation der Markenhierarchie

```
PARENT-MARKE: [Name]
KERN-MERKMALE (nicht verhandelbar):
  [Merkmal 1]: Grenzen [min]-[max] auf 5-Punkte-Skala
  [Merkmal 2]: Grenzen [min]-[max] auf 5-Punkte-Skala
GEMEINSAMES VOKABULAR: [Begriffe, die alle Child-Marken nutzen/vermeiden müssen]

CHILD-MARKE: [Name]
ERBT VON: [Parent-Name]
MERKMALS-OVERRIDES:
  [Merkmal 1]: Standard = [N] (innerhalb der Parent-Grenzen [min]-[max])
  [Zusätzliches Merkmal]: [Definition und Skala] (child-spezifisch)
PUBLIKUM: [wie sich das Publikum dieser Child-Marke vom Parent unterscheidet]
KANAL-FOKUS: [primäre Kanäle dieser Child-Marke]
```

### Konvergenz-Roadmap (übernommene Marken)

| Phase | Dauer | Maßnahme |
| --- | --- | --- |
| Assessment | Wochen 1–2 | Voice der übernommenen Marke gegen das Parent-Framework auditieren; Lücken identifizieren |
| Alignment | Wochen 3–8 | Nicht verhandelbare Merkmale angleichen; distinktive Merkmale der übernommenen Marke bewahren, wo sie Mehrwert bieten |
| Integration | Monate 3–6 | Migration auf das Parent-Framework mit genehmigten Child-Brand-Variationen |
| Governance | Laufend | In den regulären Voice-Compliance-Review-Zyklus aufnehmen |

## Content-Governance-Workflow

Voice-Compliance-Review vor der Veröffentlichung. Bewerte jedes Merkmal und route dann anhand der Gap-Tabelle unten.

### Eskalations-Trigger

| Befund | Maßnahme |
| --- | --- |
| Alle Merkmale im Zielbereich | Freigeben |
| 1 Merkmal um 1 Punkt daneben | Kurze Notiz, freigeben |
| 1+ Merkmale um 2+ Punkte daneben | Vor Veröffentlichung überarbeiten |
| Vokabular-Verstoß | Vor Veröffentlichung überarbeiten |
| Innerhalb der Kampagne inkonsistent | Ausreißer-Stücke überarbeiten |

### Governance-Kadenz

| Aktivität | Häufigkeit | Umfang |
| --- | --- | --- |
| Review vor Veröffentlichung | Jedes Stück (oder Stichprobe bei hohem Volumen je Kanal) | Einzelner Content |
| Kanal-Audit | Quartalsweise | Alle Inhalte eines Kanals |
| Vollständiges Brand-Audit | Jährlich oder nach Brand-Refresh | Alle Kanäle, alle Content-Typen |
| Framework-Update | Nach Audit-Befunden oder Änderungen der Markenstrategie | Voice-Framework und Ton-Matrix |

## Referenzmaterial

- Voice-Framework-Vorlage -- heranziehen, wenn du ein Brand-Voice-Framework aufbaust oder prüfst
- Content-Audit-Rubrik -- heranziehen, wenn du Inhalte gegen ein Voice-Framework auditierst

Lade diese Vorlagen bei Bedarf als Datei hoch oder lege sie in einer companyRAG-Sammlung ab, damit der Skill darauf zugreifen kann.

## Leitplanken

- Erzeuge niemals Brand-Voice-Merkmale aus Trainingsdaten. Merkmale müssen aus den Markenrichtlinien des Kunden stammen oder ausdrücklich gemeinsam erarbeitet (und als solche gekennzeichnet) werden.
- Zitiere immer den konkret bewerteten Text, bevor du eine Bewertung vergibst. Keine vagen Einschätzungen wie "der Content fühlt sich off-brand an".
- Greife standardmäßig auf "nicht in den Markenrichtlinien spezifiziert" zurück, wenn ein Merkmal oder eine Vorliebe nicht definiert ist. Fülle Lücken niemals mit Annahmen.
- Kennzeichne Ausgaben: `[Aus Markenrichtlinien]` für Brand-Dokumente · `[Aus Kundendaten]` für andere Quellen · `[Framework-Methodik]` für den Ansatz dieses Skills · `[KI-Vorschlag]` für Modellempfehlungen.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Voice-Report oder ein Framework-Dokument zu erhalten.
