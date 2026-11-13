---
name: en-forecast
description: Build a weighted revenue forecast with risk flags, commit recommendations, and gap-to-quota analysis. Use when preparing for a forecast call, evaluating end-of-quarter projections, or assessing pipeline coverage. Trigger with "build forecast", "forecast for this quarter", "where do I stand against quota".
---

# Forecast Skill

Transform pipeline data into weighted projections with risk assessment, commit-category recommendations, and gap-to-quota action plans. All pipeline data, quota targets, and historical performance comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce, Dynamics) | Pipeline deals, stages, values, close dates, activity history |
| **companyRAG collections** | Past forecast accuracy, seasonal patterns, win-rate data |
| **File upload (CSV/XLSX)** | Pipeline export, quota targets, deal-level confidence, context not in the CRM |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Forecasting Workflow

```
1. PULL pipeline data
   |
   +--> All open opportunities for the forecast period
   +--> Include: deal name, value, stage, close date, age, last activity, owner
   +--> Flag deals with close dates in the past (slipped deals)
   +--> Flag deals with no activity in the last 14 days
   |
2. CATEGORISE each deal
   |
   +--> Apply forecast categories (see Category Framework below)
   +--> For each deal, document the rationale for category assignment
   +--> Flag category disagreements between CRM stage and assessed confidence
   |
3. WEIGHT by probability
   |
   +--> Apply stage-based or assessed probability (see Weighting Methodology below)
   +--> Calculate weighted value per deal
   +--> Sum by category for category-level totals
   |
4. FLAG risks
   |
   +--> Apply risk criteria to every deal (see Risk Flagging below)
   +--> Classify risk severity: High / Medium / Low
   +--> Deals with High risk get downgraded one category or flagged for review
   |
5. CALCULATE gap-to-quota
   |
   +--> Compare weighted forecast to quota target
   +--> Identify gap (or surplus) at commit level and best-case level
   +--> Assess pipeline coverage (see Coverage Analysis below)
   |
6. RECOMMEND actions
   |
   +--> For forecast gaps: identify most movable deals to close the gap
   +--> For at-risk deals: recommend specific actions to de-risk
   +--> For coverage shortfalls: flag pipeline-generation need with urgency
   |
7. COMPILE forecast output (see Output Template below)
```

## Forecast Category Framework

Assign each deal to exactly one category based on evidence, not optimism:

| Category | Definition | Evidence Required |
| --- | --- | --- |
| **Closed Won** | Signed, booked, or verbally committed with written confirmation | Contract executed or PO received |
| **Commit** | High confidence of closing this period — specific evidence of buyer commitment | Verbal commitment + defined paper process + agreed timeline within period |
| **Best Case** | Realistic chance of closing this period — deal is progressing but commitments are soft | Active engagement + budget confirmed + decision-maker involved + timeline plausible |
| **Pipeline** | In active sales process but unlikely to close this period | Qualified opportunity with activity but missing commitment signals |
| **Omit** | Stale, disqualified, or placeholder deals that should not appear in the forecast | No activity >30 days, or missing fundamental qualification criteria |

### Category Assignment Decision Tree

```
Deal in CRM for this period
  |
  +--> Contract signed or PO received?
  |      YES --> CLOSED WON
  |
  +--> Buyer has verbally committed + paper process defined + timeline in period?
  |      ALL YES --> COMMIT
  |      SOME YES --> Check: which elements are missing?
  |                   +--> Missing verbal commitment --> BEST CASE at most
  |                   +--> Missing paper process --> BEST CASE (risk: procurement delay)
  |                   +--> Timeline slipping beyond period --> PIPELINE or BEST CASE
  |
  +--> Active engagement + budget confirmed + decision-maker involved?
  |      ALL YES + timeline plausible --> BEST CASE
  |      SOME YES --> PIPELINE
  |
  +--> Qualified but early-stage or timeline is next period+?
  |      YES --> PIPELINE
  |
  +--> No meaningful activity in >30 days or fundamental qualification gaps?
         YES --> OMIT (flag for pipeline cleanup)
```

## Weighting Methodology

Two approaches — use whichever the customer's data supports:

### Stage-Based Weighting

Derive probabilities from the customer's own historical close rates per stage. Never prescribe probabilities.

| Step | Action |
| --- | --- |
| 1 | Pull historical closed-won and closed-lost deals for the last 4+ quarters |
| 2 | Calculate win rate per stage: deals that entered stage X and eventually closed-won / total that entered stage X |
| 3 | Apply derived rate to current pipeline: weighted value = deal value × stage probability |
| 4 | Adjust for known biases: if reps consistently over-forecast from a specific stage, apply a haircut factor derived from recent accuracy data |

### Assessed-Confidence Weighting

When historical data is insufficient or deal characteristics vary too widely:

| Step | Action |
| --- | --- |
| 1 | For each deal, the rep (or AI based on CRM signals) assigns a confidence percentage |
| 2 | Confidence must be justified with specific evidence, not gut feel |
| 3 | Weighted value = deal value × assessed confidence |
| 4 | Compare rep-assessed vs. stage-based probability — large divergence flags either data quality or deal-specific insight |

**Never prescribe conversion rates, stage probabilities, or benchmark percentages.** Always derive from the customer's own data or flag as "[Assumed — calibrate from historical data]."

## Risk Flagging

Apply these criteria to every deal in the forecast. A deal can carry multiple risk flags:

| Risk Factor | Trigger Condition | Severity |
| --- | --- | --- |
| **No next step** | No defined, agreed next action with a date | High |
| **Single-threaded** | Only one contact engaged; no multi-threading | High |
| **Close date slipped** | Close date pushed back one or more times this quarter | High |
| **Stale engagement** | No meaningful activity (email, call, meeting) in >14 days | High |
| **Missing economic buyer** | No interaction with budget authority | Medium |
| **Competitive threat** | Active competitor evaluation without clear differentiation plan | Medium |
| **Champion risk** | Champion changed roles, went silent, or left the company | High |
| **Paper process undefined** | No clarity on procurement steps, contract review, or legal timeline | Medium |
| **Value misalignment** | CRM deal value has not been validated with the buyer | Medium |
| **Late-stage qualification gap** | Deal in late stage but MEDDPICC/BANT elements scored low | High |

### Risk-to-Action Mapping

| Severity | Forecast Impact | Recommended Action |
| --- | --- | --- |
| **High** | Downgrade one category or flag for override | Immediate rep action required; include in forecast call notes |
| **Medium** | Discount weighted value by a factor the customer defines | Add to weekly deal-review agenda; assign specific follow-up |

## Gap-to-Quota Analysis

```
QUOTA TARGET for period: [Q]

COMMIT total (weighted): [C]
BEST CASE total (weighted): [B]
PIPELINE total (weighted): [P]

GAP at Commit level: Q - C = [Gap or Surplus]
GAP at Best Case level: Q - (C + B) = [Gap or Surplus]

COVERAGE RATIO:
  Total active pipeline value / Q = [X]x coverage
  Weighted pipeline / Q = [Y]x weighted coverage

  Compare to customer's historical coverage-to-close ratio:
    ABOVE historical ratio --> Coverage is adequate (but verify deal quality)
    AT historical ratio --> On track, minimal margin for slippage
    BELOW historical ratio --> Coverage gap — pipeline generation urgency
```

## Coverage Analysis

Pipeline coverage contextualised to the customer's reality:

| Factor | Assessment |
| --- | --- |
| **Raw coverage** | Total pipeline value / quota target |
| **Weighted coverage** | Weighted pipeline value / quota target |
| **Quality-adjusted coverage** | Remove omit-category and high-risk deals, recalculate |
| **Time-adjusted coverage** | Weight deals by alignment of close date to period end |
| **Source mix** | Breakdown of pipeline by source (inbound, outbound, expansion, partner) — over-reliance on one source is a coverage risk |

## Output Template: Forecast Summary

```
# Revenue Forecast: [Period]
**Prepared**: [Date]  |  **Quota**: [Target]
**Forecast Method**: [Stage-based / Assessed-confidence / Blended]

## Forecast by Category
| Category     | Deal Count | Total Value   | Weighted Value | % of Quota  |
| ------------ | ---------- | ------------- | -------------- | ----------- |
| Closed Won   | [N]        | [Value]       | [Value]        | [%]         |
| Commit       | [N]        | [Value]       | [Weighted]     | [%]         |
| Best Case    | [N]        | [Value]       | [Weighted]     | [%]         |
| Pipeline     | [N]        | [Value]       | [Weighted]     | [%]         |
| **Total**    | [N]        | [Value]       | [Weighted]     | [%]         |

## Gap Analysis
- **Commit Gap**: [Quota] - [Commit weighted] = [Gap/Surplus]
- **Best-Case Gap**: [Quota] - [Commit + Best Case weighted] = [Gap/Surplus]
- **Coverage Ratio**: [X]x raw | [Y]x weighted | [Z]x quality-adjusted

## Risk Report
| Deal          | Value   | Category   | Risk Flags     | Severity | Recommended Action |
| ------------- | ------- | ---------- | -------------- | -------- | ------------------ |
| [Deal name]   | [Value] | [Category] | [Flags]        | [H/M]    | [Specific action]  |

## Deals Most Likely to Move (Gap-Closing Opportunities)
| Deal          | Value   | Current Category | What's Needed to Advance      | Probability of Advancing |
| ------------- | ------- | ---------------- | ----------------------------- | ------------------------ |
| [Deal name]   | [Value] | [Category]       | [Specific blocker to resolve] | [Based on evidence]      |

## Pipeline Generation Needs
- **Coverage status**: [Adequate / Thin / Critical]
- **Recommended new pipeline**: [Amount needed based on coverage gap and historical conversion]
- **Urgency**: [Based on days remaining in period and typical cycle length]

## Assumptions & Caveats
- [List every assumption made in building this forecast]
- [Flag data quality issues, missing historical baselines, or deals with insufficient information]
```

## Guardrails

1. Never generate pipeline data. All deal names, values, stages, and close dates must come from the user or CRM. If pipeline data is not provided, generate the forecast template with "[Pipeline data needed]" in each field.
2. Never prescribe conversion rates or probabilities. All stage probabilities, coverage ratios, and win rates must be derived from the customer's own historical data. If unavailable, flag as "[Historical baseline needed — using placeholder]."
3. Source labeling. Tag every assertion — [From CRM], [From user input], [From historical data], [AI assessment]. AI category recommendations must be flagged for rep validation.
4. Human judgment required. Include "This forecast is a decision-support tool. Category assignments and risk assessments require rep and manager validation before submission" on all outputs.

> **Tip:** Ask for XLSX output via companyFILES to get a formatted spreadsheet ready for distribution (DOCX or Markdown also available).
