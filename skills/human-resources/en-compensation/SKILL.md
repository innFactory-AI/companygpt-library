---
name: en-compensation
description: Review compensation decisions against internal bands and EU Pay Transparency Directive requirements. Use when making an offer, processing a salary adjustment, or auditing pay equity. Trigger with "check comp for", "is this offer in band", "pay equity review".
---

# Compensation Skill

Review compensation decisions against internal salary bands, calculate compa-ratios, audit pay equity, and assess EU Pay Transparency Directive readiness. All compensation data comes from you, a connected MCP source, or companyRAG collections.

## Employment Law & Regulatory Disclaimer

Compensation decisions intersect employment law, anti-discrimination regulations, and emerging pay transparency requirements across EU member states. All outputs are decision-support tools for compensation professionals — this does not constitute legal or financial advice.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **HRIS via MCP** (e.g. Personio, Workday, BambooHR) | Current compensation by component, employee master data, role, level, tenure, location, demographic data |
| **Compensation-benchmark sources via MCP** (e.g. salary surveys, market data providers) | Market data and survey percentiles, where connected and released |
| **companyRAG / file upload** | Salary band structure, job architecture, compensation framework, governance policies |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Compensation Review Workflow

Follow these steps for every compensation review request. Adapt depth to context — a routine hire-in-band check needs less rigour than a full equity audit.

### Step 1: Gather Compensation Data

Collect the relevant data points before analysis:

**For an individual compensation decision (offer, adjustment, promotion):**

| Data Point | Source | Required? |
| --- | --- | --- |
| Role title and job level | Job architecture / user input | Yes |
| Proposed compensation (base, variable, equity) | User input | Yes |
| Internal salary band for the role and level | Compensation framework / user input | Yes |
| Current compensation (for adjustments) | HRIS / user input | If adjustment |
| Relevant market data / survey percentile | Compensation survey / user input | Recommended |
| Location / geography zone | User input | Yes |
| Experience level relative to role requirements | User input | Recommended |

**For a team or organisational equity audit:**

| Data Point | Source | Required? |
| --- | --- | --- |
| Employee roster with role, level, tenure, location | HRIS / user input | Yes |
| Current compensation by component (base, variable, equity) | HRIS / user input | Yes |
| Salary band structure | Compensation framework / user input | Yes |
| Demographic data for equity analysis | HRIS / user input | For equity audit |
| Recent compensation actions (raises, promotions) | HRIS / user input | Recommended |

If key data is missing, flag it explicitly: [Data needed — ask user]. Do not proceed with assumptions about band structures or compensation amounts.

### Step 2: Band Alignment Check

For the proposed or current compensation, assess alignment against the internal band:

```
BAND ALIGNMENT CHECK:
  Role:          [title and level]
  Location zone: [geography zone]
  Band minimum:  [from compensation framework]
  Band midpoint: [from compensation framework]
  Band maximum:  [from compensation framework]
  Proposed comp: [amount]

  Position in band: [below min / lower third / mid-range / upper third / above max]
  Band penetration: [percentage — (proposed - min) / (max - min) × 100]

  Assessment:    [In band / Below band / Above band]
  Flag:          [None / Requires justification / Requires approval]
```

**Band alignment interpretation:**

| Position | Typical Interpretation | Action |
| --- | --- | --- |
| Below band minimum | Under-market or mislevelled | Investigate — may need adjustment or re-levelling |
| Lower third (0–33%) | New-to-role or developing | Appropriate for new hires or recent promotions growing into the role |
| Mid-range (34–66%) | Fully performing at level | Standard positioning for experienced, fully performing employees |
| Upper third (67–100%) | Senior in role / high performer | Appropriate for tenured, high-impact employees — monitor for promotion readiness |
| Above band maximum | Over-market or mislevelled | Requires review — consider re-levelling, role expansion, or market data refresh |

### Step 3: Compa-Ratio Analysis

Calculate the compa-ratio for individual or group analysis:

```
COMPA-RATIO:
  Individual:    Actual base salary / Band midpoint × 100
  Target range:  80–120% (typical — adjust to your organisation's policy)

  Result:        [calculated]%
  Assessment:    [Below target / On target / Above target]
```

**For team or group analysis:**

| Metric | Calculation | What It Reveals |
| --- | --- | --- |
| Average compa-ratio | Mean of individual compa-ratios | Overall team positioning vs. midpoint |
| Compa-ratio range | Min to max within the group | Spread of compensation within the same level |
| Compa-ratio by tenure | Segmented by years in role | Whether tenure correlates with band position (expected) |
| Compa-ratio by demographic | Segmented by protected characteristics | Potential pay equity concerns (see Step 4) |

