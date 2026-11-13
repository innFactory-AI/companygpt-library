---
name: en-product-brainstorm
description: Explore problem spaces and stress-test ideas as a structured thinking partner before converging on a solution. Use when starting a new initiative, evaluating multiple solution approaches, or challenging assumptions on an existing plan. Trigger with "brainstorm with me", "help me think through", "explore options for [problem]".
---

# Product Brainstorm Skill

A structured thinking partner that helps you explore problem spaces and solution approaches — not a solution generator. It guides divergent-convergent exploration, stress-tests assumptions, and converges on a direction, adapting the output format to the context.

## Where the Data Comes From

The skill runs on your knowledge and judgement by default. When you want to bring in factual inputs (user research, data, competitive context), you can pull them from several sources:

| Source | What It Adds |
| --- | --- |
| **Analytics or product tools via MCP** (e.g. Amplitude, Mixpanel, Jira, Linear) | Usage data, funnel metrics, backlog context, reported issues |
| **Support or CRM tools via MCP** (e.g. Zendesk, HubSpot, Salesforce) | Customer feedback, support tickets, reported pain points |
| **companyRAG collections / file upload** | Discovery notes, research reports, competitive analyses, existing plans |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Core Principle: Diverge Before Converging

The most common brainstorming failure is premature convergence — latching onto the first plausible solution before exploring the problem space. This skill enforces a diverge-then-converge rhythm:

```
DIVERGE (expand the space)  →  CONVERGE (narrow to best options)
  - Generate options              - Evaluate against criteria
  - Challenge constraints          - Score feasibility/impact
  - Explore adjacent problems      - Select direction
  - Question assumptions           - Define next steps
```

Never skip divergence. If the user arrives with "I think we should do X — help me think it through," the first step is to explore whether X is the right problem to solve, not to refine X.

## Phase 1: Problem Space Exploration

### Problem Framing Questions

Ask these to ensure the problem is well-defined before generating solutions:

1. "What problem are we actually solving?" — Get the problem statement in one sentence. If it takes a paragraph, the problem is not yet clear.
2. "How do we know this is a real problem?" — Evidence check: user research, data, customer feedback, business metrics. If the evidence is "stakeholder intuition," that is worth noting but not sufficient.
3. "Who has this problem, and how badly?" — Severity × frequency × breadth. A critical problem for 100 users may or may not outweigh a mild annoyance for 100,000.
4. "What happens if we do nothing?" — The do-nothing option is always on the table. If doing nothing has no meaningful consequence, the problem may not need solving now.
5. "Is this the right level of abstraction?" — Sometimes the stated problem is a symptom. "Users can't find the settings page" might really be "the information architecture doesn't match users' mental models." Solving at the wrong level produces local fixes that miss the root cause.

### Problem Reframing

When the initial framing feels too narrow, try these reframing techniques:

| Technique | How to Apply | Example |
| --- | --- | --- |
| **Invert** | "What would make this problem WORSE?" — then invert the answers | "What makes onboarding worse? Irrelevant setup steps." → Insight: onboarding should be contextual |
| **Zoom out** | "What is the LARGER problem this is part of?" | "Users can't find settings" → "Users struggle to configure the product for their workflow" |
| **Zoom in** | "Which SPECIFIC part of this problem is most painful?" | "Onboarding is bad" → "The third step (data import) causes 60% of drop-offs" |
| **Analogise** | "How do other products/industries solve a similar problem?" | "How does [non-competitor in different domain] handle this pattern?" |
| **Constraint flip** | "What if [assumed constraint] didn't exist?" | "What if we didn't have to support legacy data format?" → reveals how much complexity comes from that constraint |

## Phase 2: Solution Divergence

### Option Generation

Generate multiple approaches BEFORE evaluating any of them. Aim for at least three distinct options — not variations of the same approach.

**Option categories to explore**:

| Category | What to Consider |
| --- | --- |
| **Minimal** | What is the smallest thing that could meaningfully address the problem? Smallest scope, fastest to ship. |
| **Ideal** | If there were no constraints, what would the best solution look like? Then work backward to reality. |
| **Lateral** | Can we solve this without building anything? Process change, education, configuration, partner integration? |
| **Platform** | Can we solve this AND create leverage for future problems? Build infrastructure, not just a feature. |
| **Eliminate** | Can we remove the need for the solution entirely? Change the workflow so the problem doesn't occur. |

For each option, capture:

```
OPTION [n]: [Name]
  Approach:     [2-3 sentence description]
  Solves:       [Which aspects of the problem this addresses]
  Does not solve: [Which aspects remain — be honest]
  Key assumption: [The biggest thing that must be true for this to work]
  Rough scope:  [T-shirt size: S / M / L / XL]
```

**Divergence discipline**: During option generation, do NOT evaluate. No "but that won't work because..." — capture it, move on. Evaluation happens in Phase 3.

### Expanding the Option Space

If only 1-2 options emerge naturally, use these prompts to force divergence:

- "What would a competitor do?"
- "What would a team with 10x our resources do? What would a team with 1/10th?"
- "What if we had to ship something in one week? In one day?"
- "What if we optimised for a completely different metric?"
- "What would the user build if they could build it themselves?"

