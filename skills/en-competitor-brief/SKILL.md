---
name: en-competitor-brief
description: Create competitive analysis documents for product strategy decisions, feature prioritisation, and differentiation. Use when a competitor launches something new, entering a new market segment, or preparing for a strategy review. Trigger with "competitive brief on", "what is [competitor] doing", "compare us to [competitor]".
---

# Competitor Brief Skill

Build competitive intelligence briefs that inform product strategy, feature prioritisation, and market positioning. All competitive data must come from you, companyRAG collections, or web search — never from training data.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **MCP servers** (e.g. CRM like HubSpot/Salesforce, analyst or review platforms) | Sales-call notes, churn interviews, prospect objections, RFP responses |
| **companyRAG collections / file upload** | Analyst reports, customer reviews, technical assessments, your own feature documentation |
| **Web search** | Public product documentation, press coverage, job postings, patent applications, conference talks |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Competitive Brief Workflow

Run these four phases in order. Each phase feeds the next.

### Phase 1: Intelligence Gathering

Before analysis, establish what is known and what needs investigation.

**Source inventory** — for each competitor being analysed:

| Source Type | Examples | Reliability |
| --- | --- | --- |
| **Primary** | Direct product usage, free trials, public demos, published documentation | Highest — first-hand observation |
| **Secondary** | Analyst reports, customer reviews (G2, Capterra), press coverage, blog posts | High — but may be outdated or biased |
| **Field intelligence** | Sales-call notes, customer churn interviews, prospect objections, RFP responses | High for intent signals — but anecdotal |
| **Public filings** | SEC filings, job postings, patent applications, conference talks | High for strategic direction — low for product detail |

**Gap identification**: After inventorying sources, explicitly list what is NOT known. Unknown areas become research tasks, not assumptions.

```
INTELLIGENCE INVENTORY — [Competitor Name]
  Known (sourced):    [List with source and recency date]
  Partially known:    [List with gaps identified]
  Unknown:            [List — these are research tasks, not areas to guess about]
  Last updated:       [Date]
```

### Phase 2: Feature Comparison Matrix

Build a structured comparison of capabilities across evaluation dimensions relevant to your product category.

**Matrix construction process**:

1. Define dimensions: Use your product's own feature categories, not the competitor's marketing language. Dimensions should reflect how customers evaluate the category.
2. Score capabilities: For each dimension, assess each player (your product + competitors):   - Strong: Fully addresses the need; no significant gaps   - Adequate: Addresses the core need; some limitations   - Weak: Partially addresses or does not address the need   - Unknown: Insufficient data — flag for research
3. Add evidence: Every score must cite its source. Unsourced scores are assumptions.

```
FEATURE COMPARISON — [Category]
| Dimension | Your Product | Competitor A | Competitor B | Notes |
|---|---|---|---|---|
| [dimension] | [score + source] | [score + source] | [score + source] | [key differences] |
```

**Scoring discipline**:

- Score based on current shipped product, not announced roadmap
- Do not give your own product favourable scores without evidence — self-serving analysis is worse than no analysis
- "Unknown" is a valid and honest score — never fill gaps with assumptions
- Refresh scores when any player ships a significant update

### Phase 3: Strategic Analysis

Move from feature comparison to strategic interpretation.

#### Positioning Analysis

Map each competitor's positioning along the dimensions that matter to your target segments:

1. Value proposition: What problem do they lead with? Who is their ideal customer?
2. Go-to-market motion: Self-serve vs. sales-led vs. partner-led? SMB vs. enterprise vs. both?
3. Pricing model: Per-seat vs. usage-based vs. flat-rate? Free tier? Premium positioning?
4. Differentiation claim: What do they say makes them different? Is the claim substantiated?

#### Threat / Opportunity Assessment

For each competitor, classify the strategic situation:

| Signal | Classification | Implication |
| --- | --- | --- |
| Competitor strong where you are weak, in a dimension customers care about | **Threat — Active** | Requires response: build, partner, or reposition |
| Competitor investing in your stronghold area (hiring, features, marketing) | **Threat — Emerging** | Monitor closely; prepare defensive positioning |
| Competitor weak where you are strong, in a dimension customers care about | **Opportunity — Differentiation** | Amplify in positioning and sales enablement |
| Competitor ignoring a segment or use case you serve well | **Opportunity — White space** | Lean into the underserved segment |
| Competitor and you are equally strong | **Parity** | Compete on other dimensions (price, experience, trust, ecosystem) |

#### Market Movement Indicators

Track signals that indicate strategic direction shifts:

- Hiring patterns: What roles are they hiring for? (Engineering in new areas, sales in new geographies, specific domain expertise)
- Partnership announcements: New integrations, channel partners, platform plays
- Pricing changes: Lowering prices (land-grab), raising prices (value extraction), new tiers (segment expansion)
- Acquisition activity: What capabilities are they buying?
- Customer segment shifts: Are they moving upmarket, downmarket, or into adjacent segments?

### Phase 4: Recommended Response

For each active threat or actionable opportunity, structure a response recommendation:

```
RESPONSE RECOMMENDATION:
  Trigger:         [What competitive action prompted this?]
  Classification:  [Threat — Active / Threat — Emerging / Opportunity]
  Impact:          [Which of your segments, metrics, or positioning is affected?]
  Response options:
    1. [Build] — [What to build + rough scope + timeline implication]
    2. [Partner] — [Partnership that could close the gap]
    3. [Reposition] — [Messaging change to reframe the dimension]
    4. [Monitor] — [Watch and reassess at next review cycle]
  Recommended option: [number + rationale]
  Decision owner:  [Who should approve this response?]
  Urgency:         [Immediate / This quarter / Next planning cycle]
```

**Response selection criteria**:

- Build when the gap is in a must-win dimension and you have the capacity
- Partner when the gap is real but not your core competency
- Reposition when the competitor's advantage matters less than they claim, or when you can reframe the evaluation criteria
- Monitor when the threat is emerging but not yet impacting customers or pipeline

## Output Template — Competitive Brief

```
# Competitive Brief — [Competitor Name]
Date: [date]    |    Author: [name]    |    Classification: [Internal / Confidential]

## 1. Executive Summary
[2-3 sentence overview: who they are, what changed, why it matters to us]

## 2. Intelligence Inventory
[Sources consulted, recency, known gaps]

## 3. Feature Comparison Matrix
[Structured comparison — see Phase 2]

## 4. Positioning Analysis
[Value proposition, GTM, pricing, differentiation — see Phase 3]

## 5. Threat & Opportunity Assessment
[Classified signals — see Phase 3]

## 6. Recommended Response
[Action items with owners and urgency — see Phase 4]

## 7. Open Questions
[What we still need to learn, with assigned research tasks]

## 8. Review Cadence
[When to revisit this brief — typically quarterly or after major competitor moves]
```

## Competitive Review Cadence

| Trigger | Action |
| --- | --- |
| **Competitor launches major feature** | Update affected feature matrix rows; reassess threats |
| **Quarterly planning** | Full brief refresh for top 2-3 competitors |
| **Lost deal to competitor** | Post-mortem to update threat assessment and response |
| **Entering new market segment** | Build new brief for segment-specific competitors |
| **Competitor funding / acquisition** | Update market movement indicators and strategic analysis |

## Guardrails

- NEVER generate competitor features, pricing, market share, or positioning from training data. All competitive claims must come from you, companyRAG collections, or web search with cited sources.
- NEVER claim "market standard" or "typical" for any competitive dimension. Every assertion must be sourced.
- When no competitor data is provided, generate the blank brief template and list the specific data needed — do not fill gaps with assumptions.
- Source-label every assertion as `[From user / companyRAG]`, `[From web search — {date}]`, `[Analysis framework]`, or `[AI assessment — verify]`.

> **Tip:** Ask for DOCX, Markdown, or PPTX output via companyFILES to get a formatted brief ready to share.
