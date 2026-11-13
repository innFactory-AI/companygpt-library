---
name: en-outreach
description: Research a prospect then draft personalised outreach with research-backed hooks, subject-line variants, and follow-up sequences. Use when cold-emailing a prospect, writing LinkedIn outreach, or building a multi-touch sequence. Trigger with "draft outreach to [person/company]", "write cold email to", "outreach sequence for".
---

# Outreach Skill

Pair prospect intelligence with message crafting to produce personalised, multi-channel outreach — initial messages, subject-line variants, follow-up sequences, and LinkedIn connection requests. Prospect data comes from you, a connected MCP source, companyRAG collections, or file upload.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. Salesforce, HubSpot, Dynamics) | Prior interactions, deal history, contact status, do-not-contact flags |
| **Sales-engagement / enrichment tools via MCP** (e.g. LinkedIn, company website, news) | Role context, recent activity, company signals, mutual connections |
| **companyRAG collections** | ICP definitions, messaging frameworks, relevant proof points |
| **companyRAG / file upload** | Trigger events, public statements, shared interests, context material |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Outreach Workflow

```
1. CHECK existing relationship
   |
   +--> Search CRM for prospect and account
   |      EXISTING CONTACT --> Review history, last interaction, opt-out status
   |      PRIOR DEAL --> Adjust tone: re-engagement, not cold outreach
   |      NO RECORD --> Proceed as net-new outreach
   |
2. RESEARCH the prospect (person-level)
   |
   +--> Current role, tenure, and scope of responsibility
   +--> Recent professional activity (posts, talks, job change, promotion)
   +--> Stated priorities or challenges (interviews, panel quotes, blog posts)
   +--> Mutual connections or shared context (events, groups, alma mater)
   |
3. RESEARCH the account (company-level)
   |
   +--> Recent signals: funding, product launch, leadership change, hiring surge
   +--> Industry context: regulatory shifts, competitive moves, market trends
   +--> Technology stack indicators (if relevant to your solution)
   |
4. IDENTIFY personalisation hooks
   |
   +--> Match prospect/account signals to value propositions
   +--> Rank hooks by specificity and recency (see Hook Ranking below)
   +--> Select 1-2 primary hooks per message
   |
5. DRAFT message(s)
   |
   +--> Select channel and format (see Channel Routing below)
   +--> Apply message structure (see Message Architecture below)
   +--> Generate subject-line variants (email only)
   +--> Review against quality criteria
   |
6. BUILD follow-up sequence (if multi-touch)
   |
   +--> Design 3-5 touch sequence with varied angles
   +--> Space touches appropriately (see Sequence Architecture below)
   +--> Each touch adds new value or angle — never just "bumping" the thread
   |
7. COMPILE output (see Output Template below)
```

## Hook Ranking

Not all personalisation is equal. Rank hooks by impact:

| Rank | Hook Type | Example | Why It Works |
| --- | --- | --- | --- |
| 1 | **Trigger event + role match** | "Saw you just took over EMEA ops — that's when teams often evaluate..." | Timely + relevant to their new mandate |
| 2 | **Stated priority + your value** | "You mentioned [priority] at [event] — we help teams..." | Proves research + direct relevance |
| 3 | **Mutual connection referral** | "[Name] suggested I reach out because..." | Warm intro through trusted contact |
| 4 | **Company signal + implication** | "With [company]'s expansion into [market], teams often face..." | Shows you understand their business context |
| 5 | **Shared context** | "Fellow [group] member — noticed your post about..." | Genuine common ground |
| 6 | **Industry trend + specificity** | "Teams in [their specific sub-sector] are dealing with..." | Relevant but less personal |

Hooks ranked 1-3 are strong enough to open a message. Hooks ranked 4-6 are supporting context, better as second-sentence reinforcement.

## Channel Routing

| Channel | Best For | Length Guideline | Tone |
| --- | --- | --- | --- |
| **Email** | Detailed value prop, multi-stakeholder, formal industries | 80-150 words body | Professional |
| **LinkedIn message** | Peer-to-peer, tech/startup, after connection accepted | 50-80 words | Conversational |
| **LinkedIn InMail** | Cold outreach when no email, senior prospects | 60-100 words | Professional-casual |
| **LinkedIn connection request** | First touch, building network | Under 300 characters | Brief, specific |

## Message Architecture

Every outreach message follows this structure regardless of channel:

### Line-by-Line Framework

