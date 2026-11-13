---
name: en-brand-voice
description: Review content against brand voice and style guidelines — flag deviations by severity with before/after improvement suggestions. Use when auditing marketing copy, onboarding a new content creator, or establishing brand voice documentation. Trigger with "review this against our brand voice", "check brand consistency", "audit this copy".
---

# Brand Voice Skill

Construct, audit, and govern brand voice frameworks — voice decomposition, tone adaptation, content scoring, and governance workflows. All voice traits must come from the customer's brand documentation or be co-created with the user.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CMS / content tools via MCP** (e.g. Contentful, WordPress, Notion) | Existing copy, published content per channel, content inventory |
| **Analytics / social tools via MCP** (e.g. GA4, LinkedIn, HubSpot) | Performance data, high- and low-performing content, channel context |
| **companyRAG collections** (esp. brand and style guides) | Brand guidelines, tone-of-voice rules, existing voice frameworks |
| **File upload** | Style guides, individual content pieces, stakeholder notes |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Voice Decomposition Methodology

Systematic process for breaking a brand voice into measurable, scorable components.

### Step 1: Identify Core Voice Traits

Extract 3-5 core voice traits from brand guidelines or stakeholder input.

Rules:

- Each trait is a spectrum, not a binary (e.g., "formal <-> casual" with positions 1-5)
- Traits must be independent -- adjusting one should not logically require adjusting another
- Validation test: shifting a trait by 2 points should produce a noticeably different content feel
- If fewer than 3 traits emerge, the brand guidelines may be incomplete -- flag to user

### Step 2: Define Each Trait

For each identified trait, complete this template:

| Element | Description |
| --- | --- |
| Trait name | One word or short phrase |
| Definition | What this trait means for this brand (1 sentence) |
| Scale | 1-5 intensity with labeled endpoints |
| Default position | Where the brand sits on the scale normally |
| Do examples | 2-3 phrases that exemplify this trait at the default position |
| Don't examples | 2-3 phrases that violate this trait |
| Channel modulations | How the intensity shifts per channel (see tone adaptation matrix) |

Fill-in format per trait:

```
TRAIT: [name]
DEFINITION: [one sentence]
SCALE:
  1 = [low-end label]
  2 = [description]
  3 = [midpoint label]
  4 = [description]
  5 = [high-end label]
DEFAULT POSITION: [1-5]
DO:
  - "[example phrase at default position]"
  - "[example phrase at default position]"
DON'T:
  - "[example phrase that violates this trait]"
  - "[example phrase that violates this trait]"
```

### Step 3: Construct Vocabulary Guidelines

Define: preferred terms, avoided terms (with rationale), jargon policy, contraction policy, and sentence structure preferences. Capture them in a short structured block (e.g., **Preferred terms** / **Avoid** / **Jargon** / **Contractions** / **Sentence shape**) so they stay auditable alongside the trait definitions in Step 2.

CRITICAL: Voice traits MUST come from customer brand guidelines or be explicitly co-created with the user. Never generate traits from training data. If co-creating, label output: "These traits are being co-created in this conversation and should be validated against your full brand guidelines."

## Tone Adaptation Matrix

### Matrix Structure

| Context | Trait 1 shift | Trait 2 shift | ... | When to use |
| --- | --- | --- | --- | --- |
| Crisis communication | [direction + magnitude] | ... | ... | Active incidents, public statements |
| Product launch | ... | ... | ... | New product/feature announcements |
| Customer support | ... | ... | ... | Help docs, support responses |
| Thought leadership | ... | ... | ... | Blog posts, conference talks, research |
| Social media | ... | ... | ... | Short-form, conversational contexts |
| Legal/compliance | ... | ... | ... | Terms, policies, regulatory communications |

### Construction Process

1. List the brand's communication contexts (use the standard set above as starting point, add/remove as needed)
2. For each context, determine which traits modulate and in which direction
3. Define the magnitude of shift (use +1, +2, -1, -2 relative to the default position on the 5-point scale)
4. Validate: does the modulated voice still feel like the same brand? If a shift exceeds +/-2, the result may break brand coherence
5. Document exceptions -- contexts where a trait is intentionally pushed to an extreme (e.g., legal copy at maximum formality)

### Shift Notation

```
CONTEXT: [name]
TRAIT SHIFTS:
  [Trait 1]: [default] -> [shifted] ([+/-N], [rationale])
  [Trait 2]: [default] -> [shifted] ([+/-N], [rationale])
  [Trait 3]: no shift
WHEN TO USE: [specific triggers or content types]
EXAMPLE: "[short example sentence showing the modulated voice]"
```

### Matrix Validation

After constructing the matrix, validate with these checks:

| Check | Question | If No |
| --- | --- | --- |
| Coherence | Does each row still sound like the brand? | Reduce shift magnitude |
| Coverage | Are all major communication contexts represented? | Add missing rows |
| Distinctness | Do different contexts actually produce different modulations? | Merge similar contexts |
| Boundary safety | Are any shifts pushing past the 1-5 scale bounds? | Cap at endpoints |

## Content Audit Scoring

Systematic process for evaluating existing content against the voice framework.

CRITICAL: Always QUOTE the specific text being evaluated before assigning any score. No vague assessments.

### Step 1: Select Content Sample

Choose a representative sample, not an exhaustive inventory:

- Include all active channels
- Include both recent and older content
- Include high-performing and underperforming pieces
- Minimum: 2-3 pieces per channel for pattern detection

