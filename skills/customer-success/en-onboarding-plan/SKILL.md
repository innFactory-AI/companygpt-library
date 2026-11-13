---
name: en-onboarding-plan
description: Build a structured customer onboarding plan with milestones, owner assignments, and 30/60/90-day success checkpoints. Use when kicking off a new customer, redesigning an onboarding process, or scaling CSM capacity. Trigger with "create onboarding plan for", "new customer setup", "30/60/90 plan for [customer]".
---

# Onboarding Plan Skill

Build milestone-driven onboarding plans that move a new customer from signed contract to first realised value. Customer-specific data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account details, contract scope, ARR, key contacts, closed-won notes |
| **Project tracker via MCP** (e.g. Asana, Monday, Jira, Notion) | Task tracking, milestone status, owner assignments |
| **companyRAG / file upload** | Sales-handoff notes, discovery-call summaries, technical assessments |

> **No connected source?** Provide the inputs in chat or upload the relevant files — the plan works as a standalone document.

## Onboarding Planning Workflow

Run these steps in order for every new onboarding plan.

### Step 1: Gather Requirements

Before building the plan, collect these inputs. Flag any gaps — incomplete requirements cause rework later.

| Input | Source | Why It Matters |
| --- | --- | --- |
| **Contract scope** | CRM / sales handoff | Defines what the customer purchased and what must be delivered |
| **Customer business goals** | Sales notes, discovery calls | Anchors milestones to outcomes the customer actually cares about |
| **Technical environment** | Pre-sales technical assessment | Determines integration complexity and technical milestones |
| **Customer team** | Sales handoff, CRM contacts | Identifies stakeholders, decision-makers, and day-to-day contacts |
| **Timeline constraints** | Contract, customer request | Hard deadlines (e.g. go-live before fiscal year end) shape the plan |
| **Known risks** | Sales handoff notes | Concerns flagged during the sales process (e.g. limited IT resources) |
| **Success criteria** | Customer-stated or jointly defined | What "done" looks like from the customer's perspective |

### Step 2: Define Onboarding Phases

Structure the plan into three phases with clear entry and exit criteria.

**Phase 1 — Foundation (Days 1–30)**

| Element | Detail |
| --- | --- |
| **Goal** | Technical setup complete, key stakeholders onboarded, first value demonstrated |
| **Entry criteria** | Contract signed, sales-to-CS handoff completed |
| **Key milestones** | Kickoff call, technical setup, admin training, initial configuration, first use case live |
| **Exit criteria** | Core platform configured, admin users trained, at least one use case operational |

**Phase 2 — Adoption (Days 31–60)**

| Element | Detail |
| --- | --- |
| **Goal** | Broader team adoption, workflows established, early ROI evidence |
| **Entry criteria** | Phase 1 exit criteria met |
| **Key milestones** | End-user training, workflow configuration, adoption check-in, usage review |
| **Exit criteria** | Target activation rate achieved, core workflows running, initial success metrics captured |

**Phase 3 — Optimisation (Days 61–90)**

| Element | Detail |
| --- | --- |
| **Goal** | Full deployment, value confirmed, transition to steady-state relationship |
| **Entry criteria** | Phase 2 exit criteria met |
| **Key milestones** | Advanced feature enablement, success-metric review, executive sponsor check-in, formal handoff to ongoing CS |
| **Exit criteria** | Success criteria from Step 1 achieved, ongoing cadence established, success plan drafted |

### Step 3: Assign Ownership

Every milestone needs a clear owner on both sides — your team and the customer's.

| Role | Responsibilities | Typical Owner |
| --- | --- | --- |
| **CSM** | Overall plan ownership, relationship management, milestone tracking, escalation | Your team |
| **Implementation / Solutions** | Technical setup, configuration, integrations, data migration | Your team |
| **Trainer** | Admin and end-user training delivery | Your team |
| **Customer Project Lead** | Internal coordination, resource availability, decision-making | Customer team |
| **Customer IT / Admin** | Technical access, environment setup, security review | Customer team |
| **Executive Sponsor** (both sides) | Strategic alignment, unblocking escalations, success validation | Both teams |

For smaller accounts, one person may fill several roles. For enterprise accounts, expand roles as needed (e.g. a dedicated data-migration lead or change-management lead).

### Step 4: Set Success Checkpoints

