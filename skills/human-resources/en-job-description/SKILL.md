---
name: en-job-description
description: Write clear, inclusive job descriptions with levelling guidance and EU Pay Transparency Directive compliance. Use when creating a new role, refreshing an existing JD, or auditing JDs for bias and compliance. Trigger with "write JD for", "create job description", "update this job posting".
---

# Job Description Skill

Write, review, and audit job descriptions — role scoping, requirements calibration, inclusive language, job levelling, and EU Pay Transparency Directive compliance. Organisation-specific details come from your HR systems, companyRAG collections, or uploaded files.

> **Note:** This skill assists with HR workflows but does not constitute employment law advice. Verify all output with qualified HR professionals and employment counsel in the applicable jurisdiction.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **ATS via MCP** (e.g. Greenhouse, Lever) | Existing postings, role templates, pipeline status, hiring-manager notes |
| **HRIS via MCP** | Job architecture, levelling framework, compensation bands, org structure |
| **companyRAG collections / file upload** | Job-architecture documents, values statements, existing job descriptions, hiring-manager briefs |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## EU AI Act Compliance Boundary

AI-assisted recruitment, including AI-generated job descriptions used in recruitment pipelines, may interact with EU AI Act (Annex III, Category 4) obligations depending on how the descriptions are used in automated screening or matching systems. This skill generates job description TEXT for human review and publication — it does not screen, match, or evaluate candidates. All output must be reviewed and approved by a human before publication.

## Job Description Workflow

### Step 1: Role Scoping

Before writing, gather and confirm these inputs:

```
ROLE SCOPING
=============
Role title:         [working title — will be refined]
Department / team:  [organizational unit]
Reporting to:       [title of direct manager]
Location:           [office / hybrid / remote — specify jurisdictions for remote roles]
Employment type:    [permanent / fixed-term / contractor / intern]
Job level:          [from organizational job architecture, if available]
Headcount context:  [new role / backfill / expansion]
Business need:      [why this role exists — the problem it solves or the outcome it enables]
Collaboration:      [key internal and external stakeholders this role works with]
```

If the organization has a job architecture or levelling framework, anchor the role within it before writing. If no framework exists, reference the design-learning-plan skill for career framework design or establish level expectations with the hiring manager.

### Step 2: Requirements Calibration

The single most impactful quality decision in a job description is the distinction between requirements and preferences. Inflated requirements systematically reduce applicant diversity and exclude qualified candidates.

#### Requirements vs. Preferences Framework

| Category | Definition | Test |
| --- | --- | --- |
| **Must-Have (Requirements)** | Capabilities without which the person cannot perform the role on day one, even with onboarding support | Would you reject an otherwise exceptional candidate who lacked this? If no, it is not a requirement. |
| **Nice-to-Have (Preferences)** | Capabilities that accelerate ramp-up or add value but can be developed on the job | Could a strong candidate learn this within 6-12 months in the role? If yes, it is a preference. |
| **Bonus (Differentiators)** | Capabilities that would be exceptional to find but are not expected | Would you actively recruit for this, or only value it if it happened to be present? |

#### Calibration Process

1. List everything the hiring manager initially identifies as "required"
2. Apply the Must-Have test to each item
3. Move items that fail the test to Nice-to-Have or Bonus
4. Limit Must-Haves to 5-7 items — research consistently shows that longer requirements lists disproportionately discourage underrepresented applicants
5. Frame Must-Haves as outcomes or capabilities, not credentials — "experience designing distributed systems" rather than "5+ years of backend engineering"

#### Years-of-Experience Anti-Pattern

Avoid specifying years of experience as a requirement. Years of experience is a proxy, not a competency. Problems with years-based requirements:

- They disadvantage career changers, self-taught professionals, and those who progressed faster than average
- They create legal risk in jurisdictions where age discrimination protections apply (which includes the EU under Directive 2000/78/EC)
- They do not correlate well with capability beyond the first few years in a domain

Instead: describe the CAPABILITY LEVEL expected. "Able to independently design and implement microservice architectures" is more informative and inclusive than "7+ years of backend development."