### Step 2: Per-Trait Scoring

For each content piece, score each voice trait:

| Trait | Target position | Actual position (1-5) | Evidence (quote the text) | Gap |
| --- | --- | --- | --- | --- |
| [trait name] | [from framework] | [scored] | "[quoted text]" | [difference] |

CRITICAL: Always QUOTE the specific text being evaluated before assigning a score. No vague assessments like "the content feels off-brand" or "the tone doesn't match."

### Step 3: Aggregate Scores

Three levels of aggregation:

| Level | Calculation | Reveals |
| --- | --- | --- |
| Per-piece score | Average across traits (weighted by trait importance if defined) | Individual content quality |
| Per-trait gap analysis | Average gap per trait across all pieces | Which traits consistently deviate |
| Per-channel pattern | Average scores grouped by channel | Whether deviations correlate with channels |

### Step 4: Gap Identification and Remediation

Priority matrix for action:

| Gap size | Strategic importance | Action |
| --- | --- | --- |
| Large (>2) | High | Immediate rewrite |
| Large (>2) | Low | Schedule rewrite |
| Small (<=1) | High | Minor adjustment |
| Small (<=1) | Low | Accept or batch |

Additional remediation triggers:

- Same trait off-target across 3+ pieces -> systemic issue (training, process, or unclear guidelines)
- Same channel consistently off-target -> channel-specific guidance needed in the tone adaptation matrix
- Vocabulary violations -> update the preferred/avoided terms list or improve distribution

Use the scoring dimensions above to build a detailed assessment worksheet for each content piece.

## Multi-Brand Voice Architecture

Methodology for managing voice frameworks across brand hierarchies.

### Parent/Child Model

- Parent brand defines core traits and non-negotiable trait positions (minimum and maximum bounds)
- Child brands inherit core traits but can:   - (a) Add 1-2 brand-specific traits unique to their audience   - (b) Shift default positions within defined bounds   - (c) Define their own channel modulations within the tone adaptation matrix
- Governance rule: a child brand's content should be identifiable as part of the parent family even without explicit branding

### Architecture Decision Tree

| Scenario | Approach | Voice Framework Count |
| --- | --- | --- |
| Single brand, multiple products | One voice framework, product-specific tone modulations | 1 framework + product modulation rows |
| Brand house (parent + named sub-brands) | Parent framework + child variation rules | 1 parent + N child overlays |
| House of brands (independent brands) | Separate frameworks, shared governance process | N independent frameworks |
| Acquired brand in transition | Dual framework with convergence roadmap | 2 frameworks + timeline |

### Brand Hierarchy Documentation

```
PARENT BRAND: [name]
CORE TRAITS (non-negotiable):
  [Trait 1]: bounds [min]-[max] on 5-point scale
  [Trait 2]: bounds [min]-[max] on 5-point scale
SHARED VOCABULARY: [terms that all child brands must use/avoid]

CHILD BRAND: [name]
INHERITS: [parent name]
TRAIT OVERRIDES:
  [Trait 1]: default = [N] (within parent bounds [min]-[max])
  [Additional trait]: [definition and scale] (child-specific)
AUDIENCE: [how this child's audience differs from parent]
CHANNEL FOCUS: [primary channels for this child brand]
```

### Convergence Roadmap (Acquired Brands)

| Phase | Duration | Action |
| --- | --- | --- |
| Assessment | Weeks 1-2 | Audit acquired brand voice against parent framework; identify gaps |
| Alignment | Weeks 3-8 | Align non-negotiable traits; preserve acquired brand's distinctive traits where they add value |
| Integration | Months 3-6 | Migrate to parent framework with approved child-brand variations |
| Governance | Ongoing | Include in standard voice compliance review cycle |

## Content Governance Workflow

Pre-publication voice compliance review process. Score each trait, then route based on the gap table below.

### Escalation Triggers

| Finding | Action |
| --- | --- |
| All traits within range | Approve |
| 1 trait off by 1 point | Minor note, approve |
| 1+ traits off by 2+ points | Revise before publication |
| Vocabulary violation | Revise before publication |
| Inconsistent within campaign | Revise outlier pieces |

### Governance Cadence

| Activity | Frequency | Scope |
| --- | --- | --- |
| Pre-publication review | Every piece (or sample for high-volume channels) | Individual content |
| Channel audit | Quarterly | All content on one channel |
| Full brand audit | Annually or after brand refresh | All channels, all content types |
| Framework update | After audit findings or brand strategy changes | Voice framework and tone matrix |

## Reference Material

- Voice framework template -- use when building or reviewing a brand voice framework
- Content audit rubric -- use when auditing content against a voice framework

Upload these templates as files when needed, or place them in a companyRAG collection so the skill can draw on them.

## Guardrails

- Never generate brand voice traits from training data. Traits must come from customer brand guidelines or be explicitly co-created (and labelled as such).
- Always quote the specific text being evaluated before assigning any score. No vague assessments like "the content feels off-brand."
- Default to "not specified in brand guidelines" when a trait or preference hasn't been defined. Never fill gaps with assumptions.
- Flag outputs: `[From brand guidelines]` for brand docs · `[From customer data]` for other sources · `[Framework methodology]` for this skill's approach · `[AI suggestion]` for model recommendations.

> **Tip:** Request DOCX or Markdown output via companyFILES to get a formatted, instantly shareable voice report or framework document.
