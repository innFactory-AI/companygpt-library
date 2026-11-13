---
name: de-performance-review
description: Unterstützt Führungskräfte beim Entwerfen fairer, konkreter Leistungsbeurteilungen mit Kalibrierungshilfe und Zielsetzungs-Leitlinien. Verwende ihn, wenn du Jahres- oder Halbjahresbeurteilungen schreibst, eine Kalibrierungssitzung vorbereitest oder eine Führungskraft beim Feedback coachst. Auslösen mit "Leistungsbeurteilung schreiben für", "hilf mir mit dieser Beurteilung", "Kalibrierungsvorbereitung".
---

# Leistungsbeurteilung-Skill

Gestalte Leistungsmanagement-Systeme, moderiere Kalibrierungssitzungen, führe Talentbewertungen durch und baue Zielsetzungs-Frameworks. Organisationsspezifische Daten (Ratings, Mitarbeiterakten, Ziel-Frameworks, Kompetenzdefinitionen) kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **HRIS über MCP** (z. B. Workday, BambooHR, Personio) | Mitarbeiterakten, Job-Level, Vergütungsdaten, historische Ratings |
| **OKR-/Ziel-Tools über MCP** | Zielsetzungen, Key Results, Zielerreichung, KPI-Verlauf |
| **companyRAG / Datei-Upload** | Kompetenz-Frameworks, Job-Architektur, Kalibrierungsrichtlinien, frühere Beurteilungen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## EU-KI-Verordnung & DSGVO — Grenzen der Compliance

KI-gestützte Leistungsüberwachung und Workforce-Management gilt als **Hochrisiko nach der EU-KI-Verordnung (Anhang III, Kategorie 4 — Beschäftigung und Personalmanagement)**. Nach Art. 22 DSGVO haben Personen das Recht, nicht ausschließlich automatisierten Entscheidungen unterworfen zu werden, die rechtliche oder ähnlich erhebliche Wirkungen entfalten. Alle Ergebnisse sind Entscheidungshilfen für menschliche Fachkräfte — Leistungsratings, Talentklassifizierungen und Entwicklungsentscheidungen müssen von qualifizierten Menschen getroffen werden.

## Auswahl des Leistungsmanagement-Modells

Leistungsmanagement ist eine DESIGN-ENTSCHEIDUNG, kein Fortschritt von "traditionell" zu "modern". Jedes Modell hat berechtigte Anwendungsfälle, und die richtige Wahl hängt vom organisationalen Kontext ab, nicht von Trends. Stelle alle Modelle als Optionen mit Trade-offs dar.

### Modelloptionen

| Modell | Kernansatz | Beste Eignung | Wichtige Design-Überlegung |
| --- | --- | --- | --- |
| **Zyklusbasiert** | Zielsetzung → Check-in → Beurteilung → Kalibrierung | Strukturierte Vergütungszyklen; regulierte Branchen | Recency-Bias-Risiko bei Jahresbeurteilungen; administrativer Aufwand |
| **Kontinuierliches Feedback** | Laufendes 1:1-Coaching, Echtzeit-Anerkennung, regelmäßige Check-ins | Schnelllebige Organisationen; Rollen mit rasch wechselnden Prioritäten | Schwerer für Vergütung zu aggregieren; erfordert hohe Führungskompetenz; Kalibrierung ohne diskrete Datenpunkte komplexer |
| **OKR-basiert** | Quartalsweise Objectives mit messbaren Key Results | Produkt- und Technologieorganisationen mit klarer strategischer Kadenz | OKR-Scores von der Vergütung trennen, um Sandbagging zu verhindern; nicht alle Rollen eignen sich für Quartalsziele |
| **Hybrid** | Kombination von Elementen (z. B. kontinuierliche 1:1s + Jahreskalibrierung) | Organisationen im Modellwechsel oder mit diversen Rollentypen | Höhere Design-Komplexität; Risiko des "Schlechtesten aus beiden Welten" ohne bewusste Gestaltung |

### Auswahlkriterien

Bewerte bei der Modellwahl einer Organisation:

