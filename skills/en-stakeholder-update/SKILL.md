---
name: en-stakeholder-update
description: Generate tailored product status updates for different audiences and cadences — exec summary, engineering detail, customer-facing. Use when writing weekly updates, preparing for a leadership review, or communicating launch status. Trigger with "write product update", "status update for [audience]", "weekly product summary".
---

# Stakeholder Update Skill

Write product status updates tailored to audience, cadence, and purpose. The skill makes updates actionable rather than ceremonial — with audience-specific templates, tone calibration, and a clear information hierarchy.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Asana, Linear) | Story status, sprint progress, blockers, milestone tracking |
| **Analytics via MCP** (e.g. Amplitude, Mixpanel, GA) | KPI values, activation and usage metrics, trends |
| **companyRAG collections / file upload** | Roadmaps, OKRs, feature specs, prior updates, sales-handoff notes |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Audience Framework

Every update serves a specific audience. The same product status, framed differently, is useful or useless depending on the reader.

| Audience | What They Need | What They Do NOT Need |
| --- | --- | --- |
| **Executive / C-suite** | Business impact, strategic alignment, decisions needed, risk escalation | Implementation details, individual ticket status, technical jargon |
| **Engineering / Design** | Scope clarity, dependency status, technical decisions, blockers | Business justification for every item, high-level strategy narrative |
| **Cross-functional peers** (Marketing, Sales, CS) | Timeline, feature descriptions in user terms, launch readiness, enablement needs | Technical architecture, sprint-level detail, internal prioritisation debates |
| **Customers / External** | Value delivered, what is coming (in ranges, not dates), how to provide feedback | Internal roadmap, prioritisation rationale, unshipped features, competitor context |
| **Board / Investors** | Traction metrics, strategic progress, resource allocation, competitive position | Operational detail, sprint planning, individual feature status |

## Update Templates

### Executive Update

Cadence: Weekly or biweekly. Length: 5-10 bullet points maximum.

The executive update answers three questions: Are we on track? What do you need to know? What do you need to decide?

```
PRODUCT UPDATE — [Period]
To: [Audience]    |    From: [PM name]    |    Date: [date]

📊 STATUS: [On Track / At Risk / Off Track]

HEADLINE: [One sentence — the single most important thing to know this period]

PROGRESS:
• [Milestone achieved] — Impact: [why it matters in business terms]
• [Milestone achieved] — Impact: [why it matters]

COMING NEXT:
• [Next milestone] — Expected: [timeframe]
• [Next milestone] — Expected: [timeframe]

RISKS & BLOCKERS:
• [Risk] — Mitigation: [what we are doing] — Decision needed: [Yes/No]
  [If yes: specific decision with options and recommendation]

METRICS:
• [Key metric]: [current value] → [target] ([on track / behind / ahead])

DECISIONS NEEDED:
• [Decision description] — Options: [A / B] — Recommendation: [which and why]
  Deadline for decision: [date]
```

**Executive update principles**:

- Lead with status (the RAG signal) — don't bury bad news
- Business impact first, product detail second
- Every risk must have a mitigation — never present a problem without a plan
- Decisions needed are the most important section — they drive action
- If there are no decisions needed, the update may not need to be sent

### Engineering Update

Cadence: Weekly (aligned with sprint cadence). Length: As needed for clarity.

```
ENGINEERING STATUS — Sprint [number] — [dates]

SPRINT GOAL: [outcome statement]
GOAL STATUS: [On Track / At Risk / Blocked]

COMPLETED THIS SPRINT:
• [Story/feature] — [Acceptance criteria met] — [Any follow-up needed]
• [Story/feature] — [Acceptance criteria met]

IN PROGRESS:
• [Story/feature] — [% complete or days remaining] — Owner: [name]
  [Any blockers or decisions needed]

BLOCKED:
• [Story/feature] — Blocked by: [description] — Owner of resolution: [name]
  Expected resolution: [date]

CARRY-OVER:
• [Story/feature] — Reason: [why it did not complete] — New estimate: [timeframe]

DEPENDENCIES:
• [Dependency] — Status: [Resolved / On Track / At Risk] — Owner: [name]

NEXT SPRINT PREVIEW:
• [Planned focus or goal for next sprint]

TECH DEBT / MAINTENANCE:
• [Any significant tech debt items addressed or flagged]
```

### Cross-Functional Update

Cadence: Weekly or tied to launch milestones. Length: Concise, action-oriented.

