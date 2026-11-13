---
name: en-postmortem
description: Blameless incident postmortem with timeline reconstruction, root-cause analysis, and action items. Use after a production incident, service outage, or significant bug. Trigger with "run postmortem for", "incident review", "what went wrong".
---

# Postmortem Skill

Blameless postmortem methodology for production incidents, service outages, and significant defects. It reconstructs timelines, performs 5 Whys root-cause analysis, and produces action-item-driven reports that prevent recurrence. Incident data comes from you, a connected MCP source, or companyRAG collections.

## Blameless Principles

Every postmortem conducted with this skill follows these non-negotiable principles:

1. **People are not the root cause.** Systems, processes, and tooling fail — individuals operating within those systems made the best decisions they could with the information available. The postmortem examines the system that allowed the failure, not the person who triggered it.
2. **Hindsight is not foresight.** It is easy to see what should have been done after the fact. The postmortem must reconstruct what was known and visible at each decision point during the incident — not judge decisions with information that was unavailable at the time.
3. **The goal is learning, not punishment.** A postmortem that assigns blame guarantees that the next incident will be hidden or downplayed. A postmortem that produces actionable improvements guarantees that the team gets better.
4. **Every incident has multiple contributing factors.** Single-cause narratives ("the developer pushed a bad config") are almost always incomplete. The postmortem must identify the chain of contributing factors — the missing test, the inadequate review, the absent alert, the unclear runbook — that collectively allowed the incident.
5. **Action items without owners and deadlines are wishes.** Every postmortem action item must have an owner, a deadline, and a verification method. Unowned action items from previous postmortems should be reviewed before generating new ones.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **APM / monitoring via MCP** (e.g. Datadog, Grafana, PagerDuty) | Alert triggers, metric anomalies, error rates, latency spikes, affected services |
| **Git provider via MCP** (e.g. GitHub, GitLab, Bitbucket) | Commits and deployments in the time window around the incident |
| **CI/CD via MCP** (e.g. GitHub Actions, GitLab CI, Jenkins) | Build/deploy events, rollback events, pipeline status |
| **Chat via MCP** (e.g. Slack, Teams) | Incident channel messages, decisions made, escalation points |
| **Project tracker via MCP** (e.g. Jira, Linear, Asana) | Incident ticket, related bugs, previous postmortem action items |
| **companyRAG / file upload** | Prior postmortems, recurring patterns, existing runbooks, status updates |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Postmortem Workflow

### Phase 1: Establish the Facts

Before analysis, collect the raw facts of the incident. Resist the urge to explain — first document what happened.

**Incident identification:**

| Field | Content |
| --- | --- |
| **Incident ID** | Tracking identifier (ticket number, incident number) |
| **Severity** | SEV-1 (critical) / SEV-2 (major) / SEV-3 (minor) — per the organisation's severity definitions |
| **Duration** | Time from detection to full resolution |
| **Impact** | Who was affected, how many, what functionality was degraded or unavailable |
| **Detection method** | How was the incident discovered? Alert, customer report, internal observation, automated check |
| **Time to detect (TTD)** | Elapsed time from incident start to detection |
| **Time to mitigate (TTM)** | Elapsed time from detection to customer impact resolved |
| **Time to resolve (TTR)** | Elapsed time from detection to root cause fixed |

**Data collection checklist:**

- Monitoring alerts and timestamps from APM/observability tools
- Deployment and commit history from CI/CD and git provider for the 24h before the incident
- Incident channel or war-room chat logs
- Customer reports or support tickets filed during the incident
- Status page updates and their timestamps
- On-call rotation — who was paged and when
- Any rollback, hotfix, or mitigation actions taken and their timestamps

### Phase 2: Reconstruct the Timeline

Build a chronological timeline from the collected data. The timeline is the backbone of the postmortem — all analysis flows from it.

**Timeline format:**

```
| Time (UTC) | Event | Source | Actor |
|------------|-------|--------|-------|
| [HH:MM] | [What happened] | [Where this was observed] | [Person or system] |
```

**Timeline construction rules:**

