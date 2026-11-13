---
name: en-sprint-planning
description: Plan sprints by scoping work, estimating capacity, setting goals, and mapping dependencies. Use when kicking off a new sprint, rebalancing mid-sprint, or reviewing capacity for upcoming work. Trigger with "plan next sprint", "sprint planning for", "what fits in this sprint".
---

# Sprint Planning Skill

Plan fixed-length iteration cycles — scope work to capacity, set outcome-oriented sprint goals, map dependencies, and distinguish commitments from stretch items. Team metrics and backlog data come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Linear, GitHub) | Backlog items, story estimates, historical velocity, sprint status, ownership |
| **companyRAG collections** | Roadmap, OKRs, technical specs, team agreements, retrospective notes |
| **File upload** | Capacity spreadsheets, velocity history, exported backlog lists |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Capacity Estimation

### Step 1: Calculate Raw Capacity

Raw capacity is the theoretical maximum before adjustments.

```
RAW CAPACITY = Team members × Sprint length (days) × Hours per day
```

Use the team's standard working hours — do NOT assume 8 hours/day of productive engineering time. Most teams operate at 5–6 productive hours/day after meetings, context switching, and overhead.

### Step 2: Apply Availability Adjustments

Reduce raw capacity for known absences:

| Adjustment | How to Apply |
| --- | --- |
| **PTO / holidays** | Subtract full days per person |
| **On-call rotation** | Reduce that person's capacity by 30–50% (based on historical interrupt rate) |
| **Recurring meetings** | Subtract total meeting hours across the sprint per person |
| **Onboarding / ramp-up** | New team members at 25–50% capacity for first 2–4 sprints |
| **Support rotation** | Subtract the team's historical average for support work |

```
ADJUSTED CAPACITY = RAW CAPACITY − (PTO hours + on-call reduction + meetings + support)
```

### Step 3: Apply Focus Factor

The focus factor accounts for unplanned work, bug fixes, code review, and other overhead not captured above. Derive it from the team's own history:

```
FOCUS FACTOR = (Actual story points completed) / (Adjusted capacity in hours) — averaged over last 3–5 sprints
```

If historical data is unavailable, start with 0.7 (70%) and calibrate after 2–3 sprints. Never prescribe a universal focus factor — it varies by team maturity, codebase health, and interrupt patterns.

```
EFFECTIVE CAPACITY = ADJUSTED CAPACITY × FOCUS FACTOR
```

### Step 4: Express as Story Points or Hours

Convert effective capacity into the team's estimation unit. If the team uses story points, map via historical velocity:

```
SPRINT CAPACITY (points) = Average velocity over last 3–5 sprints, adjusted for capacity differences
```

If this sprint has 80% of normal capacity, plan for roughly 80% of average velocity. Velocity is an empirical measure, not a target — do not inflate or "stretch" it.

## Sprint Goal Definition

A sprint goal is an outcome statement, not a list of tickets. It answers: "If we complete this sprint successfully, what will be true that isn't true today?"

### Goal Quality Checklist

| Criterion | Pass | Fail |
| --- | --- | --- |
| **Outcome-oriented** | "Users can complete checkout without page refresh" | "Finish tickets ENG-123, ENG-124, ENG-125" |
| **Singular focus** | One coherent theme or objective | Multiple unrelated objectives bundled |
| **Testable** | A demo or metric can verify achievement | No way to know if the goal is met |
| **Achievable** | Fits within sprint capacity after estimation | Requires optimistic assumptions about capacity |
| **Stakeholder-meaningful** | Non-engineers can understand the value delivered | Expressed in purely technical jargon |

### Goal Setting Process

1. Review product priorities: What is the highest-impact work from the backlog? Reference the roadmap and current OKRs.
2. Draft 1–2 candidate goals: Frame as outcomes, not task lists.
3. Scope-check: Can the team realistically achieve this goal within effective capacity? If not, narrow scope — reduce the goal, don't reduce quality.
4. Team alignment: The team must understand and commit to the goal. A goal imposed without team buy-in produces compliance, not commitment.

## Dependency Mapping

### Dependency Categories

| Type | Definition | Mitigation |
| --- | --- | --- |
| **Internal team** | Work that depends on another story within the same sprint | Sequence stories; pair-assign if possible |
| **Cross-team** | Work blocked by another team's deliverable | Confirm delivery date before sprint commitment; add buffer |
| **External** | Third-party API, vendor deliverable, customer approval | Do not commit dependent work without confirmed timeline |
| **Technical** | Shared infrastructure, database migration, deployment pipeline | Identify and schedule early in the sprint |

### Dependency Resolution Protocol

For each dependency identified:

1. Classify by type (above)
2. Confirm status: Is the dependency already resolved, in progress, or not started?
3. Assess risk: What happens if the dependency is late? Is there alternative work the team can pull?
4. Assign owner: Someone on the team owns tracking each external dependency
5. Set check-in: When will you verify the dependency is on track? (Not the last day of the sprint)

**Rule**: If a story has an unresolved external dependency with no confirmed delivery date, it goes to stretch — never commitment.

## Commitment vs. Stretch

Split the sprint backlog into two explicit categories:

### Commitment

Work the team is confident they will complete within the sprint. Confidence threshold: the team believes there is at least an 80–90% chance of completion given effective capacity.

- Must fit within effective capacity
- Dependencies must be resolved or have confirmed delivery dates
- Acceptance criteria must be clear — if the team cannot describe "done," it is not ready for commitment

### Stretch

Work the team will pull if commitment items finish early. Stretch items:

- Are fully groomed and ready to start (no blocking questions)
- Have no unresolved dependencies
- Are independent — pulling a stretch item does not destabilise committed work
- Are ordered by priority so the team knows what to pull first

**Capacity allocation guideline**: Commit to 80–90% of effective capacity; fill the remaining 10–20% with ordered stretch items. The exact ratio depends on the team's historical accuracy — teams that consistently under-commit can tighten the ratio; teams that over-commit should loosen it.

## Sprint Planning Workflow

### Before Planning (Preparation)

1. Groom the backlog: Top candidates must have clear descriptions, acceptance criteria, and estimates. Ungroomed items cannot enter the sprint.
2. Calculate capacity: Run Steps 1–4 from Capacity Estimation with current sprint data.
3. Surface dependencies: Identify cross-team and external dependencies for candidate stories.
4. Review prior sprint: What carried over? What was learned? Carry-over items get priority consideration but are not automatically included — reassess priority.

### During Planning

1. Present the sprint goal (from Goal Definition above)
2. Walk the candidate stories: For each, confirm scope, estimate, dependencies, and acceptance criteria
3. Load commitment: Add stories to commitment until effective capacity is reached
4. Sequence for dependencies: Order committed stories so that dependent work starts after its prerequisites
5. Add stretch: Fill the stretch backlog in priority order
6. Team confirmation: Each team member confirms they understand their work and believe the commitment is achievable

### Sprint Plan Output

```
SPRINT: [Name / Number]
DATES:  [Start] — [End]
GOAL:   [Outcome statement]

CAPACITY:
  Team members:       [count]
  Raw capacity:       [hours or points]
  Adjustments:        [PTO, on-call, etc.]
  Effective capacity: [final number]
  Velocity reference: [last 3–5 sprint average]

COMMITMENT: [total points/hours] ([X]% of effective capacity)
  | # | Story | Estimate | Owner | Dependencies | Status |
  |---|-------|----------|-------|--------------|--------|
  | 1 | [title] | [est] | [name] | [deps] | Ready |

STRETCH: [total points/hours]
  | # | Story | Estimate | Pull Priority | Dependencies |
  |---|-------|----------|---------------|--------------|
  | 1 | [title] | [est] | 1 (pull first) | [deps] |

DEPENDENCIES:
  | Dependency | Type | Owner | Expected Resolution | Check-in Date |
  |------------|------|-------|---------------------|---------------|

RISKS:
  [Key risks to sprint goal achievement — from dependency analysis and capacity review]

CARRY-OVER FROM PREVIOUS SPRINT:
  [Items, reason for carry-over, updated priority assessment]
```

## Mid-Sprint Rebalancing

When sprint health deteriorates (blocked items, scope changes, unexpected absences), use this triage:

1. Assess remaining capacity: Recalculate effective capacity for the remaining sprint days
2. Re-evaluate commitment: Which committed items are at risk? Which are on track?
3. Protect the sprint goal: If the goal is achievable with a subset of committed work, shed non-goal items to stretch
4. Escalate blockers: Unresolved dependencies that threaten the sprint goal require immediate escalation — do not wait for the next stand-up
5. Communicate: If the commitment changes, inform stakeholders — use the write-stakeholder-update skill

## Guardrails

- NEVER generate velocity data, estimates, or capacity numbers. All team metrics must come from the user, project tracker, or a companyRAG collection.
- NEVER prescribe universal focus factors, velocity targets, or capacity ratios. Teach the calculation; the team derives their own numbers.
- NEVER populate sprint plans with fabricated stories or estimates. Generate blank templates when no data is provided.
- Source-label every element as `[From user/tracker data]`, `[From sprint planning framework]`, or `[AI suggestion — verify with team]`.

> **Tip:** Ask for Markdown, DOCX, or XLSX output via companyFILES to get a formatted sprint plan ready to share.
