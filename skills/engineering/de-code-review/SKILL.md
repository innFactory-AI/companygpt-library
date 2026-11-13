---
name: de-code-review
description: Strukturiertes Code-Review — prüft auf Bugs, Sicherheitsprobleme, Performance-Regressionen und Style-Verstöße mit umsetzbarem Feedback. Verwende ihn, wenn du einen PR prüfst, einen Codeabschnitt auditierst oder eine zweite Meinung zu deiner Implementierung brauchst. Auslösen mit "diesen Code reviewen", "diesen PR prüfen", "was ist hier falsch".
---

# Code-Review-Skill

Prüfe Codeänderungen auf Bugs, Sicherheitsprobleme, Performance-Regressionen und Style-Verstöße. Der Skill erzeugt priorisiertes, umsetzbares Feedback, das ein Entwickler von oben nach unten abarbeiten kann. Den Code oder das Diff gibst du selbst an oder ziehst ihn aus einer angebundenen Quelle.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Git-Provider über MCP** (z. B. GitHub, GitLab, Bitbucket) | PR-Diffs, Commit-Historie, verknüpfte Issues |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear, Asana) | Ticket oder Issue, das die Änderung adressiert |
| **companyRAG / Datei-Upload** | Interne Style Guides, ADRs, Security-Richtlinien |

> **Keine angebundene Quelle?** Gib den Code oder das Diff im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Review-Workflow

Führe diese sieben Schritte für jedes Review der Reihe nach aus. Überspringe keine Schritte — ein Review, das einen Style-Nit findet, aber eine Sicherheitslücke übersieht, ist gescheitert.

### Schritt 1: Kontext verstehen

Bevor du eine einzige Codezeile liest, kläre:

1. Zweck: Was macht diese Änderung? Lies die PR-Beschreibung, das verknüpfte Ticket oder frage den Nutzer. Ein Review ohne Verständnis der Absicht kann einen Bug nicht von einem Feature unterscheiden.
2. Umfang: Wie groß ist die Änderung? Ein 10-zeiliger Bugfix und ein 500-zeiliges Feature erfordern unterschiedliche Review-Strategien.
3. Risikoprofil: Was könnte schiefgehen? Änderungen an Authentifizierung, Billing, Datenmodellen oder öffentlichen APIs tragen ein höheres Risiko als CSS-Anpassungen. Richte deine Aufmerksamkeit entsprechend aus.
4. Historie: Ist das ein neues Feature, ein Refactoring oder ein Hotfix? Hotfixes unter Zeitdruck verdienen besondere Sorgfalt bezüglich Abkürzungen, die zu langfristiger Schuld werden.

### Schritt 2: Auf Korrektheits-Bugs scannen

Lies den Code auf logische Fehler. Konzentriere dich auf:

| Bug-Kategorie | Worauf zu achten ist |
| --- | --- |
| **Off-by-one-Fehler** | Schleifengrenzen, Array-Indizierung, Pagination, Zaunpfahl-Bedingungen |
| **Null/Undefined-Behandlung** | Ungeschützte Dereferenzierungen, fehlendes Optional Chaining, fehlende Nil-Checks |
| **Typ-Mismatches** | Implizite Coercions, falsche Generic-Parameter, asymmetrische Serialisierung/Deserialisierung |
| **State-Management** | Race Conditions, veraltete Closures, fehlende State-Übergänge, geteilter mutabler State |
| **Fehlerbehandlung** | Verschluckte Exceptions, fehlende Fehlerpfade, Catch-Blöcke, die loggen, aber nicht weiterreichen |
| **Grenzbedingungen** | Leere Collections, Strings der Länge null, maximale Integer-Werte, Unicode-Sonderfälle |
| **Datenintegrität** | Partielle Writes ohne Transaktion, fehlendes Rollback bei Fehler, verwaiste Datensätze |
| **Nebenläufigkeit** | Fehlende Locks, Deadlock-Potenzial, nicht-atomare Read-Modify-Write-Sequenzen |

Verifiziere jeden vermuteten Bug, indem du den Ausführungspfad nachverfolgst — markiere nicht allein aufgrund eines Musters.

### Schritt 3: Sicherheit prüfen

Wende die relevanten OWASP-Top-10-Kategorien auf die Änderung an. Nicht jede Kategorie trifft auf jeden PR zu; konzentriere dich auf die, die für den geprüften Code relevant sind.

