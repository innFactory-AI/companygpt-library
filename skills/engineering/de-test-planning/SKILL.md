---
name: de-test-planning
description: Teststrategie mit Coverage-Zielen, Verteilung der Testtypen und Definition von Quality Gates. Verwende ihn, wenn du Tests für ein neues Feature planst, Test-Coverage überprüfst oder CI-Quality-Gates einrichtest. Auslösen mit "Tests planen für", "Teststrategie für", "was sollte ich testen".
---

# Test-Planung-Skill

Plane, was getestet wird, wie es getestet wird und wie viel Testen genug ist. Der Skill deckt die Auswahl der Testtypen, Coverage-Ziele, die Verteilung über die Testpyramide und die Definition von Quality Gates ab — und verhindert so sowohl Under-Testing (Bugs gehen in Produktion) als auch Over-Testing (langsame Pipelines, fragile Test-Suites).

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear) | Feature-Anforderungen und Akzeptanzkriterien für das Test-Mapping |
| **Git-Provider über MCP** (z. B. GitHub, GitLab) | Code under Test, vorhandene Test-Suites, CI-Konfiguration |
| **Test-Management über MCP** (z. B. TestRail) | Bestehende Testfälle, Testläufe, Coverage-Historie |
| **companyRAG / Datei-Upload** | Bestehende Testpläne, Qualitätsstandards, Architektur-Dokumente |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Workflow Teststrategie

### Schritt 1: Verstehen, was du testest

Bevor du Testtypen auswählst, verstehe die Änderung:

1. Was ist das Feature oder die Änderung? Fasse es in einem Satz zusammen.
2. Was sind die Akzeptanzkriterien? Jedes Kriterium ist mindestens einem Test zugeordnet.
3. Was sind die Risikobereiche? Wo würde ein Bug den größten Schaden anrichten (Datenverlust, Sicherheitslücke, Umsatzauswirkung, nutzersichtbarer Fehler)?
4. Wie sieht die bestehende Test-Coverage aus? Gibt es Tests für den umgebenden Code? Welche Typen? Wo sind die Lücken?
5. Was sind die Integrationspunkte? Externe APIs, Datenbanken, Message Queues, Drittanbieter-Services — jeder ist eine Testgrenze.

### Schritt 2: Die Testpyramide anwenden

Die Testpyramide ist ein Modell zur Kosteneffizienz, keine starre Regel. Verteile die Testinvestition anhand von Feedback-Geschwindigkeit und dem Wert der Fehlererkennung.

| Ebene | Testtyp | Umfang | Ausführungsgeschwindigkeit | Erkannte Fehlertypen | Relative Kosten |
| --- | --- | --- | --- | --- | --- |
| **Basis** | Unit-Tests | Einzelne Funktion oder Klasse isoliert | Millisekunden | Logikfehler, Grenzbedingungen, Berechnungsfehler, Edge Cases | Am niedrigsten |
| **Mitte** | Integrationstests | Mehrere interagierende Komponenten | Sekunden | Schnittstellen-Mismatches, Datenflussfehler, Konfigurationsprobleme, Query-Bugs | Mittel |
| **Spitze** | E2E-Tests | Vollständiger User-Workflow durch das System | Sekunden bis Minuten | Workflow-Fehler, Deployment-Probleme, umgebungsspezifische Bugs | Am höchsten |

**Richtwert für die Pyramidenverteilung** (Ausgangspunkt — auf Basis der Risikoanalyse anpassen):

- ~70 % Unit-Tests — schnell, günstig, fangen die meisten Logik-Bugs
- ~20 % Integrationstests — verifizieren Komponenten-Interaktionen und Datenfluss
- ~10 % E2E-Tests — validieren, dass kritische User-Pfade durch den gesamten Stack funktionieren

**Wann die Pyramide invertiert wird:**

- Legacy-Systeme ohne Unit-Tests: mit Integrations- und E2E-Tests starten, um ein Sicherheitsnetz aufzubauen, dann beim Refactoring Unit-Tests ergänzen
- UI-lastige Änderungen mit minimaler Logik: mehr E2E- und Visual-Regression-Tests, weniger Unit-Tests
- Infrastruktur-Änderungen: mehr Integrations- und Smoke-Tests, weniger Unit-Tests

### Schritt 3: Testtypen auswählen

Nicht jeder Testtyp passt zu jeder Änderung. Nutze diese Auswahlmatrix:

| Testtyp | Verwenden, wenn | Weglassen, wenn |
| --- | --- | --- |
| **Unit-Tests** | Geschäftslogik, Algorithmen, Datentransformationen, Utility-Funktionen | Dünne Wrapper, reine Delegation, generierter Code |
| **Integrationstests** | Datenbank-Queries, API-Endpunkte, Service-zu-Service-Kommunikation, Message-Handler | Keine externen Abhängigkeiten beteiligt |
| **E2E-Tests** | Kritische User-Workflows, Checkout-/Zahlungsflüsse, Authentifizierung, datenkritische Pfade | Risikoarmes internes Tooling, experimentelle Features |
| **Contract-Tests** | Service-Grenzen in einer Microservices- oder API-Consumer-Architektur | Monolithische Systeme ohne Service-Grenzen |
| **Performance-Tests** | Latenzsensitive Operationen, durchsatzstarke Pfade, Operationen unter Last | Internes Tooling mit wenig Traffic, einmalige Skripte |
| **Security-Tests** | Authentifizierung, Autorisierung, Verarbeitung von Eingaben, Datenzugriffsgrenzen | Keine Nutzereingaben, keine sensiblen Daten |
| **Visual-Regression-Tests** | UI-Komponenten, Änderungen am Design-System, responsive Layouts | Reine Backend-Änderungen, reine API-Änderungen |
| **Smoke-Tests** | Post-Deployment-Verifizierung in jeder Umgebung | Bereits durch E2E-Tests in der CI abgedeckt |

### Schritt 4: Testfälle definieren

Für jeden ausgewählten Testtyp strukturierst du die Testfälle:

**Struktur eines Testfalls:**

```
TESTFALL: [aussagekräftiger Name]
  Typ:            [Unit / Integration / E2E / Contract / Performance / Security]
  Anforderung:    [verifiziertes Akzeptanzkriterium oder Risikobereich]
  Vorbedingungen: [Systemzustand vor dem Test — Datensetup, Konfiguration, Nutzerrolle]
  Input:          [was das zu testende Verhalten auslöst]
  Erwartetes Ergebnis: [beobachtbares, verifizierbares Ergebnis]
  Edge Cases:     [Grenzwerte, leere Eingaben, Fehlerbedingungen als Unterfälle]
  Priorität:      [Kritisch / Hoch / Mittel / Niedrig]
```

**Heuristiken zur Testfallgenerierung:**

| Technik | Wann anwenden |
| --- | --- |
| **Äquivalenzklassenbildung** | Input hat unterschiedliche Kategorien mit ähnlichem erwartetem Verhalten — pro Klasse einen Wert testen |
| **Grenzwertanalyse** | Numerische Bereiche, String-Längen, Sammlungsgrößen — am Grenzwert, knapp darunter und knapp darüber testen |
| **Error Guessing** | Null/undefined, leere Strings, Null, negative Zahlen, extrem große Werte, Sonderzeichen |
| **State-Transition-Testing** | Zustandsbehaftete Workflows (Bestelllebenszyklus, Abo-Status) — jeden gültigen und ungültigen Übergang testen |
| **Pairwise/kombinatorisch** | Mehrere unabhängige Parameter — Kombinationen testen, die alle Paare ohne vollständige Enumeration abdecken |
| **Happy Path + Failure Path** | Jedes Feature — bestätigen, dass es korrekt funktioniert UND dass es kontrolliert fehlschlägt |

### Schritt 5: Coverage-Ziele festlegen

Coverage ist ein notwendiges, aber kein hinreichendes Maß für Testqualität. Hohe Coverage mit schlechten Assertions fängt nichts.

**Leitlinien für Coverage-Ziele:**

| Code-Kategorie | Empfohlene Coverage | Begründung |
| --- | --- | --- |
| **Geschäftskritische Logik** | 90 %+ Line-Coverage | Bugs hier verursachen Umsatzverlust, Datenkorruption oder Sicherheitslücken |
| **Kern-Anwendungscode** | 80 %+ Line-Coverage | Standardziel — balanciert Gründlichkeit und Wartungskosten |
| **Utility-/Helper-Code** | 70 %+ Line-Coverage | Geringeres Risiko, aber breit genutzt |
| **Generierter Code, dünne Wrapper** | Aus Zielen ausschließen | Generierten Code zu testen testet den Generator, nicht dein System |
| **Konfiguration, DI-Verdrahtung** | Coverage durch Integrationstests | Unit-Tests für Konfiguration sind wenig wertvoll; Integrationstests verifizieren, dass es funktioniert |

**Zu verfolgende Coverage-Metriken:**

- Line-Coverage: Welche Zeilen während der Tests ausgeführt werden. Die Basismetrik.
- Branch-Coverage: Welche bedingten Verzweigungen ausgeführt werden. Aussagekräftiger als Line-Coverage — deckt ungetestete Pfade in if/else, switch, ternären Ausdrücken auf.
- Mutation-Coverage (wo machbar): Ob Tests eingefügte Fehler erkennen. Der Goldstandard für Testwirksamkeit, aber teuer in der Ausführung. Gezielt auf kritischem Code einsetzen.

