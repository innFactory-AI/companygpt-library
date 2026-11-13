---
name: de-debugging
description: Arbeite einen systematischen Debugging-Workflow mit Hypothesenbildung, Isolationstests und Ursachenanalyse durch. Verwende ihn, wenn du an einem Bug feststeckst, unerwartetes Verhalten untersuchst oder ein Produktionsproblem diagnostizierst. Auslösen mit "hilf mir beim Debuggen", "warum passiert das", "untersuche diesen Fehler".
---

# Debugging-Skill

Schließe über eine disziplinierte Methodik zur Diagnose von Software-Defekten vom Symptom auf die Ursache. Das verhindert die zwei häufigsten Debugging-Fehler: planlose Code-Änderungen ohne Verständnis sowie das Beheben von Symptomen, während die Ursache bestehen bleibt. Logs, Fehler und Code kommen von dir, aus einer angebundenen MCP-Quelle, aus companyRAG-Sammlungen oder per Datei-Upload.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Error-Tracking / Monitoring über MCP** (z. B. Sentry, Datadog) | Fehlermeldungen, Stack Traces, Metriken, Latenz- und Fehlerraten-Trends |
| **Repository über MCP** (z. B. GitHub) | Quellcode, jüngste Änderungen, Commit-Historie, Änderungsgrenze (Deployment-Boundary) |
| **companyRAG / Datei-Upload** | Eingefügte Logs, Stack Traces, Quelldateien, Runbooks, Notizen früherer Incidents |

> **Keine angebundene Quelle?** Gib Logs, Fehlermeldungen oder den Code im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Debugging-Workflow

Folge diesen sieben Phasen. Die Disziplin liegt darin, keine Phase zu überspringen — die Versuchung, vom Symptom direkt zur Lösung zu springen, ist die häufigste Ursache für gescheitertes Debugging.

### Phase 1: Den Bug reproduzieren

Ein Bug, den du nicht reproduzieren kannst, ist ein Bug, dessen Behebung du nicht verifizieren kannst.

**Reproduktions-Checkliste:**

1. Das exakte Symptom identifizieren : Welches beobachtbare Verhalten ist falsch? Trenne das Symptom ("Seite zeigt Fehler 500") von der vermuteten Ursache ("die Datenbank ist down"). Arbeite mit dem Symptom.
2. Reproduktionsschritte festlegen : Was ist die minimale Abfolge von Aktionen, die das Symptom auslöst? Lass alles Unzusammenhängende weg.
3. Konsistenz bestimmen : Tritt es jedes Mal auf (deterministisch) oder sporadisch (nicht-deterministisch)? Sporadische Bugs erfordern zusätzliche Datensammlung vor der Hypothesenbildung.
4. Die Umgebung identifizieren : Wo tritt es auf? Nur in Produktion? Staging? Lokal? Der Unterschied schränkt den Suchraum ein.
5. Die Grenze finden : Was ist die jüngste Änderung, nach der der Bug auftrat? Prüfe jüngste Deployments, Konfigurationsänderungen, Datenmigrationen und Dependency-Updates.

**Wenn die Reproduktion scheitert:**

- Erhöhe das Logging im verdächtigen Bereich und warte auf das erneute Auftreten
- Prüfe, ob der Bug umgebungsspezifisch ist (Daten, Konfiguration, Skalierung, Timing)
- Suche nach nicht-deterministischen Auslösern: Race Conditions, Cache-Zustand, zeitabhängige Logik, Verhalten externer Dienste
- Frage: "Unter welchen Bedingungen würde dieser Code dieses Symptom erzeugen?" und arbeite rückwärts

### Phase 2: Evidenz sammeln

Sammle Daten, bevor du Hypothesen bildest. Verfrühte Hypothesen erzeugen Bestätigungsfehler (Confirmation Bias).