| Faktor | Spricht für Zyklusbasiert | Spricht für Kontinuierlich | Spricht für OKR-basiert |
| --- | --- | --- | --- |
| Vergütungskopplung | Stark — braucht diskrete Datenpunkte | Schwach — schwerer zu aggregieren | Mittel — Quartalsdaten verfügbar |
| Führungskompetenz | Niedrigere Hürde — strukturierter Prozess leitet Führungskräfte | Höhere Hürde — erfordert Coaching-Fähigkeit | Mittel — Zielsetzung ist erlernbar |
| Betriebsrats-Anforderungen | Natürliche Passung — formale Prozessdokumentation | Kompatibel — erfordert strukturierte Dokumentation laufenden Feedbacks für formale Mitbestimmung | Abhängig von der Jurisdiktion |
| Veränderungsrate | Langsamer — Jahresziele bleiben stabil | Schneller — Prioritäten verschieben sich häufig | Mittel — quartalsweise Anpassung |
| Organisationsgröße | Größer — braucht Konsistenz im Maßstab | Kleiner — beziehungsgetrieben | Mittel — strategisches Alignment zählt |

> [Methodik-Framework] Dieses Auswahl-Framework ist ein Design-Werkzeug, keine Empfehlung. Kein Modell ist von Natur aus überlegen. Die Organisation muss anhand ihres spezifischen Kontexts, ihrer Kultur und ihrer Rahmenbedingungen wählen.

## Zielsetzungs-Methodik

Zielsetzungs-Frameworks sind Komponenten des Leistungsmanagements, keine Systeme an sich. Die Methodik zur Gestaltung der Zielsetzung variiert je nach gewähltem Leistungsmodell.

### Optionen für Ziel-Frameworks

Jedes Ziel-Framework hat eine kritische Design-Überlegung für das Leistungsmanagement:

- OKR : OKR-Erreichungsscores von Leistungsratings trennen, um Sandbagging zu verhindern (konservative Ziele setzen, um hohe Scores zu erreichen)
- KPI-basiert : Zwischen Frühindikatoren (Aktivitäten) und Spätindikatoren (Ergebnissen) unterscheiden — Rollen sollten an Indikatoren gemessen werden, die sie beeinflussen können
- Kompetenzbasiert : Kompetenzbewertung erfordert verhaltensbasierte Evidenz, keine Selbstauskunft — verknüpfe mit der Verhaltensanker-Methodik aus dem strukturierten Recruiting

### Zielqualität und Kaskadierung

Wende Standard-Zielqualitätskriterien an (SMART oder gleichwertig), damit jedes Ziel spezifisch, messbar und terminiert ist. Die folgende Methodik behandelt die nicht offensichtlichen Design-Entscheidungen:

Wenn Ziele unterschiedliche Gewichte in der Leistungsbewertung tragen:

1. Gewichte zum Zeitpunkt der Zielsetzung kommunizieren, nicht zum Bewertungszeitpunkt
2. Sicherstellen, dass die Gewichte sich auf 100 % summieren und dokumentiert sind
3. Kaskadierung: Organisationsziele → Funktionsziele → Teamziele → Individualziele. Jede Ebene sollte sehen können, wie ihre Ziele nach oben anknüpfen.
4. Kaskadierungs-Artefakte vermeiden: Das CEO-Ziel "20 % Umsatzwachstum" sollte nicht zum persönlichen Ziel jedes Einzelnen werden — übersetze es in den Beitragsbereich der jeweiligen Person

## Methodik der Kalibrierungssitzung

Die Kalibrierungs-Methodik ist hier detailliert ausgeführt, weil strukturiertes Moderationstraining in den meisten Organisationen unüblich ist. Die meisten Führungskräfte wurden nie in strukturierter Kalibrierungs-Moderation geschult.

### Zweck der Kalibrierung

Kalibrierung sichert Rating-Konsistenz über Führungskräfte und Teams hinweg. Ohne sie schafft Milde-/Strenge-Variation zwischen Führungskräften inäquitable Vergütungs- und Beförderungsergebnisse und verhindert einen sinnvollen teamübergreifenden Vergleich.

### Vorbereitung vor der Sitzung

1. Datenaufbereitung : Ratings nach Führungskraft, Team, Funktion und Job-Level aggregieren. Verteilungsdiagramme erstellen, die die Rating-Streuung je Gruppe zeigen.
2. Ausreißer-Identifikation : Ratings markieren, die deutlich von der Gruppenverteilung abweichen, zur Diskussion (nicht zur automatischen Korrektur)
3. Teamübergreifender Vergleich : Verteilungen über Teams auf gleichem Job-Level vergleichen — deutliche Unterschiede deuten auf mögliche Kalibrierungsprobleme hin
4. Vorarbeit der Führungskräfte : Jede Führungskraft bereitet eine evidenzbasierte Begründung für jedes Rating über oder unter der mittleren Kategorie vor, mit Bezug auf konkrete Leistungen, Verhaltensweisen und Zielergebnisse

