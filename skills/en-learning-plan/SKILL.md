---
name: en-learning-plan
description: Design role-specific learning and development plans from career frameworks, skill gaps, and business priorities. Use when creating individual development plans, designing team training programmes, or mapping career progression. Trigger with "create learning plan for", "development plan for [role]", "skill gap analysis".
---

# Learning Plan Skill

Assess skill gaps, map development activities to a career framework, and design individual or team learning plans with measurable milestones. Role requirements, competency definitions, and employee data come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **LMS via MCP** (e.g. Moodle, Cornerstone, SAP SuccessFactors) | Learning catalogue, completed courses, certifications, available learning paths |
| **companyLEARN** (if enabled) | Internal course catalogue and course overviews, plus your own learning progress |
| **HRIS via MCP** (e.g. Workday, Personio, BambooHR) | Roles and levels, team roster, performance data, career framework |
| **companyRAG / file upload** | Competency frameworks, job architecture, self- and manager assessments, 360 feedback |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Regulatory Awareness

Employee development activities may involve processing personal data (skill assessments, performance-linked development plans, learning records). Reference the handle-gdpr skill for data processing requirements when development plans are stored in systems or shared beyond the direct manager-employee relationship.

Works council or employee representative consultation may be required when establishing or modifying systematic training programmes in some jurisdictions. Verify with employment counsel in the applicable jurisdiction.

## Learning Plan Workflow

Follow these steps in order. The workflow scales from a single individual development plan to a team-wide training programme.

### Step 1: Assess Current Skills

Establish a baseline of current capabilities before identifying gaps.

**For an individual:**

| Input | Source | Purpose |
| --- | --- | --- |
| Current role and job level | Job architecture / user input | Sets the baseline expectation |
| Target role or next level | Career framework / user input | Sets the aspiration |
| Self-assessment | Employee input | Employee's own view of strengths and gaps |
| Manager assessment | Manager input | Manager's view of demonstrated capabilities |
| Performance data | Review outcomes / user input | Evidence of demonstrated strengths and development areas |
| Feedback (peers, stakeholders) | 360 data / user input | Broader perspective on capabilities |

**For a team:**

| Input | Source | Purpose |
| --- | --- | --- |
| Team roster with roles and levels | HRIS / user input | Scope of the assessment |
| Team capability requirements | Business strategy / user input | What the team needs to deliver |
| Individual assessments (aggregated) | Per-individual process above | Aggregate skill landscape |
| Business priorities for the period | Leadership / user input | Directional filter for development investment |

Produce a skill inventory using the competency framework relevant to the role or team. If no formal framework exists, co-create a role-relevant skill list with the user and label it: [Co-created — validate against your career framework].

### Step 2: Identify Gaps

Compare current capabilities against requirements for the current role (performance gaps) and the target role (development gaps).

```
SKILL GAP ANALYSIS:
  Employee / Team: [name or team]
  Current role:    [title and level]
  Target role:     [title and level, if different]

  SKILL: [name]
    Current level:  [from assessment — e.g., Developing / Competent / Advanced / Expert]
    Required level: [from framework — for current role]
    Target level:   [from framework — for target role]
    Gap:            [none / minor / significant / critical]
    Priority:       [high / medium / low — based on business impact and career aspiration]

  SKILL: [next skill]
    ...
```

**Gap prioritisation criteria:**

| Factor | High Priority | Medium Priority | Low Priority |
| --- | --- | --- | --- |
| Business impact | Skill gap blocks current deliverables or team goals | Skill would improve quality or efficiency | Nice-to-have for future capability |
| Career progression | Required for next-level promotion readiness | Expected within 12 months | Aspirational or exploratory |
| Urgency | Needed in next quarter | Needed within 6 months | 6–12 month development horizon |
| Availability of learning | Learning opportunities are available now | Opportunities exist but require planning | Requires creating new learning pathways |

### Step 3: Map to Development Activities

For each prioritised gap, identify appropriate development activities. Use the 70-20-10 framework as a DESIGN LENS, not a rigid allocation rule — the actual mix depends on the skill type and the learner's context.

