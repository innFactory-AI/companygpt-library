---
name: en-employee-onboarding
description: Generate personalised onboarding checklists and 30/60/90-day plans for new hires, tailored to role and location. Use when onboarding a new team member, redesigning the onboarding experience, or scaling onboarding across teams. Trigger with "onboarding plan for", "new hire checklist", "30/60/90 for [role]".
---

# Employee Onboarding Skill

> **Note:** This skill assists with HR workflows but does not constitute employment law advice. Verify all output with qualified HR professionals and employment counsel in the applicable jurisdiction.

Design personalised onboarding programmes — pre-boarding, first-day logistics, 30/60/90-day milestones, buddy assignment, and effectiveness measurement. Organisation-specific details come from you, connected HR systems, companyRAG collections, or uploaded files.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **HRIS via MCP** (e.g. Workday, BambooHR, Personio) | New hire details, role and level, department, manager, start date, employment type |
| **Task tracker via MCP** (e.g. Asana, Monday, Jira, Notion) | Onboarding tasks, owner assignments, status of checklist items |
| **companyRAG collections / file upload** | Role descriptions, team playbooks, compliance requirements, existing onboarding templates |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Onboarding Design Workflow

### Step 1: Gather Role Context

Before generating any onboarding content, collect these inputs:

```
ONBOARDING CONTEXT
==================
New hire name:      [name]
Role:               [title and level]
Department / team:  [organizational unit]
Manager:            [name]
Start date:         [date]
Location:           [office / hybrid / remote — city, country]
Employment type:    [permanent / fixed-term / contractor]
Internal transfer:  [yes / no — internal moves require modified onboarding]
Previous context:   [relevant background — industry, similar roles, internal experience]
Team size:          [how many people on the immediate team]
Key stakeholders:   [cross-functional contacts the new hire will work with regularly]
```

### Step 2: Pre-Boarding Checklist (Before Day 1)

Pre-boarding covers everything that should happen between offer acceptance and the first day. This period significantly impacts first-day experience and early engagement.

#### Administrative Pre-Boarding

| Item | Owner | Timing | Status |
| --- | --- | --- | --- |
| **Employment contract signed** | HR | Before start date | ☐ |
| **IT equipment ordered and configured** | IT / HR | 5+ business days before start | ☐ |
| **System accounts created** | IT | 2-3 business days before start | ☐ |
| **Email and calendar set up** | IT | 1-2 business days before start | ☐ |
| **Building access / security badge** | Facilities | Before start date | ☐ |
| **Payroll and benefits enrolment initiated** | HR / Payroll | Before start date | ☐ |
| **Workspace prepared** | Team / Facilities | Before start date | ☐ |
| **Welcome pack sent** | HR / Team | 3-5 days before start | ☐ |

#### Manager Pre-Boarding

| Item | Owner | Timing | Status |
| --- | --- | --- | --- |
| **Onboarding buddy assigned** | Manager | 1+ week before start | ☐ |
| **First-week calendar populated** | Manager + buddy | 2-3 days before start | ☐ |
| **Team informed of new hire** | Manager | 1 week before start | ☐ |
| **30/60/90-day plan drafted** | Manager | Before start date | ☐ |
| **Key stakeholder introductions scheduled** | Manager | Before or during first week | ☐ |

#### Location-Specific Pre-Boarding

Adapt pre-boarding based on the new hire's location:

| Location Type | Additional Items |
| --- | --- |
| **Office-based** | Desk assignment, parking/transit info, office tour scheduled, lunch plans for day 1 |
| **Hybrid** | Office schedule communicated, home office equipment shipped, video conferencing tested |
| **Remote** | All equipment shipped and received, virtual onboarding schedule confirmed, time zone considerations addressed |
| **International** | Work permit verified, local entity employment confirmed, country-specific mandatory training identified, local public holidays shared |

### Step 3: First Week Structure

The first week sets the tone for the entire onboarding experience. Structure it to balance information delivery with relationship building.

#### Day 1 Agenda

