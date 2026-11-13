---
name: en-performance-report
description: Generate marketing performance reports with trend analysis, wins/misses, attribution notes, and prioritised optimisation recommendations. Use when preparing a weekly or monthly marketing review, analysing campaign ROI, or diagnosing a funnel drop. Trigger with "marketing performance report", "campaign analysis", "what's working in marketing".
---

# Performance Report Skill

Build measurement plans, select attribution models, analyse campaign results, and design marketing experiments. All performance data comes from your sources — this skill provides process and structure, not benchmarks.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Analytics & ad platforms via MCP** (e.g. GA4, ad platforms) | Traffic, impressions, clicks, spend, conversions, campaign performance |
| **CRM via MCP** (e.g. HubSpot) | Leads, pipeline influence, deals, CAC inputs, closed-won data |
| **companyRAG collections** | Historical reports, measurement plans, campaign briefs, prior learnings |
| **File upload (CSV/XLSX exports)** | Manually exported campaign data, funnel breakdowns, spend tables |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Attribution Model Selection

This is the core decision framework of this skill. Use it whenever a customer needs to choose, evaluate, or migrate between attribution approaches.

### Decision Tree

Pre-filter: If more than half of customer touchpoints occur offline (events, phone calls, direct mail, field sales), start with Marketing Mix Modeling (see MMM vs MTA section below) rather than this digital-oriented attribution decision tree.

Score each factor to determine the right model type. Majority column wins; if split, start with multi-touch.

| Factor | Single-Touch | Multi-Touch | Hybrid |
| --- | --- | --- | --- |
| Sales cycle length | Short (< 30 days typical) | Medium (30-180 days typical) | Long (> 180 days typical) or mixed |
| Avg touchpoints per conversion | Few (1-3 typical) | Moderate (4-10 typical) | Many (> 10 typical) or unknown |
| Data maturity | Basic (last-click available) | Intermediate (multi-touch tracking) | Advanced (cross-device, offline) |
| Marketing channels | 1-2 dominant | 3-5 active | 6+ with offline mix |
| Analytics investment | Minimal | Moderate | Significant |

These thresholds are starting points -- calibrate to your business. A "short" cycle for enterprise software differs from a "short" cycle for consumer goods.

**Selection process**:

1. Score each factor using the table above
2. If majority point to one column, use that model type
3. If split, start with multi-touch (most versatile) and add complexity as data matures
4. Document the selection rationale before implementation -- revisit quarterly

### Single-Touch Models

| Model | Use when | Limitation |
| --- | --- | --- |
| First-click | Awareness is the primary constraint | Ignores conversion optimization |
| Last-click | Conversion optimization is the focus | Ignores awareness generation |

Route to single-touch only when the decision tree clearly points there. Default to multi-touch when uncertain.

### Multi-Touch Models

| Model | Credit distribution | Best for |
| --- | --- | --- |
| Linear | Equal to all touchpoints | No clear dominant touchpoint, exploratory phase |
| Time-decay | More credit to recent touchpoints | Short consideration cycles, recency matters |
| Position-based (U-shaped) | Common default: 40/40/20 first/last/middle -- adjust based on your data | Both awareness and conversion matter equally |
| W-shaped | Common default: 30/30/30/10 first/lead-creation/last/middle -- adjust based on your data | B2B with distinct lead creation moment |
| Algorithmic/data-driven | ML-based, varies by data | Large data volumes, mature analytics team |

**Multi-touch selection within the category**:

```
Do you have a distinct lead creation event (e.g., form fill, trial start)?
  YES --> W-shaped (if B2B) or Position-based (if B2C)
  NO  --> Is recency a strong signal in your conversion data?
            YES --> Time-decay
            NO  --> Do you have enough data for algorithmic modeling?
                      YES --> Algorithmic/data-driven
                      NO  --> Linear (safest default)
```

### MMM vs MTA Decision Framework

These are complementary, not competing. Use this framework to determine which to prioritize or how to combine them.

