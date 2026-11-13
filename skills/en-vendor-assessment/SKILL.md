---
name: en-vendor-assessment
description: Evaluates vendors against security, compliance, capability, and operational criteria and produces structured assessment reports. Use it when onboarding a new SaaS tool, running annual vendor reviews, or responding to procurement requests. Trigger with "assess this vendor", "vendor security review", "should we use [tool]".
---

# Vendor Assessment Skill

Evaluate technology vendors against security, compliance, capability, and operational criteria. Aligned with ISO 27001 supplier management and NIST CSF supply chain risk management. Vendor-specific data comes from you, a connected MCP source, companyRAG collections, or uploaded files.

## Where the Data Comes From

| Source | What it contributes |
| --- | --- |
| **Procurement/GRC tool via MCP** (e.g. ServiceNow, OneTrust, Vanta) | Vendor master data, existing risk ratings, contract and procurement status |
| **Ticketing via MCP** (e.g. Jira, ServiceNow) | Open risk items, prior assessment tickets, incident history |
| **companyRAG collections / file upload** | Vendor documentation, questionnaire responses (CAIQ, SIG, VSAQ), SOC 2 / ISO reports, DPA and contracts |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Assessment Workflow

Execute these phases in order for every vendor assessment:

### Phase 1: Scoping

Define the assessment scope before evaluating anything:

1. Use case : What will this vendor/tool be used for? Which teams? Which workflows?
2. Data classification : What categories of data will the vendor access or process? (Public, Internal, Confidential, Restricted/PII/PHI)
3. Integration depth : Standalone tool, API integration, SSO-connected, data sync, or embedded in critical path?
4. User population : How many users? Which roles? Self-service or admin-managed?
5. Criticality : If this vendor were unavailable for 24h, what is the business impact? (Informational, Operational impact, Revenue impact, Business-critical)
6. Regulatory context : Which regulations apply to the data or process? (GDPR, NIS2, DORA, AI Act, industry-specific)

The scoping answers determine which sections of the assessment are mandatory vs. optional and how deep each section needs to go.

### Phase 2: Security Assessment

Evaluate the vendor's security posture across these domains:

#### Authentication and Access Control

| Criterion | Requirement | Scoring |
| --- | --- | --- |
| SSO support | SAML 2.0 or OIDC integration | Required for Confidential+ data |
| MFA enforcement | Enforced MFA for all users, including admin | Required for all tiers |
| RBAC/ABAC | Granular role-based access with least-privilege defaults | Required for Confidential+ |
| Admin audit trail | Immutable log of admin actions with timestamps | Required for Confidential+ |
| API authentication | OAuth 2.0, API keys with rotation, or mutual TLS | Required if API integration |
| Session management | Configurable timeout, concurrent session limits | Recommended |
| SCIM provisioning | Automated user lifecycle management | Required for >50 users |

#### Data Protection

| Criterion | Requirement | Scoring |
| --- | --- | --- |
| Encryption at rest | AES-256 or equivalent, customer-managed keys option | Required for Confidential+ |
| Encryption in transit | TLS 1.2+ enforced, no fallback to weaker protocols | Required for all tiers |
| Data isolation | Logical or physical tenant isolation documented | Required for Confidential+ |
| Backup and recovery | Documented backup frequency, retention, tested recovery | Required for Operational+ criticality |
| Data deletion | Documented deletion process, timeline, and certification on contract end | Required for GDPR scope |
| Key management | HSM-backed, documented key rotation schedule | Required for Restricted data |

#### Infrastructure Security

| Criterion | Requirement | Scoring |
| --- | --- | --- |
| Hosting environment | Documented cloud provider, region(s), architecture overview | Required for all tiers |
| Vulnerability management | Regular scanning, documented patching cadence | Required for all tiers |
| Penetration testing | Annual third-party pentest with remediation evidence | Required for Confidential+ |
| Incident response | Documented IR plan with defined notification timelines | Required for all tiers |
| Business continuity | Documented BCP/DR with tested RTO/RPO | Required for Operational+ criticality |
| Network security | WAF, DDoS protection, network segmentation | Required for Confidential+ |

#### Security Questionnaire Approach

When sending a security questionnaire to the vendor, structure it around the domains above. Accept industry-standard questionnaires (CAIQ, SIG, VSAQ) as valid responses -- do not force vendors to duplicate effort. Map their responses to your assessment criteria rather than requiring your exact format.

