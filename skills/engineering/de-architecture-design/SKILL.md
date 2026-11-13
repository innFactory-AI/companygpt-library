---
name: de-architecture-design
description: Systementwurf mit Trade-off-Analyse, Kapazitätsschätzung und Architecture Decision Records. Verwende ihn, wenn du ein neues System entwirfst, architektonische Optionen bewertest oder Designentscheidungen dokumentierst. Auslösen mit "Architektur entwerfen für", "wie sollten wir bauen", "Architektur für [System]".
---

# Architektur-Design-Skill

Entwirf Softwaresysteme von den Anforderungen bis zu dokumentierten Architekturentscheidungen. Der Skill deckt Trade-off-Analyse, Kapazitätsschätzung und Architecture Decision Records (ADRs) für Entscheidungen ab, die teuer rückgängig zu machen sind. Kontext und bestehende Unterlagen kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Wiki / Doku über MCP** (z. B. Confluence, GitHub) | Bestehende Architektur-Docs, ADRs, Infrastruktur-Diagramme, System-Inventare |
| **Projekt-Tracker über MCP** (z. B. Jira, Linear) | Epics, Anforderungen und technische Spikes |
| **companyRAG / Datei-Upload** | Bestehende Designdokumente, Assessments, Notizen aus Discovery-Sessions |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Design-Workflow

Führe diese sechs Phasen der Reihe nach aus. Die ersten beiden Phasen (Anforderungen und Constraints) müssen abgeschlossen sein, bevor du architektonische Optionen generierst — ein Entwurf ohne Verständnis der Constraints liefert Lösungen, die sich nicht bauen lassen.

### Phase 1: Anforderungen klären

Trenne funktionale Anforderungen (was das System tut) von nicht-funktionalen Anforderungen (wie gut es das tut). Beide prägen die Architektur, aber nicht-funktionale Anforderungen haben typischerweise den größeren Einfluss auf die architektonischen Entscheidungen.

**Funktionale Anforderungen erheben:**

1. Liste die zentralen Use Cases. Für jeden: Wer ist der Akteur, was tut er, was ist das erwartete Ergebnis?
2. Identifiziere die Datenentitäten und ihre Beziehungen. Welche Daten erzeugt, liest, aktualisiert und löscht das System?
3. Kartiere die Integrationspunkte. Mit welchen externen Systemen interagiert dies? Was sind deren APIs, Datenformate und Zuverlässigkeitseigenschaften?
4. Definiere die Systemgrenze. Was liegt innerhalb des entworfenen Systems und was ist eine externe Abhängigkeit?

**Nicht-funktionale Anforderungen (Qualitätsattribute):**

Frage jedes Attribut ab. Nicht alle sind gleich wichtig — der Nutzer muss priorisieren.

| Attribut | Schlüsselfragen |
| --- | --- |
| **Verfügbarkeit** | Was ist die Ziel-Uptime? Was kostet Ausfallzeit (pro Minute, pro Stunde)? Welche Komponenten sind kritisch vs. degradierbar? |
| **Skalierbarkeit** | Welche Lastniveaus werden erwartet (Nutzer, Requests/Sek., Datenvolumen) beim Launch und nach 1 Jahr / 3 Jahren? Ist das Wachstum linear oder schubweise? |
| **Latenz** | Was sind die Zielzeiten für die Antwort? p50, p95, p99? Welche Operationen sind latenzempfindlich? |
| **Dauerhaftigkeit** | Was ist das akzeptable Datenverlustfenster? Null (Finanzdaten) oder ein kleines Fenster (Analytics)? |
| **Konsistenz** | Braucht das System starke Konsistenz (Banküberweisungen) oder ist eventual consistency akzeptabel (Social Feeds)? |
| **Sicherheit** | Welche Datenklassifizierungsstufen? Welche Compliance-Frameworks (SOC 2, GDPR, HIPAA, PCI-DSS)? Wer sind die Bedrohungsakteure? |
| **Betreibbarkeit** | Wie hoch ist die operative Kapazität des Teams? 24/7-On-Call oder nur Geschäftszeiten? Welche Observability-Reife? |
| **Kosten** | Wie hoch ist das Budget? Präferenz CapEx vs. OpEx? Priorität der Kostenoptimierung relativ zu anderen Attributen? |

**Gate**: Es existiert eine priorisierte Liste nicht-funktionaler Anforderungen mit messbaren Zielwerten. "Das System sollte schnell sein" ist keine Anforderung. "p95-API-Latenz unter 200 ms bei 10.000 gleichzeitigen Nutzern" ist eine.

