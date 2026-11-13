---
name: en-email-sequence
description: Design and draft multi-email sequences — onboarding, nurture, re-engagement — with branching logic and performance benchmarks. Use when building an automated email flow, optimising an existing sequence, or designing lifecycle communications. Trigger with "write email sequence for", "onboarding email flow", "nurture sequence for [segment]".
---

# Email Sequence Skill

Design multi-email automated sequences — from goal definition through sequence architecture with timing and branching logic to individual email drafts and performance benchmarks. For automated sequences only, not one-off campaigns or newsletters.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **ESP / marketing automation via MCP** (e.g. HubSpot, Mailchimp) | Existing sequences, segments, historical open/click data, personalisation tokens |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Lifecycle stages, lead scores, account data, enrollment triggers |
| **companyRAG / file upload** | Brand guidelines, tone-of-voice rules, past campaign briefs, product information |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Sequence Design Workflow

Follow these steps in order. Each step informs the next — rushing to drafting without defining the goal and mapping the sequence produces emails that do not work together as a system.

### Step 1: Define the Sequence Goal

Every sequence exists to move a recipient from a current state to a desired state. Define both.

```
SEQUENCE GOAL:
  Sequence name:   [descriptive name]
  Sequence type:   [onboarding / nurture / re-engagement / event-triggered / lifecycle]
  Entry trigger:   [what action or event enrolls someone in this sequence?]
  Current state:   [where is the recipient now? — e.g., signed up but not activated]
  Desired state:   [where should they be after the sequence? — e.g., completed first project]
  Primary metric:  [the ONE number that defines sequence success]
  Exit conditions: [what removes someone from the sequence — achieved goal, unsubscribed, enrolled in another sequence, time elapsed]
```

**Goal quality check:**

| Check | Question | If No |
| --- | --- | --- |
| Specific | Can you describe the desired state in one sentence? | Narrow the scope |
| Measurable | Can you track whether recipients reached the desired state? | Choose a trackable metric |
| Bounded | Does the sequence have a clear end? | Define exit conditions |
| Distinct | Is this goal different from other active sequences? | Merge or differentiate |

### Step 2: Select Sequence Type and Map Architecture

Use the sequence type router to determine the appropriate architecture pattern, then map the specific sequence.

#### Sequence Type Router

| Type | Entry Trigger | Typical Length | Core Pattern |
| --- | --- | --- | --- |
| **Onboarding** | Account creation, purchase, subscription start | 5–10 emails over 14–30 days | Progressive activation milestones |
| **Nurture** | Content download, webinar registration, lead score threshold | 4–8 emails over 3–8 weeks | Value delivery building to conversion ask |
| **Re-engagement** | Inactivity for defined period (30/60/90 days) | 3–5 emails over 10–21 days | Escalating urgency with final sunset |
| **Event-triggered** | Specific user action (cart abandonment, feature use, milestone) | 2–4 emails over 3–7 days | Contextual follow-up on the trigger event |
| **Lifecycle** | Time-based milestones (anniversary, renewal date approaching) | 3–6 emails over 2–4 weeks | Relationship reinforcement and expansion |

#### Architecture Mapping

For each email in the sequence, define:

```
SEQUENCE MAP:

Email 1: [Name / Purpose]
  Timing:     [Trigger + delay — e.g., "Immediately after signup" or "Day 3"]
  Goal:       [What should the recipient DO after reading this email?]
  Content theme: [Core message — not the full draft yet]
  CTA:        [Primary call to action]
  Branch after: [If recipient takes action → skip to Email X / exit. If no action → continue to Email 2]

Email 2: [Name / Purpose]
  Timing:     [Delay from previous email or trigger]
  Condition:  [Who receives this? — e.g., "Recipients who did NOT complete onboarding step 1"]
  Goal:       [...]
  Content theme: [...]
  CTA:        [...]
  Branch after: [...]

  ...continue for all emails in the sequence
```

**Timing guidelines by sequence type:**

| Type | Email 1 | Subsequent Emails | Final Email |
| --- | --- | --- | --- |
| Onboarding | Immediate | 1–3 days apart (faster early, slower later) | Day 14–30 depending on activation timeline |
| Nurture | Immediate or next day | 3–7 days apart | After full value delivery, before going stale |
| Re-engagement | Day 1 of inactivity threshold | 3–5 days apart | 14–21 days — final sunset notice |
| Event-triggered | Within 1 hour of trigger | 1–3 days apart | Within 7 days of trigger |

### Step 3: Draft Individual Emails

For each email in the sequence map, produce a draft. Each email must stand on its own (recipients may not read every email) while contributing to the sequence arc.

**Email draft structure:**

```
EMAIL [N]: [Name]
  Subject line:   [Primary option]
  Subject line B: [A/B test variant — change ONE element]
  Preview text:   [The text that appears after the subject in inbox view]

  ---

  [Salutation]

  [Opening — 1-2 sentences connecting to the recipient's context or the sequence trigger.
   Answer: why am I receiving this? why should I care?]

  [Body — 2-4 short paragraphs delivering on the email's content theme.
   One idea per paragraph. Short sentences. Scannable.]

  [CTA — clear, specific, single primary action.
   Button text: [action-oriented verb phrase]
   Link: [destination]]

  [Closing — 1-2 sentences. Set expectation for next email if appropriate.]

  [Signature]

  ---

  Notes for implementation:
  - Personalisation tokens: [list any merge fields used — e.g., {{first_name}}, {{company}}, {{product_feature}}]
  - Dynamic content: [any sections that vary by segment or behaviour]
  - Legal requirements: [unsubscribe link, physical address, any industry-specific disclosures]
```

