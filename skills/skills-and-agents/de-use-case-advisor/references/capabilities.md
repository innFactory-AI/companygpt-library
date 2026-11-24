# companyGPT-Fähigkeiten

Wofür jeder Baustein da ist, wofür nicht, und was vorhanden sein muss. Eine App ist nur nutzbar, wenn sie für das
Unternehmen und den Nutzer freigeschaltet ist; dann erscheinen ihre Tools in der Tool-Liste des Agenten.

Inhalt: Chat- und Agenten-Funktionen · companyRAG · companyFILES · companyM365 · Office-Add-in · companyTRANSCRIBE ·
companyTRANSLATE · companyLEARN · Angebundene Systeme (MCP) · Automatisierung (n8n) · Skills und Agenten

## Chat- und Agenten-Funktionen

In companyGPT eingebaut, ohne App.

- **Chat:** Fragen, Texte, Zusammenfassungen, Ideen, Analyse angehängter Dateien. Wähl das Modell passend:
  stärkere Modelle für Analysen und lange Dokumente, schnellere für einfache Aufgaben.
- **Datei-Upload:** Dateien im Chat für dieses Gespräch anhängen. Nicht dauerhaft und für andere nicht
  durchsuchbar.
- **File Context / File Search (im Agenten):** wenige Schlüsseldokumente, die der Agent immer sieht (File Context,
  kostet in jeder Nachricht Kontext), oder ein kleiner Dokumentenbestand, den er bei Bedarf durchsucht (File
  Search). Für viele oder sich ändernde Dokumente: companyRAG.
- **Run Code (Code-Ausführung):** Python in einer Sandbox ohne Netzwerkzugang, für Berechnungen, Datenanalyse,
  Diagramme und Massenbearbeitung von Dateien. Nicht überall verfügbar (Unternehmen, Rolle oder Nutzer können sie
  abschalten).
- **Websuche, Memory, Artifacts, `ask_user_question`:** je nach Agent und Einrichtung des Unternehmens.

## companyRAG

Suche im Unternehmenswissen über Dokumenten-Collections, und SQL über Tabellen.

- **Für:** viele Dokumente, die ein Team immer wieder durchsucht: Handbücher, Richtlinien, Verträge, Wikis,
  Projektordner, Produktdokumentation. Antworten kommen mit Quellen.
- **Quellen:** Upload in der companyRAG-App, SharePoint, Google Drive, Nextcloud, GitHub, Web-Crawl (welche, hängt
  von der Einrichtung ab). Collections werden mit ihrer Quelle synchron gehalten.
- **Datasets:** Tabellen (CSV/Excel), die mit SQL abgefragt werden, z. B. Preislisten, Bestände, Kennzahlen. Nur
  wo Datasets aktiviert sind.
- **Zugriff:** Jede Collection hat eigene Berechtigungen; der Nutzer durchsucht nur Collections, die er nutzen darf
  (`list_collections` zeigt sie).
- **Nicht für:** eine im Chat angehängte Datei (companyRAG kann Chat-Anhänge nicht indexieren), einmalige Fragen zu
  wenigen Dokumenten (einfach anhängen), Live-Daten aus Fachsystemen (MCP-Server).
- **Tools:** `list_collections`, `search_content`; Datasets: `execute_sql` und weitere Dataset-Tools.
- **Skills:** **de-ai-search**, **de-dataset**.
- **Voraussetzung:** eine Collection mit den richtigen Dokumenten, eingerichtet in der companyRAG-App von Nutzern
  mit der passenden Berechtigung oder von den Administratoren.

## companyFILES

Erstellt und liest Office-Dokumente. Erstellte Dateien kommen als normale Chat-Dateien zurück.

- **Für:** Word, Excel, PowerPoint, PDF (und ODT) neu oder aus Firmenvorlagen, PDF-Formulare ausfüllen, Formate
  umwandeln, Diagramme, angehängte Dokumente lesen, bestehende Dateien bearbeiten.
- **Vorlagen:** Firmenvorlagen (Briefkopf, Folienmaster, Berichtslayout) werden mit `list_templates` und
  `create_*_from_template` gefüllt.
- **Nicht für:** Dateien in OneDrive/SharePoint (companyM365), dauerhafte Suche über viele Dateien (companyRAG).
- **Tools (Beispiele):** `create_word`, `create_excel`, `create_powerpoint`, `read_word`, `read_excel`, `read_pdf`,
  `convert_document`, `list_templates`.
- **Skills:** **de-file-routing**, **de-word-odt**, **de-excel**, **de-powerpoint**, **de-pdf**, **de-templates**,
  **de-convert**, **de-charts-diagram**.

## companyM365

Das Microsoft 365 des Nutzers, in seinem Namen und mit seinen Berechtigungen.

- **Für:** Mail (suchen, lesen, Anhänge, Entwürfe, Antworten, Ordner, Regeln, Kategorien, freigegebene Postfächer),
  Kalender (Termine, freie Zeiten, Terminplanung), OneDrive- und SharePoint-Dateien (suchen, lesen, Excel-Bereiche,
  Freigabelinks), Teams-Nachrichten und -Chats (lesen), Transkripte von Teams-Besprechungen, OneNote, Planner- und
  To-Do-Aufgaben, Personen und Gruppen.
- **Sicherheit:** Mails werden als Entwurf angelegt; der Nutzer verschickt sie in Outlook. Änderungen an Kalendern,
  Aufgaben oder Dateien erst nach Bestätigung durch den Nutzer.
