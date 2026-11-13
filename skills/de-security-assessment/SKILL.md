---
name: de-security-assessment
description: Bewertet geplante Änderungen, Features und Systemanpassungen gegen Sicherheits- und Datenschutzvorgaben mit STRIDE-basierter Bedrohungsmodellierung, Datenflussanalyse, Zugriffskontroll-Review und EU-Datenschutzbewertung. Verwende ihn beim Prüfen einer neuen Integration, beim Bewerten eines Features auf Sicherheitsauswirkungen oder bei einem Pre-Deployment-Security-Check. Auslösen mit "Security-Assessment für", "ist diese Integration sicher", "Sicherheit prüfen von".
---

# Security-Assessment-Skill

Bewerte die Sicherheitsauswirkungen geplanter Änderungen, Integrationen und Systemanpassungen mit STRIDE-basierter Bedrohungsmodellierung, Datenflussanalyse, Zugriffskontroll-Review und EU-Datenschutzbetrachtung. Systemspezifische Details kommen von dir, aus einer angebundenen MCP-Quelle oder aus companyRAG-Sammlungen — der Skill analysiert die bereitgestellten Informationen und führt selbst keine Scans aus.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Security-Tools über MCP** (z. B. Vulnerability-Scanner, SIEM, Ticketing) | Scan-Ergebnisse, Schwachstellen-Findings, Sicherheitsvorfälle, offene Tickets |
| **companyRAG-Sammlungen** | Architektur-Dokumentation, Sicherheitsrichtlinien, frühere Assessments, Datenflussbeschreibungen |
| **Datei-Upload** | Systemdiagramme, Anforderungsdokumente, Integrationsspezifikationen, Vertragsunterlagen |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Assessment-Workflow

### Schritt 1: Assessment-Scope definieren

Lege vor jeder Analyse die Grenzen fest:

| Scope-Element | Zu klärende Frage |
| --- | --- |
| **Gegenstand** | Was wird bewertet? (Feature, Integration, Infrastrukturänderung, Architekturvorschlag) |
| **Betroffene Daten** | Welche Daten sind betroffen? Klassifiziere: Öffentlich, Intern, Vertraulich, Eingeschränkt/PII |
| **Systemgrenzen** | Welche Systeme, Services oder Komponenten sind im Scope? Was ist explizit ausgeschlossen? |
| **Nutzer und Akteure** | Wer interagiert damit? (Endnutzer, Admins, Service-Accounts, externe Systeme, Dritte) |
| **Deployment-Kontext** | Wo läuft das? (Produktion, Staging, nur intern, kundenseitig, mandantenfähig) |
| **Regulatorischer Kontext** | Welche Regularien gelten? (DSGVO, NIS2, DORA, AI Act, branchenspezifisch) |

Ein klarer Scope verhindert, dass das Assessment unbegrenzt ausufert. Dokumentiere, was NICHT bewertet wird, ebenso explizit wie das, was bewertet wird.

### Schritt 2: Datenflussanalyse

Bilde ab, wie Daten durch das bewertete System fließen. Das ist die Grundlage, um Angriffspunkte zu identifizieren.

#### Elemente des Datenflussdiagramms

Dokumentiere für jeden Datenfluss:

```
Quelle → [Protokoll/Methode] → Ziel
  Daten: [welche Daten übertragen werden]
  Klassifizierung: [Öffentlich / Intern / Vertraulich / Eingeschränkt]
  Authentifizierung: [wie die Verbindung authentifiziert wird]
  Verschlüsselung: [in transit / at rest / beides / keine]
  Speicherung: [wo Daten persistiert werden, Aufbewahrungsdauer]
```

#### Datenfluss-Inventartabelle

| # | Quelle | Ziel | Daten | Klassifizierung | Auth | Verschlüsselung | Speicherung |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Komponente] | [Komponente] | [Beschreibung] | [Stufe] | [Methode] | [TLS/mTLS/keine] | [wo/wie lange] |
| 2 | [Komponente] | [Komponente] | [Beschreibung] | [Stufe] | [Methode] | [TLS/mTLS/keine] | [wo/wie lange] |

Achte besonders auf:

- Überschreitungen von Vertrauensgrenzen: Daten, die zwischen Netzwerken, Umgebungen, Organisationen oder Jurisdiktionen wandern
- Datenaggregationspunkte: Wo mehrere Datenflüsse zusammenlaufen (Datenbanken, Logs, Analytics)
- Datentransformationspunkte: Wo Daten angereichert, kombiniert oder abgeleitet werden (kann neue Datenklassifizierungen erzeugen)
- Externe Integrationen: Jede Verbindung zu einem Drittanbieter-Service oder -System

