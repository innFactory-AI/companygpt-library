---
name: en-runbook
description: Create standard operating procedures and operational runbooks with step-by-step execution guides and escalation paths. Use when documenting a repeatable operational procedure, creating on-call guides, or standardising team workflows. Trigger with "write a runbook for", "create SOP for", "document this procedure".
---

# Runbook Skill

Create operational runbooks and SOPs with step-by-step execution guides, decision trees, escalation paths, and verification checks. All technical details come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Monitoring / alerting via MCP** (e.g. PagerDuty, Datadog, Grafana) | Alert definitions, trigger conditions, severity levels, on-call rotations |
| **Ticketing / tracker via MCP** (e.g. Jira, ServiceNow, Notion) | Existing procedures, escalation history, ownership assignments |
| **companyRAG / file upload** | Architecture notes, past incident reports, technical documentation, configuration exports |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Runbook vs. SOP

Use the right document type for the context:

| Attribute | Runbook | SOP |
| --- | --- | --- |
| **Purpose** | Execute a specific operational procedure in response to a trigger | Standardise a recurring business process |
| **Audience** | Operator performing the procedure (often under time pressure) | Anyone performing the process (routine execution) |
| **Trigger** | Specific event, alert, or request | Recurring schedule or business event |
| **Tone** | Direct, imperative, concise — "do this, then check that" | Descriptive, thorough — "this step ensures quality by..." |
| **Decision trees** | Essential — multiple paths based on observations | Fewer — mostly linear with documented exceptions |
| **Verification** | After every critical step — "confirm X before proceeding" | At quality gates and handoff points |

Both types follow the same structural methodology below; adjust tone and detail level based on the document type.

## Runbook Structure

### Metadata Header

Every runbook starts with essential metadata for quick orientation:

    RUNBOOK: [Procedure Name]
      Version:        [document version]
      Last updated:   [date]
      Owner:          [role responsible for maintaining this runbook]
      Reviewed by:    [who validated the procedure]
      Review cadence: [how often this runbook is re-validated]
      Trigger:        [what event or condition activates this procedure]
      Audience:       [who should execute this — role and required access level]
      Estimated time: [typical duration to complete]
      Severity:       [if applicable — impact level of the triggering event]

### Prerequisites Section

List everything the operator needs before starting — this prevents mid-procedure delays:

    PREREQUISITES:
      Access required:
        - [system/tool] — [permission level needed]
        - [system/tool] — [permission level needed]

      Information needed:
        - [data point] — [where to find it]
        - [data point] — [where to find it]

      Tools/resources:
        - [tool] — [purpose in this procedure]

      Prior conditions:
        - [condition that must be true before starting]

### Step-by-Step Procedure

Each step follows a consistent structure optimised for execution under pressure:

    STEP [number]: [Action verb + what]
      Action:        [precise instruction — what to do, where to do it, how to do it]
      Expected:      [what you should observe if the step succeeds]
      If unexpected: [what to do if the outcome differs — branch to decision tree or escalate]
      Verify:        [how to confirm the step completed correctly before moving on]
      Caution:       [warnings about common mistakes or destructive actions, if applicable]
      Rollback:      [how to undo this step if needed, if applicable]

### Writing Principles for Runbook Steps

- One action per step: If a step contains "and", it's probably two steps
- Imperative mood: "Restart the service" not "The service should be restarted"
- Concrete references: "Run [command] in [location]" not "Execute the relevant command"
- Expected outcomes for every step: The operator must know what "success" looks like before proceeding
- Explicit verification: Never rely on "it should work" — include a verification action
- No assumed knowledge: Write for a qualified team member who has never performed this specific procedure. Include what to look for, not just what to do.

## Decision Trees

For procedures with multiple paths based on observations or conditions:

### Decision Point Structure

    DECISION: [What are you observing or checking?]
      IF [condition A]:
        → [Action or go to Step X]
      IF [condition B]:
        → [Action or go to Step Y]
      IF [none of the above / unclear]:
        → Escalate to [role] via [channel] with [information to provide]

### Decision Tree Design Rules

- Every branch must end in either a resolution, a continuation to another step, or an escalation
- Never leave a dangling branch — "if something else, figure it out" defeats the purpose
- Include the "unclear / none of the above" catch-all — reality often presents conditions not in the tree
- Keep decision trees shallow (2-3 levels maximum). Deeper trees should be broken into sub-procedures.

## Escalation Design

### Escalation Matrix

