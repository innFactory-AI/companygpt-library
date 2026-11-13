---
name: en-call-summary
description: Extract action items, key topics, and objections from call notes or transcripts and draft a customer-facing follow-up email. Use after a sales call, demo, or discovery session. Trigger with "summarise this call", "call notes from", "write follow-up for this meeting".
---

# Call Summary Skill

Turn call notes or transcripts into actionable intelligence and draft customer-ready follow-up emails. The skill produces call summaries, action-item registers, objection logs, and follow-up drafts. You provide all call content, or it comes from a connected source.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **CRM via MCP** (e.g. HubSpot, Salesforce) | Account context, opportunity stage, known stakeholders, prior call notes |
| **Call-recording / transcription via MCP** (e.g. Gong) | Raw transcripts, participant lists, timestamps of key moments |
| **companyTRANSCRIBE** (if enabled) | Transcribes a call recording (audio or video) attached to the chat with speaker labels, or retrieves your existing transcripts |
| **companyM365** (if enabled) | Transcripts of Teams meetings |
| **companyRAG collections** | Discovery summaries, competitive profiles, product info for context-aware follow-ups |
| **File upload (transcripts)** | Transcript or notes files you drop directly into the chat |

> **No connected source?** Paste the transcript or notes in chat or upload the relevant files — the skill works the same way.

## Call-Processing Workflow

```
1. INGEST call content
   |
   +--> Accept raw transcript, structured notes, or bullet-point recap
   +--> Identify call type: Discovery / Demo / Negotiation / Check-In / Other
   +--> Identify participants (from transcript headers, notes, or user input)
   |
2. EXTRACT key topics
   |
   +--> Categorize discussion points (see Topic Categorization below)
   +--> Capture direct quotes that carry weight (decisions, commitments, objections)
   +--> Note topics raised but not resolved — these become open items
   |
3. IDENTIFY action items
   |
   +--> For each commitment or next step mentioned:
   |      Owner (our side / their side / joint)
   |      Action (specific and verifiable)
   |      Deadline (stated or inferred from context)
   |      Priority (blocks deal progression / important / nice-to-have)
   |
4. FLAG objections and concerns
   |
   +--> Capture the objection as stated (not paraphrased away)
   +--> Note whether it was addressed, partially addressed, or left open
   +--> Record the response given (if any) for consistency in future calls
   +--> Classify by type (see Objection Classification below)
   |
5. ASSESS deal impact
   |
   +--> Did the call advance, stall, or regress the deal?
   +--> What changed about our understanding of the opportunity?
   +--> Are there new stakeholders, risks, or timeline shifts?
   |
6. DRAFT follow-up (see Follow-Up Email Framework below)
   |
7. COMPILE output (see Output Templates below)
```

## Topic Categorization

Classify each discussion topic to make the summary scannable:

| Category | What It Covers | CRM Relevance |
| --- | --- | --- |
| **Requirements** | Stated needs, use cases, evaluation criteria | Update opportunity requirements |
| **Decision Process** | Timeline, stakeholders involved, approval steps | Update close date, decision map |
| **Budget / Commercial** | Pricing discussion, budget constraints, ROI expectations | Update deal value, stage |
| **Technical** | Integration needs, security, compliance, architecture | Log as technical requirements |
| **Competitive** | Mentions of alternatives, incumbent vendor, evaluation comparison | Update competitive field in CRM |
| **Relationship** | Rapport signals, internal politics, champion strength indicators | Update stakeholder notes |
| **Next Steps** | Agreed actions, follow-up meetings, deliverables promised | Create CRM tasks |

## Objection Classification

| Type | Definition | Follow-Up Priority |
| --- | --- | --- |
| **Deal-blocking** | Objection that will prevent close if unresolved | Immediate |
| **Stage-blocking** | Prevents advancement to next stage but not necessarily a deal-killer | High |
| **Concern** | Expressed worry that needs addressing but is not blocking progress | Medium |
| **Skepticism** | General doubt about value or approach — needs proof points | Medium |
| **Clarification** | Misunderstanding or information gap — easily resolved with data | Low |

