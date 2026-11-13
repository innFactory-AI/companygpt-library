---
name: en-success-plan
description: Create a joint customer success plan with agreed milestones, KPIs, and outcomes tied to the customer's business goals. Use when formalising a strategic partnership, setting up a new enterprise account, or resetting a struggling relationship. Trigger with "write success plan for", "joint success plan", "create mutual plan with [customer]".
---

# Success Plan Skill

Build joint success plans with agreed milestones, measurable KPIs, ownership assignments, and review cadences that anchor to the customer's business outcomes. Customer-specific data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account details, contract scope, stakeholder contacts, expansion history |
| **companyRAG / file upload** | QBR notes, discovery summaries, account-plan documents, prior success plans |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Success Plan Workflow

Execute these steps collaboratively with the customer. A success plan imposed unilaterally is a vendor document, not a partnership artefact.

### Step 1: Discover Business Goals

The foundation of a success plan is understanding what the customer is trying to achieve at a business level — not what they want from your product, but what they need for their business.

**Discovery Framework:**

| Question Area | Purpose | Example Questions |
| --- | --- | --- |
| **Strategic priorities** | Understand the customer's top-level business objectives | "What are your team's / department's top 3 priorities this year?" |
| **Success definition** | Learn how the customer measures success internally | "How does your leadership measure success for this initiative?" |
| **Current challenges** | Identify pain points your product can address | "What's the biggest obstacle to achieving [priority]?" |
| **Stakeholder expectations** | Map what different stakeholders need from this partnership | "What does success look like for [executive sponsor / end users / IT]?" |
| **Timeline pressures** | Understand external deadlines or dependencies | "Are there any hard deadlines or business events driving the timeline?" |
| **Previous experience** | Learn from past vendor relationships | "What's worked well in past partnerships? What hasn't?" |

**Critical rule**: Goals must come from the customer, not from your product's feature list. "Increase AI adoption" is a vendor goal; "Reduce contract review cycle time by 30%" is a customer goal.

### Step 2: Define Success Metrics

For each business goal, define measurable KPIs that both sides agree represent success.

**KPI Construction Framework:**

| Element | Definition | Example |
| --- | --- | --- |
| **Metric name** | What is being measured | Contract review cycle time |
| **Baseline** | Current state (measured, not assumed) | Average 5.2 days per contract review |
| **Target** | Agreed goal state | Average 3.0 days per contract review |
| **Measurement method** | How the metric will be tracked | Customer's CLM system report, reviewed monthly |
| **Data owner** | Who is responsible for providing the data | Customer's legal ops team |
| **Review frequency** | How often the metric is assessed | Monthly in CSM check-in; quarterly in QBR |
| **Timeline** | When the target should be achieved | Within 6 months of full deployment |

**KPI Quality Checklist:**

