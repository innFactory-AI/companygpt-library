---
name: en-it-docs
description: Write technical documentation, runbooks, architecture decision records, and process guides from informal descriptions. Use when documenting a new system, creating runbooks for operations, or converting tribal knowledge into structured docs. Trigger with "write docs for", "create a runbook", "document this process".
---

# IT Docs Skill

Turn informal descriptions, meeting notes, or tribal knowledge into clean technical documentation — runbooks, ADRs, process guides, and reference docs. The skill routes your input to the correct document type and applies the matching template. Technical content comes from you or your connected sources.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Documentation & wiki via MCP** (e.g. Confluence, SharePoint) | Existing pages, prior runbooks, environment notes, process descriptions |
| **Code & infra via MCP** (e.g. GitHub) | Repository details, configuration files, deployment definitions, READMEs |
| **companyRAG / file upload** | Meeting notes, incident write-ups, architecture sketches, tribal knowledge |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Document Type Router

Classify the documentation request before writing. The document type determines the structure, audience, and level of detail.

| Type | Purpose | Audience | When to Use |
| --- | --- | --- | --- |
| **Runbook** | Step-by-step operational procedures for executing a task or responding to a scenario | On-call engineers, SREs, operations staff | Deploying, restarting, failing over, scaling, recovering, or diagnosing a specific system |
| **ADR** | Record of an architecture or technology decision with context and rationale | Engineering team, future maintainers | Choosing a technology, changing architecture, adopting a pattern, deprecating a component |
| **Process Guide** | Documented workflow for a repeatable business or IT process | IT staff, cross-functional teams | Onboarding, offboarding, access provisioning, change management, incident management |
| **Reference Doc** | Factual description of a system, service, or environment | Anyone who needs to understand the system | System architecture overview, network topology, service catalog entry, environment configuration |

When the request could fit multiple types, ask the user which type they need or recommend based on context. A "document for the deployment" could be a runbook (how to deploy), an ADR (why we chose this deployment strategy), or a reference doc (how the deployment pipeline works).

---

## Runbook Template

Runbooks are for execution under stress. They must be usable by someone who has never touched this system, at 3am, with an alert firing.

```
# Runbook: [Action] [System/Service]

**Owner**: [team]
**Last tested**: [date — runbooks must be tested regularly]
**Last updated**: [date]
**Estimated time**: [how long this procedure takes under normal conditions]

## Purpose
[One sentence: when and why you run this procedure.]

## Prerequisites
- [ ] Access to [system/environment] with [role/permissions]
- [ ] [Tool] installed and configured (version [X]+)
- [ ] [Credential/token] available from [location]

## Pre-Flight Checks
[Verification steps BEFORE executing the procedure. Catch wrong-environment mistakes here.]

1. Verify you are connected to [correct environment]: `[command to verify]`
2. Confirm current state: `[command to check]`
   Expected output: [what you should see]
3. [Additional verification]

## Procedure

### Step 1: [Action verb] [object]
    [exact command or action]
**Expected output**: [what you should see]
**If this fails**: [what to check, what to do]

### Step 2: [Action verb] [object]
    [exact command or action]
**Expected output**: [what you should see]
**If this fails**: [what to check, what to do]

### Step 3: [Action verb] [object]
    [exact command or action]
**Expected output**: [what you should see]
**If this fails**: [what to check, what to do]

## Verification
[How to confirm the procedure was successful.]

1. [Check command or URL]
   Expected: [specific outcome]
2. [Monitor for X minutes]
   Expected: [stable metrics]

## Rollback
[How to undo this procedure if something goes wrong.]

1. [Rollback step]
2. [Rollback step]
3. [Verify rollback was successful]

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| [what you see] | [why] | [what to do] |
| [what you see] | [why] | [what to do] |

## Escalation
If the procedure fails and troubleshooting does not resolve:
- **During business hours**: Contact [team/person] via [channel]
- **After hours**: Page [on-call rotation] via [tool]
```

### Runbook Writing Rules

- Commands must be copy-pasteable. No placeholders that require interpretation under pressure. Use <VARIABLE_NAME> for values that vary and list them in Prerequisites with instructions on where to find them.
- Every step has a failure path. "If this fails" is mandatory for every step. An on-call engineer hitting an unexpected error at 3am needs the next step, not a blank wall.
- Include expected output. Without expected output, the operator doesn't know if the step worked.
- Test the runbook. An untested runbook is fiction. Include a "Last tested" date and make testing part of the review cycle.
- Time estimates are honest. If it takes 45 minutes, don't write 15. Accurate time estimates help incident commanders plan.

---

## Architecture Decision Record (ADR) Template

ADRs capture the WHY behind decisions so future engineers understand the context, not just the outcome.

```
# ADR-[number]: [Decision Title]

**Date**: [date of decision]
**Status**: [Proposed / Accepted / Deprecated / Superseded by ADR-XXX]
**Deciders**: [who made or approved this decision]

## Context
[What situation or problem prompted this decision? What constraints exist?
Describe the technical and business context. A reader 2 years from now should
understand why this decision was being made.]

## Decision Drivers
- [Driver 1: e.g., "Must support 10x current throughput within 6 months"]
- [Driver 2: e.g., "Team has no experience with technology X"]
- [Driver 3: e.g., "Budget constraint of EUR X/month for infrastructure"]

## Options Considered

### Option A: [Name]
[Description of the approach.]
- **Pros**: [advantages]
- **Cons**: [disadvantages]
- **Estimated effort**: [time/cost]

### Option B: [Name]
[Description of the approach.]
- **Pros**: [advantages]
- **Cons**: [disadvantages]
- **Estimated effort**: [time/cost]

### Option C: [Name]
[Description of the approach.]
- **Pros**: [advantages]
- **Cons**: [disadvantages]
- **Estimated effort**: [time/cost]

## Decision
[Which option was chosen and a concise statement of why.]

## Consequences
- **Positive**: [expected benefits]
- **Negative**: [accepted trade-offs and risks]
- **Neutral**: [implications that are neither positive nor negative]

## Follow-Up Actions
- [ ] [Specific action to implement the decision]
- [ ] [Specific action to mitigate known risks]

## References
- [Links to relevant documents, RFCs, or prior ADRs]
```

