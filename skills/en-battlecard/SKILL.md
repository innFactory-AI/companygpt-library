---
name: en-battlecard
description: Build side-by-side competitor comparisons with win/loss patterns, objection handlers, and differentiation talk tracks. Use when preparing for a competitive deal, briefing a new rep, or updating competitive intelligence. Trigger with "build a battlecard for", "competitor comparison", "how do we compete against".
---

# Battlecard Skill

Build competitive battlecards using FIA (Fact-Impact-Act), positioning matrices, and structured objection handling. The skill provides structure, not intelligence: all competitive data comes from you, companyRAG collections, or web search.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Deal context, competitive situation, closed-won/closed-lost notes, stakeholders |
| **Battlecard library / companyRAG collections** | Existing competitive intelligence, proof points, reference customers |
| **File upload** | RFPs, discovery-call notes, competitive analyses, pricing documents |
| **Web search** | Current, publicly available competitor information (verifiable facts only) |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Complexity and Depth

This skill's frameworks (FIA, LAER, win/loss analysis, positioning matrix) apply universally across all complexity levels from the Sales Motion Complexity Assessment shared across sales skills (cycle length, deal value, stakeholder count, solution complexity -- all relative to the customer's own norms). Higher-complexity deals warrant more detailed battlecards and deeper competitive analysis, but the fundamental methodology does not change. Adjust depth based on deal significance: a full battlecard with landmine questions for a High-complexity deal; a focused FIA summary for a Low-complexity deal.

## FIA Battlecard Methodology

Fact-Impact-Act (FIA) framework for structuring competitive intelligence into actionable battlecards.

### Structure Per Competitive Point

| Layer | Definition | Example Structure |
| --- | --- | --- |
| **Fact** | Specific, verifiable intelligence about the competitor. Must be sourced and current. No speculation, no training-data claims. | "Competitor requires [specific technical constraint]" -- [Source: battlecard library / user input / web search] |
| **Impact** | Why this fact matters to the deal. Connects to the customer's specific situation or evaluation criteria. | "This means the customer would need to [specific consequence], which affects their [stated priority]." |
| **Act** | What the rep should say or do. Concrete talk track, question, or proof point. | "Ask: 'How important is [capability] to your team?' Then share [proof point]." |

### Battlecard Sections (FIA Applied)

1. Competitor Overview : Company context, market position, typical customer profile (all sourced, never generated)
2. Strengths with Neutralization : Competitor advantages + FIA to neutralize each
3. Weaknesses with Exploitation : Competitor vulnerabilities + FIA to leverage each
4. Pricing Comparison Framework : Structure for comparing pricing models (not actual prices). Dimensions: model type, TCO factors, hidden costs, value-per-unit methodology
5. Objection-Response Pairs : Mapped to responses using LAER (see below)
6. Landmine Questions : Discovery questions per vulnerability category (see below)
7. Customer Proof Points : Template for organizing evidence -- populated from companyRAG collections, never generated

Use the battlecard sections and FIA methodology above as your structural template; expand each section with sourced intelligence from you or from companyRAG collections.

## Competitive Positioning Matrix

Framework for comparing solutions across evaluation criteria:

1. Identify customer's evaluation criteria : From RFP, stated requirements, or discovery. Never assume criteria.
2. Classify criteria : Must-win (deal-breaker if weak) vs. Nice-to-have (differentiator if strong)
3. Score per solution : Strong / Neutral / Weak from evidence only.
4. Identify positioning angles :   - Must-win + You Strong + Competitor Weak = primary differentiation   - Must-win + You Weak = risk area requiring mitigation   - Nice-to-have + You Strong = secondary talking points

## Objection Handling (Carew LAER Bonding Process)

Apply Listen-Acknowledge-Explore-Respond to each competitive objection in the battlecard. The key discipline: Explore the root concern before responding -- the stated objection is often a proxy.

**Important disambiguation**: This is the Carew International LAER Bonding Process, NOT the TSIA Land-Adopt-Expand-Renew lifecycle model which shares the acronym.

Organize objection-response pairs by category (Pricing, Capability gaps, Compliance/Security, References, Vendor maturity) and map evidence from companyRAG collections to each.

## Landmine Question Methodology

Questions designed to expose competitor weaknesses during discovery:

| Vulnerability Category | Question Pattern | What It Exposes |
| --- | --- | --- |
| **Delivery/fulfillment risk** | "How important is [reliable delivery / implementation predictability]?" | Inconsistent delivery, delays |
| **Total cost of ownership** | "Beyond the quoted price, what other costs factor into your evaluation?" | Hidden costs (services, integrations, training) |
| **Integration/interoperability** | "How does [the solution] need to work with your existing [systems/tools]?" | Ecosystem lock-in, compatibility issues |
| **Implementation complexity** | "What does a typical rollout look like? What resources do you allocate?" | Heavy implementation, long time-to-value |
| **Dependency/switching** | "What if you needed to change direction? How portable is your [data/investment]?" | Vendor lock-in, switching costs |
| **Service continuity** | "How important is team stability and continuity of service to your organization?" | Staff turnover, key-person dependency, inconsistent service quality |
| **Domain expertise** | "What level of [industry/domain] expertise do you expect from your provider?" | Shallow domain knowledge, generic approaches, lack of credentials |
| **Fulfillment track record** | "How do you evaluate a provider's ability to deliver consistently at the quality you need?" | Inconsistent delivery, quality variance, missed commitments |

Select 2-3 per deal based on known competitor vulnerabilities from the battlecard.

## Win/Loss Analysis Framework

Structured post-mortem methodology:

1. Data collection : For each closed deal, capture outcome, deciding factors (customer's words), evaluation process, stakeholder dynamics, timeline, pricing discussion, and cited strengths/weaknesses.
2. Root cause categorization : Classify by primary root cause (Product, Price, Relationship, Timing, Competition). Multiple losses with the same root cause = systemic issue.
3. Pattern identification : Look for recurring patterns by root cause, competitor, segment, and win correlations. When losses to the same pattern represent a significant share of total outcomes (relative to portfolio size), it warrants strategic response and battlecard update.

## Competitive Deal Strategy

Apply appropriate strategy based on scenario (head-to-head, displacement, greenfield, multi-vendor). Each calls for different emphasis from the battlecard and positioning matrix -- use FIA points and landmine questions most relevant to the scenario.

## Reference Template

When building a battlecard, follow the structure of the seven Battlecard Sections (FIA Applied) above. Require sourced intelligence for each section, and tag every claim with its source.

## Guardrails

1. Never generate competitive claims. All competitor features, pricing, and positioning must come from you, companyRAG collections, or web search.
2. "Competitive data needed" default. When no data is provided, output this rather than generating analysis.
3. Source labeling. Tag every assertion — [ From battlecard/companyRAG collection ] , [ From user input ] , [ From web search ] , [ AI framework application ] .
4. Verification disclaimer. Include "Verify competitive claims before customer-facing use" on all battlecard content.

> **Tip:** Ask for DOCX, Markdown, or PPTX output via companyFILES to get a formatted document ready for distribution.
