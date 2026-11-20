---
name: de-create-skill
description: Erstellt, verbessert und testet Skills für companyGPT-Agenten. Verwende diesen Skill immer, wenn der Nutzer einen neuen Skill schreiben, einen Ablauf aus diesem Chat als Skill speichern, einen bestehenden Skill verbessern oder reparieren, eine bessere Skill-Beschreibung formulieren möchte oder fragt, warum ein Skill nicht genutzt wird, auch wenn er nur sagt „speicher das als wiederverwendbare Anleitung“ oder „bring dem Agenten bei, wie wir X machen“.
---

# Skill erstellen

Du hilfst dem Nutzer, einen Skill zu bauen: eine wiederverwendbare Anleitung, die companyGPT-Agenten eine Aufgabe
beibringt. Ein guter Skill macht aus dem allgemeinen Agenten einen Spezialisten für diese Aufgabe, ohne dass jemand
den Prompt neu tippen muss. Du befragst, schreibst, speicherst, testest und verbesserst den Skill gemeinsam mit dem
Nutzer.

## So funktionieren Skills in companyGPT

Mit diesem Wissen schreibst du Skills, die auch wirklich genutzt werden:

- **Katalog:** Der Agent sieht von jedem verfügbaren Skill nur `name` und `description`, jeweils etwa 250 Zeichen.
  Die Beschreibung ist der einzige Auslöser. Ist sie vage, wird der Skill nie geladen.
- **Laden:** Passt eine Anfrage, ruft der Agent das Tool `skill` auf und bekommt den Inhalt der `SKILL.md`. Nutzer
  können einen Skill auch starten, indem sie im Chat-Eingabefeld `$` tippen und ihn auswählen.
- **Mitgelieferte Dateien:** Ein Skill kann weitere Dateien enthalten (`references/…`, `scripts/…`, `assets/…`).
  Der Agent liest sie mit `read_file` (`skills/<name>/references/x.md`) erst, wenn er sie braucht; bis dahin kosten
  sie nichts. Mit Code-Ausführung liegen sie außerdem schreibgeschützt in der Sandbox unter
  `/mnt/data/skills/<name>/`.
- **Verfügbarkeit:** Deine eigenen Skills sind für dich aktiv. Ein Agent nutzt Skills nur, wenn sein Skills-Modus
  **All** oder **Selected** ist (mit ausgewähltem Skill). Jeder Nutzer kann einen Skill mit **Available to agent**
  für sich ausschalten.

## Schritt 1: Das Ziel erfassen

Enthält der Chat den Ablauf schon (der Nutzer hat die Aufgabe gerade mit dir erledigt), zieh ihn zuerst heraus: die
Schritte, die genutzten Tools, die Korrekturen des Nutzers, das Format des Ergebnisses. Dann füll die Lücken. Du
brauchst:

1. **Die Aufgabe:** Was soll der Agent mit diesem Skill können? Eine Aufgabe pro Skill.
2. **Den Auslöser:** Welche Anfragen sollen ihn laden? Sammle die Wörter, die Nutzer wirklich tippen, in jeder
   Sprache, in der deine Nutzer schreiben.
3. **Das Ergebnis:** Wie sieht ein gutes Ergebnis aus (Format, Länge, Dateityp, Ton)? Frag nach einem echten
   Beispiel.
4. **Daten und Tools:** Woher kommt die Eingabe (angehängte Datei, companyRAG-Collection, Microsoft 365, Web), und
   wohin geht das Ergebnis (Antwort im Chat, Word/Excel/PowerPoint/PDF über companyFILES, Mail-Entwurf)?
5. **Die Regeln:** firmenspezifische Konventionen, was früher schiefgelaufen ist, was nie passieren darf.

Frag nur, was du nicht herausziehen kannst, immer nur wenige Fragen auf einmal. Nutze `ask_user_question`, wenn es
in deiner Tool-Liste steht. Frag nicht nach Dingen, die das Modell ohnehin kann (eine Zusammenfassung schreiben,
eine SWOT erstellen); ein Skill ergänzt das Wissen des Teams, nicht Allgemeinwissen.

## Schritt 2: Prüfen, ob ein Skill das Richtige ist

Ein Skill enthält **Ablaufwissen**: wie diese Organisation eine Aufgabe erledigt. Prüf zuerst die Alternativen:

| Der Bedarf ist … | Besser geeignet |
| --- | --- |
| Eine einmalige Aufgabe | Einfach im Chat erledigen |
| Nachschlagematerial (Handbücher, Richtlinien, Preislisten), das der Agent durchsuchen soll | Eine companyRAG-Collection oder Dateien im Agenten |
| Zugriff auf ein System (Live-Daten lesen, eine Aktion ausführen) | Ein Tool / MCP-Server; Admins können REST-APIs anbinden |
| Eine feste Rolle mit eigenem Modell, eigenen Tools und Anweisungen für ein Team | Ein Agent (siehe **de-agent-design**), der dann diesen Skill nutzt |
| Wie eine wiederkehrende Aufgabe erledigt wird, mit Schritten, Regeln und Ausgabeformat | **Ein Skill** |

Oft ist es eine Kombination: Der MCP-Server liefert den Zugriff, der Skill sagt, wie man ihn nutzt.

## Schritt 3: Die Tools prüfen

Ein Skill darf nur Tools nennen, die es gibt. Schau in deine eigene Tool-Liste oder nutze die Tool-Suche (siehe
**de-tool-search**) und übernimm Tool-Namen und Parameter exakt. Für ein Tool, das nicht immer da ist (eine App,
die im Mandanten nicht aktiv ist, Code-Ausführung, die für eine Rolle abgeschaltet ist), schreib „falls verfügbar“
und nenne eine Alternative. Erfinde nie ein Tool, einen Parameter oder ein Limit.

Typische Bausteine in companyGPT (nur, wenn sie in deiner Tool-Liste stehen):

- **companyFILES:** Word, Excel, PowerPoint, PDF erstellen und lesen; Vorlagen; Diagramme (siehe die Datei-Skills
  wie **de-excel**, **de-powerpoint**, **de-templates**).
- **companyRAG (`ai-search`):** Wissens-Collections des Unternehmens durchsuchen, Datasets abfragen.
- **companyM365:** Mail, Kalender, OneDrive/SharePoint, Teams, OneNote, Planner.
- **companyTRANSLATE, companyTRANSCRIBE:** Texte und Dokumente übersetzen, Audio und Video transkribieren.
- **Code-Ausführung:** Berechnungen, Datenanalyse, mitgelieferte Skripte ausführen. Nicht überall verfügbar.
- **Websuche / WebFetch, `ask_user_question`, Erinnerung:** je nach Agent.

## Schritt 4: Den Skill schreiben

### Name

- Kleinbuchstaben, Ziffern und Bindestriche, höchstens 64 Zeichen, z. B. `quartalsbericht` oder `angebotspruefung`.
  Er darf nicht mit `claude-` oder `anthropic-` beginnen.
- Konkret, nicht `helfer` oder `tools`. Führt deine Organisation Skills in mehreren Sprachen, halte dich an ihre
  Präfix-Konvention (z. B. `de-…` / `en-…`).
- Der Name ist die Identität des Skills: Agenten verweisen darauf, und er lässt sich später nicht umbenennen (nur
  unter neuem Namen neu anlegen). Wähle ihn sorgfältig.

### Beschreibung (der wichtigste Teil)

Max. 1024 Zeichen, aber alles, was über den Auslöser entscheidet, gehört in die **ersten 250 Zeichen**, weil der
Katalog längere Beschreibungen kürzt.

- Sag, **was** der Skill tut und **wann** er genutzt wird, in der dritten Person: „Erstellt … Verwende diesen Skill,
  wenn …“.
- Nenne die konkreten Auslöser: Aufgabenwörter, Dokumenttypen, Systeme, die Formulierungen, die Nutzer tippen.
- Sei ruhig etwas nachdrücklich, denn Agenten lassen Skills aus, bei denen sie unsicher sind: „Verwende diesen Skill
  immer, wenn der Nutzer … erwähnt, auch wenn er nicht ausdrücklich danach fragt.“
- Lässt sich der Skill leicht mit einem anderen verwechseln, sag, wofür er **nicht** gedacht ist.

Schwach: `Hilft bei Berichten.`
Stark: `Erstellt den monatlichen Vertriebsbericht als Excel-Datei aus dem CRM-Export. Verwende diesen Skill immer,
wenn der Nutzer nach dem Vertriebsbericht, Monatszahlen, Umsatz nach Region fragt oder einen CRM-Export anhängt,
auch wenn er nicht „Bericht“ sagt.`

### Inhalt

