---
name: de-postmortem
description: Schuldfreies Incident-Postmortem mit Timeline-Rekonstruktion, Root-Cause-Analyse und Action Items. Verwende ihn nach einem Produktions-Incident, einem Service-Ausfall oder einem schwerwiegenden Bug. Auslösen mit "Postmortem durchführen für", "Incident Review", "was ist schiefgelaufen".
---

# Postmortem-Skill

Schuldfreie Postmortem-Methodik für Produktions-Incidents, Service-Ausfälle und schwerwiegende Defekte. Der Skill rekonstruiert Timelines, führt eine 5-Whys-Root-Cause-Analyse durch und erzeugt action-item-getriebene Berichte, die eine Wiederholung verhindern. Die Incident-Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Schuldfreie Prinzipien

Jedes mit diesem Skill durchgeführte Postmortem folgt diesen nicht verhandelbaren Prinzipien:

1. **Menschen sind nicht die Root Cause.** Systeme, Prozesse und Tooling versagen — Personen, die innerhalb dieser Systeme handeln, haben mit den verfügbaren Informationen die bestmöglichen Entscheidungen getroffen. Das Postmortem untersucht das System, das den Fehler ermöglicht hat, nicht die Person, die ihn ausgelöst hat.
2. **Im Nachhinein ist man immer klüger.** Es ist leicht, im Rückblick zu sehen, was hätte getan werden sollen. Das Postmortem muss rekonstruieren, was an jedem Entscheidungspunkt während des Incidents bekannt und sichtbar war — und darf Entscheidungen nicht mit Informationen beurteilen, die zu diesem Zeitpunkt nicht verfügbar waren.
3. **Das Ziel ist Lernen, nicht Bestrafung.** Ein Postmortem, das Schuld zuweist, garantiert, dass der nächste Incident verheimlicht oder heruntergespielt wird. Ein Postmortem, das umsetzbare Verbesserungen erzeugt, garantiert, dass das Team besser wird.
4. **Jeder Incident hat mehrere beitragende Faktoren.** Erzählungen mit einer einzigen Ursache ("der Entwickler hat eine fehlerhafte Config ausgerollt") sind fast immer unvollständig. Das Postmortem muss die Kette beitragender Faktoren identifizieren — den fehlenden Test, das unzureichende Review, den fehlenden Alert, das unklare Runbook — die gemeinsam den Incident ermöglicht haben.
5. **Action Items ohne Verantwortliche und Fristen sind Wünsche.** Jedes Postmortem-Action-Item braucht einen Verantwortlichen, eine Frist und eine Verifizierungsmethode. Nicht zugewiesene Action Items aus früheren Postmortems sollten überprüft werden, bevor neue erzeugt werden.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **APM / Monitoring über MCP** (z. B. Datadog, Grafana, PagerDuty) | Alert-Trigger, Metrik-Anomalien, Error-Rates, Latenz-Spikes, betroffene Services |
| **Git-Provider über MCP** (z. B. GitHub, GitLab, Bitbucket) | Commits und Deployments im Zeitfenster rund um den Incident |
| **CI/CD über MCP** (z. B. GitHub Actions, GitLab CI, Jenkins) | Build-/Deploy-Events, Rollback-Events, Pipeline-Status |
| **Chat über MCP** (z. B. Slack, Teams) | Nachrichten aus dem Incident-Channel, getroffene Entscheidungen, Eskalationspunkte |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear, Asana) | Incident-Ticket, verwandte Bugs, Action Items aus früheren Postmortems |
| **companyRAG / Datei-Upload** | Frühere Postmortems, wiederkehrende Muster, bestehende Runbooks, Status-Updates |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Postmortem-Workflow

### Phase 1: Die Fakten feststellen

Sammle vor der Analyse die rohen Fakten des Incidents. Widerstehe dem Drang zu erklären — dokumentiere zuerst, was passiert ist.

**Incident-Identifikation:**

| Feld | Inhalt |
| --- | --- |
| **Incident-ID** | Tracking-Identifier (Ticketnummer, Incident-Nummer) |
| **Severity** | SEV-1 (kritisch) / SEV-2 (schwerwiegend) / SEV-3 (gering) — gemäß den Severity-Definitionen der Organisation |
| **Dauer** | Zeit von der Erkennung bis zur vollständigen Behebung |
| **Impact** | Wer war betroffen, wie viele, welche Funktionalität war beeinträchtigt oder nicht verfügbar |
| **Erkennungsmethode** | Wie wurde der Incident entdeckt? Alert, Kundenmeldung, interne Beobachtung, automatisierte Prüfung |
| **Time to detect (TTD)** | Verstrichene Zeit vom Incident-Start bis zur Erkennung |
| **Time to mitigate (TTM)** | Verstrichene Zeit von der Erkennung bis zur Behebung des Kunden-Impacts |
| **Time to resolve (TTR)** | Verstrichene Zeit von der Erkennung bis zur Behebung der Root Cause |