```
PRODUCT UPDATE FOR [Marketing / Sales / CS] — [Period]

WHAT SHIPPED:
• [Feature/change] — What it does: [user-facing description in plain language]
  Who it affects: [user segment]
  Enablement needed: [docs update / training / FAQ / nothing]

WHAT'S COMING:
• [Feature] — Expected: [timeframe range, not exact date]
  Early access: [available / not yet]
  Enablement timeline: [when materials will be ready]

WHAT CHANGED:
• [Timeline shift / scope change / priority change]
  Why: [brief explanation]
  Impact on your team: [what they need to adjust]

ACTION ITEMS FOR YOUR TEAM:
• [Specific ask] — By: [date] — Owner: [name]

CUSTOMER-FACING MESSAGING:
• [Approved language for customer communications, if applicable]
```

### Customer-Facing Update

Cadence: Monthly, quarterly, or tied to major releases. Length: Brief, value-focused.

```
PRODUCT UPDATE — [Month/Quarter Year]

WHAT'S NEW:
• [Feature name]: [One-sentence description of the value it provides]
  How to use it: [brief instruction or link to docs]

COMING SOON:
• [Feature/improvement]: [Problem it solves — described from the user's perspective]
  Expected: [This quarter / Next quarter / First half of year]

IMPROVEMENTS:
• [Performance improvement / bug fix / UX refinement]: [What changed and why it matters]

YOUR FEEDBACK MATTERS:
[How to submit feedback, request features, or participate in research]
```

**Customer-facing rules**:

- Value-first language: describe what users can DO, not what you BUILT
- Time ranges only — never specific dates ("Q3" not "August 15th")
- Never mention unshipped features as committed — use "exploring," "planned," or "coming soon"
- Never expose internal project names, prioritisation scores, or competitive context
- Never discuss features that were cut, deprioritised, or cancelled — this creates confusion

## Cadence Selection Guide

| Cadence | Best For | Content Focus |
| --- | --- | --- |
| **Daily** (stand-up notes) | Engineering team during active sprint | Blockers and help needed — keep extremely brief |
| **Weekly** | Executive, engineering, cross-functional during active development | Progress, risks, decisions needed |
| **Biweekly** | Executive during steady-state periods | Milestone progress, strategic alignment |
| **Monthly** | Customer-facing, board-level | Cumulative progress, upcoming themes |
| **Quarterly** | Board, investors, company all-hands | Strategic progress, metric trends, next-quarter outlook |

**Cadence discipline**: Do not send an update just because it is the scheduled day. If there is nothing meaningful to communicate, say so in one sentence and skip the full update. Ceremonial updates train readers to ignore them.

## Status Framing

### RAG (Red / Amber / Green) Definitions

Define these once for your organisation and apply consistently:

| Status | Definition | Reader Action |
| --- | --- | --- |
| **Green — On Track** | Delivering to plan. No unmitigated risks. Metrics within target range. | No action needed. Acknowledge. |
| **Amber — At Risk** | Deliverable, timeline, or metric is at risk. Mitigation underway but outcome uncertain. | Awareness needed. Escalation may follow. |
| **Red — Off Track** | Deliverable will miss target without intervention. Mitigation requires help or decision. | Decision needed. Escalation active. |

**Framing discipline**:

- Never report Red without a mitigation plan and a specific ask
- Never report Green when you privately believe the status is Amber — trust erosion is worse than bad news
- Amber is not "I'm not sure" — it means a specific, named risk exists with an active mitigation
- Status should refer to the GOAL, not the activity — "We shipped 8 of 10 stories" is activity; "The sprint goal is at risk because the payment integration is blocked" is status

### Communicating Bad News

When status is Amber or Red:

1. State the fact: What happened or what is at risk — no hedging
2. Explain the impact: What does this mean for the timeline, metric, or deliverable?
3. Present the mitigation: What is already being done?
4. Make the ask: What decision or help is needed from the reader?
5. Give a next-check date: When will you update on resolution?

Never bury bad news in the middle of an update. Lead with it or call it out in a clearly marked section.

## Guardrails

- NEVER fabricate progress, metrics, timelines, or status data. When data is missing, mark the field as [Data needed] rather than estimating.
- NEVER generate customer-facing feature descriptions without information. Ask the user for feature details rather than inventing.
- NEVER assign RAG status without data. If status cannot be determined, state "Status cannot be assessed — [specify what data is needed]".
- Source-label every element as [From user/project data], [Communication framework], or [AI draft — verify before sending].

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted document ready for distribution.
