---
name: en-incident-response
description: Structure IT incidents with severity classification, escalation paths, communication templates, and post-mortem guides. Use when an incident occurs, coordinating response across teams, or running a post-incident review. Trigger with "incident response", "we have a P1", "production is down".
---

# Incident Response Skill

Classify, manage, and resolve IT incidents with severity frameworks, escalation matrices, communication templates, timeline tracking, and blameless post-mortem facilitation. Organisation-specific data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Incident / on-call tools via MCP** (e.g. PagerDuty, Opsgenie) | Alert data, on-call rosters, escalation chains, incident status |
| **ITSM via MCP** (e.g. ServiceNow) | Ticket history, change records, SLA terms, asset information |
| **Monitoring via MCP** (e.g. Datadog) | Metrics, logs, alert history, affected services |
| **companyRAG / file upload** | Runbooks, organisation-specific SLA targets, on-call rosters, prior post-mortems |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Severity Classification Framework

Classify every incident against these four levels before any other action. Severity determines response speed, communication cadence, and escalation path.

### Severity Definitions

| Severity | Name | Impact Criteria | Example Scenarios |
| --- | --- | --- | --- |
| **P1** | Critical | Complete service outage affecting all users OR confirmed data breach OR safety risk. Revenue-impacting. SLA clock running. | Production database down, authentication service unavailable, ransomware detected, payment processing failure |
| **P2** | High | Major feature degraded for a significant user segment. Workaround may exist but is not sustainable. Approaching SLA breach. | Search functionality broken, API response times >10x normal, SSO failing for one identity provider, email delivery delayed >2h |
| **P3** | Moderate | Non-critical feature impaired. Limited user impact. Workaround available and viable. | Report generation slow, single integration failing, UI rendering issue on one browser, non-production environment down |
| **P4** | Low | Cosmetic issue, minor bug, or informational alert. No user workflow blocked. | Typo in error message, log noise from deprecated endpoint, minor UI alignment issue, scheduled maintenance follow-up |

### Classification Decision Tree

Apply these questions in order:

1. Is the service completely unavailable to all users? → P1
2. Is there a confirmed or suspected security breach? → P1
3. Is revenue directly impacted right now? → P1
4. Is a major feature degraded for >25% of users? → P2
5. Is an SLA breach imminent (within next reporting period)? → P2
6. Is a non-critical feature impaired with a viable workaround? → P3
7. Is the impact cosmetic or informational only? → P4

When uncertain between two levels, classify at the HIGHER severity. Downgrading is always easier than catching up after under-classifying.

### Severity Escalation and De-escalation

Severity is not static. Re-evaluate at every status update:

- Escalate when: impact spreads to more users, workaround fails, SLA window is narrowing, root cause reveals larger scope
- De-escalate when: workaround is confirmed effective for all affected users, impact is contained and shrinking, root cause is isolated and fix is in progress

Document every severity change with timestamp, reason, and who authorized it.

---

## Incident Roles

Define these roles at incident declaration. One person per role (though Incident Commander and Communications Lead can be the same person for P3/P4).

| Role | Responsibility | Required For |
| --- | --- | --- |
| **Incident Commander (IC)** | Owns the incident lifecycle. Makes decisions on severity, escalation, resource allocation. Single point of authority. | P1, P2 (recommended for P3) |
| **Technical Lead** | Drives diagnosis and resolution. Coordinates engineering work. Reports progress to IC. | P1, P2, P3 |
| **Communications Lead** | Owns all stakeholder communication. Sends updates on cadence. Manages status page. | P1, P2 |
| **Scribe** | Maintains the incident timeline. Logs every action, decision, and finding with timestamps. | P1, P2 (recommended for P3) |

The IC does NOT need to be the most senior engineer. The IC needs to be someone who can coordinate, delegate, and make decisions under pressure. Technical depth comes from the Technical Lead.

---

## Escalation Matrix

### Response Time Targets

| Severity | Acknowledge | First Update | Resolution Target | Update Cadence |
| --- | --- | --- | --- | --- |
| **P1** | 15 min | 30 min | 4h | Every 30 min |
| **P2** | 30 min | 1h | 8h | Every 1h |
| **P3** | 2h | 4h | 3 business days | Every 4h during business hours |
| **P4** | 1 business day | 2 business days | Next sprint/cycle | On resolution |

These are starting defaults. Replace them with your organization's SLA-driven targets from the companyRAG collection or system prompt.

### Escalation Triggers

Escalate to the next management tier when ANY of these conditions is met:

| Trigger | Action |
| --- | --- |
| Resolution target at 50% elapsed with no root cause identified | Escalate to engineering management |
| Resolution target at 75% elapsed with no fix deployed | Escalate to VP/Director level |
| Customer-facing SLA breach imminent | Escalate to account management + engineering leadership |
| Incident involves data breach or regulatory exposure | Escalate to CISO/DPO + Legal immediately regardless of time elapsed |
| IC requests additional resources beyond their authority | Escalate to IC's management chain |
| Incident scope expands across multiple services/teams | Escalate to platform/infrastructure leadership |

