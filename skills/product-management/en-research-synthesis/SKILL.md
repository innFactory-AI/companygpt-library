---
name: en-research-synthesis
description: Transforms raw user research into structured insights — themes, opportunity areas, and prioritised recommendations. Use it when consolidating interview notes, analysing survey results, or preparing research readouts for the team. Trigger with "synthesise this research", "what are the themes", "research summary for [project]".
---

# Research Synthesis Skill

Transform raw qualitative and quantitative research data into actionable product insights. The skill covers thematic analysis, evidence strength assessment, insight-to-opportunity mapping, and readout structuring. All research data must come from you, a connected source, or companyRAG collections.

## Where the Data Comes From

| Source | What it contributes |
| --- | --- |
| **MCP servers** (e.g. Notion, Confluence, Jira, a connected research repository) | Research databases, study pages, tickets carrying user feedback |
| **companyRAG collections** | Interview notes, transcripts, survey exports, usability-test protocols |
| **File upload** | Individual transcripts, survey CSV exports, readout drafts |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Research Synthesis Workflow

Execute these five phases sequentially. Rushing to recommendations (Phase 5) without proper coding (Phase 2) and theming (Phase 3) produces unreliable insights.

### Phase 1: Inventory & Classify Source Data

Before analysis, catalogue what data is available and assess its characteristics.

```
RESEARCH INVENTORY
  Project:          [research project name]
  Research question: [the question this research was designed to answer]

  Data sources:
  | Source Type | Count | Method | Participants | Date Range |
  |---|---|---|---|---|
  | [e.g., user interviews] | [count] | [1:1 / group / unmoderated] | [segment description] | [dates] |
  | [e.g., survey responses] | [count] | [open-ended / structured / mixed] | [segment description] | [dates] |

  Participant coverage:
  | Segment | Target | Actual | Gap |
  |---|---|---|---|
  | [segment] | [target n] | [actual n] | [over/under/met] |

  Known limitations:
  - [e.g., only interviewed power users — new user perspective missing]
  - [e.g., survey had 15% response rate — self-selection bias likely]
```

**Data sufficiency check**: Before proceeding, assess whether the data can credibly answer the research question. If significant participant segments are missing or sample sizes are very small, flag this limitation prominently — it constrains every finding that follows.

### Phase 2: Code the Data

Coding transforms raw data into structured, analysable units. This is the most labour-intensive phase and the one most tempted to skip.

**Coding process**:

1. Extract observations : Go through each data source and pull out discrete observations — specific things participants said, did, or experienced. One observation per unit.

```
OBSERVATION:
  Participant: [ID — anonymised]
  Source:      [interview / survey / usability test / support ticket]
  Verbatim:   [exact quote or description of observed behaviour]
  Context:     [what prompted this — question asked, task attempted, scenario]
```

1. Assign codes : Label each observation with a descriptive code. Codes are short labels that capture the concept.

**Coding discipline**:

- Use participant language where possible — resist imposing your own framework prematurely
- One observation can have multiple codes (behaviour often relates to multiple themes)
- Start with open coding (bottom-up from data) before applying any predefined categories
- When the same concept appears with different wording across participants, use a consistent code
- Track code frequency but do NOT equate frequency with importance — a rare but severe pain point may matter more than a common mild one

1. Build the codebook : As codes accumulate, organise them:

```
CODEBOOK
| Code | Definition | Example Observation | Frequency |
|---|---|---|---|
| [code name] | [what this code means] | [representative quote] | [n participants] |
```

### Phase 3: Thematic Analysis

Themes are patterns that emerge from grouping related codes. A theme is NOT a summary of individual observations — it is an interpretive claim about what the observations collectively mean.

**Theme construction process**:

1. **Cluster codes**: Group related codes that point to the same underlying pattern. Look for:   - Codes that frequently co-occur (same participants exhibit both)   - Codes that describe different facets of the same experience   - Codes that form a causal chain (one leads to another)
2. **Name the theme**: A good theme name is an interpretive statement, not a topic label.   - Topic label (weak): "Onboarding"   - Interpretive theme (strong): "Users abandon onboarding when they cannot connect it to their immediate task"
3. **Assess theme strength**:

| Evidence Level | Criteria | Confidence |
| --- | --- | --- |
| **Strong** | Theme supported by 5+ participants across multiple segments; consistent pattern with specific, detailed evidence | High — reliable basis for product decisions |
| **Moderate** | Theme supported by 3-4 participants or concentrated in one segment; pattern is clear but coverage is limited | Medium — worth acting on with awareness of limitations |
| **Emerging** | Theme supported by 1-2 participants; the observation is striking but not yet a pattern | Low — hypothesis for further research, not a basis for decisions |

1. Document each theme :

```
THEME: [Interpretive statement]
  Strength:     [Strong / Moderate / Emerging]
  Codes included: [list of codes that form this theme]
  Supporting evidence:
    - P[id]: "[verbatim quote]" — [context]
    - P[id]: "[verbatim quote]" — [context]
    - P[id]: "[observed behaviour]" — [context]
  Counter-evidence: [any observations that contradict this theme]
  Segments affected: [which participant segments exhibit this pattern]
  Relationship to other themes: [does this theme interact with others?]
```