1. Use UTC consistently. Timezone confusion during incident analysis is a secondary incident.
2. Separate observation from interpretation. "Error rate exceeded 5% threshold" is an observation. "The deployment caused errors" is an interpretation — it belongs in the analysis, not the timeline.
3. Include system events and human actions. Deployments, alert firings, rollbacks, configuration changes, and communication events all belong on the timeline.
4. Mark uncertainty. When the exact time of an event is unknown, use "~HH:MM (approximate)" rather than guessing a precise time.
5. Identify the key transitions. Mark these explicitly:   - Incident start : When the system first entered a degraded state (may be before detection)   - Detection : When a human or system first identified the problem   - Escalation : When additional people or teams were engaged   - Mitigation : When customer impact was reduced or eliminated   - Resolution : When the root cause was fixed (not just mitigated)

### Phase 3: Identify Contributing Factors

List every factor that contributed to the incident occurring, going undetected, or taking longer to resolve. Contributing factors are NOT assigned to individuals — they are systemic observations.

**Contributing factor categories:**

| Category | Examples |
| --- | --- |
| **Code / Configuration** | Bug in business logic, incorrect configuration value, missing validation, untested edge case |
| **Testing** | Missing test coverage for the failure mode, test that didn't reflect production conditions, load test gap |
| **Deployment** | Missing canary phase, no automated rollback, configuration change without feature flag |
| **Monitoring / Alerting** | Missing alert for the failure mode, alert threshold too high, noisy alert masked the real signal |
| **Runbook / Documentation** | No runbook for this failure mode, outdated runbook, missing escalation path |
| **Architecture** | Single point of failure, missing circuit breaker, no graceful degradation, cascading dependency |
| **Communication** | Delayed escalation, unclear ownership, information siloed in one team |
| **Process** | Skipped code review, bypassed staging environment, manual step in deployment pipeline |
| **External** | Third-party service outage, unexpected traffic pattern, upstream API behaviour change |

For each contributing factor, note:

- What the factor was
- How it contributed to the incident (caused it, worsened it, delayed detection, or delayed resolution)
- Whether this factor has appeared in previous postmortems (recurring pattern)

### Phase 4: Root-Cause Analysis (5 Whys)

Apply the 5 Whys technique to trace from the symptom to the deepest actionable cause. The technique asks "why" iteratively until reaching a systemic cause that can be addressed to prevent recurrence.

**5 Whys structure:**

```
Symptom: [Observable problem — e.g., "Customers received 500 errors on the checkout page for 45 minutes"]

Why 1: [Direct cause]
  Evidence: [What data supports this]

Why 2: [Cause of the direct cause]
  Evidence: [What data supports this]

Why 3: [Deeper cause]
  Evidence: [What data supports this]

Why 4: [Systemic cause]
  Evidence: [What data supports this]

Why 5: [Root cause — the deepest actionable cause]
  Evidence: [What data supports this]

Root cause statement: [One sentence summarising the systemic failure that must be addressed]
```

**5 Whys discipline:**

- Stop when you reach an actionable systemic cause. "The developer made a mistake" is not a root cause — it is a proximate cause. Continue asking why the system allowed the mistake to reach production.
- Branch when multiple paths exist. A single chain of 5 Whys may not capture all root causes. If the incident had multiple independent contributing paths, run a separate 5 Whys chain for each.
- Verify each "why" with evidence. Each step must be supported by data from the timeline or collected evidence. A 5 Whys chain based on assumptions produces a false root cause.
- Distinguish root cause from contributing factors. The root cause is the single most impactful systemic failure. Contributing factors made the incident possible or worse, but fixing only the root cause would not necessarily have prevented the incident. Both need action items.

### Phase 5: Generate Action Items

Every contributing factor and the root cause must map to at least one action item. Action items without this mapping are unbounded — they may feel productive but do not address the incident.

**Action item requirements:**

| Field | Required | Content |
| --- | --- | --- |
| **ID** | Yes | Unique identifier (e.g., AI-001) |
| **Description** | Yes | Specific, concrete action — not "improve monitoring" but "Add alert for checkout error rate exceeding 2% sustained for 5 minutes" |
| **Addresses** | Yes | Which contributing factor or root cause this action item addresses |
| **Priority** | Yes | P1 (prevents recurrence of this incident) / P2 (reduces blast radius or detection time) / P3 (general improvement surfaced by this incident) |
| **Owner** | Yes | Named individual or team responsible for completion |
| **Deadline** | Yes | Target completion date |
| **Verification** | Yes | How completion will be verified (e.g., "Alert fires correctly in staging test", "Runbook updated and reviewed by on-call team") |

