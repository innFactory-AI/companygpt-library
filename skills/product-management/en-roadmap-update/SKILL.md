---
name: en-roadmap-update
description: Update or reprioritise roadmaps using Now/Next/Later, quarterly, or OKR-aligned frameworks with dependency mapping. Use when reprioritising after a strategy shift, preparing a roadmap review, or communicating product direction. Trigger with "update the roadmap", "reprioritise roadmap", "roadmap for Q[n]".
---

# Roadmap Update Skill

Build, update, and communicate product roadmaps with framework selection, prioritisation scoring (RICE, MoSCoW, weighted), dependency mapping, and audience-tailored communication formats. Roadmap data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Productboard, Linear) | Backlog items, current roadmap state, status, dependencies, owners |
| **companyRAG collections** | Strategy documents, OKRs, customer feedback, discovery notes, competitive analyses |
| **File upload** | Current roadmap exports, capacity plans, metric reports |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Framework Selection

Choose the roadmap framework that fits the team's planning maturity, stakeholder needs, and delivery cadence. Use one framework consistently — mixing frameworks creates confusion.

| Framework | Best For | Trade-off |
| --- | --- | --- |
| **Now / Next / Later** | Teams with high uncertainty, continuous delivery, or stakeholder audiences that over-index on dates | Low commitment specificity — harder to coordinate cross-team dependencies |
| **Quarterly (Q1/Q2/Q3/Q4)** | Teams with predictable delivery cadence, board reporting cycles, or regulatory timelines | Date-bound — creates implicit commitments that may be premature |
| **OKR-aligned** | Teams with mature OKR practice where roadmap items map directly to measurable objectives | Requires well-defined OKRs; poorly written OKRs produce poorly structured roadmaps |
| **Theme-based** | Portfolio-level roadmaps spanning multiple teams or product lines | High-level — requires decomposition for execution planning |

### Selection Decision Tree

```
Does the team have a mature OKR practice with measurable Key Results?
  YES → OKR-aligned (initiatives grouped under objectives)
  NO  → Does the team commit to quarterly delivery dates?
          YES → Quarterly
          NO  → Is the roadmap for a single team or multiple?
                  Single team → Now / Next / Later
                  Multiple teams / portfolio → Theme-based (with team-level decomposition)
```

## Prioritisation Methodology

### RICE Scoring

Use RICE when the backlog has many competing items and the team needs a quantitative first-pass ranking. RICE does NOT make the decision — it creates an informed starting point for discussion.

| Factor | Definition | Scoring Guidance |
| --- | --- | --- |
| **Reach** | How many users/accounts will this affect in a defined time period? | Use a consistent time window (e.g., per quarter). Count from your own data, not estimates. |
| **Impact** | How much will this move the target metric per user reached? | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **Confidence** | How certain are you about reach and impact estimates? | 100% = high confidence with data, 80% = educated estimate, 50% = gut feel |
| **Effort** | How many person-sprints (or person-weeks) will this take? | Include design, engineering, QA, and rollout — not just coding |

```
RICE SCORE = (Reach × Impact × Confidence) / Effort
```

**RICE calibration rules**:

- Score all items in the same session to avoid drift
- Re-score when new data arrives (user research, technical discovery)
- Never compare RICE scores across different product areas — the scales are not calibrated
- RICE is an input to prioritisation, not the output — override for strategic alignment, dependencies, or sequencing constraints

### MoSCoW for Scope Gates

When the roadmap has a fixed time boundary (quarterly, release-based), apply MoSCoW to classify what fits:

- Must have : The roadmap period fails without it. Non-negotiable commitments (regulatory, contractual, critical bugs).
- Should have : High value, strong stakeholder expectation, but deferrable by one period without critical impact.
- Could have : Valuable if capacity allows. First to cut when capacity is tight.
- Won't have (this period) : Explicitly deferred. Document the "won't" to prevent scope drift and set expectations.

### Weighted Scoring for Strategic Alignment