Schedule formal checkpoints at each phase boundary and at the 90-day mark.

| Checkpoint | Timing | Attendees | Agenda |
| --- | --- | --- | --- |
| **Kickoff** | Day 1–5 | All stakeholders | Introductions, plan review, goal confirmation, timeline alignment |
| **30-day review** | Day 28–32 | CSM, customer project lead, sponsors (optional) | Phase 1 milestone review, issue resolution, Phase 2 readiness |
| **60-day review** | Day 58–62 | CSM, customer project lead | Adoption metrics review, workflow effectiveness, Phase 3 planning |
| **90-day review** | Day 88–92 | CSM, customer project lead, executive sponsors | Success-criteria assessment, value summary, transition to ongoing cadence |

Each checkpoint produces a documented outcome: milestones achieved, milestones delayed (with new dates), open issues, and agreed next steps.

### Step 5: Create a Communication Cadence

Define how and when you communicate throughout onboarding.

| Communication | Frequency | Channel | Owner |
| --- | --- | --- | --- |
| **Status update** | Weekly | Email or shared document | CSM |
| **Working sessions** | As needed per milestones | Video call | Implementation lead |
| **Escalation** | As needed | Direct message + email | CSM or customer project lead |
| **Checkpoint review** | At phase boundaries | Video call with agenda | CSM |

Adapt the cadence to the customer — some prefer async updates, others want weekly syncs. Ask at kickoff.

## Output Template — Onboarding Plan

```
CUSTOMER ONBOARDING PLAN
Account: [name]
CSM: [name]
Start date: [date]
Target completion: [date — typically 90 days from start]
Contract scope: [brief summary of what was purchased]
Success criteria: [customer-stated definition of success]

PHASE 1 — FOUNDATION (Days 1–30)
Goal: [specific to this customer]
  Milestone 1: [description]
    Owner: [name/role] | Due: [date] | Status: [Not started / In progress / Complete]
  Milestone 2: [description]
    Owner: [name/role] | Due: [date] | Status: [...]
  ...
  Exit criteria: [what must be true to move to Phase 2]
  30-day checkpoint: [date]

PHASE 2 — ADOPTION (Days 31–60)
Goal: [specific to this customer]
  Milestone 1: [description]
    Owner: [name/role] | Due: [date] | Status: [...]
  ...
  Exit criteria: [what must be true to move to Phase 3]
  60-day checkpoint: [date]

PHASE 3 — OPTIMISATION (Days 61–90)
Goal: [specific to this customer]
  Milestone 1: [description]
    Owner: [name/role] | Due: [date] | Status: [...]
  ...
  Exit criteria: [what must be true to consider onboarding complete]
  90-day checkpoint: [date]

RISKS & MITIGATIONS:
  1. [risk] → [mitigation plan] → Owner: [name]
  2. ...

COMMUNICATION CADENCE:
  [as defined in Step 5]

STAKEHOLDER MAP:
  Your team:     [name — role, name — role, ...]
  Customer team: [name — role, name — role, ...]
```

## Adapt to Your Business

The 30/60/90 framework is a default. Adjust it for your product and customer profile:

- **Simple product, SMB customer:** compress to 14/30/45 days, fewer milestones, lighter checkpoints.
- **Complex platform, enterprise customer:** extend to 30/60/90/120 days; add a Phase 0 (pre-kickoff prep) and a Phase 4 (advanced enablement).
- **Usage-based product:** replace time-based phase gates with usage-based triggers (e.g. Phase 2 starts at X active users, not at day 31).
- **Multi-product deployment:** create parallel tracks per product with a shared timeline and consolidated checkpoints.
- **High-touch vs. tech-touch:** for pooled onboarding, replace individual milestones with automated triggers (welcome sequence, in-app guides, self-serve training) and scheduled group check-ins.

## Guardrails

- Never fabricate customer requirements, technical environments, or business goals. All customer-specific details must come from the user or connected data. When data is missing, generate clearly marked placeholder fields.
- Never assume the customer's team structure or resource availability. Ask; do not infer.
- Never generate specific adoption metrics or usage targets without customer data.
- Source-label every element: `[From account data]`, `[From onboarding framework]`, or `[CSM input needed]`.

> **Tip:** Ask for DOCX or XLSX output via companyFILES to get a formatted plan ready to share.