### Schritt 3: Bedrohungsmodellierung (STRIDE-basiert)

Wende STRIDE auf jede in Schritt 2 identifizierte Komponente und jeden Datenfluss an. STRIDE ist ein bei Microsoft entwickeltes Akronym für sechs Bedrohungskategorien. Bestimme für jede Kategorie, ob die Bedrohung zutrifft und welche Auswirkung sie hätte.

#### STRIDE-Kategorien

| Kategorie | Bedrohung | Frage | Beispiele |
| --- | --- | --- | --- |
| **S — Spoofing** | Vortäuschung eines Nutzers oder Systems | Kann ein Angreifer sich als legitimer Nutzer, Service oder Komponente ausgeben? | Gestohlene Zugangsdaten, gefälschte Tokens, IP-Spoofing, Zertifikats-Imitation |
| **T — Tampering** | Unautorisierte Datenmanipulation | Kann ein Angreifer Daten in transit, at rest oder während der Verarbeitung verändern? | SQL-Injection, Parametermanipulation, Log-Tampering, Man-in-the-Middle |
| **R — Repudiation** | Abstreiten durchgeführter Aktionen | Kann ein Nutzer eine Aktion abstreiten, ohne dass sie sich nachweisen lässt? | Fehlende Audit-Logs, unsignierte Transaktionen, kein Activity-Tracking |
| **I — Information Disclosure** | Unautorisierte Datenoffenlegung | Kann ein Angreifer auf Daten zugreifen, die er nicht sehen sollte? | Ausführliche Fehlermeldungen, unsichere Speicherung, Log-Leakage, API-Überexposition |
| **D — Denial of Service** | Störung der Verfügbarkeit | Kann ein Angreifer oder Fehler den Service unverfügbar machen? | Ressourcenerschöpfung, Umgehung von Rate-Limits, Kaskadenfehler, Ausfall von Abhängigkeiten |
| **E — Elevation of Privilege** | Erlangen unautorisierter Zugriffsebenen | Kann ein Angreifer höhere Privilegien erlangen als vorgesehen? | Defekte Zugriffskontrolle, Privilege-Escalation, unsichere Standardrollen |

#### STRIDE-Anwendungsprozess

Für jede Komponente oder jeden Datenfluss im Scope:

1. Gehe jede STRIDE-Kategorie durch
2. Dokumentiere für jede zutreffende Bedrohung: Bedrohungsbeschreibung: Was konkret passieren könnte. Angriffsvektor: Wie ein Angreifer das ausnutzen würde. Bestehende Kontrollen: Welche Gegenmaßnahmen bereits vorhanden sind. Restrisiko: Welches Risiko nach den bestehenden Kontrollen verbleibt. Empfohlene Gegenmaßnahme: Zusätzliche Kontrollen, die in Betracht zu ziehen sind
3. Überspringe Kategorien, die wirklich nicht zutreffen (z. B. Repudiation kann für eine reine Lese-API ohne Belang sein) — dokumentiere aber, WARUM sie nicht zutreffen

#### Bedrohungsbewertungstabelle

| # | Komponente/Fluss | STRIDE-Kategorie | Bedrohung | Bestehende Kontrollen | Restrisiko | Schweregrad | Empfehlung |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Name] | [S/T/R/I/D/E] | [Beschreibung] | [was vorhanden ist] | [was verbleibt] | [C/H/M/L] | [Maßnahme] |

### Schritt 4: Zugriffskontroll-Review

Bewerte das Autorisierungsmodell des bewerteten Systems:

#### Authentifizierungsbewertung

| Kriterium | Bewertung |
| --- | --- |
| **Authentifizierungsmethode** | Welcher Mechanismus? (SSO, Benutzername/Passwort, API-Key, Zertifikat, Service-Account) |
| **MFA-Durchsetzung** | Ist MFA erforderlich? Für welche Nutzer/Rollen? Kann sie umgangen werden? |
| **Credential-Management** | Wie werden Zugangsdaten gespeichert, rotiert und widerrufen? |
| **Service-zu-Service-Auth** | Wie authentifizieren sich Services gegenseitig? (mTLS, JWT, Shared Secrets, IAM-Rollen) |
| **Session-Management** | Session-Dauer, Timeout, Handhabung paralleler Sessions, Widerruf |

#### Autorisierungsbewertung