If the hiring manager insists on years of experience, frame as a guideline: "Typically requires X+ years of relevant experience" rather than a hard requirement.

### Step 3: Inclusive Language Review

Apply these checks to the full job description text before publication.

#### Language Audit Checklist

| Check | What to Look For | Action |
| --- | --- | --- |
| **Gendered language** | "He/she", gendered nouns ("chairman", "manpower"), pronouns defaulting to one gender | Use gender-neutral alternatives ("they", "chairperson", "workforce") |
| **Aggressive/competitive framing** | "Crush goals", "dominate the market", "rockstar", "ninja", "killer instinct" | Replace with achievement-oriented language ("deliver results", "drive growth", "high-performing") |
| **Unnecessary superlatives** | "World-class", "best-in-class", "top-tier" without definition | Remove or replace with specific expectations |
| **Exclusionary jargon** | Internal acronyms, niche terminology not explained, culture-specific references | Define terms or use plain language |
| **Ability assumptions** | "Must be able to lift 50kg" when not actually required, "clean driving license" when not needed for the role | Remove unless genuinely required for the job function and documented as an essential function |
| **Credential inflation** | Requiring a degree when the role can be performed without one, requiring specific institutions or certifications | Require credentials only when legally necessary (e.g., licensed professions) or genuinely essential; otherwise accept equivalent experience |

#### Inclusive Framing Patterns

| Instead of | Use |
| --- | --- |
| "Must have X years in Y" | "Demonstrated ability to [outcome] in [domain]" |
| "Self-starter who thrives in chaos" | "Comfortable working autonomously and adapting to evolving priorities" |
| "Culture fit" | "Aligned with [specific named values]" |
| "Native English speaker" | "Professional proficiency in English" (or the actual language level required for the role) |
| "Young, dynamic team" | "Collaborative team" (age references create discrimination risk) |
| "Competitive salary" | Specific pay range (see Pay Transparency section) |

### Step 4: Job Description Structure

#### Standard JD Template

```
[ROLE TITLE]
[Department] · [Location] · [Employment type]

ABOUT THE ROLE
[2-3 sentences: what this role does, why it matters, and the impact the person will have.
Lead with outcomes, not activities. Answer: "Why would a talented person want this job?"]

WHAT YOU'LL DO
[5-8 key responsibilities. Start each with an action verb.
Order by importance to the role, not by frequency.
Frame as outcomes where possible: "Drive X" rather than "Attend meetings about X."]

- [Responsibility 1 — highest impact activity]
- [Responsibility 2]
- [Responsibility 3]
- [Responsibility 4]
- [Responsibility 5]

WHAT WE'RE LOOKING FOR
[Must-Haves — 5-7 items maximum. Frame as capabilities, not credentials.]

- [Requirement 1 — capability-based]
- [Requirement 2]
- [Requirement 3]

NICE TO HAVE
[Preferences — clearly separated from requirements]

- [Preference 1]
- [Preference 2]

WHAT WE OFFER
[Compensation range, benefits, development opportunities, working model.
Be specific — vague promises ("competitive package") signal a lack of transparency.]

- Salary range: [range in local currency, per Pay Transparency requirements]
- [Benefit 1]
- [Benefit 2]
- [Working model: office/hybrid/remote details]

EQUAL OPPORTUNITY
[Organization's equal opportunity statement.
Should be specific and genuine, not boilerplate.]

HOW TO APPLY
[Application process, what to submit, timeline expectations]
```

### Step 5: Job Levelling Integration

If the organization has a job architecture or levelling framework, align the JD:

| JD Element | Levelling Alignment |
| --- | --- |
| **Role title** | Maps to a specific level in the job architecture (e.g., IC3, M2, Senior Engineer) |
| **Responsibilities** | Reflect the scope, complexity, and autonomy expected at this level |
| **Requirements** | Calibrated to the level — not over-indexed on the level above |
| **Compensation** | Within the band defined for this level (see Pay Transparency section) |
| **Growth path** | Where this role leads — the next level in the career framework |

When levelling information is not available, ask the hiring manager to describe:

- The scope of independent decision-making
- The complexity of problems the role is expected to solve
- Whether the role manages people, projects, or neither
- Who the role's peers are (for calibration)

### Step 6: EU Pay Transparency Directive Compliance

The EU Pay Transparency Directive (Directive (EU) 2023/970) introduces requirements for pay transparency in job postings. Member states must transpose the Directive by 7 June 2026. Key requirements for job descriptions:

#### Pre-Application Pay Transparency (Article 5)

- Job applicants have the right to receive information on the initial pay level or pay range for the position
- This information must be provided in the job vacancy notice or before the job interview, without the applicant having to request it
- The employer must not ask applicants about their pay history in current or previous employment relationships

#### Compliance Checklist for JDs

| Requirement | How to Comply in the JD |
| --- | --- |
| **Pay range disclosure** | Include the salary range (or starting salary) in the posting. Derive from the organization's pay structure for the job level. |
| **No pay history inquiry** | Do not include questions about current or previous salary in the application process. Remove any such fields from application forms. |
| **Gender-neutral job classification** | Ensure the role title and classification are gender-neutral and based on objective criteria |
| **Equal pay for equal work** | Verify the offered range is consistent with what existing employees at the same level and in comparable roles receive |

#### Implementation Notes

- The Directive requires member state transposition — specific requirements may vary. Monitor transposition in the jurisdictions where the role is posted.
- Even before full transposition, several member states already have national pay transparency requirements (e.g., Germany's Entgelttransparenzgesetz, which provides individual pay information rights for employees in organizations with 200+ employees).
- For compensation band analysis, use the check-compensation skill.

## JD Audit Mode

When reviewing an existing job description rather than writing a new one:

### Audit Scoring Framework

Score each dimension on a 1-5 scale:

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
| --- | --- | --- | --- |
| **Clarity** | Vague responsibilities, unclear expectations | Responsibilities listed but generic | Specific outcomes, clear scope, measurable where appropriate |
| **Requirements calibration** | Inflated requirements, no must/nice distinction | Some distinction but still over-indexed | Clear must/nice separation, capability-based, 5-7 must-haves |
| **Inclusivity** | Gendered language, credential inflation, exclusionary framing | Mostly neutral but some issues | Deliberately inclusive, capability-based, no unnecessary barriers |
| **Levelling accuracy** | Mismatched level signals (too senior or too junior for the actual scope) | Generally aligned but some inconsistencies | Precisely calibrated to the job level |
| **Pay transparency** | No pay information | Vague ("competitive") | Specific range included, compliant with applicable requirements |
| **Employer value** | No information about the role's value or team context | Generic company description | Specific, compelling articulation of why this role matters and what makes the team attractive |

### Audit Output Template

```
JD AUDIT REPORT
================
Role:          [title]
Audited by:    [AI audit — requires HR review]
Date:          [date]

SCORES:
  Clarity:              [1-5] — [brief rationale]
  Requirements:         [1-5] — [brief rationale]
  Inclusivity:          [1-5] — [brief rationale]
  Levelling:            [1-5] — [brief rationale]
  Pay transparency:     [1-5] — [brief rationale]
  Employer value:       [1-5] — [brief rationale]
  Overall:              [average]

ISSUES FOUND:
  [Priority: High/Medium/Low] [Issue description] — [Specific text quoted] — [Recommended fix]

REVISED TEXT (where applicable):
  [Before]: "[original text]"
  [After]:  "[improved text]"
```

## Guardrails

- Never generate compensation data, salary ranges, or market benchmarks. If pay information is not provided, flag it as a required input.
- Never generate organisation-specific culture statements, values, or employer brand messaging. These must come from the organisation.
- In audit mode, quote the specific text being evaluated before suggesting changes. Flag jurisdiction dependencies for pay transparency and anti-discrimination requirements.
- Source-label all output: `[From role requirements]`, `[From job architecture]`, `[JD methodology]`, or `[AI suggestion — verify with HR]`.

> **Tip:** Ask for DOCX or Markdown output via companyFILES to get a formatted document ready for distribution.