| Time Block | Activity | Owner | Purpose |
| --- | --- | --- | --- |
| **First 30 min** | Manager welcome — 1:1 check-in | Manager | Personal welcome, set expectations for the day |
| **Morning** | HR orientation — policies, benefits, compliance training | HR | Administrative foundations |
| **Late morning** | IT setup — verify all systems, access, tools working | IT / Buddy | Remove technical blockers |
| **Lunch** | Team lunch or virtual coffee | Team / Buddy | Social connection |
| **Afternoon** | Team introduction — meet immediate team members | Manager / Team | Context and relationships |
| **End of day** | Buddy check-in — questions, first impressions | Buddy | Support and comfort |

#### Days 2-5 Framework

| Focus Area | Activities | Outcome |
| --- | --- | --- |
| **Product / service understanding** | Product demos, documentation review, customer journey walkthrough | New hire can articulate what the organization does and for whom |
| **Team context** | Team goals, current projects, ways of working, communication norms | New hire understands the team's priorities and how work flows |
| **Stakeholder introductions** | Scheduled 1:1s with key cross-functional partners | New hire has faces to names and understands collaboration touchpoints |
| **Role-specific onboarding** | Domain training, tool-specific tutorials, shadow sessions | New hire begins to understand the daily work of the role |
| **Culture and values** | Values session, culture-specific onboarding, ERG introductions (if applicable) | New hire understands organizational norms and community |

### Step 4: 30/60/90-Day Plan

The 30/60/90 plan structures the new hire's ramp-up into three phases. Each phase has learning objectives, key activities, expected outcomes, and success criteria.

#### Phase 1: Learn (Days 1-30)

```
PHASE 1: LEARN — Days 1-30
============================
Objective: Build foundational knowledge of the role, team, and organization.

LEARNING GOALS:
  1. [Role-specific knowledge goal — e.g., "Understand the product architecture and key components"]
  2. [Process knowledge goal — e.g., "Complete all mandatory compliance training"]
  3. [Relationship goal — e.g., "Meet all key stakeholders and understand their priorities"]

KEY ACTIVITIES:
  - [Activity 1 with owner and timeline]
  - [Activity 2]
  - [Activity 3]

EXPECTED OUTCOMES:
  - Can articulate the team's goals and current priorities
  - Has completed all mandatory training and compliance requirements
  - Has met all key stakeholders and understands collaboration touchpoints
  - Can navigate core tools and systems independently

SUCCESS CRITERIA (assessed at Day 30 check-in):
  - [Specific, observable criterion 1]
  - [Specific, observable criterion 2]

SUPPORT:
  - Weekly 1:1 with manager (30 min)
  - Daily check-in with buddy (15 min, tapering to as-needed)
  - Access to onboarding documentation and knowledge base
```

#### Phase 2: Contribute (Days 31-60)

```
PHASE 2: CONTRIBUTE — Days 31-60
==================================
Objective: Begin making meaningful contributions while deepening domain expertise.

CONTRIBUTION GOALS:
  1. [First independent deliverable — e.g., "Own and deliver a small-scope project end-to-end"]
  2. [Process improvement — e.g., "Identify one process improvement opportunity from fresh-eyes perspective"]
  3. [Collaboration goal — e.g., "Lead or co-lead a cross-functional initiative"]

KEY ACTIVITIES:
  - [Activity 1 with increasing autonomy]
  - [Activity 2]

EXPECTED OUTCOMES:
  - Has delivered at least one meaningful piece of work independently
  - Is contributing to team discussions and planning with informed perspectives
  - Has identified areas where they need further development

SUCCESS CRITERIA (assessed at Day 60 check-in):
  - [Specific deliverable or outcome 1]
  - [Specific deliverable or outcome 2]

SUPPORT:
  - Weekly 1:1 with manager (30 min)
  - Buddy check-ins as needed (transition from scheduled to on-demand)
  - Feedback from stakeholders solicited by manager
```

#### Phase 3: Own (Days 61-90)

```
PHASE 3: OWN — Days 61-90
===========================
Objective: Operate at full productivity for the role level, owning responsibilities independently.

OWNERSHIP GOALS:
  1. [Full ownership area — e.g., "Own [specific responsibility] end-to-end with manager oversight only for escalations"]
  2. [Strategic contribution — e.g., "Propose a plan or initiative that builds on first 60 days of learning"]
  3. [Team integration — e.g., "Actively contribute to team rituals, code reviews, planning sessions"]

KEY ACTIVITIES:
  - [Activity 1 at full role scope]
  - [Activity 2]

EXPECTED OUTCOMES:
  - Operating independently at the expected level for the role
  - Has a clear development plan for the next 6-12 months (see design-learning-plan skill)
  - Team and stakeholders view the new hire as a contributing team member

SUCCESS CRITERIA (assessed at Day 90 review):
  - [Specific outcome 1]
  - [Specific outcome 2]
  - Manager and new hire align on: what's going well, what needs development, goals for the next quarter

SUPPORT:
  - Weekly or biweekly 1:1 with manager
  - Buddy relationship transitions to peer relationship
  - Formal feedback collection from key stakeholders
```

