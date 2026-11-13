---
name: en-pipeline-review
description: Analyse deal health, surface stale or at-risk opportunities, and produce a prioritised weekly action plan. Use when preparing for a pipeline review meeting, assessing forecast accuracy, or identifying stuck deals. Trigger with "review my pipeline", "pipeline health check", "deal risk analysis".
---

# Pipeline Review Skill

Diagnose pipeline and deal health, qualify opportunities, and build forecasts using complexity-routed frameworks (BANT through full MEDDPICC). All deal and pipeline data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Deal stages, values, owners, days-in-stage, close history, contact engagement |
| **Analytics / forecasting tools via MCP** | Conversion rates, historical close data, pipeline snapshots over time |
| **companyRAG / file upload (CSV/XLSX)** | Exported pipeline reports, deal notes, qualification frameworks, lost-deal analyses |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Sales Motion Complexity Assessment

Assess the deal's complexity along four dimensions. All thresholds are relative to the customer's own norms -- never absolute values.

| Dimension | Low | Medium | High |
| --- | --- | --- | --- |
| **Sales cycle length** | Well below customer's average | Around customer's average | Well above customer's average |
| **Deal value** | Below customer's average | Around customer's average | Significantly above customer's typical range |
| **Stakeholder count** | Single contact or small group | Defined buying center | Cross-functional buying committee |
| **Solution complexity** | Single product/service, standard | Some customization, multi-product | Custom solution, multi-department |

### Complexity Routing

```
Assess the 4 dimensions for this deal (relative to customer's own norms):

  Mostly LOW across dimensions
    --> BANT qualification + Status-based forecasting
    --> 3-point scoring (Weak / Adequate / Strong)
    --> Historical conversion rates per status determine forecast

  Mix of LOW and MEDIUM, or mostly MEDIUM
    --> BANT+ or simplified MEDDPICC + Milestone-based forecasting
    --> 0-3 scoring per selected elements
    --> Forecast probability tied to milestone completion

  Multiple HIGH dimensions, or HIGH in stakeholder/value/solution (cycle length alone does not escalate), or MEDIUM across all four
    --> Full MEDDPICC (all 8 elements) + Probability-based forecasting
    --> 0-3 scoring with behavioral anchors
    --> Stage-probability framework with scenario analysis
```

Mixed sales motions: If a customer sells across complexity levels, segment the pipeline and apply the appropriate methodology per segment. Users can always override to a more or less detailed framework.

## BANT Qualification Framework

For LOW complexity deals. Score each element on a 3-point scale:

| Element | Weak (1) | Adequate (2) | Strong (3) |
| --- | --- | --- | --- |
| **Budget** | No budget discussion | Budget range acknowledged | Budget confirmed and allocated |
| **Authority** | Decision maker unknown | Decision maker identified | Decision maker engaged and supportive |
| **Need** | Pain vaguely stated | Need articulated with business impact | Need quantified with urgency driver |
| **Timeline** | No timeline discussed | General timeframe mentioned | Specific deadline with compelling event |

**Advancement threshold**: All elements Adequate (2) or above. Any element Weak (1) triggers gap analysis (see below).

For medium complexity, use the BANT+ / simplified MEDDPICC routing in the complexity section above; elaborate rubrics and question banks should follow the same evidence standards as the tables in this skill.

## MEDDPICC Scoring Framework

For HIGH complexity deals. Score each of the 8 elements on a 0-3 scale:

| Score | Definition |
| --- | --- |
| **0** | Not identified -- no information available |
| **1** | Identified but unverified -- mentioned but not confirmed with evidence |
| **2** | Verified and engaged -- confirmed through direct interaction or documentation |
| **3** | Fully validated and mobilized -- actively supporting the deal with evidence of action |

Apply to: **M**etrics, **E**conomic Buyer, **D**ecision Criteria, **D**ecision Process, **P**aper Process, **I**mplicate the Pain, **C**hampion, **C**ompetition.

Use the 0-3 definitions above as behavioral anchors; for each low-scored element, draft targeted discovery questions that seek verifiable evidence (who confirmed, when, artifact or meeting).

### Simplified MEDDPICC for Medium Complexity

Select a subset of elements based on historical failure modes:

1. Identify historical failure modes : What caused the customer's last 3-5 lost deals?
2. Map failures to MEDDPICC elements : Each failure maps to the element that would have caught it
3. Prioritize those elements : The right subset depends on the customer's deal dynamics
4. Score using 0-3 scale above

If failure data unavailable, start with: Metrics, Economic Buyer, Champion, Decision Process.

## SPIN as Discovery Tool

SPIN (Situation, Problem, Implication, Need-payoff) FEEDS INTO qualification -- not a standalone framework. Each question type maps to specific qualification gaps:

| SPIN Type | Feeds Into (BANT) | Feeds Into (MEDDPICC) |
| --- | --- | --- |
| **Situation** | Authority, Timeline | Economic Buyer, Decision Process |
| **Problem** | Need | Implicate the Pain, Metrics |
| **Implication** | Need (urgency), Budget | Metrics, Champion |
| **Need-payoff** | Budget (value justification) | Decision Criteria, Metrics |

Use SPIN to fill gaps in elements scored 0-1 (MEDDPICC) or Weak (BANT), mapping question types to the qualification gaps in the SPIN table above.

## Gap Analysis Decision Tree

For any element scored below threshold:

