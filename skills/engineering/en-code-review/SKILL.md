---
name: en-code-review
description: Structured code review — check for bugs, security issues, performance regressions, and style violations with actionable feedback. Use when reviewing a PR, auditing a codebase section, or getting a second opinion on your implementation. Trigger with "review this code", "check this PR", "what's wrong with this".
---

# Code Review Skill

Review code changes for bugs, security issues, performance regressions, and style violations. The skill produces prioritised, actionable feedback a developer can work through top-to-bottom. You provide the code or diff yourself, or pull it from a connected source.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Git provider via MCP** (e.g. GitHub, GitLab, Bitbucket) | PR diffs, commit history, linked issues |
| **Project tracker via MCP** (e.g. Jira, Linear, Asana) | Ticket or issue the change addresses |
| **companyRAG / file upload** | Internal style guides, ADRs, security policies |

> **No connected source?** Paste the code or diff in chat or upload the relevant files — the skill works the same way.

## Review Workflow

Run these seven steps in order for every review. Do not skip steps — a review that catches a style nit but misses a security flaw has failed.

### Step 1: Understand Context

Before reading a single line of code, establish:

1. Purpose: What does this change do? Read the PR description, linked ticket, or ask the user. A review without understanding intent cannot distinguish a bug from a feature.
2. Scope: How large is the change? A 10-line bug fix and a 500-line feature addition require different review strategies.
3. Risk profile: What could go wrong? Changes to authentication, billing, data models, or public APIs carry higher risk than CSS adjustments. Calibrate attention accordingly.
4. History: Is this a new feature, a refactor, or a hotfix? Hotfixes under time pressure deserve extra scrutiny for shortcuts that become long-term debt.

### Step 2: Scan for Correctness Bugs

Read the code for logical errors. Focus on:

| Bug Category | What to Look For |
| --- | --- |
| **Off-by-one errors** | Loop bounds, array indexing, pagination, fence-post conditions |
| **Null/undefined handling** | Unguarded dereferences, missing optional chaining, absent nil checks |
| **Type mismatches** | Implicit coercions, wrong generic parameters, serialisation/deserialisation asymmetry |
| **State management** | Race conditions, stale closures, missing state transitions, shared mutable state |
| **Error handling** | Swallowed exceptions, missing error paths, catch blocks that log but do not propagate |
| **Boundary conditions** | Empty collections, zero-length strings, maximum integer values, Unicode edge cases |
| **Data integrity** | Partial writes without transactions, missing rollback on failure, orphaned records |
| **Concurrency** | Missing locks, deadlock potential, non-atomic read-modify-write sequences |

For each suspected bug, verify by tracing the execution path — do not flag based on pattern alone.

### Step 3: Check Security

Apply the relevant OWASP Top 10 categories to the change. Not every category applies to every PR; focus on those relevant to the code under review.

| OWASP Category | Code Review Check |
| --- | --- |
| **Injection** | User input flows into SQL, shell commands, OS calls, template engines, or log statements without sanitisation or parameterisation |
| **Broken Authentication** | Credential handling, session management, token validation, password storage, MFA bypass paths |
| **Sensitive Data Exposure** | Secrets in source, PII in logs, unencrypted storage, overly broad API responses, missing redaction |
| **Broken Access Control** | Missing authorisation checks, IDOR (direct object references without ownership validation), privilege escalation paths |
| **Security Misconfiguration** | Permissive CORS, debug mode in production, default credentials, verbose error responses leaking internals |
| **Insecure Deserialisation** | Untrusted data deserialised into objects, missing schema validation on external input |
| **Dependency vulnerabilities** | New dependencies without vetting, known-vulnerable versions, unnecessary transitive dependencies |

Additionally check for STRIDE threats where relevant:

- Spoofing: Can an attacker impersonate a legitimate user or service?
- Tampering: Can request or response data be modified in transit or at rest?
- Repudiation: Are security-relevant actions logged with sufficient detail for audit?
- Information Disclosure: Does the change leak information through error messages, timing, or side channels?
- Denial of Service: Can the change be abused to exhaust resources (unbounded queries, recursive calls, large uploads)?
- Elevation of Privilege: Can a lower-privilege user reach higher-privilege functionality?

### Step 4: Assess Performance

Evaluate the change for performance regressions. Focus on:

| Area | What to Check |
| --- | --- |
| **Algorithmic complexity** | O(n²) or worse in hot paths, unnecessary nested loops, quadratic string concatenation |
| **Database queries** | N+1 query patterns, missing indices for new query patterns, full table scans, unbounded result sets |
| **Memory allocation** | Large objects created in loops, unbounded caches, missing cleanup of listeners or subscriptions |
| **Network calls** | Sequential calls that could be parallelised, missing timeouts, retry storms, chatty APIs |
| **Rendering** | Unnecessary re-renders, layout thrashing, large DOM updates, missing virtualisation for long lists |
| **Caching** | Missing cache for expensive operations, cache invalidation bugs, unbounded cache growth |

Flag only issues that would have measurable impact at the system's actual scale. A quadratic loop over 5 items is not a performance issue; a quadratic loop over 50,000 is.

### Step 5: Review Style and Maintainability

Check for readability and long-term maintainability:

- Naming: Do variable, function, and class names communicate intent? Would a new team member understand them without context?
- Function length: Functions doing too many things. If a function needs more than one or two paragraphs to explain, it likely needs decomposition.
- Duplication: Code that duplicates existing functionality. Check whether a utility or shared function already exists.
- Abstractions: Are the abstractions at the right level? Over-abstraction (unnecessary interfaces, premature generalisation) is as harmful as under-abstraction.
- Comments: Are complex decisions explained? Are comments accurate (stale comments are worse than no comments)?
- Consistency: Does the code follow the existing patterns in the codebase? Introducing a new pattern for one file creates maintenance burden.
- Test coverage: Are new code paths tested? Are edge cases from Step 2 covered? Are tests testing behaviour (not implementation details)?

