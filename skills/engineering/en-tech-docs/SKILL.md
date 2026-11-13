---
name: en-tech-docs
description: Write technical documentation — API references, runbooks, ADRs, and onboarding guides — from code context or informal descriptions. Use when documenting a system, creating onboarding materials, or writing an ADR. Trigger with "write docs for", "document this API", "create an ADR for".
---

# Tech Docs Skill

Produce technical documentation — API references, runbooks, ADRs, onboarding guides, and READMEs — from code, informal descriptions, or system context. The skill routes to the right template and ensures docs are useful on day one and maintainable for the long run.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **companyRAG collection** | Existing docs, architecture context, code conventions |
| **Git provider via MCP** (e.g. GitHub, GitLab) | Source code, commit history, existing documentation |
| **File upload / companyFILES** | Export in the team's preferred format (DOCX, PDF) |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Document Type Router

Start here. The document type determines the template, audience, and level of detail.

| Document Type | Use When | Primary Audience | Key Characteristic |
| --- | --- | --- | --- |
| **API Reference** | Documenting a REST, GraphQL, or RPC API | Developers consuming the API | Exhaustive, machine-parseable, example-driven |
| **Runbook** | Documenting an operational procedure | On-call engineers, SREs | Step-by-step, executable under pressure |
| **ADR** | Recording an architecture or design decision | Current and future engineers | Context-preserving, decision-focused |
| **Onboarding Guide** | Helping new team members get productive | New engineers joining the team | Progressive, assumption-free, practical |
| **README** | Introducing a project, service, or library | Anyone encountering the code for the first time | Concise, self-contained, quick-start oriented |

If the document does not fit these types, ask the user to describe the audience and purpose — then adapt the closest template.

## Documentation Principles

Apply to every document type:

1. Write for the reader, not the author. The reader does not know what you know. Do not assume context that is not on the page.
2. Start with why. Before explaining how something works, explain why someone would need to know this.
3. Show, then tell. Lead with a concrete example, then explain the general pattern. Examples are the most-read part of any technical document.
4. Keep it current or delete it. Stale documentation is worse than no documentation — it actively misleads. If a document cannot be maintained, mark it with a staleness warning or remove it.
5. One source of truth. Do not duplicate information across documents. Reference the authoritative source instead. Duplicated docs drift apart.

## API Reference Template

```
# [API Name] Reference

## Overview
[One paragraph: what this API does, who uses it, and how to get started.]

## Authentication
[Authentication method, token format, where to obtain credentials.]

## Base URL
[Base URL for each environment — production, staging, sandbox.]

## Endpoints

### [HTTP Method] [Path]
[One-line description of what this endpoint does.]

**Request**

| Parameter | Location | Type | Required | Description |
|---|---|---|---|---|
| [name] | [path/query/header/body] | [type] | [yes/no] | [what it is] |

**Request Example**
[Complete, copy-pasteable request with realistic (but not real) data.]

**Response**

| Field | Type | Description |
|---|---|---|
| [name] | [type] | [what it means] |

**Response Example**
[Complete response body with realistic data.]

**Error Responses**

| Status Code | Error Code | Description | Resolution |
|---|---|---|---|
| [code] | [error_code] | [what went wrong] | [how to fix it] |

[Repeat for each endpoint.]

## Rate Limits
[Limits per endpoint or globally. What happens when exceeded.]

## Pagination
[Pagination mechanism (cursor, offset), parameters, default page size.]

## Versioning
[How API versions are specified. Deprecation policy.]

## Changelog
[Recent changes with dates. Breaking changes highlighted.]
```

## Runbook Template

