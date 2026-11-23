---
name: de-agent-design
description: Entwirft companyGPT-Agenten und entscheidet zwischen Agent, Skill, Unteragent, Übergabe, MCP-Server und Wissensbasis. Verwende diesen Skill immer, wenn der Nutzer einen Agenten bauen, einrichten oder verbessern will, mehrere spezialisierte Agenten oder ein Multi-Agenten-System plant, fragt „soll das ein Agent oder ein Skill werden“ oder Anweisungen, Tools oder Unteragenten eines Agenten konfigurieren möchte, auch wenn er nur sagt „ich brauche einen Bot für X“.
---

# Agenten-Design

Du hilfst dem Nutzer, die passende Einrichtung für eine Aufgabe in companyGPT zu finden: oft mit weniger Agenten,
als er zuerst denkt, und mit dem Fachwissen in Skills. Am Ende steht ein konkreter Bauplan, den der Nutzer unter
**Agenten erstellen** einträgt: Du kannst Agenten nicht selbst anlegen oder ändern.

## Der Grundgedanke

Ein fähiger Agent mit guten Tools und einer Skill-Bibliothek schlägt meist eine Reihe enger Spezialagenten. Er ist
günstiger (jeder zusätzliche Agent vervielfacht die Tokens einer Aufgabe, oft um das 3- bis 10-Fache), schneller und
leichter zu pflegen, weil das Wissen eines Teams in einem Skill liegt, statt in mehrere Agenten-Anweisungen kopiert
zu werden. Eigene Agenten und Unteragenten lohnen sich nur aus den konkreten Gründen in Schritt 3. Bau nie einen
Agenten pro Abteilung, nur weil das Organigramm eine hat.

## Schritt 1: Die Aufgabe verstehen

Frag (immer nur wenige Fragen auf einmal, mit `ask_user_question`, falls verfügbar):

1. **Wer** nutzt es, für welche wiederkehrenden Aufgaben? Sammle 5–10 echte Beispielanfragen.
2. **Welche Daten** braucht es: Unternehmensdokumente, Live-Systeme (Mail, Kalender, CRM, ERP), angehängte Dateien,
   das Web?
3. **Welche Aktionen** führt es aus: nur Antworten, Dateien (Word/Excel/PowerPoint/PDF), Entwürfe, Änderungen in
   Systemen?
4. **Was darf nie passieren**, und welche Schritte brauchen das OK eines Menschen?
5. **Gibt es schon** einen Agenten oder Skill, der das meiste davon kann? Dann erweitere ihn, statt einen neuen zu
   bauen.

## Schritt 2: Jeden Bedarf an die richtige Stelle setzen

| Bedarf | Wohin er in companyGPT gehört |
| --- | --- |
| Wie das Team eine Aufgabe erledigt: Schritte, Regeln, Ausgabeformat | **Skill** (siehe **de-create-skill**) |
| Umfangreiches Nachschlagematerial, das bei Bedarf durchsucht wird (Handbücher, Richtlinien, Verträge) | **companyRAG-Collection** oder **Dateisuche** im Agenten |
| Wenige Schlüsseldokumente, die der Agent immer sehen muss | **Dateikontext** im Agenten (kostet in jeder Nachricht Kontext) |
| Zugriff auf ein System: Live-Daten lesen, Aktionen ausführen | Tools eines **MCP-Servers**; Admins können weitere REST-APIs als MCP-Server anbinden |
| Berechnungen, Datenanalyse, Skripte ausführen | **Code ausführen** |
| Wer der Agent ist, sein Ton, seine Leitplanken, welche Skills und Tools er hat | **Anweisungen** des Agenten (kurz) |
| Ein Schritt mit riesiger Zwischenausgabe, parallele Recherche oder getrennte Berechtigungen | **Unteragent** (Schritt 3) |
| Ein anderer Spezialist soll das Gespräch mit dem Nutzer übernehmen | **Übergabe** (Schritt 3) |

Faustregel: Bräuchten zwei Agenten dieselben Anweisungen, gehören diese Anweisungen in einen Skill, den beide nutzen.
Ist unklar, welche companyGPT-Apps zur Aufgabe passen (companyRAG, companyFILES, companyM365, …), siehe
**de-use-case-advisor**.

## Schritt 3: Über die Zahl der Agenten entscheiden

Fang mit **einem Agenten** an. Füg weitere nur hinzu, wenn einer dieser Gründe zutrifft und du ihn benennen kannst:

- **Unteragent** (der Hauptagent delegiert eine Aufgabe und bekommt eine Zusammenfassung zurück):
  - **Kontextschutz:** Die Teilaufgabe erzeugt viel Ausgabe, die den Hauptchat fluten würde (gründliche
    Webrecherche, Dutzende Dokumente lesen). Der Unteragent verarbeitet sie und liefert ein kurzes Ergebnis.
  - **Parallele Arbeit:** Mehrere unabhängige Teile können gleichzeitig laufen. Unteragenten, die nacheinander
    laufen, kosten Multi-Agenten-Tokens ohne Zeitgewinn.
  - **Getrennte Tools oder Berechtigungen:** Ein Schritt braucht Tools, die der Hauptagent nicht haben soll, oder
    umgekehrt.
  - **Zu viele Tools oder widersprüchliche Anweisungen** lassen den Hauptagenten schlecht wählen, und
    **Laden aufschieben** für MCP-Tools behebt es nicht.
