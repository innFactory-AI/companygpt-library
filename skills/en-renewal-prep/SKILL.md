---
name: en-renewal-prep
description: Prepare renewal strategy — identify expansion or churn risk factors, draft a renewal conversation guide with recommended pricing approach. Use when a renewal is 60-90 days out, reviewing renewal pipeline, or preparing for a renewal negotiation. Trigger with "prep renewal for", "renewal strategy for [account]", "renewal risk assessment".
---

# Renewal Prep Skill

Prepare renewal briefs that combine a risk assessment, a conversation guide, and a recommended pricing approach. Account data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Contract terms, ARR, renewal date, expansion history, stakeholder contacts |
| **Billing via MCP** (e.g. Stripe, Chargebee) | Payment history, current pricing, usage-based billing data |
| **companyRAG / file upload** | QBR notes, success-plan metrics, support summaries, prior renewal records |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Renewal Preparation Workflow

Begin this workflow 60–90 days before the renewal date. Earlier for strategic accounts; later is acceptable for auto-renewing contracts with low risk.

### Step 1: Review Account Health

Pull or generate a current health score using the **en-customer-health**. If a recent score exists, review it. If not, run a fresh assessment.

Key health dimensions for renewal context:

| Dimension | Renewal Relevance |
| --- | --- |
| **Product Engagement** | Declining usage is the strongest predictor of non-renewal |
| **Support** | Unresolved escalations create negotiation leverage for the customer |
| **Relationship** | Champion departure or executive disengagement signals risk |
| **Sentiment** | NPS trend indicates willingness to renew and expand |
| **Outcomes** | Documented ROI is the strongest argument for renewal and expansion |

### Step 2: Assess Risk Factors

Evaluate each risk category and classify as High / Medium / Low.

| Risk Category | High Risk Indicators | Medium Risk Indicators | Low Risk Indicators |
| --- | --- | --- | --- |
| **Usage** | Declining usage, low adoption vs. licence, key features unused | Stable but flat usage, moderate adoption | Growing usage, high adoption, expanding use cases |
| **Relationship** | Champion left, executive disengaged, stakeholder map thin | Champion stable but not expanding, limited multi-threading | Strong multi-threading, executive sponsor engaged |
| **Support** | Open escalations, high ticket volume, declining CSAT | Moderate ticket volume, resolved escalations | Low ticket volume, high CSAT, self-service adoption |
| **Commercial** | Payment delays, budget constraints communicated, competitive evaluation | Flat budget, no expansion signals, price sensitivity mentioned | On-time payments, expansion interest, budget confirmed |
| **Value** | No documented ROI, customer cannot articulate value | Some ROI evidence but not quantified, partial goal achievement | Strong ROI documented, goals exceeded, internal case study |
| **Market** | Customer undergoing M&A, leadership change, industry downturn | Some organisational change, budget reviews underway | Stable organisation, growing business, strategic alignment |

**Overall renewal risk** = highest individual risk category. Any single High Risk factor can derail a renewal regardless of other dimensions.

### Step 3: Identify Expansion Opportunities

Look for signals that indicate the customer may be ready to expand.

| Expansion Signal | Evidence Required | Expansion Type |
| --- | --- | --- |
| Usage approaching or exceeding licence limits | Usage data vs. contract capacity | Licence uplift |
| New departments or teams expressing interest | Customer request, CSM observation | Seat expansion |
| Customer requesting features in higher tiers | Support tickets, feature requests | Tier upgrade |
| New use cases emerging beyond original scope | Usage patterns, customer conversations | Product cross-sell |
| Customer's business growing (headcount, revenue) | Public data, customer communication | Organic expansion |
| Positive ROI enabling budget justification | QBR data, success plan metrics | Value-based upsell |

### Step 4: Draft Renewal Strategy

Based on risk and opportunity assessment, select a strategy posture.

| Scenario | Strategy Posture | Focus |
| --- | --- | --- |
| Low risk + expansion signals | **Expand** | Lead with value delivered, propose expanded scope, anchor on ROI |
| Low risk + no expansion signals | **Secure** | Confirm value, lock in multi-year if appropriate, maintain momentum |
| Medium risk + any expansion | **Stabilise then expand** | Resolve risk factors first, demonstrate value, then introduce expansion |
| Medium risk + no expansion | **Defend** | Focus on retention, address concerns, build a recovery plan |
| High risk + any | **Recover** | Full attention on risk mitigation, executive engagement, value reinforcement |

### Step 5: Prepare Conversation Guide

Structure the renewal conversation based on the strategy posture.

**Conversation Framework:**