| Evidenztyp | Wo suchen | Was extrahieren |
| --- | --- | --- |
| **Fehlermeldungen** | Anwendungslogs, Browser-Konsole, stderr | Exakte Meldung, Fehlercode, Stack Trace |
| **Stack Traces** | Exception-Handler, Crash-Dumps, APM-Tools | Vollständige Aufrufkette, der Frame, in dem der Fehler entsteht, vs. der, in dem er gefangen wird |
| **Logs** | Anwendungslogs, Systemlogs, Request-Logs | Einträge aus dem Zeitfenster um den Fehler, korreliert über Request-ID oder Zeitstempel |
| **Metriken** | APM-Dashboards, Infrastruktur-Monitoring | Latenzspitzen, Änderungen der Fehlerrate, Ressourcenauslastung (CPU, Speicher, Verbindungen) |
| **Zustand** | Datenbank, Cache, Session-Storage, Message-Queues | Tatsächliche Werte zum Zeitpunkt des Fehlers vs. erwartete Werte |
| **Jüngste Änderungen** | Git-Log, Deployment-Historie, Konfigurationsänderungen | Was sich zwischen "funktioniert" und "funktioniert nicht" geändert hat |

**Evidenz-Triage:** Nicht jede Evidenz ist gleich wertvoll. Priorisiere:

1. Die Fehlermeldung und den Stack Trace (am direktesten)
2. Was sich kürzlich geändert hat (höchste Vorwahrscheinlichkeit)
3. Zeitliche Korrelation mit externen Ereignissen (Deployment, Traffic-Spitze, Ausfall einer Dependency)

### Phase 3: Hypothesen bilden

Erzeuge mögliche Erklärungen, nach Wahrscheinlichkeit geordnet. Eine gute Hypothese ist:

- Spezifisch : "Das Session-Cookie des Nutzers wird nicht gesetzt, weil das SameSite-Attribut auf Strict steht und der Login-Flow einen Cross-Origin-Redirect enthält" — nicht "irgendwas stimmt mit den Cookies nicht."
- Testbar : Du kannst eine Beobachtung oder ein Experiment entwerfen, das sie bestätigt oder widerlegt.
- Falsifizierbar : Du kannst beschreiben, welche Evidenz sie widerlegen würde.

**Techniken zur Hypothesenbildung:**

1. Änderungsbasiert : Was hat sich kürzlich geändert? Die häufigste Ursache für "gestern lief es noch" ist "heute hat sich etwas geändert." Prüfe Deployments, Konfigurationsänderungen, Dependency-Updates, Datenmigrationen und Infrastrukturänderungen.
2. Fehlermeldungsgetrieben : Lies die Fehlermeldung wörtlich. Fehlermeldungen sind oft präzise — "Connection refused on port 5432" bedeutet zuerst genau das, was es sagt, bevor es etwas anderes bedeutet.
3. Fehlerbaumanalyse (Fault-Tree) : Arbeite rückwärts vom Symptom. "Die API gibt 500 zurück" → "Der Handler hat eine ungefangene Exception geworfen" → "Die Datenbankabfrage ist fehlgeschlagen" → "Der Connection-Pool ist erschöpft" → "Verbindungen lecken, weil Transaktionen auf Fehlerpfaden nicht geschlossen werden."
4. Analog : Hast du ein ähnliches Symptom schon einmal gesehen? Was war damals die Ursache? Mit Vorsicht anwenden — ähnliche Symptome können verschiedene Ursachen haben.

**Hypothesen ordnen** nach: (1) Konsistenz mit aller Evidenz, (2) Einfachheit (Ockhams Rasiermesser), (3) Nähe zu jüngsten Änderungen.

### Phase 4: Isolieren und testen

Teste jede Hypothese, beginnend mit der wahrscheinlichsten. Ziel ist, sie zu bestätigen oder auszuschließen.

**Isolationstechniken:**

| Technik | Wann anwenden | Methode |
| --- | --- | --- |
| **Binäre Suche (Bisect)** | Bug trat an einem unbekannten Punkt in einer Folge von Änderungen auf | git bisect oder den Änderungsbereich manuell halbieren, bis der einführende Commit gefunden ist |
| **Minimale Reproduktion** | Bug tritt in einem komplexen System auf | Komponenten nacheinander entfernen, bis das minimale Setup gefunden ist, das den Bug noch auslöst |
| **Variablen-Substitution** | Unklar, ob das Problem an Daten, Code oder Umgebung liegt | Eine Variable nach der anderen austauschen: denselben Code mit anderen Daten, dieselben Daten mit anderem Code oder dieselbe Code+Daten-Kombination in einer anderen Umgebung ausführen |
| **Logging-Injektion** | Interner Zustand ist undurchsichtig | Gezieltes Logging an Entscheidungspunkten ergänzen, um den tatsächlichen Ausführungspfad vs. den erwarteten nachzuverfolgen |
| **Breakpoint-Debugging** | Zustand an einem bestimmten Punkt der Ausführung muss inspiziert werden | Breakpoints vor dem Fehlerpunkt setzen und den Variablenzustand Schritt für Schritt inspizieren |
| **Teile und herrsche** | Mehrere Komponenten könnten schuld sein | Jede Komponente isoliert testen, um zu identifizieren, welche die falsche Ausgabe erzeugt |

