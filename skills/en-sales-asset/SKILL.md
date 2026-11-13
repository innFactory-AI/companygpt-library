---
name: en-sales-asset
description: Produce tailored one-pagers, landing pages, case study drafts, and demo narratives personalised to a specific deal and buyer persona. Use when preparing collateral for a specific deal, building leave-behind materials, or customising standard assets for a prospect. Trigger with "create a one-pager for", "sales deck for [deal]", "customise this asset for".
---

# Sales Asset Skill

Produce deal-specific sales collateral — one-pagers, case study drafts, executive summaries, demo narratives, and proposal inserts — personalised to the buyer's industry, role, and stated priorities. All product information, case studies, pricing, and deal context comes from you, companyRAG collections, or a connected CRM.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Deal stage, deal value, stakeholders, competitive situation, closed-won notes |
| **companyRAG collections** | Product specs, case studies, proof points, industry references |
| **File upload** | Discovery notes, battlecards, account research, call summaries |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Asset-Type Routing

Identify the right asset format based on the sales situation:

| Situation | Recommended Asset | Purpose |
| --- | --- | --- |
| First meeting — leave-behind for champion | **One-Pager** | Concise overview the champion can forward internally |
| Executive sponsor engagement | **Executive Summary** | Business-outcome focused, minimal technical detail |
| Technical evaluation underway | **Solution Brief** | Architecture, integration, security, compliance focus |
| Prospect asked "who else uses this?" | **Case Study Draft** | Social proof mapped to their industry/use case |
| Demo scheduled — need a narrative arc | **Demo Narrative** | Storyline tying demo flow to their specific pain |
| Proposal or RFP response section | **Proposal Insert** | Tailored section addressing specific evaluation criteria |
| Multi-stakeholder deal — different needs | **Messaging Matrix** | Stakeholder-specific value props in one reference doc |

When the user's request does not clearly map to one type, ask clarifying questions about audience, timing, and intended use before drafting.

## Asset Creation Workflow

```
1. IDENTIFY asset type and audience
   |
   +--> Route to asset type (table above)
   +--> Identify primary audience: role, seniority, technical depth
   +--> Identify secondary audience: who else will see this?
   +--> Determine context: where in the deal cycle, what prompted the request
   |
2. GATHER deal context
   |
   +--> From CRM: deal stage, value, stakeholders, competitive situation
   +--> From user: specific pain points, evaluation criteria, buyer language
   +--> From companyRAG collections: product specs, case studies, proof points
   +--> From prior skills: account research, call summaries, battlecard intel
   |
3. MAP messaging to persona
   |
   +--> Apply the Persona-Message Matrix (see below)
   +--> Select value propositions ranked by relevance to this buyer
   +--> Choose proof points that match their industry and company size
   +--> Adapt language register to audience seniority and function
   |
4. GENERATE draft
   |
   +--> Apply the asset-specific template (see Asset Templates below)
   +--> Ensure every claim is backed by a source or flagged as needing one
   +--> Check against quality criteria before presenting
   |
5. REVIEW and refine
   |
   +--> Run the Asset Review Checklist (see below)
   +--> Flag sections that need user input or approval
   +--> Suggest alternative framings for key messages
```

## Persona-Message Matrix

Match messaging emphasis to the buyer's role and priorities:

| Persona | Primary Concerns | Message Emphasis | Proof-Point Type |
| --- | --- | --- | --- |
| **C-Suite / Executive** | Revenue impact, risk, strategic alignment | Business outcomes, ROI, competitive advantage | Revenue metrics, market position |
| **VP / Director** | Team productivity, budget justification | Operational efficiency, time-to-value, TCO | Productivity gains, cost savings |
| **Manager / Team Lead** | Day-to-day impact, adoption, workflow fit | Ease of use, integration, support quality | User satisfaction, adoption rates |
| **Technical Evaluator** | Architecture, security, scalability | Technical specs, compliance, API coverage | Technical benchmarks, certifications |
| **Procurement** | Cost, contract terms, vendor risk | Pricing transparency, vendor stability, SLAs | Financial health, customer count |
| **End User / Practitioner** | Daily workflow, learning curve, reliability | Usability, speed, reliability, support | User testimonials, ease-of-use metrics |

### Language Register by Seniority

| Audience Level | Register | Avoid |
| --- | --- | --- |
| **Executive** | Concise, outcome-first, strategic framing, minimal jargon | Feature lists, technical specifications, acronyms |
| **Management** | Balanced — outcomes with supporting detail, metric-driven | Vague claims without numbers, excessive length |
| **Practitioner** | Specific, practical, workflow-oriented, technically precise | High-level platitudes, marketing superlatives |

## Asset Templates

### One-Pager Template

```
# [Solution Name] for [Industry / Use Case]

## The Challenge
[1-2 sentences describing the specific problem this prospect faces — use their language, not yours]

## How [Solution] Helps
[3-4 bullet points — each structured as: Outcome → How it works → Proof]
- **[Outcome]**: [Brief mechanism] — [Proof point with metric]
- **[Outcome]**: [Brief mechanism] — [Proof point with metric]
- **[Outcome]**: [Brief mechanism] — [Proof point with metric]

## Why [Company Name] Specifically
[2-3 sentences connecting your differentiation to their stated evaluation criteria or competitive situation]

## Customer Proof
"[Quote from a reference customer in their industry or similar use case]"
— [Name, Title, Company]   |   [Key metric achieved]

## Next Step
[Specific CTA relevant to where they are in the deal cycle]
```

