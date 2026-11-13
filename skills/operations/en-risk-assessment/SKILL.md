---
name: en-risk-assessment
description: Operational risk assessment with a Severity x Likelihood matrix, mitigation planning, and risk register maintenance. Use when evaluating risks for a project, conducting periodic risk reviews, or building a risk register. Trigger with "assess risk for", "risk analysis", "what could go wrong with".
---

# Risk Assessment Skill

Identify, score, and mitigate operational risks. The skill produces risk registers, risk matrices, mitigation plans, and periodic review reports. The data to assess comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project / issue tracker via MCP** (e.g. Jira, Asana, Monday) | Project scope, dependencies, open issues, historical incidents |
| **Incident / monitoring tools via MCP** (e.g. PagerDuty, Sentry) | Past incidents, near-misses, post-mortems for historical review |
| **companyRAG collections / file upload** | Process descriptions, contracts, pre-mortem notes, existing risk registers |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Risk Identification

### Identification Techniques

Use multiple approaches to build a comprehensive risk inventory — no single technique captures all risks:

| Technique | How It Works | Best For |
| --- | --- | --- |
| **Brainstorming with structure** | Walk through each process step, decision point, dependency, and external factor asking "what could go wrong here?" | Known processes with identifiable failure modes |
| **Pre-mortem** | Assume the project/initiative has failed; work backwards to identify what caused the failure | Projects and initiatives — surfaces risks people are reluctant to raise |
| **Historical review** | Examine past incidents, near-misses, and post-mortems for recurring patterns | Operational processes with incident history |
| **Dependency mapping** | Trace all dependencies (people, systems, vendors, data, approvals) and assess each for failure potential | Complex processes with many external dependencies |
| **Assumption testing** | List all assumptions underlying the plan; each assumption that could prove false is a risk | Strategic initiatives and business cases |
| **PESTLE scan** | Check Political, Economic, Social, Technological, Legal, Environmental factors | External risk landscape assessment |

### Risk Description Standard

Each risk must be described as a specific event with a cause and consequence — not a vague concern:

**Pattern**: "Due to [cause], [event] may occur, resulting in [consequence]."

| Quality | Bad Example | Good Example |
| --- | --- | --- |
| **Specific** | "Technology risk" | "Due to the vendor's single-region hosting, a regional cloud outage may occur, resulting in 4-8 hours of service unavailability" |
| **Causal** | "We might lose data" | "Due to the lack of automated backup verification, an undetected backup failure may occur, resulting in data loss up to 24 hours" |
| **Consequential** | "Supply chain issues" | "Due to single-source dependency for component X, a supplier production halt may occur, resulting in 6-week delivery delay for customer orders" |

## Risk Scoring

### Severity Scale

Define severity in terms meaningful to the organisation:

| Level | Label | Definition Template |
| --- | --- | --- |
| 5 | **Critical** | Threatens organisational viability, major regulatory sanction, or irreversible damage |
| 4 | **Major** | Significant financial loss, reputational damage affecting customer relationships, or extended operational disruption |
| 3 | **Moderate** | Material impact requiring management attention, temporary operational degradation, or contained financial loss |
| 2 | **Minor** | Limited impact manageable within normal operations, minor delays, or small financial variance |
| 1 | **Negligible** | Minimal impact, easily absorbed, no lasting effect |

