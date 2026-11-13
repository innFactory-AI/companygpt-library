---
name: de-knowledge-article
description: Draft searchable, publish-ready knowledge base articles from resolved issues, workarounds, or FAQs. Use when closing a support ticket with a reusable solution, documenting a new process, or refreshing stale KB content. Trigger with "write KB article for", "turn this into a knowledge article", "document this solution".
---

# Knowledge-Article-Skill

Erstelle durchsuchbare Knowledge-Base-Artikel aus gelösten Incidents, Workarounds oder FAQs. Der Skill folgt KCS-Prinzipien — Wissen wird als Nebenprodukt der Problemlösung festgehalten. Die technischen Inhalte kommen von dir, aus gelösten Tickets oder aus angebundenen Quellen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **ITSM / KB über MCP** (z. B. ServiceNow, Confluence, SharePoint) | Gelöste Tickets, bestehende Artikel, Resolution-Notizen, KB-Struktur |
| **companyRAG-Sammlungen** | Interne Runbooks, Prozessdokumentation, frühere Lösungen |
| **Datei-Upload** | Ticket-Exporte, Screenshots, Konfigurationsauszüge, Mailverläufe |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Artikeltyp klassifizieren

Klassifiziere den Artikel vor dem Schreiben. Der Typ bestimmt Struktur, Tonalität und erwartete Inhalte.

| Typ | Zweck | Wann verwenden | Typische Länge |
| --- | --- | --- | --- |
| **How-To** | Schritt-für-Schritt-Anleitung zur Erledigung einer Aufgabe | Nutzer muss eine konkrete Aktion ausführen (einrichten, konfigurieren, aktivieren, migrieren) | 300–800 Wörter |
| **Troubleshooting** | Ein konkretes Problem diagnostizieren und beheben | Nutzer stößt auf einen Fehler, unerwartetes Verhalten oder einen Ausfall | 400–1000 Wörter |
| **Reference** | Faktische Informationen zu einem System, Feature oder einer Richtlinie | Nutzer muss Spezifikationen, Limits, Berechtigungen oder Konfigurationsoptionen nachschlagen | 200–600 Wörter |
| **FAQ** | Antworten auf häufig gestellte Fragen zu einem Thema | Mehrere Nutzer stellen dieselbe Frage; Onboarding- oder Launch-Szenarien | 200–500 Wörter |

Wenn das Quellmaterial zu mehreren Typen passt, teile es in separate Artikel auf, statt einen Hybrid zu erstellen. Ein Troubleshooting-Artikel, der Setup-Schritte voraussetzt, sollte auf einen How-To-Artikel verlinken, statt sie einzubetten.

---

## Artikelvorlagen

### How-To-Artikel

```
# How to [Aktion] [Objekt]

## Überblick
[1–2 Sätze: Wobei dieser Artikel dem Nutzer hilft und wann er ihn braucht.]

## Voraussetzungen
- [Erforderliche Zugriffe, Berechtigungen oder Rollen]
- [Erforderliche Softwareversionen oder Konfigurationen]
- [Erforderliche vorherige Schritte — auf andere Artikel verlinken, falls zutreffend]

## Schritte

### Schritt 1: [Aktionsverb] [Objekt]
[Anweisung. Eine Aktion pro Schritt. Erwartetes Ergebnis angeben.]

### Schritt 2: [Aktionsverb] [Objekt]
[Anweisung.]

> **Hinweis:** [Bedingte Information — nur einfügen, wenn ein Schritt eine häufige Variante oder Stolperfalle hat.]

### Schritt 3: [Aktionsverb] [Objekt]
[Anweisung.]

## Verifikation
[Wie der Nutzer bestätigt, dass die Aufgabe erfolgreich abgeschlossen wurde. Konkretes beobachtbares Ergebnis.]

## Verwandte Artikel
- [Link zu verwandten How-To-, Troubleshooting- oder Reference-Artikeln]
```

### Troubleshooting-Artikel