Define who to contact, when, and how:

    ESCALATION MATRIX:
      Level 1 — [role/team]:
        When:    [conditions triggering L1 escalation]
        Contact: [how to reach them — channel, not personal phone numbers in the document]
        SLA:     [expected response time]
        Provide: [information they need from you]

      Level 2 — [role/team]:
        When:    [conditions triggering L2 — typically time-based or severity-based]
        Contact: [channel]
        SLA:     [expected response time]
        Provide: [information needed]

      Level 3 — [role/team]:
        When:    [conditions triggering L3 — critical impact or extended duration]
        Contact: [channel]
        SLA:     [expected response time]
        Provide: [information needed]

### Escalation Trigger Guidelines

| Trigger Type | Description | Example |
| --- | --- | --- |
| **Time-based** | Procedure exceeds expected duration without resolution | "If not resolved within 30 minutes, escalate to L2" |
| **Severity-based** | Impact is greater than initially assessed | "If customer-facing impact confirmed, escalate to L2 immediately" |
| **Competency-based** | Operator reaches a step requiring expertise they don't have | "If database recovery is needed, escalate to DBA on-call" |
| **Authority-based** | Action requires approval the operator cannot give | "If downtime window extension needed, escalate to [role]" |
| **Uncertainty-based** | Operator is unsure about the correct path | "If symptoms don't match any decision tree branch, escalate to L1" |

## Communication Templates

Include pre-written communication templates for common scenarios during procedure execution:

    COMMUNICATION TEMPLATE — [Scenario Name]
      Audience: [who receives this communication]
      Channel:  [where to send it]
      When:     [at which point in the procedure]
      Template:
        Subject: [template with placeholders]
        Body:    [template with placeholders — keep brief, factual, and actionable]

Placeholders use [BRACKETS] for values the operator fills in. Example: "Incident started at [TIME]. Impact: [DESCRIPTION]. Current status: [STATUS]. Next update at [TIME]."

## Verification and Testing

### Runbook Validation Process

Before a runbook is considered production-ready:

1. Technical review: Subject-matter expert validates that the steps are correct and complete
2. Walk-through test: Someone other than the author executes the procedure in a non-production environment (or traces through it step by step if no test environment exists)
3. Blind test: A qualified team member who was NOT involved in writing the runbook attempts to execute it using only the document. If they get stuck, the runbook needs improvement.
4. Edge case review: Identify scenarios not covered by the main flow — add decision trees or escalation paths as needed

### Post-Execution Review

After each real execution of the runbook:

    POST-EXECUTION REVIEW:
      Date:               [when the procedure was executed]
      Executed by:        [operator]
      Trigger:            [what initiated the procedure]
      Duration:           [actual time to complete]
      Steps followed:     [confirm all steps were executed as written]
      Deviations:         [any steps where the actual procedure differed from the document]
      Issues encountered: [problems with the runbook itself — unclear steps, missing information, incorrect sequence]
      Outcome:            [result of the procedure]
      Updates needed:     [specific changes to make to the runbook based on this execution]

## Runbook Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
| --- | --- | --- |
| **Wall of prose** | Impossible to follow under pressure | Numbered steps with clear action/verify structure |
| **Assumed context** | Fails for anyone other than the original author | Explicit prerequisites, expected outcomes, and system references |
| **Happy path only** | No guidance when things don't go as expected | Decision trees and escalation paths for deviations |
| **Stale contacts** | Escalation fails because contacts have changed | Reference roles and channels, not individual names; include a maintenance cadence |
| **No verification steps** | Operator proceeds without confirming success, cascading errors | Verify after every critical action |
| **Destructive steps without rollback** | No recovery path if the action causes harm | Document rollback for any step that modifies state |
| **Missing "do not" warnings** | Common mistakes not flagged | Include cautions where destructive mistakes are likely |

## Output Template

    # [Runbook/SOP]: [Procedure Name]

    ## Metadata
    [Header from metadata section]

    ## Prerequisites
    [Access, information, tools, and prior conditions]

    ## Procedure
    [Numbered steps with action/expected/verify structure]

    ## Decision Trees
    [Decision points with branching paths]

    ## Escalation Matrix
    [Tiered escalation with triggers, contacts, and SLAs]

    ## Communication Templates
    [Pre-written messages for stakeholder updates]

    ## Rollback Procedure
    [How to undo the procedure if needed — reverse order of critical steps]

    ## Post-Execution Checklist
    [Quick checklist for the operator to complete after finishing]

    ## Revision History
    | Version | Date | Author | Changes |
    |---------|------|--------|---------|

## Guardrails

- Never generate system commands, IPs, URLs, or credentials from training data. All technical details come from the user.
- Never invent escalation contacts, SLA times, or thresholds. Use `[to be defined by team]` placeholders. When the description is incomplete, identify gaps and ask.
- Never assume the technology stack or communication channels. Ask the user for specifics.
- Label generated content: `[From procedure description]`, `[Framework methodology]`, `[Placeholder — define with operations team]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted document ready for distribution.
