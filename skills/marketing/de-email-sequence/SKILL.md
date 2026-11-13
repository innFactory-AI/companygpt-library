---
name: de-email-sequence
description: Entwirft und textet mehrteilige E-Mail-Sequenzen — Onboarding, Nurture, Re-Engagement — mit Verzweigungslogik und Performance-Benchmarks. Verwende ihn, wenn du einen automatisierten E-Mail-Flow aufbaust, eine bestehende Sequenz optimierst oder Lifecycle-Kommunikation gestaltest. Auslösen mit "E-Mail-Sequenz erstellen für", "Onboarding-E-Mail-Flow", "Nurture-Sequenz für [Segment]".
---

# E-Mail-Sequenz-Skill

Entwirf mehrteilige automatisierte E-Mail-Sequenzen — von der Zieldefinition über die Sequenz-Architektur mit Timing und Verzweigungslogik bis zu den einzelnen E-Mail-Entwürfen und Performance-Benchmarks. Nur für automatisierte Sequenzen, nicht für einmalige Kampagnen oder Newsletter.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **ESP / Marketing-Automation über MCP** (z. B. HubSpot, Mailchimp) | Bestehende Sequenzen, Segmente, historische Open-/Click-Daten, Personalisierungs-Tokens |
| **CRM über MCP** (z. B. HubSpot, Salesforce) | Lifecycle-Stages, Lead-Scores, Account-Daten, Enrollment-Trigger |
| **companyRAG / Datei-Upload** | Markenrichtlinien, Tone-of-Voice-Vorgaben, frühere Kampagnen-Briefings, Produktinformationen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Sequenz-Design-Workflow

Führe diese Schritte der Reihe nach aus. Jeder Schritt baut auf dem vorherigen auf — wer ohne Zieldefinition und Sequenz-Map direkt zum Texten springt, produziert E-Mails, die nicht als System zusammenwirken.

### Schritt 1: Sequenz-Ziel definieren

Jede Sequenz existiert, um Empfänger von einem aktuellen Zustand in einen gewünschten Zustand zu bewegen. Definiere beide.

```
SEQUENZ-ZIEL:
  Sequenzname:     [aussagekräftiger Name]
  Sequenztyp:      [Onboarding / Nurture / Re-Engagement / Event-getriggert / Lifecycle]
  Enrollment-Trigger: [welche Aktion oder welches Ereignis nimmt jemanden in diese Sequenz auf?]
  Aktueller Zustand:  [wo steht der Empfänger jetzt? — z. B. registriert, aber nicht aktiviert]
  Gewünschter Zustand: [wo soll er nach der Sequenz stehen? — z. B. erstes Projekt abgeschlossen]
  Primäre Kennzahl: [die EINE Zahl, die den Erfolg der Sequenz definiert]
  Austrittsbedingungen: [was entfernt jemanden aus der Sequenz — Ziel erreicht, abgemeldet, in andere Sequenz aufgenommen, Zeit abgelaufen]
```

**Qualitätscheck des Ziels:**

| Check | Frage | Wenn Nein |
| --- | --- | --- |
| Spezifisch | Kannst du den gewünschten Zustand in einem Satz beschreiben? | Scope verengen |
| Messbar | Kannst du nachverfolgen, ob Empfänger den gewünschten Zustand erreichen? | Eine trackbare Kennzahl wählen |
| Begrenzt | Hat die Sequenz ein klares Ende? | Austrittsbedingungen definieren |
| Eindeutig | Unterscheidet sich dieses Ziel von anderen aktiven Sequenzen? | Zusammenführen oder differenzieren |

### Schritt 2: Sequenztyp wählen und Architektur kartieren

Nutze den Sequenztyp-Router, um das passende Architekturmuster zu bestimmen, und kartiere anschließend die konkrete Sequenz.

#### Sequenztyp-Router

