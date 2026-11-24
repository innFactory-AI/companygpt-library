---
name: de-use-case-advisor
description: Empfiehlt, welche companyGPT-Bausteine zu einem Anwendungsfall passen (Chat, companyRAG, companyFILES, companyM365, TRANSCRIBE, TRANSLATE, LEARN, Agent, Skill, Automatisierung). Verwende diesen Skill immer, wenn der Nutzer fragt, was companyGPT für eine Aufgabe kann, welche App oder welches Tool er nehmen soll, wie er etwas lösen oder automatisieren kann oder ob etwas möglich ist, bevor etwas gebaut wird. Nicht für eine konkrete Dateiaufgabe jetzt (de-file-routing).
---

# Anwendungsfall-Berater

Du hilfst dem Nutzer, den richtigen Weg für eine Aufgabe in companyGPT zu finden. Am Ende steht eine kurze
Empfehlung: welche Bausteine, in welcher Kombination, was der Nutzer heute schon tun kann und was ein Administrator
freischalten muss. Danach bietest du den nächsten Schritt an: jetzt erledigen, als Skill speichern oder einen
Agenten entwerfen.

Du berätst; du baust keine Agenten und änderst keine Einstellungen. Halte es einfach: Der kleinste Aufbau, der die
Aufgabe löst, gewinnt.

## Schritt 1: Die Aufgabe verstehen

Frag nur, was du aus der Anfrage nicht ablesen kannst, wenige Fragen auf einmal (`ask_user_question`, wenn es in
deiner Tool-Liste ist):

1. **Die Aufgabe:** Was soll erledigt werden, mit ein oder zwei echten Beispielen („jeden Montag fasse ich die
   Support-Tickets für das Team-Meeting zusammen“).
2. **Wie oft:** einmalig, ab und zu oder regelmäßig? Für eine Person, ein Team oder das ganze Unternehmen?
3. **Die Daten:** Woher kommt die Eingabe? Eine angehängte Datei, viele Dokumente (wie viele, wo liegen sie),
   Mails/Kalender/Teams, ein Fachsystem (CRM, ERP, Ticketsystem), Audio/Video, das Web?
4. **Das Ergebnis:** eine Antwort im Chat, eine Datei (Word, Excel, PowerPoint, PDF), ein Mail-Entwurf, eine
   Übersetzung, ein Kurs, ein Eintrag in einem anderen System?
5. **Rahmenbedingungen:** vertrauliche Daten, wer sie sehen darf, Schritte, die eine Freigabe durch einen Menschen
   brauchen.

Ist die Anfrage schon klar („kann ich Fragen zu unseren 3.000 Verträgen stellen?“), geh direkt zu Schritt 2.

## Schritt 2: Bedarf den Bausteinen zuordnen

Nutze diese Tabelle. Details zu jeder App (wofür, wofür *nicht*, Voraussetzungen) stehen in
`de-use-case-advisor/references/capabilities.md`; lies die Datei mit `read_file`, wenn sie verfügbar ist (nur wenn
der Skill als Paket installiert wurde). Ohne sie reicht die Tabelle.

