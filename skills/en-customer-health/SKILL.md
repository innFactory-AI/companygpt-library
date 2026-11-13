---
name: en-customer-health
description: Assess account health across product usage, support history, and sentiment — flag churn risk with recommended next actions. Use when reviewing accounts, preparing for a CS team meeting, or identifying at-risk customers. Trigger with "score this customer", "account health check", "churn risk for [account]".
---

# Customer Health Skill

Assess account health across multiple dimensions, classify churn risk, and produce prioritised intervention plans. Account data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account metadata, contract dates, ARR, owner, lifecycle stage |
| **Support platform via MCP** (e.g. Zendesk, Intercom, Freshdesk) | Ticket volume, resolution time, CSAT scores, escalations |
| **Product analytics via MCP** (e.g. Amplitude, Mixpanel, Pendo, or internal) | Login frequency, feature adoption, usage trends |
| **companyRAG / file upload** | CSM notes, QBR records, survey results, uploaded exports |

> **No connected source?** Provide the data in chat or upload exports — and flag any dimension where data is missing. Never score without evidence.

## Health Scoring Workflow

Execute these steps in order for every health assessment.

### Step 1: Gather Account Signals

Collect data across six signal categories. For each signal, record the source and recency of the data point.

| Signal Category | Key Indicators | Source |
| --- | --- | --- |
| **Product Engagement** | Login frequency trend (30/60/90 day), feature adoption breadth, usage depth vs. licence capacity | Product analytics, CRM |
| **Support** | Ticket volume trend, average resolution time, escalation count, CSAT/satisfaction scores | Support platform |
| **Relationship** | Executive sponsor engagement, champion responsiveness, stakeholder coverage, meeting cadence | CRM, CSM notes |
| **Commercial** | Contract value trend, expansion history, on-time payment, renewal date proximity | CRM, billing |
| **Sentiment** | NPS/CSAT trend, qualitative feedback themes, social mentions if available | Surveys, CRM |
| **Outcomes** | Customer-reported ROI, goal attainment vs. success plan, business impact evidence | CSM notes, QBR records |

If a signal category has no data available, mark it as NO DATA and exclude it from the composite score. Note the gap prominently — missing data is itself a risk signal.

### Step 2: Score Each Dimension

Rate each dimension on a 1–5 scale using the behavioural anchors below.

| Score | Label | Definition |
| --- | --- | --- |
| **1** | Critical | Active disengagement or severe negative trend. Immediate intervention required. |
| **2** | At Risk | Declining trend or repeated negative signals. Proactive outreach needed within days. |
| **3** | Neutral | Stable but unremarkable. No clear positive or negative trajectory. Monitor closely. |
| **4** | Healthy | Positive trend across most indicators. Maintain current engagement cadence. |
| **5** | Thriving | Strong positive signals, expanding usage, vocal advocacy. Explore expansion opportunities. |

Apply these anchors per dimension:

**Product Engagement:**

- 1 = Usage dropped >50% vs. prior period or near-zero active users
- 3 = Stable usage, moderate feature adoption, no significant trend
- 5 = Growing usage, broad feature adoption, usage exceeds licence baseline

**Support:**

- 1 = High ticket volume with unresolved escalations, declining CSAT
- 3 = Normal ticket volume, acceptable resolution times, stable satisfaction
- 5 = Low ticket volume, fast resolution, high CSAT, self-service adoption

**Relationship:**

- 1 = Champion departed or unresponsive, no executive engagement, meetings cancelled
- 3 = Regular contact maintained, stable stakeholder map, adequate meeting cadence
- 5 = Multi-threaded relationships, executive sponsor actively engaged, proactive communication

**Commercial:**

- 1 = Contraction signals, payment issues, or customer has signalled non-renewal intent
- 3 = Flat contract, on-time payments, renewal not yet discussed
- 5 = Expansion history, early renewal signals, customer initiating growth conversations

**Sentiment:**

- 1 = Detractor NPS, negative qualitative feedback, unresolved complaints
- 3 = Passive NPS, neutral feedback, no strong signals either way
- 5 = Promoter NPS, positive testimonials, willing to be a reference

**Outcomes:**

- 1 = No evidence of value realisation, customer cannot articulate ROI
- 3 = Some goals met, partial ROI evidence, value narrative exists but not quantified
- 5 = Customer-reported ROI exceeds expectations, business goals achieved, internal case study material

### Step 3: Classify Overall Health

Calculate a weighted composite score. Default weights below — adjust based on what predicts churn in your customer base.

| Dimension | Default Weight | Rationale |
| --- | --- | --- |
| Product Engagement | 25% | Strongest leading indicator of retention |
| Support | 15% | Lagging but high-signal when negative |
| Relationship | 20% | Multi-threading is a proven churn buffer |
| Commercial | 15% | Direct revenue signal |
| Sentiment | 10% | Subjective but directionally valuable |
| Outcomes | 15% | Ties health to the customer's own goals |

**Composite score** = Σ (dimension score × weight)

Map the composite to a health classification:

| Composite Range | Classification | Colour | Meaning |
| --- | --- | --- | --- |
| 4.0–5.0 | Thriving | GREEN | Low churn risk. Focus on expansion and advocacy. |
| 3.0–3.9 | Stable | YELLOW | Moderate risk. Monitor trends and address any declining dimension. |
| 2.0–2.9 | At Risk | ORANGE | Elevated churn risk. Proactive intervention plan required. |
| 1.0–1.9 | Critical | RED | High churn risk. Escalate internally and engage immediately. |

