---
name: en-product-spec
description: Create feature specifications or PRDs from vague ideas via structured clarifying questions and scope management. Use when defining a new feature, writing a brief for engineering, or turning stakeholder requests into actionable specs. Trigger with "write a spec for", "help me spec this out", "PRD for [feature]".
---

# Product Spec Skill

Turn ambiguous product ideas into clear, engineering-ready specifications. Covers clarification workflows, scope management, requirement structuring, and risk identification so reliable PRDs result. The inputs come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Linear, Asana, Shortcut) | Existing tickets, epics, or OKRs for context; push finalised stories back |
| **Design tool via MCP** (e.g. Figma, Miro) | Wireframes, user flows, design-system constraints |
| **companyRAG collections** | Existing specs, prior research, competitive context, architecture docs |
| **companyRAG / file upload** | Confluence pages, discovery notes, technical assessments |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Specification Workflow

Execute these five phases sequentially. Each phase has a gate — do not advance until the gate condition is met.

### Phase 1: Clarify the Problem

Before writing a single requirement, establish what problem this feature solves and for whom. Most spec failures trace back to skipping this phase.

**Clarification question sequence** (ask in this order, adapt phrasing to context):

1. Problem statement: "What problem does this solve, and how do you know it's a real problem?" — Look for evidence: user research, support tickets, churn data, sales feedback. If the answer is "stakeholder X wants it," probe for the underlying problem.
2. Affected users: "Who experiences this problem, and how often?" — Establish the user segment, frequency, and severity. A problem affecting 5% of users daily may matter more than one affecting 50% annually.
3. Current workaround: "How do users solve this today without the feature?" — Workarounds reveal the true workflow, expectations, and pain intensity. No workaround may indicate low urgency.
4. Business context: "Why solve this now? What changes if we don't?" — Connects to OKRs, revenue targets, competitive pressure, or regulatory deadlines. If the answer is vague, the priority is uncertain.
5. Prior attempts: "Has this been tried before? What happened?" — Prevents re-treading failed approaches and surfaces organisational constraints.

**Gate**: A problem statement exists that names the user, the pain, and the evidence. If the user cannot articulate the problem, help them formulate one before proceeding — do NOT skip to solution design.

### Phase 2: Define Scope

Scope creep is the primary cause of spec failure. Use explicit in/out boundaries and a phasing framework.

**Scope definition steps**:

1. Solution sketch: Ask the user to describe their ideal solution in 2-3 sentences — maximum. This forces prioritisation before detail.
2. In-scope / out-of-scope table: For every capability mentioned, classify explicitly:

| Capability | In Scope (v1) | Future (v2+) | Out of Scope | Rationale |
| --- | --- | --- | --- | --- |
| [capability] | ✓ / — | — / ✓ | — / ✓ | [why this classification] |

1. **MoSCoW classification** for in-scope items:   - Must have: Feature is broken without it. Ship-blocking.   - Should have: Significant value, strong expectation, but a workaround exists.   - Could have: Nice-to-have if capacity allows. First to cut.   - Won't have (this time): Explicitly deferred. Documenting "won't" prevents scope drift.
2. **Scope anchoring question**: "If we could only ship ONE thing from this spec, what would it be?" — The answer is the non-negotiable core. Everything else is relative priority around it.

**Gate**: An in/out table exists, MoSCoW classification is applied, and the user has confirmed the scope boundary.

### Phase 3: Write Spec Sections

Structure the PRD using the output template below. For each section, apply these writing principles:

- Requirements over solutions: Describe WHAT and WHY, not HOW. "Users must be able to filter by date range" not "Add a date-picker component."
- Testable acceptance criteria: Every requirement must have a verifiable condition. "The page loads" is not testable. "The page renders the first 20 results within 2 seconds on a 3G connection" is.
- Edge cases upfront: For each requirement, ask "What happens when...?" — empty states, error conditions, permission boundaries, data limits, concurrent access.
- One requirement, one statement: Compound requirements ("the system should X and Y") hide complexity and create ambiguous acceptance criteria. Split them.

**Requirement decomposition pattern**:

```
REQUIREMENT: [Clear, single-purpose statement]
  User story:        As a [role], I want [capability] so that [outcome]
  Acceptance criteria:
    GIVEN [context]
    WHEN  [action]
    THEN  [observable result]
  Edge cases:
    - [What if input is empty/malformed/at limit?]
    - [What if user lacks permission?]
    - [What if dependent service is unavailable?]
  Dependencies:      [Other requirements or systems this depends on]
  Open questions:    [Unresolved decisions — owner and deadline for resolution]
```

### Phase 4: Identify Risks

Systematically surface risks before engineering begins. Categorise using:

| Risk Category | What to Look For | Mitigation Pattern |
| --- | --- | --- |
| **Technical** | New technology, integration complexity, performance requirements, data migration | Spike/prototype first, define fallback approach |
| **Scope** | Ambiguous requirements, undefined edge cases, implicit assumptions | Tighten acceptance criteria, add explicit constraints |
| **Dependency** | External teams, third-party APIs, platform approvals, shared infrastructure | Identify critical path, establish SLAs or deadlines with owners |
| **User adoption** | Workflow disruption, learning curve, migration from existing behaviour | Plan rollout strategy, define adoption metrics |
| **Timeline** | Competing priorities, team availability, sequential dependencies | Identify parallelisable work, flag resource conflicts early |