| Typ | Enrollment-Trigger | Typische Länge | Kernmuster |
| --- | --- | --- | --- |
| **Onboarding** | Account-Erstellung, Kauf, Abo-Start | 5–10 E-Mails über 14–30 Tage | Progressive Aktivierungs-Meilensteine |
| **Nurture** | Content-Download, Webinar-Anmeldung, Lead-Score-Schwelle | 4–8 E-Mails über 3–8 Wochen | Mehrwert-Lieferung, die zur Conversion-Aufforderung führt |
| **Re-Engagement** | Inaktivität über definierten Zeitraum (30/60/90 Tage) | 3–5 E-Mails über 10–21 Tage | Eskalierende Dringlichkeit mit finalem Sunset |
| **Event-getriggert** | Konkrete Nutzeraktion (Warenkorbabbruch, Feature-Nutzung, Meilenstein) | 2–4 E-Mails über 3–7 Tage | Kontextueller Follow-up zum Trigger-Ereignis |
| **Lifecycle** | Zeitbasierte Meilensteine (Jubiläum, nahender Verlängerungstermin) | 3–6 E-Mails über 2–4 Wochen | Beziehungspflege und Expansion |

#### Architektur-Mapping

Definiere für jede E-Mail in der Sequenz:

```
SEQUENZ-MAP:

E-Mail 1: [Name / Zweck]
  Timing:     [Trigger + Verzögerung — z. B. "Sofort nach Anmeldung" oder "Tag 3"]
  Ziel:       [Was soll der Empfänger nach dem Lesen dieser E-Mail TUN?]
  Content-Thema: [Kernbotschaft — noch nicht der vollständige Entwurf]
  CTA:        [Primärer Call-to-Action]
  Verzweigung danach: [Wenn Empfänger handelt → springe zu E-Mail X / Austritt. Wenn keine Aktion → weiter zu E-Mail 2]

E-Mail 2: [Name / Zweck]
  Timing:     [Verzögerung gegenüber vorheriger E-Mail oder Trigger]
  Bedingung:  [Wer erhält diese? — z. B. "Empfänger, die Onboarding-Schritt 1 NICHT abgeschlossen haben"]
  Ziel:       [...]
  Content-Thema: [...]
  CTA:        [...]
  Verzweigung danach: [...]

  ...für alle E-Mails der Sequenz fortsetzen
```

**Timing-Richtlinien nach Sequenztyp:**

| Typ | E-Mail 1 | Folge-E-Mails | Letzte E-Mail |
| --- | --- | --- | --- |
| Onboarding | Sofort | 1–3 Tage Abstand (früh schneller, später langsamer) | Tag 14–30 je nach Aktivierungs-Zeitlinie |
| Nurture | Sofort oder am nächsten Tag | 3–7 Tage Abstand | Nach vollständiger Mehrwert-Lieferung, bevor es abkühlt |
| Re-Engagement | Tag 1 der Inaktivitätsschwelle | 3–5 Tage Abstand | 14–21 Tage — finaler Sunset-Hinweis |
| Event-getriggert | Innerhalb 1 Stunde nach Trigger | 1–3 Tage Abstand | Innerhalb 7 Tagen nach Trigger |

### Schritt 3: Einzelne E-Mails texten

Erstelle für jede E-Mail der Sequenz-Map einen Entwurf. Jede E-Mail muss für sich allein funktionieren (Empfänger lesen nicht zwingend jede E-Mail) und gleichzeitig zum Sequenz-Bogen beitragen.

**Struktur des E-Mail-Entwurfs:**

```
E-MAIL [N]: [Name]
  Betreffzeile:   [primäre Option]
  Betreffzeile B: [A/B-Test-Variante — ändere NUR EIN Element]
  Preview-Text:   [der Text, der nach dem Betreff in der Inbox-Ansicht erscheint]

  ---

  [Anrede]

  [Einstieg — 1–2 Sätze, die an den Kontext des Empfängers oder den Sequenz-Trigger anknüpfen.
   Beantworte: Warum erhalte ich das? Warum sollte mich das interessieren?]

  [Body — 2–4 kurze Absätze, die das Content-Thema der E-Mail einlösen.
   Eine Idee pro Absatz. Kurze Sätze. Scannbar.]

  [CTA — klar, spezifisch, eine einzige primäre Aktion.
   Button-Text: [handlungsorientierte Verbphrase]
   Link: [Ziel]]

  [Abschluss — 1–2 Sätze. Setze ggf. eine Erwartung für die nächste E-Mail.]

  [Signatur]

  ---

  Hinweise zur Umsetzung:
  - Personalisierungs-Tokens: [liste verwendete Merge-Felder — z. B. {{first_name}}, {{company}}, {{product_feature}}]
  - Dynamischer Content: [Abschnitte, die je nach Segment oder Verhalten variieren]
  - Rechtliche Anforderungen: [Abmeldelink, Postanschrift, branchenspezifische Pflichthinweise]
```