| Learning Type | Examples | Best For |
| --- | --- | --- |
| **On-the-job (experiential)** | Stretch assignments, project rotations, shadowing, deputising, leading a workstream | Building practical capability, applying new knowledge, developing judgment |
| **Social (relationship-based)** | Mentoring, coaching, peer learning groups, cross-functional collaboration, community of practice | Tacit knowledge transfer, perspective broadening, network building |
| **Formal (structured)** | Courses, certifications, workshops, conferences, structured reading programmes | Foundational knowledge, technical skills, compliance requirements |

**Activity selection process:**

1. For each skill gap, identify at least one activity from each learning type that could address it
2. Assess feasibility: time commitment, cost, availability, manager support, business disruption
3. Select the activity mix that balances learning effectiveness with practical constraints
4. Ensure at least one experiential activity per gap — formal learning alone rarely closes capability gaps

### Step 4: Design the Plan

Assemble the gap analysis and activity mapping into a structured development plan.

```
# Individual Development Plan — [Name]
Date created: [date]
Review date:  [next review date — recommend quarterly]
Manager:      [name]

## Development Summary
  Current role:  [title and level]
  Target role:   [title and level, if different]
  Plan horizon:  [6 months / 12 months]
  Focus areas:   [2-4 priority skills from gap analysis]

## Development Goals

### Goal 1: [Skill / Competency Name]
  Current state: [assessment]
  Target state:  [expected level by review date]
  Priority:      [high / medium]
  Business link: [how this connects to current deliverables or team goals]

  Activities:
  - [Activity 1 — type: experiential / social / formal]
    Timeline: [start — end]
    Success indicator: [observable evidence that learning is happening]
    Support needed: [from manager, team, budget]

  - [Activity 2]
    ...

  Milestone: [Specific, observable checkpoint — what will be demonstrably different?]
  Milestone date: [date]

### Goal 2: [next skill]
  ...

## Support and Resources
  Manager commitments: [time for 1:1s, access to projects, feedback cadence]
  Budget: [if applicable — courses, conferences, certifications]
  Time allocation: [dedicated learning time, protected calendar blocks]

## Review Schedule
  - [Date]: Quarterly check-in — assess progress against milestones
  - [Date]: Mid-plan review — adjust activities if gaps are closing faster or slower than expected
  - [Date]: Plan completion review — assess outcomes, set next development cycle
```

### Step 5: Set Milestones and Success Indicators

Every development goal needs observable milestones — not just "complete the course" but evidence of capability change.

**Milestone quality criteria:**

| Criterion | Good Milestone | Weak Milestone |
| --- | --- | --- |
| Observable | "Lead a client presentation independently" | "Improve presentation skills" |
| Time-bound | "By end of Q2" | "Eventually" |
| Evidence-based | "Deliver the Q3 architecture proposal to the team" | "Understand architecture better" |
| Proportional | Achievable within the plan horizon with the planned activities | Requires a career's worth of development |

**Progress indicators by development phase:**

| Phase | Duration | Indicator |
| --- | --- | --- |
| Awareness | Weeks 1–4 | Can articulate the skill and why it matters for the role |
| Application | Months 1–3 | Applies the skill with support or guidance |
| Competence | Months 3–6 | Applies the skill independently in standard situations |
| Proficiency | Months 6–12 | Applies the skill in complex or novel situations; can coach others |

## Team Training Programme Design

When designing learning plans for a team rather than an individual:

1. Aggregate the skill gap analysis across team members — identify common gaps vs. individual gaps
2. Common gaps → group learning activities (workshops, team learning sessions, shared projects)
3. Individual gaps → personalised development activities within the team programme
4. Sequence activities so foundational skills are addressed before advanced ones
5. Balance development with delivery — the team still has work to do; plan development in realistic increments

## Guardrails

- Never generate specific course names, training providers, or platform recommendations from training data. All learning resources must come from the user's L&D catalogue.
- Never assess an individual's skill level without explicit input from the employee, manager, or performance data. Do not infer capabilities from job titles or tenure.
- Never claim specific timelines for skill development. Development pace depends on the individual, the skill, and the context.
- Source-label all output: `[Framework methodology]`, `[From career framework]`, `[Co-created — validate]`, or `[AI suggestion — verify with L&D team]`.

> **Tip:** Ask for DOCX, XLSX, or Markdown output via companyFILES to get a formatted plan ready to share.
