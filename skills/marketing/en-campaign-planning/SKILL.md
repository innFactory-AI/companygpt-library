---
name: en-campaign-planning
description: Generate campaign briefs with objectives, audience segments, channel strategy, content calendar, and success metrics. Use when launching a new campaign, planning quarterly marketing activities, or briefing an agency. Trigger with "plan campaign for", "campaign brief", "marketing plan for [launch]".
---

# Campaign Planning Skill

Plan marketing campaigns from objective definition through content calendar production to success measurement. All brand guidelines, audience data, historical performance, and budgets come from you or from connected sources.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Analytics via MCP** (e.g. Google Analytics, Adobe, Mixpanel) | Historical performance, audience behaviour, conversions |
| **CRM via MCP** (e.g. Salesforce, HubSpot) | Customer segments, deal stage data, contact lists |
| **Ad platforms via MCP** (e.g. Google Ads, Meta Ads, LinkedIn Ads) | Past campaign performance, targeting data, spend history |
| **CMS via MCP** (e.g. WordPress, Contentful, Webflow) | Content inventory, publishing schedule, SEO data |
| **Email via MCP** (e.g. Mailchimp, HubSpot, Braze, Customer.io) | List size, engagement metrics, sequence performance |
| **companyRAG collections / file upload** | Brand guidelines, past briefs, campaign templates |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Campaign Planning Workflow

Follow these steps in order. Each step builds on the previous one — skipping steps produces incomplete briefs that require rework.

### Step 1: Define Campaign Objectives

Every campaign starts with a clear, measurable objective. Without one, there is no way to determine success or allocate resources rationally.

**Objective framework:**

```
CAMPAIGN OBJECTIVE:
  Business goal:     [The overarching business outcome this campaign supports]
  Campaign goal:     [The specific marketing outcome — what changes because of this campaign?]
  Primary metric:    [The ONE number that defines success]
  Target:            [Specific, measurable target for the primary metric]
  Timeline:          [Campaign start — end dates]
  Baseline:          [Current value of the primary metric, from YOUR data]
```

**Objective quality check:**

| Check | Question | If No |
| --- | --- | --- |
| Measurable | Can you put a number on success? | Redefine until quantifiable |
| Time-bound | Is there a clear end date? | Set one — open-ended campaigns drift |
| Baselined | Do you know the current state? | Establish baseline before setting targets |
| Singular | Is there ONE primary metric? | Choose one primary, move others to secondary |
| Influenceable | Can marketing meaningfully move this metric? | Re-scope to a metric marketing controls |

### Step 2: Segment the Audience

Define who the campaign targets. Campaigns that target "everyone" target no one effectively.

**Segmentation methodology:**

1. Start with the business objective — who needs to take what action for the objective to be met?
2. Define primary segments (2-4 maximum per campaign) using available data dimensions:

| Dimension | Examples | Best for |
| --- | --- | --- |
| Demographic | Company size, industry, job title, geography | B2B targeting, account-based campaigns |
| Behavioural | Purchase history, engagement level, product usage | Retention, upsell, re-engagement |
| Stage-based | Funnel stage, lifecycle stage, buyer journey position | Nurture, conversion, onboarding |
| Needs-based | Pain points, use cases, jobs-to-be-done | Content marketing, thought leadership |

1. For each segment, complete:

```
SEGMENT: [name]
  Size estimate:     [from CRM/analytics data or user input]
  Key characteristics: [defining attributes]
  Primary pain point:  [what problem does this campaign solve for them?]
  Desired action:      [what should they DO after encountering the campaign?]
  Current awareness:   [unaware / problem-aware / solution-aware / product-aware]
  Channels:            [where does this segment consume content? — from data or user input]
```

### Step 3: Select Channels and Tactics

Match channels to segments and objectives. Channel selection is a strategic choice, not a checklist.

**Channel selection matrix:**

For each candidate channel, assess:

| Factor | Assessment |
| --- | --- |
| Audience presence | Is the target segment active on this channel? (from data, not assumption) |
| Objective fit | Can this channel drive the desired action (awareness, consideration, conversion)? |
| Historical performance | How has this channel performed for similar campaigns? (from your data) |
| Budget efficiency | What is the expected cost per result relative to other channels? |
| Content fit | Does the campaign message work in this channel's format? |
| Capacity | Does the team have the skills and bandwidth to execute well on this channel? |

**Channel role assignment:**

Assign each selected channel a specific role in the campaign:

| Role | Purpose | Example |
| --- | --- | --- |
| **Reach** | Generate awareness among the target audience | Paid social, display, PR, SEO content |
| **Engage** | Deepen interest and move toward consideration | Blog posts, webinars, email nurture, retargeting |
| **Convert** | Drive the specific desired action | Landing pages, paid search, direct email, sales enablement |
| **Retain** | Post-conversion reinforcement | Onboarding emails, community, customer content |

Not every campaign needs all four roles. Match to your funnel objective.

### Step 4: Plan the Content Calendar

Translate the channel strategy into a production and publishing schedule.

**Calendar construction process:**