**Prinzipien des E-Mail-Textens:**

| Prinzip | Anwendung |
| --- | --- |
| Eine E-Mail, ein Ziel | Jede E-Mail hat einen einzigen primären CTA. Sekundäre Links sind erlaubt, dürfen aber nicht konkurrieren. |
| Progressiver Mehrwert | Jede E-Mail der Sequenz liefert Mehrwert, unabhängig davon, ob vorherige E-Mails gelesen wurden. |
| Aufmerksamkeit respektieren | Halte E-Mails scannbar. Nutze kurze Absätze, Bulletpoints und klare visuelle Hierarchie. |
| Verdiente Eskalation | Verlange keine Aktionen mit hohem Commitment (Kauf, Demo, Meeting), bevor Mehrwert etabliert ist. |
| Kontextbewusstsein | Beziehe dich auf das Trigger-Ereignis oder die Phase des Empfängers. Generisch wirkende Automatik-Mails werden ignoriert. |

### Schritt 4: Verzweigungslogik entwerfen

Definiere die Entscheidungspunkte, an denen sich die Sequenz an das Verhalten des Empfängers anpasst.

**Standard-Verzweigungsmuster:**

| Trigger | Verzweigungs-Aktion |
| --- | --- |
| Empfänger erreicht das Sequenz-Ziel | Austritt → in die nächste Lifecycle-Phase überführen |
| Empfänger klickt CTA, konvertiert aber nicht | In eine Follow-up-E-Mail verzweigen, die häufige Einwände adressiert |
| Empfänger öffnet, klickt aber nicht | Nach 2–3 Tagen mit anderer Betreffzeile oder anderem CTA erneut senden |
| Empfänger öffnet 2+ aufeinanderfolgende E-Mails nicht | Frequenz reduzieren oder in eine Re-Engagement-Sequenz überführen |
| Empfänger meldet sich ab | Sofortiger Austritt — rechtliche Pflicht |
| Empfänger wird in eine höher priorisierte Sequenz aufgenommen | Diese Sequenz pausieren oder beenden, um Überschneidungen zu vermeiden |

**Dokumentationsformat für Verzweigungen:**

```
ENTSCHEIDUNGSPUNKT: Nach E-Mail [N]
  WENN [Bedingung — z. B. "CTA geklickt und Aktivierungsschritt abgeschlossen"]
    DANN → [Aktion — z. B. "Sequenz verlassen, in Nurture-Sequenz aufnehmen"]
  SONST WENN [Bedingung — z. B. "geöffnet, aber nicht geklickt"]
    DANN → [Aktion — z. B. "E-Mail N+1 (alternativer CTA) nach 2 Tagen senden"]
  SONST [Standard — z. B. "nicht geöffnet"]
    DANN → [Aktion — z. B. "E-Mail N+1 nach 3 Tagen senden"]
```

### Schritt 5: Performance-Benchmarks festlegen

Definiere, wie die Gesundheit der Sequenz überwacht wird. Alle Benchmarks müssen aus DEINEN historischen Daten stammen oder während einer Baseline-Phase erhoben werden.

**Sequenz-Gesundheitskennzahlen:**

| Kennzahl | Was sie misst | Überwachen auf |
| --- | --- | --- |
| Sequenz-Abschlussrate | % der aufgenommenen Empfänger, die den gewünschten Zustand erreichen | Sequenzebene |
| Open-Rate je E-Mail | Engagement mit einzelnen E-Mails | E-Mail-Ebene |
| Click-Rate je E-Mail | Auf einzelnen E-Mails ausgelöste Aktionen | E-Mail-Ebene |
| Drop-off-Rate | % derer, die bei jedem Schritt aussteigen | Pro E-Mail-Übergang |
| Time-to-Goal | Wie lange Abschließer bis zum gewünschten Zustand brauchen | Sequenzebene |
| Abmelderate | Opt-outs der Empfänger je E-Mail | E-Mail-Ebene |

**Prozess zur Benchmark-Festlegung:**

