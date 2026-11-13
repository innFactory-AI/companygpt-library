---
name: en-process-doc
description: Document business processes with step-by-step workflows, RACI matrices, exception handling, and a maintainable structure. Use when formalising a process, onboarding someone to a workflow, or improving process documentation. Trigger with "document this process", "create a process doc for", "RACI for".
---

# Process Doc Skill

Capture business processes as step-by-step workflows — with RACI matrices, exception handling, and a maintainable structure. All process content comes from your description, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What it contributes |
| --- | --- |
| **Knowledge platform via MCP** (e.g. Confluence, SharePoint) | Existing process descriptions, policies, prior SOPs, role and system references |
| **companyRAG collections** | Internal handbooks, onboarding material, archived procedure documents |
| **File upload** | Process interview notes, workshop transcripts, spreadsheets of roles and SLAs |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Process Mapping

### Information Gathering

Before writing documentation, systematically gather process information:

| Element | Question | Why It Matters |
| --- | --- | --- |
| **Trigger** | What event or condition starts this process? | Defines when the process applies — without a clear trigger, people won't know when to use it |
| **Input** | What information, materials, or prerequisites are needed? | Prevents process failures due to missing inputs |
| **Steps** | What happens, in what order? | The core of the documentation |
| **Decision points** | Where do paths diverge based on conditions? | Ensures the document covers all scenarios, not just the happy path |
| **Roles** | Who performs each step? | Establishes accountability — use role titles, not individual names |
| **Systems** | What tools or systems are used at each step? | Practical execution guidance |
| **Output** | What is produced when the process completes? | Defines "done" — measurable completion criteria |
| **Handoffs** | Where does work pass from one person/team to another? | Handoffs are where processes break — document them explicitly |
| **Exceptions** | What happens when things go wrong or deviate from normal? | Prevents improvisation during exceptions |
| **SLAs/timing** | How long should each step or the overall process take? | Sets expectations and enables monitoring |

### Process Boundary Definition

Clearly define what is IN and OUT of scope for this process document:

```
PROCESS BOUNDARY:
  Process name:   [clear, descriptive name]
  Purpose:        [one sentence — what this process achieves]
  Trigger:        [event or condition that starts the process]
  Starts when:    [first action]
  Ends when:      [completion criteria]
  In scope:       [what this document covers]
  Out of scope:   [what this document explicitly does NOT cover]
  Related processes: [upstream and downstream processes with cross-references]
```

## RACI Matrix Construction

### Role Assignment Methodology

For each step in the process, assign exactly one of four responsibility levels to each involved role:

| Code | Role | Definition | Rule |
| --- | --- | --- | --- |
| **R** | Responsible | Performs the work | At least one R per step; can be shared if genuinely collaborative |
| **A** | Accountable | Approves or has final authority | Exactly ONE A per step — never more; the buck stops here |
| **C** | Consulted | Provides input before the step is completed | Two-way communication — their input is sought and considered |
| **I** | Informed | Notified after the step is completed | One-way communication — told about the outcome |

### RACI Validation Rules

After constructing the matrix, check for these common problems:

| Problem | Symptom | Fix |
| --- | --- | --- |
| **No accountability** | A step has no A | Assign exactly one accountable role |
| **Shared accountability** | A step has multiple As | Choose one; move others to C or R |
| **No responsibility** | A step has no R | Assign the role that does the work |
| **Everyone consulted** | A step has many Cs | Reduce to essential consultees — over-consultation slows the process |
| **Role overload** | One role has R or A on most steps | Redistribute or acknowledge as a single-threaded dependency risk |
| **Orphan roles** | A role appears in the matrix but has no R, A, C, or I on any step | Remove from the matrix or clarify their involvement |

### RACI Output Format

```
| Step | [Role 1] | [Role 2] | [Role 3] | [Role 4] |
|------|----------|----------|----------|----------|
| 1. [Step name] | R | A | C | I |
| 2. [Step name] | I | R/A | | C |
| ... | | | | |
```

## Step Documentation

### Step Structure

Document each step with consistent structure:

```
STEP [number]: [Action verb + object — e.g., "Review submitted request"]
  Responsible:    [role from RACI]
  Input:          [what is needed to start this step]
  Action:         [detailed description of what to do — precise enough for someone unfamiliar with the process]
  System:         [tool or system used, if applicable]
  Decision point: [if this step involves a choice, state the condition and the path for each outcome]
  Output:         [what this step produces]
  Handoff:        [who receives the output and how — email, system notification, manual transfer]
  SLA:            [expected time to complete, if defined]
  Notes:          [edge cases, tips, common mistakes]
```

### Writing Principles for Process Steps

- Start each step with an action verb: "Review", "Submit", "Approve", "Notify" — not "The request is reviewed"
- Be specific about actions: "Click 'Submit' in the approval queue" — not "Submit the request"
- State the condition before the path: "If the amount exceeds €10,000, escalate to Finance Director. Otherwise, approve and proceed to Step 5."
- Document the handoff mechanism: "Send the approved document to [role] via [channel]" — handoffs without explicit mechanisms are where processes fail
- Include what NOT to do when it's a common mistake: "Do NOT approve if the budget code is missing — return to requestor (Step 2)"

## Exception Handling

### Exception Classification

| Exception Type | Definition | Documentation Approach |
| --- | --- | --- |
| **Known exception** | Anticipated deviation with a defined response | Document the exception path inline with the step or in a dedicated exceptions section |
| **Escalation trigger** | Condition requiring a higher authority or different process | Define the escalation criteria, path, and expected response |
| **Error recovery** | Process step fails (system error, incorrect input, etc.) | Document the recovery steps — how to get back on track |
| **Boundary exception** | Request or situation that falls outside the process scope | Define how to identify out-of-scope items and where to redirect them |

### Exception Documentation Format

For each known exception:

```
EXCEPTION: [descriptive name]
  Occurs at:    [which step]
  Condition:    [what triggers the exception]
  Response:     [what to do — step by step]
  Escalation:   [who to contact if the response does not resolve the exception]
  Return point: [where the process resumes after the exception is handled]
```

## Process Document Template

Structure the final document as follows:

```
# [Process Name]

## Overview
- Purpose: [what this process achieves]
- Owner: [role accountable for the process]
- Last reviewed: [date]
- Review frequency: [how often this document is reviewed for accuracy]
- Version: [document version]

## Scope
- Trigger: [what starts the process]
- In scope: [covered]
- Out of scope: [not covered]
- Related processes: [links to upstream/downstream process documents]

## Roles
[Brief description of each role involved — role title, not individual name]

## RACI Matrix
[Matrix from RACI construction]

## Process Steps
[Numbered steps using the step structure above]

## Exceptions
[Exception entries using the exception format above]

## Definitions
[Glossary of process-specific terms — only include terms that are ambiguous or organisation-specific]

## Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| [ver] | [date] | [role] | [what changed] |
```

## Documentation Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
| --- | --- | --- |
| **Wall of text** | Unstructured prose is hard to follow during execution | Use numbered steps, tables, and consistent formatting |
| **Too granular** | Documenting every mouse click makes the document unusable | Document at the decision/action level, not the click level |
| **Too abstract** | "Process the request appropriately" gives no guidance | Be specific about what "appropriately" means in each context |
| **Happy path only** | Ignores exceptions, errors, and edge cases | Document the top 3-5 exceptions explicitly |
| **Individual names** | Breaks when people change roles | Use role titles; maintain a separate role-to-person mapping |
| **Write and forget** | Process evolves but documentation doesn't | Set a review cadence and owner; version the document |
| **Assumed knowledge** | "As you know..." excludes new team members | Write for someone new to the role; include all necessary context |

## Guardrails

- Never generate process steps from training data. All process content comes from the user's description of how work actually happens.
- Never assume roles, systems, or thresholds. Ask the user for specifics. Use `[to be defined by process owner]` for unknowns.
- Never fill in SLAs, budget thresholds, or system names without user input. When the description is incomplete, ask rather than inventing plausible steps.
- Label generated content: `[From process description]`, `[Framework methodology]`, `[Placeholder — define with process owner]`.

> **Tip:** Ask for DOCX, Markdown, or PDF output via companyFILES to get a formatted document ready for distribution. If the document includes a flowchart, companyFILES can render Mermaid diagrams.
