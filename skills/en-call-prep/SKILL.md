---
name: en-call-prep
description: Build a comprehensive call brief from CRM, calendar, and email context — attendees, deal history, open questions, recommended angles. Use when preparing for a sales call, demo, or customer meeting. Trigger with "prep call with [person/company]", "call brief for", "what should I know before this meeting".
---

# Call Prep Skill

Combine CRM context, attendee intelligence, and deal history into a concise, actionable call brief. The skill produces briefs, attendee profiles, objective-setting worksheets, and talking-point sequences. All deal data and contact information comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. Salesforce, HubSpot, Dynamics) | Deal stage, history, contact roles, notes, past activity timeline |
| **Calendar via MCP** (e.g. Google Calendar, Outlook) | Meeting time, attendees, agenda, recurring pattern |
| **Email via MCP** (e.g. Gmail, Outlook) | Recent correspondence, open threads, tone of last exchange |
| **companyM365** (if enabled) | Outlook calendar and mail, plus people lookup from your Microsoft 365 account |
| **companyRAG collections** | Discovery frameworks, objection libraries, relevant proof points |
| **Web search via MCP** (e.g. LinkedIn, company news) | Attendee background, recent company signals |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Call-Prep Workflow

```
1. GATHER meeting context
   |
   +--> Pull calendar event: time, attendees, agenda
   +--> Check CRM for deal record: stage, value, history, last activity
   +--> Scan recent emails with attendees for open threads or tone shifts
   |
2. RESEARCH attendees
   |
   +--> For each attendee:
   |      +--> CRM contact record (role, past interactions, notes)
   |      +--> Buying center role classification (from deal strategy if available)
   |      +--> Recent professional context (promotion, role change, public posts)
   |      +--> Communication style cues (formal/informal, detail-oriented/big-picture)
   |
3. REVIEW deal history
   |
   +--> Timeline of key interactions (meetings, proposals, follow-ups)
   +--> Commitments made by both sides (and whether fulfilled)
   +--> Open objections or unresolved concerns from prior calls
   +--> Competitive mentions or alternative-evaluation signals
   |
4. SET call objectives
   |
   +--> Primary objective: the one outcome that makes this call a success
   +--> Secondary objectives: additional ground to cover if time allows
   +--> Minimum viable outcome: the floor — what you must leave with at minimum
   +--> Progression marker: what deal-stage advancement looks like after this call
   |
5. BUILD talking-point sequence
   |
   +--> Map talking points to objectives (see Talking-Point Sequencing below)
   +--> Prepare questions for each attendee's role
   +--> Pre-load objection responses for known concerns
   +--> Identify proof points and references to have ready
   |
6. COMPILE call brief (see Output Template below)
```

## Attendee Analysis

For each meeting participant, build a concise profile:

| Field | Description |
| --- | --- |
| **Name & Title** | Current role — verify against CRM and LinkedIn |
| **Buying Center Role** | Economic Buyer, Champion, Technical Evaluator, End User, Blocker, Other |
| **Relationship History** | Prior meetings, correspondence summary, rapport level |
| **Known Priorities** | What they care about — stated goals, evaluation criteria, pain points |
| **Communication Style** | Formal / casual, detail-oriented / big-picture, consensus / decisive |
| **Watch-Outs** | Unresolved objections, past friction, competing priorities |

When attendee data is thin, note the gap: "Limited background — plan discovery questions for this contact."

## Objective-Setting Framework

Every call needs a tiered objective structure:

| Tier | Definition | Example |
| --- | --- | --- |
| **Primary Objective** | The ideal outcome — advancing the deal to a defined next milestone | "Secure agreement to a technical proof-of-concept by [date]" |
| **Secondary Objectives** | Valuable side-outcomes worth pursuing if the call allows | "Confirm budget timeline; identify procurement contact" |
| **Minimum Viable Outcome** | The floor — the least you must walk away with | "Schedule a follow-up with the technical team present" |
| **Progression Marker** | What evidence of forward motion looks like after this call | "Mutual Action Plan shared and accepted" |