| Factor | Marketing Mix Modeling (MMM) | Multi-Touch Attribution (MTA) |
| --- | --- | --- |
| Data requirement | Aggregate (spend, revenue, external factors) | Individual-level (user journeys) |
| Time horizon | Long-term (12-24 months history needed) | Short-term (real-time or near) |
| Offline channels | Handles well (TV, radio, print, events) | Cannot track without workarounds |
| Digital channels | Coarse (channel-level) | Granular (campaign, ad, keyword) |
| Privacy impact | Low (no individual tracking) | High (requires user-level data) |
| Best for | Budget allocation across channels | Optimizing within digital channels |
| Update frequency | Quarterly or less | Continuous |

**Complementary use pattern**: MMM for channel-level budget allocation, MTA for within-channel optimization. When both are available, MMM sets the budget envelope per channel; MTA optimizes spend within each envelope.

**Selection when only one is feasible**:

```
Do you have significant offline media spend (TV, radio, print, events)?
  YES --> Start with MMM (MTA cannot capture offline impact)
  NO  --> Is user-level tracking available across your digital channels?
            YES --> Start with MTA (faster feedback loops)
            NO  --> Start with MMM (works with aggregate data)
```

### Attribution Model Migration Path

When moving from a simpler to more complex model:

1. Run the new model in parallel for 1-2 full sales cycles before switching
2. Compare outputs: where do the models agree? Where do they diverge?
3. Investigate divergences -- they reveal the channels being over/under-credited
4. Switch primary reporting only after stakeholder alignment on the new model's implications
5. Keep the old model available for comparison during the first quarter post-switch

## Measurement Plan Construction

Structured methodology for building a measurement plan from scratch. Follow all four steps in order; skipping steps produces incomplete plans.

### Step 1: KPI Hierarchy by Funnel Stage

| Funnel stage | Metric types | Metric name examples (never generate VALUES) |
| --- | --- | --- |
| Awareness | Reach, visibility | Impressions, reach, share-of-voice, brand recall |
| Consideration | Engagement, interest | Click-through rate, time on page, content downloads, email opens |
| Conversion | Action, acquisition | Conversion rate, CAC, cost per lead, pipeline influenced, deals created |
| Retention | Loyalty, expansion | Customer lifetime value, churn rate, NPS, expansion revenue |

NOTE: This table names metric TYPES as methodology. It never generates specific target VALUES or benchmarks. The customer establishes their own baselines from their own historical data.

**KPI selection process**:

1. Identify 1-2 primary metrics per funnel stage relevant to the campaign objective
2. Define leading indicators (predictive) and lagging indicators (outcome) for each
3. Establish which metrics the customer can actually track with current infrastructure
4. Remove any metric that cannot be reliably measured -- an unmeasurable KPI is worse than none

### Step 2: Attribution Window Selection

| Sales cycle | Recommended window | Rationale |
| --- | --- | --- |
| < 7 days | 7-14 days | Short consideration, recent touchpoints matter |
| 7-30 days | 30-60 days | Trial period + pre-trial research |
| 30-90 days | 60-90 days | Multiple stakeholders, longer evaluation |
| 90+ days | 90-180 days | Complex buying committees, long evaluation cycles |

Set the window BEFORE launching the campaign. Changing the attribution window mid-campaign invalidates comparisons.

### Step 3: Reporting Cadence Design

| Report type | Frequency | Audience | Focus |
| --- | --- | --- | --- |
| Campaign pulse | Weekly | Campaign managers | Leading indicators, spend pacing, anomaly detection |
| Performance review | Monthly | Marketing leadership | KPI trends, channel effectiveness, budget reallocation |
| Strategic review | Quarterly | CMO / exec team | ROI, attribution insights, budget recommendations |
| Annual analysis | Yearly | Board / C-suite | Year-over-year trends, strategic investment recommendations |

Each report type should have a defined template, owner, and distribution list before the campaign launches.

### Step 4: Baseline-Setting Methodology

How to establish baselines from YOUR data (not industry averages):

1. Collect 3-6 months of historical data per metric
2. Calculate mean and standard deviation for each metric
3. Set targets: baseline + improvement target based on investment level and historical variance
4. Track variance from YOUR baseline, not external benchmarks
5. Re-baseline annually or after significant business model changes

