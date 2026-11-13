---
name: de-deployment-prep
description: Pre-Deployment-Verifizierungs-Checkliste mit Rollback-Planung und Anleitung für schrittweise Rollouts. Verwende sie, wenn du ein Release vorbereitest, ein riskantes Deployment planst oder Deployment-Runbooks erstellst. Auslösen mit "Deployment vorbereiten", "Release-Checkliste", "Deploy-Plan für".
---

# Deployment-Vorbereitung-Skill

Erkenne Deployment-Probleme, bevor sie deine Nutzer erreichen, und halte den Blast Radius klein, wenn doch etwas schiefgeht. Der Skill deckt Pre-Deployment-Checklisten, Rollback-Planung, Canary-/Blue-Green-Strategien und Kommunikationspläne ab. Die kontextspezifischen Daten kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Git-Provider über MCP** (z. B. GitHub, GitLab) | Release-Branch, Changelog, gemergte PRs |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear) | Abgeschlossene Tickets; prüfen, ob alle geplanten Punkte gemergt sind |
| **CI-System über MCP** (z. B. GitHub Actions, GitLab CI) | Status der CI-Checks auf dem Release-Branch |
| **companyRAG / Datei-Upload** | Bestehende Runbooks, Infrastruktur-Dokumentation, SLA-Definitionen, frühere Post-mortems |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Pre-Deployment-Checkliste

Arbeite jeden Abschnitt durch, bevor du das Deployment startest. Hake Punkte erst ab, wenn sie verifiziert sind — verlasse dich nicht auf Annahmen.

### Code-Bereitschaft

- Alle geplanten Änderungen sind in den Release-Branch gemergt
- Keine offenen PRs blockieren das Release
- Alle CI-Checks laufen auf dem Release-Branch durch (Tests, Linting, Type-Checks, Security-Scans)
- Code-Review für alle Änderungen seit dem letzten Deployment ist abgeschlossen
- Keine bekannten kritischen oder schwerwiegenden Bugs im Release

### Datenbank und Daten

- Datenbank-Migrationen sind gegen einen produktionsnahen Datensatz getestet
- Migrationen sind abwärtskompatibel (alter Code läuft gegen das neue Schema)
- Das Rollback der Migration wurde getestet (sofern die Migration reversibel ist)
- Große Daten-Migrationen sind hinsichtlich Dauer und Lock-Auswirkung benchmarkt
- Daten-Backups sind aktuell und nachweislich wiederherstellbar

### Abhängigkeiten und Konfiguration

- Neue Umgebungsvariablen sind in allen Zielumgebungen gesetzt
- Neue Feature-Flags sind mit korrekten Standardzuständen konfiguriert
- Drittanbieter-Service-Abhängigkeiten sind betriebsbereit (Statusseiten prüfen)
- API-Versionskompatibilität mit Upstream- und Downstream-Services verifiziert
- Neue Secrets sind im Secrets Manager bereitgestellt

### Infrastruktur

- Die Zielumgebung hat ausreichend Kapazität für das Release (Compute, Memory, Storage)
- Auto-Scaling-Policies sind für erwartete Lastveränderungen konfiguriert
- Health-Check-Endpunkte sind aktualisiert, falls sich die Health-Kriterien geändert haben
- Load-Balancer-Routing-Regeln sind aktualisiert, falls neue Services oder Pfade eingeführt werden
- SSL-Zertifikate sind gültig und laufen nicht in Kürze ab

### Observability

- Monitoring-Dashboards decken neue Features und geänderte Komponenten ab
- Alerts sind für neue Fehlerfälle konfiguriert
- Log-Level sind angemessen (kein Debug in Produktion)
- Deployment-Marker oder -Annotationen sind für die Monitoring-Tools vorbereitet
- Runbook-Links sind an neue Alerts angehängt

### Kommunikation

- Der Deployment-Zeitplan ist an die Stakeholder kommuniziert
- Eine On-Call-Person ist benannt und während des Deployment-Fensters verfügbar
- Für Nutzer sichtbare Änderungen sind für das Support-Team dokumentiert
- Das Wartungsfenster ist kommuniziert (falls zutreffend)
- Ein Statusseiten-Update ist vorbereitet (falls zutreffend)

## Rollback-Plan

Jedes Deployment muss vor der Ausführung einen Rollback-Plan haben. "Roll forward" ist nur dann eine gültige Strategie, wenn sie bewusst gewählt wurde — nicht, weil ein Rollback nie geplant wurde.

### Rollback-Plan-Vorlage

