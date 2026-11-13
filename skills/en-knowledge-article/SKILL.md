---
name: en-knowledge-article
description: Draft searchable, publish-ready knowledge base articles from resolved issues, workarounds, or FAQs. Use when closing a support ticket with a reusable solution, documenting a new process, or refreshing stale KB content. Trigger with "write KB article for", "turn this into a knowledge article", "document this solution".
---

# Knowledge Article Skill

Build searchable knowledge base articles from resolved incidents, workarounds, or FAQs. The skill follows KCS principles — capturing knowledge as a by-product of solving problems. Technical content comes from you, resolved tickets, or connected sources.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **ITSM / KB via MCP** (e.g. ServiceNow, Confluence, SharePoint) | Resolved tickets, existing articles, resolution notes, KB structure |
| **companyRAG collections** | Internal runbooks, process documentation, prior solutions |
| **File upload** | Ticket exports, screenshots, configuration excerpts, mail threads |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Article Type Classification

Classify the article before writing. Type determines structure, tone, and expected content.

| Type | Purpose | When to Use | Typical Length |
| --- | --- | --- | --- |
| **How-To** | Step-by-step instructions to accomplish a task | User needs to perform a specific action (setup, configure, enable, migrate) | 300-800 words |
| **Troubleshooting** | Diagnose and resolve a specific problem | User encounters an error, unexpected behavior, or failure | 400-1000 words |
| **Reference** | Factual information about a system, feature, or policy | User needs to look up specifications, limits, permissions, or configuration options | 200-600 words |
| **FAQ** | Answers to commonly asked questions on a topic | Multiple users ask the same question; onboarding or launch scenarios | 200-500 words |

When the source material fits multiple types, split into separate articles rather than creating a hybrid. A troubleshooting article that requires setup steps should link to a how-to article for the setup, not inline it.

---

## Article Templates

### How-To Article

```
# How to [Action] [Object]

## Overview
[1-2 sentences: what this article helps the user accomplish and when they would need to.]

## Prerequisites
- [Required access, permissions, or roles]
- [Required software versions or configurations]
- [Required prior steps — link to other articles if applicable]

## Steps

### Step 1: [Action verb] [object]
[Instruction. One action per step. Include the expected outcome.]

### Step 2: [Action verb] [object]
[Instruction.]

> **Note:** [Conditional information — only include if a step has a common variation or gotcha.]

### Step 3: [Action verb] [object]
[Instruction.]

## Verification
[How the user confirms the task was completed successfully. Specific observable outcome.]

## Related Articles
- [Link to related how-to, troubleshooting, or reference articles]
```

### Troubleshooting Article

```
# [Error message / Symptom description]

## Symptoms
- [Observable symptom 1 — what the user sees, exact error text if applicable]
- [Observable symptom 2]

## Affected Systems
- [Product, service, or component]
- [Version(s) affected, if relevant]
- [Environment: production, staging, specific OS/browser]

## Cause
[Brief explanation of what causes this issue. Technical enough to be useful, plain enough for the target audience.]

## Resolution

### Option A: [Primary fix — most common or most reliable]
1. [Step]
2. [Step]
3. [Verification step]

### Option B: [Alternative fix — if Option A doesn't apply]
1. [Step]
2. [Step]
3. [Verification step]

## Workaround
[If no permanent fix exists yet: temporary workaround with any limitations noted.]

## Prevention
[How to avoid this issue in the future, if applicable.]

## Related Articles
- [Links]
```

### Reference Article

```
# [System/Feature/Component] Reference

## Overview
[1-2 sentences: what this reference covers.]

## [Category 1]

| Parameter | Value | Notes |
|-----------|-------|-------|
| [name] | [value] | [constraints, defaults, edge cases] |

## [Category 2]

[Structured information — tables, lists, or definition blocks depending on content type.]

## Permissions / Access

| Role | Access Level | Notes |
|------|-------------|-------|
| [role] | [read/write/admin/none] | [conditions] |

## Related Articles
- [Links]
```

### FAQ Article

```
# [Topic] — Frequently Asked Questions

## [Question 1 — phrased exactly as users ask it]
[Answer. Direct, concise. Link to detailed articles for complex topics rather than inlining full explanations.]

## [Question 2]
[Answer.]

## [Question 3]
[Answer.]

## Still Need Help?
[Escalation path: support channel, team contact, or ticket creation link.]
```