1. **Open with value** — Lead with specific outcomes the customer has achieved. Reference QBR data, success plan metrics, or ROI evidence. Never open with pricing.
2. **Acknowledge the relationship** — Reference specific milestones, challenges overcome, and partnership moments. Demonstrate that you know this account.
3. **Address known concerns** — Proactively raise any issues you know about rather than waiting for the customer to surface them. This builds trust and controls the narrative.
4. **Present the renewal proposal** — Based on your strategy posture:   - Expand: "Based on what you've achieved, here's how we can help you do more..."   - Secure: "We'd love to continue this partnership. Here's what renewal looks like..."   - Defend: "We know there have been challenges. Here's our plan to address them and what we're committing to..."   - Recover: "We hear your concerns. Before we discuss renewal, let's align on what needs to change..."
5. **Handle objections** — Prepare responses for the most likely objections based on your risk assessment.
6. **Agree on next steps** — Never end a renewal conversation without a clear, time-bound next step.

**Common Objections and Preparation:**

| Objection Type | Preparation Required |
| --- | --- |
| "We're not seeing enough value" | ROI evidence, usage data, outcome metrics — prepare before the call |
| "Budget is tight / we need to cut" | Cost of switching analysis, efficiency gains, essential vs. nice-to-have framing |
| "We're evaluating alternatives" | Competitive positioning (use a battlecard skill from the sales pack, if available), switching cost analysis, unique value differentiators |
| "We need a discount" | Value justification, multi-year incentive options, scope adjustment options |
| "Our champion left" | Re-engage with new stakeholders early, rebuild the value narrative for the new audience |

## Output Template — Renewal Brief

```
RENEWAL BRIEF
Account: [name]
ARR: [current value]
Renewal date: [date]
Days to renewal: [number]
Prepared by: [CSM name]
Date: [date]

ACCOUNT HEALTH SUMMARY:
  Overall health: [GREEN / YELLOW / ORANGE / RED]
  Key scores: Product [X/5], Support [X/5], Relationship [X/5],
              Commercial [X/5], Sentiment [X/5], Outcomes [X/5]

RISK ASSESSMENT:
  Overall risk: [High / Medium / Low]
  Usage risk:        [H/M/L] — [brief evidence]
  Relationship risk: [H/M/L] — [brief evidence]
  Support risk:      [H/M/L] — [brief evidence]
  Commercial risk:   [H/M/L] — [brief evidence]
  Value risk:        [H/M/L] — [brief evidence]
  Market risk:       [H/M/L] — [brief evidence]

EXPANSION OPPORTUNITIES:
  1. [opportunity] — [evidence] — [estimated value]
  2. ...
  (or: No expansion signals identified at this time)

STRATEGY: [Expand / Secure / Stabilise then Expand / Defend / Recover]
  Rationale: [why this posture]

VALUE EVIDENCE:
  - [specific outcome or metric the customer has achieved]
  - [specific outcome or metric]
  - ...

CONVERSATION GUIDE:
  Opening: [value-led opening tailored to this account]
  Concerns to address: [list known concerns with prepared responses]
  Proposal: [renewal terms to propose — flat, expansion, multi-year, etc.]
  Likely objections: [top 2-3 with prepared responses]
  Ask: [specific next step to propose at end of conversation]

INTERNAL ALIGNMENT:
  CSM: [name]
  Account executive: [name, if involved in renewal]
  Executive sponsor: [name, if executive engagement needed]
  Pre-renewal actions: [any internal steps before the customer conversation]
```

## CUSTOMIZE — Adapt to Your Renewal Motion

- Auto-renewing contracts : Focus the workflow on risk detection and expansion opportunity — the renewal itself is automatic, but churn risk remains.
- Usage-based pricing : Replace fixed ARR analysis with usage trend analysis and projected billing.
- Multi-year renewals : Start the workflow 120–180 days out instead of 60–90.
- Channel/partner renewals : Add a partner alignment step between Steps 4 and 5.
- High-volume / tech-touch renewals : Focus risk scoring (Step 2) on health score data and concentrate manual effort on High and Medium risk accounts only.

## Guardrails

- Never fabricate contract values, renewal dates, pricing, or usage data. All commercial data must come from the user, CRM, or billing system.
- Never generate specific discount recommendations or pricing numbers. This skill structures the approach; your pricing team provides the numbers.
- Never assume the customer's budget situation or competitive landscape. Ask; do not infer.
- Source-label every assertion : [From account data] , [From renewal framework] , or [CSM assessment] .

> **Tip:** Ask for DOCX output via companyFILES to get a formatted renewal brief ready to share.