```
# Rollback-Plan: [Release-Version/Name]

## Entscheidungskriterien für Rollback
Starte ein Rollback, wenn EINE dieser Bedingungen erfüllt ist:
- [ ] Fehlerrate übersteigt [X]% (Baseline: [Y]%)
- [ ] p95-Latenz übersteigt [X]ms (Baseline: [Y]ms)
- [ ] Health-Check-Fehler auf [N]+ Instanzen
- [ ] Bestätigtes, von Kunden gemeldetes kritisches Problem
- [ ] Datenintegritätsproblem erkannt

## Rollback-Befugnis
- Primär: [Name/Rolle — wer das Rollback autorisieren darf]
- Backup: [Name/Rolle]

## Rollback-Ablauf
1. [Schritt-für-Schritt-Ablauf, spezifisch für deine Deployment-Methode]
2. [z. B. Kubernetes-Deployment auf vorherige Revision zurücksetzen]
3. [z. B. Datenbank-Migrations-Rollback-Skript ausführen]
4. [z. B. Feature-Flag auf vorherigen Zustand zurücksetzen]
5. [z. B. CDN/Cache leeren, falls statische Assets geändert wurden]

## Geschätzte Rollback-Dauer
- Anwendungs-Rollback: [X Minuten]
- Datenbank-Rollback: [X Minuten — oder "irreversibel, siehe Gegenmaßnahme"]
- Vollständige Wiederherstellung: [X Minuten]

## Irreversible Komponenten
[Liste alle Änderungen auf, die nicht zurückgerollt werden können — Daten-Migrationen, externe Benachrichtigungen, Drittanbieter-Provisioning — samt Gegenmaßnahme]

## Verifizierung nach dem Rollback
- [ ] Anwendungs-Health-Checks laufen durch
- [ ] Fehlerrate ist auf Baseline zurückgekehrt
- [ ] Für Nutzer sichtbare Funktionalität verifiziert
- [ ] Stakeholder über das Rollback informiert
```

### Rollback-Strategie nach Änderungstyp

| Änderungstyp | Rollback-Ansatz | Zu beachten |
| --- | --- | --- |
| **Nur Anwendungscode** | Vorherige Version erneut deployen | Schnellstes Rollback. Prüfe, dass kein State geschrieben wurde, den die alte Version nicht lesen kann. |
| **Code + additive Schema-Migration** | Vorherigen Code erneut deployen; neues Schema belassen | Neue Spalten/Tabellen sind für alten Code harmlos, wenn Defaults gesetzt sind. Sauberer als das Migrations-Rollback. |
| **Code + destruktive Schema-Migration** | Erfordert getestetes Migrations-Rollback-Skript | Spalten-Umbenennungen, -Drops und Typänderungen sind gefährlich. Bevorzuge das Expand-Contract-Pattern. |
| **Feature-Flag-Änderung** | Flag auf vorherigen Zustand zurückschalten | Am schnellsten. Kein Deployment nötig. Prüfe die Propagationszeit des Flag-Zustands. |
| **Infrastruktur-Änderung** | Terraform/Helm auf vorherigen Zustand zurücksetzen | Längere Rollback-Dauer. Manche Infra-Änderungen (DNS, Zertifikat) haben Propagationsverzögerungen. |
| **Daten-Migration/Backfill** | Aus Backup wiederherstellen oder Reverse-Migration ausführen | Am langsamsten. Kann zu Datenverlust für nach der Migration erstellte Datensätze führen. Plane kompensierende Maßnahmen. |

## Strategien für schrittweise Rollouts

Wähle eine Rollout-Strategie basierend auf Risikostufe und Infrastruktur-Fähigkeiten.

### Strategie-Auswahl

| Risikostufe | Empfohlene Strategie | Begründung |
| --- | --- | --- |
| **Niedrig** (Konfig-Änderung, Copy-Update, Feature mit wenig Traffic) | Direktes Deployment mit Monitoring | Schnell, geringer Overhead. 15–30 Minuten nach dem Deploy monitoren. |
| **Mittel** (neues Feature, API-Änderung, Dependency-Update) | Canary-Deployment | Zuerst an einen kleinen Prozentsatz ausspielen. Vor dem vollständigen Rollout validieren. |
| **Hoch** (Datenbank-Migration, Auth-Änderungen, Payment-Flow) | Blue-Green mit Traffic-Shifting | Vollständige Parallel-Umgebung. Sofortiges Rollback per Traffic-Switch. |
| **Kritisch** (Kern-Infrastruktur, Multi-Service-Änderung) | Blue-Green + manuelle Verifizierungs-Gates | Vollständige Parallel-Umgebung mit menschlichen Checkpoints in jeder Stufe. |

### Canary-Deployment