**Checkliste zur Datensammlung:**

- Monitoring-Alerts und Zeitstempel aus APM-/Observability-Tools
- Deployment- und Commit-Historie aus CI/CD und Git-Provider für die 24 h vor dem Incident
- Chat-Logs aus dem Incident-Channel oder War-Room
- Kundenmeldungen oder Support-Tickets, die während des Incidents erstellt wurden
- Status-Page-Updates und ihre Zeitstempel
- On-Call-Rotation — wer wurde wann gepaged
- Alle durchgeführten Rollback-, Hotfix- oder Mitigation-Maßnahmen und ihre Zeitstempel

### Phase 2: Die Timeline rekonstruieren

Baue aus den gesammelten Daten eine chronologische Timeline. Die Timeline ist das Rückgrat des Postmortems — die gesamte Analyse fließt aus ihr.

**Timeline-Format:**

```
| Zeit (UTC) | Event | Quelle | Akteur |
|------------|-------|--------|--------|
| [HH:MM] | [Was passiert ist] | [Wo dies beobachtet wurde] | [Person oder System] |
```

**Regeln für die Timeline-Erstellung:**

1. Verwende durchgängig UTC. Zeitzonen-Verwirrung während der Incident-Analyse ist ein sekundärer Incident.
2. Trenne Beobachtung von Interpretation. "Error-Rate überschritt den 5-%-Schwellenwert" ist eine Beobachtung. "Das Deployment verursachte Fehler" ist eine Interpretation — sie gehört in die Analyse, nicht in die Timeline.
3. Erfasse System-Events und menschliche Aktionen. Deployments, Alert-Auslösungen, Rollbacks, Konfigurationsänderungen und Kommunikations-Events gehören alle auf die Timeline.
4. Markiere Unsicherheit. Wenn die genaue Zeit eines Events unbekannt ist, verwende "~HH:MM (ungefähr)", statt eine präzise Zeit zu raten.
5. Identifiziere die wichtigsten Übergänge. Markiere diese explizit:   - Incident-Start: Wann das System erstmals in einen degradierten Zustand eintrat (kann vor der Erkennung liegen)   - Erkennung: Wann ein Mensch oder System das Problem erstmals identifizierte   - Eskalation: Wann weitere Personen oder Teams hinzugezogen wurden   - Mitigation: Wann der Kunden-Impact reduziert oder beseitigt wurde   - Behebung: Wann die Root Cause behoben wurde (nicht nur mitigiert)

### Phase 3: Beitragende Faktoren identifizieren

Liste jeden Faktor auf, der dazu beigetragen hat, dass der Incident auftrat, unentdeckt blieb oder länger zur Behebung brauchte. Beitragende Faktoren werden NICHT Personen zugewiesen — es sind systemische Beobachtungen.

**Kategorien beitragender Faktoren:**

| Kategorie | Beispiele |
| --- | --- |
| **Code / Konfiguration** | Bug in der Business-Logik, falscher Konfigurationswert, fehlende Validierung, ungetesteter Edge Case |
| **Testing** | Fehlende Testabdeckung für den Fehlermodus, Test, der keine Produktionsbedingungen abbildete, Lasttest-Lücke |
| **Deployment** | Fehlende Canary-Phase, kein automatischer Rollback, Konfigurationsänderung ohne Feature Flag |
| **Monitoring / Alerting** | Fehlender Alert für den Fehlermodus, zu hoher Alert-Schwellenwert, lauter Alert maskierte das echte Signal |
| **Runbook / Dokumentation** | Kein Runbook für diesen Fehlermodus, veraltetes Runbook, fehlender Eskalationspfad |
| **Architektur** | Single Point of Failure, fehlender Circuit Breaker, keine Graceful Degradation, kaskadierende Abhängigkeit |
| **Kommunikation** | Verzögerte Eskalation, unklare Verantwortlichkeit, Informationen in einem Team siloiert |
| **Prozess** | Übersprungenes Code-Review, umgangene Staging-Umgebung, manueller Schritt in der Deployment-Pipeline |
| **Extern** | Ausfall eines Drittanbieter-Service, unerwartetes Traffic-Muster, geändertes Verhalten einer Upstream-API |

Notiere für jeden beitragenden Faktor:

- Was der Faktor war
- Wie er zum Incident beitrug (verursachte ihn, verschlimmerte ihn, verzögerte die Erkennung oder verzögerte die Behebung)
- Ob dieser Faktor bereits in früheren Postmortems aufgetaucht ist (wiederkehrendes Muster)