| OWASP-Kategorie | Code-Review-Check |
| --- | --- |
| **Injection** | Nutzereingaben fließen ohne Sanitisierung oder Parametrisierung in SQL, Shell-Befehle, OS-Calls, Template-Engines oder Log-Statements |
| **Broken Authentication** | Credential-Handling, Session-Management, Token-Validierung, Passwort-Speicherung, MFA-Bypass-Pfade |
| **Sensitive Data Exposure** | Secrets im Quellcode, PII in Logs, unverschlüsselte Speicherung, zu weitreichende API-Antworten, fehlende Redaction |
| **Broken Access Control** | Fehlende Autorisierungs-Checks, IDOR (direkte Objektreferenzen ohne Ownership-Validierung), Privilege-Escalation-Pfade |
| **Security Misconfiguration** | Permissive CORS, Debug-Modus in Produktion, Default-Credentials, ausführliche Fehlerantworten, die Internas preisgeben |
| **Insecure Deserialisation** | Untrusted Data in Objekte deserialisiert, fehlende Schema-Validierung bei externem Input |
| **Dependency-Schwachstellen** | Neue Dependencies ohne Prüfung, bekannte verwundbare Versionen, unnötige transitive Dependencies |

Prüfe zusätzlich auf STRIDE-Bedrohungen, wo relevant:

- Spoofing: Kann ein Angreifer einen legitimen Nutzer oder Dienst imitieren?
- Tampering: Können Request- oder Response-Daten in Transit oder at Rest verändert werden?
- Repudiation: Werden sicherheitsrelevante Aktionen mit ausreichendem Detailgrad für ein Audit geloggt?
- Information Disclosure: Leakt die Änderung Informationen über Fehlermeldungen, Timing oder Seitenkanäle?
- Denial of Service: Kann die Änderung missbraucht werden, um Ressourcen zu erschöpfen (unbegrenzte Queries, rekursive Calls, große Uploads)?
- Elevation of Privilege: Kann ein Nutzer mit geringeren Rechten Funktionalität mit höheren Rechten erreichen?

### Schritt 4: Performance bewerten

Bewerte die Änderung auf Performance-Regressionen. Konzentriere dich auf:

| Bereich | Was zu prüfen ist |
| --- | --- |
| **Algorithmische Komplexität** | O(n²) oder schlechter in Hot Paths, unnötige verschachtelte Schleifen, quadratische String-Konkatenation |
| **Datenbank-Queries** | N+1-Query-Muster, fehlende Indizes für neue Query-Muster, Full Table Scans, unbegrenzte Result Sets |
| **Speicherallokation** | Große Objekte in Schleifen erzeugt, unbegrenzte Caches, fehlendes Cleanup von Listenern oder Subscriptions |
| **Netzwerk-Calls** | Sequenzielle Calls, die parallelisiert werden könnten, fehlende Timeouts, Retry-Stürme, geschwätzige APIs |
| **Rendering** | Unnötige Re-Renders, Layout-Thrashing, große DOM-Updates, fehlende Virtualisierung bei langen Listen |
| **Caching** | Fehlendes Caching für teure Operationen, Cache-Invalidierungs-Bugs, unbegrenztes Cache-Wachstum |

Markiere nur Probleme, die bei der tatsächlichen Skalierung des Systems messbare Auswirkungen hätten. Eine quadratische Schleife über 5 Elemente ist kein Performance-Problem; eine quadratische Schleife über 50.000 schon.

### Schritt 5: Style und Wartbarkeit reviewen

Prüfe auf Lesbarkeit und langfristige Wartbarkeit:

- Naming: Kommunizieren Variablen-, Funktions- und Klassennamen ihre Absicht? Würde ein neues Teammitglied sie ohne Kontext verstehen?
- Funktionslänge: Funktionen, die zu viel tun. Wenn eine Funktion mehr als ein bis zwei Absätze zur Erklärung braucht, sollte sie wahrscheinlich zerlegt werden.
- Duplikation: Code, der bestehende Funktionalität dupliziert. Prüfe, ob bereits eine Utility- oder Shared-Funktion existiert.
- Abstraktionen: Liegen die Abstraktionen auf der richtigen Ebene? Über-Abstraktion (unnötige Interfaces, verfrühte Generalisierung) ist genauso schädlich wie Unter-Abstraktion.
- Kommentare: Sind komplexe Entscheidungen erklärt? Sind Kommentare korrekt (veraltete Kommentare sind schlimmer als keine)?
- Konsistenz: Folgt der Code den bestehenden Mustern in der Codebasis? Ein neues Muster für eine einzelne Datei erzeugt Wartungsaufwand.
- Testabdeckung: Sind neue Codepfade getestet? Sind die Grenzfälle aus Schritt 2 abgedeckt? Testen die Tests Verhalten (nicht Implementierungsdetails)?

