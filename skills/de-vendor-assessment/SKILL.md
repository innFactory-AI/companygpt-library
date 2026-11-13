---
name: de-vendor-assessment
description: Bewertet Anbieter gegen Security-, Compliance-, Capability- und Betriebskriterien und erstellt strukturierte Assessment-Reports. Verwende ihn beim Onboarding eines neuen SaaS-Tools, bei jährlichen Anbieter-Reviews oder zur Beantwortung von Beschaffungsanfragen. Auslösen mit "diesen Anbieter bewerten", "Vendor-Security-Review", "sollten wir [Tool] einsetzen".
---

# Vendor-Assessment-Skill

Bewerte Technologieanbieter strukturiert gegen Security-, Compliance-, Capability- und Betriebskriterien. Ausgerichtet an ISO 27001 Supplier Management und dem NIST CSF Supply Chain Risk Management. Anbieterspezifische Daten kommen von dir, aus einer angebundenen MCP-Quelle, aus companyRAG-Sammlungen oder aus hochgeladenen Dateien.

## Woher die Daten kommen

| Quelle | Was sie beiträgt |
| --- | --- |
| **Beschaffungs-/GRC-Tool über MCP** (z. B. ServiceNow, OneTrust, Vanta) | Anbieterstammdaten, vorhandene Risikobewertungen, Vertrags- und Beschaffungsstatus |
| **Ticketing über MCP** (z. B. Jira, ServiceNow) | Offene Risiko-Items, frühere Assessment-Tickets, Incident-Historie |
| **companyRAG-Sammlungen / Datei-Upload** | Anbieterdokumentation, Fragebogen-Antworten (CAIQ, SIG, VSAQ), SOC-2-/ISO-Reports, DPA und Verträge |

> **Keine angebundene Quelle?** Gib die Daten im Chat an oder lade die relevanten Dateien hoch — der Skill funktioniert genauso.

## Assessment-Workflow

Führe diese Phasen für jedes Anbieter-Assessment der Reihe nach aus:

### Phase 1: Scoping

Lege den Umfang des Assessments fest, bevor du irgendetwas bewertest:

1. Use Case : Wofür wird dieser Anbieter/dieses Tool eingesetzt? Welche Teams? Welche Workflows?
2. Datenklassifizierung : Welche Datenkategorien wird der Anbieter abrufen oder verarbeiten? (Öffentlich, Intern, Vertraulich, Eingeschränkt/PII/PHI)
3. Integrationstiefe : Eigenständiges Tool, API-Integration, SSO-angebunden, Datensynchronisation oder im kritischen Pfad eingebettet?
4. Nutzerkreis : Wie viele Nutzer? Welche Rollen? Self-Service oder Admin-verwaltet?
5. Kritikalität : Wenn dieser Anbieter 24 Stunden nicht verfügbar wäre, welche Auswirkung hätte das auf das Geschäft? (Informativ, Betriebliche Auswirkung, Umsatzauswirkung, Geschäftskritisch)
6. Regulatorischer Kontext : Welche Regulierungen gelten für die Daten oder den Prozess? (DSGVO, NIS2, DORA, AI Act, branchenspezifisch)

Die Scoping-Antworten bestimmen, welche Abschnitte des Assessments verpflichtend bzw. optional sind und wie tief jeder Abschnitt gehen muss.

### Phase 2: Security-Assessment

Bewerte die Security-Posture des Anbieters über diese Domänen:

#### Authentifizierung und Zugriffskontrolle

| Kriterium | Anforderung | Bewertung |
| --- | --- | --- |
| SSO-Unterstützung | SAML 2.0 oder OIDC-Integration | Erforderlich ab Vertraulich |
| MFA-Durchsetzung | Erzwungene MFA für alle Nutzer, inklusive Admins | Erforderlich für alle Stufen |
| RBAC/ABAC | Granulare rollenbasierte Zugriffskontrolle mit Least-Privilege-Defaults | Erforderlich ab Vertraulich |
| Admin-Audit-Trail | Unveränderliches Log aller Admin-Aktionen mit Zeitstempeln | Erforderlich ab Vertraulich |
| API-Authentifizierung | OAuth 2.0, API-Keys mit Rotation oder Mutual TLS | Erforderlich bei API-Integration |
| Session-Management | Konfigurierbares Timeout, Limits für parallele Sessions | Empfohlen |
| SCIM-Provisioning | Automatisiertes Nutzer-Lifecycle-Management | Erforderlich bei >50 Nutzern |