If historical data is unavailable: run a measurement-only period (no optimization changes) for 4-8 weeks to establish baselines before setting targets.

Document the measurement plan using the four steps above (KPI hierarchy, attribution window, reporting cadence, baselines) in a structured fill-in format your organization prefers.

## Campaign Analysis Methodology

Structured post-campaign analysis process. Follow all four steps sequentially.

### Step 1: Hypothesis Documentation

Before analysis, document:

```
CAMPAIGN ANALYSIS HYPOTHESIS:
  Objective:          [What was the campaign trying to achieve?]
  Expected outcome:   [What did we expect to happen, quantified?]
  Success metrics:    [Which specific metrics define success?]
  Success threshold:  [What level of each metric = success?]
  Time period:        [Campaign dates + attribution window]
```

Complete this BEFORE looking at results to prevent post-hoc rationalization.

### Step 2: Data Collection Checklist

| Element | Specify |
| --- | --- |
| Time period | Campaign start/end + attribution window extension |
| Data sources | Analytics platform, CRM, ad platforms, call tracking, etc. |
| Segments | Geographic, audience, channel, creative variants |
| Baseline | Pre-campaign period of equal length for comparison |
| Control group | If available, unexposed group for causal inference |

Flag any data source gaps: "Channel X data unavailable -- analysis excludes this channel."

### Step 3: Performance Decomposition

Systematic drill-down from overall to granular. At each level, compare against the hypothesis documented in Step 1.

**Overall**: Did the campaign meet its stated objectives? Yes / No / Partially -- with data.

**By channel**: Which channels drove results? Which underperformed relative to spend?

```
CHANNEL DECOMPOSITION:
  Channel:        [name]
  Spend:          [from customer data]
  Primary metric: [value from customer data]
  Cost per result: [calculated]
  vs. Baseline:   [% change from pre-campaign period]
  Assessment:     [Over/Under/At expected performance]
```

**By audience**: Which segments responded? Which did not? Any unexpected segments?

**By creative**: Which messaging or creative variants performed? Document the specific differences between variants -- not just "Creative A won" but what differed (headline, CTA, imagery, offer).

**By timing**: When did performance peak? Day-of-week patterns, time-of-day patterns, fatigue curves.

### Step 4: Insight Extraction

For each finding, document:

| Element | Content |
| --- | --- |
| Finding | What happened (data-backed, cite source and time period) |
| Confidence | High / Medium / Low (based on sample size and data quality) |
| Why it matters | Business impact quantified where possible |
| Recommended action | Specific, testable next step |
| Data needed to validate | What would confirm or refute this finding |

Separate findings into: confirmed (high confidence, sufficient data), directional (medium confidence, worth acting on with monitoring), and hypotheses (low confidence, requires further testing).

Structure post-campaign analysis using the hypothesis documentation, data checklist, performance decomposition, and insight extraction steps above.

## A/B Testing Framework

Experiment design methodology for marketing. Use this whenever designing tests of messaging, creative, channels, audiences, or offers.

### Hypothesis Structure

"If we [change], then [metric] will [direction] by [magnitude] because [rationale]."

All five elements are required. A hypothesis without a stated rationale is just a guess; a hypothesis without a magnitude makes it impossible to determine required sample size.

### Design Checklist