### ADR Writing Rules

- Context is the most important section. The decision itself is often obvious in hindsight. What's not obvious is WHY it was made — the constraints, pressures, and trade-offs that existed at the time.
- Include rejected options. Future engineers will ask "why didn't we just use X?" The ADR should preemptively answer that.
- Keep ADRs immutable. Don't edit an accepted ADR. If the decision changes, write a new ADR that supersedes it and update the status of the old one.
- Number sequentially. ADR-001, ADR-002, etc. This creates a decision log that can be browsed chronologically.

---

## Process Guide Template

Process guides document repeatable workflows that cross team or system boundaries.

```
# Process: [Process Name]

**Owner**: [team/role responsible for this process]
**Last reviewed**: [date]
**Review cycle**: [quarterly / semi-annual / annual]

## Purpose
[What this process achieves and when it is triggered.]

## Scope
- **In scope**: [what this process covers]
- **Out of scope**: [what this process does NOT cover — link to other processes]

## Roles

| Role | Responsibility |
|------|---------------|
| [Requestor] | [what they do] |
| [Approver] | [what they do] |
| [Executor] | [what they do] |

## Inputs
- [What triggers the process: request form, ticket, event, scheduled date]
- [Required information or artifacts]

## Workflow

### 1. [Phase name]
**Who**: [role]
**Action**: [what they do]
**Output**: [what this phase produces]
**SLA**: [time expectation, if any]

### 2. [Phase name]
**Who**: [role]
**Action**: [what they do]
**Output**: [what this phase produces]
**SLA**: [time expectation, if any]

### 3. [Phase name]
**Who**: [role]
**Action**: [what they do]
**Output**: [what this phase produces]
**SLA**: [time expectation, if any]

## Exception Handling
[What happens when the process hits an edge case or fails at a step.]

| Exception | Action | Escalation |
|-----------|--------|-----------|
| [scenario] | [what to do] | [who to contact] |

## Metrics
| Metric | Definition | Target |
|--------|-----------|--------|
| [e.g., Cycle time] | [end-to-end time from trigger to completion] | [target] |

## Audit Trail
[What records are kept, where, and for how long.]
```

---

## Reference Document Template

Reference docs describe what exists. They are the "current state" documentation that everyone needs but nobody writes.

```
# [System/Service/Component] — Reference

**Owner**: [team]
**Last updated**: [date]

## Overview
[2-3 sentences: what this system does, who uses it, why it exists.]

## Architecture

[High-level description of components and their relationships. Include a diagram
reference if one exists, but do not generate ASCII art that will become stale.]

### Components

| Component | Purpose | Technology | Owner |
|-----------|---------|-----------|-------|
| [name] | [what it does] | [stack] | [team] |

### Dependencies

| Dependency | Type | Impact if Unavailable |
|-----------|------|----------------------|
| [service/system] | [hard / soft] | [what breaks] |

## Configuration

| Parameter | Value | Location | Notes |
|-----------|-------|----------|-------|
| [name] | [current value or reference] | [where configured] | [constraints] |

## Access

| Role | Access Level | How to Request |
|------|-------------|---------------|
| [role] | [read / write / admin] | [process or link] |

## Monitoring

| Alert | Condition | Response |
|-------|----------|----------|
| [alert name] | [trigger condition] | [runbook link or action] |

## Related Documents
- [Runbook: link]
- [ADR: link]
- [Process guide: link]
```

---

## Writing Guidelines for IT Documentation

### Principles

1. Write for the worst case. Documentation is most valuable when things are broken and people are stressed. Assume the reader is under time pressure, unfamiliar with the system, and needs unambiguous instructions.
2. Commands over descriptions. "Run `kubectl get pods -n production`" is better than "Check the pods in the production namespace." Operators copy-paste; they don't interpret prose into commands.
3. Current state only. Document what exists today, not what will exist after a planned migration. Update the docs when the migration is complete, not before.
4. One source of truth. Never duplicate content across documents. Link to the canonical source. Duplicated documentation diverges within weeks.
5. Testable. If someone follows the doc and gets a different result than described, the doc is wrong. Include verification steps so the reader can confirm they are on the right track.

### Formatting Standards

- Headings: Use heading hierarchy strictly (H1 for title, H2 for major sections, H3 for subsections). Never skip levels.
- Commands: Always in code blocks with the shell language specified. Include the full command — no "etc." or "as above."
- Variables: Use <ANGLE_BRACKET_CAPS> for values the reader must substitute. List all variables in the Prerequisites section.
- Tables: Use for structured data (configurations, roles, alerts). Do not use for prose.
- Links: Relative links to other internal docs. Absolute URLs for external references.

---

## Guardrails

- Never generate system-specific commands, configurations, or architecture from training data. If critical details are missing, ask. Use [NEEDS INPUT: ...] placeholders rather than plausible-sounding assumptions.
- Never invent monitoring thresholds, SLA values, or escalation contacts. These are organisation-specific — use [TO BE DEFINED] placeholders.
- Never fabricate tool versions, API endpoints, or infrastructure details. Training data is unreliable for specifics.
- Source-label all output: [From user input], [Document template], or [AI-structured — verify with SME].

> **Tip:** Ask for Markdown, DOCX, or PDF output via companyFILES to get a formatted doc ready to publish.