### Phase 4: Root-Cause-Analyse (5 Whys)

Wende die 5-Whys-Technik an, um vom Symptom zur tiefsten umsetzbaren Ursache zu gelangen. Die Technik fragt iterativ "warum", bis eine systemische Ursache erreicht ist, die behoben werden kann, um eine Wiederholung zu verhindern.

**5-Whys-Struktur:**

```
Symptom: [Beobachtbares Problem — z. B. "Kunden erhielten 45 Minuten lang 500-Fehler auf der Checkout-Seite"]

Warum 1: [Direkte Ursache]
  Beleg: [Welche Daten dies stützen]

Warum 2: [Ursache der direkten Ursache]
  Beleg: [Welche Daten dies stützen]

Warum 3: [Tiefere Ursache]
  Beleg: [Welche Daten dies stützen]

Warum 4: [Systemische Ursache]
  Beleg: [Welche Daten dies stützen]

Warum 5: [Root Cause — die tiefste umsetzbare Ursache]
  Beleg: [Welche Daten dies stützen]

Root-Cause-Statement: [Ein Satz, der das systemische Versagen zusammenfasst, das behoben werden muss]
```

**5-Whys-Disziplin:**

- Höre auf, wenn du eine umsetzbare systemische Ursache erreichst. "Der Entwickler hat einen Fehler gemacht" ist keine Root Cause — es ist eine proximale Ursache. Frage weiter, warum das System zuließ, dass der Fehler in Produktion gelangte.
- Verzweige, wenn mehrere Pfade existieren. Eine einzelne 5-Whys-Kette erfasst möglicherweise nicht alle Root Causes. Wenn der Incident mehrere unabhängige beitragende Pfade hatte, führe für jeden eine separate 5-Whys-Kette durch.
- Verifiziere jedes "Warum" mit Belegen. Jeder Schritt muss durch Daten aus der Timeline oder den gesammelten Belegen gestützt sein. Eine 5-Whys-Kette auf Basis von Annahmen erzeugt eine falsche Root Cause.
- Unterscheide Root Cause von beitragenden Faktoren. Die Root Cause ist das einzelne wirkmächtigste systemische Versagen. Beitragende Faktoren machten den Incident möglich oder schlimmer, aber die alleinige Behebung der Root Cause hätte den Incident nicht zwangsläufig verhindert. Beide brauchen Action Items.

### Phase 5: Action Items erzeugen

Jeder beitragende Faktor und die Root Cause müssen mindestens einem Action Item zugeordnet werden. Action Items ohne diese Zuordnung sind unbegrenzt — sie mögen produktiv wirken, adressieren den Incident aber nicht.

**Anforderungen an Action Items:**

| Feld | Erforderlich | Inhalt |
| --- | --- | --- |
| **ID** | Ja | Eindeutiger Identifier (z. B. AI-001) |
| **Beschreibung** | Ja | Spezifische, konkrete Maßnahme — nicht "Monitoring verbessern", sondern "Alert hinzufügen für Checkout-Error-Rate über 2 %, 5 Minuten anhaltend" |
| **Adressiert** | Ja | Welchen beitragenden Faktor oder welche Root Cause dieses Action Item adressiert |
| **Priorität** | Ja | P1 (verhindert Wiederholung dieses Incidents) / P2 (reduziert Blast Radius oder Erkennungszeit) / P3 (allgemeine Verbesserung, die dieser Incident sichtbar machte) |
| **Verantwortlicher** | Ja | Namentlich genannte Person oder Team, die für die Umsetzung verantwortlich ist |
| **Frist** | Ja | Ziel-Abschlussdatum |
| **Verifizierung** | Ja | Wie der Abschluss verifiziert wird (z. B. "Alert feuert korrekt im Staging-Test", "Runbook aktualisiert und vom On-Call-Team reviewt") |

**Action-Item-Kategorien:**

| Kategorie | Zweck | Beispiele |
| --- | --- | --- |
| **Fix** | Die Root Cause beseitigen | Code-Fix, Konfigurationskorrektur, Architekturänderung |
| **Detect** | Diesen Fehlermodus beim nächsten Mal früher erkennen | Neuer Alert, verbessertes Monitoring-Dashboard, automatisierter Health Check |
| **Mitigate** | Blast Radius reduzieren, falls diese Fehlerklasse erneut auftritt | Circuit Breaker, Feature Flag, Graceful Degradation, automatisierter Rollback |
| **Prevent** | Verhindern, dass diese Fehlerklasse eingeführt wird | Testabdeckung, aktualisierte Code-Review-Checkliste, Deployment-Gate, Linting-Regel |
| **Document** | Sicherstellen, dass das Team beim nächsten Mal schneller reagieren kann | Neues oder aktualisiertes Runbook, Dokumentation des Eskalationspfads, Architekturdiagramm |

