---
name: en-capacity-planning
description: Plan resource and workforce capacity with demand forecasting and utilisation analysis. Use when planning headcount, balancing workloads across teams, or forecasting resource needs for upcoming projects. Trigger with "plan capacity for", "do we have enough people", "resource forecast for".
---

# Capacity Planning Skill

Assess workforce and resource capacity against forecasted demand — with utilisation analysis, gap identification, and scenario modelling. The underlying numbers come from you, a connected source, or uploaded files.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project / resource tools via MCP** (e.g. Jira, Asana, Monday) | Current allocations, project schedules, milestones, open work |
| **HRIS via MCP** (e.g. Personio, Workday) | Headcount, FTE equivalents, leave, skill profiles |
| **companyRAG collections** | Historical utilisation data, past capacity plans, planning guidelines |
| **File upload (CSV/XLSX)** | Utilisation sheets, demand pipelines, headcount lists |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Capacity Assessment Framework

### Supply Inventory

Before forecasting demand, establish what capacity currently exists. For each team or resource pool:

1. Headcount: Number of people, FTE equivalents (account for part-time, contractors, shared resources)
2. Available hours: Total working hours minus planned leave, public holidays, training days, admin overhead
3. Skill profile: Capabilities per person or role — what types of work each resource can perform
4. Current allocation: Existing commitments by project, BAU (business-as-usual), and support obligations
5. Utilisation rate: (Allocated hours ÷ Available hours) × 100 — calculated from the organisation's own data

### Utilisation Classification

| Band | Utilisation | Interpretation | Action |
| --- | --- | --- | --- |
| **Under-utilised** | Below target band | Capacity available for new work or reallocation | Identify suitable work; check for skill mismatches |
| **Target band** | Organisation-defined optimal range | Healthy operating state with buffer for unplanned work | Maintain; monitor for drift |
| **Over-utilised** | Above target band | Sustained overload risk — quality, morale, and attrition exposure | Redistribute, defer, or augment |

The target band is organisation-specific. Do not assume a default. Ask the user to define their target utilisation range. If undefined, prompt them to set one based on their historical data and tolerance for unplanned work absorption.

### Capacity Calculation

For each team or resource pool:

```
CAPACITY SUMMARY:
  Team/Pool:              [name]
  Headcount (FTE):        [from org data]
  Available hours/period: [total working hours - leave - overhead]
  Currently allocated:    [hours committed to existing work]
  Remaining capacity:     [available - allocated]
  Utilisation rate:       [allocated ÷ available × 100]%
  Utilisation band:       [Under / Target / Over]
```

Aggregate across teams to produce an organisational capacity view. Flag teams where utilisation bands differ significantly — one team under-utilised while another is over-utilised signals a rebalancing opportunity.

## Demand Forecasting

### Demand Source Identification

Catalogue all sources of demand on the resource pool:

| Source Type | Examples | Predictability |
| --- | --- | --- |
| **Committed projects** | Approved roadmap items, signed contracts, regulatory deadlines | High — known scope and timeline |
| **Pipeline projects** | Proposals in progress, budget requests pending approval | Medium — adjust by probability of approval |
| **BAU / run-the-business** | Support, maintenance, operational tasks, recurring reporting | High — use historical average with seasonal adjustment |
| **Unplanned / reactive** | Incidents, ad-hoc requests, executive priorities | Low — reserve capacity based on historical frequency |
| **Strategic initiatives** | Transformation programmes, new market entry, M&A integration | Variable — scenario-dependent |

### Demand Quantification

For each demand source:

1. Estimate effort: Hours or FTEs required per period. Use three-point estimation (optimistic, likely, pessimistic) for uncertain items.
2. Weight by probability: For pipeline items, multiply effort by probability of materialising. Committed = 100%, pipeline = organisation's historical conversion rate.
3. Map timing: When does the demand hit? Spread across periods based on project schedules.
4. Identify skill requirements: What capabilities does each demand source require? Match against the supply skill profile.

### Three-Point Estimation

For uncertain demand items, use:

```
Expected effort = (Optimistic + 4 × Likely + Pessimistic) ÷ 6
Standard deviation = (Pessimistic - Optimistic) ÷ 6
```

This produces a weighted average that accounts for estimation uncertainty. The standard deviation indicates confidence — large spreads between optimistic and pessimistic signal high uncertainty that should be addressed through scenario modelling rather than single-point planning. Work these calculations from the provided numbers and show your reasoning so the result stays verifiable.

## Gap Analysis

### Supply-Demand Comparison

For each period and skill category:

```
GAP ANALYSIS:
  Period:             [time window]
  Skill category:     [role type or capability]
  Supply (FTE):       [available capacity from supply inventory]
  Demand (FTE):       [forecasted demand, probability-weighted]
  Gap:                [supply - demand; positive = surplus, negative = shortfall]
  Confidence:         [High / Medium / Low based on estimation spread]
  Gap classification: [Surplus / Balanced / Moderate shortfall / Critical shortfall]
```

