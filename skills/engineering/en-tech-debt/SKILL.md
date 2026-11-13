---
name: en-tech-debt
description: Technical debt inventory with severity scoring, business impact assessment, and remediation prioritisation. Use when auditing tech debt, making a case for refactoring, or planning tech debt sprints. Trigger with "assess tech debt in", "tech debt inventory", "should we refactor".
---

# Tech Debt Skill

Turn vague "we should refactor this" conversations into data-driven investment decisions. This skill walks you through identification, classification, severity scoring, business-impact assessment, and remediation prioritisation — all grounded in the context you provide.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **companyRAG collections** | Architecture docs, past assessments, quality reports |
| **Project tracker via MCP** (e.g. Jira, Linear) | Remediation ticket creation and tracking; link debt to affected features |
| **Git provider via MCP** (e.g. GitHub, GitLab) | Code history, change frequency, contributor patterns |
| **Code quality via MCP** (e.g. SonarQube) | Coverage, complexity metrics, reported code smells |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Assessment Workflow

### Step 1: Identify Debt

Technical debt is not just "code I don't like." It is a design or implementation choice that creates ongoing cost — slower development, higher defect rates, operational burden, or scaling limitations.

**Identification sources:**

| Source | What It Reveals |
| --- | --- |
| **Developer interviews** | Pain points, areas that are feared or avoided, "here be dragons" zones |
| **Incident history** | Recurring failures, systems that break under load, areas with frequent rollbacks |
| **Change frequency + defect correlation** | Files changed often AND producing bugs indicate structural problems |
| **Code review friction** | Areas where reviews consistently flag issues, take longer, or produce debates |
| **Onboarding difficulty** | Systems that new team members cannot understand within a reasonable ramp-up period |
| **Build/test pipeline** | Slow builds, flaky tests, tests that are routinely skipped or ignored |
| **Dependency age** | Libraries multiple major versions behind, deprecated APIs, unsupported runtimes |

**Identification questions to ask the team:**

1. "Which part of the codebase do you dread working in? Why?"
2. "What takes longer than it should? What would be faster if the code were different?"
3. "Where do bugs keep coming from? Is there a pattern?"
4. "What breaks when we try to scale?"
5. "What cannot be changed without risk of breaking something else?"

### Step 2: Classify Debt Type

Not all debt is the same. Classification determines the remediation approach.

**Tech Debt Taxonomy:**

| Debt Type | Definition | Examples | Typical Remediation |
| --- | --- | --- | --- |
| **Architecture debt** | System structure that does not match current or near-future requirements | Monolith that needs independent scaling; synchronous calls that need async; missing service boundaries | Incremental restructuring, strangler fig pattern, domain boundary extraction |
| **Code debt** | Implementation that is correct but costly to maintain or extend | Long functions, deep nesting, duplicated logic, unclear naming, missing abstractions | Refactoring during feature work, dedicated refactoring sprints |
| **Test debt** | Insufficient, unreliable, or poorly structured tests | Low coverage on critical paths, flaky tests, tests coupled to implementation details, missing integration tests | Test improvement campaigns, coverage ratcheting, flaky test elimination |
| **Dependency debt** | Outdated or problematic external dependencies | Libraries multiple major versions behind, deprecated APIs, unmaintained packages, known vulnerabilities | Dependency update sprints, migration to supported alternatives |
| **Infrastructure debt** | Deployment, build, or operational systems that create friction | Slow CI pipelines, manual deployment steps, missing monitoring, inadequate alerting | DevOps investment, pipeline modernisation, observability improvements |
| **Documentation debt** | Missing or outdated documentation that slows development | No architecture docs, outdated API references, tribal knowledge, missing runbooks | Documentation sprints, docs-as-code practices, ADR adoption |
| **Design debt** | Decisions made under time pressure that created known suboptimal structures | Shortcuts in data models, temporary workarounds that became permanent, leaky abstractions | Planned rework, expand-contract migrations |

### Step 3: Score Severity and Impact

Score each debt item on two dimensions: technical severity and business impact. The combination determines priority.

**Technical Severity (how bad is it technically?):**

| Score | Level | Criteria |
| --- | --- | --- |
| **4** | Critical | Actively causing production incidents, data integrity issues, or security vulnerabilities. Cannot be safely worked around. |
| **3** | High | Significantly slows feature development (2x+ effort), produces frequent bugs, or prevents scaling to known near-term requirements. |
| **2** | Medium | Causes friction and occasional bugs. Workarounds exist but add complexity. Development is slower than it should be. |
| **1** | Low | Cosmetic or minor. Noticeable to developers but does not measurably impact velocity, reliability, or scalability. |

**Business Impact (how much does it affect outcomes?):**

| Score | Level | Criteria |
| --- | --- | --- |
| **4** | Critical | Blocking revenue-generating features, causing customer-visible incidents, or creating compliance/security risk. |
| **3** | High | Slowing delivery of high-priority roadmap items. Team velocity is measurably reduced in a business-critical area. |
| **2** | Medium | Affecting development efficiency but not on the critical path. Impact is real but the team can work around it. |
| **1** | Low | Minimal business impact currently. May become relevant as the system or team grows. |

**Priority Matrix:**