### Phase 3: Compliance Assessment

#### Certifications and Attestations

| Certification | What It Covers | Verification |
| --- | --- | --- |
| **SOC 2 Type II** | Security, availability, processing integrity, confidentiality, privacy controls over a period (typically 12 months) | Request current report. Check report period, scope, and any exceptions noted. Type I (point-in-time) is significantly less valuable than Type II. |
| **ISO 27001** | Information security management system | Request certificate. Verify scope covers the relevant service (not just corporate HQ). Check the Statement of Applicability for excluded controls. |
| **ISO 27701** | Privacy information management (extends ISO 27001) | Request certificate. Relevant for GDPR processor compliance. |
| **CSA STAR** | Cloud-specific security (based on CAIQ/CCM) | Level 1 (self-assessment) vs. Level 2 (third-party audit) -- Level 2 is materially stronger. |
| **ISAE 3402 / SSAE 18** | Service organization controls (financial focus) | Relevant for financial data processing. Check report scope. |
| **C5 (BSI)** | Cloud security attestation (German federal standard) | Increasingly expected by German public sector and regulated industries. |

A certification is a starting point, not an endpoint. Always verify: (1) the scope covers the service you are evaluating, (2) the report period is current, and (3) any exceptions or qualifications are reviewed.

#### GDPR Compliance

| Criterion | Requirement | Reference |
| --- | --- | --- |
| Data Processing Agreement | DPA compliant with Article 28(3) requirements | GDPR Art. 28 |
| Lawful basis | Documented legal basis for processing | GDPR Art. 6 |
| Data subject rights | Process for handling DSARs within 30-day timeline | GDPR Art. 15-22 |
| Breach notification | Notification within timeframe enabling controller to meet 72h DPA obligation | GDPR Art. 33 |
| Sub-processor management | List of sub-processors, notification mechanism for changes, right to object | GDPR Art. 28(2) |
| Records of processing | Maintained as required for processors | GDPR Art. 30(2) |
| DPO designation | DPO appointed where required | GDPR Art. 37 |
| International transfers | Valid transfer mechanism in place (see EU data residency section) | GDPR Ch. V |

#### EU Data Residency and Transfer

This section is critical for EU-based organizations and must be thoroughly assessed for any vendor processing personal data.

| Criterion | Assessment |
| --- | --- |
| **Data storage location** | In which country/region is data stored at rest? EU/EEA storage is simplest. |
| **Data processing location** | Where is data processed? May differ from storage (e.g., stored in EU, processed via US-based service). |
| **Sub-processor locations** | Where are sub-processors located? A single non-EU sub-processor can trigger transfer requirements. |
| **Transfer mechanism** | If data leaves EU/EEA: adequacy decision, EU SCCs (Commission Implementing Decision 2021/914), BCRs, or other valid mechanism. For US transfers: verify current framework status and vendor participation. |
| **Transfer Impact Assessment** | Has the vendor conducted a TIA for non-EU transfers? Can they provide it? |
| **Government access risk** | For non-EU jurisdictions: risk of government access to data (surveillance laws, national security orders). Assess per Schrems II requirements. |
| **Data localization option** | Can the vendor offer EU-only data processing? At what cost or feature limitation? |

**Schrems II Practical Checklist:**

1. Map all data flows to/from non-EU countries
2. Identify the legal basis for each transfer
3. Assess the laws of the destination country regarding government access
4. Determine if supplementary measures are needed (encryption, pseudonymization, contractual commitments)
5. Document the assessment and review periodically

### Phase 4: Capability Assessment

Evaluate the vendor's fitness for the intended use case:

| Category | Assessment Criteria |
| --- | --- |
| **Functional fit** | Does the tool meet the stated requirements? Gap analysis against must-have vs. nice-to-have features. |
| **Integration capability** | API availability, webhook support, standard protocols, existing connectors to your stack. |
| **Scalability** | Can the solution grow with your usage? Rate limits, user limits, data volume constraints. |
| **Reliability** | Published uptime SLA, historical uptime data, incident history (check status page archives). |
| **Support** | Support tiers, response time SLAs, support hours, escalation path, dedicated account management. |
| **Roadmap alignment** | Does the vendor's product direction align with your future needs? Assess concentration risk if you depend on an unbuilt feature. |
| **Vendor viability** | Financial stability, funding stage, customer base size, market position. A brilliant tool from a vendor that may not exist in 18 months is a risk. |
| **Exit strategy** | Data export capability, API access for bulk extraction, standard data formats, contractual data return provisions. |