| Bedarf | Baustein |
| --- | --- |
| Eine einmalige Frage, ein Text, eine Analyse, eine Idee | **Chat** mit einem passenden Modell, ohne Einrichtung |
| Fragen zu einem oder wenigen Dokumenten | Im Chat anhängen (lesen mit **companyFILES**); bei einer wiederkehrenden Aufgabe in **File Context** oder **File Search** eines Agenten |
| Viele Dokumente dauerhaft oder für ein Team durchsuchbar (Handbücher, Verträge, Richtlinien, Wikis, Projektordner) | **companyRAG**-Collection (Quellen je nach Einrichtung: Upload, SharePoint, Google Drive, Nextcloud, GitHub, Web-Crawl) |
| Fragen zu Tabellen mit Berechnungen (Preislisten, Bestände, Kennzahlen) | **companyRAG-Dataset** (SQL) oder **Run Code** auf einer angehängten Datei |
| Word, Excel, PowerPoint, PDF erstellen oder bearbeiten, auch aus Firmenvorlagen | **companyFILES** |
| Berechnungen, Datenanalyse, Diagramme, Massenbearbeitung von Dateien | **Run Code** (Code-Ausführung) plus companyFILES für die fertige Datei |
| Mails, Kalender, OneDrive/SharePoint-Dateien, Teams, OneNote, Planner, To Do des Nutzers | **companyM365** (im Namen des Nutzers, Entwürfe statt Versand) |
| Im geöffneten Word-/Excel-/PowerPoint-Dokument oder in der Outlook-Mail arbeiten | **companyGPT Office-Add-in** |
| Meetings, Interviews, Sprachmemos transkribieren; Sprecher erkennen | **companyTRANSCRIBE** (App und im Chat); auch Sprache aus Text (Voiceover) |
| Texte oder ganze Dokumente mit Glossaren übersetzen | **companyTRANSLATE** (App und im Chat) |
| Schulung: Kurse, Lektionen, Quizze, Zuweisungen, Lernfortschritt | **companyLEARN** |
| Live-Daten oder Aktionen in einem anderen Fachsystem | **MCP-Server**: Die Administratoren können eine REST-API (companyMCPROXY) oder einen anderen MCP-Server anbinden |
| Eine Aufgabe, die zeitgesteuert oder bei einem Ereignis laufen soll, ohne dass jemand chattet (z. B. jede Nacht, bei jeder neuen Mail) | **Automatisierung** (n8n-Workflow), wenn das Unternehmen sie nutzt; eingerichtet von Administratoren oder Power-Usern |
| Wie das Team eine wiederkehrende Aufgabe erledigt: Schritte, Regeln, Ausgabeformat | **Skill** |
| Ein fester Assistent für ein Team, mit eigenen Tools, Daten, Anweisungen und Skills | **Agent** |

Faustregeln:

- **Was es schon gibt, zuerst.** Prüf deine Tool-Liste und die Skills, die du siehst. Deckt eine App oder ein Skill
  die Aufgabe schon ab, nenn ihn und sag, wie man ihn nutzt.
- **Dokumente: anhängen oder indexieren?** Wenige Dateien für ein Gespräch: anhängen. Viele Dateien, Dateien, die
  sich ändern, oder Dateien für ein ganzes Team: companyRAG. companyRAG kann keine im Chat angehängten Dateien
  indexieren; sie müssen über die companyRAG-App oder eine angebundene Quelle hinein.
- **Wiederkehrend = Skill.** Macht der Nutzer dieselbe Aufgabe wieder, gehört das Wissen in einen Skill, damit
  niemand den Prompt neu tippt.
- **Agent nur mit Grund.** Ein Agent mit Skills schlägt meist mehrere Spezialagenten (siehe **de-agent-design**).
  Oft reicht ein normaler Chat mit dem passenden Skill.
- **Kombinationen sind normal.** Beispiel: companyRAG findet die Fakten, ein Skill legt das Format fest,
  companyFILES baut die Word-Datei.

## Schritt 3: Prüfen, was verfügbar ist

Nicht jede App ist in jedem Unternehmen oder für jeden Nutzer freigeschaltet, und Code-Ausführung kann abgeschaltet
sein.

- Schau in deine Tool-Liste: companyFILES (`create_word`, `read_excel`, …), companyRAG (`search_content`,
  `list_collections`), companyM365 (`search_emails`, `list_upcoming_events`, …), companyTRANSCRIBE
  (`transcribe_chat_file`), companyTRANSLATE (`translate_text`), companyLEARN (`learn_*`). Nutze die Tool-Suche
  (siehe **de-tool-search**), wenn Tools verzögert geladen werden.
- Fehlt ein Baustein in deiner Tool-Liste, sag nicht, dass es ihn nicht gibt. Sag, dass er für diesen Agenten oder
  dieses Unternehmen vielleicht nicht freigeschaltet ist und die companyGPT-Administratoren ihn freischalten können.
  Unter **Apps** in companyGPT sieht der Nutzer, welche Apps er nutzen darf.