#### Datenschutz und Datensicherheit

| Kriterium | Anforderung | Bewertung |
| --- | --- | --- |
| Verschlüsselung at Rest | AES-256 oder gleichwertig, Option für kundenverwaltete Schlüssel | Erforderlich ab Vertraulich |
| Verschlüsselung in Transit | TLS 1.2+ erzwungen, kein Fallback auf schwächere Protokolle | Erforderlich für alle Stufen |
| Datenisolation | Logische oder physische Mandantentrennung dokumentiert | Erforderlich ab Vertraulich |
| Backup und Recovery | Dokumentierte Backup-Frequenz, Aufbewahrung, getestete Wiederherstellung | Erforderlich ab Kritikalität Betrieblich |
| Datenlöschung | Dokumentierter Löschprozess, Zeitrahmen und Zertifizierung bei Vertragsende | Erforderlich im DSGVO-Geltungsbereich |
| Key-Management | HSM-gestützt, dokumentierter Schlüsselrotationsplan | Erforderlich bei eingeschränkten Daten |

#### Infrastruktur-Security

| Kriterium | Anforderung | Bewertung |
| --- | --- | --- |
| Hosting-Umgebung | Dokumentierter Cloud-Provider, Region(en), Architekturüberblick | Erforderlich für alle Stufen |
| Vulnerability-Management | Regelmäßige Scans, dokumentierte Patching-Kadenz | Erforderlich für alle Stufen |
| Penetration-Testing | Jährlicher Drittanbieter-Pentest mit Nachweis der Behebung | Erforderlich ab Vertraulich |
| Incident-Response | Dokumentierter IR-Plan mit definierten Benachrichtigungsfristen | Erforderlich für alle Stufen |
| Business Continuity | Dokumentiertes BCP/DR mit getesteten RTO/RPO | Erforderlich ab Kritikalität Betrieblich |
| Netzwerk-Security | WAF, DDoS-Schutz, Netzwerksegmentierung | Erforderlich ab Vertraulich |

#### Vorgehen beim Security-Fragebogen

Wenn du einen Security-Fragebogen an den Anbieter schickst, strukturiere ihn entlang der obigen Domänen. Akzeptiere branchenübliche Fragebögen (CAIQ, SIG, VSAQ) als gültige Antworten — zwinge Anbieter nicht zu Doppelarbeit. Mappe ihre Antworten auf deine Assessment-Kriterien, statt dein exaktes Format zu verlangen.

### Phase 3: Compliance-Assessment

#### Zertifizierungen und Attestierungen

| Zertifizierung | Was sie abdeckt | Verifizierung |
| --- | --- | --- |
| **SOC 2 Type II** | Security-, Verfügbarkeits-, Verarbeitungsintegritäts-, Vertraulichkeits- und Datenschutzkontrollen über einen Zeitraum (typischerweise 12 Monate) | Aktuellen Report anfordern. Berichtszeitraum, Scope und vermerkte Ausnahmen prüfen. Type I (Zeitpunktbetrachtung) ist deutlich weniger wert als Type II. |
| **ISO 27001** | Informationssicherheits-Managementsystem | Zertifikat anfordern. Prüfen, ob der Scope den relevanten Dienst abdeckt (nicht nur die Unternehmenszentrale). Statement of Applicability auf ausgeschlossene Controls prüfen. |
| **ISO 27701** | Datenschutz-Informationsmanagement (erweitert ISO 27001) | Zertifikat anfordern. Relevant für die DSGVO-Auftragsverarbeiter-Compliance. |
| **CSA STAR** | Cloud-spezifische Security (basierend auf CAIQ/CCM) | Level 1 (Selbstauskunft) vs. Level 2 (Drittanbieter-Audit) — Level 2 ist deutlich aussagekräftiger. |
| **ISAE 3402 / SSAE 18** | Service-Organisationskontrollen (Finanzfokus) | Relevant für die Verarbeitung von Finanzdaten. Report-Scope prüfen. |
| **C5 (BSI)** | Cloud-Security-Attestierung (deutscher Bundesstandard) | Zunehmend vom deutschen öffentlichen Sektor und regulierten Branchen erwartet. |