| Kriterium | Bewertung |
| --- | --- |
| **Zugriffsmodell** | RBAC, ABAC, ACL oder individuell? |
| **Least Privilege** | Sind Standardberechtigungen minimal? Starten Nutzer ohne Zugriff und erhalten nur, was sie brauchen? |
| **Funktionstrennung** | Kann ein einzelner Nutzer sensible Aktionen sowohl anlegen als auch genehmigen? |
| **Admin-Zugriff** | Wie viele Admin-Accounts existieren? Sind sie personalisiert oder geteilt? Werden Admin-Aktionen auditiert? |
| **API-Autorisierung** | Sind API-Endpunkte einzeln autorisiert? Gibt es Scope-basierte Zugriffskontrolle? |
| **Zugriff auf Datenebene** | Können Nutzer nur ihre eigenen Daten sehen (Mandantenfähigkeit)? Wie wird Mandantenisolation durchgesetzt? |

#### Vorlage Zugriffskontroll-Findings

```
## Zugriffskontroll-Findings

### Stärken
- [Was gut umgesetzt ist]

### Lücken
| # | Lücke | Risiko | Schweregrad | Empfehlung |
|---|-------|--------|-------------|------------|
| 1 | [Beschreibung] | [was passieren könnte] | [C/H/M/L] | [Maßnahme] |

### Identifizierte überzogene Berechtigungen
| Principal | Aktueller Zugriff | Erforderlicher Zugriff | Maßnahme |
|-----------|-------------------|------------------------|----------|
| [Nutzer/Rolle/Service] | [was vorhanden] | [was nötig] | [reduzieren/widerrufen] |
```

### Schritt 5: EU-Datenschutzbewertung

Bewerte für jedes System, das personenbezogene Daten von EU/EWR-Personen verarbeitet, die Datenschutzauswirkungen:

| Kriterium | Bewertung |
| --- | --- |
| **Verarbeitete personenbezogene Daten** | Welche Kategorien personenbezogener Daten? (Identifikatoren, Kontakt, Verhalten, sensible/besondere Kategorien) |
| **Rechtsgrundlage** | Welche Rechtsgrundlage nach DSGVO Artikel 6 (und Artikel 9 für besondere Kategorien)? |
| **Zweckbindung** | Werden Daten nur für den genannten Zweck verwendet? Könnte eine neue Verarbeitung den Umfang erweitern? |
| **Datenminimierung** | Werden nur notwendige Daten erhoben? Ließe sich dasselbe Ergebnis mit weniger Daten erreichen? |
| **Speicherbegrenzung** | Wie ist die Aufbewahrungsdauer? Gibt es automatisierte Löschung? |
| **Grenzüberschreitende Übermittlung** | Verlassen Daten die EU/den EWR? Welcher Übermittlungsmechanismus ist vorhanden? |
| **Auftragsverarbeitung** | Verarbeiten Dritte Daten? Gibt es einen AV-Vertrag nach Artikel 28? |
| **DSFA-Auslöser** | Löst diese Verarbeitung eine Datenschutz-Folgenabschätzung nach Artikel 35 aus? (Neue Technologie, Profiling, umfangreiche Verarbeitung, automatisierte Entscheidungen) |

Markiere jede Verarbeitung, die eine DSFA oder Änderungen am Verzeichnis von Verarbeitungstätigkeiten (VVT) erfordern würde. Für detaillierte operative DSGVO-Workflows verweise den Nutzer auf den handle-gdpr-Skill.

### Schritt 6: Risikobewertung und Priorisierung

Bewerte jedes Finding des Assessments anhand der folgenden Matrix:

#### Schweregrade

| Stufe | Definition |
| --- | --- |
| **Kritisch** | Ausnutzbare Schwachstelle mit hoher Wahrscheinlichkeit, die zu einer Datenpanne, vollständiger Service-Kompromittierung oder regulatorischer Strafe führt. Erfordert sofortiges Handeln. |
| **Hoch** | Erhebliche Sicherheitslücke, die unter realistischen Bedingungen ausgenutzt werden könnte. Materielles Risiko von Datenexposition oder Serviceunterbrechung. Erfordert Handeln vor dem Deployment. |
| **Mittel** | Sicherheitsschwäche, die das Risiko erhöht, aber zusätzliche Faktoren zur Ausnutzung benötigt. Sollte im nächsten Entwicklungszyklus behoben werden. |
| **Niedrig** | Geringfügige Verbesserungsmöglichkeit. Stärkt Defense-in-Depth, ist aber kein unmittelbares Risiko. Bei Gelegenheit beheben. |

#### Priorisierungslogik

1. Kritische Findings blockieren das Deployment oder die Freigabe. Keine Ausnahmen ohne dokumentierte Freigabe durch CISO/Risk-Owner.
2. Hohe Findings müssen vor der Freigabe einen Remediation-Plan mit Frist haben. Kompensierende Kontrollen können als Übergangsmaßnahme akzeptiert werden.
3. Mittlere Findings werden im Risikoregister erfasst und bis zur Behebung verfolgt. Sie blockieren das Deployment nicht.
4. Niedrige Findings werden als Empfehlungen dokumentiert und nach Ermessen des Teams behoben.