| Section | Purpose | Length |
| --- | --- | --- |
| **Opening line** | Personalised hook — why you are reaching out to them specifically | 1 sentence |
| **Context bridge** | Connect the hook to a problem or opportunity they likely face | 1-2 sentences |
| **Value statement** | What outcome you help achieve — not what your product does | 1 sentence |
| **Proof point** | Credibility signal — specific result, named customer, metric | 1 sentence (optional in short formats) |
| **Call to action** | Specific, low-friction ask | 1 sentence |

### Opening-Line Patterns (Select Based on Hook)

- Trigger: "I noticed [specific event] — when teams go through [change], they often..."
- Referral: "[Name] mentioned you're the right person to talk to about [topic]..."
- Content: "Your [post/talk] on [topic] resonated — especially the point about..."
- Observation: "Looking at how [company] is approaching [initiative], I had a thought about..."

### Call-to-Action Patterns

| CTA Type | When to Use | Example |
| --- | --- | --- |
| **Question CTA** | Discovery-stage, low commitment | "Is [specific problem] on your radar this quarter?" |
| **Meeting CTA** | When intent signals are present | "Worth a 20-minute conversation next week?" |
| **Resource CTA** | Nurture-stage, building credibility | "I put together a [brief/analysis] — want me to send it over?" |
| **Introduction CTA** | Multi-threaded, need different stakeholder | "Who on your team owns [function]?" |

## Subject-Line Methodology (Email Only)

Generate 3 subject-line variants per email, testing different angles:

| Variant Type | Pattern | Example |
| --- | --- | --- |
| **Trigger-based** | References the specific signal | "[Company]'s EMEA expansion + [topic]" |
| **Question-based** | Poses the problem as a question | "How is [company] handling [challenge]?" |
| **Outcome-based** | Leads with the result | "[Metric improvement] for [their industry] teams" |

Subject-line rules: under 50 characters preferred, no ALL CAPS, no spam-trigger words, no false urgency, no misleading Re: or Fwd: prefixes.

## Sequence Architecture

For multi-touch sequences, vary the angle with each touch:

| Touch | Timing | Angle | Channel |
| --- | --- | --- | --- |
| 1 | Day 0 | Primary hook + value statement | Email or LinkedIn |
| 2 | Day 3-4 | New proof point or case study angle | Same or alternate |
| 3 | Day 7-8 | Industry insight or resource offer | Alternate channel |
| 4 | Day 14 | Different stakeholder angle or referral ask | Email |
| 5 | Day 21-28 | Break-up: direct ask about fit/timing | Email |

### Sequence Rules

- Each touch must introduce new value or a new angle — never "just following up" or "bumping this".
- If the prospect responds at any point, exit the sequence and respond conversationally.
- Respect opt-out signals: explicit requests, auto-replies indicating leave, or company-level do-not-contact.
- Adjust timing for prospect seniority: C-suite gets longer gaps between touches.
- Maximum sequence length: 5 touches over 4 weeks for cold outreach.

## Output Template — Outreach Package

```
# Outreach: [Prospect Name] at [Company]
**Channel**: [Email / LinkedIn / Multi-channel]
**Sequence Length**: [Single message / X-touch sequence]
**Prospect Context**: [1-2 sentence summary of research]

## Research Summary
- **Role**: [Title, scope, tenure]
- **Signals**: [Key triggers identified — with dates and sources]
- **Hooks Selected**: [Ranked hooks chosen for this outreach]

## Message 1: Initial Outreach
**Subject Line Options** (email only):
1. [Variant A]
2. [Variant B]
3. [Variant C]

**Body**:
[Full message text — plain text, no markdown formatting]

---

## Message 2: Follow-Up 1
**Timing**: [Days after Message 1]
**Angle**: [What is new in this touch]

**Subject**: [Reply to thread or new subject]

**Body**:
[Full message text]

---

[Continue for each sequence touch]

## Personalisation Notes
- [Why specific hooks were chosen]
- [Alternative angles if these don't land]
- [Contacts to CC or reference if warming the thread]
```

## Guardrails

1. Never fabricate prospect details. All names, titles, company facts, and activity must come from CRM, enrichment, web search, or user input. If research is thin, use bracketed placeholders: "[insert specific signal]."
2. Never invent mutual connections. Only reference a mutual connection if confirmed by the user or CRM data.
3. Opt-out awareness. If CRM indicates opt-out, do-not-contact, or unsubscribed status, refuse to draft outreach and flag the restriction.
4. Source labeling. Tag research — [From CRM], [From LinkedIn], [From web search], [From user input], [AI draft].

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted outreach package ready to share.
