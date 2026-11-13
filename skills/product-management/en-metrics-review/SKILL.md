---
name: en-metrics-review
description: Review product metrics with trend analysis, anomaly detection, and actionable recommendations. Use when preparing a product review, investigating a metric change, or setting up KPI tracking for a new feature. Trigger with "review product metrics", "why did [metric] change", "metrics dashboard review".
---

# Metrics Review Skill

Review product metrics, detect anomalies, diagnose root causes, and translate metric movements into actionable product decisions. All metric data comes from you, connected analytics tools, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Analytics tools via MCP** (e.g. Amplitude, Mixpanel, GA4) | Current and historical metric values, funnel data, segment breakdowns, event streams |
| **companyRAG collections** | Metric definitions, prior review documents, launch and incident notes, KPI targets |
| **File upload (CSV/XLSX exports)** | Dashboard exports, cohort tables, raw extracts from your analytics stack |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Metric Hierarchy Framework

Product metrics exist in a hierarchy. Understanding the hierarchy prevents reacting to symptoms while missing root causes.

### Hierarchy Structure

```
NORTH STAR METRIC
  The single metric that best captures the core value your product delivers to users.
  Changes slowly. Reflects cumulative product health.
  │
  ├── INPUT METRICS (3-5)
  │     Directly influence the North Star. Actionable by the product team.
  │     Changes on a weekly/monthly cadence. Each maps to a product lever.
  │     │
  │     ├── FEATURE METRICS
  │     │     Measure specific feature adoption, usage depth, and satisfaction.
  │     │     Changes on a daily/weekly cadence.
  │     │
  │     └── FUNNEL METRICS
  │           Measure conversion between key product stages.
  │           Changes on a daily/weekly cadence.
  │
  └── HEALTH METRICS (2-4)
        Must NOT degrade while optimising input metrics.
        Performance, reliability, support load, user sentiment.
```

### Hierarchy Construction Process