### Moderation der Sitzung

Die moderierende Person (typischerweise HR Business Partner oder Talentmanagement-Spezialist) besitzt den Prozess; die Führungskräfte besitzen den Inhalt.

1. Grundregeln : Ratings basieren auf Evidenz gegen die Erwartungen des Job-Levels, nicht auf Vergleich mit Peers, persönlicher Beziehung oder Betriebszugehörigkeit
2. Job-Level-Verankerung : Beginne jeden Diskussionsabschnitt damit, neu zu benennen, was das relevante Job-Level erwartet (aus der Job-Architektur)
3. Review-Reihenfolge : Mit Ausreißer-Ratings (höchste und niedrigste) beginnen, dann die mittlere Verteilung durchgehen
4. Evidenz-Standard : Für jedes diskutierte Rating präsentiert die Führungskraft konkrete verhaltensbasierte Evidenz. "Sie ist eine starke Leistungsträgerin" ist keine Evidenz. "Sie lieferte [ konkretes Ergebnis ] gegen [ konkretes Ziel ], während sie [ konkrete Herausforderung ] meisterte" ist Evidenz.
5. Challenge-Protokoll : Andere Führungskräfte und die moderierende Person dürfen Verständnisfragen stellen. Einwände müssen evidenzbasiert sein: "In meinem Team wäre dieses Ergebnis auf IC3 ein Meets, kein Exceeds — und zwar deshalb..."
6. Anpassungs-Tracking : Alle Rating-Änderungen mit Begründung dokumentieren. Änderungen müssen evidenz-, nicht druckgetrieben sein.
7. Bias-Checks : In jedem Abschnitt explizit auf gängige Verzerrungen prüfen (siehe Abschnitt Bias-Minderung unten)
8. Zeitmanagement : Diskussionszeit proportional zur Teamgröße und Rating-Divergenz zuweisen, nicht gleichmäßig je Führungskraft

Für Agenden, den Umgang mit Meinungsverschiedenheiten, die Nachbereitungsdokumentation und Führungskräfte-Kommunikation erweitere die obigen Moderationsschritte mit den HR-Vorlagen und Zeitplänen deiner Organisation.

### Kalibrierungs-Modelle

Organisationen können anhand von Ratings, Narrativen oder einer Kombination kalibrieren:

**Rating-basierte Kalibrierung**: Richtet numerische oder kategoriale Ratings über Führungskräfte hinweg aus. Am stärksten strukturiert. Erfordert eine Rating-Skala (siehe unten).

**Narrativ-basierte Kalibrierung**: Führungskräfte präsentieren schriftliche Leistungszusammenfassungen und diskutieren, ob die beschriebene Leistung zur beabsichtigten Rating-Kategorie passt. Nuancierter, aber im Maßstab schwerer zu moderieren.

**Hybrid**: Rating, verankert durch narrative Evidenz. Das Rating liefert die Struktur; das Narrativ liefert die Substanz.

## Ansätze der Talentbewertung

Talentbewertung ist ein Menü von Ansätzen, kein einzelnes Werkzeug. Jeder hat berechtigte Anwendungsfälle.

**9-Box-Grid** (Leistung × Potenzial)

- Wann es funktioniert: große Organisationen, die einen visuellen Überblick brauchen, Nachfolgeplanungs-Gespräche, Organisationen, die mit expliziter Potenzialbewertung vertraut sind
- Grenzen: "Potenzial" ist schwer objektiv zu definieren, kann Labeling-Effekte erzeugen, kulturelle Vorbehalte in manchen europäischen Kontexten
- Moderation: beide Achsen vor der Sitzung mit verhaltensbasierten Beschreibungen definieren; Potenzial ist nicht "Sympathie" oder "Sichtbarkeit"

**Narrativ-basierte Talentreview**

- Wann es funktioniert: Führungskräfte-Review auf höchster Ebene, Rollen mit mehrdimensionaler, schwer auf Scores reduzierbarer Leistung, Organisationen, die qualitative Diskussion schätzen
- Grenzen: zeitintensiv, schwerer zu aggregieren, Moderationsfähigkeit ist entscheidend
- Moderation: das Narrativ mit konsistenten Prompts strukturieren (Stärken, Entwicklungsfelder, Readiness, Risiko)

