---
name: en-weekly-review
description: Summarise open tasks, deadlines, progress, and carry-over items into a structured weekly reset. Use when starting or ending your week, reviewing what got done, or planning the week ahead. Trigger with "weekly review", "what's on my plate", "week in review".
---

# Weekly Review Skill

Gather open work, assess progress, surface blockers, and produce a clear plan for the week ahead — all in one structured pass. Data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Task manager via MCP** (e.g. Jira, Linear, Asana, Todoist, Monday.com, Notion) | Open tasks, due dates, status, assignee |
| **Calendar via MCP** (e.g. Google Calendar, Outlook Calendar) | Upcoming meetings, time blocks, deadlines |
| **Email & chat via MCP** (e.g. Gmail, Outlook, Slack, Microsoft Teams) | Action items from correspondence, commitments made in conversations, mentions |
| **companyM365** (if enabled) | Outlook calendar and mail, Teams messages, Microsoft To Do and Planner tasks from your Microsoft 365 account |
| **companyRAG / file upload** | Review templates, project briefs, meeting notes with action items |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Review Workflow

Run these steps in order. The review is most effective when done at a consistent time — either Friday afternoon (close the week) or Monday morning (open the week).

### Step 1: Gather Open Items

Collect everything that is in-flight, overdue, or upcoming:

**From task managers** (if connected):

- All tasks assigned to the user with status ≠ Done/Closed
- Tasks completed this week (for the retrospective)
- Tasks due in the next 7 days
- Tasks overdue

**From calendar** (if connected):

- Meetings and events for the coming week
- Deadlines or milestones appearing as calendar events
- Recurring commitments (standups, 1:1s, reviews)

**From email and chat** (if connected):

- Action items from the past week's correspondence
- Outstanding replies or commitments
- Mentions requiring follow-up

**From user input**:

- Any tasks, projects, or commitments not captured in tools
- Personal goals or development items
- Items remembered during the review process

### Step 2: Categorise and Assess

Organise gathered items into these categories:

| Category | Definition | Action |
| --- | --- | --- |
| **Completed this week** | Tasks finished since last review | Acknowledge and archive. Note any that took significantly longer or shorter than expected. |
| **In progress** | Started but not finished | Assess: on track, at risk, or blocked? Estimate remaining effort. |
| **Carry-over** | Planned for this week but not started | Why didn't it happen? Re-prioritise for next week or deliberately defer. |
| **Overdue** | Past due date and not complete | Escalate, renegotiate deadline, or reprioritise. Overdue items need a decision, not just a note. |
| **Upcoming (next 7 days)** | Due or scheduled for the coming week | Estimate effort and assign to specific days if possible. |
| **Waiting on others** | Blocked by someone else's action | Note who, what, and when you last followed up. Plan a follow-up if stale. |
| **Someday / backlog** | Items with no deadline but still relevant | Review quarterly. If an item has been on this list for 4+ weeks without progress, decide: schedule it or drop it. |

### Step 3: Identify Patterns and Blockers

Look across the categorised items for systemic issues:

- Recurring carry-over : The same task appearing as carry-over for 2+ weeks signals either over-commitment, unclear requirements, or avoidance. Name it.
- Time allocation mismatch : If the calendar is full of meetings but the task list expects 20 hours of focused work, there is a math problem. Flag it.
- Blocker concentration : Multiple items blocked by the same person, team, or dependency? That is a single blocker to escalate, not many separate ones.
- Priority drift : Are urgent-but-unimportant tasks crowding out important-but-not-urgent work? Note the drift.

### Step 4: Plan the Coming Week

Translate the assessment into a concrete plan:

1. Select 3-5 priorities : Not a full task list — the 3-5 most important outcomes for the coming week. These are the items that, if completed, make the week a success.
2. Time-block estimates : For each priority, estimate the focused time needed. Compare against available focused time (calendar minus meetings, minus buffer for reactive work).
3. Day assignment (optional but recommended): Assign priorities to specific days based on deadlines, energy, and meeting patterns. Front-load the most important work.
4. Follow-up list : Items where you need to chase someone, send an update, or check on status.
5. Deliberate deferrals : Items explicitly pushed to a future week — not forgotten, but consciously deprioritised. Note the reason.

### Step 5: Generate the Review Document

Produce the structured output using the template below.

## Output Template: Weekly Review

```
# Weekly Review — [Week of DATE]

## Last Week: What Got Done
  ✓ [Completed item 1]
  ✓ [Completed item 2]
  ✓ [Completed item 3]
  ...

  Highlights: [1-2 sentences on what went well or notable achievements]

## Carried Over (Not Completed)
  → [Item 1] — Reason: [why it didn't happen] — Decision: [do next week / defer / drop]
  → [Item 2] — Reason: [...] — Decision: [...]

## Currently In Progress
  ⟳ [Item 1] — Status: [on track / at risk / blocked] — ETA: [estimate]
  ⟳ [Item 2] — Status: [...] — ETA: [...]

## Overdue
  ⚠ [Item 1] — Due: [date] — Action: [renegotiate / escalate / complete by X]

## Waiting On Others
  ⏳ [Item 1] — Waiting on: [person] — Since: [date] — Follow-up: [plan]

## This Week: Priorities
  1. [Priority 1] — Estimated time: [hours] — Due: [date or "no hard deadline"]
  2. [Priority 2] — Estimated time: [hours] — Due: [date]
  3. [Priority 3] — Estimated time: [hours] — Due: [date]

  Available focused time: ~[hours] (based on [total hours] minus [meeting hours] minus [buffer])

## Follow-ups to Send
  - [Follow-up 1] — To: [person] — By: [day]
  - [Follow-up 2] — To: [person] — By: [day]

## Deliberately Deferred
  ↓ [Item 1] — Deferred to: [week/date] — Reason: [why]

## Patterns Noticed
  [Any systemic observations from Step 3]

## Notes for Next Review
  [Anything to remember or check next week]
```

## Review Cadence Variants

The core methodology adapts to different cadences:

| Cadence | When to Use | Modification |
| --- | --- | --- |
| **Weekly** (default) | Standard knowledge work | Full workflow as described above |
| **Bi-weekly** | Lower task volume or longer project cycles | Extend the retrospective window; add a mid-cycle pulse check |
| **Daily standup prep** | High-velocity environments | Abbreviated: skip Steps 3-4; focus on today's 1-3 items and blockers |
| **Monthly** | Strategic/leadership review | Add: goal progress, OKR check-in, delegation assessment, team capacity |

## Guardrails

- NEVER fabricate task status or calendar events — if data is unavailable, ask the user.
- NEVER prioritise for the user without their input — present items and a recommended order, framed as a suggestion.
- NEVER estimate domain-specific work without the user's input — ask for effort estimates on technical or specialised tasks.
- Flag outputs: `[From connected source]`, `[From user input]`, `[Suggested]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted review ready to share.