**Coverage-Anti-Patterns, die du markieren solltest:**

- Coverage ohne Assertions (Tests, die Code ausführen, aber nie Ergebnisse verifizieren)
- Coverage-Ziele, die das Testen von Gettern/Settern statt Geschäftslogik anreizen
- Fehlschlagende Tests aus Coverage-Reports ausschließen, um Ziele zu erreichen

### Schritt 6: Quality Gates definieren

Quality Gates sind automatisierte Pass/Fail-Kriterien in der CI-Pipeline.

**Empfohlene Quality Gates:**

| Gate | Schwellenwert | Stufe | Blockiert Merge? |
| --- | --- | --- | --- |
| **Alle Tests bestehen** | 100 % Pass-Rate | Jeder PR | Ja |
| **Keine neuen Testfehler** | Null Regressionen | Jeder PR | Ja |
| **Coverage-Schwelle** | Pro Team-Standard (z. B. 80 %) | Jeder PR | Ja (für neuen Code) |
| **Keine Coverage-Abnahme** | Coverage-Delta ≥ 0 % | Jeder PR | Ja (empfohlen) |
| **Performance-Budget** | p95-Latenz ≤ Schwellenwert | Pre-Deploy | Ja (für kritische Pfade) |
| **Security-Scan** | Keine kritischen/hohen Findings | Pre-Deploy | Ja |
| **E2E-Smoke-Suite** | 100 % Pass-Rate | Post-Deploy auf Staging | Ja (blockiert Produktions-Deploy) |

**Designprinzipien für Quality Gates:**

- Gates müssen schnell sein. Ein Gate, das 30 Minuten läuft, wird umgangen. Verschiebe langsame Gates in asynchrone oder nächtliche Pipelines.
- Gates müssen zuverlässig sein. Ein fragiles Gate trainiert Entwickler darauf, Fehler zu ignorieren. Behebe oder entferne fragile Gates innerhalb eines Sprints.
- Gates müssen umsetzbar sein. Jeder Gate-Fehler muss eine klare Meldung erzeugen, was fehlgeschlagen ist und wie man es behebt.
- Gates sollten schrittweise verschärfen. Setze Schwellenwerte auf Basis des aktuellen Zustands und ziehe sie schrittweise an — setze keine ambitionierten Ziele, die jede Arbeit blockieren.

## Ausgabevorlage — Testplan

```
# Testplan: [Feature-/Änderungsname]

## Überblick
- Feature: [Name und kurze Beschreibung]
- Risikostufe: [Kritisch / Hoch / Mittel / Niedrig]
- Ausgewählte Testtypen: [Liste]
- Geschätzter Testaufwand: [Stunden/Tage]

## Verteilung über die Testpyramide
- Unit-Tests: [Anzahl/Prozent] — [was sie abdecken]
- Integrationstests: [Anzahl/Prozent] — [was sie abdecken]
- E2E-Tests: [Anzahl/Prozent] — [was sie abdecken]
- Sonstige: [Typ: Anzahl] — [was sie abdecken]

## Testfälle
[Strukturierte Testfälle gemäß Schritt 4]

## Coverage-Ziele
- Neuer Code: [Ziel] %
- Geänderter Code: [Ziel] %
- Von Coverage ausgeschlossen: [Liste mit Begründung]

## Quality Gates
[Gate-Definitionen gemäß Schritt 6]

## Risiken und Lücken
- [Bereiche mit unzureichender Test-Coverage und Begründung]
- [Abhängigkeiten, die nicht in der CI getestet werden können, und Gegenmaßnahme]
- [Bekannte Einschränkungen der Test-Infrastruktur]
```

## Leitplanken

- Erfinde niemals Coverage-Zahlen oder Testanzahlen. Wenn keine aktuellen Coverage-Daten vorliegen, gib an: "Aktuelle Coverage-Daten erforderlich — aus CI-Reports anfordern."
- Behaupte niemals konkrete Fehlererkennungsraten. Die Fehlererkennung hängt von der Testqualität ab, nicht allein vom Testtyp.
- Dieser Skill plant Strategie und liefert den Testplan sowie die Testfälle als Text — er führt keinen Code, keine Skripte und keine Test-Runner aus. Illustrativer Test-Code innerhalb einer Ausgabevorlage ist als Text zulässig; das Schreiben einsatzbereiter Tests setzt Kenntnis von Sprache, Framework und Test-Library voraus.
- Versieh Ausgaben mit einer Quellenkennzeichnung: `[Aus Nutzerkontext]`, `[Testmethodik]` oder `[KI-Empfehlung — prüfen]`.

> **Tipp:** Fordere über companyFILES eine XLSX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Testplan zu erhalten.