When RICE alone is insufficient (e.g., strategic bets that don't score well on reach), add strategic dimensions:

| Dimension | Weight (customise) | Score (1-5) |
| --- | --- | --- |
| Strategic alignment | [weight] | How well does this advance the company/product strategy? |
| Customer demand | [weight] | Frequency and intensity of customer requests |
| Revenue impact | [weight] | Direct or indirect revenue contribution |
| Technical debt reduction | [weight] | Does this reduce maintenance burden or unlock future velocity? |
| Competitive necessity | [weight] | Does not building this create competitive disadvantage? |

Weights must sum to 1.0 and be set BEFORE scoring items. Changing weights after scoring is a prioritisation smell — it suggests reverse-engineering the answer.

## Roadmap Update Workflow

### Step 1: Gather Inputs

Before reprioritising, collect current state:

1. Current roadmap : What was planned? What shipped? What slipped?
2. New inputs : Strategy changes, customer feedback, competitive moves, technical discoveries, regulatory requirements
3. Capacity changes : Team size changes, new hires ramping, departures, reorgs
4. Dependency updates : Cross-team commitments that have changed, external timelines that shifted
5. Metric performance : Are current initiatives moving target metrics? Reference the review-metrics skill for analysis.

### Step 2: Triage New Items

For each new item entering the backlog:

1. Problem validation : Does this solve a validated problem? (Reference write-spec Phase 1)
2. Strategic fit : Does this align with current strategy and OKRs?
3. Size estimate : Rough t-shirt size (S/M/L/XL) for initial prioritisation — detailed estimation happens later
4. Urgency assessment : Is there a time-bound trigger (competitive, regulatory, contractual)?

### Step 3: Reprioritise

Apply the selected prioritisation methodology (RICE, MoSCoW, weighted scoring) to the combined backlog (existing + new items). Compare the new ranking to the current roadmap:

| Change Type | Action |
| --- | --- |
| **New item ranks above existing committed work** | Evaluate: swap, defer, or increase capacity? Document the trade-off explicitly. |
| **Existing item's priority dropped** | Move to next period or backlog. Communicate the change to affected stakeholders. |
| **Item completed or no longer relevant** | Remove and document why. Celebrate completions; explain cancellations. |
| **Item blocked by unresolved dependency** | Move to "blocked" status. Assign dependency owner. Do not keep on roadmap without a resolution path. |

### Step 4: Validate Dependencies

For the updated roadmap, build or refresh the dependency map:

```
DEPENDENCY MAP:
  Initiative: [name]
  Depends on: [initiative / team / external]
  Dependency type: Sequential (must finish first) / Parallel (can overlap) / Informational (needs input, not blocking)
  Status: Resolved / In progress / At risk / Unresolved
  Owner: [name]
  Expected resolution: [date]
```

**Critical path identification**: Trace the longest chain of sequential dependencies. This is the minimum timeline for the roadmap regardless of team capacity. If the critical path exceeds the planning period, scope must be reduced.

### Step 5: Communicate Changes

Tailor the roadmap update to each audience. See the Stakeholder Communication Format section below.

## Stakeholder Communication Format

Different audiences need different views of the same roadmap.

### Executive / Board View

Focus: Strategy alignment, business outcomes, resource allocation.

```
ROADMAP SUMMARY — [Period]
Strategic priorities:  [2-3 themes tied to company OKRs]
Key deliverables:      [3-5 headline items with expected outcomes]
Resource allocation:   [% of capacity per theme]
Key risks:             [Top 2-3 risks to roadmap delivery]
Changes since last review:  [What moved in/out and why]
```

### Engineering / Design View

Focus: Scope, dependencies, sequencing, technical requirements.

```
ROADMAP — [Period]
Sprint-level breakdown:  [Initiatives decomposed into sprint-sized work]
Dependencies:            [Full dependency map with owners and dates]
Technical risks:         [Architecture decisions, spikes needed, unknowns]
Capacity allocation:     [Team-by-team capacity vs. planned work]
```

### Customer-Facing View

Focus: Value delivered, timeline ranges (not exact dates), no internal details.

```
PRODUCT UPDATE — [Period]
Coming soon:    [Features in active development — describe value, not implementation]
On our radar:   [Planned features — express as problems being solved, not solutions]
Recently shipped: [Completed features with adoption/impact data if available]
```

**Rule**: Customer-facing roadmaps use time ranges ("this quarter," "first half"), never specific dates. Never expose internal prioritisation scores, internal project names, or technical implementation details.

## Guardrails

- Never fabricate initiative data, timelines, or capacity numbers. All roadmap content must come from the user, project tracker, or a companyRAG collection.
- Never generate RICE scores, effort estimates, or reach numbers. Provide the scoring framework; the team populates it with their data.
- Never claim "industry standard" prioritisation weights or roadmap structures. Frameworks are methodology; specific weights and priorities are organisation-specific.
- Roadmap items are not commitments unless explicitly marked as such. Maintain that distinction in every output.
- Source-label every element as `[From user/roadmap data]`, `[Roadmap framework]`, or `[AI suggestion — verify]`.

> **Tip:** Ask for Markdown, DOCX, or XLSX output via companyFILES to get a formatted roadmap ready to share.