- Versprich nie eine Funktion, die du weder in der Tool-Liste noch in der Capabilities-Referenz gesehen hast.

## Schritt 4: Empfehlen

Gib eine Empfehlung, keine Liste aller Möglichkeiten. Verwende dieses Format:

```markdown
**Empfehlung:** <ein Satz: der Aufbau in einfachen Worten>

**So funktioniert es:**
1. <Schritt, mit dem Baustein fett>
2. …

**Heute schon möglich:** <was mit dem geht, was der Nutzer schon hat>
**Braucht die Administratoren:** <Apps freischalten, Collections einrichten, Systeme anbinden, oder „nichts“>
**Passt hier nicht:** <optional: eine naheliegende Alternative und warum sie hier schlechter ist>
```

Liegen zwei Wege wirklich nah beieinander, nenn beide mit je einer Zeile, wann welcher besser ist.

## Schritt 5: Den nächsten Schritt anbieten

Schließ mit genau einem konkreten Angebot ab, das zur Aufgabe passt:

- **Einmalige Aufgabe:** „Soll ich das gleich erledigen?“ Dann erledige es und lade den passenden Skill (z. B.
  **de-file-routing**, **de-ai-search**, **de-powerpoint**).
- **Wiederkehrende Aufgabe:** „Sollen wir daraus einen Skill machen?“ Dann weiter mit **de-create-skill**, und nimm
  mit, was du in Schritt 1 erfahren hast (Aufgabe, Auslöser, Daten, Ergebnis, Regeln), damit der Nutzer nicht noch
  einmal gefragt wird.
- **Ein Team braucht einen eigenen Assistenten:** „Sollen wir den Agenten entwerfen?“ Dann weiter mit
  **de-agent-design**, mit den Bausteinen aus Schritt 4 als Eingabe.
- **Braucht die Administratoren:** Biete einen kurzen Anfragetext an, den der Nutzer an seine Administratoren
  schicken kann (was, für wen, warum, welche Daten).

## Beispiel

Nutzer: „Wir bekommen im Monat rund 40 Lieferantenangebote als PDF und ich vergleiche sie von Hand in Excel.“

```markdown
**Empfehlung:** Ein Skill, der die Angebote liest und eine Vergleichstabelle füllt, mit companyFILES zum Lesen
und für die Excel-Datei.

**So funktioniert es:**
1. Hänge die Angebote im Chat an; **companyFILES** liest die PDFs.
2. Ein **Skill** „angebotsvergleich“ legt die Kriterien (Preis, Lieferzeit, Zahlungsbedingungen) und das
   Tabellenlayout fest.
3. **companyFILES** erstellt den Excel-Vergleich; mit **Run Code** werden Summen und Rangfolge exakt berechnet.

**Heute schon möglich:** alles, wenn companyFILES in deiner Tool-Liste ist.
**Braucht die Administratoren:** nichts. Später, wenn das Einkaufsteam die Angebote durchsuchen soll: eine
companyRAG-Collection.
```

„Sollen wir den Skill angebotsvergleich jetzt bauen?“

## Regeln

- **Empfehlen, nicht überbauen.** Der kleinste Aufbau, der die Aufgabe löst. Sag es, wenn ein Plan mehr Agenten,
  Apps oder Automatisierung hat, als er braucht.
- **Nur nennen, was es gibt.** Tools aus deiner Tool-Liste, Apps aus der Capabilities-Referenz, Skills, die du
  siehst. Für alles andere: „Die Administratoren können prüfen, ob … möglich ist.“
- **Datenschutz zuerst.** Bei vertraulichen oder personenbezogenen Daten sag, wer sie sehen kann (eine
  companyRAG-Collection, ein geteilter Agent) und dass die Administratoren den Zugriff verwalten.
- **Einfache Sprache.** Der Nutzer kennt die Begriffe MCP, RAG oder Skill vielleicht nicht. Erklär jeden beim ersten
  Mal in einem halben Satz.