These definitions are templates — the organisation should calibrate with specific thresholds (e.g., "significant financial loss" should be defined in currency terms relevant to the organisation's scale). Prompt the user to define their thresholds if not established.

### Likelihood Scale

| Level | Label | Definition |
| --- | --- | --- |
| 5 | **Almost Certain** | Expected to occur within the assessment period; has happened repeatedly before |
| 4 | **Likely** | Will probably occur; has happened before under similar conditions |
| 3 | **Possible** | Could occur; conditions exist but additional factors needed |
| 2 | **Unlikely** | Not expected but conceivable; would require unusual circumstances |
| 1 | **Rare** | Highly improbable; would require exceptional circumstances |

### Risk Matrix

Severity × Likelihood produces a risk score:

|  | Rare (1) | Unlikely (2) | Possible (3) | Likely (4) | Almost Certain (5) |
| --- | --- | --- | --- | --- | --- |
| **Critical (5)** | 5 — High | 10 — High | 15 — Critical | 20 — Critical | 25 — Critical |
| **Major (4)** | 4 — Medium | 8 — High | 12 — High | 16 — Critical | 20 — Critical |
| **Moderate (3)** | 3 — Low | 6 — Medium | 9 — High | 12 — High | 15 — Critical |
| **Minor (2)** | 2 — Low | 4 — Medium | 6 — Medium | 8 — High | 10 — High |
| **Negligible (1)** | 1 — Low | 2 — Low | 3 — Low | 4 — Medium | 5 — Medium |

### Risk Rating Thresholds

| Rating | Score Range | Required Action |
| --- | --- | --- |
| **Critical** | 15–25 | Immediate action required; escalate to senior leadership; cannot proceed without mitigation plan |
| **High** | 8–14 | Mitigation plan required; assign owner; review at least monthly |
| **Medium** | 4–7 | Monitor actively; mitigation desirable; review quarterly |
| **Low** | 1–3 | Accept and monitor; no active mitigation required unless low-effort |

Thresholds and required actions should be calibrated to the organisation's risk appetite. The scores and ranges above are a starting framework — adjust based on the organisation's risk tolerance.

## Risk Register

### Register Entry Format

For each identified risk:

```
RISK REGISTER ENTRY:
  Risk ID:          [unique identifier]
  Description:      [cause-event-consequence format]
  Category:         [Strategic / Operational / Financial / Compliance / Technology / People / External]
  Severity:         [1-5 with label]
  Likelihood:       [1-5 with label]
  Risk score:       [severity × likelihood]
  Rating:           [Critical / High / Medium / Low]
  Existing controls: [what is already in place to address this risk]
  Residual risk:    [risk level after existing controls — reassess severity and likelihood]
  Mitigation plan:  [additional actions to reduce risk — see mitigation planning]
  Owner:            [person accountable for managing this risk]
  Review date:      [next scheduled review]
  Status:           [Open / Mitigating / Accepted / Closed]
  Trend:            [↑ Increasing / → Stable / ↓ Decreasing — compared to last review]
```

### Residual Risk Assessment

After documenting existing controls, reassess the risk:

1. Identify controls already in place (preventive, detective, or corrective)
2. Assess control effectiveness — are they consistently applied? Are they tested?
3. Re-score severity and likelihood considering the controls
4. The residual risk score determines the required mitigation effort

If residual risk is above the organisation's tolerance after existing controls, additional mitigation is required.

## Mitigation Planning

### Mitigation Strategy Selection

For each risk requiring mitigation, select one or more strategies:

| Strategy | Action | When to Use |
| --- | --- | --- |
| **Avoid** | Eliminate the risk by removing the cause or changing the plan | When the risk is unacceptable and an alternative path exists |
| **Reduce** | Lower severity or likelihood through controls or design changes | When the risk can be brought within tolerance with reasonable effort |
| **Transfer** | Shift the risk to another party (insurance, outsourcing, contractual terms) | When another party can manage the risk more effectively |
| **Accept** | Acknowledge the risk and monitor without active mitigation | When the risk is within tolerance, or mitigation cost exceeds the expected impact |
| **Contingency** | Prepare a response plan to execute if the risk materialises | When the risk cannot be prevented but the response can be pre-planned |

### Mitigation Plan Format

For each mitigation action:

```
MITIGATION ACTION:
  Risk ID:         [linked to register entry]
  Strategy:        [Avoid / Reduce / Transfer / Accept / Contingency]
  Action:          [specific, concrete step — not "reduce the risk" but "implement automated backup verification running daily with alert on failure"]
  Owner:           [person responsible for implementing the action]
  Deadline:        [when the action must be complete]
  Cost/effort:     [resources required to implement]
  Expected effect: [how this changes the severity or likelihood score]
  Verification:    [how completion and effectiveness will be confirmed]
  Status:          [Not started / In progress / Complete / Verified]
```

## Risk Review Process

### Periodic Review Cadence

| Review Type | Frequency | Scope | Participants |
| --- | --- | --- | --- |
| **Risk register review** | Monthly or as triggered by events | All open risks — check status, update scores, flag new risks | Risk owners + risk coordinator |
| **Deep-dive review** | Quarterly | Critical and high-rated risks — detailed mitigation progress, control effectiveness | Risk owners + senior leadership |
| **Emerging risk scan** | Quarterly | New risks from environmental changes, strategy shifts, incidents | Cross-functional leadership |
| **Annual risk assessment** | Yearly | Full re-identification and re-scoring of all risks | Full risk governance team |

### Review Output Format

```
RISK REVIEW SUMMARY — [Date]

Register snapshot:
  Total risks:     [count]
  Critical:        [count] — [list risk IDs]
  High:            [count]
  Medium:          [count]
  Low:             [count]

Changes since last review:
  New risks added:       [count and brief descriptions]
  Risks escalated:       [risk IDs that moved to a higher rating]
  Risks de-escalated:    [risk IDs that moved to a lower rating]
  Risks closed:          [risk IDs and closure rationale]

Overdue mitigations:     [actions past their deadline]
Upcoming deadlines:      [actions due within next review period]
Emerging concerns:       [new or developing risk themes not yet in register]
```

## Output Template

Structure the full risk assessment as follows:

```
# Risk Assessment — [Subject] — [Date]

## Executive Summary
- Total risks identified: [count]
- Risk profile: [Critical: x, High: x, Medium: x, Low: x]
- Top risk: [highest-rated risk with brief description]
- Key mitigation priorities: [top 3 actions]

## Risk Register
[Full register entries]

## Risk Matrix Visualisation
[5×5 matrix with risk IDs plotted]

## Mitigation Plan
[Prioritised actions with owners and deadlines]

## Review Schedule
[Next review dates and scope]

## Methodology Notes
- Scoring scales calibrated to: [organisation's definitions or skill defaults]
- Assumptions: [any assumptions made during assessment]
- Limitations: [data gaps, areas not assessed, confidence caveats]
```

## Guardrails

- Never generate specific risks from training data as if they apply to the user's situation. All risks must come from user context, process description, or domain knowledge.
- Never fabricate severity or likelihood scores. Guide the user through the scoring methodology rather than assigning scores unilaterally.
- Never claim "typical risk profile" or "common industry risks." Risk profiles are organisation-specific.
- Label generated content: `[From risk data]`, `[Framework methodology]`, `[AI-identified risk — verify with domain expert]`.

> **Tip:** Ask for XLSX, DOCX, or Markdown output via companyFILES to get a formatted risk register ready for distribution.
