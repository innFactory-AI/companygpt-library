---
name: en-meeting-prep
description: Generate agenda drafts and pre-read briefings from calendar context, prior meeting notes, and connected sources. Use when preparing for any meeting, creating agendas, or compiling pre-reads. Trigger with "prep for my meeting with", "create agenda for", "meeting brief for".
---

# Meeting Prep Skill

Gather context from calendars, email, chat, and notes to draft agendas, compile pre-read briefings, and suggest talking points for any meeting. The data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Calendar via MCP** (e.g. Google Calendar, Outlook) | Meeting title, time, attendees, location, attached agenda |
| **Email via MCP** (e.g. Gmail, Outlook) | Recent correspondence with attendees, shared documents |
| **Chat via MCP** (e.g. Slack, Microsoft Teams) | Recent conversations with attendees, channel context |
| **Documents via MCP** (e.g. Notion, Confluence, Google Docs) | Prior meeting notes, shared documents, project pages |
| **CRM via MCP** (e.g. Salesforce, HubSpot) | Account history, deal status, contact details (for external meetings) |
| **Issue tracker via MCP** (e.g. Jira, Linear, Asana) | Open items relevant to the meeting topic |
| **companyM365** (if enabled) | Outlook calendar and mail, Teams messages and OneDrive/SharePoint documents from your Microsoft 365 account |
| **companyRAG / file upload** | Recurring meeting templates, background documents |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Preparation Workflow

Follow these steps for every meeting preparation request. The depth of preparation scales with meeting importance — a quick 1:1 needs less than a board presentation.

### Step 1: Identify the Meeting

Establish the basics:

- Meeting type: 1:1, team standup, project review, client call, board meeting, interview, brainstorm, decision meeting, informational, retrospective
- Attendees: Who is attending? What are their roles? Are any attendees external (clients, partners, vendors)?
- Duration: How long is the meeting? This constrains the agenda.
- Objective: What should be true after this meeting that is not true before? If the user cannot articulate this, help them define it — a meeting without an objective is a meeting without value.
- Recurrence: Is this a one-off or recurring meeting? For recurring meetings, pull prior meeting notes if available.

### Step 2: Gather Context

Pull relevant information from connected sources:

**Prior meetings with these attendees:**

- Last meeting notes, action items, decisions made
- Outstanding action items from previous sessions
- Topics that were deferred or parked

**Recent correspondence:**

- Email threads with attendees from the past 1-2 weeks
- Chat messages in relevant channels
- Shared documents recently edited

**Relevant project/account status:**

- Open tasks or issues related to the meeting topic
- For external meetings: account status, deal stage, recent interactions from CRM
- For project meetings: milestone status, blockers, recent changes

**Background documents:**

- Any pre-reads already shared by the organiser
- Relevant policies, specifications, or reference materials from companyRAG collections

If connected sources are not available, ask the user to provide the context they have. Even a 2-sentence summary of "what this meeting is about and what happened last time" dramatically improves preparation quality.

### Step 3: Draft Agenda

Construct the agenda using this framework:

**Agenda structure:**

```
# [Meeting Title]
Date: [date and time]
Duration: [length]
Attendees: [list]
Objective: [what should be true after this meeting]

## Agenda

1. [Opening / Check-in]                          [X min]
   - [Brief context-setter or warm-up]

2. [Topic A — highest priority]                   [X min]
   - Context: [1-2 sentences of background]
   - Decision needed: [yes/no — if yes, what decision]
   - Pre-read: [link or reference, if any]

3. [Topic B]                                      [X min]
   - Context: [...]
   - Decision needed: [...]

4. [Topic C]                                      [X min]
   - Context: [...]

5. [Action items and next steps]                  [5 min]
   - Review decisions made
   - Assign action items with owners and deadlines

## Open Items from Last Meeting
  - [Item 1] — Owner: [name] — Status: [done / in progress / not started]
  - [Item 2] — ...
```