### Phase 5: Risk Classification

Combine the assessment results into an overall risk classification:

| Risk Level | Criteria | Approval Path |
| --- | --- | --- |
| **Low** | Public data only, standalone tool, no integration, informational use | Team lead approval |
| **Medium** | Internal data, limited integration, operational but not critical | IT manager + data owner approval |
| **High** | Confidential data, deep integration, significant user population, hard to replace | CISO + legal review + management approval |
| **Critical** | Restricted/PII data, business-critical dependency, regulatory implications | CISO + DPO + legal + executive approval |

### Risk Scoring Matrix

For each assessment domain, score on a 1-5 scale:

| Score | Meaning |
| --- | --- |
| 5 | Fully meets requirements, evidence-backed, no gaps |
| 4 | Meets requirements with minor gaps, roadmap items, or documentation weaknesses |
| 3 | Partially meets requirements, material gaps exist but are manageable with compensating controls |
| 2 | Significant gaps, compensating controls are costly or complex |
| 1 | Does not meet requirements, blocking gaps with no viable compensating controls |

Aggregate scores by domain (Security, Compliance, Capability) and produce an overall vendor risk score. Weight the domains based on scoping answers from Phase 1 — a vendor handling Restricted data should weight Security and Compliance higher than Capability.

---

## Assessment Report Template

```
# Vendor Assessment Report

**Vendor**: [name]
**Product/Service**: [specific product being assessed]
**Assessment date**: [date]
**Assessor**: [name/team]
**Assessment type**: [New vendor / Annual review / Triggered review]

## Executive Summary

**Overall risk classification**: [Low / Medium / High / Critical]
**Recommendation**: [Approve / Approve with conditions / Defer pending remediation / Reject]
**Key findings**: [3-5 bullet points of the most significant findings]

## Scoping

- Use case: [description]
- Data classification: [Public / Internal / Confidential / Restricted]
- Integration depth: [Standalone / API / SSO / Data sync / Critical path]
- Criticality: [Informational / Operational / Revenue / Business-critical]
- Regulatory scope: [applicable regulations]

## Security Assessment — Score: [X/5]
[Summary of security findings, strengths, gaps]

## Compliance Assessment — Score: [X/5]
[Summary of compliance findings, certifications held, gaps]

## Capability Assessment — Score: [X/5]
[Summary of capability findings, fit assessment]

## EU Data Residency Assessment
[Data flow summary, transfer mechanisms, Schrems II findings]

## Risk Register

| # | Risk | Severity | Likelihood | Mitigation | Owner | Status |
|---|------|----------|-----------|-----------|-------|--------|
| 1 | [description] | [H/M/L] | [H/M/L] | [action] | [name] | [Open] |

## Conditions for Approval (if applicable)
1. [Condition — must be met before / within X days of contract signing]
2. [Condition]

## Review Schedule
- Next review: [date — based on risk level: Critical=6mo, High=annual, Medium=18mo, Low=24mo]
- Trigger events: [what would trigger an earlier review]
```

---

## Annual Review Process

For existing vendors, the annual review is lighter than initial assessment but must cover:

1. Certification currency : Are SOC 2, ISO 27001, and other certifications still current? Request updated reports.
2. Incident history : Has the vendor had any security incidents since last review? Check their security advisories and public disclosures.
3. Sub-processor changes : Have sub-processors changed? Review the current list against the last review.
4. Scope changes : Has your usage of the vendor expanded? New data types, new integrations, more users?
5. Compliance changes : Have new regulations become applicable since last review?
6. Contract alignment : Does the current contract still reflect actual usage and requirements?
7. Open risk items : Review and update the risk register from the prior assessment.

---

## Guardrails

- Never generate vendor security posture from training data. All vendor information must come from vendor documentation, questionnaire responses, certification reports, or verified web sources.
- Never fabricate compliance status. Do not claim a vendor has or lacks a certification without evidence. Compliance status changes; training data may be outdated.
- Never recommend or rank vendors. This skill evaluates one vendor against criteria — comparison requires separate assessments. Mark unevaluated criteria as "Not assessed," not as failures.
- Source-label all output : [From vendor documentation] , [From user requirements] , [Assessment framework] , or [AI assessment — verify with vendor] .

> **Tip:** Ask for DOCX, XLSX, or Markdown output via companyFILES to get a formatted, instantly shareable report.