|  | Business Impact 4 | Business Impact 3 | Business Impact 2 | Business Impact 1 |
| --- | --- | --- | --- | --- |
| **Severity 4** | P0 — Fix now | P0 — Fix now | P1 — Next sprint | P2 — Plan this quarter |
| **Severity 3** | P0 — Fix now | P1 — Next sprint | P2 — Plan this quarter | P3 — Backlog |
| **Severity 2** | P1 — Next sprint | P2 — Plan this quarter | P3 — Backlog | P4 — Monitor |
| **Severity 1** | P2 — Plan this quarter | P3 — Backlog | P4 — Monitor | P4 — Monitor |

### Step 4: Estimate Remediation Cost

For each debt item, estimate the cost of remediation to enable ROI-based prioritisation.

**Cost estimation framework:**

| Factor | Estimation Approach |
| --- | --- |
| **Effort** | Engineering time in person-days or story points. Break into discovery (understand the problem), implementation (fix it), and verification (prove it is fixed). |
| **Risk** | Probability that remediation introduces regressions. Higher for architectural changes, lower for isolated refactoring. |
| **Disruption** | Will remediation block other work? Require feature freezes? Need coordination across teams? |
| **Opportunity cost** | What feature work is displaced by this remediation? Is the trade-off justified? |

**Cost classification:**

| Cost Level | Definition |
| --- | --- |
| **Low** (< 1 week) | Contained refactoring, dependency update, documentation |
| **Medium** (1-4 weeks) | Cross-cutting refactoring, test infrastructure improvements, migration of one component |
| **High** (1-3 months) | Architectural restructuring, major migration, platform change |
| **Very High** (> 3 months) | System rewrite, multi-service decomposition, foundational infrastructure overhaul |

### Step 5: Prioritise and Plan

Combine severity, business impact, and remediation cost into a prioritised backlog.

**Prioritisation strategies:**

| Strategy | Best When |
| --- | --- |
| **Fix on contact** | Debt is encountered during feature work. Refactor the area you are already touching. Low overhead, steady improvement. |
| **Dedicated debt sprints** | Accumulated debt is slowing velocity across the board. Allocate a fixed percentage of capacity (commonly 15-20%) to debt remediation. |
| **Strategic investment** | Architecture debt requires focused multi-sprint effort. Treat as a project with planning, milestones, and success metrics. |
| **Containment** | Debt exists but remediation cost exceeds benefit. Draw a boundary: do not let it spread further, but do not invest in fixing it. |
| **Planned retirement** | The system will be replaced. Invest only in keeping it operational until the replacement is ready. |

**Remediation plan template per item:**

```
TECH DEBT ITEM: [ID] — [Short name]
  Type:             [Architecture / Code / Test / Dependency / Infra / Docs / Design]
  Severity:         [1-4] — [rationale]
  Business Impact:  [1-4] — [rationale]
  Priority:         [P0-P4]
  Remediation Cost: [Low / Medium / High / Very High]
  Strategy:         [Fix on contact / Dedicated sprint / Strategic investment / Containment / Planned retirement]
  Description:      [What the debt is and why it matters]
  Root Cause:       [How this debt was created — time pressure, changed requirements, knowledge gap]
  Remediation Plan: [High-level approach — not a full design doc]
  Success Metric:   [How do we know it is fixed? — reduced incident rate, improved velocity, coverage target]
  Owner:            [Team or individual]
  Target Date:      [When remediation should be complete]
```

## Tech Debt Report Template

```
# Technical Debt Assessment: [System/Area Name]

## Executive Summary
- Total debt items identified: [N]
- Priority distribution: [N] P0, [N] P1, [N] P2, [N] P3, [N] P4
- Estimated total remediation effort: [person-weeks]
- Top 3 recommendations: [brief]

## Debt by Type
| Type | Count | Avg Severity | Avg Business Impact |
|---|---|---|---|
| Architecture | [N] | [X] | [X] |
| Code | [N] | [X] | [X] |
| Test | [N] | [X] | [X] |
| Dependency | [N] | [X] | [X] |
| Infrastructure | [N] | [X] | [X] |
| Documentation | [N] | [X] | [X] |
| Design | [N] | [X] | [X] |

## Priority Items (P0-P1)
[Detailed entries per Step 5 template]

## Remediation Roadmap
| Quarter | Focus Area | Expected Outcome | Effort |
|---|---|---|---|
| [Q] | [area] | [measurable improvement] | [person-weeks] |

## Metrics to Track
- Development velocity trend (story points / sprint)
- Defect escape rate (bugs found in production)
- Incident frequency by system area
- Mean time to implement a feature in affected area
- CI pipeline duration
```

## Guardrails

- Never fabricate code quality metrics. Do not claim coverage percentages or complexity scores without data from the user. State which tools to run and what to look for.
- Never score debt without justification. Every severity and business impact score must include a brief rationale — scores without reasoning cannot be validated by the team.
- Never assume business priorities. Ask the user for their priorities rather than assuming what the organisation values most.
- Source-label outputs as `[From user context]`, `[Assessment methodology]`, or `[AI assessment — verify with team]`.

> **Tip:** Ask for XLSX, Markdown, or DOCX output via companyFILES to get a formatted, ready-to-share inventory.