### On-Call Escalation Path

```
Primary on-call (team level)
  → Secondary on-call (team level)
    → Engineering Manager (team)
      → Director of Engineering / VP
        → CTO (P1 only, if unresolved after 2h)
```

Populate with your organization's actual roster. The structure above is the default chain. Parallel paths for Security (→ CISO) and Customer Impact (→ VP Customer Success) activate based on incident type.

---

## Communication Templates

### P1/P2: Initial Declaration

```
INCIDENT DECLARED — [P1/P2]

Service affected: [service name]
Impact: [who is affected, what they cannot do]
Detected: [timestamp, how detected — alert / customer report / internal]
Current status: Investigating
Incident Commander: [name]
War room: [link to call/channel]

Next update: [timestamp, per cadence]
```

### P1/P2: Status Update

```
INCIDENT UPDATE — [P1/P2] — [Investigating / Identified / Mitigated]

Service: [service name]
Duration: [time since detection]
Current impact: [updated impact scope]
What we know: [factual findings only — no speculation]
What we're doing: [current action and who owns it]
ETA to next milestone: [if known, otherwise "investigating"]

Next update: [timestamp]
```

### P1/P2: Resolution

```
INCIDENT RESOLVED — [P1/P2]

Service: [service name]
Total duration: [detection to resolution]
Root cause: [one-line summary]
Resolution: [what fixed it]
User action required: [if any — e.g., "clear cache", "re-authenticate"]
Data impact: [confirmed: none / under investigation / details]

Post-mortem scheduled: [date/time]
```

### P3/P4: Lightweight Notification

```
INCIDENT — [P3/P4]

Service: [service name]
Impact: [brief description]
Workaround: [if available]
Status: [Investigating / Fix in progress / Resolved]
ETA: [if known]
Owner: [name/team]
```

### External Customer Communication (P1/P2)

```
Subject: Service disruption — [service name]

We are aware of an issue affecting [plain-language description of impact].

Our engineering team is actively working to resolve this. We will provide updates every [cadence].

Current status: [Investigating / Identified / Fix in progress]
Estimated resolution: [if known, otherwise "We are working to resolve this as quickly as possible."]

We apologize for the inconvenience and will keep you informed.

[Support contact or status page link]
```

Keep external communication factual and free of technical jargon. Never speculate on root cause in external comms until the post-mortem is complete.

---

## Incident Timeline Tracking

Maintain a running timeline from the moment an incident is declared. The scribe owns this document. Every entry follows this format:

```
[YYYY-MM-DD HH:MM UTC] [ROLE] — [ACTION/FINDING/DECISION]
```

### Required Timeline Entries

Capture at minimum:

| Event | When to Log |
| --- | --- |
| Incident detected (alert fired, customer reported, etc.) | First entry |
| Incident declared and severity assigned | At declaration |
| Roles assigned (IC, Tech Lead, Comms, Scribe) | At declaration |
| Each status update sent | At send time |
| Root cause hypothesis formed | When identified |
| Root cause confirmed | When confirmed |
| Mitigation action taken (failover, rollback, hotfix) | When executed |
| Severity change (up or down) | When changed |
| Escalation triggered | When escalated |
| Service restored | When confirmed |
| Incident closed | When all follow-up items are logged |

### Timeline Template

```
## Incident: [ID] — [Title]
Severity: [P1/P2/P3/P4]
Service: [name]
Commander: [name]

### Timeline

[2025-01-15 14:02 UTC] ALERT — PagerDuty alert: API response time >5000ms for 3 min
[2025-01-15 14:05 UTC] IC — Incident declared P2. War room opened. Roles assigned.
[2025-01-15 14:08 UTC] TECH LEAD — Confirmed: database connection pool exhausted on primary replica.
[2025-01-15 14:12 UTC] IC — Severity escalated to P1: impact broader than initially assessed, all API calls failing.
[2025-01-15 14:15 UTC] COMMS — First status update sent (internal + status page).
[2025-01-15 14:22 UTC] TECH LEAD — Failover to secondary replica initiated.
[2025-01-15 14:28 UTC] TECH LEAD — Secondary replica serving traffic. API response times normalizing.
[2025-01-15 14:30 UTC] IC — Service restored. Monitoring for stability.
[2025-01-15 14:45 UTC] COMMS — Resolution notice sent. Post-mortem scheduled for 2025-01-16 10:00 UTC.
[2025-01-15 15:00 UTC] IC — Incident closed. Duration: 58 min (detection to resolution).
```

---

## Blameless Post-Mortem

Run a post-mortem for every P1 and P2 incident. P3 incidents get a post-mortem if they recur or if the team requests one. The goal is systemic improvement, not individual accountability.