### Schritt 7: Assessment-Bericht

```
# Security-Assessment-Bericht

**Gegenstand**: [was bewertet wurde]
**Datum**: [Datum]
**Bewertender**: [Name/Team]
**Assessment-Typ**: [Pre-Deployment / Integrations-Review / Architektur-Review / Periodisches Review]
**Gesamt-Risikoeinstufung**: [Kritisch / Hoch / Mittel / Niedrig]

## Executive Summary
[3-5 Sätze: was bewertet wurde, wichtigste Findings, allgemeine Risikolage, primäre Empfehlungen.]

## Scope
[Aus Schritt 1 — was im Scope ist, was explizit ausgeschlossen wird.]

## Datenfluss-Zusammenfassung
[Aus Schritt 2 — übergeordnete Datenflussbeschreibung mit hervorgehobenen Überschreitungen von Vertrauensgrenzen.]

## Findings Bedrohungsmodell
[Aus Schritt 3 — STRIDE-Findings-Tabelle, nach Schweregrad sortiert.]

## Zugriffskontroll-Findings
[Aus Schritt 4 — Ergebnisse der Authentifizierungs- und Autorisierungsbewertung.]

## Datenschutz-Findings
[Aus Schritt 5 — EU-Datenschutzbewertung, DSFA-Auslöser-Analyse.]

## Risikoregister

| # | Finding | Kategorie | Schweregrad | Empfehlung | Verantwortlich | Status |
|---|---------|-----------|-------------|------------|----------------|--------|
| 1 | [Beschreibung] | [STRIDE/Zugriff/Datenschutz] | [C/H/M/L] | [Maßnahme] | [Name] | [Offen] |

## Bedingungen für die Freigabe
[Liste aller Bedingungen, die erfüllt sein müssen, bevor die Änderung/das Feature/die Integration fortfahren kann.]

## Akzeptierte Risiken
[Risiken, die der Risk-Owner explizit akzeptiert hat, mit Begründung und Freigabe.]
```

---

## Gängige Sicherheitsmuster bei Integrationen

Prüfe beim Bewerten von Drittanbieter-Integrationen diese Muster:

| Muster | Sicherheitsbedenken | Was zu prüfen ist |
| --- | --- | --- |
| **OAuth-2.0-Verbindung** | Token-Scope, Speicherung von Refresh-Tokens, Korrektheit des Consent-Screens | Minimal erforderliche Scopes, sichere Token-Speicherung, Handhabung des Token-Ablaufs |
| **Webhook-Empfänger** | Eingabevalidierung, Authentifizierung eingehender Anfragen | HMAC-Signaturprüfung, IP-Allowlisting, Payload-Validierung |
| **API-Key-Integration** | Key-Exposition, Rotation, Scope-Begrenzung | Key-Speicherung (Vault, nicht im Code), Rotationsprozess, Keys je Umgebung |
| **File-Sync / Datenexport** | Datenexfiltration, Over-Sharing, veraltete Berechtigungen | Welche Daten geteilt werden, wer auf geteilte Daten zugreifen kann, Aufbewahrung auf der Remote-Seite |
| **SSO / SAML-Federation** | Ausweitung der Vertrauensgrenze, Attribut-Mapping, Session-Management | Assertion-Validierung, Audience-Restriction, signierte Assertions, Abstimmung der Session-Timeouts |
| **Eingebettetes iframe / Widget** | XSS, Clickjacking, Datenleck über postMessage | CSP-Header, Sandbox-Attribute, Origin-Validierung bei Cross-Origin-Messaging |

---

## Leitplanken

- Bewerte niemals die Sicherheit eines Systems aus Trainingsdaten. Alle systemspezifischen Details kommen vom Nutzer. Erzeuge keine Schwachstellenbewertungen auf Basis angenommener Architektur.
- Bezeichne ein System niemals als "sicher". Verwende "keine Findings im Scope identifiziert" — Security-Assessments identifizieren bekannte Risiken, sie zertifizieren nicht die Abwesenheit von Risiko.
- Erzeuge niemals konkrete CVEs aus dem Gedächtnis. Schwachstellendatenbanken ändern sich täglich — verifiziere per Websuche.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Systembeschreibung]`, `[Assessment-Framework]` oder `[KI-Analyse — mit Security-Team verifizieren]`. Kennzeichne nicht bewertete STRIDE-Kategorien explizit.

> **Tipp:** Fordere über companyFILES eine DOCX-, XLSX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Bericht zu erhalten.
