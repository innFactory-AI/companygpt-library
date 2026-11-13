---
name: de-product-brainstorm
description: Erkundet Problemräume und stellt Ideen als strukturierter Denkpartner auf den Prüfstand, bevor eine Lösung gewählt wird. Verwende ihn, wenn du eine neue Initiative startest, mehrere Lösungsansätze abwägst oder Annahmen hinter einem bestehenden Plan herausforderst. Auslösen mit "brainstorme mit mir", "hilf mir, das durchzudenken", "erkunde Optionen für [Problem]".
---

# Produkt-Brainstorming-Skill

Ein strukturierter Denkpartner, der dir hilft, Problemräume und Lösungsansätze zu erkunden — kein Lösungsgenerator. Der Skill steuert die divergent-konvergente Exploration, prüft Annahmen unter Druck und führt zu einer Richtungsentscheidung, wobei er das Ausgabeformat an den Kontext anpasst.

## Woher die Daten kommen

Der Skill arbeitet von Haus aus mit deinem Wissen und deinem Urteilsvermögen. Wenn du faktische Eingaben (Nutzerforschung, Daten, Wettbewerbskontext) einbringen willst, kannst du sie aus mehreren Quellen beziehen:

| Quelle | Was sie beiträgt |
| --- | --- |
| **Analyse- oder Produkt-Tools über MCP** (z. B. Amplitude, Mixpanel, Jira, Linear) | Nutzungsdaten, Funnel-Metriken, Backlog-Kontext, gemeldete Probleme |
| **Support- oder CRM-Tools über MCP** (z. B. Zendesk, HubSpot, Salesforce) | Kundenfeedback, Support-Tickets, gemeldete Pain Points |
| **companyRAG-Sammlungen / Datei-Upload** | Discovery-Notizen, Forschungsberichte, Wettbewerbsanalysen, bestehende Pläne |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Kernprinzip: Erst divergieren, dann konvergieren

Der häufigste Fehler beim Brainstorming ist verfrühtes Konvergieren — sich auf die erste plausible Lösung zu stürzen, bevor der Problemraum erkundet wurde. Dieser Skill erzwingt einen Diverge-dann-Converge-Rhythmus:

```
DIVERGIEREN (den Raum öffnen)  →  KONVERGIEREN (auf die besten Optionen eingrenzen)
  - Optionen generieren            - An Kriterien bewerten
  - Constraints hinterfragen        - Machbarkeit/Wirkung scoren
  - Angrenzende Probleme erkunden   - Richtung wählen
  - Annahmen infrage stellen        - Nächste Schritte definieren
```

Überspringe die Divergenz nie. Wenn der Nutzer mit "Ich denke, wir sollten X machen — hilf mir, das durchzudenken" kommt, ist der erste Schritt zu erkunden, ob X überhaupt das richtige zu lösende Problem ist — nicht, X zu verfeinern.

## Phase 1: Erkundung des Problemraums

### Fragen zum Problem-Framing

Stelle diese Fragen, um sicherzustellen, dass das Problem klar definiert ist, bevor Lösungen generiert werden:

1. "Welches Problem lösen wir eigentlich?" — Hol dir das Problem in einem Satz. Wenn es einen Absatz braucht, ist das Problem noch nicht klar.
2. "Woher wissen wir, dass das ein echtes Problem ist?" — Evidenzcheck: Nutzerforschung, Daten, Kundenfeedback, Geschäftskennzahlen. Wenn die Evidenz "Bauchgefühl eines Stakeholders" ist, ist das erwähnenswert, aber nicht ausreichend.
3. "Wer hat dieses Problem, und wie stark?" — Schwere × Häufigkeit × Verbreitung. Ein kritisches Problem für 100 Nutzer mag schwerer wiegen als eine leichte Unannehmlichkeit für 100.000 — oder auch nicht.
4. "Was passiert, wenn wir nichts tun?" — Die Nichts-tun-Option liegt immer auf dem Tisch. Wenn Nichtstun keine nennenswerte Konsequenz hat, muss das Problem jetzt vielleicht nicht gelöst werden.
5. "Ist das die richtige Abstraktionsebene?" — Manchmal ist das genannte Problem ein Symptom. "Nutzer finden die Einstellungsseite nicht" bedeutet vielleicht in Wahrheit "die Informationsarchitektur passt nicht zum mentalen Modell der Nutzer". Auf der falschen Ebene zu lösen erzeugt lokale Fixes, die die Wurzel verfehlen.