For each risk, document: description, likelihood (High/Medium/Low), impact (High/Medium/Low), mitigation plan, and owner.

**Gate**: At least three risks are identified and documented. A spec with zero risks has not been examined critically.

### Phase 5: Set Success Metrics

Define how the team will know the feature succeeded. Use the metric hierarchy:

1. Primary metric (1 only): The single number that most directly measures whether the problem from Phase 1 is solved. Tied to the problem statement, not the solution.
2. Leading indicators (2-3): Metrics that move BEFORE the primary metric, providing early signal. Example: if primary is retention, leading might be feature adoption rate or task completion rate.
3. Guardrail metrics (1-2): Metrics that must NOT degrade. Prevent solving one problem by creating another. Example: page load time must not increase; support ticket volume must not spike.

For each metric:

```
METRIC: [name]
  Type:       Primary / Leading / Guardrail
  Definition: [Precise calculation — numerator, denominator, time window]
  Baseline:   [Current value or "to be established in first 2 weeks"]
  Target:     [Specific threshold with timeframe]
  Source:     [Where the data comes from — analytics tool, database query, survey]
```

**Gate**: At least one primary metric, one leading indicator, and one guardrail are defined with measurable targets.

## PRD Output Template

Use this structure for the final document. Adapt section depth to feature complexity — a two-week feature needs less detail than a quarter-long initiative.

```
# [Feature Name] — Product Requirements Document

## 1. Problem Statement
[From Phase 1 — the problem, who experiences it, evidence it matters]

## 2. Solution Overview
[2-3 sentence description of the proposed solution approach]

## 3. Goals & Success Metrics
[From Phase 5 — primary metric, leading indicators, guardrails with targets]

## 4. Scope
### 4a. In Scope (v1)
[MoSCoW-classified capabilities for this release]

### 4b. Out of Scope
[Explicitly deferred items with rationale]

## 5. User Stories & Requirements
[From Phase 3 — decomposed requirements with acceptance criteria]

### 5a. Must Have
[Ship-blocking requirements]

### 5b. Should Have
[High-value requirements with workarounds]

### 5c. Could Have
[If capacity allows]

## 6. User Flows
[Key workflows — reference design files if available]

## 7. Edge Cases & Error Handling
[Consolidated from Phase 3 requirement decomposition]

## 8. Technical Considerations
[Known constraints, API dependencies, performance requirements, data model changes]

## 9. Risks & Mitigations
[From Phase 4 — categorised risks with owners]

## 10. Dependencies
[External teams, services, approvals required]

## 11. Open Questions
[Unresolved decisions — owner and deadline for each]

## 12. Release Plan
[Rollout strategy, feature flags, phased launch criteria]

## 13. Appendix
[Supporting research, competitive context, prior art references]
```

## Spec Sizing Guide

Match spec depth to feature scope:

| Feature Scope | Typical Duration | Spec Depth | Key Sections |
| --- | --- | --- | --- |
| **Small** (bug fix, copy change, config) | < 1 week | Lightweight — problem + requirements + acceptance criteria | Sections 1, 5, 7 |
| **Medium** (new feature, workflow change) | 1-6 weeks | Standard — full PRD minus appendix | Sections 1-10 |
| **Large** (new product area, platform change) | 1+ quarter | Comprehensive — full PRD with appendix, phased scope | All sections, phased release plan |

## Anti-Patterns

Recognise and flag these when they appear:

1. Spec without a problem statement: A solution searching for a problem. If Phase 1 cannot produce a clear problem statement with evidence, the feature is not ready to spec. Redirect to user research or stakeholder alignment.
2. Unbounded scope: No explicit out-of-scope section, no MoSCoW classification, or every item is "Must have." Challenge with the scope anchoring question and force prioritisation.
3. Requirements disguised as solutions: "Add a dropdown" instead of "Users must be able to select from predefined options." Solution specificity in requirements constrains engineering unnecessarily and conflates the PM and engineering roles.
4. Acceptance criteria that cannot fail: "The feature works correctly" is not testable. Every criterion must have a clear pass/fail condition.
5. Zero risks identified: Signals insufficient critical examination. Push back — every feature has risks. The question is whether they are identified and managed.
6. Metrics without baselines: A target of "increase retention by 10%" is meaningless without knowing the current rate. If baselines are unavailable, the first milestone is establishing them.
7. Orphaned open questions: Questions listed but no owner or deadline for resolution. Every open question must have a name and a date, or it will block engineering.

## Next Steps After Spec Completion

Once the PRD is reviewed and approved:

1. Engineering review: Schedule a technical review to surface implementation concerns, refine estimates, and identify spikes.
2. Design handoff: If design work is required, ensure wireframes or prototypes cover all user flows and edge cases in the spec.
3. Spec as living document: Specs evolve during implementation. Establish a change-log section and a lightweight change-approval process (who can approve scope changes mid-build).

## Guardrails

- NEVER fabricate user research, metrics, or data. When data is not provided, state "Data needed — [specify what]" and leave the field for the user to fill.
- NEVER assume technical constraints. Flag as [Requires engineering input] unless the user or a companyRAG collection provides specifics.
- NEVER generate competitor features or market data. Reference the competitive-analysis skill or ask the user.
- Source-label every element as [From user input], [Spec framework], or [AI suggestion — verify].

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted document ready for distribution.