```
# Runbook: [Procedure Name]

## Purpose
[What problem does this runbook solve? When should it be used?]

## Prerequisites
- [ ] [Access/permissions required]
- [ ] [Tools that must be installed]
- [ ] [Context that must be understood before starting]

## Severity / Urgency
[When is this runbook triggered? What is the time pressure?]

## Steps

### Step 1: [Action]
**Command/Action:**
[Exact command or UI steps. Copy-pasteable.]

**Expected Output:**
[What you should see if it worked.]

**If It Fails:**
[What to do if this step does not produce the expected output.]

### Step 2: [Action]
[Repeat pattern for each step.]

## Verification
[How to confirm the procedure was successful. Specific checks.]

## Rollback
[How to undo the procedure if something goes wrong.]

## Escalation
[Who to contact if the runbook does not resolve the issue.]

## History
| Date | Author | Change |
|---|---|---|
| [date] | [name] | [what changed] |
```

## Architecture Decision Record (ADR) Template

```
# ADR-[NNN]: [Decision Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-NNN]

## Date
[YYYY-MM-DD]

## Context
[What technical or business situation prompted this decision? What forces are at play? What constraints exist? Write enough that someone reading this in two years understands the situation without asking follow-up questions.]

## Decision
[The decision, stated clearly. "We will [do X] for [purpose Y]."]

## Options Considered

### Option A: [Name]
- Pros: [list]
- Cons: [list]

### Option B: [Name]
- Pros: [list]
- Cons: [list]

## Consequences
- [What becomes easier as a result of this decision]
- [What becomes harder]
- [What new constraints are introduced]
- [What follow-up decisions are needed]

## Review Triggers
[When should this decision be revisited? Specific conditions, not vague "periodically".]
```

## Onboarding Guide Template

```
# Onboarding: [Team/System Name]

## Welcome
[One paragraph: what this team or system does and why it exists.]

## Before Your First Day
- [ ] [Account/access setup]
- [ ] [Software to install]
- [ ] [Documents to read]

## Day 1: Getting Running
[Step-by-step guide to get the development environment set up. Assume nothing beyond a standard laptop.]

### Clone and Build
[Exact commands. Expected output at each step.]

### Run Locally
[How to start the system. How to verify it is running.]

### Run Tests
[How to run the test suite. How to interpret the output.]

## Week 1: Understanding the System
[Architecture overview. Key components and how they interact. Links to deeper docs.]

### Architecture Overview
[High-level diagram description. Major components and their responsibilities.]

### Key Concepts
[Domain-specific terms and concepts a new engineer needs to know.]

### Where Things Live
[Directory structure, important files, configuration locations.]

## Week 2-4: Contributing
[How to pick up a task, make a change, submit a PR, get it reviewed and deployed.]

### Development Workflow
[Branch naming, commit conventions, PR process, CI/CD pipeline.]

### Common Tasks
[Step-by-step guides for the most frequent types of changes — new endpoint, new UI component, database migration, etc.]

## Who to Ask
[Team members and their areas of expertise. Communication channels.]

## Glossary
[Domain terms, acronyms, and internal jargon with definitions.]
```

## README Template

```
# [Project Name]

[One sentence: what this project does.]

## Quick Start

[Minimum steps to get the project running. Target: under 5 minutes for a developer with the prerequisites installed.]

## Prerequisites

- [Runtime and version]
- [Package manager]
- [Any external services]

## Installation

[Exact commands.]

## Usage

[The most common use case with a concrete example.]

## Configuration

[Environment variables, config files, and their purpose. Defaults noted.]

## Development

[How to set up the development environment, run tests, and submit changes.]

## Architecture

[Brief overview of the project structure. What lives where and why.]

## Troubleshooting

[Common issues and their solutions.]

## Contributing

[How to contribute. Link to more detailed contributing guide if it exists.]
```

## Guardrails

- Never fabricate API endpoints, parameters, or response formats. When API details are not provided, generate the template with `[TO BE FILLED]` placeholders.
- Never invent system architecture or operational procedures. Flag gaps explicitly: `[Missing: describe the authentication mechanism used by this service]`.
- Never generate unverified code examples. Mark source: `[From user-provided code]`, `[From API documentation]`, or `[Illustrative example — verify against actual API]`.
- Prefer incomplete and accurate over complete and fabricated. A document with marked gaps is more trustworthy than one filled with plausible but unverified details.

> **Tip:** Ask for Markdown, DOCX, or PDF output via companyFILES to get a formatted doc ready to share.