Schreib den Inhalt für eine fähige Kollegin, die neu im Team ist: Das Modell kann bereits schreiben, rechnen und
zusammenfassen. Jeder Absatz muss seine Tokens wert sein. Eine bewährte Struktur:

```markdown
# <Titel>

<Ein oder zwei Sätze: was der Skill erreicht.>

## Schritt 1: … (Eingaben sammeln)
## Schritt 2: … (Die Arbeit erledigen, mit den genauen Tools)
## Schritt 3: … (Das Ergebnis liefern: Format, Datei, wohin)

## Ausgabeformat
<Eine Vorlage oder ein kurzes Beispiel für ein gutes Ergebnis.>

## Regeln
<Konventionen und Leitplanken, jeweils mit Begründung.>
```

- **Schritte:** nummeriert und in Reihenfolge. Für lange oder riskante Aufgaben eine Checkliste, die der Agent
  abarbeitet.
- **Erklär das Warum.** „Runde auf volle Euro, weil der Vorstandsbericht das auch tut“ wirkt besser als „IMMER
  RUNDEN“. Eine Regel in Großbuchstaben ohne Begründung ist ein Warnzeichen.
- **Ein Standardweg, eine Alternative.** Nicht fünf Optionen. Beispiel: „Erstelle die Datei mit companyFILES
  `create_excel`; ist companyFILES nicht verfügbar, gib die Tabelle als Markdown aus.“
- **Konkrete Beispiele** für Eingabe und Ausgabe statt abstrakter Beschreibungen.
- **Strenge passend zum Risiko:** freier Text für offene Aufgaben, genaue Schritte oder eine feste Vorlage, wo
  Fehler teuer sind (Verträge, Zahlen, Mails an Kunden).
- **Bestätigung vor Nebenwirkungen:** Mails senden, Dateien löschen oder fremde Kalender ändern erst, wenn der
  Nutzer zustimmt.
- **Einheitliche Begriffe:** ein Wort pro Konzept, durchgehend.
- **Keine Datumsangaben oder „aktuell“**, die veralten; keine Passwörter, Schlüssel, personenbezogenen Daten oder
  Kundengeheimnisse im Skill.
- **Länge:** Halte die `SKILL.md` deutlich unter 500 Zeilen. Lagere langes Material in mitgelieferte Dateien aus
  (nächster Abschnitt).

### Mitgelieferte Dateien (optional)

Für langes Nachschlagematerial (ein Styleguide, ein ausführliches Rezept, ein Skript):

- Leg es in `references/<thema>.md` (oder `scripts/…`, `assets/…`) ab, eine Ebene tief, und verlinke es aus der
  `SKILL.md` mit Pfad und Anlass: „Für die vollständige Preistabelle lies `skills/<name>/references/preise.md`.“
- Referenzdateien mit mehr als etwa 100 Zeilen beginnen mit einem kurzen Inhaltsverzeichnis.
- Die `SKILL.md` muss allein funktionieren, denn ein als einzelne Datei eingefügter Skill hat keine mitgelieferten
  Dateien.

### Code (optional)

Der Skill muss ohne Code-Ausführung funktionieren. Code-Schritte kommen in einen optionalen Abschnitt, der mit „Wenn
Code-Ausführung verfügbar ist …“ beginnt, die Alternative nennt, Python-Pakete per `import` prüft, bevor er sich auf
sie verlässt, und daran denkt, dass die Sandbox keinen Netzwerkzugang hat. Skripte, die der Agent ausführen soll,
gehören in `scripts/`; sie fangen ihre Fehler selbst ab und erklären, wofür jede Konstante steht.

### Optionale Frontmatter-Felder

Die meisten Skills brauchen nur `name` und `description`. Nutze diese Felder nur mit Grund:

| Feld | Wirkung |
| --- | --- |
| `disable-model-invocation: true` | Der Agent lädt den Skill nie von sich aus; nur `$` im Chat startet ihn. Für Skills mit Nebenwirkungen. |
| `user-invocable: false` | Im `$`-Menü ausgeblendet; nur der Agent lädt ihn. |
| `always-apply: true` | In jedem Gespräch geladen. Sparsam einsetzen: kostet in jedem Chat Kontext. |
| `allowed-tools` | Tools, die der Skill für den Durchlauf mitbringt, als Liste. |

`$ARGUMENTS` im Inhalt wird durch das ersetzt, was der Nutzer beim Start mit `$` hinter den Skill getippt hat.

## Schritt 5: Den Skill speichern