Eine Zertifizierung ist ein Ausgangspunkt, kein Endpunkt. Verifiziere immer: (1) der Scope deckt den zu bewertenden Dienst ab, (2) der Berichtszeitraum ist aktuell und (3) alle Ausnahmen oder Einschränkungen wurden geprüft.

#### DSGVO-Compliance

| Kriterium | Anforderung | Referenz |
| --- | --- | --- |
| Auftragsverarbeitungsvertrag | DPA konform mit den Anforderungen aus Art. 28(3) | DSGVO Art. 28 |
| Rechtsgrundlage | Dokumentierte Rechtsgrundlage für die Verarbeitung | DSGVO Art. 6 |
| Betroffenenrechte | Prozess für die Bearbeitung von DSARs innerhalb der 30-Tage-Frist | DSGVO Art. 15-22 |
| Meldung von Verletzungen | Benachrichtigung in einem Zeitrahmen, der dem Verantwortlichen die 72h-Frist ermöglicht | DSGVO Art. 33 |
| Unterauftragsverarbeiter-Management | Liste der Unterauftragsverarbeiter, Benachrichtigungsmechanismus bei Änderungen, Widerspruchsrecht | DSGVO Art. 28(2) |
| Verzeichnis von Verarbeitungstätigkeiten | Gepflegt wie für Auftragsverarbeiter erforderlich | DSGVO Art. 30(2) |
| DSB-Benennung | DSB benannt, wo erforderlich | DSGVO Art. 37 |
| Internationale Übermittlungen | Gültiger Übermittlungsmechanismus vorhanden (siehe Abschnitt EU-Datenresidenz) | DSGVO Kap. V |

#### EU-Datenresidenz und -Übermittlung

Dieser Abschnitt ist für EU-basierte Organisationen entscheidend und muss für jeden Anbieter, der personenbezogene Daten verarbeitet, gründlich bewertet werden.

| Kriterium | Bewertung |
| --- | --- |
| **Datenspeicherort** | In welchem Land/welcher Region werden Daten at Rest gespeichert? Speicherung in der EU/im EWR ist am einfachsten. |
| **Datenverarbeitungsort** | Wo werden Daten verarbeitet? Kann vom Speicherort abweichen (z. B. in der EU gespeichert, aber über einen US-basierten Dienst verarbeitet). |
| **Standorte der Unterauftragsverarbeiter** | Wo sitzen die Unterauftragsverarbeiter? Ein einzelner Nicht-EU-Unterauftragsverarbeiter kann Übermittlungsanforderungen auslösen. |
| **Übermittlungsmechanismus** | Wenn Daten die EU/den EWR verlassen: Angemessenheitsbeschluss, EU-SCCs (Durchführungsbeschluss 2021/914 der Kommission), BCRs oder ein anderer gültiger Mechanismus. Bei US-Übermittlungen: aktuellen Status des Rahmenwerks und Teilnahme des Anbieters prüfen. |
| **Transfer Impact Assessment** | Hat der Anbieter ein TIA für Nicht-EU-Übermittlungen durchgeführt? Kann er es vorlegen? |
| **Risiko des behördlichen Zugriffs** | Bei Nicht-EU-Jurisdiktionen: Risiko des behördlichen Datenzugriffs (Überwachungsgesetze, nationale Sicherheitsanordnungen). Bewertung gemäß den Schrems-II-Anforderungen. |
| **Option zur Datenlokalisierung** | Kann der Anbieter eine reine EU-Datenverarbeitung anbieten? Zu welchen Kosten oder funktionalen Einschränkungen? |

**Schrems-II-Praxis-Checkliste:**

1. Alle Datenflüsse in/aus Nicht-EU-Ländern abbilden
2. Die Rechtsgrundlage für jede Übermittlung identifizieren
3. Die Gesetze des Ziellandes hinsichtlich behördlichen Zugriffs bewerten
4. Bestimmen, ob zusätzliche Maßnahmen erforderlich sind (Verschlüsselung, Pseudonymisierung, vertragliche Zusagen)
5. Die Bewertung dokumentieren und regelmäßig überprüfen

### Phase 4: Capability-Assessment

Bewerte die Eignung des Anbieters für den vorgesehenen Use Case:

| Kategorie | Bewertungskriterien |
| --- | --- |
| **Funktionale Eignung** | Erfüllt das Tool die genannten Anforderungen? Gap-Analyse zwischen Must-have- und Nice-to-have-Funktionen. |
| **Integrationsfähigkeit** | API-Verfügbarkeit, Webhook-Unterstützung, Standardprotokolle, vorhandene Connectoren zu deinem Stack. |
| **Skalierbarkeit** | Kann die Lösung mit deiner Nutzung wachsen? Rate-Limits, Nutzerlimits, Beschränkungen beim Datenvolumen. |
| **Zuverlässigkeit** | Veröffentlichtes Uptime-SLA, historische Uptime-Daten, Incident-Historie (Statusseiten-Archive prüfen). |
| **Support** | Support-Stufen, Reaktionszeit-SLAs, Supportzeiten, Eskalationspfad, dedizierte Account-Betreuung. |
| **Roadmap-Alignment** | Passt die Produktrichtung des Anbieters zu deinen künftigen Anforderungen? Konzentrationsrisiko bewerten, falls du von einer noch nicht gebauten Funktion abhängst. |
| **Anbieter-Lebensfähigkeit** | Finanzielle Stabilität, Finanzierungsphase, Größe der Kundenbasis, Marktposition. Ein brillantes Tool von einem Anbieter, den es in 18 Monaten vielleicht nicht mehr gibt, ist ein Risiko. |
| **Exit-Strategie** | Datenexport-Fähigkeit, API-Zugriff für Massenextraktion, Standard-Datenformate, vertragliche Regelungen zur Datenrückgabe. |

### Phase 5: Risikoklassifizierung

Führe die Assessment-Ergebnisse zu einer Gesamt-Risikoklassifizierung zusammen:

| Risikostufe | Kriterien | Freigabepfad |
| --- | --- | --- |
| **Niedrig** | Nur öffentliche Daten, eigenständiges Tool, keine Integration, informative Nutzung | Freigabe durch Teamlead |
| **Mittel** | Interne Daten, begrenzte Integration, betrieblich aber nicht kritisch | Freigabe durch IT-Manager + Data Owner |
| **Hoch** | Vertrauliche Daten, tiefe Integration, großer Nutzerkreis, schwer ersetzbar | CISO + Legal-Review + Management-Freigabe |
| **Kritisch** | Eingeschränkte/PII-Daten, geschäftskritische Abhängigkeit, regulatorische Implikationen | CISO + DSB + Legal + Executive-Freigabe |

### Risiko-Scoring-Matrix

Bewerte jede Assessment-Domäne auf einer Skala von 1-5:

| Score | Bedeutung |
| --- | --- |
| 5 | Erfüllt Anforderungen vollständig, durch Nachweise belegt, keine Lücken |
| 4 | Erfüllt Anforderungen mit geringen Lücken, Roadmap-Punkten oder Dokumentationsschwächen |
| 3 | Erfüllt Anforderungen teilweise, materielle Lücken vorhanden, aber mit kompensierenden Maßnahmen handhabbar |
| 2 | Erhebliche Lücken, kompensierende Maßnahmen sind teuer oder komplex |
| 1 | Erfüllt Anforderungen nicht, blockierende Lücken ohne tragfähige kompensierende Maßnahmen |

Aggregiere die Scores nach Domäne (Security, Compliance, Capability) und erzeuge einen Gesamt-Risiko-Score für den Anbieter. Gewichte die Domänen anhand der Scoping-Antworten aus Phase 1 — ein Anbieter, der eingeschränkte Daten verarbeitet, sollte Security und Compliance höher gewichten als Capability.

---

## Vorlage Assessment-Report