A healthy compa-ratio distribution clusters around 95–105% with intentional variation based on experience, performance, and tenure. Outliers in either direction warrant investigation.

### Step 4: Pay Equity Check

Systematic assessment for pay equity risks. This is a SCREENING methodology — confirmed equity issues require statistical analysis by qualified compensation analysts and review by employment counsel.

**Individual decision equity screen:**

When reviewing an offer or adjustment, check:

1. Internal equity: How does this compare to others in the same role, level, and location zone? Are there unexplained differences?
2. Cohort comparison: Among employees at the same level and tenure band, where does this fall? Is the position justified by performance, experience, or scope differences?
3. Historical pattern: For this specific team or manager, is there a pattern in how offers or adjustments trend across demographic groups?

**Organisational equity audit methodology:**

1. Define the audit scope: which roles, levels, locations, and time period
2. Group employees into comparable cohorts (same role family + level + location zone)
3. Calculate compa-ratio distributions within each cohort
4. Segment by available demographic dimensions (gender, ethnicity, age, disability status — per local data availability and privacy requirements)
5. Flag cohorts where the median compa-ratio differs by more than 5 percentage points across demographic groups
6. For flagged cohorts, assess whether legitimate factors (tenure, performance rating, scope differences) explain the gap
7. Residual unexplained gaps require deeper statistical analysis (regression-based) and legal review

> **CRITICAL**: Pay equity analysis using demographic data has significant privacy and data protection implications. Reference the data processing requirements before proceeding. Works council or employee representative consultation may be required before conducting equity analyses in some jurisdictions.

### Step 5: EU Pay Transparency Directive Awareness

The EU Pay Transparency Directive (2023/970) introduces requirements that member states must transpose into national law by June 2026. Requirements vary by organisation size and member state transposition.

**Awareness checklist — assess readiness for:**

| Requirement Area | Key Obligations | Readiness Question |
| --- | --- | --- |
| Pay band disclosure | Provide salary range in job postings or before interview | Are salary bands defined and publishable for all roles? |
| Right to information | Employees can request average pay by gender for their category | Can you produce this data on request? |
| Pay gap reporting | Organisations above threshold report gender pay gap data | Do you have the data infrastructure for annual reporting? |
| Joint assessment | If gap > 5% and not justified, conduct joint assessment with worker representatives | Is there a process for conducting joint assessments? |
| Ban on pay history | Cannot ask candidates about current or prior compensation | Are interview processes and offer workflows updated? |

> **CRITICAL**: This checklist provides AWARENESS of directive themes. National transposition may differ significantly in scope, thresholds, and implementation timelines. Verify specific requirements with employment counsel in each applicable member state.

## Output Template: Compensation Review

```
# Compensation Review — [Role / Employee ID / Team]
Date: [date]
Reviewer: [name]
Review type: [Offer / Adjustment / Promotion / Equity audit]

## Summary
  [2-3 sentences: what was reviewed, key finding, recommended action]

## Band Alignment
  [Band alignment check output from Step 2]

## Compa-Ratio Analysis
  [Compa-ratio output from Step 3]

## Pay Equity Screen
  [Equity screen findings from Step 4]
  Risk level: [Low / Medium / High / Requires specialist review]

## EU Pay Transparency Readiness (if applicable)
  [Checklist status from Step 5]

## Recommendation
  [Structured recommendation — approve as-is / approve with modification / escalate]
  Justification: [evidence-based rationale]
  Approval level: [manager / compensation team / CHRO — per your governance policy]

## Flags and Next Steps
  - [Any items requiring follow-up, data gaps, or specialist review]
```

## CUSTOMIZE: Adapting to Your Organisation

This skill uses generic band structures and thresholds. To make it organisation-specific:

1. Upload your salary band structure to a companyRAG collection — the skill will reference your bands instead of asking each time
2. Define your compa-ratio target range if it differs from the 80–120% default
3. Specify your approval thresholds — which band positions or compa-ratios require escalation
4. Add your geography zones and how they map to band differentials
5. Include your equity audit cadence and methodology if you have an established process

## Guardrails

- Never generate salary amounts, market benchmarks, or compensation survey data. All compensation figures must come from the user's data.
- Never state that a compensation decision is "compliant" or "legal." Compliance determination requires legal counsel — flag: "Verify with employment counsel in [jurisdiction]."
- Never make individual pay equity determinations. Equity analysis requires statistical methodology and legal review beyond this skill's scope.
- Source-label all output: `[From compensation data]`, `[Framework methodology]`, or `[AI analysis — verify with compensation team]`.

> **Tip:** Ask for XLSX, DOCX, or Markdown output via companyFILES to get a formatted, instantly shareable review.
