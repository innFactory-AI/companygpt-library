---
name: en-deal-strategy
description: Map stakeholder power dynamics, surface deal risks, and recommend a step-by-step engagement strategy. Use when entering a complex deal, preparing for an executive sponsor meeting, or diagnosing a stuck opportunity. Trigger with "plan deal strategy for", "stakeholder map", "how do I advance this deal".
---

# Deal Strategy Skill

Map stakeholders, score their influence, plan multi-threading, and detect organisational change signals. The skill produces stakeholder maps, engagement strategies, and Mutual Action Plans. All contact data, org charts, and relationship context comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account details, contacts, org charts, opportunity stage, activity history |
| **Communication tools via MCP** (e.g. email, calendar, Slack) | Interaction history, last touchpoints, engagement trend per stakeholder |
| **companyRAG / file upload** | Discovery-call notes, relationship mapping, account plans, competitive context |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Relationship Complexity Assessment

Assess the account's relationship complexity. The primary routing dimension is stakeholder count, informed by the Sales Motion Complexity Assessment shared across sales skills (cycle length, deal value, stakeholder count, solution complexity — all relative to the customer's own norms).

```
  FEW stakeholders (single contact or small buying center)
    --> LIGHTWEIGHT stakeholder tracking
    --> Simple contact list (role, influence level, last interaction)
    --> Next-steps tracking
    --> Basic engagement cadence

  MODERATE stakeholder group (multi-contact, defined buying center)
    --> STANDARD stakeholder mapping
    --> Stakeholder map with role classification and influence scoring
    --> Milestone-based action tracking
    --> Structured engagement plan

  LARGE stakeholder group (complex org, multiple departments/divisions)
    --> FULL stakeholder strategy
    --> Complete power/influence matrix with org chart navigation
    --> Mutual Action Plans with buyer/seller milestones
    --> Multi-threading plan across departments
    --> Organizational change monitoring
```

## Stakeholder Mapping Methodology

### Role Classification

Classify each stakeholder by role and define the engagement strategy. These are archetypes, not rigid categories — one person may fill multiple roles, and not all roles exist in every deal or account:

| Role | Engagement Strategy |
| --- | --- |
| **Champion** | Equip with ammunition (business case, proof points). Protect the relationship. Regular check-ins. |
| **Coach** | Cultivate trust. Ask for organizational intelligence. Never expose them politically. |
| **Economic Buyer** | Communicate in business outcomes, not features. Engage at strategic moments (budget cycles, renewals, expansions). |
| **Technical Evaluator** | Provide technical depth. Address concerns directly. Involve in proof-of-concept or pilot design. |
| **Blocker** | Understand their concerns (often legitimate). Address root objections. Engage through the champion if the direct approach fails. |
| **End User** | Ensure adoption success. Collect usage feedback. Use satisfaction as expansion leverage. |

**Cultural context**: Engagement strategies assume direct-access norms. In hierarchical cultures (e.g. Japan, Korea, Middle East), adjust for: protocol-driven access (introductions through proper channels), seniority-first engagement, and indirect communication preferences. Consult the account owner or local team for cultural guidance.

### Influence Scoring (1–5)

Score each stakeholder's organizational influence from 1 (minimal — informational only) to 5 (decision authority — can approve or veto independently).

### Relationship Strength (1–5)

Score the current relationship from 1 (no relationship) to 5 (active advocate who champions internally).

**For lightweight accounts**: Track role, influence level (High/Medium/Low), and last interaction date only. Skip the full matrix.

**Power/influence matrix** (standard/full): rows for each stakeholder with columns for role, influence (1–5), relationship strength (1–5), stance (support/neutral/block), last touchpoint, and next planned action. **Multi-threading**: ensure parallel coverage across Champion, Economic Buyer, and Technical Evaluator (and procurement at renewal); map dependencies between milestones. **Organizational change signals**: role changes, M&A, reorgs, new procurement involvement, champion departure, or sudden stakeholder silence — treat as triggers to refresh the map and reassess risk.

## Action Tracking Methodology

Scaled by relationship complexity:

**Lightweight (few stakeholders)**:

- Next-steps list: action, owner, due date
- Track in conversation or CRM task

**Standard (moderate stakeholder group)**:

- Milestone-based tracking: key milestones with dependencies
- Shared informally with the customer
- Stall detection: flag milestones overdue beyond a threshold proportional to deal cycle length (e.g. 5–10% of typical cycle)

**Full (large stakeholder group)**:

- Mutual Action Plan (MAP): joint plan with buyer and seller milestones
- Shared success criteria agreed with the customer
- Timeline with dependencies and critical path
- Stall detection triggers: milestone overdue, stakeholder unresponsive, requirements changing without MAP update

## Renewal/Retention Stakeholder Dynamics

Stakeholder maps shift at renewal and retention milestones:

- Procurement gains influence: At renewal, procurement often enters or gains weight. Map them early in the renewal cycle.
- Champion continuity risk: The original champion may have changed roles or left. Verify champion status before renewal.
- New stakeholders: Usage expansion may have introduced new departments or users not in the original map. Update the map before renewal conversations.
- Value validation: At renewal, the Economic Buyer needs evidence of value delivered. Prepare metrics and business outcomes for the renewal conversation.

## Stakeholder Health Assessment

**Full methodology** (standard and full complexity):

| Factor | Assessment |
| --- | --- |
| **Relationship coverage** | Key roles filled? Gaps in Champion, Economic Buyer, or Technical Evaluator = risk. |
| **Influence balance** | Are your strongest relationships with high-influence stakeholders? Or only with low-influence contacts? |
| **Engagement trend** | Direction of interaction frequency and depth across stakeholders (improving, stable, declining). |
| **Champion strength** | Is the champion equipped, active, and politically safe? Champion loss = highest-risk event. |
| **Blocker status** | Are blockers' concerns addressed or escalating? |

**Simplified (lightweight)**: Is the primary contact engaged and responsive? Green / Yellow / Red.

## Output Template — Stakeholder Strategy

```
STAKEHOLDER STRATEGY
Account: [name]
Opportunity: [name / stage]
Complexity: [Lightweight / Standard / Full]

STAKEHOLDER MAP:
  Stakeholder 1: [name — role]
    Influence: [1–5] | Relationship strength: [1–5] | Stance: [support/neutral/block]
    Last touchpoint: [date] | Next action: [description]
  Stakeholder 2: [name — role]
    ...

MULTI-THREADING COVERAGE:
  Champion:            [name or "No data available — requires input"]
  Economic Buyer:      [name or "No data available — requires input"]
  Technical Evaluator: [name or "No data available — requires input"]

ENGAGEMENT STRATEGY:
  [per stakeholder: recommended next step, source label]

RISKS & SIGNALS:
  1. [risk/signal] → [recommendation] → Owner: [name]
  2. ...

MUTUAL ACTION PLAN (if standard/full):
  [buyer/seller milestones with dates and dependencies]
```

## Reference Material

- Relationship-mapping guide — use when mapping deal stakeholders. Upload it as a file or store it in a companyRAG collection so the skill can draw on it.

## Guardrails

1. Never fabricate stakeholder data. All contact information, org charts, and relationship details must come from you, the CRM, or a companyRAG collection.
2. "No data available" defaults. For any field without data, display "No data available — requires input."
3. Source labeling. Tag assertions — `[From account data]`, `[From mapping framework]`, `[AI recommendation]`.
4. Verification disclaimer. Include "Verify stakeholder information with account owner" on all maps. Org structures change.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted stakeholder strategy ready to share.