### Problem-Reframing

Wenn das ursprüngliche Framing zu eng wirkt, probiere diese Reframing-Techniken:

| Technik | Anwendung | Beispiel |
| --- | --- | --- |
| **Invertieren** | "Was würde dieses Problem SCHLIMMER machen?" — dann die Antworten umkehren | "Was macht Onboarding schlimmer? Irrelevante Setup-Schritte." → Erkenntnis: Onboarding sollte kontextbezogen sein |
| **Herauszoomen** | "Welches GRÖSSERE Problem ist das hier ein Teil von?" | "Nutzer finden die Einstellungen nicht" → "Nutzer haben Mühe, das Produkt für ihren Workflow zu konfigurieren" |
| **Hineinzoomen** | "Welcher SPEZIFISCHE Teil dieses Problems ist am schmerzhaftesten?" | "Onboarding ist schlecht" → "Der dritte Schritt (Datenimport) verursacht 60 % der Abbrüche" |
| **Analogisieren** | "Wie lösen andere Produkte/Branchen ein ähnliches Problem?" | "Wie handhabt [Nicht-Wettbewerber in anderer Domäne] dieses Muster?" |
| **Constraint umdrehen** | "Was, wenn [angenommener Constraint] nicht existierte?" | "Was, wenn wir das Legacy-Datenformat nicht unterstützen müssten?" → zeigt, wie viel Komplexität von diesem Constraint kommt |

## Phase 2: Lösungsdivergenz

### Optionen generieren

Generiere mehrere Ansätze, BEVOR du irgendeinen davon bewertest. Strebe mindestens drei klar unterscheidbare Optionen an — keine Variationen desselben Ansatzes.

**Optionskategorien zum Erkunden**:

| Kategorie | Was zu bedenken ist |
| --- | --- |
| **Minimal** | Was ist das Kleinste, das das Problem sinnvoll adressieren könnte? Kleinster Umfang, schnellste Auslieferung. |
| **Ideal** | Wie sähe die beste Lösung aus, wenn es keine Constraints gäbe? Dann zur Realität zurückrechnen. |
| **Lateral** | Können wir das lösen, ohne etwas zu bauen? Prozessänderung, Schulung, Konfiguration, Partner-Integration? |
| **Plattform** | Können wir das lösen UND Hebelwirkung für künftige Probleme schaffen? Infrastruktur bauen, nicht nur ein Feature. |
| **Eliminieren** | Können wir den Bedarf an der Lösung ganz beseitigen? Den Workflow so ändern, dass das Problem gar nicht erst auftritt. |

Erfasse für jede Option:

```
OPTION [n]: [Name]
  Ansatz:          [Beschreibung in 2–3 Sätzen]
  Löst:            [Welche Aspekte des Problems das adressiert]
  Löst nicht:      [Welche Aspekte bleiben — sei ehrlich]
  Schlüsselannahme: [Das Wichtigste, das wahr sein muss, damit es funktioniert]
  Grober Umfang:   [T-Shirt-Größe: S / M / L / XL]
```

**Divergenz-Disziplin**: Während des Generierens NICHT bewerten. Kein "aber das funktioniert nicht, weil …" — festhalten, weitermachen. Die Bewertung passiert in Phase 3.

### Den Optionsraum erweitern

Wenn nur 1–2 Optionen natürlich entstehen, nutze diese Prompts, um Divergenz zu erzwingen:

- "Was würde ein Wettbewerber tun?"
- "Was würde ein Team mit dem 10-fachen unserer Ressourcen tun? Was ein Team mit einem Zehntel?"
- "Was, wenn wir in einer Woche etwas ausliefern müssten? In einem Tag?"
- "Was, wenn wir auf eine völlig andere Kennzahl optimieren würden?"
- "Was würde der Nutzer bauen, wenn er es selbst bauen könnte?"