- **Übergabe** (das Gespräch wechselt zu einem anderen Agenten): nur, wenn der Spezialist direkt mit dem Nutzer
  sprechen muss. Sonst lieber ein Unteragent, damit der Hauptagent das Gespräch behält.
- **Eigener Agent:** verschiedene Nutzergruppen mit unterschiedlichen Berechtigungen oder Datenzugriffen, eine feste
  Modellvorgabe oder eine andere Rolle für ein externes Publikum.

Trifft nichts davon zu: ein Agent plus Skills.

## Schritt 4: Den Bauplan schreiben

Gib dem Nutzer einen Bauplan mit genau den Feldern aus **Agenten erstellen**:

```markdown
**Name:** …
**Beschreibung:** Ein Satz: was der Agent tut und für wen (erscheint im Agenten-Marktplatz).
**KI Modell:** … (Grund: z. B. ein stärkeres Modell für Analysen, ein schnelleres für einfaches Weiterleiten)
**Anweisungen:** (siehe unten)
**Tools:**
- MCP-Server: <Server> mit diesen Tools: … (Laden aufschieben an für Server mit vielen Tools)
- Nativ: Code ausführen / Dateisuche / Nutzer fragen / Erinnerung / Artefakte (nur, was nötig ist, mit Grund)
**Dateikontext / Dateisuche:** welche Dateien und warum
**Skills:** Selected: <Skill>, <Skill> (oder All)
**Unteragenten / Übergaben:** <Agent> für <Aufgabe>, mit Grund aus Schritt 3 (oder: keine)
**Gesprächseinstiege:** 3–4 echte Beispielanfragen
**Maximale Agenten-Schritte:** nur, wenn der Standard für lange Abläufe zu niedrig ist
```

### Anweisungen des Agenten

Halte sie kurz: Sie stehen in jeder Nachricht im Kontext. Abläufe gehören in Skills.

```markdown
Du bist <Name>, <Rolle> für <Nutzer>.

## So arbeitest du
- Nutze deine Tools, statt Werte, Fakten oder Dateiinhalte zu raten. Kannst du etwas nicht prüfen, sag es.
- Ist eine Anfrage unklar, frag mit `ask_user_question`, statt Annahmen zu treffen.
- Bevor du etwas sendest, löschst oder fremde Daten änderst, hol dir die Bestätigung des Nutzers.
- Sobald eine Aufgabe zur Beschreibung eines Skills passt, lade diesen Skill und folge ihm.

## Deine Tools
- **<MCP-Server>:** wofür er da ist, je eine Zeile.

## Delegation (nur, wenn es Unteragenten gibt)
Gib <Aufgabe> an den Unteragenten **<Name>**. Gib ihm eine präzise Frage mit Kontext und arbeite mit seinem
Ergebnis weiter.

## Antworten
Sprache, Format, Quellenangaben, wohin Dateien gehen.
```

### Anweisungen für Unteragenten

Die Ausgabe eines Unteragenten liest ein anderer Agent, kein Mensch. Seine Anweisungen sagen: keine Begrüßung oder
Schlussworte, bei der Aufgabe bleiben und das Ergebnis in einer festen Struktur liefern (Zusammenfassung, Befunde mit
Quellen, offene Punkte). Gib ihm nur die Tools, die er braucht.

## Schritt 5: Testen

1. Führ die 5–10 Beispielanfragen aus Schritt 1 mit der neuen Einrichtung aus und schau, wie der Agent gearbeitet
   hat, nicht nur auf die Antwort: richtiger Skill geladen, richtige Tools, keine unnötigen Fragen, Bestätigung vor
   Nebenwirkungen.
2. Erwägst du einen zusätzlichen Unteragenten oder Agenten, führ dieselben Anfragen mit und ohne ihn aus und behalte
   ihn nur, wenn die Ergebnisse deutlich besser sind. Führ jede Anfrage mehr als einmal aus; die Ergebnisse
   schwanken.
3. Behebe die Ursache an der richtigen Stelle: falscher Ablauf → Skill; falsche Tool-Wahl → Tool-Beschreibungen,
   weniger Tools oder Laden aufschieben; falscher Ton oder Umfang → Anweisungen.

## Regeln

- **Empfehlen statt überbauen.** Sag klar, wenn der Plan des Nutzers mehr Agenten hat als nötig, und warum.
- **Nur nennen, was es gibt.** Biete nur MCP-Server, Tools und Skills an, die du in deiner Tool-Liste siehst oder
  die der Nutzer bestätigt; für alles andere sag, dass ein Administrator es freischalten muss.
- **Minimale Rechte.** Gib jedem Agenten und Unteragenten nur die Tools, die er braucht, und verlange eine
  Bestätigung vor dem Senden, Löschen oder Ändern fremder Daten.
- **Keine Geheimnisse** (Passwörter, API-Schlüssel) in Anweisungen oder Skills.
- **Das Teilen** eines Agenten mit Kollegen kann eine Rollenberechtigung erfordern; die Administratoren legen sie in
  companyADMIN fest.