### Gap Classification

| Classification | Condition | Risk Level |
| --- | --- | --- |
| **Surplus** | Supply exceeds demand by more than the unplanned buffer | Low — but monitor for cost efficiency |
| **Balanced** | Supply meets demand within the unplanned buffer | Low — healthy operating state |
| **Moderate shortfall** | Demand exceeds supply by up to the organisation's defined threshold | Medium — addressable through prioritisation or temporary augmentation |
| **Critical shortfall** | Demand exceeds supply beyond the threshold | High — requires immediate action: scope reduction, timeline extension, or resource acquisition |

The threshold between moderate and critical is organisation-specific. Prompt the user to define it if not established.

## Scenario Modelling

Build at minimum three scenarios to stress-test the capacity plan:

### Scenario Structure

| Scenario | Demand Assumption | Supply Assumption | Purpose |
| --- | --- | --- | --- |
| **Base case** | Committed + probability-weighted pipeline | Current headcount + approved hires | Most likely outcome |
| **High demand** | Committed + all pipeline at 100% + unplanned demand uplift | Current headcount + approved hires | Stress test for demand surge |
| **Constrained supply** | Base case demand | Current headcount minus attrition estimate, no new hires | Impact of hiring freeze or attrition spike |

For each scenario, run the gap analysis and document:

- Which teams or skill categories hit critical shortfall first
- At what point in the timeline the gap becomes unmanageable
- What levers are available (see Recommendation Framework below)

Add organisation-specific scenarios as needed (e.g., M&A integration, market expansion, technology migration).

## Recommendation Framework

When gaps are identified, evaluate mitigation options in this priority order:

| Priority | Lever | Lead Time | Cost Impact | Reversibility |
| --- | --- | --- | --- | --- |
| 1 | **Reprioritise demand** | Immediate | None | High |
| 2 | **Redistribute across teams** | Days–weeks | Low | High |
| 3 | **Improve efficiency** | Weeks–months | Low–Medium | High |
| 4 | **Temporary augmentation** (contractors, vendors) | Weeks | Medium–High | High |
| 5 | **Permanent hire** | Months | High | Low |
| 6 | **Defer or descope work** | Immediate | Variable | Medium |

For each recommendation:

```
RECOMMENDATION:
  Gap addressed:     [which shortfall this mitigates]
  Lever:             [from priority table]
  Specific action:   [concrete step — not "hire more people" but "hire 2 senior backend engineers by Q3"]
  Effort to implement: [time and resources required to execute the lever]
  Expected impact:   [FTE equivalent or hours recovered]
  Timeline:          [when the capacity becomes available]
  Risk:              [what could prevent this from working]
  Dependencies:      [approvals, budget, market availability]
```

## Output Template

Structure the final capacity plan as follows:

```
# Capacity Plan — [Team/Organisation] — [Period]

## Executive Summary
- Current utilisation: [aggregate rate and band]
- Forecasted demand: [total FTE demand for planning period]
- Gap assessment: [number of teams/skills in shortfall]
- Key risk: [single biggest capacity risk]
- Primary recommendation: [highest-impact action]

## Supply Inventory
[Per-team capacity summary tables]

## Demand Forecast
[Per-source demand quantification with timing]

## Gap Analysis
[Per-period, per-skill gap classification]

## Scenario Analysis
[Base case, high demand, constrained supply results]

## Recommendations
[Prioritised actions with expected impact]

## Assumptions and Limitations
[Document all assumptions made during the analysis]

## Review Cadence
[When this plan should be refreshed — typically quarterly or when material changes occur]
```

## Adapt to Your Business

Adapt this skill to your organisation by defining:

- Target utilisation band: Your optimal range (e.g., 75-85%) and the rationale behind it
- Planning horizon: How far ahead you plan (quarterly, semi-annually, annually)
- Demand probability thresholds: Your conversion rates for pipeline to committed work
- Critical shortfall threshold: The gap size that triggers escalation
- Unplanned work buffer: Percentage of capacity reserved for reactive work (based on historical data)
- Attrition assumptions: Expected turnover rate for supply modelling
- Approval workflows: Who authorises each mitigation lever

## Guardrails

- Never generate headcount benchmarks, staffing ratios, or utilisation targets from training data. All numbers must come from the user's organisational data.
- Never assume a "standard" utilisation target. Ask the user to define their target band.
- Never fabricate pipeline data or demand forecasts. All demand inputs come from the user. When data is insufficient, state "insufficient data to forecast" rather than extrapolating.
- Label generated content: `[From org data]`, `[Framework methodology]`, `[AI estimate — verify]`.

> **Tip:** Request an XLSX, DOCX, or Markdown output via companyFILES to get a formatted, ready-to-share capacity plan.