If the user does not specify objectives, infer them from the deal stage and attendee composition, but flag them as "[AI-suggested — confirm before call]".

## Talking-Point Sequencing

Structure the conversation flow based on call type:

### Discovery Call

1. Context set (2 min): Confirm what you know, show preparation
2. Situation exploration (10-15 min): Open questions about current state
3. Problem surfacing (10-15 min): Dig into pain points and implications
4. Value connection (5 min): Bridge their pain to your capability — questions, not pitches
5. Next-step commitment (3 min): Propose specific next action with date

### Demo / Presentation Call

1. Recap and agenda confirm (3 min): Restate what they asked to see and why
2. Tailored demonstration (15-20 min): Map features to their stated priorities
3. Reaction check (5 min): Pause for feedback after each major section
4. Objection surfacing (5-10 min): Proactively ask what concerns remain
5. Next-step commitment (3 min): Propose evaluation criteria or next meeting

### Negotiation / Close Call

1. Alignment check (5 min): Confirm mutual understanding of scope and value
2. Terms discussion (15-20 min): Walk through outstanding items
3. Concern resolution (10 min): Address blockers with prepared responses
4. Agreement framing (5 min): Summarize what was agreed
5. Process next steps (5 min): Define exact actions to paper and sign

### Check-In / Relationship Call

1. Personal rapport (3-5 min): Genuine connection, not scripted small talk
2. Value delivered (5-10 min): Review outcomes since last interaction
3. Feedback loop (5-10 min): What is working, what is not
4. Expansion signals (5 min): New use cases, departments, or pain points
5. Forward plan (3 min): Next touchpoint and any action items

## Output Template: Call Brief

```
# Call Brief: [Meeting Title]
**Date/Time**: [Meeting date and time]
**Duration**: [Scheduled length]
**Call Type**: [Discovery / Demo / Negotiation / Check-In / Other]

## Deal Context
- **Account**: [Company name]
- **Deal Stage**: [Current stage] | **Value**: [Amount or range]
- **Days in Stage**: [Count] | **Expected Close**: [Date or "TBD"]
- **Last Interaction**: [Date — summary of last meaningful contact]

## Attendees
| Name | Title | Role | Relationship | Key Priority |
| --- | --- | --- | --- | --- |
| [Name] | [Title] | [Buying role] | [History] | [What they care about] |

## Open Items from Prior Calls
- [ ] [Commitment or question still unresolved — owner and date]
- [ ] [Objection raised but not fully addressed]

## Call Objectives
- **Primary**: [Ideal outcome]
- **Secondary**: [Additional goals]
- **Minimum Viable**: [Floor outcome]

## Recommended Talking Points
1. [Topic] — [Why it matters] — [Suggested framing or question]
2. [Topic] — [Why it matters] — [Suggested framing or question]
3. [Topic] — [Why it matters] — [Suggested framing or question]

## Objections to Prepare For
| Likely Objection | Prepared Response | Evidence / Proof Point |
| --- | --- | --- |
| [Anticipated concern] | [Response framework] | [Reference to have ready] |

## Materials to Have Ready
- [ ] [Document, case study, or demo environment]
- [ ] [Pricing or proposal if applicable]

## Post-Call Checklist
- [ ] Send recap email within [timeframe]
- [ ] Update CRM with call notes and next steps
- [ ] Log any new contacts or stakeholder-map changes
```

## Guardrails

1. Never fabricate attendee information. All names, titles, and relationship history must come from CRM, calendar, email, or user input. Unknown attendees: "[Name from calendar — no CRM record, plan discovery]".
2. Never invent deal history. If no CRM record exists, state "No prior deal record found" rather than assuming first engagement.
3. Source labeling. Tag every assertion — [From CRM], [From calendar], [From email], [From user input], [AI recommendation].
4. Verification reminder. Include "Review brief against your own account knowledge before the call" on all outputs.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted, ready-to-share call brief.