| Element | Requirement |
| --- | --- |
| Single variable | Only one thing differs between A and B |
| Success metric | Primary metric defined before launch |
| Guardrail metrics | Secondary metrics that must not degrade |
| Sample size | Calculated for statistical significance (use tools, do not guess) |
| Duration | Long enough for full business cycles (weekly patterns, paydays, seasonal) |
| Segmentation | Pre-define segments for post-hoc analysis (check for Simpson's paradox in segment-level results) |
| Minimum detectable effect | Smallest meaningful difference worth implementing |
| No early stopping | Do not stop or declare winners before planned sample size is reached |

For regulated industries: verify that test variants comply with industry-specific content requirements (pharma MLR approval, financial FINRA review, healthcare HIPAA considerations) before launching experiments.

### Result Interpretation

| Outcome | Action |
| --- | --- |
| Statistically significant + meaningful effect size | Implement winner, document learning |
| Statistically significant + trivial effect size | Consider operational cost of change vs. gain |
| Not significant + sufficient sample | No detectable difference -- test a bigger change |
| Not significant + insufficient sample | Extend test or increase traffic allocation |

### Test Prioritization

When multiple tests are possible, prioritize using:

```
PRIORITIZATION SCORE:
  Impact:     [High/Medium/Low] -- How much could this move the primary metric?
  Confidence: [High/Medium/Low] -- How strong is the rationale?
  Ease:       [High/Medium/Low] -- How quickly can this be implemented and measured?

  Priority = Impact x Confidence x Ease (High=3, Medium=2, Low=1)
  Run highest-scoring tests first.
```

## Funnel Diagnostics

Systematic approach to diagnosing funnel performance issues. Use when conversion rates are below expectations or declining.

### Diagnostic Process

**1. Map the funnel stages**

Define the customer's actual funnel (not a generic template). Common stages: awareness, consideration, conversion, retention -- but use the customer's terminology and stage definitions.

**2. Calculate stage-by-stage conversion rates from YOUR data**

Never use assumed or "typical" rates. If data is unavailable for a stage, flag it as a blind spot.

**3. Identify the biggest absolute drop-off**

Focus on the stage with the largest absolute volume loss, not just the lowest percentage. A 50% drop from 10,000 to 5,000 matters more than a 70% drop from 100 to 30.

**4. Diagnose the drop-off stage**

For each drop-off stage, investigate the matching causes:

- Awareness → Consideration drop : Review targeting criteria, messaging resonance, channel mix, proposal quality, sales follow-up speed
- Consideration → Conversion drop : Review landing pages, pricing presentation, social proof, CTA clarity, procurement friction, compliance barriers, budget approval process
- Conversion → Retention drop : Review onboarding flow, first-value time, churn surveys, implementation complexity, service delivery quality
- Declining previously stable stage : Compare to prior periods, check competitive landscape, audience freshness

**5. Formulate a hypothesis for root cause**

Use the same hypothesis structure as the A/B testing framework: "If [root cause], then [fixing it] will [improve metric] by [magnitude] because [rationale]."

**6. Design a specific, testable intervention**

Not "improve the landing page" but "change the headline from feature-focused to outcome-focused" or "add customer testimonials above the fold." Vague interventions produce uninterpretable results.

**7. Test the intervention**

Use the A/B testing framework above. If the intervention cannot be A/B tested (e.g., pricing change), use a before/after design with appropriate controls and caveats about confounding factors.

### Funnel Health Monitoring

Ongoing monitoring framework (not just one-time diagnosis):

| Check | Frequency | Alert trigger |
| --- | --- | --- |
| Stage conversion rates | Weekly | Define threshold based on your historical variance (e.g., 2+ standard deviations) |
| Funnel velocity (time between stages) | Weekly | Increasing trend over 3+ weeks |
| Stage volume | Weekly | Significant drop from prior period (define threshold based on your data) |
| Drop-off concentration | Monthly | Single stage accounts for > 50% of total funnel loss |

## Templates

- Campaign analysis template -- pull in when analysing campaign performance
- Measurement plan template -- pull in when creating a measurement plan

Store these templates as a companyRAG collection or upload them as files so the skill builds on them consistently.

## Guardrails

- Never generate benchmark data, conversion rates, or industry averages. Naming metric types (CAC, pipeline velocity) is methodology; generating specific values is fabrication.
- Always cite the specific data source and time period when analysing campaigns. Default to "insufficient data to determine" rather than speculating.
- Human verification required for budget allocation recommendations, attribution model changes, and KPI target setting.
- Flag outputs: [From customer data] for sourced data · [Framework methodology] for this skill's approach · [AI analysis] for model synthesis. Use [High/Medium/Low confidence] ratings.

> **Tip:** The skill does not run queries itself — it analyses the data you provide. Ask for XLSX, PPTX, or Markdown output via companyFILES to get a formatted, instantly shareable report.