1. Identify the North Star : What single metric most directly measures whether your product is delivering its core value? Not revenue (that's a business metric) — the action or outcome that LEADS to revenue.
2. Map input metrics : What user behaviours directly drive the North Star? Each input metric should be actionable — the product team can design interventions that move it.
3. Add feature metrics : For each major feature or product area, what measures adoption (are users trying it?), engagement (are they using it meaningfully?), and retention (do they come back?).
4. Define health metrics : What must NOT break? Page load time, error rates, support ticket volume, NPS/CSAT. These are guardrails, not goals.

### Hierarchy Validation

A well-constructed hierarchy satisfies these checks:

| Check | Pass | Fail |
| --- | --- | --- |
| **Causal link** | Moving an input metric plausibly moves the North Star | Input metric is correlated but not causal |
| **Actionable** | The product team can design features/changes to move the input metric | Metric is influenced primarily by external factors |
| **Non-redundant** | Each input metric captures a distinct product lever | Two input metrics measure the same underlying behaviour |
| **Complete** | Together, input metrics cover the major pathways to the North Star | Important drivers are unrepresented |
| **Measurable** | The metric can be reliably tracked with current infrastructure | Data source is unavailable, unreliable, or prohibitively expensive |

## Metrics Review Workflow

### Step 1: Establish Review Context

Before examining any numbers, clarify:

- Review type : Routine cadence (weekly/monthly), ad-hoc investigation, or new feature launch review?
- Time window : What period is being reviewed? Include comparison period (prior period, year-over-year, or baseline).
- Scope : Full product, specific feature, specific segment, or specific metric?
- Known context : Any launches, incidents, marketing campaigns, seasonality, or external events in the review period?

### Step 2: Top-Down Metric Scan

Start at the North Star and work down the hierarchy:

```
METRIC SCAN — [Period]

North Star: [metric name]
  Current:   [value from user data]
  Prior:     [comparison value]
  Change:    [absolute and percentage]
  Trend:     [direction over last 3+ periods]
  Status:    On track / Below target / Above target / No target set

Input Metrics:
  [metric 1]: [current] vs [prior] → [change] — [status]
  [metric 2]: [current] vs [prior] → [change] — [status]
  ...

Health Metrics:
  [metric 1]: [current] vs [prior] → [change] — [status]
  ...
```

**Scan discipline**: Report the numbers before interpreting them. Humans anchor on the first narrative they hear — present data, then analysis.

### Step 3: Anomaly Detection

An anomaly is a metric movement that deviates meaningfully from its expected pattern. "Meaningful" is defined by the metric's own historical variance, not a universal threshold.

**Detection criteria**:

| Anomaly Type | How to Detect | Significance |
| --- | --- | --- |
| **Sudden shift** | Value jumps/drops by more than 2 standard deviations from the rolling mean | Likely caused by a discrete event — search for it |
| **Trend break** | Direction reversal sustained for 2+ periods after a consistent trend | May indicate a structural change — investigate root cause |
| **Divergence** | Input metric moves but North Star does not (or vice versa) | Suggests the hierarchy link is weaker than assumed — re-examine causal model |
| **Segment anomaly** | Overall metric is stable but a specific segment shows significant change | Hidden problem or opportunity — drill into segment data |
| **Seasonal deviation** | Metric departs from its historical seasonal pattern | Either a real change or a calendar artefact — compare year-over-year |

**Standard deviation calculation**: Use the metric's own trailing 8-12 period values to determine mean and standard deviation. This is metric-specific — never apply a universal threshold. If historical data is insufficient (< 8 periods), flag that anomaly detection is unreliable and use directional judgment.

### Step 4: Root Cause Analysis

For each flagged anomaly, apply the diagnostic framework:

#### 5-Why Decomposition

Start with the observed anomaly and ask "why" iteratively, following the metric hierarchy down:

```
ANOMALY: [Metric] changed by [amount] in [period]

Why 1: [First-level explanation — which input metric moved?]
Why 2: [What drove that input metric change?]
Why 3: [What user behaviour or system change caused that?]
Why 4: [What triggered that behaviour or system change?]
Why 5: [Root cause — the actionable thing that happened]

Confidence: [High / Medium / Low]
Evidence:   [What data supports this root cause?]
```

**Stop decomposing when** you reach an actionable factor the product team can influence. If the root cause is "competitor launched a better feature," the next step is response planning, not further decomposition.

#### Cause Category Checklist

When diagnosing, check these categories systematically:

| Category | Check | Common Signals |
| --- | --- | --- |
| **Product change** | Was anything shipped in this period? | Timing correlation with deployment |
| **Bug / incident** | Were there errors, downtime, or degraded performance? | Error rate spike, support ticket increase |
| **Traffic change** | Did traffic volume or source mix change? | Marketing campaign, press mention, SEO shift |
| **Segment shift** | Did the user mix change? | New customer cohort, geographic expansion, churn in specific segment |
| **Seasonality** | Is this a known seasonal pattern? | Year-over-year comparison matches |
| **External event** | Market event, competitor action, regulatory change? | Timing correlation with external event |
| **Measurement change** | Did tracking, definitions, or tooling change? | Sudden clean break in data (not gradual) |

**Critical check**: Always verify whether a measurement change explains the anomaly BEFORE assuming a real product change. Tracking bugs, definition changes, and analytics tool updates are common false-alarm sources.

### Step 5: Formulate Response

For each confirmed anomaly with a diagnosed root cause, determine the response:

| Root Cause Type | Response Pattern |
| --- | --- |
| **Bug / incident** | Fix the bug. Quantify impact window. Add monitoring to prevent recurrence. |
| **Product change caused regression** | Assess severity. Roll back or fast-follow fix. Update feature metrics. |
| **Product change worked as intended** | Celebrate. Document the winning pattern. Consider amplifying. |
| **Segment shift** | Assess whether the shift is desirable. Adjust targeting or product priorities. |
| **Competitive / external** | Reference the brief-competitor skill. Assess strategic response. |
| **Seasonality** | Note for future planning. No product response needed. |
| **Measurement issue** | Fix tracking. Restate historical data. Communicate correction to stakeholders. |

### Response Output Format

```
METRIC REVIEW SUMMARY — [Period]

HEADLINE: [One-sentence summary of the review — the single most important finding]

METRICS OVERVIEW:
  [Top-down scan from Step 2]

ANOMALIES DETECTED: [count]
  1. [Metric]: [change] — Root cause: [explanation] — Confidence: [H/M/L]
     Recommended action: [specific action with owner]
  2. ...

POSITIVE TRENDS:
  [Metrics moving in the right direction — acknowledge wins]

AREAS TO WATCH:
  [Metrics not yet anomalous but trending toward concern]

RECOMMENDATIONS:
  1. [Action] — Owner: [name] — Priority: [High/Medium/Low] — Timeline: [when]
  2. ...

OPEN QUESTIONS:
  [Anomalies without clear root cause — assigned for further investigation]
```

## New Feature Metric Setup

When launching a new feature, define metrics BEFORE launch using this framework:

1. Adoption metric : What % of eligible users try the feature? (Measures awareness and first-use friction)
2. Activation metric : What % of users who try the feature complete the core action? (Measures whether the feature delivers on its promise)
3. Engagement metric : How frequently or deeply do activated users use the feature? (Measures ongoing value)
4. Retention metric : Do users who adopt the feature return? At what cadence? (Measures sustained value)
5. Impact metric : Does feature usage correlate with improvement in the relevant input metric? (Validates the product hypothesis)

```
FEATURE METRIC PLAN — [Feature Name]
  Adoption:    [metric definition, measurement source]
  Activation:  [metric definition, measurement source]
  Engagement:  [metric definition, measurement source]
  Retention:   [metric definition, measurement source]
  Impact:      [metric definition, measurement source]
  Baseline:    [to be established in first 2 weeks post-launch]
  Review date: [when to first assess — typically 2-4 weeks post-launch]
```

## Guardrails

- NEVER generate metric values, benchmarks, or industry averages. All numbers must come from the user, analytics tools, or a companyRAG collection.
- NEVER fabricate root causes. When cause is unknown, state "Root cause not determined — requires further investigation" and assign a research task.
- NEVER claim causal relationships without evidence. Correlation is a hypothesis unless confirmed by experiment or clear mechanism. Always check whether a measurement/tracking change explains an anomaly before attributing it to real product behaviour.
- Source-label every element as `[From user/analytics data]`, `[Metrics framework]`, or `[AI analysis — verify]`.

> **Tip:** Ask for XLSX, DOCX, or Markdown output via companyFILES to get a formatted review document ready to share.