```
Element scored below threshold
  |
  +--> First assessment?
  |      YES --> Generate targeted SPIN discovery questions
  |              Schedule touchpoint, re-score after discovery
  |
  +--> Discovery attempted but element remains low?
  |      YES --> Escalation check:
  |              - Gap blocking deal progression? (stage-gate violation)
  |              - Persisted for >1 review cycle?
  |              - 3+ elements low simultaneously?
  |              |
  |              ANY YES --> Flag at-risk. Recommend: executive sponsor
  |                          engagement, champion development, or
  |                          disqualification review
  |              ALL NO --> Continue discovery, adjust approach
  |
  +--> Low across 3+ review cycles?
         YES --> Stuck deal. Explicit disqualification review:
                 "What would need to change?"
                 If unclear --> strong disqualification signal
```

## Deal Health vs. Deal Risk

Two distinct assessments that work together:

**Deal health** (qualification completeness): Do we know enough about this deal?

- BANT: Sum scores / 12. Any Weak = Yellow, 2+ Weak = Red.
- MEDDPICC: Sum scores / 24. Weight critical elements if customer specifies.

**Deal risk** (pipeline risk): Will this deal close on time and at value?

| Factor | Assessment Method |
| --- | --- |
| **Days-in-stage** | Compare to customer's historical average for that stage |
| **Qualification completeness** | Deal health score feeds in here |
| **Engagement recency** | Time since last meaningful customer interaction |
| **Stakeholder coverage** | Engaged stakeholders vs. typical for this deal size |
| **Competitive presence** | Active competition without differentiation strategy = risk |
| **Next-step clarity** | No defined, agreed next step with a date = risk flag |

Composite risk: weight factors by what's most predictive in customer's historical data. Classify as Low / Medium / High risk.

**Stage alignment**: Compare deal health against pipeline stage expectations. Define per stage: "What must be true to advance?" Misalignment = risk flag.

## Pipeline Coverage Analysis

Coverage ratio -- DERIVED from customer's own data, never prescribed.

1. Historical conversion rate : Deals closed-won / Total entering pipeline (customer-specified period)
2. Derive coverage : Coverage = 1 / conversion rate
3. Segment if rates vary : By deal type, source, rep tenure, or product line
4. Age-adjust : Stale pipeline converts at lower rates -- calculate separate rates
5. Current coverage : Active pipeline value / Target

**Never prescribe specific ratios.** Teach the calculation; the customer derives their own number.

## Forecast Categories

Matched to the forecasting methodology from complexity routing:

**Status-based (transactional)**: Map each deal status to historical close rate. Forecast = sum of (value x rate). Recalibrate from recent data.

**Milestone-based (project)**: Milestones drive close probability (adjusted for milestone difficulty). Revenue phasing follows contract terms (ratable, annual, upon delivery), not milestone completion itself.

**Probability-based (complex)**: Derive stage probabilities from historical data. Set category thresholds (Commit/Best Case/Pipeline) from customer's confidence levels. Run scenario analysis: Best Case, Most Likely, Worst Case.

Apply the status-, milestone-, and probability-based definitions above when building forecast models; document assumptions and calibrate from the customer's historical close data.

**Low-volume pipelines**: When the customer has fewer than 20 deals per stage, standard probability calibration is unreliable. Options: combine adjacent stages to increase sample size, use Bayesian smoothing with priors from overall pipeline rates, or fall back to milestone-based forecasting which requires less historical volume.

## Pipeline Health Diagnostics

All benchmarks relative to customer's own historical norms. Analyze four dimensions:

1. Stage distribution : Compare current value distribution to historical norms. Imbalances signal specific issues (top-heavy = qualification/advancement, bottom-heavy = generation shortfall).
2. Velocity : Track days-per-stage and conversion rates against baselines. Trends matter more than snapshots.
3. Aging : Identify deals exceeding typical cycle length. Quantify conversion discount from customer's data.
4. Creation vs. close balance : Compare created vs. closed over rolling periods. Sustained negative balance = future gap.

## Pipeline Review Cadence

| Motion | Cadence | Focus | Action Triggers |
| --- | --- | --- | --- |
| **Transactional** | Daily/weekly snapshots | Conversion trends, volume, distribution shifts | Rate drop vs. historical, volume shortfall |
| **Project-Based** | At milestone transitions | Completion rates, delivery risk, revenue timing | Milestone delays, scope changes |
| **Complex** | Weekly deal + monthly shape + quarterly accuracy | Stuck deals, stage distribution, forecast vs. actual | Risk escalation, shape imbalance, forecast miss |

## Qualification Review Output

Scale detail by complexity: Lightweight (BANT) produces scores + advance/hold/disqualify. Standard adds evidence, gap analysis with SPIN questions, and stage alignment. Comprehensive (Full MEDDPICC) adds per-element confidence levels (High/Medium/Low), weighted health scoring, and risk escalation triggers.

All reviews must include evidence source tags: [From CRM/user input], [From qualification framework], [AI assessment].

## Guardrails

1. Never generate deal or pipeline data. All prospect information, deal values, stages, and conversion history must come from the user, a connected MCP source, companyRAG collections, or uploaded files.
2. No prescribed numbers. Never prescribe coverage ratios, conversion rates, stage probabilities, or benchmarks. Teach the calculation; the customer derives their number.
3. Source labeling. Tag every assertion — [From CRM/user input], [From qualification framework], [AI assessment]. For forecasts, add [Scenario analysis].
4. Human verification required. Include "Verify with sales leadership before acting on qualification/risk assessments" on all outputs.

> **Tip:** Ask for XLSX output via companyFILES to get a formatted spreadsheet ready for distribution; DOCX or Markdown work well for the written review summary.