**Isolationsdisziplin:**

- Ändere IMMER nur eine Sache. Wenn du zwei Dinge änderst und der Bug verschwindet, weißt du nicht, welche Änderung ihn behoben hat.
- Halte fest, was du versucht und was du beobachtet hast. Debugging ohne Notizen führt dazu, dieselbe Hypothese erneut zu testen.
- Setze ein Zeitlimit (Time-Box). Lässt sich eine Hypothese nicht in vertretbarer Zeit bestätigen oder ausschließen, stelle sie zurück und gehe zur nächsten über.

### Phase 5: Die Ursache verifizieren

Die brechende Zeile zu finden, reicht nicht. Stelle fest, WARUM sie bricht.

**Verifizierung der Ursache:**

1. Die vollständige Kette erklären : Kannst du von der Ursache → den Zwischenfehlern → dem beobachteten Symptom lückenlos nachverfolgen? Gibt es Lücken, könnte die Ursache tiefer liegen.
2. Weitere Symptome vorhersagen : Wenn dies die Ursache ist, welche anderen beobachtbaren Effekte müssten existieren? Prüfe diese Effekte als bestätigende Evidenz.
3. Das Timing erklären : Warum trat der Bug jetzt auf? Wenn die Ursache schon immer vorhanden war, was hat sich geändert, um sie auszulösen (Datenmuster, Last, Verhalten einer Dependency, Konfiguration)?
4. Ursache von Mitwirkungsfaktoren unterscheiden : Die Ursache ist das, was sich ändern muss, um ein erneutes Auftreten zu verhindern. Mitwirkungsfaktoren haben die Auswirkung verschlimmert, sind aber nicht der Ursprung.

**5-Why-Technik (auf Code angewendet):**

```
Symptom: Nutzer sehen nach dem Login eine leere Seite
Why 1: Die Dashboard-API gibt einen 500-Fehler zurück
Why 2: Die User-Profile-Abfrage wirft eine Null-Pointer-Exception
Why 3: Das Feld "preferences" ist bei neu angelegten Nutzern null
Why 4: Der Endpunkt zur Nutzererstellung initialisiert das preferences-Objekt nicht
Why 5: Die preferences-Initialisierung wurde bei einem Refactoring entfernt (Commit abc123)
Ursache: Das Refactoring entfernte die preferences-Initialisierung, ohne den Pfad zur Nutzererstellung anzupassen
```

Höre auf, wenn du eine Ursache erreichst, die umsetzbar und systemisch ist — etwas, das du so beheben kannst, dass die gesamte Bug-Klasse verhindert wird.

### Phase 6: Beheben und verifizieren

1. Den Fix schreiben : Behandle die Ursache, nicht nur das Symptom. Ist die Ursache "die Nutzererstellung initialisiert preferences nicht", besteht der Fix darin, preferences zu initialisieren — nicht darin, im Dashboard einen Null-Check hinzuzufügen.
2. Einen Regressionstest hinzufügen : Schreibe einen Test, der ohne den Fix fehlschlägt und mit ihm besteht. Das ist der wichtigste einzelne Schritt, um ein erneutes Auftreten zu verhindern.
3. Den Fix verifizieren : Bestätige mit den exakten Reproduktionsschritten aus Phase 1, dass das ursprüngliche Symptom nicht mehr auftritt.
4. Auf Kollateralschäden prüfen : Hat der Fix etwas anderes kaputt gemacht? Führe die bestehende Test-Suite aus. Prüfe verwandte Funktionen manuell, wenn die Testabdeckung unvollständig ist.

### Phase 7: Erneutes Auftreten verhindern

Der Bug ist behoben. Frage jetzt: Warum hat das System diesen Bug überhaupt zugelassen?