**Frühere Action Items prüfen:** Prüfe vor dem Abschluss, ob frühere Postmortems ähnliche Action Items erzeugt haben, die nie umgesetzt wurden. Wiederkehrende Action Items sind ein systemisches Signal — eskaliere sie.

### Phase 6: Den Postmortem-Bericht schreiben

Stelle alle Erkenntnisse in der untenstehenden Ausgabevorlage zusammen.

## Ausgabevorlage

```
# Postmortem: [Incident-Titel]
**Incident-ID**: [ID]**Datum**: [Incident-Datum]**Severity**: [SEV-1 / SEV-2 / SEV-3]**Autor**: [Postmortem-Autor]**Status**: [Entwurf / In Review / Final]
---
## Zusammenfassung
[2-3 Sätze Zusammenfassung: was passiert ist, wie lange es dauerte, wer betroffen war und wie es behoben wurde. Geschrieben für einen Leser, der nicht am Incident beteiligt war.]
## Impact
| Metrik | Wert ||--------|------|| **Dauer** | [Gesamtdauer des Incidents] || **Time to detect** | [TTD] || **Time to mitigate** | [TTM] || **Time to resolve** | [TTR] || **Betroffene Nutzer** | [Anzahl oder Prozentsatz] || **Umsatz-Impact** | [Falls messbar, sonst "Nicht quantifiziert"] || **SLA-Impact** | [Verbrauchtes SLA-Budget, falls zutreffend] |## Timeline
| Zeit (UTC) | Event | Quelle ||------------|-------|--------|| [HH:MM] | [Event-Beschreibung] | [Quelle] || ... | ... | ... |## Root Cause
[Root-Cause-Statement aus der 5-Whys-Analyse]
### 5-Whys-Analyse
1. **Warum**: [Direkte Ursache] — Beleg: [Daten]2. **Warum**: [Tiefere Ursache] — Beleg: [Daten]3. **Warum**: [Tiefere Ursache] — Beleg: [Daten]4. **Warum**: [Systemische Ursache] — Beleg: [Daten]5. **Warum**: [Root Cause] — Beleg: [Daten]
## Beitragende Faktoren
| Faktor | Kategorie | Beitrag | Wiederkehrend? ||--------|-----------|---------|----------------|| [Faktor 1] | [Kategorie] | [Wie er beitrug] | [Ja/Nein — Link zum früheren Postmortem, falls ja] || [Faktor 2] | ... | ... | ... |## Was gut lief
- [Dinge, die während der Incident-Response funktionierten — schnelle Erkennung, effektive Kommunikation, erfolgreiche Mitigation usw.]
## Action Items
| ID | Beschreibung | Adressiert | Priorität | Verantwortlicher | Frist | Verifizierung ||----|--------------|------------|-----------|------------------|-------|---------------|| AI-001 | [Spezifische Maßnahme] | [Faktor/Root Cause] | P1 | [Verantwortlicher] | [Datum] | [Wie zu verifizieren] || AI-002 | ... | ... | ... | ... | ... | ... |## Lessons Learned
- [Wichtige Erkenntnis 1 — was das Team jetzt weiß, das es vorher nicht wusste]- [Wichtige Erkenntnis 2 — welcher Prozess oder welche Annahme widerlegt wurde]
## Referenzen
- [Link zum Incident-Ticket]- [Link zum Incident-Chat-Channel]- [Link zum Monitoring-Dashboard während des Incidents]- [Links zu verwandten früheren Postmortems]
```

## Leitplanken

- Weise NIEMALS Personen Schuld zu. Formuliere als systemisches Versagen um: "Das System ließ zu, dass [ Aktion ] in Produktion gelangte, weil [ fehlende Schutzmaßnahme ]." Dies ist nicht verhandelbar.
- Erfinde NIEMALS Timeline-Events. Jeder Eintrag muss aus Monitoring-Daten, Chat-Logs, Deployment-Aufzeichnungen oder Nutzeraussagen stammen. Markiere unbekannte Zeiten als ungefähr.
- Fabriziere NIEMALS Root Causes. Wenn die Belege unzureichend sind, schreibe "Root Cause unbestimmt — zusätzliche Daten erforderlich" und liste auf, welche Daten benötigt werden.
- Versieh jede Erkenntnis mit einer Quellenkennzeichnung: `[Aus Monitoring]`, `[Aus Chat-Logs]`, `[Aus Deployment-Aufzeichnungen]`, `[Aus Nutzermeldung]` oder `[KI-Analyse — verifizieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX-Ausgabe an, um ein formatiertes, verteilfertiges Word-Dokument zu erhalten.
