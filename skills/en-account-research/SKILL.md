---
name: en-account-research
description: Research a company or prospect for actionable sales intelligence — overview, recent signals, key people, and conversation hooks. Use when preparing for a first meeting, taking over a new account, or refreshing stale account knowledge. Trigger with "research [company]", "what do I need to know about [account]", "account briefing for".
---

# Account Research Skill

Turn raw company data into actionable sales intelligence — account briefs, signal summaries, key-person profiles, and conversation hooks. All company data comes from you, a connected MCP source, web search, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. Salesforce, HubSpot, Dynamics) | Deal history, past interactions, existing contacts, account-owner notes |
| **Web search** (company website, news, press) | Recent announcements, leadership changes, product launches, financials |
| **Enrichment data via MCP** (e.g. LinkedIn, Crunchbase, Owler) | Firmographics, funding rounds, headcount trends, tech stack |
| **companyRAG / file upload** | Historical context, competitive positioning, persona definitions, financial filings (e.g. annual report, 10-K, earnings call) |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

When a data source is unavailable, note the gap explicitly in the output rather than compensating with assumptions.

## Research Workflow

```
1. IDENTIFY the target
   |
   +--> Company name + context from user
   +--> Check CRM for existing account record
   |      FOUND --> Pull deal history, contact list, notes
   |      NOT FOUND --> Note as net-new account
   |
2. GATHER firmographic foundation
   |
   +--> Company overview: industry, HQ, employee count, revenue range
   +--> Business model: who they sell to, how they deliver value
   +--> Growth trajectory: hiring trends, funding, expansion signals
   +--> Tech stack: known tools and platforms (enrichment or user input only)
   |
3. FIND recent signals (last 90 days prioritized)
   |
   +--> Leadership changes (C-suite, VP-level hires/departures)
   +--> Earnings or funding events
   +--> Product launches or pivots
   +--> Partnerships or acquisitions
   +--> Regulatory or compliance developments
   +--> Layoffs, restructuring, or strategic shifts
   |
4. MAP key people
   |
   +--> Identify likely buying center roles (see Key-Person Mapping below)
   +--> Cross-reference CRM contacts with current org
   +--> Flag stale contacts (role changed, left company)
   +--> Identify warm paths (mutual connections, past interactions)
   |
5. SURFACE conversation hooks
   |
   +--> Match signals to your value proposition (see Hook Generation below)
   +--> Identify pain points implied by signals
   +--> Draft 2-3 opening angles ranked by relevance
   |
6. COMPILE account brief (see Output Template below)
```

## Signal Categorization

Classify every signal by type and sales relevance:

| Signal Type | Examples | Sales Relevance |
| --- | --- | --- |
| **Growth** | Funding round, IPO filing, market expansion | Budget availability, urgency to scale, new initiative spend |
| **Leadership Change** | New CxO, VP hire in target function | Fresh mandate, willingness to evaluate new vendors |
| **Strategic Shift** | Digital transformation, new market entry, M&A | Re-evaluation of existing tools, expanded buying center |
| **Pain Indicator** | Layoffs, earnings miss, product recall, churn news | Cost pressure, need for efficiency, urgency to show results |
| **Regulatory** | New compliance requirements, audit findings | Compliance-driven purchase, mandatory timeline |
| **Technology** | Platform migration, tool consolidation, RFP issued | Active evaluation cycle, defined procurement timeline |
| **Competitive** | Competitor mentioned in news, switched vendors | Displacement opportunity, dissatisfaction signal |

Recency weighting: signals from the last 30 days carry highest relevance, 30-90 days moderate, beyond 90 days flag as potentially stale.

## Key-Person Mapping

For each identified contact, capture:

| Field | Description |
| --- | --- |
| **Name & Title** | Current role at the company (verify currency) |
| **Buying Center Role** | Economic Buyer, Champion, Technical Evaluator, End User, Blocker |
| **Relevance** | Why this person matters to your deal (functional responsibility) |
| **Warm Path** | Mutual connections, prior interactions, shared events |
| **Engagement Status** | New contact / Existing relationship / Stale (no contact >6 months) |

When enrichment data is unavailable, list the role archetype needed (e.g., "VP Engineering — not yet identified") so the rep knows what to look for.

### Org Navigation Heuristics

