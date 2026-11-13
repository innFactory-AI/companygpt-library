---
name: en-seo-audit
description: Audit a website's SEO health, surface keyword opportunities, identify content gaps, and benchmark against competitors. Use when running a quarterly SEO review, diagnosing organic-traffic drops, or planning content strategy. Trigger with "audit SEO for", "keyword opportunities", "why is traffic down".
---

# SEO Audit Skill

Audit a website's SEO health across five phases — technical audit, content audit, keyword analysis, competitor benchmarking, and prioritised recommendations. All data comes from your SEO tools, analytics, and search console; the skill does not crawl sites itself, it analyses the data you provide.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Search console via MCP** (e.g. Google Search Console) | Impressions, clicks, CTR, position, index coverage, crawl data |
| **Web analytics via MCP** (e.g. GA4) | Traffic data, user behaviour, conversions, landing-page performance |
| **SEO tools via MCP** (e.g. Ahrefs, Semrush) | Keyword rankings, backlinks, technical crawl data, competitor analysis |
| **companyRAG collections** | Past audits, keyword research, content-strategy docs |
| **File upload (crawl exports)** | Crawl exports, CMS inventories, metadata tables, screenshots from your tools |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## SEO Audit Workflow

Follow these five phases in order. Each phase builds on the previous one and feeds into the prioritised recommendations.

### Phase 1: Technical Audit

Assess the technical foundations that affect crawlability, indexability, and site performance.

**Technical audit checklist:**

| Category | Check | What to Look For | Data Source |
| --- | --- | --- | --- |
| **Crawlability** | Robots.txt | Unintentional blocks, missing directives | Crawl export / manual check |
|  | XML sitemap | Present, submitted, up-to-date, no errors | Search console / manual check |
|  | Crawl errors | 4xx, 5xx, redirect chains, orphan pages | Search console / crawl export |
|  | Internal linking | Broken links, deep pages with no internal links | Crawl export |
| **Indexability** | Index coverage | Pages indexed vs. submitted, noindex misuse | Search console |
|  | Canonical tags | Missing, self-referencing, conflicting with other signals | Crawl export |
|  | Duplicate content | Identical or near-identical pages without canonical resolution | Crawl export |
| **Performance** | Core Web Vitals | LCP, INP, CLS scores | PageSpeed Insights / Search console |
|  | Mobile usability | Mobile-friendly errors, responsive design issues | Search console / manual check |
|  | Page speed | Load times, render-blocking resources, image optimisation | PageSpeed Insights / crawl export |
| **Structured data** | Schema markup | Present, valid, relevant types (Organisation, Article, Product, FAQ, etc.) | Rich results test / crawl export |
| **Security** | HTTPS | Full HTTPS migration, mixed content, certificate validity | Crawl export / manual check |
|  | Hreflang (if multilingual) | Correct language/region targeting, reciprocal tags | Crawl export |

**Technical audit output format:**

```
TECHNICAL AUDIT FINDING:
  Category:    [crawlability / indexability / performance / structured data / security]
  Issue:       [specific description]
  Severity:    [critical / high / medium / low]
  Pages affected: [count or scope — from crawl data]
  Evidence:    [specific data point from connected source]
  Impact:      [how this affects search visibility or user experience]
  Recommendation: [specific fix]
  Effort:      [quick fix / moderate / significant]
```

### Phase 2: Content Audit

Assess the quality, relevance, and performance of existing content.

**Content audit methodology:**

1. Inventory existing content — compile all indexable pages with their metadata (title, description, H1, word count, publish date, last updated)
2. Classify each page by performance:

| Category | Criteria | Action Direction |
| --- | --- | --- |
| **Performing** | Rankings + traffic + conversions meeting targets | Maintain and optimise incrementally |
| **Underperforming** | Has impressions but low CTR or declining traffic | Optimise — improve title, meta, content quality |
| **Thin** | Low word count, limited depth, no unique value | Expand, consolidate, or remove |
| **Cannibalising** | Multiple pages competing for the same keyword | Consolidate into a single authoritative page |
| **Decaying** | Previously performed well, now declining | Refresh — update data, expand coverage, re-promote |
| **Orphaned** | No internal links pointing to it | Add internal links or assess whether to keep |

1. For each underperforming or decaying page, document:

```
CONTENT AUDIT — PAGE:
  URL:            [page URL]
  Target keyword: [primary keyword — from SEO tools or user input]
  Current position: [ranking — from SEO tools]
  Impressions:    [from search console]
  Clicks:         [from search console]
  CTR:            [from search console]
  Traffic trend:  [growing / stable / declining — from analytics]
  Content quality: [assessment based on depth, freshness, uniqueness]
  Recommendation: [optimise / refresh / consolidate / remove]
```

### Phase 3: Keyword Analysis

Identify keyword opportunities — terms where the site can realistically improve rankings or capture new traffic.

**Keyword opportunity methodology:**

1. Current keyword portfolio — from SEO tools, list all keywords the site currently ranks for with position, search volume, and traffic contribution
2. Gap identification:

| Opportunity Type | Definition | How to Find |
| --- | --- | --- |
| **Quick wins** | Ranking positions 4–20 with meaningful search volume | Filter current rankings by position range |
| **Content gaps** | Keywords with search volume where the site has no ranking content | Keyword gap analysis in SEO tools |
| **Long-tail expansion** | Specific variations of keywords where the site already ranks for the head term | Related keyword analysis, "People also ask" data |
| **Emerging topics** | Growing search trends in the site's domain | Trend analysis, search console rising queries |
| **Competitor keywords** | Terms competitors rank for that this site does not | Competitor keyword gap analysis |

1. For each opportunity, document:

```
KEYWORD OPPORTUNITY:
  Keyword:          [term]
  Search volume:    [from SEO tools — never generate this]
  Current ranking:  [position, or "not ranking"]
  Difficulty:       [from SEO tools — never generate this]
  Opportunity type: [quick win / content gap / long-tail / emerging / competitor]
  Existing content: [URL if the site has relevant content, or "none"]
  Recommended action: [optimise existing page / create new content / add to existing content]
  Business relevance: [high / medium / low — how closely does this align with business goals?]
  Priority:         [from prioritisation framework in Phase 5]
```

### Phase 4: Competitor Benchmarking

Benchmark the site's SEO performance against key competitors to identify relative strengths and weaknesses.

**Competitor selection:**

- Identify 3–5 competitors: direct business competitors AND search competitors (sites that rank for the same keywords but may not be direct business competitors)
- Source: user input for business competitors; SEO tools for search competitors

**Benchmarking dimensions:**

| Dimension | Metrics to Compare | Data Source |
| --- | --- | --- |
| Domain authority / strength | Domain rating, domain authority, or equivalent | SEO tools |
| Keyword overlap | % of shared keywords, unique keywords per competitor | SEO tools |
| Content volume | Number of indexed pages, content publishing frequency | SEO tools / manual check |
| Backlink profile | Total referring domains, quality distribution, link velocity | SEO tools |
| SERP feature presence | Featured snippets, knowledge panels, image results, video results | SEO tools / manual search |
| Content depth | Average content length, topic coverage breadth | SEO tools / manual assessment |

**Benchmark output format:**

```
COMPETITOR BENCHMARK:
  Competitor:     [name / domain]
  Relationship:   [direct competitor / search competitor / both]

  Where they outperform us:
  - [Dimension]: [specific evidence from data]
  - [Dimension]: [...]

  Where we outperform them:
  - [Dimension]: [specific evidence from data]
  - [Dimension]: [...]

  Key content they have that we lack:
  - [Topic / keyword]: [their URL, ranking, estimated traffic]

  Actionable takeaway:
  - [Specific, data-backed action]
```

### Phase 5: Prioritised Recommendations

Synthesise findings from all phases into a prioritised action plan.

**Prioritisation framework:**

Score each recommendation on three dimensions:

| Dimension | Score 1 (Low) | Score 2 (Medium) | Score 3 (High) |
| --- | --- | --- | --- |
| **Impact** | Marginal traffic or ranking improvement | Moderate improvement to target keywords | Significant traffic, ranking, or conversion impact |
| **Effort** | Significant development or content effort | Moderate effort — days, not weeks | Quick fix — hours, not days |
| **Confidence** | Hypothesis — limited supporting data | Directional — some data supports this | Strong evidence from data |

**Priority = Impact × Effort × Confidence** (max 27). Execute highest-scoring actions first.

**Recommendation output format:**

```
RECOMMENDATION [N]:
  Finding:      [What the audit revealed]
  Phase:        [Technical / Content / Keyword / Competitor]
  Action:       [Specific, actionable recommendation]
  Impact:       [1–3] — [rationale]
  Effort:       [1–3] — [rationale]
  Confidence:   [1–3] — [rationale]
  Priority score: [calculated]
  Owner:        [who should execute — SEO, content, engineering]
  Timeline:     [suggested timeframe]
```

## Output Template: SEO Audit Report

```
# SEO Audit Report — [Domain]
Date: [date]
Audit period: [date range of data analysed]
Auditor: [name]

## Executive Summary
  [3-5 sentences: overall SEO health assessment, top 3 opportunities, top 3 risks]

## Technical Health
  Critical issues: [count]
  High-priority issues: [count]
  [List of technical findings sorted by severity]

## Content Assessment
  Total pages audited: [count]
  Performing: [count] | Underperforming: [count] | Thin/remove: [count]
  [Top content findings]

## Keyword Opportunities
  Quick wins: [count]
  Content gaps: [count]
  [Top keyword opportunities sorted by priority]

## Competitor Landscape
  [Key competitor insights and gaps]

## Prioritised Action Plan
  [Top 10-15 recommendations sorted by priority score]

## Appendix
  [Detailed data tables, full keyword lists, technical crawl details]
```

## Guardrails

- Never generate SEO metric values (search volume, keyword difficulty, domain authority, traffic estimates, CTR by position). All data must come from your tools.
- Never guarantee ranking improvements or traffic outcomes. SEO results depend on many uncontrollable factors.
- Never present qualitative claims about keywords ("high volume", "low competition") without data from your tools.
- Flag outputs: `[From SEO data]` for tool-sourced data · `[Framework methodology]` for this skill's approach · `[AI analysis]` for model synthesis · `[Data needed]` for placeholders requiring real data.

> **Tip:** Request XLSX, DOCX, or Markdown output via companyFILES for a formatted, instantly shareable report.