### Phase 2: Constraints identifizieren

Constraints sind nicht verhandelbare Grenzen. Sie eliminieren Optionen, bevor du sie bewertest.

| Constraint-Kategorie | Beispiele |
| --- | --- |
| **Technisch** | Muss in bestehende Oracle-Datenbank integrieren; Team hat nur Python-Expertise; muss on-premises laufen |
| **Organisatorisch** | Muss innerhalb von 3 Monaten launchen; keine neuen Engineers einstellbar; muss freigegebene Vendor-Liste nutzen |
| **Regulatorisch** | Daten müssen in der EU residieren; muss PCI-DSS erfüllen; Audit-Log-Aufbewahrung von 7 Jahren |
| **Finanziell** | Infrastrukturbudget von X €/Monat; keine neuen Lizenzkosten; muss aktuelle Hosting-Kosten senken |
| **Bestehende Verpflichtungen** | Bereits unterschriebener Vertrag mit Cloud-Provider X; bestehendes SLA mit Upstream-Service Y |

Dokumentiere jeden Constraint. Ungenannte Constraints tauchen während der Implementierung als Blocker auf.

### Phase 3: Architektonische Optionen vorschlagen

Generiere mindestens zwei und idealerweise drei deutlich verschiedene Optionen. Ein Designdokument mit nur einer Option ist eine Rechtfertigung, keine Entscheidung.

Für jede Option:

1. Architekturstil: Monolith, modularer Monolith, Microservices, Event-Driven, Serverless, CQRS usw.
2. Komponentendiagramm: Benenne die Hauptkomponenten, ihre Verantwortlichkeiten und wie sie kommunizieren (synchron vs. asynchron, Protokolle, Datenformate).
3. Datenarchitektur: Wo liegen die Daten? Was sind die Storage-Technologien und Datenflussmuster?
4. Deployment-Modell: Wie und wo läuft es? Cloud-Region, Container-Orchestrierung, Skalierungsansatz.
5. Zentrale technische Entscheidungen: Die 3–5 Entscheidungen innerhalb dieser Option, die das Verhalten des Systems am stärksten prägen.

**Strategien zur Optionsgenerierung:**

- Variiere die primäre Zerlegungsachse: Eine Option zerlegt nach Business-Domäne, eine andere nach technischer Schicht, eine weitere nach Deployment-Einheit.
- Variiere den Trade-off zwischen Konsistenz und Verfügbarkeit: Eine Option bevorzugt starke Konsistenz, eine andere Verfügbarkeit mit eventual consistency.
- Variiere das Build/Buy-Verhältnis: Eine Option baut eine eigene Komponente, eine andere nutzt einen Managed Service, eine weitere eine Open-Source-Lösung.

### Phase 4: Trade-offs analysieren

Das ist die intellektuelle Kernarbeit der Architektur. Nutze die Trade-off-Matrix unten.

**Trade-off-Analyse-Matrix:**

Bewerte für jede nicht-funktionale Anforderung aus Phase 1 jede Option:

```
| Anforderung       | Zielwert            | Option A       | Option B       | Option C       |
|-------------------|---------------------|----------------|----------------|----------------|
| Verfügbarkeit     | 99,9 %              | [Bewertung]    | [Bewertung]    | [Bewertung]    |
| Skalierbarkeit    | 50k gleichzeitig    | [Bewertung]    | [Bewertung]    | [Bewertung]    |
| Latenz (p95)      | < 200 ms            | [Bewertung]    | [Bewertung]    | [Bewertung]    |
| Betriebskosten    | < X €/Monat         | [Bewertung]    | [Bewertung]    | [Bewertung]    |
| Time to Market    | 3 Monate            | [Bewertung]    | [Bewertung]    | [Bewertung]    |
| Team-Kompetenz    | Aktuelle Skills     | [Bewertung]    | [Bewertung]    | [Bewertung]    |
```

Bewerte jede Zelle als: Erfüllt / Teilweise erfüllt / Nicht erfüllt — mit einer kurzen Erklärung.

**Häufige architektonische Trade-offs, die explizit zu adressieren sind:**