```
# [Fehlermeldung / Symptombeschreibung]

## Symptome
- [Beobachtbares Symptom 1 — was der Nutzer sieht, exakter Fehlertext falls zutreffend]
- [Beobachtbares Symptom 2]

## Betroffene Systeme
- [Produkt, Service oder Komponente]
- [Betroffene Version(en), falls relevant]
- [Umgebung: Produktion, Staging, spezifisches OS/Browser]

## Ursache
[Kurze Erklärung, was das Problem verursacht. Technisch genug, um nützlich zu sein, einfach genug für die Zielgruppe.]

## Lösung

### Option A: [Primäre Lösung — am häufigsten oder am zuverlässigsten]
1. [Schritt]
2. [Schritt]
3. [Verifikationsschritt]

### Option B: [Alternative Lösung — falls Option A nicht greift]
1. [Schritt]
2. [Schritt]
3. [Verifikationsschritt]

## Workaround
[Falls noch keine dauerhafte Lösung existiert: temporärer Workaround mit Hinweis auf etwaige Einschränkungen.]

## Prävention
[Wie sich dieses Problem künftig vermeiden lässt, falls zutreffend.]

## Verwandte Artikel
- [Links]
```

### Reference-Artikel

```
# [System/Feature/Komponente] Reference

## Überblick
[1–2 Sätze: Was diese Referenz abdeckt.]

## [Kategorie 1]

| Parameter | Wert | Hinweise |
|-----------|-------|-------|
| [Name] | [Wert] | [Beschränkungen, Defaults, Edge Cases] |

## [Kategorie 2]

[Strukturierte Informationen — Tabellen, Listen oder Definitionsblöcke je nach Inhaltstyp.]

## Berechtigungen / Zugriff

| Rolle | Zugriffslevel | Hinweise |
|------|-------------|-------|
| [Rolle] | [read/write/admin/none] | [Bedingungen] |

## Verwandte Artikel
- [Links]
```

### FAQ-Artikel

```
# [Thema] — Häufig gestellte Fragen

## [Frage 1 — exakt so formuliert, wie Nutzer sie stellen]
[Antwort. Direkt, prägnant. Für komplexe Themen auf Detailartikel verlinken, statt vollständige Erklärungen einzubetten.]

## [Frage 2]
[Antwort.]

## [Frage 3]
[Antwort.]

## Brauchst du weitere Hilfe?
[Eskalationspfad: Support-Kanal, Team-Kontakt oder Link zur Ticketerstellung.]
```

---

## Schreibrichtlinien

### Strukturregeln

1. Titel = Sprache des Nutzers. Formuliere den Titel so, wie ein Nutzer danach suchen würde. "How to reset MFA" statt "Multi-Factor Authentication Token Regeneration Procedure". Triff das Vokabular, das deine Nutzer tatsächlich verwenden.
2. Ein Artikel, ein Thema. Wenn du im Titel eine Konjunktion ("und", "oder") brauchst, erwäge, in zwei Artikel aufzuteilen.
3. Mit der Antwort beginnen. Stelle die kritischste Information an den Anfang. Troubleshooting-Artikel starten mit der Lösung, nicht mit der Theorie. Wer nach Lösungen scannt, soll sie ohne Scrollen finden.
4. Eine Aktion pro Schritt. Jeder nummerierte Schritt sollte eine einzelne, verifizierbare Aktion sein. "Klicke auf Einstellungen, dann zu Sicherheit navigieren, dann MFA aktivieren" sind drei Schritte, nicht einer.
5. Verifikation einbauen. Jeder How-To- und Troubleshooting-Artikel endet damit, wie der Nutzer den Erfolg bestätigt. "Du solltest [konkretes Ergebnis] sehen" ist besser als "Der Vorgang ist abgeschlossen".
6. Verlinken, nicht duplizieren. Wenn Voraussetzungsschritte in einem anderen Artikel existieren, verlinke darauf. Duplizierter Inhalt wird mit der Zeit inkonsistent.

### Sprache und Tonalität

- Aktiv und Imperativ für Anweisungen: "Klicke auf Speichern" statt "Der Speichern-Button sollte angeklickt werden"
- Direkte Anrede des Lesers: "Du kannst konfigurieren..." statt "Nutzer können konfigurieren..."
- Präsens für Systemverhalten: "Das System zeigt einen Fehler an" statt "Das System wird einen Fehler anzeigen"
- Exakte UI-Labels in Fettschrift: Klicke auf Einstellungen > Sicherheit > MFA aktivieren
- Exakte Fehlermeldungen in Code-Formatierung: Error: SAML assertion expired
- Kein Fachjargon ohne Definition für die Zielgruppe. Ein Artikel für Endnutzer sollte keine Vertrautheit mit Backend-Terminologie voraussetzen. Ein Artikel für Sysadmins darf das.
- Keine relativierende Sprache: Entferne "einfach", "nur", "problemlos" — wäre es einfach, bräuchten Nutzer den Artikel nicht.