1. Auf Canary-Instanzen deployen (typischerweise 5–10 % der Flotte)
2. Einen kleinen Traffic-Anteil auf die Canary routen (Start bei 1–5 %)
3. Canary vs. Baseline über eine definierte Bake-Time (mindestens 15 Minuten) monitoren:   - Fehlerraten (Canary darf Baseline + Schwellenwert nicht übersteigen)   - Latenz-Perzentile (p50, p95, p99)   - Business-Metriken (Conversion-Rate, Transaktions-Erfolgsrate)
4. Wenn die Canary gesund ist, den Traffic-Anteil stufenweise erhöhen (5 % → 25 % → 50 % → 100 %)
5. Wenn die Canary Degradation zeigt, allen Traffic auf die Baseline zurückrouten und untersuchen

### Blue-Green-Deployment

1. Neue Version in die grüne (inaktive) Umgebung deployen
2. Smoke-Tests gegen die grüne Umgebung ausführen
3. Traffic von blau (aktuell) auf grün umleiten:   - Option A: Sofortiger Switch (Load-Balancer-Regeländerung)   - Option B: Gradueller Shift (gewichtetes Routing, 10 % → 50 % → 100 %)
4. Die grüne Umgebung während der Bake-Time monitoren
5. Wenn gesund, blau außer Betrieb nehmen oder als nächstes Deployment-Ziel behalten
6. Wenn ungesund, Traffic auf blau zurückschalten (sofortiges Rollback)

### Bake-Time-Anhaltspunkte

| Systemmerkmal | Minimale Bake-Time |
| --- | --- |
| Stateless-API mit konstantem Traffic | 15–30 Minuten |
| Stateful-Service mit Sessions | 1–2 Stunden (vollständiger Session-Lebenszyklus) |
| Batch-Processing-System | 1 voller Batch-Zyklus |
| System mit täglichen Traffic-Mustern | 24 Stunden (Peak und Off-Peak abdecken) |
| System mit wöchentlichen Mustern | Erweitertes Monitoring über den ersten Wochenzyklus erwägen |

## Deployment-Runbook-Vorlage

Erstelle für komplexe oder risikoreiche Deployments ein Schritt-für-Schritt-Runbook:

```
# Deployment-Runbook: [Release-Version/Name]

## Vor dem Deployment (T-60 Min)
- [ ] Pre-Deployment-Checkliste als vollständig verifiziert
- [ ] Verfügbarkeit der On-Call-Person bestätigt
- [ ] Datenbank-Backup erstellt und verifiziert
- [ ] Stakeholder über Deployment-Start informiert
- [ ] Monitoring-Dashboards geöffnet

## Deployment-Ausführung
- [ ] Schritt 1: [konkrete Aktion mit erwartetem Ergebnis]
- [ ] Schritt 2: [konkrete Aktion mit erwartetem Ergebnis]
- [ ] Schritt 3: [konkrete Aktion mit erwartetem Ergebnis]
- [ ] Verifizieren: [Health-Check / Smoke-Test / Metrik-Check]

## Verifizierung nach dem Deployment (T+0 bis T+30 Min)
- [ ] Health-Checks laufen auf allen Instanzen durch
- [ ] Fehlerrate innerhalb des Schwellenwerts
- [ ] Latenz innerhalb des Schwellenwerts
- [ ] Wichtige Nutzer-Flows manuell verifiziert
- [ ] Keine unerwarteten Log-Einträge

## Monitoring nach dem Deployment (T+30 Min bis Ende der Bake-Time)
- [ ] Automatisiertes Monitoring bestätigt Stabilität
- [ ] Keine von Kunden gemeldeten Probleme
- [ ] Business-Metriken (falls zutreffend) im erwarteten Bereich

## Deployment abgeschlossen
- [ ] Deployment-Marker/-Annotation entfernen
- [ ] Statusseite aktualisieren (falls ein Wartungsfenster kommuniziert wurde)
- [ ] Stakeholder über erfolgreiches Deployment informieren
- [ ] Release Notes / Changelog aktualisieren
```

## Leitplanken

- Erfinde niemals Infrastruktur-Details. Nimm weder Cloud-Provider, Orchestrierungs-Plattform noch Deployment-Tooling an. Frage den Nutzer nach seinem Kontext.
- Generiere niemals konkrete Monitoring-Schwellenwerte. Alert-Schwellen müssen aus den SLAs und Baseline-Metriken des Nutzers stammen — stelle die Vorlage zum Ausfüllen bereit.
- Behaupte niemals, ein Rollback sei sicher, ohne die Änderung zu verstehen. Destruktive Migrationen, Daten-Backfills und externe Seiteneffekte können ein Rollback unmöglich machen. Bewerte die Irreversibilität immer explizit.
- Versieh Ausgaben mit einer Quellenkennzeichnung: `[Aus Nutzerkontext]`, `[Deployment-Methodik]` oder `[KI-Empfehlung — verifizieren]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um ein formatiertes, sofort teilbares Runbook zu erhalten.
