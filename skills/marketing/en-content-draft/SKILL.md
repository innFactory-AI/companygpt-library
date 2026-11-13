---
name: en-content-draft
description: Generate first drafts across content types — blog posts, social media, emails, landing pages, press releases, case studies — with channel best practices baked in. Use when writing marketing content, creating first drafts for review, or adapting content across channels. Trigger with "draft a blog post about", "write social copy for", "landing page for [product]".
---

# Content Draft Skill

Generate first-draft marketing content across six content types. Each type follows channel-specific best practices for structure, length, and tone. Output is always a working first draft ready for human review and refinement — not a final publish-ready piece.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CMS via MCP** | Existing content for tone matching and internal linking |
| **Brand guidelines via companyRAG / file upload** | Voice, tone, terminology, visual style rules |
| **Analytics via MCP** | Top-performing content patterns for the audience |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

---

## Workflow

### Step 1: Gather Brief

Before drafting, clarify:

1. Content type — blog post, social media, email, landing page, press release, or case study
2. Topic or subject — what is this about?
3. Target audience — who reads this? (persona, job role, stage in funnel)
4. Goal — what should the reader do or feel after reading? (awareness, click, sign up, share)
5. Key messages — 1-3 points that must be communicated
6. Tone — formal, conversational, playful, authoritative? (load brand guidelines if available)
7. Constraints — word count, required CTAs, SEO keywords, compliance disclaimers

Proceed with partial answers. Note assumptions.

### Step 2: Route by Content Type

Each content type has different structural requirements:

**Blog Post**

- Length: 800-2000 words depending on depth
- Structure: Hook → Context → Main argument (with subheadings) → Takeaway → CTA
- Include: H2/H3 hierarchy, scannable paragraphs (3-4 sentences max), one CTA
- SEO: Target keyword in title, H1, first 100 words, meta description
- Tone: Match the publication's voice; default to informative and approachable

**Social Media**

- Produce variants for each platform requested:   - LinkedIn: 150-300 words, professional, hook in first line, 3-5 hashtags   - X/Twitter: Under 280 characters, punchy, optional thread format for longer content   - Instagram: Caption 125-200 words, visual hook, relevant hashtags (10-15)
- Structure: Hook line → Value → CTA
- Include: 2-3 variants per platform with different angles

**Email**

- Length: 150-400 words body text
- Structure: Subject line (3-5 variants) → Preview text → Opening hook → Body → CTA → P.S.
- Plain text only — no markdown formatting (asterisks and underscores render as raw characters in most email clients)
- Subject lines: Under 50 characters, create urgency or curiosity without clickbait

**Landing Page**

- Structure: Headline → Subheadline → Hero section → Benefits (3-5) → Social proof placeholder → CTA → FAQ
- Copy style: Benefit-driven, scannable, action-oriented
- Include: Primary CTA copy and secondary CTA copy
- SEO: Target keyword in headline and meta description

**Press Release**

- Structure: Headline → Dateline → Lead paragraph (who, what, when, where, why) → Body (quotes, context, details) → Boilerplate → Contact info
- Tone: Factual, third-person, newsworthy angle
- Length: 400-600 words
- Include: One executive quote, one supporting quote (customer/partner if applicable)

**Case Study**

- Structure: Customer overview → Challenge → Solution → Results → Quote → CTA
- Results: Quantified where possible (%, time saved, revenue impact)
- Length: 600-1200 words
- Tone: Factual but narrative; let the customer be the hero

### Step 3: Research and Hook

Before writing:

1. Search for relevant context if connected sources are available
2. Identify the strongest hook — what makes this worth reading?
3. Check for competing content on the same topic — what angle is not yet covered?

Hook types:

- Contrarian: Challenge a common assumption
- Data-led: Open with a surprising statistic
- Story: Start with a specific scenario the reader recognises
- Question: Ask a question the reader wants answered
- Urgency: Frame a time-sensitive opportunity or risk

### Step 4: Draft

Write the full draft following the content type structure. Apply these principles:

- Lead with value — the reader's benefit comes before your product
- One idea per paragraph — don't stack multiple points
- Active voice — "We launched..." not "It was launched by..."
- Specific over general — "37% faster" not "significantly faster"
- Show, don't tell — examples and scenarios over abstract claims

### Step 5: Self-Review

Before presenting the draft, check:

- Does the opening hook earn the next sentence?
- Is the key message clear within the first 20% of the content?
- Does every section serve the stated goal?
- Is the CTA specific and actionable?
- Does the tone match the brand/audience?
- Are all claims supported by provided facts (not fabricated)?
- Is it the right length for the content type?

---

## Output Format

Present the draft with clear metadata:

```
## [Content Type]: [Title / Subject]

**Audience:** [Target reader]
**Goal:** [Desired action or outcome]
**SEO keyword:** [If applicable]
**Word count:** [Approximate]

---

[Full draft content here]

---

**Notes:**
- [Assumptions made]
- [Sections that need client input — quotes, data, approval]
- [Suggested visuals or supporting assets]
```

---

## Guardrails

- Never fabricate statistics, quotes, or case study results. Use only data from the user; mark placeholders clearly: [INSERT: customer quote about results].
- No markdown formatting in email drafts. Email clients render asterisks and underscores as raw characters — use plain text and line breaks.
- Skip generic openings. "In today's fast-paced world…" and "Are you looking for…" — start with the hook.
- Ask about the audience before drafting. A blog post for CTOs reads very differently from one for junior developers.

---

## After Drafting

Ask:

- "Want me to create variants for a different channel?"
- "Should I write the social media posts to promote this blog post?"
- "Want me to optimise this draft for a specific SEO keyword?"
- "Should I adapt this for a different audience segment?"
- "Want me to check this against your brand voice guidelines?"

> **Tip:** Request DOCX or Markdown output via companyFILES to get a formatted, instantly shareable draft.