### Executive Summary Template

```
# Executive Summary: [Solution] for [Prospect Company]

**Prepared for**: [Name, Title]
**Date**: [Date]

## Strategic Context
[2-3 sentences on the business challenge, framed in terms of their strategic priorities — reference annual report, earnings call, or stated goals if available]

## Recommended Approach
[Brief description of the proposed solution — outcomes first, then how — never feature-first]

## Expected Business Impact
| Outcome Area          | Current State        | Projected Improvement | Basis               |
| --------------------- | -------------------- | --------------------- | ------------------- |
| [Area]                | [Metric if known]    | [Projected change]    | [Source/comparables]|

## Risk Mitigation
[Address the top 2-3 concerns this executive likely has — security, integration, change management, vendor stability]

## Investment Overview
[High-level framing — not detailed pricing. Position as investment with expected return, not a cost]

## Recommended Next Step
[Specific, executive-appropriate ask]
```

### Case Study Draft Template

```
# [Customer Name]: [Headline Result]

## Company Profile
- **Industry**: [Sector]  |  **Size**: [Employees / Revenue]
- **Use Case**: [What they were trying to accomplish]

## The Challenge
[3-4 sentences — the specific problem, its business impact, and why previous approaches fell short]

## The Solution
[How they implemented your solution — timeline, scope, approach. Focus on decisions, not features]

## Results
| Metric              | Before           | After            | Improvement         |
| ------------------- | ---------------- | ---------------- | ------------------- |
| [KPI]               | [Value]          | [Value]          | [% or absolute]     |

## Key Quote
"[Customer quote that captures the transformation]"
— [Name, Title]

## Relevance to [Prospect]
[2-3 sentences explaining why this case study is specifically relevant to the prospect's situation]
```

### Demo Narrative Template

```
# Demo Narrative: [Prospect Company]

**Audience**: [Names, roles]
**Duration**: [Scheduled time]
**Objective**: [What success looks like for this demo]

## Opening Context (2 min)
[Connect their stated challenge to what they are about to see. Reference a specific conversation or discovery finding.]

## Scene 1: [Pain Point → Capability] (X min)
- **Setup**: "[Describe the scenario in their terms]"
- **Show**: [Specific feature/workflow to demonstrate]
- **Outcome**: "[What this means for their team]"
- **Check-in question**: "[Gauge reaction and relevance]"

## Scene 2: [Pain Point → Capability] (X min)
[Same structure]

## Scene 3: [Differentiator Moment] (X min)
- **Setup**: "[This is where we are different from alternatives]"
- **Show**: [Unique capability mapped to their evaluation criteria]
- **Bridge**: "[Tie back to their decision criteria]"

## Closing (3 min)
- Recap: [3 key takeaways mapped to their priorities]
- Ask: "[Next-step proposal]"
- Leave-behind: [What you will send after — one-pager, trial, proposal]

## Backup Scenes
[2-3 additional features ready if specific questions arise or time allows — do not show unless prompted]
```

### Messaging Matrix Template

```
# Messaging Matrix: [Deal Name]

| Stakeholder         | Title          | Primary Pain         | Value Prop                   | Proof Point               | Key Objection           | Talk Track                      |
| ------------------- | -------------- | -------------------- | ---------------------------- | ------------------------- | ----------------------- | ------------------------------- |
| [Name]              | [Role]         | [Their top concern]  | [Tailored value statement]   | [Relevant case/metric]    | [Likely pushback]       | [How to frame the conversation] |
```

## Asset Review Checklist

Before delivering any asset, verify:

| Criterion | Check |
| --- | --- |
| **Audience alignment** | Does the language, depth, and emphasis match the intended reader? |
| **Claim substantiation** | Is every claim backed by a sourced proof point or flagged? |
| **Prospect specificity** | Could this asset only apply to this prospect, or is it generic? |
| **Competitive awareness** | Does it address known alternatives without naming competitors negatively? |
| **CTA appropriateness** | Is the call-to-action matched to the deal stage? |
| **Length appropriateness** | One-pager: 1 page. Exec summary: 1-2 pages. Case study: 1-2 pages. |
| **Brand consistency** | Does it match the customer's brand voice guidelines (if provided)? |
| **Formatting** | Professional, clean, no markdown artifacts in customer-facing copy |
| **Legal/compliance** | No unapproved claims, accurate case study data, no NDA violations |

## Guardrails

1. Never fabricate case studies or customer quotes. All customer names, results, and testimonials must come from the user or companyRAG collections. Use "[Insert customer reference for this industry]" when none are provided.
2. Never generate product capabilities not provided by the user. If product details are not in companyRAG collections or user input, flag as "[Verify with product team]" rather than assuming features.
3. Never invent metrics or ROI figures. Business-impact projections must be based on provided case data or flagged as "[Placeholder — needs validation with customer success team]".
4. Source labeling. Tag content origin — [From companyRAG collection], [From user input], [From CRM], [From deal context], [AI draft — verify].

> **Tip:** Ask for PPTX output via companyFILES to get a formatted slide deck, or DOCX for a one-pager ready for distribution. PDF and Markdown are also available for longer collateral.