```
# Vendor-Assessment-Report

**Anbieter**: [Name]
**Produkt/Service**: [konkret bewertetes Produkt]
**Assessment-Datum**: [Datum]
**Assessor**: [Name/Team]
**Assessment-Typ**: [Neuer Anbieter / Jährliches Review / Anlassbezogenes Review]

## Executive Summary

**Gesamt-Risikoklassifizierung**: [Niedrig / Mittel / Hoch / Kritisch]
**Empfehlung**: [Freigeben / Mit Auflagen freigeben / Bis zur Behebung zurückstellen / Ablehnen]
**Wichtigste Erkenntnisse**: [3-5 Stichpunkte zu den bedeutendsten Erkenntnissen]

## Scoping

- Use Case: [Beschreibung]
- Datenklassifizierung: [Öffentlich / Intern / Vertraulich / Eingeschränkt]
- Integrationstiefe: [Eigenständig / API / SSO / Datensync / Kritischer Pfad]
- Kritikalität: [Informativ / Betrieblich / Umsatz / Geschäftskritisch]
- Regulatorischer Geltungsbereich: [anwendbare Regulierungen]

## Security-Assessment — Score: [X/5]
[Zusammenfassung der Security-Erkenntnisse, Stärken, Lücken]

## Compliance-Assessment — Score: [X/5]
[Zusammenfassung der Compliance-Erkenntnisse, gehaltene Zertifizierungen, Lücken]

## Capability-Assessment — Score: [X/5]
[Zusammenfassung der Capability-Erkenntnisse, Eignungsbewertung]

## EU-Datenresidenz-Assessment
[Zusammenfassung der Datenflüsse, Übermittlungsmechanismen, Schrems-II-Erkenntnisse]

## Risikoregister

| # | Risiko | Schweregrad | Eintrittswahrscheinlichkeit | Maßnahme | Verantwortlich | Status |
|---|------|----------|-----------|-----------|-------|--------|
| 1 | [Beschreibung] | [H/M/N] | [H/M/N] | [Maßnahme] | [Name] | [Offen] |

## Freigabe-Auflagen (falls zutreffend)
1. [Auflage — muss vor / innerhalb von X Tagen nach Vertragsunterzeichnung erfüllt sein]
2. [Auflage]

## Review-Zeitplan
- Nächstes Review: [Datum — nach Risikostufe: Kritisch=6 Mon., Hoch=jährlich, Mittel=18 Mon., Niedrig=24 Mon.]
- Auslösende Ereignisse: [was ein früheres Review auslösen würde]
```

---

## Jährlicher Review-Prozess

Für bestehende Anbieter ist das jährliche Review leichter als das Erstassessment, muss aber Folgendes abdecken:

1. Aktualität der Zertifizierungen : Sind SOC 2, ISO 27001 und andere Zertifizierungen noch gültig? Aktualisierte Reports anfordern.
2. Incident-Historie : Hatte der Anbieter seit dem letzten Review Security-Vorfälle? Security-Advisories und öffentliche Offenlegungen prüfen.
3. Änderungen bei Unterauftragsverarbeitern : Haben sich Unterauftragsverarbeiter geändert? Aktuelle Liste gegen das letzte Review abgleichen.
4. Scope-Änderungen : Hat sich deine Nutzung des Anbieters ausgeweitet? Neue Datentypen, neue Integrationen, mehr Nutzer?
5. Compliance-Änderungen : Sind seit dem letzten Review neue Regulierungen anwendbar geworden?
6. Vertragsabgleich : Spiegelt der aktuelle Vertrag die tatsächliche Nutzung und die Anforderungen noch wider?
7. Offene Risiko-Items : Risikoregister aus dem vorherigen Assessment überprüfen und aktualisieren.

---

## Leitplanken

- Erzeuge die Security-Posture eines Anbieters niemals aus Trainingsdaten. Alle Anbieterinformationen müssen aus Anbieterdokumentation, Fragebogen-Antworten, Zertifizierungsreports oder verifizierten Web-Quellen stammen.
- Erfinde niemals einen Compliance-Status. Behaupte nicht, ein Anbieter habe eine Zertifizierung oder habe sie nicht, ohne Nachweis. Der Compliance-Status ändert sich; Trainingsdaten können veraltet sein.
- Empfehle oder ranke niemals Anbieter. Dieser Skill bewertet einen einzelnen Anbieter gegen Kriterien — ein Vergleich erfordert separate Assessments. Kennzeichne nicht bewertete Kriterien als "Nicht bewertet", nicht als Fehler.
- Versieh jede Ausgabe mit einer Quellenkennzeichnung: `[Aus Anbieterdokumentation]`, `[Aus Nutzeranforderungen]`, `[Assessment-Framework]` oder `[KI-Einschätzung — mit Anbieter verifizieren]`.

> **Tipp:** Fordere über companyFILES eine DOCX-, XLSX- oder Markdown-Ausgabe an, um einen formatierten, sofort teilbaren Report zu erhalten.