Wenn ein Projekt-Style-Guide in einer companyRAG-Sammlung verfügbar ist, reviewe dagegen. Wenn kein Style-Guide geladen ist, reviewe gegen die etablierten Muster im umgebenden Code.

### Schritt 6: Operative Bereitschaft prüfen

Für Änderungen, die das Produktionsverhalten betreffen:

| Check | Details |
| --- | --- |
| **Observability** | Werden neue Codepfade auf angemessenen Leveln geloggt? Werden Metriken für Schlüsseloperationen emittiert? Kann das Team das in Produktion debuggen? |
| **Feature Flags** | Ist die Änderung hinter einem Feature Flag für sicheren Rollout gegated? Sollte sie es sein? |
| **Rückwärtskompatibilität** | Bricht die Änderung bestehende API-Verträge, Datenbankschemata oder Message-Formate? |
| **Migrationssicherheit** | Sind Datenbankmigrationen reversibel? Kann die Migration laufen, während der alte Code noch Traffic bedient? |
| **Konfiguration** | Sind neue Konfigurationswerte dokumentiert? Haben sie sinnvolle Defaults? Werden Secrets über Umgebungsvariablen statt hartkodiert behandelt? |
| **Rollback-Plan** | Kann diese Änderung unabhängig zurückgenommen werden? Gibt es irreversible Seiteneffekte (Datenmigration, externe Benachrichtigungen)? |

### Schritt 7: Feedback verfassen

Strukturiere die Review-Ausgabe nach der Severity-Klassifizierung und dem Format unten.

## Severity-Klassifizierung

Jedes Finding muss klassifiziert werden. Reviews mit gemischter Severity ohne Klassifizierung zwingen den Autor zu raten, was wichtig ist.

| Severity | Definition | Aktion des Autors | Blockiert Merge? |
| --- | --- | --- | --- |
| **Critical** | Bug, der Datenverlust, eine Sicherheitslücke oder einen Produktionsausfall verursacht. Muss behoben werden. | Vor Merge beheben | Ja |
| **Major** | Signifikanter Bug, Performance-Regression oder fehlende Fehlerbehandlung, die unter realistischen Bedingungen Probleme verursacht. | Vor Merge beheben | Ja |
| **Minor** | Code-Qualitätsproblem, Style-Inkonsistenz oder Grenzfall, der vermutlich nicht bald Probleme verursacht, aber die Wartbarkeit verschlechtert. | Vor Merge beheben (bevorzugt) oder Follow-up-Ticket erstellen | Nein (Team-Ermessen) |
| **Suggestion** | Alternativer Ansatz, Refactoring-Gelegenheit oder Wissens-Kommentar. Kein Korrektheitsproblem. | Erwägen, diskutieren oder zurückstellen | Nein |

Wenn ein Review null Critical- oder Major-Findings erzeugt, sage das explizit — "Keine blockierenden Probleme gefunden" ist eine wertvolle Information.

## Review-Checkliste

Schnellreferenz-Checkliste, die den obigen Workflow verdichtet. Nutze sie als Pre-Submission-Check nach dem vollständigen Review.

### Korrektheit

- Logik behandelt alle erwarteten Input-Typen und Grenzfälle
- Fehlerpfade sind behandelt und getestet
- State-Übergänge sind vollständig (keine unmöglichen/verwaisten States)
- Nebenläufiger Zugriff ist sicher, wo zutreffend

### Sicherheit

- Nutzereingaben werden vor Verwendung validiert und sanitisiert
- Autorisierungs-Checks existieren für alle geschützten Operationen
- Keine Secrets, Credentials oder PII im Quellcode oder in Logs
- Neue Dependencies sind geprüft und notwendig

### Performance

- Keine N+1-Queries oder unbegrenzte Result Sets
- Algorithmische Komplexität im Hot Path ist bei Produktionsskalierung akzeptabel
- Netzwerk-Calls haben Timeouts und Fehlerbehandlung
- Ressourcen-Cleanup existiert (Listener, Connections, File Handles)

### Wartbarkeit

