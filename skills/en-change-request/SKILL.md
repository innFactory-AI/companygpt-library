---
name: en-change-request
description: Prepare structured IT change requests with risk analysis, rollback plans, and approval routing. Use when scheduling infrastructure changes, deploying to production, or requesting access modifications. Trigger with "prepare change request for", "CR for [change]", "schedule this change".
---

# Change Request Skill

Prepare IT change requests aligned with ITIL 4 change enablement — classification, risk analysis, implementation plans, rollback procedures, test plans, and communication plans. Change-specific details come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **ITSM via MCP** (e.g. ServiceNow, Jira Service Management) | Change records, linked incidents, CAB schedules, affected configuration items |
| **Monitoring / CMDB via MCP** | Service dependencies, blast radius, active alerts, configuration-management data |
| **companyRAG / file upload** | Runbooks, approved standard-change procedures, architecture and reference documentation |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Change Classification

Classify the change before writing the request. Classification determines the approval path, documentation depth, and lead time requirements.

### Change Types

| Type | Definition | Approval Path | Lead Time | Documentation Depth |
| --- | --- | --- | --- | --- |
| **Standard** | Pre-approved, low-risk, repeatable change with a documented procedure. Has been successfully executed before. | Pre-approved — no CAB review | Per procedure SLA | Reference to existing procedure |
| **Normal** | Planned change that requires assessment and approval. May be routine but is not pre-approved. | CAB or delegated approver | Organization-defined (typically 5+ business days) | Full change request |
| **Emergency** | Unplanned change required to restore service or prevent imminent failure. Cannot wait for normal approval cycle. | Emergency CAB (ECAB) or designated authority — retrospective full review | Immediate — approval during or after implementation | Abbreviated request, full post-implementation review |

### Classification Decision Tree

1. Is this a response to an active P1/P2 incident? → Emergency
2. Does an approved standard change procedure exist for this exact change? → Standard
3. Is this a routine, low-risk change that has been done successfully 3+ times with the same procedure? → Candidate for Standard (submit for pre-approval)
4. Everything else → Normal

### Standard Change Criteria

A change qualifies for Standard classification only when ALL of these are true:

- Documented, tested procedure exists and is current
- Risk is well-understood and consistently low
- Change has been executed successfully at least 3 times
- Rollback procedure is documented and tested
- No change to the change scope since the procedure was approved
- Approved by the CAB or change authority as a standard change

If ANY criterion is not met, classify as Normal regardless of how "simple" the change seems.

---

## Change Request Template

### Standard Change Request

```
# Standard Change Request

**Change ID**: [auto-generated or assigned]
**Date**: [date]
**Requestor**: [name, team]

## Change Description
**Standard change procedure**: [reference to approved procedure ID/name]
**What is being changed**: [specific instance — which server, service, or environment]
**Scheduled window**: [date and time]
**Estimated duration**: [time]

## Pre-Conditions
- [ ] Procedure [ID] is current (last reviewed: [date])
- [ ] All prerequisites from procedure are met
- [ ] Rollback procedure is ready
- [ ] Affected parties notified (if required by procedure)

## Implementation
Per procedure [ID]. No deviations.

## Post-Implementation Verification
Per procedure [ID] verification steps.
```

### Normal Change Request

