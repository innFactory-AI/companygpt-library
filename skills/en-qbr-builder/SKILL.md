---
name: en-qbr-builder
description: Build quarterly business review content with usage trends, ROI highlights, mutual success metrics, and agreed next steps. Use when preparing for a customer QBR, building executive-level account summaries, or demonstrating product value. Trigger with "build QBR for", "quarterly review for [customer]", "prepare business review".
---

# QBR Builder Skill

Build QBR documents that combine usage analytics, an ROI narrative, success metrics, and agreed next steps. Account data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account metadata, contract details, expansion history, stakeholder contacts |
| **Product analytics via MCP** (e.g. Amplitude, Mixpanel, Pendo, or internal) | Usage metrics, feature adoption, trend data |
| **companyRAG / file upload** | Success plans, CSM notes, support exports, customer-reported data |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## QBR Building Workflow

Begin preparation 2–3 weeks before the QBR date to allow time for data gathering, narrative construction, and internal review.

### Step 1: Gather Metrics

Collect data across four metric categories. For each metric, record the current value, the prior period value, and the trend direction.

| Metric Category | Key Metrics | Source |
| --- | --- | --- |
| **Usage & Adoption** | Active users vs. licensed, login frequency trend, feature adoption breadth, usage depth, time-in-platform | Product analytics |
| **Value & Outcomes** | Customer-stated goals progress, ROI metrics (if quantifiable), efficiency gains, business impact evidence | Success plan, CSM notes, customer-reported data |
| **Support & Satisfaction** | Ticket volume trend, resolution time, CSAT/NPS scores, escalation history | Support platform |
| **Partnership** | Milestones achieved, training completions, feature requests addressed, roadmap alignment | CSM notes, CRM |

For each metric, note the source and date range. Stale or incomplete data should be flagged, not omitted.

### Step 2: Build the Value Narrative

The QBR is not a data dump — it is a story about the value the customer has received and where the partnership is headed.

**Narrative Structure:**

1. **Where we started** — Remind the audience of the customer's original goals and the starting baseline. This anchors the conversation in what matters to them.
2. **What we accomplished** — Present achievements using the customer's language and metrics, not your product's feature names. "Your team reduced contract review time by 40%" is stronger than "Users adopted the AI review feature."
3. **Wins and highlights** — Call out 2–3 specific wins that the customer's leadership would care about. Connect each to a business outcome.
4. **Challenges and how we addressed them** — Be transparent about issues that arose. Show that they were handled and what was learned. Hiding problems erodes trust.
5. **What's next** — Forward-looking goals for the next quarter, aligned with the customer's evolving business priorities.

### Step 3: Highlight ROI

ROI is the centrepiece of any executive-level QBR. Structure it using evidence the customer can validate.

**ROI Framework:**

| ROI Type | Calculation Approach | Evidence Source |
| --- | --- | --- |
| **Time savings** | Hours saved per week × number of users × hourly cost (customer-provided or agreed rate) | Usage data, workflow comparison |
| **Cost avoidance** | Costs that would have been incurred without the product (e.g., additional headcount, tool licences) | Customer estimate, industry reference |
| **Revenue impact** | Pipeline influenced, deals accelerated, conversion improvements attributable to the product | CRM data, customer attribution |
| **Risk reduction** | Compliance incidents avoided, security improvements, audit readiness | Customer assessment, support data |
| **Efficiency gains** | Process improvements, error reduction, automation of manual tasks | Before/after workflow comparison |

**Critical rule**: Only claim ROI that the customer has confirmed or can validate. Never fabricate ROI numbers. If ROI cannot be quantified, use qualitative evidence — "your team reports that..." or "based on your feedback in our last check-in..."

### Step 4: Prepare the Agenda

A QBR should be a conversation, not a presentation. Structure the agenda to ensure executive engagement.

| Agenda Section | Duration (suggested) | Purpose |
| --- | --- | --- |
| **Business context** | 5–10 min | Customer shares their current priorities and any changes since last quarter |
| **Value delivered** | 10–15 min | CSM presents the value narrative (Step 2) with metrics |
| **ROI review** | 5–10 min | Walk through the ROI evidence; ask the customer to validate |
| **Challenges & feedback** | 5–10 min | Open discussion of what could be better; acknowledge issues proactively |
| **Product roadmap alignment** | 5–10 min | Share relevant upcoming capabilities; gather customer input |
| **Forward plan** | 10–15 min | Agree on next quarter goals, success metrics, and action items |

**Total**: 40–70 minutes depending on account complexity.

Adapt timing to the audience. Executive sponsors want the summary and the "so what" — skip granular usage data unless asked. Operational stakeholders want the detail.

### Step 5: Draft the QBR Document

Use the output template below. The document serves both as the presentation framework and the post-meeting record.

## Output Template — QBR Document

```
QUARTERLY BUSINESS REVIEW
Account: [name]
Period: [Q_ 20__]
QBR date: [date]
Prepared by: [CSM name]
Attendees: [list]

EXECUTIVE SUMMARY:
  [3-5 sentence summary: what was achieved, key highlight, forward focus]

BUSINESS CONTEXT:
  Customer priorities this quarter: [from customer input]
  Key changes since last QBR: [organisational, strategic, or market changes]

VALUE DELIVERED:
  Goal 1: [customer's stated goal]
    Status: [Achieved / On track / Behind / Revised]
    Evidence: [specific metrics or outcomes]
    Impact: [business significance]

  Goal 2: [customer's stated goal]
    Status: [...]
    Evidence: [...]
    Impact: [...]

  [Repeat for each goal]

USAGE & ADOPTION HIGHLIGHTS:
  Active users: [current] vs. [prior quarter] ([trend])
  Feature adoption: [key features and adoption rates]
  Usage trend: [summary with directional indicators]

ROI SUMMARY:
  [ROI type 1]: [quantified or qualitative evidence]
  [ROI type 2]: [quantified or qualitative evidence]
  Total estimated value: [if quantifiable, with methodology note]
  Customer validation: [confirmed / pending validation / qualitative only]

WINS THIS QUARTER:
  1. [specific win with business impact]
  2. [specific win with business impact]
  3. [specific win with business impact]

CHALLENGES & RESOLUTION:
  1. [challenge] → [how it was addressed] → [current status]
  2. ...

PRODUCT ROADMAP ALIGNMENT:
  Upcoming capabilities relevant to [account]:
  - [feature/capability] — [expected timeline] — [relevance to customer]
  Customer feedback / requests:
  - [request] — [status in roadmap]

FORWARD PLAN — NEXT QUARTER:
  Goal 1: [description] — Success metric: [how we'll measure] — Owner: [name]
  Goal 2: [description] — Success metric: [...] — Owner: [...]
  Goal 3: [description] — Success metric: [...] — Owner: [...]

ACTION ITEMS:
  | Action | Owner | Due Date |
  |--------|-------|----------|
  | [action] | [name] | [date] |
  | [action] | [name] | [date] |

NEXT QBR: [proposed date]
```

## Guardrails

- Never fabricate metrics, adoption rates, or ROI figures. All account data must come from the user, a connected MCP source, or companyRAG collections. When data is missing, mark fields as [DATA NEEDED].
- Never generate ROI claims without customer-confirmable evidence. Use qualitative framing when quantitative data is unavailable.
- Never present roadmap items as commitments. Use "planned" or "on our roadmap" — never "will be delivered by."
- Source-label every assertion: [From account data], [From QBR framework], [Customer-reported], or [CSM observation].

> **Tip:** Ask for PPTX output via companyFILES to get a formatted presentation ready for distribution.
