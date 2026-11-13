---
name: en-compliance-tracking
description: Operational compliance monitoring, gap analysis, and remediation tracking against frameworks and policies. Use when preparing for an audit, monitoring ongoing compliance, or assessing gaps against a framework. Trigger with "track compliance for", "compliance gap analysis", "audit readiness check".
---

# Compliance Tracking Skill

Monitor compliance against frameworks, policies, and standards — gap analysis, remediation tracking, and audit-readiness assessment. For legal interpretation, use the check-compliance or handle-gdpr skills instead. Compliance data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **GRC tools via MCP** (e.g. Vanta, Drata, OneTrust) | Control register, evidence status, framework mappings, maturity ratings |
| **Ticketing via MCP** (e.g. Jira, ServiceNow, Asana) | Remediation items, status, ownership, due dates |
| **companyRAG / file upload** | Policy documents, audit reports, evidence files, framework documentation |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Requirements Identification

### Framework Mapping

Identify all compliance obligations relevant to the scope:

| Source Type | Examples | How to Identify |
| --- | --- | --- |
| **Regulatory** | GDPR, SOX, HIPAA, DORA, NIS2, industry-specific regulations | Legal/compliance team, regulatory register |
| **Contractual** | Customer DPAs, SLAs, vendor agreements, partnership terms | Contract repository, procurement records |
| **Internal policy** | Information security policy, acceptable use, data classification | Policy management system, governance documents |
| **Industry standards** | ISO 27001, SOC 2, PCI DSS, NIST CSF | Certification scope, customer requirements |
| **Voluntary commitments** | ESG frameworks, industry codes of conduct, pledges | Corporate communications, sustainability reports |

### Control Decomposition

For each framework or policy, break requirements into discrete, assessable controls:

```
CONTROL REGISTER ENTRY:
  Control ID:       [unique identifier — use organisation's numbering scheme if one exists]
  Framework:        [source framework or policy]
  Requirement:      [specific clause or section reference]
  Control description: [what must be in place or done — concrete and observable]
  Control type:     [Preventive / Detective / Corrective]
  Control nature:   [Technical / Administrative / Physical]
  Frequency:        [Continuous / Periodic (specify) / Event-driven]
  Owner:            [responsible person or role]
  Evidence type:    [what demonstrates compliance — logs, policies, screenshots, attestations]
```

## Current State Assessment

### Control Effectiveness Rating

Assess each control against a maturity scale:

| Rating | Definition | Evidence Characteristics |
| --- | --- | --- |
| **Not implemented** | Control does not exist or is not operational | No evidence available |
| **Ad hoc** | Control exists but is informal, inconsistent, or person-dependent | Anecdotal evidence only; no documentation |
| **Defined** | Control is documented with clear procedures | Written procedure exists; execution may vary |
| **Managed** | Control is consistently executed and monitored | Consistent evidence; periodic review occurs |
| **Optimised** | Control is continuously improved based on metrics and feedback | Metrics-driven; proactive improvement cycle |

### Assessment Process

For each control in the register:

1. Gather evidence: Collect the evidence type specified in the control register.
2. Evaluate completeness: Does the evidence cover the full scope and time period?
3. Assess effectiveness: Is the control achieving its intended purpose?
4. Rate maturity: Apply the rating scale above based on evidence quality and consistency.
5. Document gaps: Where the control falls short, describe the specific gap.
6. Note dependencies: Identify controls that depend on other controls being effective.

### Assessment Output Format

```
CONTROL ASSESSMENT:
  Control ID:          [from register]
  Control description: [from register]
  Current rating:      [Not implemented / Ad hoc / Defined / Managed / Optimised]
  Target rating:       [organisation's required maturity level]
  Gap:                 [specific shortfall if current < target]
  Evidence reviewed:   [list of evidence items examined]
  Evidence gaps:       [missing or incomplete evidence]
  Risk if unaddressed: [consequence of the gap persisting]
  Assessor:            [who performed the assessment]
  Assessment date:     [when]
```

## Gap Analysis

### Gap Classification

| Gap Type | Definition | Example |
| --- | --- | --- |
| **Design gap** | Control is missing or the design does not address the requirement | No access review process exists for a system that requires quarterly reviews |
| **Operating gap** | Control exists but is not executed consistently or effectively | Access review process exists but was only performed once in the past year |
| **Evidence gap** | Control operates correctly but evidence is insufficient to demonstrate compliance | Access reviews are performed quarterly but results are not documented |
| **Scope gap** | Control covers some but not all in-scope systems, processes, or locations | Access reviews cover production systems but not staging environments |

### Gap Prioritisation Matrix