- Namen sind klar und konsistent mit den Codebasis-Konventionen
- Funktionen haben eine einzelne, verständliche Verantwortung
- Keine unnötige Duplikation bestehender Utilities
- Tests decken neue Codepfade und Grenzfälle ab

### Operations

- Logging und Metriken reichen für Produktions-Debugging aus
- Datenbankmigrationen sind rückwärtskompatibel und reversibel
- Konfigurationsänderungen sind mit sinnvollen Defaults dokumentiert
- Änderung kann unabhängig zurückgerollt werden

## Feedback-Format

Verwende für jedes Finding diese Struktur:

```
### [Severity]: [Kurztitel]

**Datei**: [pfad/zur/datei.ext], Zeile [N]
**Kategorie**: [Korrektheit / Sicherheit / Performance / Style / Operations]

**Problem**: [Was falsch ist und warum es wichtig ist. Sei spezifisch — "das könnte null sein" ist weniger nützlich als "request.user ist undefined, wenn die Auth-Middleware auf öffentlichen Routes umgangen wird."]

**Vorschlag**: [Konkreter Fix oder Ansatz. Zeige ein Code-Snippet, wenn es die Absicht verdeutlicht.]

**Beleg**: [Wie du das identifiziert hast — verfolge den Ausführungspfad, referenziere die Dokumentation oder zitiere den konkreten Input, der das Problem auslöst.]
```

### Feedback-Prinzipien

- Sei spezifisch: Referenziere exakte Zeilen, Variablennamen und Ausführungspfade. "Diese Funktion ist verwirrend" ist nicht umsetzbar.
- Erkläre das Warum: Verknüpfe jedes Finding mit einer konkreten Konsequenz — einem Crash, einer Sicherheitslücke, einem Wartungsaufwand, einer Performance-Regression bei Skalierung.
- Vorschlagen, nicht diktieren: Gib einen empfohlenen Fix, erkenne aber an, wenn mehrere Ansätze existieren. Der Autor kennt die Codebasis besser.
- Trenne Blockierendes von Nicht-Blockierendem: Der Autor muss sofort wissen, welche Findings den Merge blockieren und welche Verbesserungsvorschläge sind.
- Würdige gute Arbeit: Wenn der Code einen kniffligen Fall gut behandelt, ein sauberes Muster demonstriert oder gute Testabdeckung zeigt, sage das. Reviews, die nur Probleme markieren, entmutigen gutes Engineering.
- Bündle verwandte Probleme: Wenn dasselbe Muster über mehrere Dateien wiederkehrt, markiere es einmal mit allen Fundstellen, statt denselben Kommentar zu wiederholen.

## Review-Sizing-Guide

Passe die Review-Tiefe an den Änderungsumfang an:

| Änderungsgröße | Geänderte Zeilen | Review-Strategie |
| --- | --- | --- |
| **Klein** | < 50 Zeilen | Vollständiges Review, alle Schritte. Schnelle Bearbeitung erwartet. |
| **Mittel** | 50–300 Zeilen | Vollständiges Review. Extra Aufmerksamkeit auf Schritte 2–3 (Bugs und Sicherheit). |
| **Groß** | 300–1000 Zeilen | Vollständiges Review, kann aber mehrere Durchgänge brauchen. Erwäge, die Aufteilung der Änderung anzufragen. |
| **Sehr groß** | > 1000 Zeilen | Markiere die Größe selbst als Problem. Große PRs verbergen Bugs. Empfehle dringend eine Aufteilung. Reviewe in logischen Abschnitten, falls eine Aufteilung nicht machbar ist. |

## Leitplanken

- Behaupte niemals, ein Bug existiere, ohne den Ausführungspfad nachverfolgt zu haben. Kennzeichne unsichere Findings als [Vermutet — Ausführungspfad prüfen].
- Erfinde niemals Sicherheitslücken. Wende OWASP/STRIDE-Checks auf den tatsächlichen Code an. Wenn unbestätigt, notiere als [Potenzielles Risiko — Verifizierung erforderlich].
- Nimm niemals Code-Kontext an, der nicht gezeigt wird. Formuliere Annahmen explizit: "Unter der Annahme, dass der Aufrufer X validiert, bevor diese Funktion aufgerufen wird."
- Quellenkennzeichne Findings als [Aus Code], [Aus Style-Guide] oder [KI-Einschätzung — prüfen].

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um einen formatierten, sofort teilbaren Review-Bericht zu erhalten.