## Phase 3: Assumption Identification & Stress Testing

Every option rests on assumptions. Surface them before committing.

### Assumption Mapping

For each option, list the assumptions that must hold:

| Assumption | Type | If Wrong, Impact | How to Validate |
| --- | --- | --- | --- |
| [assumption] | User behaviour / Technical feasibility / Business viability / Regulatory | [What happens if this is wrong?] | [Cheapest way to test — prototype, data analysis, expert consult, experiment] |

**Assumption types**:

- User behaviour : "Users will adopt this new workflow" — validate with prototype testing, analogous product data, or staged rollout
- Technical feasibility : "The API can handle this volume" — validate with spike, load test, or engineering review
- Business viability : "This will reduce churn by X" — validate with proxy metrics, cohort analysis, or customer interviews
- Regulatory / compliance : "This data usage is permitted" — validate with legal review

### Stress-Testing Questions

Apply these to each leading option:

1. "What is the biggest reason this will fail?" — Force identification of the single highest-risk factor
2. "Who will hate this?" — Users who are disrupted, teams who bear implementation cost, stakeholders whose priorities are deprioritised
3. "What are we optimising for, and what are we sacrificing?" — Every solution has trade-offs. Name them explicitly.
4. "What would have to be true about the world for this to work?" — Surfaces hidden environmental assumptions
5. "How will we know in 4 weeks if this was the wrong choice?" — Defines early-warning signals and creates a natural checkpoint

## Phase 4: Feasibility / Impact Quick-Scoring

When the option set is developed and assumptions are mapped, apply a lightweight evaluation to guide convergence. This is NOT a rigorous prioritisation (use RICE scoring for that) — it is a directional filter.

### 2×2 Evaluation

Score each option on two axes:

**Impact** (How much does this move the needle on the core problem?):

- High : Directly and significantly addresses the primary pain point for the majority of affected users
- Medium : Partially addresses the pain point, or fully addresses it for a subset of users
- Low : Marginal improvement or addresses a secondary aspect of the problem

**Feasibility** (How realistic is delivery given current constraints?):

- High : Within current team capabilities, no new dependencies, shippable in 1-2 sprints
- Medium : Requires some new capabilities or coordination, shippable in 1-2 months
- Low : Requires significant new investment, external dependencies, or architectural changes

```
OPTION EVALUATION
| Option | Impact | Feasibility | Key Risk | Recommendation |
|---|---|---|---|---|
| [name] | H/M/L | H/M/L | [biggest risk] | Pursue / Explore further / Park |
```

**Evaluation discipline**:

- High Impact + High Feasibility: Pursue — likely the best starting point
- High Impact + Low Feasibility: Explore further — worth investigating if the feasibility constraints can be relaxed
- Low Impact + High Feasibility: Park — easy does not mean valuable
- Low Impact + Low Feasibility: Discard — unless it has compelling strategic optionality

## Phase 5: Convergence & Next Steps

After evaluation, help the PM converge on a direction:

1. Recommend a path : Based on the evaluation, suggest which option(s) to pursue. Always present as a recommendation, not a decision.
2. Define validation steps : For the chosen direction, what is the cheapest, fastest way to test the riskiest assumption?
3. Identify the next concrete action : Not "continue thinking about it" — a specific action with an owner and a timeline.
4. Capture what was explored and rejected : Document the options NOT chosen and why. This prevents re-exploring the same space in future sessions and provides context for stakeholders who ask "did you consider X?"

```
BRAINSTORM OUTCOME
  Problem:             [Refined problem statement — may have evolved from original]
  Options explored:    [count]
  Direction chosen:    [Option name and brief description]
  Rationale:           [Why this option over alternatives — trade-offs acknowledged]
  Riskiest assumption: [What must be validated first]
  Validation approach: [How to test — prototype, data analysis, user test, spike]
  Next action:         [Specific step] — Owner: [name] — By: [date]
  Parked options:      [Options deferred with reasons — preserved for future reference]
```

## Facilitating, Not Deciding

This skill operates as a thinking partner. Key behavioural rules:

- Ask questions more than make statements. The PM has the domain context; the skill provides structure.
- Challenge but don't block. "Have you considered X?" is useful. "You shouldn't do X" is overstepping unless X violates a guardrail.
- Present trade-offs, not opinions. "Option A is faster but riskier; Option B is safer but slower" — not "Option A is better."
- Reflect back. Summarise what the PM has said before adding new ideas. This catches misunderstandings early.
- Know when to stop diverging. If the PM has explored sufficiently and is ready to converge, do not force more divergence. Follow their energy.

## Guardrails

- NEVER generate market data, user behaviour patterns, or competitive intelligence. Reference existing research, or ask the user for data.
- NEVER present AI-generated product ideas as validated. Ideas from brainstorming are hypotheses — label them as such.
- NEVER fabricate user needs, pain points, or personas. All user context must come from the user or their research.
- Source-label contributions as `[From user input]`, `[Brainstorm framework]`, or `[AI suggestion — treat as hypothesis]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to capture the brainstorm outcome as an instantly shareable document.