### Suchoptimierung für die interne KB

Interne Knowledge Bases setzen auf Keyword-Matching und Metadaten. Optimiere auf Auffindbarkeit:

1. Titel: Nimm die exakte Aktion oder Fehlermeldung auf, nach der Nutzer suchen. Stelle die Schlüsselbegriffe nach vorn.
2. Synonyme und alternative Formulierungen: Füge einen Metadaten-Abschnitt oder einen einleitenden Absatz ein, der alternative Suchbegriffe natürlich verwendet. Geht es um "MFA zurücksetzen", erwähne "Zwei-Faktor-Authentifizierung", "2FA", "Authenticator-App" im Überblick.
3. Fehlercodes und exakte Meldungen: Nimm die wortgetreue Fehlerzeichenfolge auf, die Nutzer in die Suche kopieren würden. In Code-Formatierung zur Klarheit.
4. Tags/Labels: Schlage Kategorie-Tags vor anhand von: Produktbereich, Nutzerrolle, Problemtyp, betroffene Plattform.
5. Querverweise: Jeder Artikel sollte auf 2–5 verwandte Artikel verlinken. Das verbessert Auffindbarkeit und Navigation.

### Metadaten-Block

Füge diese Metadaten am Anfang jedes Artikels für die Aufnahme in die KB-Plattform ein:

```
Article ID: [automatisch generiert oder manuell zugewiesen]
Type: [How-To / Troubleshooting / Reference / FAQ]
Product/Service: [Name]
Audience: [End User / IT Admin / Developer / All]
Tags: [kommagetrennt]
Created: [Datum]
Last Reviewed: [Datum]
Review Cycle: [quarterly / semi-annual / annual / on-change]
Owner: [Team oder Person]
Status: [Draft / In Review / Published / Archived]
```

---

## Qualitäts-Checkliste für Artikel

Vor dem Veröffentlichen prüfen:

- Titel entspricht der Art, wie Nutzer nach dem Thema suchen
- Artikeltyp ist korrekt und die Vorlage wird eingehalten
- Voraussetzungen sind gelistet (oder als "keine" angegeben)
- Schritte sind nummeriert, einzelaktionsbasiert und verifizierbar
- Verifikations-/Bestätigungsschritt ist enthalten
- Fehlermeldungen und UI-Labels sind exakt (kopiert, nicht umformuliert)
- Screenshots oder Beispiele sind aktuell (falls referenziert)
- Kein duplizierter Inhalt — stattdessen Links verwendet
- Metadaten-Block ist vollständig
- 2–5 verwandte Artikel sind verlinkt
- Review-Datum ist je nach Inhaltsvolatilität gesetzt
- Tonalität passt zur Zielgruppe

---

## Artikel-Lifecycle-Management

### Review-Auslöser

Artikel sollten überprüft werden, wenn:

- Sich das zugrunde liegende System, Feature oder der Prozess ändert
- Ein Support-Ticket auf den Artikel verweist und die Lösung nicht funktioniert hat
- Das geplante Review-Datum erreicht ist
- Artikel-Feedback (Daumen runter, Kommentare) auf ein Problem hinweist

### Archivierungskriterien

Archiviere (lösche nicht) Artikel, wenn:

- Das Produkt oder Feature außer Betrieb genommen wurde
- Das Problem durch eine Systemänderung dauerhaft gelöst ist (als "Resolved — no longer applicable" markieren und archivieren)
- Ein neuerer Artikel diesen ersetzt (vor dem Archivieren einen Redirect oder "superseded by"-Link ergänzen)

---

## Leitplanken

- Erfinde niemals Lösungen. Alle Lösungsschritte, Konfigurationen und Befehle kommen aus der Eingabe des Nutzers oder aus verifiziertem Wissen. Frage nach fehlenden Schritten, statt plausibel klingende Anweisungen zu generieren.
- Erfinde niemals Fehlermeldungen, UI-Labels oder Menüpfade. Diese müssen wortgetreu aus dem Quellsystem stammen.
- Nimm niemals Softwareversionen oder Plattformdetails an. Frage nach der Version; generiere keine versionsspezifischen Anweisungen aus Trainingsdaten.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Quellmaterial]`, `[Artikelvorlage]` oder `[KI-Entwurf — vor Veröffentlichung prüfen]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um einen formatierten, sofort teilbaren Artikel zu erhalten.
