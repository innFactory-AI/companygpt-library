---
name: en-interview-guide
description: Create structured interview guides with behavioural questions, scoring rubrics, and bias-mitigation notes. Use when hiring for a new role, redesigning your interview process, or calibrating interviewers. Trigger with "build interview guide for", "create a scorecard for", "design interviews for this role".
---

# Interview Guide Skill

Design multi-round interview processes with behavioural scoring rubrics, interviewer calibration, and a defensible debrief methodology. Organisation-specific data — role requirements, competency definitions, team context — comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **ATS via MCP** (e.g. Greenhouse, Lever) | Open requisitions, role specifications, existing scorecards, interview-stage configuration |
| **HRIS via MCP** (e.g. Workday, Personio, Bamboo HR) | Job architecture, competency definitions, target job levels, team structure |
| **companyRAG / file upload** | Job descriptions, competency frameworks, role specifications, hiring policies |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## EU AI Act & GDPR Compliance Boundaries

AI-assisted recruitment and candidate evaluation is classified as **high-risk under the EU AI Act (Annex III, Category 4 — employment and workers' management)**. Per GDPR Article 22, individuals have the right not to be subject to decisions based solely on automated processing that produce legal or similarly significant effects. All outputs are decision-support tools for human practitioners — candidate assessment, scoring, and hiring decisions must be made by qualified human interviewers.

## Interview Process Design

### Competency-to-Stage Mapping

The foundation of structured hiring is ensuring every required competency is assessed, every competency is assessed at least once, and no competency is assessed redundantly across stages unless intentional (for reliability).

Methodology for mapping:

1. List all competencies required for the role and job level (from job architecture or role specification)
2. Categorize each competency by optimal assessment method:
   - Behavioral interview: Past behavior as predictor — best for interpersonal, leadership, problem-solving, cultural adaptability
   - Technical assessment: Demonstrated capability — best for domain expertise, coding, analytical reasoning, writing
   - Case/simulation: Applied judgment — best for strategic thinking, prioritization, stakeholder management
   - Work sample: Actual deliverable — best for creative, operational, and execution-heavy roles
3. Group competencies into assessment stages by method type
4. Assign each stage to one or more interviewers based on their qualification to evaluate those competencies
5. Verify coverage: create a matrix of competencies × stages — every competency must appear at least once; flag any that appear three or more times (likely redundant)

### Panel Design Methodology

Determine who evaluates what, and ensure no single interviewer's judgment dominates.

- Panel size: 2–4 interviewers depending on role seniority and organizational size (hiring manager + 1–3 additional). Fewer creates single-point-of-failure risk; more creates diminishing returns and scheduling burden. Smaller organizations or junior roles may use 2; senior or cross-functional roles benefit from 3–4.
- Interviewer assignment principle: Assign interviewers to competencies they are qualified to evaluate. A backend engineer should not assess product strategy; a product manager should not assess code quality.
- Overlap strategy: Intentional overlap on 1–2 critical competencies provides reliability data. Unintentional overlap wastes candidate and interviewer time.
- Independence requirement: Interviewers must NOT share notes or impressions before the debrief. Sequential contamination destroys the value of multiple independent assessments.

### Stage Sequencing

Order interview stages to optimize for both candidate experience and information value:

1. Screen (recruiter or hiring manager): Role fit, logistics, mutual interest — eliminates misalignment early
2. Technical/skill assessment: Domain capability — the highest-signal, most objective stage
3. Behavioral interviews: Past behavior evidence — requires more interviewer skill, benefits from role context established in prior stages
4. Case/simulation (if applicable): Applied judgment — cognitively demanding for the candidate, best not first
5. Values/culture-add (if applicable): Organizational alignment — sensitive to bias; apply culture-add scorecard patterns and the bias mitigation and debrief practices described in this skill
6. Final round (senior leadership): Strategic fit and sponsorship — only after earlier stages confirm capability

## Scorecard Design Framework

### Behavioral Anchor Construction

A scorecard is only as good as its anchors. Behavioral anchors define what "good" looks like at each score level for each competency, making scoring consistent across interviewers.

5-level anchor framework:

| Level | Label | Anchor Definition Pattern |
| --- | --- | --- |
| 1 | Does Not Meet | No evidence of the competency; responses lack relevant examples entirely |
| 2 | Partially Meets | Some evidence but significant gaps; examples lack specificity, ownership, or outcome |
| 3 | Meets Expectations | Clear evidence with specific examples demonstrating the competency at the target job level |
| 4 | Exceeds Expectations | Strong evidence with multiple examples showing the competency beyond the target job level |
| 5 | Exceptional | Compelling evidence of the competency at a level that would influence team or organizational practice |

For each competency on the scorecard, write level-specific anchors that describe observable candidate behaviors for that competency. Generic anchors ("good answer" / "bad answer") defeat the purpose.

Pattern for writing competency-specific anchors:

```
Competency: [Name] — Target job level: [from job architecture]
Level 1: [What would a response with NO evidence of this competency look like?]
Level 3: [What specific behaviors/examples would demonstrate this at the target level?]
Level 5: [What would exceed the target level in a way that is clearly distinguishable from Level 3?]
```

Write levels 1, 3, and 5 first. Then interpolate levels 2 and 4 as intermediate points. This prevents the common error of making all levels feel similar.

For behavioral, technical, case, and values/culture-add interviews, adapt the anchor framework above to the assessment method (see competency-to-stage mapping) and keep scorecard sections consistent across interview types.

### Scorecard Sections

Every scorecard should include:

1. Competency being assessed: Linked to the role's competency requirements
2. Target job level: From job architecture — sets the "Meets Expectations" bar
3. Behavioral anchors: Level-specific descriptions as above
4. Suggested probing areas: Not scripted questions, but areas to explore that elicit evidence for this competency
5. Evidence capture field: Space for the interviewer to record specific candidate statements and behaviors (not impressions)
6. Score: Single numerical score per competency, informed by anchors
7. Overall recommendation: Separate from individual competency scores — the interviewer's holistic hire/no-hire signal with written rationale

## STAR+ Evaluation Methodology

You already know what STAR is. This section adds the evaluation layer: how to ASSESS the quality of candidate responses using STAR+, not how to generate STAR questions.

### STAR+ Quality Indicators

When a candidate provides a behavioral response, evaluate along these dimensions beyond basic STAR structure:

| Indicator | What to Assess | Red Flag |
| --- | --- | --- |
| **Specificity** | Is the example a specific, datable event or a generalized "I usually..." pattern? | "In situations like that, I typically..." (no specific example) |
| **Ownership** | Does the candidate describe their personal actions and decisions, or team/organizational outcomes? | "We decided..." with no clarity on the candidate's role |
| **Measurable Impact** | Are outcomes quantified or qualified with concrete evidence? | "It went really well" with no specifics |
| **Proportional Credit** | Is the claimed impact proportional to the role described? | Junior role claiming organizational transformation |
| **Reflection** | Does the candidate demonstrate learning or adaptation from the experience? | Presenting every example as an unqualified success |
| **Relevance** | Does the example match the competency and job level being assessed? | Strong example, wrong competency |

### Evaluating Technical Responses

Technical assessments require different quality indicators:

- Approach before solution: Does the candidate clarify requirements and constraints before jumping to a solution?
- Trade-off articulation: Can the candidate explain why they chose one approach over alternatives?
- Edge case awareness: Does the candidate identify boundary conditions unprompted?
- Communication of reasoning: Can the candidate explain their thought process to a non-specialist?
- Calibration to job level: A senior candidate who solves but cannot teach or architect is demonstrating IC2 behavior, not IC4

## Interview Debrief Methodology

The debrief is where individual assessments become a collective hiring decision. Without structure, debriefs default to whoever speaks first or most confidently.

### Structured Debrief Process

1. Pre-debrief: All interviewers submit their scorecards BEFORE the debrief meeting. No exceptions — post-submission prevents anchoring to others' assessments.
2. Score reveal: Display all scores simultaneously (spreadsheet, whiteboard, tool). Do NOT go around the table sequentially — the first speaker anchors everyone else.
3. Divergence identification: Identify competencies where scores differ by 2+ levels. These are the discussion items.
4. Evidence review: For each divergent competency, each interviewer shares the specific candidate evidence (quotes, behaviors) that informed their score. Discussion focuses on evidence, not impressions.
5. Calibration: After evidence sharing, interviewers may adjust scores. Adjustments must be evidence-driven — "I hadn't considered that example" is valid; "I'll defer to the hiring manager" is not.
6. Aggregate assessment: Combine scores using the pre-agreed weighting (from the scorecard design). The weighted score is an input to the decision, not THE decision.
7. Hiring decision: The hiring manager makes the final call, explicitly stating whether they are following or overriding the aggregate score and why.
8. Documentation: Record the decision rationale, including any override reasoning. This documentation supports defensible hiring decisions.

### Disagreement Resolution

When interviewers genuinely disagree after evidence sharing:

- Check for different evidence bases (different stages may have revealed different behavior)
- Check for standard differences (one interviewer's "Meets" may be another's "Exceeds" — a calibration problem to fix for future hires, not this decision)
- Check for bias patterns (leniency, strictness, halo, affinity, groupthink, contrast effects) using the structured debrief process above
- If disagreement persists after evidence review, document both positions and let the hiring manager decide with full transparency

## Candidate Evaluation Matrix

For final decision-making across multiple candidates:

### Weighted Multi-Dimensional Comparison

Weight scorecard competencies by role priority and populate with each candidate's debrief scores. The matrix is ONE input to the decision, not THE decision. [AI-generated suggestion — verify] Any ranking based on matrix scores must be validated by the hiring team, who have context the matrix cannot capture (team dynamics, growth trajectory, offer competitiveness).

## AI-Assisted Hiring Compliance Awareness

When AI tools are used in any part of the hiring process (CV screening, assessment scoring, chatbot interactions, video interview analysis), this may trigger high-risk classification under the AI Act (Annex III, Category 4 — employment and workers' management).

Scoping methodology — assess whether the AI use case involves:

- Recruitment or selection decisions
- Screening or filtering of applications
- Evaluation of candidates
- Monitoring or evaluation during employment relationships

If any of these apply, confirm deployer obligations and verify specific requirements with employment counsel in the applicable jurisdiction, as national implementations may vary.

Anti-discrimination requirements in hiring assessment vary significantly by jurisdiction. Key examples: Allgemeines Gleichbehandlungsgesetz (AGG) in Germany, Code du travail provisions in France, Wet gelijke behandeling in the Netherlands. Verify assessment approach compliance with employment counsel in the applicable jurisdiction before implementing.

## Supporting Material

If you have detailed bias-mitigation strategies or scorecard templates in companyRAG collections or as uploaded files, draw on them when designing bias-mitigation approaches or building scorecards. Otherwise, build these from the frameworks in this skill.

## Guardrails

- Never generate candidate assessments, scores, rankings, or hire/no-hire recommendations. All candidate evaluation must be performed by human interviewers using the frameworks provided.
- Never infer candidate qualifications not explicitly stated in provided materials. Never generate "standard" interview questions from training data — derive all assessment content from the role's specific competency requirements.
- Flag when assessment approaches touch protected characteristics: "Validate with employment counsel in [jurisdiction] to confirm compliance with anti-discrimination requirements."
- Source-label all output: `[Framework template]`, `[From role requirements]`, or `[AI-generated suggestion — verify]`.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted interview guide and scorecards ready to share with the panel.