For each objection, track: stated objection (verbatim or near-verbatim), classification, response given during the call, resolution status (resolved / partially addressed / open), and recommended follow-up action.

## Follow-Up Email Framework

The follow-up email should be sendable with minimal editing. Structure:

### Tone Calibration

| Relationship Stage | Tone | Formality |
| --- | --- | --- |
| **First interaction** | Professional, appreciative of time | Formal |
| **Active evaluation** | Collaborative, momentum-focused | Semi-formal |
| **Established rapport** | Direct, efficient, partnership tone | Conversational |
| **Executive audience** | Concise, outcome-focused | Formal |

### Email Structure

```
Subject: [Descriptive, action-oriented — never generic like "Meeting follow-up"]

[Opening: 1 sentence — thank + reference a specific moment from the call]

[Summary: 3-5 bullet points of what was discussed — phrased in terms
 of their priorities and language, not your product features]

[Action Items: clear table or list]
  - What we committed to doing → by when
  - What we're asking them to do → by when

[Next Step: specific — date, time, agenda for next interaction]

[Close: 1 sentence — express enthusiasm about the specific outcome
 discussed, not generic excitement]
```

### Follow-Up Quality Checklist

- References something specific from the conversation (proves you listened)
- Uses their language and terminology, not internal jargon
- Action items have owners and dates
- Next step is specific and time-bound
- No markdown formatting (plain text or minimal HTML for email clients)
- Subject line would make sense in their inbox without additional context
- Appropriate length: 150-250 words for standard follow-ups

## Output Template — Call Summary

```
# Call Summary: [Meeting Title / Company Name]
**Date**: [Call date]  |  **Duration**: [Actual length]
**Call Type**: [Discovery / Demo / Negotiation / Check-In]
**Participants**: [List with roles]

## Key Topics Discussed
| # | Topic   | Category   | Summary                |
|---|---------|------------|------------------------|
| 1 | [Topic] | [Category] | [2-3 sentence summary] |
| 2 | [Topic] | [Category] | [2-3 sentence summary] |

## Action Items
| #  | Action            | Owner | Deadline | Priority         |
|----|-------------------|-------|----------|------------------|
| 1  | [Specific action] | [Who] | [When]   | [Classification] |

## Objections & Concerns
| Objection   | Type             | Status           | Follow-Up Needed     |
|-------------|------------------|------------------|----------------------|
| [As stated] | [Classification] | [Open/Addressed] | [Recommended action] |

## Deal Impact Assessment
- **Deal Movement**: [Advanced / Stalled / Regressed / Neutral]
- **Stage Recommendation**: [Stay / Advance to X / Flag for review]
- **New Information**: [What we learned that changes our understanding]
- **Risk Changes**: [New risks surfaced or existing risks mitigated]

## Follow-Up Email Draft
[Ready-to-send email following the framework above]
```

## Processing Notes for Transcript Quality

| Input Quality | Handling |
| --- | --- |
| **Full transcript** | Extract verbatim quotes for key moments; comprehensive summary |
| **Structured notes** | Organize into framework; flag potential gaps in coverage |
| **Bullet-point recap** | Build summary from bullets; note that nuance may be missing |
| **Partial / fragmentary** | Summarize what is available; clearly mark sections as "[Incomplete — ask rep to fill gaps]" |

## Guardrails

1. Never fabricate call content. Every topic, quote, and action item must be traceable to the provided notes or transcript. Ambiguous content: "[Unclear from notes — verify with attendees]".
2. Never invent attendee reactions. Do not characterise sentiment or buy-in unless explicitly stated in the notes.
3. Objection accuracy. Capture objections as close to verbatim as the source allows. Do not soften, reframe, or minimise stated concerns.
4. Source labeling. Tag assertions — [From transcript], [From notes], [From user input], [AI interpretation]. AI interpretations must be flagged for verification.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted summary ready to share.
