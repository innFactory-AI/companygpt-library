---
name: en-process-optimization
description: Analyse processes for bottlenecks, waste, and improvement opportunities with throughput measurement and prioritised recommendations. Use when a process feels slow, investigating inefficiencies, or preparing a process improvement initiative. Trigger with "optimise this process", "find bottlenecks in", "how can we improve".
---

# Process Optimization Skill

Analyse processes for bottlenecks and waste, then recommend measurable improvements with prioritised roadmaps. Process data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project / issue tracker via MCP** (e.g. Jira, Asana, Monday) | Processing and elapsed times, status dwell times, volumes, send-backs |
| **Workflow / CRM system via MCP** (e.g. HubSpot, Salesforce, ServiceNow) | Approval chains, handoffs, SLA data, error and rework rates |
| **companyRAG collections / file upload** | Process documentation, runbooks, audit logs, time and cost exports |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Process Analysis Methodology

### Current State Mapping

Before optimising, map the process as it actually operates — not as it is documented or intended to operate:

1. Walk the process end-to-end: Document every step, decision point, handoff, wait state, and rework loop as they actually occur.
2. Identify participants: Who touches the process at each stage — roles, not just departments.
3. Capture timing: For each step, record processing time (active work) and elapsed time (calendar time including waits). The gap between the two reveals queue time and delays.
4. Note volumes: How many items flow through the process per period — total and by variant.
5. Mark pain points: Where do participants report frustration, errors, or workarounds? These are optimisation signals.

### Throughput Measurement

Establish baseline metrics before recommending changes:

```
PROCESS BASELINE:
  Process:            [name]
  Measurement period: [date range]
  Volume:             [items processed per period]
  Cycle time:         [average end-to-end elapsed time]
  Processing time:    [average active work time per item]
  Process efficiency: [processing time ÷ cycle time × 100]%
  Error/rework rate:  [% of items requiring rework or correction]
  First-pass yield:   [% of items completing correctly on first pass]
  Cost per item:      [total process cost ÷ volume, if data available]
```

Process efficiency ratio reveals how much time is spent on value-adding work versus waiting. A process with 2 hours of active work time and 5 days of cycle time has a process efficiency of approximately 5% — most time is waiting, not working.

## Waste Identification

### Eight Wastes Framework

Adapted from lean methodology for knowledge work and business processes:

| Waste Type | Definition | Process Indicators |
| --- | --- | --- |
| **Waiting** | Idle time between steps — queues, approvals, information requests | Items sitting in inboxes, approval backlogs, "waiting for [person]" status |
| **Overprocessing** | Doing more than needed — unnecessary detail, redundant checks, gold-plating | Reports nobody reads, approvals that never reject, data collected but unused |
| **Rework** | Correcting errors from previous steps | High rejection rates, frequent revision cycles, "send back" patterns |
| **Handoff friction** | Information lost or degraded during transfers between people/teams | Repeated questions, context re-gathering, "I didn't know that" moments |
| **Motion** | Unnecessary movement between tools, systems, or formats | Copy-pasting between systems, manual data entry, format conversions |
| **Overproduction** | Producing more output or more frequently than the downstream consumer needs | Batch sizes larger than needed, reports generated more frequently than consumed |
| **Inventory** | Work items accumulating between steps — work-in-progress buildup | Growing backlogs, aging items, items started but not finished |
| **Unused talent** | People performing work below their capability, or expertise not leveraged | Senior staff on routine tasks, specialist knowledge not consulted |

### Waste Assessment

For each identified waste:

```
WASTE ITEM:
  Type:          [from eight wastes]
  Location:      [which step or between which steps]
  Description:   [what specifically is happening]
  Frequency:     [how often — every item, occasionally, specific conditions]
  Impact:        [time, cost, or quality effect per occurrence]
  Root cause:    [why this waste exists — not just what, but why]
  Evidence:      [data supporting the assessment — times, volumes, error rates]
```

## Bottleneck Detection

### Identification Methods

A bottleneck is the step that constrains the throughput of the entire process. The process can only move as fast as its slowest step.

**Method 1 — Queue observation**: The step with the longest queue upstream is likely the bottleneck. Work accumulates before the constraint.

**Method 2 — Utilisation analysis**: The step where resources are most heavily utilised (closest to 100%) is the constraint. Other steps have idle capacity.

**Method 3 — Flow rate comparison**: Measure throughput at each step independently. The step with the lowest throughput rate limits the process.

### Bottleneck Classification