1. Wenn historische Sequenzdaten vorliegen, nutze deine eigene Vergangenheits-Performance als Baseline
2. Wenn keine historischen Daten vorliegen, lasse die Sequenz 2–4 Wochen als Baseline-Phase laufen, bevor du optimierst
3. Setze Verbesserungsziele als prozentuale Zugewinne gegenüber DEINER Baseline — nicht gegen externe Benchmarks
4. Überwache im ersten Monat wöchentlich, danach zweiwöchentlich, sobald die Sequenz stabil ist

**Diagnose-Trigger:**

| Signal | Wahrscheinliche Ursache | Untersuchung |
| --- | --- | --- |
| Niedrige Open-Rate bei E-Mail 1 | Betreffzeile, Absendername oder Timing | Betreffzeilen per A/B-Test prüfen; Sendezeit checken |
| Viele Öffnungen, aber wenige Klicks | Content-CTA-Mismatch oder schwacher CTA | Klarheit und Relevanz des CTA überprüfen |
| Starker Drop-off nach einer bestimmten E-Mail | Diese E-Mail liefert keinen Mehrwert oder verlangt zu viel | Inhalt, Timing und Höhe der Aufforderung prüfen |
| Viele Abmeldungen bei einer bestimmten E-Mail | Wahrgenommene Irrelevanz oder zu hohe Frequenz | Targeting, Personalisierung und Timing prüfen |
| Insgesamt niedrige Abschlussrate | Sequenz-Ziel zu ambitioniert, falsche Zielgruppe oder zu viele E-Mails | Ziel, Aufnahmekriterien und Sequenzlänge neu bewerten |

## Anti-Patterns

Muster, die die Wirksamkeit von E-Mail-Sequenzen verlässlich untergraben:

| Anti-Pattern | Problem | Lösung |
| --- | --- | --- |
| **Zu viele E-Mails, zu schnell** | Empfänger-Ermüdung → Abmeldungen und Spam-Beschwerden | E-Mails angemessen timen; wenige hochwertige E-Mails schlagen viele mittelmäßige |
| **Keine klare Austrittsbedingung** | Empfänger drehen sich im Kreis oder erhalten nach Conversion irrelevante E-Mails | Für jede Sequenz Austrittsbedingungen definieren |
| **Fehlender Abmeldelink** | Rechtsverstoß (DSGVO, CAN-SPAM, CASL) | Jede E-Mail muss einen funktionierenden Abmeldemechanismus enthalten — nicht verhandelbar |
| **Generisches "Batch and Blast" als Automation getarnt** | Keine Personalisierung oder Kontextbewusstsein → niedriges Engagement | Personalisierungs-Tokens, verhaltensbasierte Trigger und segmentspezifischen Content nutzen |
| **CTA-Überladung** | Mehrere konkurrierende Calls-to-Action → Entscheidungslähmung | Ein primärer CTA pro E-Mail; sekundäre Links zurücknehmen |
| **Nur Fordern, kein Mehrwert** | Jede E-Mail drängt auf Conversion → Empfänger steigen aus | Zwischen Mehrwert-Lieferung und Conversion-Aufforderung abwechseln (Zielverhältnis 3:1) |
| **Keine Suppression-Regeln** | Empfänger in mehreren Sequenzen werden überrannt | Frequenz-Caps und Sequenz-Prioritätsregeln einführen |
| **Zeitzonen ignorieren** | E-Mails treffen zu ungünstigen Zeiten ein → niedrigere Open-Rates | Möglichst in der lokalen Zeitzone des Empfängers senden |

## Leitplanken

- Erzeuge niemals E-Mail-Performance-Benchmarks (Open-Rates, Click-Rates, Conversion-Rates). Alle Daten müssen aus der E-Mail-Plattform des Nutzers stammen.
- Behaupte niemals "beste" Sendezeiten, "optimale" Frequenz oder "ideale" Sequenzlänge. Das hängt von der Zielgruppe ab und muss getestet werden.
- Ohne Markenrichtlinien verwende einen neutralen, professionellen Ton und kennzeichne Copy als `[Entwurf — an deine Markenstimme anpassen]`.
- Kennzeichne Ausgaben: `[Aus Kundendaten]` für bezogene Daten · `[Framework-Methodik]` für den Ansatz dieses Skills · `[Entwurf — an deine Markenstimme anpassen]` für Copy, die angepasst werden muss.

> **Tipp:** Fordere über companyFILES eine DOCX- oder Markdown-Ausgabe an, um eine formatierte, sofort teilbare Sequenz zu erhalten.