For unfamiliar orgs, use these patterns to identify likely decision-makers:

- Top-down signal: Leadership hire in target function → that person likely owns the initiative
- Bottom-up signal: Job postings for roles adjacent to your solution → hiring manager is a potential champion
- Lateral signal: Existing customer contact moved to this company → warm introduction path
- Procurement signal: RFP or vendor-review mentions → procurement lead is a gatekeeper to map early

## Hook Generation

A conversation hook connects a signal to a pain point that your solution addresses. Each hook follows this structure:

```
SIGNAL: [What happened — sourced fact]
  |
  +--> IMPLICATION: [What this likely means for their business]
  |
  +--> CONNECTION: [How your solution is relevant to this implication]
  |
  +--> OPENER: [A specific question or statement to start the conversation]
```

### Hook Quality Criteria

| Criterion | Strong Hook | Weak Hook |
| --- | --- | --- |
| **Specificity** | References a concrete signal with date/source | Generic industry observation |
| **Relevance** | Connects directly to the prospect's stated priorities | Tangential to their business |
| **Timeliness** | Based on recent event (ideally <30 days) | Based on stale or undated information |
| **Value Framing** | Frames around their outcome, not your product features | Leads with product pitch |
| **Conversational** | Invites dialogue ("How are you thinking about...") | Declarative ("You need...") |

Generate 2-3 hooks per account brief, ranked by signal strength and relevance.

## Output Template: Account Brief

```
# Account Brief: [Company Name]
**Prepared**: [Date]  |  **Source freshness**: [Date of most recent signal]

## Company Overview
- **Industry**: [Sector / sub-sector]
- **Headquarters**: [Location]
- **Size**: [Employee count range] | [Revenue range if public/available]
- **Business Model**: [Brief description of what they do and for whom]
- **Growth Stage**: [Early / Growth / Mature / Turnaround — with evidence]

## CRM Context
- **Account Status**: [Net-new / Existing / Churned / Dormant]
- **Prior Interactions**: [Summary of relevant CRM history or "No prior record"]
- **Existing Contacts**: [List or "None on file"]

## Recent Signals (last 90 days)
| Date   | Signal           | Type       | Sales Relevance               | Source       |
| ------ | ---------------- | ---------- | ----------------------------- | ------------ |
| [Date] | [Specific event] | [Category] | [Why it matters to this deal] | [Source tag] |

## Key People
| Name   | Title          | Buying Role      | Warm Path         | Status        |
| ------ | -------------- | ---------------- | ----------------- | ------------- |
| [Name] | [Current role] | [Role archetype] | [Connection path] | [Engagement]  |

## Conversation Hooks
### Hook 1: [Signal-based label]
- **Signal**: [Fact + source]
- **Implication**: [What it means for them]
- **Opener**: "[Suggested question or statement]"

### Hook 2: [Signal-based label]
...

## Gaps & Next Steps
- [ ] [Missing data that needs filling — e.g., "Identify VP Engineering"]
- [ ] [Verification needed — e.g., "Confirm org restructure is complete"]
- [ ] [Recommended action — e.g., "Request intro via [mutual connection]"]
```

## Research Depth by Context

| Context | Depth | Focus |
| --- | --- | --- |
| **First meeting prep** | Full brief | All sections, prioritize hooks and key people |
| **Account refresh** | Signal and contact update | New signals since last brief, stale-contact audit |
| **Territory planning** | Lightweight scan per account | Firmographics + top signal + ICP fit assessment |
| **Competitive deal** | Full brief + competitor layer | Add competitive intelligence section from battlecard |
| **Expansion play** | Internal-focused brief | Usage data, stakeholder changes, new departments |

## Guardrails

1. Never fabricate contacts or org structures. All names, titles, and reporting lines must come from the user, CRM, enrichment tools, or web search. Unverified contacts: list the role archetype as "Not yet identified."
2. Never generate financial data. Revenue figures, funding amounts, and growth rates must be sourced. If unavailable, state "Not publicly available" rather than estimating.
3. Source labeling. Tag every assertion — `[From CRM]`, `[From web search]`, `[From enrichment]`, `[From user input]`, `[AI inference]`. AI inference must be flagged as requiring verification.
4. Verification reminder. Include "Verify key facts before customer-facing use" on all account briefs.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted, instantly shareable account brief.
