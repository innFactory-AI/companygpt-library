---
name: en-memory-management
description: Maintain personalised user context across sessions — terminology, preferences, project shorthand, and working style — for faster, sharper assistance. Use when teaching the assistant about your work context, updating preferences, or reviewing stored context. Trigger with "remember that", "update my context", "what do you know about me".
---

# Memory Management Skill

Accept, categorise, store, recall, and prune personalised user context across sessions — projects, preferences, terminology, and working patterns — so every future conversation starts with the right knowledge. Context is held persistently through the CompanyGPT Memory feature and companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CompanyGPT Memory** | Persistent store for personalised user context across sessions |
| **companyRAG collections** | Larger context documents, note collections, searchable knowledge |
| **MCP servers** (note tools, e.g. Notion, Obsidian) | Existing notes and context from connected systems |
| **File upload** | Context documents, glossaries, project notes you upload directly |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Context Management Workflow

### Accept Context

When you provide context to remember, capture it precisely.

**Intake process:**

1. Receive the context — you state something to remember ("remember that Q3 planning uses the PACE framework" or "my team calls the onboarding project 'Lighthouse'")
2. Confirm understanding — paraphrase back to you to verify accuracy. Do not store misunderstood context.
3. Categorise — assign to the appropriate context category (see taxonomy below)
4. Acknowledge storage — confirm what was stored and in which category in CompanyGPT Memory

**Intake format:**

```
STORED CONTEXT:
  Category:   [category from taxonomy]
  Key:        [short identifier — e.g., "Q3 planning framework"]
  Value:      [the context itself — verbatim or accurately paraphrased]
  Added:      [date]
  Source:     [user-provided]
```

### Categorise

Organise stored context into these categories for efficient recall.

| Category | What Belongs Here | Examples |
| --- | --- | --- |
| **Projects** | Active projects, codenames, timelines, stakeholders, status | "Project Lighthouse = onboarding redesign, launching Q3, led by Sarah" |
| **Preferences** | Working style, output format preferences, communication style | "Prefers bullet points over prose", "Uses British English spelling" |
| **Terminology** | Company-specific terms, acronyms, jargon, naming conventions | "PACE = Plan, Align, Create, Evaluate — our planning framework" |
| **Team** | Team members, roles, reporting lines, key contacts | "Direct reports: Alex (engineering), Maria (design), Tom (data)" |
| **Processes** | Recurring workflows, approval chains, standard operating procedures | "Budget requests go through Finance → VP → CFO for amounts over €50k" |
| **Tools & systems** | Preferred tools, system names, access patterns | "Uses Linear for task tracking, Notion for documentation" |
| **Constraints** | Boundaries, limitations, things to avoid | "Never use the term 'synergy' in deliverables — company culture thing" |

### Store

Storage principles:

- Atomic entries: Store each piece of context as a separate, self-contained entry. "My team uses Linear and prefers async communication" becomes two entries — one in Tools & systems, one in Preferences.
- Verbatim when possible: Use your own words. If paraphrasing for clarity, confirm with you.
- No interpretation: Store facts, not inferences. If you say "I work in Berlin," store that. Do not infer timezone, language preference, or employment law context.
- Timestamped: Every entry includes when it was added to enable staleness management.

### Recall

Use stored context proactively to improve assistance quality.

**Recall triggers:**

| Trigger | Action |
| --- | --- |
| You reference a stored project by name or codename | Apply stored project context automatically |
| Task involves a domain where preferences are stored | Apply formatting, style, and communication preferences |
| You mention a team member by name | Recall their role and relationship context |
| You use company-specific terminology | Use the stored definitions for accurate understanding |
| You ask "what do you know about me" or "what's in my context" | Present a structured summary of all stored context by category |

**Recall format when presenting stored context:**

```
# Your Stored Context

## Projects
  - [Key]: [Value] — added [date]
  - ...

## Preferences
  - [Key]: [Value] — added [date]
  - ...

## Terminology
  - [Key]: [Value] — added [date]
  - ...

[...continue for each category with entries]
```

### Prune Stale Items

Context goes stale. Regularly review and clean up stored entries.

**Staleness indicators:**

| Signal | Action |
| --- | --- |
| Project marked as completed or cancelled | Archive — move to inactive but retain for historical reference |
| Context contradicted by newer information | Update to current information; note the change |
| Entry older than 6 months with no recent recall | Flag for user review — "Is this still relevant?" |
| You explicitly say to forget something | Remove immediately |

**Pruning process:**

1. When context is recalled and seems potentially outdated, ask: "I have [context] stored from [date] — is this still current?"
2. Periodically (during weekly reviews or when you ask to review context), present entries older than 3 months for confirmation
3. When you provide updated context that conflicts with stored context, replace the old entry and confirm: "Updated [key] from [old value] to [new value]"

## Anti-Patterns

| Anti-Pattern | Problem | Rule |
| --- | --- | --- |
| **Storing sensitive PII** | Privacy risk — passwords, personal financial data, health information, identity documents | REFUSE to store passwords, financial account details, health records, government ID numbers, or other sensitive personal data. Inform the user: "I cannot store this type of sensitive information." |
| **Inferring context** | Accuracy risk — assumptions may be wrong | Only store context you explicitly provide. Never infer preferences, relationships, or facts from conversation patterns. |
| **Storing third-party data** | Privacy and accuracy risk | Do not store detailed personal information about people other than basic professional context (name, role, team). Never store assessments, performance opinions, or personal details about third parties. |
| **Over-storing** | Noise overwhelms signal | Keep entries concise and atomic. If the context summary exceeds 30-40 entries, encourage the user to review and prune. |
| **Never pruning** | Stale context leads to wrong assumptions | Proactively flag stale entries for review rather than silently applying outdated context. |

## Guardrails

- NEVER fabricate or infer user context — all stored context must be explicitly provided by the user.
- NEVER store sensitive personal data (passwords, financial accounts, health information, government IDs).
- NEVER present recalled context as current fact without noting the storage date; prompt confirmation for entries older than 90 days.
- Flag outputs: `[From stored context]`, `[User-provided this session]`, `[Suggested]`.

> **Tip:** Ask for Markdown or DOCX output of your context summary via companyFILES to get a formatted, shareable overview.