**Agenda principles:**

- Time-box every item. Total time allocations must not exceed meeting duration minus 5 minutes (buffer for overrun and wrap-up).
- Prioritise ruthlessly. Put the most important or time-sensitive topic first. If the meeting runs over, at least the critical item was addressed.
- Distinguish decisions from discussions. Mark topics that require a decision — these need the decision-maker present and enough context for an informed choice.
- Limit to 3-5 substantive items for a 30-minute meeting, 5-7 for a 60-minute meeting. More items than that guarantees nothing gets adequate attention.
- Include open items from the last meeting. Accountability requires visibility.

### Step 4: Compile Pre-Read Briefing

For meetings where attendees need background (project reviews, client calls, board meetings), produce a briefing document:

```
# Meeting Brief: [Title]
Prepared: [date]
Meeting: [date and time]

## TL;DR
  [2-3 sentences: why we're meeting, what's most important, what we need to decide]

## Context
  [Background the attendees need — keep it to 1 page maximum. Link to detailed sources rather than reproducing them.]

## Key Data Points
  - [Metric or fact 1] — Source: [where this came from]
  - [Metric or fact 2] — Source: [...]
  - [Metric or fact 3] — Source: [...]

## Open Questions
  1. [Question that needs to be resolved in this meeting]
  2. [Question 2]

## Relevant History
  - [Date]: [What happened — decision, milestone, or change]
  - [Date]: [...]

## Suggested Talking Points
  - [Point 1 — what to raise and why]
  - [Point 2]
  - [Point 3]
```

**Briefing principles:**

- Brevity over comprehensiveness. A 1-page brief that gets read beats a 10-page document that doesn't.
- Source everything. Every data point, claim, or historical reference must cite its source so attendees can dig deeper if needed.
- Lead with the decision or ask. If the meeting needs a decision, put the question and options first — context second.

### Step 5: Suggest Talking Points

Based on the gathered context, suggest specific talking points the user should raise:

| Type | When to Suggest | Format |
| --- | --- | --- |
| **Follow-up from prior meeting** | An action item was assigned or a topic was deferred | "Last time we agreed to [X]. Status update?" |
| **Proactive update** | The user has progress or news relevant to attendees | "Share that [milestone] was completed / [blocker] was resolved" |
| **Question to ask** | Information is needed from an attendee | "Ask [person] about [topic] — needed for [reason]" |
| **Risk to flag** | A risk or concern should be raised early | "Flag that [risk] could affect [timeline/outcome]" |
| **Decision to drive** | A pending decision needs attention | "We need to decide on [topic] — options are [A] or [B]" |

## Meeting Type Quick Guides

Adapt the workflow depth to the meeting type:

| Meeting Type | Preparation Depth | Key Focus |
| --- | --- | --- |
| **1:1 (manager/report)** | Light — 5-10 min prep | Open action items, blockers, career/development topics |
| **Team standup** | Minimal — 2 min prep | Your status, blockers, help needed |
| **Project review** | Medium — 15-20 min prep | Milestone status, risks, decisions needed, timeline |
| **Client/external call** | Full — 20-30 min prep | Account history, relationship context, objectives, pre-read |
| **Board/executive** | Full — 30+ min prep | Narrative structure, key metrics, decisions, pre-read package |
| **Interview** | Medium — 15 min prep | Role requirements, candidate background, prepared questions |
| **Brainstorm** | Light — 10 min prep | Problem definition, constraints, seed ideas, creative prompts |

## Guardrails

- NEVER fabricate meeting history or attendee backgrounds — if prior notes or org data are unavailable, ask the user.
- NEVER generate fake metrics or data points for briefings — use `[Data needed — ask user]` as a placeholder.
- NEVER assume the meeting objective — ask before drafting the agenda.
- Flag outputs: `[From connected source]`, `[From user input]`, `[Suggested]`, `[Data needed]`.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted agenda or briefing ready to share.