Prioritise remediation based on regulatory risk and effort:

|  | High Regulatory Risk | Medium Regulatory Risk | Low Regulatory Risk |
| --- | --- | --- | --- |
| **Low Effort** | Immediate — quick win with high value | High — easy to fix, worth doing | Medium — address in normal cycle |
| **Medium Effort** | High — invest resources given risk | Medium — plan and schedule | Low — consider in next cycle |
| **High Effort** | High — must address but plan carefully | Medium — plan for future cycle | Low — deprioritise unless strategic |

Regulatory risk should be assessed by the compliance team, not assumed. When in doubt, classify as higher risk pending expert review.

## Remediation Planning

### Remediation Tracker

For each identified gap:

```
REMEDIATION ITEM:
  Gap ID:            [unique reference linked to control assessment]
  Control ID:        [from register]
  Gap type:          [Design / Operating / Evidence / Scope]
  Gap description:   [specific shortfall]
  Priority:          [from prioritisation matrix]
  Remediation action: [concrete step to close the gap — not "improve the process" but "implement quarterly access review using [tool] covering [scope]"]
  Owner:             [person responsible for remediation]
  Target date:       [completion deadline]
  Status:            [Not started / In progress / Blocked / Complete / Verified]
  Dependencies:      [other actions, approvals, or resources required]
  Verification method: [how completion will be confirmed — evidence required]
  Verification date: [when compliance will be re-assessed post-remediation]
```

### Status Tracking

Aggregate remediation items into a programme-level view:

```
REMEDIATION DASHBOARD — [Date]

Total gaps:           [count]
Not started:          [count] — [% of total]
In progress:          [count] — [% of total]
Blocked:              [count] — [% of total] — [list blockers]
Complete:             [count] — [% of total]
Verified:             [count] — [% of total]

Overdue items:        [count with owners and original target dates]
At-risk items:        [items likely to miss target date]
Next milestone:       [upcoming audit date or reporting deadline]
```

## Audit Readiness Assessment

### Pre-Audit Checklist

When preparing for an internal or external audit:

1. Scope confirmation: Confirm which controls, systems, and time periods are in scope for the audit.
2. Evidence completeness: For each in-scope control, verify evidence exists, is current, and covers the full audit period.
3. Owner preparation: Brief control owners on their responsibilities during the audit — what they may be asked, what evidence they should have ready.
4. Gap remediation status: Identify any open gaps within audit scope — determine whether they can be closed before the audit or must be disclosed.
5. Prior findings: Review findings from the last audit — confirm all remediation actions are complete and verified.
6. Access preparation: Ensure auditors have access to required systems, documentation, and personnel.

### Readiness Score

Produce a readiness assessment per control area:

| Control Area | Controls in Scope | Fully Compliant | Gaps with Remediation | Open Gaps | Readiness |
| --- | --- | --- | --- | --- | --- |
| [area name] | [count] | [count] | [count] | [count] | Green / Amber / Red |

**Scoring**: Green = all controls compliant or gaps remediated; Amber = gaps exist with remediation in progress and expected complete before audit; Red = open gaps unlikely to be resolved before audit.

## Common Framework Reference

This skill supports tracking against any compliance framework. Commonly encountered frameworks include:

| Framework | Typical Scope | Control Domain Examples |
| --- | --- | --- |
| **ISO 27001** | Information security management | Access control, cryptography, operations security, supplier relationships |
| **SOC 2** | Service organisation controls | Security, availability, processing integrity, confidentiality, privacy |
| **GDPR** | Personal data protection | Lawful basis, data subject rights, breach notification, DPIAs |
| **DORA** | Digital operational resilience (financial services) | ICT risk management, incident reporting, resilience testing |
| **NIS2** | Network and information security | Risk management measures, incident handling, supply chain security |
| **PCI DSS** | Payment card data security | Network security, access control, monitoring, encryption |

When the user references a specific framework, map their requirements to the control register structure above. Do not generate framework-specific control lists from training data — use the user's own control mapping or the framework's official documentation.

## Guardrails

- Never generate regulatory requirements or compliance interpretations from training data. All requirements come from the user's compliance team, policies, or framework documentation.
- Never provide legal opinions on compliance status. State the assessment result and recommend verification by qualified compliance professionals.
- Never fabricate audit findings, remediation status, or evidence. All compliance data comes from the user; no compliance-status claim without evidence.
- Label generated content: `[From compliance data]`, `[Framework methodology]`, `[AI assessment — verify with compliance team]`.

> **Tip:** Ask for XLSX, DOCX, or Markdown output via companyFILES to get a formatted document ready to share.