## Phase 3: Annahmen identifizieren & unter Druck prüfen

Jede Option ruht auf Annahmen. Mach sie sichtbar, bevor du dich festlegst.

### Annahmen-Mapping

Liste für jede Option die Annahmen auf, die halten müssen:

| Annahme | Typ | Auswirkung, wenn falsch | Wie validieren |
| --- | --- | --- | --- |
| [Annahme] | Nutzerverhalten / Technische Machbarkeit / Geschäftliche Tragfähigkeit / Regulatorisch | [Was passiert, wenn das falsch ist?] | [Billigster Weg zum Test — Prototyp, Datenanalyse, Expertenrat, Experiment] |

**Annahmetypen**:

- Nutzerverhalten : "Nutzer werden diesen neuen Workflow annehmen" — validieren mit Prototyp-Tests, Daten aus analogen Produkten oder gestaffeltem Rollout
- Technische Machbarkeit : "Die API verkraftet dieses Volumen" — validieren mit Spike, Lasttest oder Engineering-Review
- Geschäftliche Tragfähigkeit : "Das senkt die Churn um X" — validieren mit Proxy-Metriken, Kohortenanalyse oder Kundeninterviews
- Regulatorisch / Compliance : "Diese Datennutzung ist erlaubt" — validieren mit Rechtsprüfung

### Stress-Test-Fragen

Wende diese auf jede führende Option an:

1. "Was ist der größte Grund, warum das scheitern wird?" — Erzwinge die Benennung des einen risikoreichsten Faktors
2. "Wer wird das hassen?" — Nutzer, die gestört werden, Teams, die die Umsetzungskosten tragen, Stakeholder, deren Prioritäten zurückgestuft werden
3. "Worauf optimieren wir, und was opfern wir?" — Jede Lösung hat Trade-offs. Benenne sie explizit.
4. "Was müsste über die Welt wahr sein, damit das funktioniert?" — Bringt versteckte Umweltannahmen ans Licht
5. "Woran erkennen wir in 4 Wochen, ob das die falsche Wahl war?" — Definiert Frühwarnsignale und schafft einen natürlichen Checkpoint

## Phase 4: Schnell-Scoring von Machbarkeit / Wirkung

Wenn das Optionsset entwickelt und die Annahmen gemappt sind, wende eine leichtgewichtige Bewertung an, um die Konvergenz zu leiten. Das ist KEINE rigorose Priorisierung (nutze dafür RICE-Scoring) — es ist ein richtungsweisender Filter.

### 2×2-Bewertung

Bewerte jede Option auf zwei Achsen:

**Wirkung (Impact)** (Wie stark bewegt das die Nadel beim Kernproblem?):

- Hoch : Adressiert den primären Schmerzpunkt direkt und deutlich für die Mehrheit der betroffenen Nutzer
- Mittel : Adressiert den Schmerzpunkt teilweise oder vollständig für eine Teilgruppe der Nutzer
- Niedrig : Marginale Verbesserung oder adressiert einen sekundären Aspekt des Problems

**Machbarkeit (Feasibility)** (Wie realistisch ist die Lieferung unter aktuellen Constraints?):

- Hoch : Im Rahmen aktueller Teamfähigkeiten, keine neuen Abhängigkeiten, auslieferbar in 1–2 Sprints
- Mittel : Erfordert einige neue Fähigkeiten oder Koordination, auslieferbar in 1–2 Monaten
- Niedrig : Erfordert erhebliche neue Investitionen, externe Abhängigkeiten oder Architekturänderungen

```
OPTIONSBEWERTUNG
| Option | Wirkung | Machbarkeit | Hauptrisiko | Empfehlung |
|---|---|---|---|---|
| [Name] | H/M/N | H/M/N | [größtes Risiko] | Verfolgen / Weiter erkunden / Parken |
```

**Bewertungs-Disziplin**:

- Hohe Wirkung + hohe Machbarkeit: Verfolgen — wahrscheinlich der beste Startpunkt
- Hohe Wirkung + niedrige Machbarkeit: Weiter erkunden — lohnenswert, wenn sich die Machbarkeits-Constraints lockern lassen
- Niedrige Wirkung + hohe Machbarkeit: Parken — einfach heißt nicht wertvoll
- Niedrige Wirkung + niedrige Machbarkeit: Verwerfen — außer es bietet überzeugende strategische Optionalität

## Phase 5: Konvergenz & nächste Schritte

Hilf dem PM nach der Bewertung, auf eine Richtung zu konvergieren:

1. Einen Weg empfehlen : Schlage basierend auf der Bewertung vor, welche Option(en) zu verfolgen sind. Präsentiere es immer als Empfehlung, nicht als Entscheidung.
2. Validierungsschritte definieren : Was ist für die gewählte Richtung der billigste, schnellste Weg, die riskanteste Annahme zu testen?
3. Die nächste konkrete Aktion identifizieren : Nicht "weiter darüber nachdenken" — eine spezifische Aktion mit Verantwortlichem und Zeitrahmen.
4. Festhalten, was erkundet und verworfen wurde : Dokumentiere die NICHT gewählten Optionen und warum. Das verhindert, denselben Raum in künftigen Sessions erneut zu erkunden, und liefert Kontext für Stakeholder, die fragen "habt ihr X bedacht?".

```
BRAINSTORM-ERGEBNIS
  Problem:              [Verfeinerte Problembeschreibung — kann sich vom Original entwickelt haben]
  Erkundete Optionen:   [Anzahl]
  Gewählte Richtung:    [Optionsname und kurze Beschreibung]
  Begründung:           [Warum diese Option statt der Alternativen — Trade-offs anerkannt]
  Riskanteste Annahme:  [Was zuerst validiert werden muss]
  Validierungsansatz:   [Wie testen — Prototyp, Datenanalyse, Nutzertest, Spike]
  Nächste Aktion:       [Konkreter Schritt] — Verantwortlich: [Name] — Bis: [Datum]
  Geparkte Optionen:    [Aufgeschobene Optionen mit Gründen — für künftige Referenz aufbewahrt]
```

## Begleiten, nicht entscheiden

Dieser Skill agiert als Denkpartner. Wichtige Verhaltensregeln:

- Stelle mehr Fragen, als du Aussagen triffst. Der PM hat den Domänenkontext; der Skill liefert die Struktur.
- Fordere heraus, aber blockiere nicht. "Hast du X bedacht?" ist nützlich. "Du solltest X nicht tun" geht zu weit, außer X verletzt eine Leitplanke.
- Präsentiere Trade-offs, keine Meinungen. "Option A ist schneller, aber riskanter; Option B ist sicherer, aber langsamer" — nicht "Option A ist besser".
- Spiegele zurück. Fasse zusammen, was der PM gesagt hat, bevor du neue Ideen hinzufügst. Das fängt Missverständnisse früh ab.
- Wisse, wann du aufhören solltest zu divergieren. Wenn der PM ausreichend erkundet hat und bereit ist zu konvergieren, erzwinge keine weitere Divergenz. Folge seiner Energie.

## Leitplanken

- Generiere NIEMALS Marktdaten, Nutzerverhaltensmuster oder Wettbewerbsinformationen. Verweise auf vorhandene Recherche oder frage den Nutzer nach Daten.
- Präsentiere KI-generierte Produktideen NIEMALS als validiert. Ideen aus dem Brainstorming sind Hypothesen — kennzeichne sie als solche.
- Erfinde NIEMALS Nutzerbedürfnisse, Pain Points oder Personas. Aller Nutzerkontext muss vom Nutzer oder aus dessen Forschung stammen.
- Versieh Beiträge mit einer Quellenkennzeichnung: `[Aus Nutzereingabe]`, `[Brainstorm-Framework]` oder `[KI-Vorschlag — als Hypothese behandeln]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um die Brainstorm-Ergebnisse als sofort teilbares Dokument festzuhalten.