```
# Change Request: [CR-number]

**Date**: [date]
**Requestor**: [name, team]
**Change type**: Normal
**Priority**: [Critical / High / Medium / Low]
**Target date**: [requested implementation date]

## 1. Change Description

### What is being changed
[Precise description of the change. Specific enough that someone unfamiliar with the context can understand what will be different after the change.]

### Why this change is needed
[Business or technical justification. What problem does this solve? What happens if we don't make this change?]

### Scope
- **In scope**: [what this change covers]
- **Out of scope**: [what this change does NOT cover]
- **Systems affected**: [list of systems, services, or components]
- **Environments**: [production, staging, etc.]
- **Users affected**: [who will notice this change and how]

## 2. Risk Assessment

### Risk Classification

Evaluate each risk dimension:

| Dimension | Rating (H/M/L) | Justification |
|-----------|----------------|--------------|
| **Service impact** | [H/M/L] | [What breaks if this goes wrong?] |
| **User impact** | [H/M/L] | [How many users affected? Can they work around it?] |
| **Complexity** | [H/M/L] | [How many components, dependencies, or manual steps?] |
| **Reversibility** | [H/M/L] | [How easily can this be rolled back? Data loss risk?] |
| **Change window** | [H/M/L] | [Is the window sufficient? What happens if it overruns?] |
| **Dependency risk** | [H/M/L] | [Does this depend on other changes, teams, or vendors?] |

### Overall Risk Score

| Ratings | Overall Risk | Approval Level |
|---------|-------------|---------------|
| All Low | Low | Team lead + change manager |
| Any Medium, no High | Medium | CAB review |
| Any High | High | CAB review + senior management |
| Multiple High or Critical service | Critical | CAB review + VP/CTO approval |

### Identified Risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|-----------|
| 1 | [what could go wrong] | [H/M/L] | [H/M/L] | [how to prevent or reduce] |
| 2 | [what could go wrong] | [H/M/L] | [H/M/L] | [how to prevent or reduce] |

## 3. Implementation Plan

### Pre-Implementation Checklist
- [ ] [Prerequisite 1: e.g., backup completed and verified]
- [ ] [Prerequisite 2: e.g., monitoring dashboards open]
- [ ] [Prerequisite 3: e.g., rollback procedure reviewed by implementor]
- [ ] [Prerequisite 4: e.g., communication sent to affected parties]

### Implementation Steps

| Step | Action | Responsible | Estimated Time | Verification |
|------|--------|------------|---------------|-------------|
| 1 | [specific action] | [who] | [time] | [how to verify success] |
| 2 | [specific action] | [who] | [time] | [how to verify success] |
| 3 | [specific action] | [who] | [time] | [how to verify success] |

### Change Window
- **Start**: [date, time, timezone]
- **End**: [date, time, timezone]
- **Maintenance window required**: [Yes/No — will users experience downtime?]
- **Backup window**: [date, time — if the primary window is missed]

## 4. Test Plan

### Pre-Change Testing
[What testing was done before requesting this change? Test environment, test cases, results.]

| Test | Environment | Result | Date |
|------|------------|--------|------|
| [test description] | [env] | [Pass/Fail] | [date] |

### Post-Change Verification
[How to verify the change was successful in production.]

| Verification | Expected Result | Actual Result |
|-------------|----------------|--------------|
| [check] | [what success looks like] | [filled in during implementation] |

### Smoke Test Procedure
[Minimal set of checks to confirm basic functionality immediately after the change.]

1. [Check 1 — critical path verification]
2. [Check 2 — integration point verification]
3. [Check 3 — user-facing functionality verification]

## 5. Rollback Plan

### Rollback Decision Criteria
Initiate rollback if ANY of these conditions are met:
- [Criterion 1: e.g., post-change verification fails for any critical check]
- [Criterion 2: e.g., error rate exceeds X% within 30 minutes]
- [Criterion 3: e.g., change window is exceeded by more than 30 minutes]

### Rollback Procedure

| Step | Action | Responsible | Estimated Time |
|------|--------|------------|---------------|
| 1 | [rollback action] | [who] | [time] |
| 2 | [rollback action] | [who] | [time] |
| 3 | [verify rollback successful] | [who] | [time] |

### Rollback Limitations
[Any scenarios where rollback is not possible or is only partial. What happens to data created between deployment and rollback? Are there any irreversible steps?]

**Total estimated rollback time**: [time]
**Data impact of rollback**: [none / data loss risk described / manual intervention needed]

## 6. Communication Plan

### Pre-Change Communication

| Audience | Channel | Timing | Message |
|----------|---------|--------|---------|
| [affected users] | [email/Slack/Teams] | [X days before] | [scheduled maintenance notice] |
| [support team] | [channel] | [X days before] | [impact briefing, expected tickets] |
| [management] | [channel] | [at approval] | [change summary, risk, schedule] |

### During-Change Communication

| Event | Audience | Channel | Message |
|-------|----------|---------|---------|
| Change started | [who] | [where] | [change in progress, ETA] |
| Change completed | [who] | [where] | [change complete, verification in progress] |
| Issues detected | [who] | [where] | [issue description, investigating] |
| Rollback initiated | [who] | [where] | [rollback in progress, ETA] |

### Post-Change Communication

| Audience | Channel | Timing | Message |
|----------|---------|--------|---------|
| [affected users] | [channel] | [within 1h of completion] | [change complete, action required (if any)] |
| [management] | [channel] | [within 1h of completion] | [change outcome summary] |

## 7. Approval

| Approver Role | Name | Decision | Date |
|--------------|------|----------|------|
| Change Manager | [name] | [Approved / Rejected / Deferred] | [date] |
| CAB (if required) | [members] | [Approved / Rejected / Deferred] | [date] |
| Senior Management (if required) | [name] | [Approved / Rejected / Deferred] | [date] |

**Approval conditions**: [any conditions attached to approval]
```