### Post-Mortem Principles

- Blameless: Focus on systems, processes, and information flow — not individuals. People made the best decisions they could with the information available at the time.
- Thorough: Map the full causal chain, not just the proximate trigger.
- Action-oriented: Every finding produces a concrete, assigned, time-bound action item — or it is explicitly noted as accepted risk.
- Time-boxed: 60–90 minutes for P1, 30–45 minutes for P2. If you need more time, the document needs more pre-work.

### Post-Mortem Document Template

```
# Post-Mortem: [Incident ID] — [Title]

**Date**: [post-mortem meeting date]
**Incident date**: [date]
**Duration**: [detection to resolution]
**Severity**: [P1/P2/P3]
**Incident Commander**: [name]
**Post-Mortem Facilitator**: [name — ideally NOT the IC]
**Attendees**: [names]

## Summary

[2-3 sentences: what happened, who was affected, how it was resolved.]

## Impact

- **Users affected**: [number or percentage]
- **Duration of user-facing impact**: [time]
- **Revenue impact**: [if measurable, otherwise "not quantified"]
- **SLA impact**: [any SLA breaches, credit obligations]
- **Data impact**: [any data loss, corruption, or unauthorized access — confirmed or ruled out]

## Root Cause

[Detailed technical explanation of the root cause. Go beyond the proximate trigger to the systemic factors. Use the "5 Whys" or causal chain analysis.]

Why 1: [immediate cause]
Why 2: [why did that happen?]
Why 3: [why did that happen?]
Why 4: [why did that happen?]
Why 5: [systemic root cause]

## Timeline

[Copy from incident timeline, annotated with hindsight notes where the team would act differently.]

## What Went Well

- [Things that worked: fast detection, effective communication, good teamwork, runbook was accurate]

## What Went Poorly

- [Things that didn't work: slow detection, missing runbook, unclear escalation, monitoring gap]

## Where We Got Lucky

- [Things that could have been worse: it happened during business hours, the right person was on-call, the secondary replica was healthy]

## Action Items

| ID | Action | Owner | Priority | Due Date | Status |
|----|--------|-------|----------|----------|--------|
| 1 | [specific, measurable action] | [name] | [P1/P2/P3] | [date] | Open |
| 2 | [specific, measurable action] | [name] | [P1/P2/P3] | [date] | Open |

Action items MUST be:
- Specific (not "improve monitoring" — instead "add alert for connection pool utilization >80%")
- Assigned to a named owner
- Time-bound with a due date
- Tracked to completion in the team's issue tracker
```

### Post-Mortem Facilitation Guide

1. Pre-meeting (facilitator): Distribute the incident timeline to all attendees 24h before. Ask each participant to review and add their perspective.
2. Opening (5 min): State the blameless principle. Remind everyone: we are here to improve the system, not assign blame.
3. Timeline walk-through (15-20 min): Walk through events chronologically. Participants add context. Facilitator probes for decision points and information gaps.
4. Root cause analysis (15-20 min): Apply 5 Whys or causal chain. Push past the proximate trigger to systemic factors.
5. What went well / poorly / got lucky (10-15 min): Structured round-robin or open discussion. The "got lucky" category surfaces hidden risks.
6. Action items (10-15 min): For each "went poorly" item and "got lucky" item, define a concrete action or explicitly accept the risk.
7. Close (5 min): Review action items, confirm owners and due dates, set follow-up review date.

---

## Incident Metrics

Track these metrics over time to measure incident management maturity:

| Metric | Definition | Target Direction |
| --- | --- | --- |
| **MTTD** (Mean Time to Detect) | Time from incident onset to detection | Decrease |
| **MTTA** (Mean Time to Acknowledge) | Time from detection to IC assignment | Decrease |
| **MTTR** (Mean Time to Resolve) | Time from detection to service restoration | Decrease |
| **MTTF** (Mean Time Between Failures) | Time between incidents for a given service | Increase |
| **Escalation rate** | Percentage of incidents requiring management escalation | Decrease |
| **Post-mortem completion rate** | Percentage of P1/P2 incidents with completed post-mortems | 100% |
| **Action item closure rate** | Percentage of post-mortem actions closed on time | Increase |
| **Recurrence rate** | Percentage of incidents with the same root cause as a prior incident | Decrease (0% = no recurring root causes) |

---

## Guardrails

- Never diagnose root cause from description alone. Respond with diagnostic steps and questions, not speculative root causes. Distinguish "confirmed" from "suspected" findings.
- Never fabricate SLA terms or on-call rosters. Use the defaults in this skill only when the organisation has not provided their own.
- During active incidents, prioritise actionable guidance over comprehensive analysis. A P1 needs next steps, not a dissertation.
- Source-label all output: `[Framework template]`, `[From incident data]`, or `[AI-generated suggestion — verify]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get the timeline or post-mortem as a formatted, ready-to-share document.