| Trade-off | Spannungsfeld |
| --- | --- |
| **Konsistenz vs. Verfügbarkeit** | CAP-Theorem — bei einer Partition wählst du eines. Was priorisiert dieses System und warum? |
| **Einfachheit vs. Flexibilität** | Ein Monolith ist einfacher zu entwickeln und zu deployen; Microservices bieten unabhängige Skalierung und Deployment. Was braucht das System tatsächlich? |
| **Latenz vs. Durchsatz** | Batching verbessert den Durchsatz, erhöht aber die Latenz. Was ist für diesen Use Case wichtiger? |
| **Build vs. Buy** | Eigener Code gibt Kontrolle; Managed Services reduzieren die operative Last. Wie hoch ist die operative Kapazität des Teams? |
| **Kopplung vs. Autonomie** | Geteilte Datenbanken vereinfachen den Datenzugriff; unabhängige Datenspeicher ermöglichen Team-Autonomie. Wie ist die Organisationsstruktur? |
| **Kosten jetzt vs. Kosten später** | Eine schnelle Lösung kann technische Schulden verursachen; eine robuste Lösung dauert länger. Was ist der Zeithorizont? |

**Failure-Mode-Analyse** (für jede Option):

1. Was passiert, wenn [Komponente X] ausfällt?
2. Was ist der Blast Radius — welche anderen Komponenten sind betroffen?
3. Wie erkennt das System den Ausfall?
4. Wie erholt sich das System — automatisch, mit manuellem Eingriff oder gar nicht?
5. Welche Daten sind während des Ausfallfensters gefährdet?

### Phase 5: Kapazität schätzen

Überschlagsrechnungen, um zu validieren, dass die vorgeschlagene Architektur die erwartete Last bewältigen kann. Dies sind Schätzungen in Größenordnungen — präzise Zahlen ergeben sich aus Lasttests. Rechne die Schätzung als Gedankenmodell direkt im Chat durch; es ist kein Code und keine Ausführung nötig.

**Framework zur Kapazitätsschätzung:**

1. Beginne mit dem Nutzerverhalten: Wie viele Nutzer? Wie viele Aktionen pro Nutzer pro Tag? Wie hoch ist das Peak-zu-Durchschnitt-Verhältnis?
2. Rechne in Systemlast um: Aktionen pro Sekunde im Peak. Read-zu-Write-Verhältnis. Payload-Größen.
3. Schätze den Storage: Daten pro Datensatz × Datensätze pro Tag × Aufbewahrungsdauer. Berücksichtige Indizes, Replikas und Backups.
4. Schätze die Compute-Last: Requests pro Sekunde × Verarbeitungszeit pro Request = benötigte Compute-Kapazität. Füge Headroom hinzu (typischerweise 2–3x für Peak-Handling und Wachstum).
5. Schätze das Netzwerk: Datenübertragung pro Request × Requests pro Sekunde. Cross-Region-Replikation, falls zutreffend.

**Schätzungsvorlage:**

```
KAPAZITÄTSSCHÄTZUNG: [Systemname]
Annahmen (alle benennen):
  - [Nutzer: X]
  - [Aktionen pro Nutzer pro Tag: Y]
  - [Peak-zu-Durchschnitt-Verhältnis: Z]
  - [Read:Write-Verhältnis: R:W]
  - [Durchschnittliche Payload-Größe: N KB]

Peak-Last:
  X Nutzer × Y Aktionen/Tag ÷ 86.400 Sek./Tag × Z Peak-Faktor = [N] Req/Sek. im Peak

Storage (1 Jahr):
  [N] Writes/Tag × [M] Bytes/Write × 365 Tage = [T] GB/Jahr
  Mit Indizes und Replikas (× 3 Schätzung): [T×3] GB/Jahr

Compute:
  [N] Req/Sek. × [M] ms/Req = [C] Compute-Sekunden/Sek.
  Benötigte Instanzen: [C] ÷ [Instanzkapazität] = [I] Instanzen + [Headroom]

Validierung: Passt das in den Kosten-Constraint aus Phase 2?
```

### Phase 6: Die Entscheidung dokumentieren

Halte die Entscheidung mit einem Architecture Decision Record (ADR) fest. Das ADR ist das Liefer-Ergebnis — ohne es geht die Begründung verloren und die Entscheidung wird erneut diskutiert.

## Architecture Decision Record (ADR) — Vorlage