### Emergency Change Request

```
# Emergency Change Request: [ECR-number]

**Date**: [date, time]
**Requestor**: [name, team]
**Related incident**: [incident ID — link to active incident]
**Approved by**: [ECAB member or designated authority]

## What
[One paragraph: what is being changed and why it cannot wait for normal process.]

## Risk
[Brief risk assessment — what could go wrong with this change. Emergency does not mean unassessed.]

## Implementation
[Steps, in order. Concise but complete.]

## Rollback
[How to undo if the change makes things worse.]

## Post-Implementation
- [ ] Retrospective change request submitted within [24/48h] for full CAB review
- [ ] Post-implementation review completed
- [ ] Incident post-mortem includes the emergency change
```

---

## Risk Assessment Deep Dive

### Service Dependency Analysis

Before assessing risk, map the change's blast radius:

1. Direct dependencies: Systems that directly consume or are consumed by the changed component
2. Indirect dependencies: Systems one hop removed — they depend on a system that depends on the changed component
3. Shared infrastructure: Load balancers, DNS, authentication services, databases that the changed component shares with other services

A "simple" change to a shared authentication service has a much larger blast radius than a change to an isolated microservice. The risk classification must reflect this.

### Change Conflict Detection

Check for conflicts with:

- Other changes scheduled in the same window
- Ongoing incidents that affect the same systems
- Freeze periods (code freezes, release moratoriums, regulatory audit windows)
- Major business events (end of quarter, product launches, peak traffic periods)

---

## Post-Implementation Review

Every change (including Standard changes) should have a lightweight post-implementation check. Normal and Emergency changes require a documented review.

### Review Checklist

- All post-change verifications passed
- No unexpected alerts triggered within the monitoring period
- No increase in error rates or support tickets
- Change documented in the configuration management database (CMDB) or equivalent
- Related documentation updated (runbooks, architecture docs, reference docs)
- Lessons learned captured (for non-trivial changes)

### Metrics to Track

| Metric | Definition | Purpose |
| --- | --- | --- |
| **Change success rate** | Percentage of changes implemented without rollback or incident | Measures change quality |
| **Change lead time** | Time from request submission to implementation | Measures process efficiency |
| **Emergency change ratio** | Percentage of changes classified as Emergency | High ratio indicates process gaps or chronic underinvestment |
| **Failed change rate** | Percentage of changes that required rollback | Identifies systemic implementation issues |
| **Change-related incidents** | Incidents caused by changes within 48h of implementation | Measures change risk management effectiveness |

---

## Guardrails

- Never generate system-specific implementation steps from training data. All technical details come from the user or referenced runbooks. If critical steps are missing, ask.
- Never fabricate rollback procedures. Flag missing rollback plans as `[ROLLBACK PLAN REQUIRED]` rather than generating plausible-sounding steps.
- Never invent approval routing, CAB membership, or change windows. These are organisation-specific. Flag incomplete sections explicitly as blockers.
- Source-label all output: `[From change description]`, `[Change request template]`, or `[AI-structured — verify with change authority]`.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted change request ready to share.