1. Work backward from launch date — identify all content assets needed, their dependencies, and production timelines
2. Map content to the campaign timeline:

```
CONTENT CALENDAR:

Week 1: [Campaign phase — e.g., Pre-launch / Teaser]
  [Date] — [Channel] — [Content piece] — [Segment] — [Owner] — [Status]
  [Date] — [Channel] — [Content piece] — [Segment] — [Owner] — [Status]

Week 2: [Campaign phase — e.g., Launch]
  ...

Week 3–4: [Campaign phase — e.g., Sustain / Nurture]
  ...

Week N: [Campaign phase — e.g., Close / Wrap-up]
  ...
```

1. Production timeline — for each content piece, define:

| Element | Detail |
| --- | --- |
| Content piece | Name and format |
| Brief due | Date the brief must be ready |
| First draft due | Date for initial creation |
| Review/approval | Date for stakeholder review |
| Final asset due | Date the finished asset is needed |
| Publish date | Date it goes live |

1. Validate capacity: total content pieces × average production time ≤ available team hours. If the math does not work, cut scope before starting — not mid-campaign.

### Step 5: Set KPIs and Measurement Plan

Define how success will be measured. Reference the report-performance skill for detailed measurement methodology.

**KPI framework for the campaign:**

```
PRIMARY KPI:
  Metric:    [from campaign objective]
  Target:    [specific number]
  Baseline:  [current value]
  Measurement source: [which tool/platform]

SECONDARY KPIs:
  [Metric 1]: [target] — Measures: [what aspect of campaign health]
  [Metric 2]: [target] — Measures: [...]

GUARDRAIL METRICS (must not degrade):
  [Metric]: [threshold] — e.g., unsubscribe rate must stay below X%
```

### Step 6: Budget Allocation

Allocate budget across channels based on expected contribution to the campaign objective.

**Allocation methodology:**

1. Start with total budget — if undefined, the plan should specify the budget needed to achieve the objective
2. Allocate by channel role: weight investment toward the funnel stages most critical to the objective
3. Within each channel: allocate based on historical cost-per-result (from your data) or test budget for unproven channels

```
BUDGET ALLOCATION:
  Total budget: [amount]

  Channel:     [name]
  Role:        [reach / engage / convert / retain]
  Allocation:  [amount or %]
  Expected result: [volume of primary metric]
  Cost per result: [from historical data or estimate]
  Confidence:  [high — historical data / medium — estimated / low — new channel]

  [Repeat for each channel]

  Reserve:     [10-15% recommended for opportunistic spend or underperforming channel reallocation]
```

**Budget reallocation triggers:**

| Signal | Action |
| --- | --- |
| Channel exceeding cost-per-result target by >25% after 2 weeks | Reduce allocation, investigate |
| Channel outperforming by >25% | Consider increasing allocation from reserve |
| New channel with insufficient data after test period | Decide: extend test or reallocate |
| Overall campaign pacing behind target at 50% mark | Review and adjust all channel allocations |

## Output Template: Campaign Brief

```
# Campaign Brief — [Campaign Name]
Date: [date]
Owner: [campaign manager]
Status: [Draft / In review / Approved]

## Objective
  [From Step 1 — business goal, campaign goal, primary metric, target, timeline, baseline]

## Audience
  [From Step 2 — segment profiles with size, characteristics, pain points, desired actions]

## Channel Strategy
  [From Step 3 — selected channels with roles, rationale, and capacity assessment]

## Content Calendar
  [From Step 4 — phased calendar with content pieces, owners, and production timeline]

## KPIs and Measurement
  [From Step 5 — primary, secondary, and guardrail metrics with targets and sources]

## Budget
  [From Step 6 — allocation by channel with expected results and confidence levels]

## Risks and Dependencies
  - [Risk 1]: [mitigation]
  - [Dependency 1]: [owner and timeline]

## Approvals
  - [ ] Campaign objective approved by [stakeholder]
  - [ ] Budget approved by [stakeholder]
  - [ ] Creative brief approved by [stakeholder]
  - [ ] Legal/compliance review (if applicable)
```

## Adapt to Your Business

1. Upload your brand guidelines to a companyRAG collection — the skill will reference them when assessing channel and content fit
2. Store campaign templates from successful past campaigns — use them as starting frameworks
3. Connect your analytics and ad platforms for historical performance data to inform channel selection and budget allocation
4. Define your standard approval workflow so briefs include the right stakeholders from the start
5. Specify your content production capacity so calendar planning accounts for real team bandwidth

## Guardrails

- Never generate performance benchmarks, conversion rates, CPM/CPC estimates, or audience size data. All performance data must come from the user's analytics or connected sources.
- Never claim "best practice" channel mixes or budget splits. Optimal allocation depends on the specific business, audience, and market.
- Never assume audience characteristics or channel preferences without data. Ask the user or flag as `[Data needed]`.
- Flag outputs: `[From customer data]` for sourced data · `[Framework methodology]` for this skill's approach · `[AI suggestion]` for model recommendations · `[Data needed]` for placeholders.

> **Tip:** Ask for XLSX, DOCX, or Markdown output via companyFILES to get a formatted brief ready to share.