- **Nicht für:** automatischen Mailversand oder Posten in Teams, Daten anderer Personen, auf die der Nutzer keinen
  Zugriff hat.
- **Tools (Beispiele):** `search_emails`, `get_email`, `create_email_draft`, `list_upcoming_events`,
  `find_meeting_times`, `search_files`, `read_file`, `search_teams_messages`, `list_my_meeting_transcripts`,
  `create_planner_task`.
- **Voraussetzung:** von den Administratoren freigeschaltet; beim ersten Mal muss der Nutzer eventuell zustimmen.

## Office-Add-in

companyGPT als Seitenbereich in Word, Excel, PowerPoint und Outlook.

- **Für:** Arbeit am geöffneten Dokument oder an der geöffneten Mail: Text schreiben und umformulieren,
  formatieren, Tabellen und Diagramme in Excel, Folien ergänzen, eine Antwort in der geöffneten Mail entwerfen.
- **Nicht für:** eine neue, separate Datei zum Herunterladen (companyFILES).
- **Voraussetzung:** von den Administratoren ausgerollt (Microsoft 365 Admin Center).

## companyTRANSCRIBE

Audio und Video zu Text, als eigene App und im Chat.

- **Für:** Meetings, Interviews, Sprachmemos, Telefonate; Sprechererkennung (wer hat was gesagt); Export des
  Transkripts. Auch umgekehrt: Sprach-Audio (MP3) aus einem Text (Voiceover).
- **Im Chat:** `transcribe_chat_file` auf eine angehängte Audio-/Videodatei, dann `get_transcript`; Voiceover mit
  `create_voiceover`. Eine Transkription dauert Minuten.
- **Typische Kombination:** transkribieren → im Chat zusammenfassen oder Protokoll schreiben → companyFILES für die
  Word-Datei → companyM365 für den Mail-Entwurf an die Teilnehmer.
- **Nicht für:** Teams-Besprechungen, die schon ein Teams-Transkript haben (das liest companyM365).

## companyTRANSLATE

Übersetzung von Texten und Dokumenten, als eigene App und im Chat.

- **Für:** Texte und ganze Dokumente mit erhaltenem Layout (Word, PowerPoint, Excel, PDF, …), Glossare für
  Firmenbegriffe, Übersetzungsverlauf.
- **Tools:** `translate_text`, `translate_document`, `list_glossaries`, `list_languages`.
- **Nicht für:** Umformulieren oder Zusammenfassen (das macht der Chat), sehr kurze Texte, bei denen der Chat
  reicht.

## companyLEARN

Lernplattform: Kurse mit Kapiteln, Lektionen, Quizzen und Abschlussprüfung, direkt im Chat angezeigt.

- **Für Lernende:** Kurse finden, Lektionen und Quizze im Chat machen, den eigenen Fortschritt sehen
  (`learn_list_courses`, `learn_watch_lesson`, `learn_take_quiz`, `learn_my_progress`).
- **Für Kurs-Admins:** Kurse aus Dokumenten, companyRAG-Collections oder SharePoint-Inhalten erstellen,
  veröffentlichen, Personen zuweisen, Fortschritt auswerten (`learn_admin_*`-Tools).
- **Skill:** **de-course-authoring** (Admins).

## Angebundene Systeme (MCP-Server)

MCP (Model Context Protocol) ist der Weg, über den Agenten Tools für andere Systeme bekommen.

- **Für:** Live-Daten oder Aktionen in einem Fachsystem (CRM, ERP, Ticketsystem, interne Datenbanken,
  Spezialsoftware).
- **REST-APIs:** Hat das System eine REST-API mit OpenAPI-Beschreibung, können die Administratoren sie ohne
  Programmierung als MCP-Server anbinden (companyMCPROXY); jede API-Operation wird ein Tool. Auch für
  On-Premises-Systeme, die über das Firmennetz erreichbar sind.
- **Andere MCP-Server:** vorhandene MCP-Server von Herstellern können die Administratoren anbinden.
- **Voraussetzung:** immer die Administratoren (Anbindung, Zugangsdaten, welche Nutzer oder Agenten Zugriff
  bekommen).

## Automatisierung (n8n)

Workflows, die ohne Chat laufen, wenn das Unternehmen n8n nutzt.

- **Für:** Aufgaben nach Zeitplan oder bei einem Ereignis: jede Nacht, bei jeder neuen Mail oder jedem
  Formulareintrag, zwischen mehreren Systemen (z. B. „jedes neue Support-Ticket wird eingeordnet und zugewiesen“).
- **Nicht für:** Aufgaben, bei denen ein Mensch zwischendurch fragt, prüft und entscheidet: Das ist ein Chat, ein
  Skill oder ein Agent.
- **Voraussetzung:** n8n ist für das Unternehmen aktiviert; Workflows bauen Administratoren oder geschulte
  Power-User.

## Skills und Agenten

- **Skill:** eine wiederverwendbare Anleitung für eine wiederkehrende Aufgabe (Schritte, Regeln, Ausgabeformat).
  Jeder Agent mit dem Skill kann ihn nutzen; Nutzer starten ihn mit `$` im Chat. Bauen mit **de-create-skill**.
- **Agent:** ein fester Assistent mit Modell, Anweisungen, Tools, Dateien und Skills, mit einem Team teilbar, wenn
  erlaubt. Meist reicht ein Agent mit Skills. Entwerfen mit **de-agent-design**.
- **Fertige Skills und Agenten:** Die companyGPT-Library hat Skills für Dateien, Vertrieb, Marketing, HR,
  Engineering und mehr; die Administratoren können sie bereitstellen.