**Kompetenzbasierte Bewertung**

- Wann es funktioniert: technische Organisationen, Rollen, in denen Kompetenzniveau der primäre Differenzierer ist, Organisationen mit reifen Kompetenz-Frameworks
- Grenzen: erfordert eine gepflegte Kompetenz-Taxonomie, kann Führungs- und Verhaltensdimensionen übersehen
- Moderation: mit der Kompetenz-Level-Matrix aus der Job-Architektur verknüpfen

**Succession-Readiness-Modelle**

- Wann es funktioniert: Fokus auf Kontinuität kritischer Rollen, Organisationen mit identifizierten Schlüsselpositionen
- Grenzen: enger Fokus (nur Nachfolge), kann Anspruchserwartungen erzeugen
- Moderation: Readiness in Zeithorizonten bewerten (jetzt bereit, in 1–2 Jahren bereit, in 3+ Jahren bereit) mit konkreten Entwicklungsmaßnahmen für jeden Horizont

### Einen Ansatz wählen

Die Wahl hängt vom organisationalen Kontext ab:

- Organisationsgröße: 9-Box skaliert besser; Narrativ skaliert schlechter
- Kultureller Kontext: manche europäische Organisationen lehnen explizites Potenzial-Labeling ab
- Reife der HR-Prozesse: kompetenzbasiert erfordert ein bestehendes Kompetenz-Framework
- Zweck: Nachfolgeplanung favorisiert Readiness-Modelle; Entwicklungsplanung favorisiert kompetenzbasiert; allgemeine Talentreview kann jeden Ansatz nutzen

## Gestaltung der Rating-Skala

Wenn das Leistungsmanagement-Modell Ratings nutzt:

### Skalenkonstruktion

| Skalentyp | Vorteile | Nachteile |
| --- | --- | --- |
| 3-stufig | Einfach, erzwingt Differenzierung | Kann für nuancierte Rollen zu grob wirken |
| 4-stufig (ohne Mittelpunkt) | Erzwingt eine Richtung (über/unter Erwartung) | Kann sich für die Kategorie "unter Mitte" strafend anfühlen |
| 5-stufig | Vertraut, erlaubt Nuancen | Risiko der zentralen Tendenz (die meisten Ratings clustern bei 3) |
| Verhaltenslabels (ohne Zahlen) | Reduziert die "Score"-Mentalität | Quantitativ schwerer zu aggregieren |

### Verteilungsansätze

**Geleitete Verteilung**: Erwartete Bandbreiten als Richtwerte vorgeben, nicht als Quoten. Die Organisation definiert die erwartete Verteilungsform; Führungskräfte begründen Abweichungen.

**Keine vorgegebene Verteilung**: Ratings dorthin fallen lassen, wo die Evidenz sie stützt. Die Kalibrierung fängt Inkonsistenz ab. Erfordert starke Kalibrierungs-Moderation.

**Erzwungene Verteilung** (Forced Ranking): Spezifische Prozentsätze je Kategorie vorschreiben. Wirksam gegen Inflation, aber kontrovers — kann Vertrauen beschädigen, Wettbewerb schaffen und leistungsstarke Teams bestrafen, in denen alle die Erwartungen tatsächlich erfüllen.

> [Methodik-Framework] Alle Verteilungsansätze sind Design-Entscheidungen mit Trade-offs. Kein einzelner Ansatz ist von Natur aus korrekt. Erzwungene Verteilung ist nicht "veraltet" und geleitete Verteilung ist keine "Best Practice" — jeder dient unterschiedlichen organisationalen Kontexten. Stelle die Trade-offs dar und lass die Organisation wählen.

## Methodik im Umgang mit Minderleistung

Dieser Abschnitt behandelt die universellen Prozesselemente im Umgang mit Minderleistung. Arbeitsrechtliche Implikationen variieren dramatisch je nach Jurisdiktion — spezifische Verfahrensanforderungen (Abmahnung in Deutschland, entretien préalable in Frankreich, dossieropbouw in den Niederlanden) sind jurisdiktionsspezifisch und erfordern die Prüfung mit arbeitsrechtlicher Beratung.

### Universelle Prozesselemente

Unabhängig von der Jurisdiktion folgt effektives Minderleistungs-Management einer konsistenten Methodik:

1. Identifikations-Trigger : Spezifische, dokumentierte Lücke zwischen erwarteter Leistung (aus Job-Level-Erwartungen) und tatsächlicher Leistung (aus während des Leistungszyklus gesammelter Evidenz)
2. Ursachenanalyse : Leistungslücken können aus Fähigkeit (Skill-Lücke), Motivation, Klarheit (unklare Erwartungen), Ressourcen (Werkzeuge, Support, Zeit) oder persönlichen Umständen entstehen. Die Intervention muss zur Ursache passen.
3. Formale Dokumentation : Jeder Schritt mit Daten, konkreten Verhaltensweisen, erwarteten Standards und vereinbarten Maßnahmen dokumentiert. Diese Dokumentation ist unabhängig von der Jurisdiktion kritisch.
4. Verbesserungsplan : Spezifische, messbare Verbesserungsziele mit realistischem Zeitrahmen, definierter Unterstützung (Training, Coaching, angepasste Arbeitslast) und klaren Erfolgskriterien
5. Regelmäßige Checkpoints : Geplante Reviews während der Verbesserungsphase mit dokumentierter Fortschrittsbewertung
6. Ergebnisentscheidung : Am Ende der Verbesserungsphase eine dokumentierte Bewertung, ob die Verbesserungskriterien erfüllt, teilweise erfüllt oder nicht erfüllt wurden, mit den daraus folgenden nächsten Schritten

> **KRITISCH**: Prüfe die spezifischen Verfahrensanforderungen, Fristen, die Einbindung von Arbeitnehmervertretungen und die rechtlichen Schutzmechanismen mit arbeitsrechtlicher Beratung in der zutreffenden Jurisdiktion, BEVOR du einen formalen Minderleistungs-Prozess einleitest. Ein fehlerhafter Prozess kann die Organisation erheblichem rechtlichem Risiko aussetzen.

## Bias-Minderung in der Leistungsbewertung

Leistungskalibrierung teilt Bias-Typen mit dem strukturierten Recruiting (siehe Skill für strukturiertes Recruiting). Die folgenden Gegenmaßnahmen sind spezifisch für den Leistungskontext:

- Recency : Evidenz aus dem GESAMTEN Beurteilungszeitraum verlangen, nicht nur aus dem letzten Quartal. Führungskräfte sollten den gesamten Zyklus über eine laufende Dokumentation pflegen.
- Milde/Strenge : Der primäre Zweck der Kalibrierung — der teamübergreifende Verteilungsvergleich legt systematisches Über-/Unterbewerten offen.
- Zentrale Tendenz : Auch für mittlere Ratings eine evidenzbasierte Begründung verlangen, nicht nur für Ausreißer. "Erfüllt Erwartungen" ist eine positive Aussage, kein Default.
- Halo/Horns : Jede Kompetenz oder jedes Ziel unabhängig bewerten, bevor ein Gesamtrating gebildet wird.
- Attribution : Individuellen Beitrag von Umweltfaktoren unterscheiden (Team-Ressourcen, Marktbedingungen, organisationale Veränderungen).
- Kontrast : Jede Diskussion an den Job-Level-Erwartungen verankern, nicht an der unmittelbar zuvor besprochenen Person.

Moderiere explizite Bias-Checks während der Kalibrierung: nach jedem Abschnitt fragen "Sehen wir Muster darin, wer die höchsten/niedrigsten Ratings erhält? Gibt es demografische, betriebszugehörigkeits- oder teambezogene Muster?"

## Guardrails

- Erzeuge niemals Mitarbeiter-Leistungsbewertungen, Ratings oder Talentklassifizierungen. Alle Leistungsdaten müssen aus der Organisation kommen.
- Stelle niemals ein einzelnes Leistungsmodell als von Natur aus überlegen dar oder behaupte "Industriestandard" für Rating-Skalen, Verteilungen oder Kalibrierungsansätze. Verteilung ist eine organisationale Design-Entscheidung.
- Markiere, wenn Empfehlungen das Arbeitsrecht berühren : "Verfahrensanforderungen mit arbeitsrechtlicher Beratung in [ Jurisdiktion ] prüfen."
- Versieh jede Ausgabe mit einer Quellenkennzeichnung : [Methodik-Framework] , [Aus Organisationsdaten] oder [KI-Bewertung — mit HR verifizieren] .

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um ein formatiertes, sofort teilbares Dokument zu erhalten.