- Is the metric within the customer's and your joint influence? (Don't set KPIs for things neither party controls.)
- Can the metric be reliably measured with available tools? (Don't set KPIs you can't track.)
- Does the customer's leadership recognise this metric as meaningful? (Don't set KPIs only the CSM cares about.)
- Is the target ambitious but achievable? (Unrealistic targets demotivate; easy targets don't demonstrate value.)

### Step 3: Map Milestones

Break each goal into milestones with clear dependencies and ownership.

**Milestone Framework:**

| Element | Definition |
| --- | --- |
| **Milestone name** | Descriptive name for the achievement |
| **Description** | What "done" looks like for this milestone |
| **Dependencies** | What must be true before this milestone can be started |
| **Owner** | Person responsible on each side (your team + customer team) |
| **Target date** | When this milestone should be completed |
| **Success indicator** | How we know the milestone is achieved (not just "completed" — measurable where possible) |
| **Risk factors** | Known risks that could delay this milestone |

Group milestones by goal and sequence them by dependency. Identify the critical path — milestones where a delay cascades to other milestones or the overall timeline.

### Step 4: Assign Ownership

Every element of the success plan needs a clear owner on both sides.

| Role | Responsibilities |
| --- | --- |
| **Executive sponsors** (both sides) | Strategic alignment, unblocking escalations, quarterly review participation |
| **CSM** | Plan ownership, progress tracking, milestone coordination, reporting |
| **Customer project lead** | Internal coordination, resource allocation, milestone delivery on customer side |
| **Subject matter experts** (both sides) | Technical delivery, training, configuration, integration work |

**Ownership principle**: Joint ownership means no ownership. Every milestone has exactly one primary owner — the person who is accountable for its completion — even if multiple people contribute.

### Step 5: Set Review Cadence

Define how and when the success plan is reviewed and updated.

| Review Type | Frequency | Participants | Focus |
| --- | --- | --- | --- |
| **Progress check** | Bi-weekly or monthly | CSM + customer project lead | Milestone status, blockers, adjustments |
| **Quarterly review** | Quarterly (aligned with QBR) | CSM + customer project lead + executive sponsors | Goal progress, KPI assessment, plan evolution |
| **Plan refresh** | Semi-annually or at renewal | Full stakeholder group | Goal relevance, new priorities, next-phase planning |

**Update triggers** (review the plan outside the regular cadence when):

- A business goal changes or a new priority emerges
- A milestone is significantly delayed or blocked
- The customer's organisation changes (M&A, leadership change, restructuring)
- A major product release creates new opportunities
- The account health score changes significantly

## Output Template — Success Plan

```
JOINT SUCCESS PLAN
Account: [name]
Plan owner (CSM): [name]
Customer lead: [name]
Executive sponsors: [your side: name] / [customer side: name]
Created: [date]
Last updated: [date]
Plan period: [start date] — [end date]

CUSTOMER BUSINESS CONTEXT:
  Industry: [industry]
  Strategic priorities: [top 2-3 customer priorities]
  Key challenges: [challenges this plan addresses]

GOAL 1: [Customer's business goal in their language]
  Why it matters: [business impact if achieved]

  Success Metrics:
    KPI: [metric name]
      Baseline: [current value] (measured: [date])
      Target: [goal value]
      Measurement: [how tracked, by whom, how often]

  Milestones:
    M1.1: [milestone name]
      Description: [what done looks like]
      Owner: [name] (your team) + [name] (customer team)
      Target date: [date]
      Dependencies: [list or "none"]
      Status: [Not started / In progress / Complete / At risk]

    M1.2: [milestone name]
      ...

GOAL 2: [Customer's business goal]
  ...

GOAL 3: [Customer's business goal]
  ...

RISKS & MITIGATIONS:
  1. [risk] → [mitigation] → Owner: [name]
  2. ...

REVIEW CADENCE:
  Progress checks: [frequency] — next: [date]
  Quarterly review: next: [date]
  Plan refresh: next: [date]

COMMUNICATION:
  Regular updates: [channel and frequency]
  Escalation path: [how issues are raised]

SIGNATURES / AGREEMENT:
  CSM: [name] — Date: [date]
  Customer lead: [name] — Date: [date]
  (Optional) Executive sponsors: [names]
```

## Customize — Adapt to Your Context

- **Post-onboarding plans:** Focus on adoption goals and time-to-value metrics. Shorter milestone horizons (30/60/90 days).
- **Strategic enterprise plans:** Multi-year horizon with annual goal refresh. Include organisational change management and executive engagement cadence.
- **Renewal recovery plans:** Focus on rebuilding value evidence and addressing specific customer concerns. Shorter review cadence (weekly check-ins until stabilised).
- **Expansion-focused plans:** Include a "future state" section that maps expansion opportunities to business goals.
- **Tech-touch / scaled CS:** Simplify to 1–2 goals with automated milestone tracking. Replace CSM check-ins with in-app progress indicators and automated alerts.

## Guardrails

- Never fabricate customer business goals, priorities, or challenges. These must come from the customer or documented discovery conversations. When data is missing, mark fields as `[DISCOVERY NEEDED]`.
- Never generate baseline metrics or KPI targets without customer data. Mark unknowns as "To be measured" — do not estimate.
- Never present the success plan as final without customer agreement. Flag any section not yet validated with the customer.
- Source-label every element: `[From account data]`, `[From success plan framework]`, `[Customer-stated]`, or `[CSM recommendation]`.

> **Tip:** Ask for DOCX output via companyFILES to get a formatted Word document ready for distribution.