```
# ADR-[NNN]: [Titel der Entscheidung]

## Status
[Vorgeschlagen | Akzeptiert | Veraltet | Abgelöst durch ADR-NNN]

## Datum
[JJJJ-MM-TT]

## Kontext
[Welche architektonische Frage wird adressiert? Welche Kräfte wirken — technisch, organisatorisch, geschäftlich? Welche Constraints existieren?]

## Entscheidung
[Die getroffene architektonische Wahl. Formuliere sie klar: "Wir werden [Ansatz X] für [Zweck Y] verwenden."]

## Betrachtete Optionen

### Option A: [Name]
- Beschreibung: [kurz]
- Pro: [Liste]
- Contra: [Liste]

### Option B: [Name]
- Beschreibung: [kurz]
- Pro: [Liste]
- Contra: [Liste]

### Option C: [Name] (falls zutreffend)
- Beschreibung: [kurz]
- Pro: [Liste]
- Contra: [Liste]

## Trade-off-Analyse
[Die Matrix aus Phase 4, zusammengefasst. Welche Anforderungen haben die Entscheidung getrieben?]

## Kapazitätsschätzung
[Zusammenfassung aus Phase 5 — Schlüsselzahlen, die die Wahl validieren]

## Konsequenzen
[Was wird einfacher? Was wird schwieriger? Welche neuen Constraints führt diese Entscheidung ein?]

## Risiken
[Was könnte mit dieser Entscheidung schiefgehen? Was würde eine erneute Prüfung auslösen?]

## Review-Trigger
[Unter welchen Bedingungen sollte diese Entscheidung überdacht werden? Beispiele: Traffic übersteigt die Schätzung um das 10-Fache, Teamgröße verdoppelt sich, Compliance-Anforderungen ändern sich.]
```

> **Tipp:** Wenn das ADR ein Diagramm enthalten soll, gib es im Output als Mermaid-Block an — companyFILES kann Mermaid rendern.

## Architektur-Bewertungs-Checkliste

Nach Abschluss des Designs zur Validierung der Vollständigkeit verwenden:

### Anforderungsabdeckung

- Jede funktionale Anforderung mappt auf eine Komponente
- Jede nicht-funktionale Anforderung hat einen messbaren Zielwert, und das Design adressiert ihn
- Alle Integrationspunkte sind mit Protokollen, Datenformaten und Failure Modes identifiziert

### Resilienz

- Single Points of Failure sind identifiziert und gemildert (oder als dokumentiertes Risiko akzeptiert)
- Failure Modes für jede Komponente sind mit Recovery-Strategien dokumentiert
- Eine Daten-Backup- und Recovery-Strategie existiert mit getesteten RPO/RTO-Zielen
- Pfade für graceful degradation existieren für nicht-kritische Komponenten

### Skalierbarkeit

- Kapazitätsschätzungen validieren, dass das Design die Ziellast bewältigt
- Ein horizontaler Skalierungspfad existiert für die Bottleneck-Komponenten
- Eine Datenpartitionierungsstrategie existiert, falls Single-Node-Storage nicht ausreicht

### Sicherheit

- Datenklassifizierung ist angewendet (was ist sensibel, was ist öffentlich)
- Authentifizierungs- und Autorisierungsgrenzen sind definiert
- Netzwerksegmentierung trennt Trust Zones
- Verschlüsselung at rest und in transit ist spezifiziert

### Betreibbarkeit

- Eine Observability-Strategie deckt Metriken, Logs und Traces ab
- Die Deployment-Strategie unterstützt Zero-Downtime-Releases
- Eine Rollback-Prozedur existiert für jede deploybare Komponente
- Der On-Call-Scope ist definiert — was erfordert menschlichen Eingriff vs. automatische Recovery

### Evolutionäre Architektur

- Das Design erlaubt, Komponenten unabhängig zu ersetzen
- Die Entscheidung enthält Review-Trigger dafür, wann die Architektur überdacht werden sollte
- Migrationspfade vom aktuellen Zustand existieren, falls dies ein Redesign ist

## Leitplanken

- Erfinde niemals Performance-Zahlen oder Benchmarks. Performance hängt von Konfiguration, Hardware und Workload ab. Gib stattdessen `[Erfordert Benchmarking mit deinem Workload und deiner Konfiguration]` an.
- Empfehle niemals konkrete Technologien ohne Nutzerkontext. Strukturiere die Trade-off-Analyse; behaupte nicht, eine Option sei besser, ohne die Anforderungen zu kennen.
- Stelle Kapazitätsschätzungen niemals als präzise dar. Kennzeichne alle Schätzungen als `[Größenordnungs-Schätzung — mit Lasttests validieren]`.
- Versieh Ausgaben mit einer Quellenkennzeichnung: `[Aus Nutzeranforderungen]`, `[Design-Methodik]` oder `[KI-Einschätzung — verifizieren]`.

> **Tipp:** Fordere über companyFILES eine Markdown- oder DOCX-Ausgabe an, um ein formatiertes, sofort teilbares Dokument zu erhalten. Mermaid-Blöcke rendert companyFILES als separates interaktives Diagramm mit PNG-Download, nicht innerhalb des Dokuments.