Zeig dem Nutzer die vollständige `SKILL.md` und hol dir zuerst sein OK. Dann speichere ihn:

1. **Wenn `create_file` in deiner Tool-Liste steht** und `skills/…`-Pfade annimmt: Leg `skills/<name>/SKILL.md` an
   (und mitgelieferte Dateien unter `skills/<name>/references/…`). Der `name` im Frontmatter muss `<name>`
   entsprechen. Setz bei einem neuen Skill kein `overwrite`; existiert der Name schon, frag vor dem Überschreiben.
   Ändere einen bestehenden Skill mit `edit_file`, statt ihn neu zu schreiben.
2. **Sonst, mit Code-Ausführung:** Schreib den Ordner `/mnt/data/<name>/` mit `SKILL.md` (und mitgelieferten
   Dateien) und pack ihn als `/mnt/data/<name>.zip`; die ZIP-Datei kommt als Chat-Anhang zurück. Der Nutzer lädt sie
   unter **Skills → + → Skill hochladen** hoch.
3. **Sonst:** Gib die vollständige `SKILL.md` in einem Markdown-Codeblock aus. Der Nutzer legt sie unter
   **Skills → + → Skill-Anweisungen schreiben** an (Name, Beschreibung und den Inhalt als Anleitung) oder speichert
   sie als `SKILL.md` und lädt sie hoch.

Sag dem Nutzer, wie er den Skill verfügbar macht: in der Skill-Ansicht **Available to agent** einschalten und ihn
bei Bedarf einem Agenten mit Skills-Modus **Selected** hinzufügen. Für das Teilen mit Kollegen kann eine
Rollenberechtigung nötig sein; ein Skill für die ganze Organisation läuft über die companyGPT-Administratoren.

## Schritt 6: Testen und verbessern

Ein Skill ist erst fertig, wenn er getestet ist. Mit dem Nutzer:

1. **Schreib 2–3 realistische Testanfragen**, so formuliert, wie Nutzer wirklich schreiben, mit echten Details
   (Dateinamen, Kundennamen, Zahlen).
2. **Prüf den Auslöser:** Liste 3–5 Anfragen, die den Skill laden sollen, und 3–5 Beinahe-Treffer, die ihn nicht
   laden sollen (ähnliche Wortwahl, andere Aufgabe). Passe die Beschreibung an, wenn eine auf der falschen Seite
   landet.
3. **Führ die Tests aus** in einem neuen Chat mit dem Agenten, der den Skill hat (einmal per `$` laden ist ein
   schneller Test nur des Inhalts). Hast du den Skill selbst gespeichert, kannst du ihn auch hier mit dem Tool
   `skill` laden und eine Testanfrage direkt ausführen.
4. **Schau, wie der Agent gearbeitet hat, nicht nur auf das Ergebnis.** Hat er einen Schritt ausgelassen, ein Tool
   geraten, unnötige Fragen gestellt, das falsche Format geliefert? Korrigiere die Anweisung, die das verursacht hat.
5. **Verbessere allgemein.** Flicke den Skill nicht nur für einen Testfall; frag, was der Fall über die Anweisungen
   zeigt. Streich Anweisungen, die nichts gebracht haben.

Wiederhole das, bis der Nutzer mit den Ergebnissen zufrieden ist.

## Prüfliste

Bevor du einen Skill als fertig bezeichnest, prüfe:

- [ ] Name: Kleinbuchstaben, Bindestriche, ≤64 Zeichen, konkret, folgt der Konvention der Organisation.
- [ ] Beschreibung: was + wann + Auslösewörter in den ersten 250 Zeichen, dritte Person.
- [ ] Jedes Tool, jeder Parameter und jedes Limit steht in der Tool-Liste; optionale Apps haben eine Alternative.
- [ ] Funktioniert ohne Code-Ausführung und ohne mitgelieferte Dateien.
- [ ] Schritte sind nummeriert; das Ausgabeformat ist mit einem Beispiel gezeigt.
- [ ] Regeln nennen ihren Grund; keine unbegründeten MUSS in Großbuchstaben.
- [ ] Bestätigung vor dem Senden, Löschen oder Ändern fremder Daten.
- [ ] Keine Geheimnisse, personenbezogenen Daten oder zeitabhängigen Aussagen.
- [ ] Unter 500 Zeilen; langes Material in `references/`, eine Ebene tief verlinkt.
- [ ] Mit realistischen Anfragen getestet, auch mit Beinahe-Treffern für den Auslöser.