| Präventionskategorie | Maßnahmen |
| --- | --- |
| **Erkennung** | Hätte Monitoring oder Alerting dies früher erkennen können? Ergänze Alerts für diesen Fehlermodus. |
| **Defence in Depth** | Hätten Eingabevalidierung, Typsicherheit oder Invariantenprüfungen den schlechten Zustand verhindert? |
| **Prozess** | War dies eine Bug-Kategorie, die Code-Review, Tests oder Linting hätten abfangen sollen? Aktualisiere Checklisten oder Tooling. |
| **Dokumentation** | Gibt es eine implizite Annahme, die explizit gemacht werden sollte? Dokumentiere die Invariante. |

## Debugging-Strategien nach Bug-Typ

Verschiedene Bug-Kategorien profitieren von unterschiedlichen Untersuchungsansätzen. Nutze den allgemeinen Workflow oben, aber passe die Schwerpunkte je nach Bug-Typ an.

### Race Conditions und Nebenläufigkeitsfehler

- Reproduziere unter Last oder mit künstlichen Verzögerungen (Sleep-Anweisungen an vermuteten Race-Punkten)
- Suche nach geteiltem, veränderbarem Zustand, auf den ohne Synchronisierung zugegriffen wird
- Prüfe auf Time-of-Check-to-Time-of-Use-(TOCTOU-)Muster
- Ergänze Logging mit Thread-/Prozess-IDs und Zeitstempeln, um die Ereignisreihenfolge festzustellen
- Überlege, ob der Fix atomar sein muss (Transaktion, Lock, CAS-Operation)

### Memory Leaks

- Nutze Profiling-Tools, um in Intervallen Heap-Snapshots zu erstellen und zu vergleichen
- Suche nach nicht entfernten Event-Listenern, Closures, die große Scopes festhalten, wachsenden Caches ohne Eviction
- Prüfe auf zirkuläre Referenzen, die die Garbage Collection verhindern
- Reproduziere unter dauerhafter Last, nicht nur mit Einzelanfrage-Tests

### Performance-Regressionen

- Profile, bevor du rätst — miss, um den tatsächlichen Engpass zu finden, nicht den vermuteten
- Vergleiche Metriken von vor und nach dem Auftreten der Regression
- Prüfe auf N+1-Query-Muster, fehlende Indizes, geänderte algorithmische Komplexität, Serialisierungs-Overhead
- Verifiziere unter realistischen Datenmengen — Performance-Probleme zeigen sich oft erst bei Skalierung

### Sporadische Fehler (Flaky-Verhalten)

- Erhöhe die Stichprobengröße: Führe die Reproduktion viele Male aus und verfolge die Fehlerrate
- Suche nach Timing-Abhängigkeiten: Netzwerklatenz, Thread-Scheduling, warmer/kalter Cache-Zustand
- Prüfe auf externe Abhängigkeiten: Hängen Test oder Feature von einem Dienst ab, der gelegentlich langsam oder nicht verfügbar ist?
- Isoliere Zufall: Seeds fixieren, Zeit mocken, externe Aufrufe stubben, um den Test deterministisch zu machen

### Datenabhängige Bugs

- Vergleiche die Daten, die den Bug auslösen, mit Daten, die das nicht tun — worin unterscheiden sie sich?
- Prüfe auf Encoding-Probleme (Unicode, Zeichensätze, Byte Order Marks)
- Suche nach Grenzwerten: leere Strings, null vs. leer, sehr große Werte, Sonderzeichen
- Verifiziere Datenannahmen: Setzt der Code Eindeutigkeit, Reihenfolge oder ein Format voraus, das die Daten nicht garantieren?

## Leitplanken

- Diagnostiziere niemals ohne Evidenz. Gehe Evidenz und Hypothesentests durch. Reicht die Evidenz nicht, benenne, welche zusätzlichen Daten nötig sind — schließe nicht per Mustererkennung auf eine Schlussfolgerung.
- Erfinde niemals Fehlermeldungen, Stack Traces oder Log-Ausgaben. Alle Diagnosedaten müssen vom Nutzer stammen. Kennzeichne illustrative Beispiele als [Illustratives Beispiel — nicht aus deinem System] .
- Behaupte niemals, ein Fix sei verifiziert, ohne Reproduktion. Hat der Nutzer nicht bestätigt, dass das Symptom behoben ist, weise darauf hin, dass die Verifizierung aussteht.
- Versieh Schlussfolgerungen mit einer Quellenkennzeichnung als [Aus Evidenz] , [Hypothese — Test erforderlich] oder [Debugging-Methodik] .

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausarbeitung an, um die Untersuchung und die Ursachenanalyse als teilbares Dokument festzuhalten.
