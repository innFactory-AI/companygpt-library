---
name: en-standup
description: Generate standup summaries from task context, recent commits, and open PRs. Use when preparing for daily standup, writing async standup updates, or summarising team activity. Trigger with "standup update", "what did I work on", "team standup summary".
---

# Standup Skill

Generate standup updates from the activity data of connected tools. The skill works for both synchronous standups (talking points) and asynchronous updates (written posts). Activity data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Git provider via MCP** (e.g. GitHub, GitLab, Bitbucket) | Commits since last standup, open/merged PRs |
| **Project tracker via MCP** (e.g. Jira, Linear, Asana, Shortcut) | Tasks in progress, completed, and blocked |
| **Chat via MCP** (e.g. Slack, Teams) | Threads with blockers or decisions |
| **companyM365** (if enabled) | Teams messages and Outlook calendar from your Microsoft 365 account |
| **companyRAG / file upload** | Sprint goals, team standup format preferences |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Standup Workflow

### Step 1: Gather Recent Activity

Collect data from connected tools for the reporting period (default: since last business day). When tools are not connected, ask the user to provide the information.

**Data to collect:**

| Category | Source | Look For |
| --- | --- | --- |
| **Completed work** | Project tracker (done/closed), Git (merged PRs) | Tickets moved to done, PRs merged, features shipped |
| **In-progress work** | Project tracker (in progress), Git (open PRs, recent commits) | Tickets being worked on, PRs in review, active branches |
| **Blocked work** | Project tracker (blocked/on hold), user input | Tickets marked blocked, PRs awaiting review for >24h, dependency on another team |
| **Upcoming work** | Project tracker (to do/next), sprint board | Next priorities after current tasks complete |

### Step 2: Categorise and Prioritise

Organise gathered data into the standup structure. Apply these rules:

1. Lead with blockers. Blockers are the only standup item that requires action from others. Put them first so the team can address them.
2. Summarise, don't enumerate. "Worked on auth refactoring — 3 PRs merged, 1 in review" is better than listing each PR title.
3. Connect to goals. When sprint goals are available, map completed and in-progress work to the goals they advance.
4. Flag risks. If in-progress work is at risk of missing a deadline, surface it under blockers or as a separate risk note.
5. Skip noise. Trivial commits (typo fixes, formatting), bot-generated PRs, and administrative tasks are not standup-worthy unless they represent meaningful effort.

### Step 3: Format Output

Use the appropriate format based on context.

## Individual Standup Update

```
## Standup — [Name] — [Date]

### Blockers
- [Blocker description — who/what is needed to unblock — how long blocked]
[or: No blockers]

### Yesterday (Completed)
- [Work item — outcome or progress made — linked ticket/PR if relevant]

### Today (Planned)
- [Work item — specific goal for today — linked ticket if relevant]

### Risks / FYI
- [Anything the team should know — approaching deadline, scope change, dependency]
[or: omit section if none]
```

## Team Standup Summary

When summarising for the whole team:

```
## Team Standup — [Team Name] — [Date]

### Blockers (Action Required)
- [Person]: [blocker] — needs [action/person]

### Sprint Goal Progress
- Goal 1: [goal description] — [on track / at risk / blocked] — [brief status]
- Goal 2: [goal description] — [on track / at risk / blocked] — [brief status]

### Highlights
- [Notable completions, deployments, or milestones]

### In Progress
- [Person]: [primary focus today]

### Risks
- [Risks to sprint commitments or upcoming deadlines]
```

## Async Standup Format

For teams using async standups (Slack/Teams posts):

```
**[Name] — [Date]**
✅ Done: [completed items, brief]
🔄 Doing: [in-progress items, brief]
🚫 Blocked: [blockers with needed action]
```

Keep async updates to 3-5 lines maximum. If more detail is needed, link to the ticket or PR.

## Standup Quality Checklist

- Blockers are specific and include what is needed to unblock
- Completed items describe outcomes, not just activity ("shipped auth fix" not "worked on code")
- Planned items are concrete enough that the team knows what you intend to finish
- No items older than 2 standups — recurring items need a different conversation (escalation or re-scoping)
- Update is concise enough to deliver in under 90 seconds (sync) or read in under 30 seconds (async)

## Guardrails

- Never fabricate activity. If no data is available, state "No activity data available — provide your update or connect [tool name]."
- Never guess ticket status. If status is unavailable from the project tracker, ask the user rather than assuming.
- Never invent blockers or risks. Report only what is confirmed as blocked or at risk by data or user input.
- Source-label each item as `[From project tracker]`, `[From git]`, or `[From user input]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get an update ready to share.