---

## Writing Guidelines

### Structure Rules

1. Title = user's language. Write the title the way a user would search for it. "How to reset MFA" not "Multi-Factor Authentication Token Regeneration Procedure." Match the vocabulary your users actually use.
2. One article, one topic. If you need a conjunction ("and", "or") in the title, consider splitting into two articles.
3. Lead with the answer. Put the most critical information first. Troubleshooting articles start with the fix, not the theory. Users scanning for solutions should find them without scrolling.
4. One action per step. Each numbered step should be a single, verifiable action. "Click Settings, then navigate to Security, then enable MFA" is three steps, not one.
5. Include verification. Every how-to and troubleshooting article ends with how the user confirms success. "You should see [specific outcome]" is better than "The process is complete."
6. Link, don't duplicate. If prerequisite steps exist in another article, link to it. Duplicated content becomes inconsistent over time.

### Language and Tone

- Active voice, imperative mood for instructions: "Click Save" not "The Save button should be clicked"
- Second person for the reader: "You can configure..." not "Users can configure..."
- Present tense for system behavior: "The system displays an error" not "The system will display an error"
- Exact UI labels in bold: Click Settings > Security > Enable MFA
- Exact error messages in code formatting: Error: SAML assertion expired
- No jargon without definition for the target audience. An article for end-users should not assume familiarity with backend terminology. An article for sysadmins can.
- No hedging language: Remove "simply", "just", "easily" — if it were simple, users wouldn't need the article

### Search Optimization for Internal KB

Internal knowledge bases rely on keyword matching and metadata. Optimize for findability:

1. Title: Include the exact action or error message users search for. Front-load the key terms.
2. Synonyms and alternate phrasing: Include a metadata section or opening paragraph that naturally uses alternate terms users might search for. If the article is about "resetting MFA", mention "two-factor authentication", "2FA", "authenticator app" in the overview.
3. Error codes and exact messages: Include the verbatim error string users would copy-paste into search. Wrap in code formatting for clarity.
4. Tags/labels: Suggest category tags based on: product area, user role, issue type, affected platform.
5. Cross-links: Every article should link to 2-5 related articles. This improves both discoverability and navigation.

### Metadata Block

Include this metadata at the top of every article for KB platform ingestion:

```
Article ID: [auto-generated or manually assigned]
Type: [How-To / Troubleshooting / Reference / FAQ]
Product/Service: [name]
Audience: [End User / IT Admin / Developer / All]
Tags: [comma-separated]
Created: [date]
Last Reviewed: [date]
Review Cycle: [quarterly / semi-annual / annual / on-change]
Owner: [team or individual]
Status: [Draft / In Review / Published / Archived]
```

---

## Article Quality Checklist

Before publishing, verify:

- Title matches how users search for this topic
- Article type is correct and template is followed
- Prerequisites are listed (or stated as "none")
- Steps are numbered, single-action, and verifiable
- Verification/confirmation step is included
- Error messages and UI labels are exact (copy-pasted, not paraphrased)
- Screenshots or examples are current (if referenced)
- No duplicated content — links used instead
- Metadata block is complete
- 2-5 related articles are linked
- Review date is set based on content volatility
- Tone matches target audience

---

## Article Lifecycle Management

### Review Triggers

Articles should be reviewed when:

- The underlying system, feature, or process changes
- A support ticket references the article and the solution didn't work
- The scheduled review date is reached
- Article feedback (thumbs down, comments) indicates a problem

### Archival Criteria

Archive (do not delete) articles when:

- The product or feature has been decommissioned
- The issue is resolved permanently by a system change (mark as "Resolved — no longer applicable" and archive)
- A newer article supersedes this one (add a redirect or "superseded by" link before archiving)

---

## Guardrails

- Never invent solutions. All resolution steps, configurations, and commands come from the user's input or verified knowledge. Ask for missing steps rather than generating plausible-sounding instructions.
- Never fabricate error messages, UI labels, or menu paths. These must come verbatim from the source system.
- Never assume software versions or platform details. Ask which version; do not generate version-specific instructions from training data.
- Source-label all output: `[From source material]`, `[Article template]`, or `[AI-drafted — verify before publishing]`.

> **Tip:** Request a Markdown or DOCX export via companyFILES to get a formatted, ready-to-share article.