**Action item categories:**

| Category | Purpose | Examples |
| --- | --- | --- |
| **Fix** | Eliminate the root cause | Code fix, configuration correction, architecture change |
| **Detect** | Catch this failure mode earlier next time | New alert, improved monitoring dashboard, automated health check |
| **Mitigate** | Reduce blast radius if this class of failure recurs | Circuit breaker, feature flag, graceful degradation, automated rollback |
| **Prevent** | Stop this class of failure from being introduced | Test coverage, code review checklist update, deployment gate, linting rule |
| **Document** | Ensure the team can respond faster next time | New or updated runbook, escalation path documentation, architecture diagram |

**Review prior action items:** Before finalising, check whether previous postmortems generated similar action items that were never completed. Recurring action items are a systemic signal — escalate them.

### Phase 6: Write the Postmortem Report

Compile all findings into the output template below.

## Output Template

```
# Postmortem: [Incident Title]
**Incident ID**: [ID]**Date**: [Incident date]**Severity**: [SEV-1 / SEV-2 / SEV-3]**Author**: [Postmortem author]**Status**: [Draft / In Review / Final]
---
## Summary
[2-3 sentence summary: what happened, how long it lasted, who was affected, and how it was resolved. Written for a reader who was not involved in the incident.]
## Impact
| Metric | Value ||--------|-------|| **Duration** | [Total incident duration] || **Time to detect** | [TTD] || **Time to mitigate** | [TTM] || **Time to resolve** | [TTR] || **Users affected** | [Count or percentage] || **Revenue impact** | [If measurable, or "Not quantified"] || **SLA impact** | [SLA budget consumed, if applicable] |## Timeline
| Time (UTC) | Event | Source ||------------|-------|--------|| [HH:MM] | [Event description] | [Source] || ... | ... | ... |## Root Cause
[Root cause statement from the 5 Whys analysis]
### 5 Whys Analysis
1. **Why**: [Direct cause] — Evidence: [data]2. **Why**: [Deeper cause] — Evidence: [data]3. **Why**: [Deeper cause] — Evidence: [data]4. **Why**: [Systemic cause] — Evidence: [data]5. **Why**: [Root cause] — Evidence: [data]
## Contributing Factors
| Factor | Category | Contribution | Recurring? ||--------|----------|--------------|------------|| [Factor 1] | [Category] | [How it contributed] | [Yes/No — link to prior postmortem if yes] || [Factor 2] | ... | ... | ... |## What Went Well
- [Things that worked during the incident response — fast detection, effective communication, successful mitigation, etc.]
## Action Items
| ID | Description | Addresses | Priority | Owner | Deadline | Verification ||----|-------------|-----------|----------|-------|----------|--------------|| AI-001 | [Specific action] | [Factor/root cause] | P1 | [Owner] | [Date] | [How to verify] || AI-002 | ... | ... | ... | ... | ... | ... |## Lessons Learned
- [Key insight 1 — what the team now knows that it didn't before]- [Key insight 2 — what process or assumption was invalidated]
## References
- [Link to incident ticket]- [Link to incident chat channel]- [Link to monitoring dashboard during incident]- [Links to related prior postmortems]
```

## Guardrails

- NEVER assign blame to individuals. Reframe as systemic failure: "The system allowed [ action ] to reach production because [ missing safeguard ] ." This is non-negotiable.
- NEVER fabricate timeline events. Every entry must be sourced from monitoring data, chat logs, deployment records, or user testimony. Mark unknown times as approximate.
- NEVER manufacture root causes. If evidence is insufficient, state "Root cause undetermined — additional data needed" and list what data is required.
- Source-label every finding as `[From monitoring]`, `[From chat logs]`, `[From deployment records]`, `[From user report]`, or `[AI analysis — verify]`.

> **Tip:** Ask for DOCX output via companyFILES to get a formatted Word document ready for distribution.