When a project style guide is available in a companyRAG collection, review against it. When no style guide is loaded, review against the established patterns in the surrounding code.

### Step 6: Check Operational Readiness

For changes that affect production behaviour:

| Check | Details |
| --- | --- |
| **Observability** | Are new code paths logged at appropriate levels? Are metrics emitted for key operations? Can the team debug this in production? |
| **Feature flags** | Is the change gated behind a feature flag for safe rollout? Should it be? |
| **Backward compatibility** | Does the change break existing API contracts, database schemas, or message formats? |
| **Migration safety** | Are database migrations reversible? Can the migration run while the old code is still serving traffic? |
| **Configuration** | Are new configuration values documented? Do they have sensible defaults? Are secrets handled via environment variables, not hardcoded? |
| **Rollback plan** | Can this change be reverted independently? Are there irreversible side effects (data migration, external notifications)? |

### Step 7: Compose Feedback

Structure the review output using the severity classification and format below.

## Severity Classification

Every finding must be classified. Mixed-severity reviews without classification force the author to guess what matters.

| Severity | Definition | Author Action | Blocks Merge? |
| --- | --- | --- | --- |
| **Critical** | Bug that will cause data loss, security vulnerability, or production outage. Must be fixed. | Fix before merge | Yes |
| **Major** | Significant bug, performance regression, or missing error handling that will cause problems under realistic conditions. | Fix before merge | Yes |
| **Minor** | Code quality issue, style inconsistency, or edge case that is unlikely to cause problems soon but degrades maintainability. | Fix before merge (preferred) or create follow-up ticket | No (team discretion) |
| **Suggestion** | Alternative approach, refactoring opportunity, or knowledge-sharing comment. No correctness issue. | Consider, discuss, or defer | No |

If a review produces zero Critical or Major findings, state that explicitly — "No blocking issues found" is valuable information.

## Review Checklist

Quick-reference checklist condensing the workflow above. Use as a pre-submission check after the full review.

### Correctness

- Logic handles all expected input types and edge cases
- Error paths are handled and tested
- State transitions are complete (no impossible/orphaned states)
- Concurrent access is safe where applicable

### Security

- User input is validated and sanitised before use
- Authorisation checks exist for all protected operations
- No secrets, credentials, or PII in source or logs
- New dependencies are vetted and necessary

### Performance

- No N+1 queries or unbounded result sets
- Hot-path algorithmic complexity is acceptable at production scale
- Network calls have timeouts and error handling
- Resource cleanup exists (listeners, connections, file handles)

### Maintainability

- Names are clear and consistent with codebase conventions
- Functions have a single, understandable responsibility
- No unnecessary duplication of existing utilities
- Tests cover new code paths and edge cases

### Operations

- Logging and metrics are sufficient for production debugging
- Database migrations are backward-compatible and reversible
- Configuration changes are documented with sensible defaults
- Change can be rolled back independently

## Feedback Format

For each finding, use this structure:

```
### [Severity]: [Short title]

**File**: [path/to/file.ext], line [N]
**Category**: [Correctness / Security / Performance / Style / Operations]

**Issue**: [What is wrong and why it matters. Be specific — "this could be null" is less useful than "request.user is undefined when the auth middleware is bypassed on public routes."]

**Suggestion**: [Concrete fix or approach. Show a code snippet when it clarifies the intent.]

**Evidence**: [How you identified this — trace the execution path, reference the documentation, or cite the specific input that triggers the issue.]
```

### Feedback Principles

- Be specific: Reference exact lines, variable names, and execution paths. "This function is confusing" is not actionable.
- Explain why: Connect every finding to a concrete consequence — a crash, a security exposure, a maintenance burden, a performance regression at scale.
- Suggest, don't dictate: Provide a recommended fix, but acknowledge when multiple approaches exist. The author knows the codebase better.
- Separate blocking from non-blocking: The author must know immediately which findings block merge and which are suggestions for improvement.
- Acknowledge good work: When the code handles a tricky case well, demonstrates a clean pattern, or shows good test coverage, say so. Reviews that only flag problems discourage good engineering.
- Batch related issues: If the same pattern recurs across multiple files, flag it once with all locations rather than repeating the same comment.

## Review Sizing Guide

Match review depth to change scope:

| Change Size | Lines Changed | Review Strategy |
| --- | --- | --- |
| **Small** | < 50 lines | Full review, all steps. Quick turnaround expected. |
| **Medium** | 50-300 lines | Full review. Focus extra attention on steps 2-3 (bugs and security). |
| **Large** | 300-1000 lines | Full review but may need multiple passes. Consider requesting the change be split. |
| **Very large** | > 1000 lines | Flag the size as an issue itself. Large PRs hide bugs. Strongly recommend splitting. Review in logical chunks if splitting is not feasible. |

## Guardrails

- Never claim a bug exists without tracing the execution path. Mark uncertain findings as [Suspected — verify execution path].
- Never fabricate security vulnerabilities. Apply OWASP/STRIDE checks to the actual code. If unconfirmed, note as [Potential risk — requires verification].
- Never assume code context not shown. State assumptions explicitly: "Assuming the caller validates X before invoking this function."
- Source-label findings as [From code], [From style guide], or [AI assessment — verify].

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted review report ready to share.