**Rigour checks**:

- Every theme must have direct evidence (quotes or observed behaviours) — not inferences
- Actively seek counter-evidence — observations that contradict the theme. A theme with no counter-evidence may not have been examined critically enough.
- If two themes overlap heavily, merge them or sharpen the distinction

### Phase 4: Insight-to-Opportunity Mapping

Translate themes into product opportunities. An insight describes what is happening and why; an opportunity describes what could be done about it.

**Mapping framework**:

```
INSIGHT → OPPORTUNITY

Insight:      [What is happening and why — derived from a theme]
Evidence:     [Theme strength: Strong / Moderate / Emerging]
User impact:  [How this affects the user — severity × frequency]
Opportunity:  [What could the product team do about it?]
Opportunity type:
  - Pain relief:      Remove or reduce a source of friction
  - Unmet need:       Deliver capability users lack today
  - Delight:          Exceed expectations in a way users did not anticipate
  - Efficiency gain:  Make an existing workflow meaningfully faster
Confidence:   [How confident are we this opportunity is real? Based on evidence strength + user impact assessment]
```

**Prioritisation of opportunities** (not a replacement for RICE — a research-informed input to it):

| Factor | Assessment |
| --- | --- |
| **Evidence strength** | Strong themes produce higher-confidence opportunities |
| **User impact** | Severity (how painful?) × Breadth (how many users affected?) |
| **Strategic alignment** | Does this opportunity connect to current OKRs or product strategy? |
| **Feasibility signal** | Did users suggest or describe workarounds that hint at solution approaches? |

Order opportunities by: Strong evidence + high impact first, then moderate evidence + high impact, then strong evidence + moderate impact. Emerging-evidence opportunities go to "further research needed," not to the product backlog.

### Phase 5: Research Readout

Structure the synthesis for team consumption. Different audiences need different formats.

#### Full Research Readout

For the product team, design team, and research stakeholders:

```
# Research Synthesis — [Project Name]
Date: [date]    |    Researcher: [name]

## 1. Research Question & Method
[What we set out to learn, how we investigated, who participated]

## 2. Participant Overview
[Segments represented, sample sizes, known gaps]

## 3. Key Themes
[Ordered by evidence strength — strongest first]
  Theme 1: [interpretive statement] — [Strong/Moderate/Emerging]
    [Supporting evidence summary with representative quotes]
  Theme 2: ...

## 4. Opportunities
[Mapped from themes, ordered by confidence × impact]
  Opportunity 1: [description] — Evidence: [strength] — Impact: [assessment]
  Opportunity 2: ...

## 5. Recommendations
[Specific product actions, with evidence basis and confidence level for each]

## 6. Limitations & Caveats
[What this research cannot tell us — sample gaps, methodological constraints]

## 7. Further Research Needed
[Questions raised but not answered — with suggested methods]
```

#### Executive Summary

For stakeholders who need the headline, not the methodology:

```
RESEARCH SUMMARY — [Project Name] — [Date]

Key finding:    [One-sentence headline — the single most important insight]
Evidence base:  [n participants, methods used, segments covered]

Top 3 insights:
1. [Insight] — [Supporting data point] — Confidence: [H/M/L]
2. [Insight] — [Supporting data point] — Confidence: [H/M/L]
3. [Insight] — [Supporting data point] — Confidence: [H/M/L]

Recommended actions:
1. [Action] — Owner: [name] — Priority: [High/Medium/Low]
2. [Action] — Owner: [name] — Priority: [High/Medium/Low]

Limitations: [Key caveats in one sentence]
```

## Combining Qualitative and Quantitative Data

When both types of data are available (e.g., interview themes + survey percentages + analytics data):

1. Quantitative first for "what" : Use metrics and survey data to identify WHAT is happening — which features are underused, where users drop off, what satisfaction scores look like
2. Qualitative for "why" : Use interview and observational data to explain WHY the quantitative patterns exist
3. Triangulation : When qual and quant point the same direction, confidence increases. When they diverge, investigate — the divergence itself is an insight.
4. Never use qual to "validate" quant (or vice versa) — they answer different questions. Qual explains motivations and context; quant measures scale and frequency.

## Guardrails

- NEVER fabricate participant quotes, observations, or research data. Every observation, code, and theme must trace to user-provided source material.
- NEVER claim research findings are "statistically significant" without quantitative analysis. Qualitative research produces thematic patterns with evidence strength levels, not statistical significance.
- Counter-evidence is mandatory. When presenting a theme, actively note contradicting observations. Omitting counter-evidence is a form of fabrication.
- Source-label every element as `[From research data]`, `[Synthesis framework]`, or `[AI interpretation — verify with researcher]`.

> **Tip:** Request a DOCX or Markdown output via companyFILES to get a formatted, instantly shareable readout.