**Override rules:**

- Any single dimension scored 1 → overall classification cannot be higher than YELLOW regardless of composite
- Product Engagement scored 1 or 2 AND Relationship scored 1 or 2 → automatic RED
- Missing data on 3+ dimensions → classify as ORANGE with a note that the score is unreliable

### Step 4: Identify Risk Factors

For each dimension scored 3 or below, document:

| Element | Content |
| --- | --- |
| **Signal** | The specific data point(s) driving the low score |
| **Trend** | Improving, stable, or declining over the last 30/60/90 days |
| **Root cause hypothesis** | What might be driving this signal (not a certainty — a hypothesis to investigate) |
| **Impact if unaddressed** | What happens to the account if this trend continues |
| **Confidence** | High / Medium / Low based on data quality and recency |

### Step 5: Recommend Next Actions

For each identified risk, recommend a specific, time-bound intervention.

| Risk Level | Response Timeframe | Action Type | Example |
| --- | --- | --- | --- |
| RED dimension | Within 48 hours | Executive outreach, internal escalation | CSM + manager joint call to champion; escalation brief to leadership |
| ORANGE dimension | Within 1 week | Proactive engagement, root cause discovery | Schedule a check-in focused on the specific risk area; prepare a value summary |
| YELLOW dimension | Within 2 weeks | Monitoring with light touch | Add to watch list; schedule a touchpoint; review at next team meeting |
| GREEN dimension | Standard cadence | Maintain and explore expansion | Continue regular engagement; identify expansion signals |

For each recommended action, specify: the action, the owner (CSM, manager, executive), the deadline, and the success indicator.

## Output Template — Health Scorecard

```
CUSTOMER HEALTH SCORECARD
Account: [name]
Date assessed: [date]
Assessed by: [CSM name]
Data sources: [list MCP sources, companyRAG collections, and manual inputs used]

OVERALL HEALTH: [GREEN / YELLOW / ORANGE / RED] — Composite: [X.X / 5.0]

DIMENSION SCORES:
  Product Engagement:  [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Support:             [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Relationship:        [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Commercial:          [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Sentiment:           [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]
  Outcomes:            [1-5] [▲▼—] [GREEN/YELLOW/ORANGE/RED]

  [▲ = improving trend | ▼ = declining trend | — = stable]

KEY RISKS:
  1. [Risk description] — [Dimension] — [Trend] — [Confidence]
     → Action: [specific intervention]
     → Owner: [name/role]
     → Deadline: [date]

  2. [Risk description] ...

EXPANSION SIGNALS:
  - [any positive signals indicating growth opportunity]

DATA GAPS:
  - [any dimensions with missing or stale data]

NEXT REVIEW DATE: [date]
```

## Health Scoring Reference Framework

### Leading vs. Lagging Indicators

Not all signals predict churn equally. Prioritise leading indicators for early intervention.

| Indicator Type | Examples | Predictive Value |
| --- | --- | --- |
| **Leading** (behaviour changes before churn) | Login frequency drop, feature adoption decline, champion disengagement, meeting cancellations | High — act on these early |
| **Coincident** (change alongside churn risk) | Support ticket spikes, NPS drop, payment delays | Medium — confirm with leading indicators |
| **Lagging** (appear after risk is established) | Non-renewal notice, explicit churn signal, competitive evaluation | Low predictive value — reactive territory |

### Trend Analysis

Always assess the direction of change, not just the current state. A score of 3 that was 5 last quarter is more concerning than a stable 3.

| Trend Pattern | Interpretation | Action Urgency |
| --- | --- | --- |
| Rapid decline (2+ points in one period) | Acute issue — something changed | Immediate investigation |
| Gradual decline (1 point over 2+ periods) | Slow disengagement — may be structural | Proactive within 1-2 weeks |
| Stable low (consistently 1-2) | Chronic issue — potentially normalised | Strategic review, consider escalation |
| Recovery (improving from low) | Intervention may be working | Continue current approach, validate |

## Guardrails

- Never fabricate usage data, ticket counts, NPS scores, or any account metric. If data is unavailable for a dimension, mark it as NO DATA — do not estimate.
- Never claim a specific churn probability. Health scores indicate risk level, not statistical probability. "RED" means "high risk requiring intervention," not "80% chance of churn."
- Health scores are decision-support inputs, not decisions. Always include: "Validate scores with the account team before acting on risk classifications."
- Source-label every assertion: `[From account data]`, `[From scoring framework]`, or `[CSM hypothesis]`. Flag per-dimension confidence (High / Medium / Low).

## Adapt Weights to Your Business

The default dimension weights above are starting points. To calibrate for your customer base:

1. Review historical churn data — which dimensions were lowest 90 days before churn events?
2. Look for correlations — which dimensions most strongly predict renewal outcomes?
3. Adjust weights — increase weight on dimensions that are most predictive in your data
4. Validate quarterly — re-review the correlation as your product and customer base evolve
5. Segment if needed — enterprise vs. mid-market vs. SMB may have different predictive signals

> **Tip:** Ask for XLSX output via companyFILES to get a formatted spreadsheet ready for distribution.
