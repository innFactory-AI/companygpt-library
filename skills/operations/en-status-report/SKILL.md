---
name: en-status-report
description: Generate cross-functional status reports with risk highlights, dependency tracking, and executive summary formatting. Use when preparing weekly project updates, programme-level reports, or executive briefings. Trigger with "status report for", "project update", "weekly report".
---

# Status Report Skill

Build cross-functional status reports that surface progress, risks, dependencies, and decisions needed — tailored by audience. The data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Asana, Linear, Monday) | Sprint progress, ticket status, blockers, velocity |
| **Calendar / meeting notes via MCP** | Recent decisions, action items, upcoming milestones |
| **Risk register** | Open risks, mitigation status, new risks raised |
| **Communication channels via MCP** (e.g. Slack, Teams) | Escalations, cross-team requests, blockers raised |
| **companyM365** (if enabled) | Outlook calendar and mail, Teams messages, OneNote pages and Teams meeting transcripts |
| **companyRAG collections / file upload** | Previous status reports, programme plans, OKRs |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Workflow

### 1. Gather Updates Per Workstream

For each workstream or project track:

```
WORKSTREAM UPDATE:
  Workstream:           [name]
  Owner:                [person or team responsible]
  Period:               [reporting period — e.g., week of 2025-04-01]
  Key accomplishments:  [what was completed or delivered]
  In progress:          [what is actively being worked on]
  Planned next:         [what is scheduled for the next period]
  Blockers:             [anything preventing progress — with owner and age]
  Decisions needed:     [decisions the audience must make or be aware of]
```

Collect updates from each workstream before assessing status. Never assess RAG status based on assumptions — use data from the workstream owner.

### 2. Assess RAG Status

Apply RAG (Red / Amber / Green) consistently across all workstreams using a defined rubric:

| Status | Criteria | Action Required |
| --- | --- | --- |
| **🟢 Green** | On track — milestones on schedule, no unmitigated risks, dependencies resolved | Continue as planned; no escalation needed |
| **🟡 Amber** | At risk — slippage possible, risks identified but mitigation in progress, dependencies not yet confirmed | Monitor closely; mitigation plan required; flag to sponsor if no improvement by next period |
| **🔴 Red** | Off track — milestone missed or will miss, unmitigated critical risk, blocker with no resolution path | Immediate escalation; recovery plan required; sponsor decision needed |

### RAG Assessment Discipline

- RAG is based on objective criteria, not optimism. A workstream with an unresolved blocker is not Green because the team "expects it to be fixed soon."
- Track RAG trend: ↑ Improving , → Stable , ↓ Deteriorating — the direction matters as much as the current colour.
- If a workstream was Amber last period and is still Amber with no progress on mitigation, escalate — persistent Amber is often unacknowledged Red.

### 3. Identify Risks and Dependencies

Extract cross-cutting risks and inter-workstream dependencies:

```
RISK / DEPENDENCY LOG:
  Item:          [description]
  Type:          [Risk / Dependency / Blocker]
  Affects:       [which workstream(s)]
  Owner:         [who is responsible for resolution]
  Status:        [Open / In progress / Resolved]
  Due date:      [when resolution is needed]
  Impact if unresolved: [what happens if this is not addressed]
```

Dependencies between workstreams are the most common source of programme-level risk. Surface them explicitly — teams often assume the other team knows.

### 4. Format for Audience

Tailor the report to who is reading it. The same underlying data is presented differently depending on the audience's decision authority and detail appetite.

## Audience Tailoring

| Audience | Focus | Detail Level | RAG Depth | Recommended Length |
| --- | --- | --- | --- | --- |
| **Executive / C-suite** | Strategic progress, top risks, decisions needed | Headlines and numbers only — no implementation detail | Overall programme RAG + top 3 workstream RAGs | 1 page / 5-minute read |
| **Steering committee** | Cross-workstream dependencies, risk mitigation, resource issues | Moderate — enough context for informed decisions | RAG per workstream with trend arrows | 2-3 pages / 10-minute read |
| **Programme / project team** | Detailed progress, blockers, next steps, action items | High — operational detail for execution | RAG per workstream with supporting evidence | 3-5 pages / 15-minute read |
| **Stakeholder group** | Impact on their area, upcoming changes, what they need to do | Selective — only what affects their domain | RAG for relevant workstreams only | 1-2 pages / 5-minute read |

### Executive Report Rules

- Lead with the single most important thing: "Programme is on track for Q3 launch" or "Programme is at risk — decision needed on scope by Friday"
- No jargon, no acronyms without expansion, no technical implementation details
- Every risk mentioned must have a "so what" — the consequence and the ask
- End with explicit decisions or actions requested from the audience

### Team Report Rules

- Include enough operational detail for team members to act on the information
- Blockers must name an owner and an expected resolution date
- Action items carry over from previous reports with status updates — never let items silently disappear
- Celebrate completions — recognition of delivered work sustains team momentum

## Output Template

```
# Status Report — [Programme/Project Name]
# Period: [reporting period]
# Overall Status: [🟢/🟡/🔴] [trend arrow]

## Executive Summary
- Overall: [one-sentence programme status]
- Key achievement: [most significant accomplishment this period]
- Top risk: [highest-priority risk with impact statement]
- Decision needed: [if any — what, from whom, by when]

## Workstream Status

| Workstream | Owner | Status | Trend | Key Update |
|---|---|---|---|---|
| [name] | [owner] | [🟢/🟡/🔴] | [↑/→/↓] | [one-line summary] |

## Workstream Detail
[Per-workstream sections with accomplishments, in progress, planned, blockers]

## Risks and Dependencies

| # | Type | Description | Affects | Owner | Status | Due |
|---|---|---|---|---|---|---|
| 1 | [Risk/Dep/Blocker] | [description] | [workstreams] | [owner] | [status] | [date] |

## Decisions Needed
[Decisions required from report audience — what, context, options, recommendation, deadline]

## Actions and Follow-ups

| # | Action | Owner | Due | Status |
|---|---|---|---|---|
| [carried from last report + new items] |

## Next Period Outlook
- Key milestones approaching: [list]
- Expected status changes: [any workstreams likely to change RAG]
```

## Guardrails

- Never fabricate progress percentages, dates, or milestone status. All progress data comes from the user's project tracking data.
- Never invent risks or blockers. Prompt for risk data rather than generating plausible-sounding risks.
- Never assign RAG status without evidence. If data is insufficient, mark as `[Data not available — status pending update from owner]`.
- Label generated content: `[From project data]`, `[Framework methodology]`, `[AI-drafted summary — verify with workstream owner]`.

> **Tip:** Ask for DOCX, Markdown, or PPTX output via companyFILES to get a formatted report ready for distribution.