**Email drafting principles:**

| Principle | Application |
| --- | --- |
| One email, one goal | Each email has a single primary CTA. Secondary links are acceptable but should not compete. |
| Progressive value | Each email in the sequence delivers value independent of whether prior emails were read. |
| Respect attention | Keep emails scannable. Use short paragraphs, bullet points, and clear visual hierarchy. |
| Earned escalation | Do not ask for high-commitment actions (purchase, demo, meeting) until value has been established. |
| Context awareness | Reference the trigger event or recipient's stage. Generic-feeling automated emails get ignored. |

### Step 4: Design Branching Logic

Define the decision points where the sequence adapts based on recipient behaviour.

**Standard branching patterns:**

| Trigger | Branch Action |
| --- | --- |
| Recipient completes the sequence goal | Exit sequence → move to next lifecycle stage |
| Recipient clicks CTA but does not convert | Branch to a follow-up email addressing common objections |
| Recipient opens but does not click | Resend with different subject line or CTA after 2–3 days |
| Recipient does not open 2+ consecutive emails | Reduce frequency or move to re-engagement sequence |
| Recipient unsubscribes | Exit immediately — legal requirement |
| Recipient enrolls in a higher-priority sequence | Pause or exit this sequence to prevent overlap |

**Branching documentation format:**

```
DECISION POINT: After Email [N]
  IF [condition — e.g., "clicked CTA and completed activation step"]
    THEN → [action — e.g., "Exit sequence, enroll in nurture sequence"]
  ELSE IF [condition — e.g., "opened but did not click"]
    THEN → [action — e.g., "Send Email N+1 (alternative CTA) after 2 days"]
  ELSE [default — e.g., "no open"]
    THEN → [action — e.g., "Send Email N+1 after 3 days"]
```

### Step 5: Set Performance Benchmarks

Define how sequence health will be monitored. All benchmarks must come from YOUR historical data or be established during a baseline period.

**Sequence health metrics:**

| Metric | What It Measures | Monitor At |
| --- | --- | --- |
| Sequence completion rate | % of enrolled recipients reaching the desired state | Sequence level |
| Per-email open rate | Engagement with individual emails | Email level |
| Per-email click rate | Action taken on individual emails | Email level |
| Drop-off rate | % who disengage at each step | Per-email transition |
| Time to goal | How long it takes completers to reach the desired state | Sequence level |
| Unsubscribe rate | Recipient opt-outs per email | Email level |

**Benchmark-setting process:**

1. If historical sequence data exists, use your own past performance as the baseline
2. If no historical data, run the sequence for 2–4 weeks as a baseline period before optimising
3. Set improvement targets as percentage gains over YOUR baseline — not against external benchmarks
4. Monitor weekly during the first month, then bi-weekly once the sequence is stable

**Diagnostic triggers:**

| Signal | Likely Cause | Investigation |
| --- | --- | --- |
| Low open rate on Email 1 | Subject line, sender name, or timing | A/B test subject lines; check send time |
| High opens but low clicks | Content-CTA mismatch or weak CTA | Review CTA clarity and relevance |
| Sharp drop-off after specific email | That email is not delivering value or is asking too much | Review content, timing, and ask level |
| High unsubscribes on a specific email | Perceived irrelevance or excessive frequency | Review targeting, personalisation, and timing |
| Overall low completion rate | Sequence goal too ambitious, wrong audience, or too many emails | Reassess goal, entry criteria, and sequence length |

## Anti-Patterns

Patterns that consistently undermine email sequence effectiveness:

| Anti-Pattern | Problem | Fix |
| --- | --- | --- |
| **Too many emails, too fast** | Recipient fatigue → unsubscribes and spam complaints | Space emails appropriately; fewer high-quality emails outperform many mediocre ones |
| **No clear exit condition** | Recipients loop or receive irrelevant emails after converting | Define exit conditions for every sequence |
| **Missing unsubscribe** | Legal non-compliance (GDPR, CAN-SPAM, CASL) | Every email must include a functioning unsubscribe mechanism — non-negotiable |
| **Generic "batch and blast" disguised as automation** | No personalisation or context awareness → low engagement | Use personalisation tokens, behavioural triggers, and segment-specific content |
| **CTA overload** | Multiple competing calls to action → decision paralysis | One primary CTA per email; secondary links de-emphasised |
| **All ask, no value** | Every email pushes for conversion → recipients disengage | Alternate between value-delivery and conversion-ask emails (aim for 3:1 ratio) |
| **No suppression rules** | Recipients in multiple sequences get overwhelmed | Implement frequency caps and sequence priority rules |
| **Ignoring time zones** | Emails arrive at inconvenient times → lower open rates | Send in recipient's local time zone when possible |

## Guardrails

- Never generate email performance benchmarks (open rates, click rates, conversion rates). All data must come from the user's email platform.
- Never claim "best" send times, "optimal" frequency, or "ideal" sequence length. These depend on the audience and must be tested.
- Without brand guidelines, use neutral professional tone and label copy as `[Draft — adapt to your brand voice]`.
- Flag outputs: `[From customer data]` for sourced data · `[Framework methodology]` for this skill's approach · `[Draft — adapt to your brand voice]` for copy requiring adaptation.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted, ready-to-share sequence.