| Type | Cause | Example | Resolution Approach |
| --- | --- | --- | --- |
| **Resource bottleneck** | Not enough people, tools, or capacity at the step | Single approver for all requests | Add capacity, redistribute, or reduce demand |
| **Policy bottleneck** | Rules or requirements that constrain flow unnecessarily | Approval required for items below a reasonable threshold | Challenge the policy — does it still serve its purpose? |
| **Dependency bottleneck** | Step blocked by external input or upstream delivery | Waiting for third-party data before proceeding | Decouple, parallelize, or pre-fetch the dependency |
| **Batching bottleneck** | Work held until a batch accumulates before processing | Monthly invoice processing when weekly would flow better | Reduce batch size or process continuously |
| **Knowledge bottleneck** | Only specific people have the expertise to perform the step | Single subject-matter expert required for every review | Cross-train, document, or redesign to reduce specialisation requirement |

## Improvement Identification

### Improvement Categories

| Category | Description | Typical Impact | Typical Effort |
| --- | --- | --- | --- |
| **Eliminate** | Remove the step entirely — it adds no value | High | Low (often just a decision) |
| **Automate** | Replace manual work with system-driven execution | High | Medium–High |
| **Simplify** | Reduce complexity — fewer fields, simpler rules, shorter forms | Medium | Low–Medium |
| **Parallelize** | Run sequential steps simultaneously where no true dependency exists | Medium | Low–Medium |
| **Reduce batch size** | Process smaller batches more frequently for faster flow | Medium | Low |
| **Standardise** | Align variations into a single consistent approach | Medium | Medium |
| **Relocate** | Move the step earlier or later in the process for better flow | Low–Medium | Low |

### Five Whys Root Cause Analysis

For each significant waste or bottleneck, apply root cause analysis before recommending solutions:

```
PROBLEM: [symptom observed]
  Why 1: [first-level cause]
  Why 2: [cause of the first-level cause]
  Why 3: [deeper cause]
  Why 4: [even deeper cause]
  Why 5: [root cause — the systemic issue to address]
  Root cause: [summary — this is what needs to change]
```

Stop when you reach a cause that is actionable and systemic. Not every chain goes to five levels; stop when you reach the actionable root.

## Impact Estimation

### Before/After Projection

For each recommended improvement, project the impact:

```
IMPROVEMENT PROJECTION:
  Improvement:         [specific change]
  Addresses:           [which waste/bottleneck]
  Current metric:      [baseline from throughput measurement]
  Projected metric:    [expected value after improvement]
  Improvement:         [delta and percentage change]
  Confidence:          [High / Medium / Low — based on data quality]
  Assumptions:         [what must be true for this projection to hold]
  Measurement method:  [how you will verify the improvement after implementation]
```

Mark all projections as [AI projection — verify with process data]. Never present projections as certainties.

### Prioritisation Matrix

Rank improvements using impact vs. effort:

|  | High Impact | Medium Impact | Low Impact |
| --- | --- | --- | --- |
| **Low Effort** | **Do first** — quick wins | **Do second** — easy value | **Consider** — marginal gains |
| **Medium Effort** | **Plan** — significant projects | **Evaluate** — weigh cost/benefit | **Defer** — limited return |
| **High Effort** | **Strategise** — major investment | **Deprioritise** — poor ratio | **Avoid** — minimal return for high cost |

## Output Template

```
# Process Optimisation Report — [Process Name]

## Executive Summary
- Current performance: [key baseline metrics]
- Primary bottleneck: [the main constraint]
- Top waste category: [biggest source of waste]
- Recommended improvements: [count and projected total impact]
- Quick wins: [improvements achievable within 2 weeks]

## Current State Analysis
- Process map: [step-by-step current state with timing]
- Baseline metrics: [throughput measurement results]
- Process efficiency: [ratio]

## Waste Assessment
[Waste items with type, location, frequency, impact, root cause]

## Bottleneck Analysis
[Identified bottlenecks with classification and evidence]

## Improvement Recommendations
[Prioritised list with impact projections]

## Implementation Roadmap
- Phase 1 (Quick wins): [low-effort improvements to implement immediately]
- Phase 2 (Planned): [medium-effort improvements with timeline]
- Phase 3 (Strategic): [high-effort improvements requiring investment decision]

## Success Metrics
[How to measure whether the optimisation achieved its goals — re-measure baseline metrics post-implementation]

## Assumptions and Limitations
[What data was available, what was estimated, what requires validation]
```

## Guardrails

- Never generate cycle times, throughput rates, or cost figures from training data. All metrics come from the user's process data.
- Never claim benchmarks. "Industry benchmark" and "best-in-class" are meaningless without the user's specific context.
- Never present projections as guaranteed outcomes. All projections are estimates requiring post-implementation measurement.
- Label generated content: `[From process data]`, `[Framework methodology]`, `[AI projection — verify with process data]`.

> **Tip:** Ask for DOCX, XLSX, or Markdown output via companyFILES to get a formatted optimisation report ready to share.