### Step 5: Buddy Assignment

The onboarding buddy is distinct from the manager and serves a different function.

#### Buddy Selection Criteria

| Criterion | Why It Matters |
| --- | --- |
| **Peer or near-peer level** | The new hire should feel comfortable asking "dumb questions" — a senior leader buddy creates a power dynamic that inhibits this |
| **Same or adjacent team** | Proximity to the new hire's daily work makes the buddy's guidance immediately relevant |
| **Tenure of 6+ months** | The buddy must know enough to be helpful; too new and they are still learning themselves |
| **Voluntary participation** | Buddy assignment should not be compulsory — unwilling buddies provide poor support |
| **Communication style** | Consider whether the buddy's style will complement the new hire (especially for remote onboarding where written communication carries more weight) |

#### Buddy Responsibilities

| Responsibility | Frequency | Duration |
| --- | --- | --- |
| Daily check-in (informal) | Daily for weeks 1-2, then as needed | 10-15 minutes |
| Answer questions and provide context | Ongoing | As needed |
| Introduce to team norms and unwritten rules | Weeks 1-4 | Organic |
| Social integration support | Ongoing | Introductions to people outside the immediate team |
| Escalate concerns to manager or HR | As needed | If the buddy notices the new hire struggling or disengaging |

## Customisation Guide

Adapt the standard framework based on these role and context dimensions:

| Dimension | Customisation |
| --- | --- |
| **Senior / leadership hire** | Compress learning phase; add stakeholder listening tour; include board/exec exposure; assign a senior peer buddy rather than a junior one |
| **Technical role** | Add codebase orientation, architecture walkthroughs, dev environment setup, first PR/commit as a milestone |
| **Customer-facing role** | Add product certification, customer shadowing, CRM training, first customer interaction as a milestone |
| **Remote hire** | Intensify virtual social touchpoints; ensure all materials are accessible asynchronously; schedule overlapping hours with the team |
| **Internal transfer** | Skip organizational onboarding; focus on team-specific and role-specific elements; leverage existing relationships |
| **International hire** | Add relocation support, local compliance training, cultural orientation, local holiday calendar, language support if applicable |

## Onboarding Effectiveness Measurement

### Measurement Framework

| Metric | When to Measure | Method | Target |
| --- | --- | --- | --- |
| **New hire satisfaction** | Day 7, Day 30, Day 90 | Pulse survey (5-7 questions) | Define threshold based on organizational data |
| **Time to productivity** | Day 30, Day 60, Day 90 | Manager assessment against 30/60/90 plan milestones | Varies by role — establish baselines |
| **30/60/90 milestone completion** | At each milestone | Checklist completion rate | 80%+ of milestones met on time |
| **Buddy satisfaction** | Day 30 | Buddy feedback form | Qualitative — are buddies finding the programme worthwhile? |
| **Early attrition** | 6-month and 12-month marks | Turnover data | Below organizational average for the role level |

### Continuous Improvement

After each onboarding cycle, capture:

- What worked well (keep)
- What was missing (add)
- What was unnecessary (remove)
- What needs adjustment (modify)

Feed improvements back into the onboarding templates for the next hire.

## Guardrails

- Never generate organisation-specific policies, system names, or procedures. Prompt the user to provide their list rather than inventing items.
- Never assume location-specific requirements. Mandatory training, works council notifications, and probation rules vary by jurisdiction — flag as "verify for [jurisdiction]".
- Never generate specific timelines for administrative tasks. These vary by organisation — use the structure and let the user fill in actual timelines.
- Source-label all output: `[From role context]`, `[From onboarding methodology]`, or `[AI suggestion — verify with HR]`.

> **Tip:** Ask for DOCX output via companyFILES to get a formatted Word document ready for distribution. XLSX or Markdown are also available.
