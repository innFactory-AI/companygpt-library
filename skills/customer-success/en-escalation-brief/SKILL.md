---
name: en-escalation-brief
description: Package a customer issue into a structured escalation brief for engineering or leadership with business impact quantified. Use when a customer issue needs executive attention, engineering prioritisation, or cross-functional coordination. Trigger with "escalate this issue", "package escalation for", "this needs engineering attention".
---

# Escalation Brief Skill

Turn customer issues into structured escalation briefs that quantify business impact and recommend specific actions. Issue details come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Support platform via MCP** (e.g. Zendesk, Intercom, Freshdesk) | Ticket history, resolution attempts, customer communication log |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account value, renewal date, strategic importance, stakeholder contacts |
| **companyRAG / file upload** | Internal notes, prior escalations, technical context |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Escalation Packaging Workflow

Execute these steps in order for every escalation.

### Step 1: Assess Severity

Classify the issue using two dimensions: customer impact and business risk.

**Customer Impact:**

| Level | Definition | Examples |
| --- | --- | --- |
| **Critical** | Customer's core workflow is blocked with no workaround | Platform outage, data loss, security breach, complete feature failure |
| **High** | Significant degradation affecting multiple users or key workflows | Performance issues, partial feature failure, integration breakdown |
| **Medium** | Noticeable issue with a viable workaround available | UI bugs, minor feature gaps, non-critical integration issues |
| **Low** | Cosmetic or minor issue, not blocking any workflow | Display glitches, documentation gaps, enhancement requests |

**Business Risk:**

| Level | Definition | Indicators |
| --- | --- | --- |
| **Critical** | Immediate churn or legal risk | Customer has threatened non-renewal, legal action, or public disclosure |
| **High** | Renewal or expansion at risk | Customer approaching renewal with unresolved issues, expansion deal stalled |
| **Medium** | Relationship damage but no immediate commercial risk | Customer frustration growing, NPS declining, champion losing credibility internally |
| **Low** | Isolated issue, relationship stable | One-off problem, customer understanding, no pattern |

**Combined severity** = highest of the two dimensions. A medium customer impact with critical business risk is a critical escalation.

### Step 2: Gather Context

Build a complete picture before drafting the brief. Incomplete escalations get deprioritised.

| Context Element | Source | Detail |
| --- | --- | --- |
| **Issue description** | Support ticket, CSM notes | What is happening, when it started, who is affected |
| **Timeline** | Support platform | When reported, resolution attempts made, current status |
| **Affected scope** | Customer, support data | Number of users impacted, which features/workflows, frequency |
| **Workaround status** | Support team | Is a workaround in place? Is the customer using it? Is it sustainable? |
| **Resolution attempts** | Support ticket history | What has been tried, by whom, with what result |
| **Customer expectation** | CSM, customer communication | What the customer expects in terms of timeline and resolution |
| **Related issues** | Support platform, engineering | Is this a known bug? Are other customers affected? Is there an existing ticket? |

### Step 3: Quantify Business Impact

Translate the issue into terms that drive internal prioritisation. Engineering and leadership respond to business impact, not frustration levels.

| Impact Dimension | Quantification Approach |
| --- | --- |
| **Revenue at risk** | ARR of affected account(s). If renewal is within 90 days, flag explicitly. |
| **User impact** | Number of affected users × frequency of impact. Daily blockers weigh more than weekly inconveniences. |
| **Strategic value** | Is this a logo account, reference customer, expansion target, or strategic segment? |
| **Ripple risk** | Are other customers affected or likely to be? Is this a systemic issue? |
| **Contractual exposure** | Are there SLA commitments being violated? Penalty clauses at risk? |
| **Relationship capital** | How much goodwill has been spent? Has the CSM or executive already made commitments? |

Use actual numbers from CRM and support data. Never estimate revenue or contract values from memory.

### Step 4: Draft the Escalation Brief

Use the output template below. Every field must be completed or explicitly marked as unknown.

### Step 5: Recommend Action

Based on severity and context, recommend a specific response.

| Severity | Recommended Response | Internal Routing |
| --- | --- | --- |
| **Critical** | War room / immediate engineering attention + executive sponsor notification | Engineering lead + CS leadership + account executive |
| **High** | Priority engineering ticket + CSM-led customer communication plan | Engineering manager + CS manager |
| **Medium** | Engineering ticket with business context + CSM follow-up cadence | Engineering team via standard queue with priority flag |
| **Low** | Standard support/engineering queue with context attached | Support team or product backlog |

## Output Template — Escalation Brief

```
ESCALATION BRIEF
Date: [date]
Prepared by: [CSM name]
Severity: [CRITICAL / HIGH / MEDIUM / LOW]

ACCOUNT CONTEXT:
  Account: [name]
  ARR: [value]
  Renewal date: [date]
  Strategic tier: [enterprise / mid-market / SMB]
  Account health: [from health score if available]
  Account owner: [CSM name]
  Executive sponsor: [name, if assigned]

ISSUE SUMMARY:
  [2-3 sentence description of the issue in plain language]

CUSTOMER IMPACT:
  Impact level: [Critical / High / Medium / Low]
  Users affected: [number]
  Workflows blocked: [list]
  Workaround available: [Yes — describe / No]
  Duration: [how long the issue has persisted]

BUSINESS RISK:
  Risk level: [Critical / High / Medium / Low]
  Revenue at risk: [ARR amount]
  Renewal proximity: [X days until renewal]
  Strategic factors: [reference customer, expansion opportunity, etc.]
  Contractual exposure: [SLA violations, penalty risk]

TIMELINE:
  [date] — Issue first reported
  [date] — [resolution attempt and result]
  [date] — [escalation trigger / what changed]
  [date] — Current status

RESOLUTION ATTEMPTS:
  1. [what was tried] → [result]
  2. [what was tried] → [result]

CUSTOMER EXPECTATION:
  [What the customer expects and by when]

REQUESTED ACTION:
  [Specific ask — e.g., "Engineering root cause analysis within 48 hours"
   or "Executive call to reset expectations by Friday"]

RECOMMENDED INTERNAL ROUTING:
  Engineering: [team/person]
  CS leadership: [person]
  Account executive: [person, if commercial risk]
  Executive: [person, if critical severity]

SUPPORTING MATERIALS:
  - [Link to support ticket]
  - [Link to CRM account]
  - [Screenshots, logs, or other evidence]
```

## Anti-Patterns — Common Escalation Mistakes

| Anti-Pattern | Why It Fails | Instead |
| --- | --- | --- |
| Escalating emotion instead of facts | "The customer is really upset" provides no actionable information | Quantify the impact: users affected, revenue at risk, duration |
| Skipping resolution history | Engineering wastes time re-investigating known dead ends | Document every attempt and its result |
| Vague impact statements | "This is a big account" does not convey urgency | State the ARR, renewal date, and strategic tier explicitly |
| Escalating without a specific ask | Recipients don't know what action to take | State exactly what you need and by when |
| Over-escalating low-severity issues | Erodes credibility for future escalations | Use the severity matrix honestly; not every issue is critical |

## Guardrails

- Never fabricate account values, revenue figures, renewal dates, or ticket details. All data must come from the user, CRM, or support platform. State "unknown — investigation needed" for missing data.
- Never assume the customer's emotional state. Report observable signals (what they said, ticket volume, meeting cancellations) rather than inferred feelings.
- Escalation briefs must be reviewed by the CSM before submission. Never auto-submit.
- Source-label every assertion: `[From account data]`, `[From escalation framework]`, or `[CSM assessment]`.

> **Tip:** Ask for DOCX output via companyFILES to get a formatted escalation brief ready to send.
