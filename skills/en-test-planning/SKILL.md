---
name: en-test-planning
description: Testing strategy with coverage targets, test type allocation, and quality gate definitions. Use when planning tests for a new feature, reviewing test coverage, or setting up CI quality gates. Trigger with "plan testing for", "test strategy for", "what should I test".
---

# Test Planning Skill

Plan what to test, how to test it, and how much testing is enough. The skill covers test type selection, coverage targeting, test pyramid allocation, and quality gate definitions — preventing both under-testing (shipping bugs) and over-testing (slow pipelines, brittle suites).

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Project tracker via MCP** (e.g. Jira, Linear) | Feature requirements and acceptance criteria for test mapping |
| **Git provider via MCP** (e.g. GitHub, GitLab) | Code under test, existing test suites, CI configuration |
| **Test management via MCP** (e.g. TestRail) | Existing test cases, test runs, coverage history |
| **companyRAG / file upload** | Existing test plans, quality standards, architecture docs |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Test Strategy Workflow

### Step 1: Understand What You Are Testing

Before selecting test types, understand the change:

1. What is the feature or change? Summarise in one sentence.
2. What are the acceptance criteria? Each criterion maps to at least one test.
3. What are the risk areas? Where would a bug cause the most damage (data loss, security breach, revenue impact, user-facing error)?
4. What is the existing test coverage? Are there tests for the surrounding code? What types? Where are the gaps?
5. What are the integration points? External APIs, databases, message queues, third-party services — each is a testing boundary.

### Step 2: Apply the Test Pyramid

The test pyramid is a cost-efficiency model, not a rigid rule. Allocate test investment based on feedback speed and defect detection value.

| Layer | Test Type | Scope | Execution Speed | Defect Types Caught | Relative Cost |
| --- | --- | --- | --- | --- | --- |
| **Base** | Unit tests | Single function or class in isolation | Milliseconds | Logic errors, boundary conditions, calculation bugs, edge cases | Lowest |
| **Middle** | Integration tests | Multiple components interacting | Seconds | Interface mismatches, data flow errors, configuration issues, query bugs | Medium |
| **Top** | End-to-end tests | Full user workflow through the system | Seconds to minutes | Workflow failures, deployment issues, environment-specific bugs | Highest |

**Pyramid allocation guideline** (starting point — adjust based on risk analysis):

- ~70% unit tests — fast, cheap, catch most logic bugs
- ~20% integration tests — verify component interactions and data flow
- ~10% end-to-end tests — validate critical user paths work through the entire stack

**When to invert the pyramid:**

- Legacy systems with no unit tests: start with integration and e2e tests to establish a safety net, then add unit tests as you refactor
- UI-heavy changes with minimal logic: more e2e and visual regression tests, fewer unit tests
- Infrastructure changes: more integration and smoke tests, fewer unit tests

### Step 3: Select Test Types

Not every test type applies to every change. Use this selection matrix:

| Test Type | Use When | Skip When |
| --- | --- | --- |
| **Unit tests** | Business logic, algorithms, data transformations, utility functions | Thin wrappers, pure delegation, generated code |
| **Integration tests** | Database queries, API endpoints, service-to-service communication, message handlers | No external dependencies involved |
| **End-to-end tests** | Critical user workflows, checkout/payment flows, authentication, data-critical paths | Low-risk internal tooling, experimental features |
| **Contract tests** | Service boundaries in a microservices or API-consumer architecture | Monolithic systems with no service boundaries |
| **Performance tests** | Latency-sensitive operations, high-throughput paths, operations at scale | Low-traffic internal tools, one-off scripts |
| **Security tests** | Authentication, authorisation, input handling, data access boundaries | No user input, no sensitive data |
| **Visual regression tests** | UI components, design system changes, responsive layouts | Backend-only changes, API-only changes |
| **Smoke tests** | Post-deployment verification in each environment | Already covered by e2e tests in CI |

### Step 4: Define Test Cases

For each test type selected, structure test cases:

**Test case structure:**

```
TEST CASE: [descriptive name]
  Type:           [Unit / Integration / E2E / Contract / Performance / Security]
  Requirement:    [Acceptance criterion or risk area being verified]
  Preconditions:  [System state before test — data setup, configuration, user role]
  Input:          [What triggers the behaviour under test]
  Expected result: [Observable, verifiable outcome]
  Edge cases:     [Boundary values, empty inputs, error conditions to include as sub-cases]
  Priority:       [Critical / High / Medium / Low]
```

**Test case generation heuristics:**

| Technique | When to Apply |
| --- | --- |
| **Equivalence partitioning** | Input has distinct categories with similar expected behaviour — test one value per partition |
| **Boundary value analysis** | Numeric ranges, string lengths, collection sizes — test at, just below, and just above boundaries |
| **Error guessing** | Null/undefined, empty strings, zero, negative numbers, extremely large values, special characters |
| **State transition testing** | Stateful workflows (order lifecycle, subscription status) — test every valid and invalid transition |
| **Pairwise/combinatorial** | Multiple independent parameters — test combinations that cover all pairs without exhaustive enumeration |
| **Happy path + failure path** | Every feature — confirm it works correctly AND confirm it fails gracefully |

### Step 5: Set Coverage Targets

Coverage is a necessary but not sufficient measure of test quality. High coverage with poor assertions catches nothing.

**Coverage targeting guidance:**

| Code Category | Recommended Coverage | Rationale |
| --- | --- | --- |
| **Business-critical logic** | 90%+ line coverage | Bugs here cause revenue loss, data corruption, or security breaches |
| **Core application code** | 80%+ line coverage | Standard target — balances thoroughness with maintenance cost |
| **Utility/helper code** | 70%+ line coverage | Lower risk, but still used broadly |
| **Generated code, thin wrappers** | Exclude from targets | Testing generated code tests the generator, not your system |
| **Configuration, DI wiring** | Integration test coverage | Unit testing configuration is low-value; integration tests verify it works |

**Coverage metrics to track:**

- Line coverage: Which lines execute during tests. The baseline metric.
- Branch coverage: Which conditional branches execute. More meaningful than line coverage — catches untested paths in if/else, switch, ternary expressions.
- Mutation coverage (when feasible): Whether tests detect inserted faults. The gold standard for test effectiveness, but expensive to run. Use selectively on critical code.

**Coverage anti-patterns to flag:**

- Coverage without assertions (tests that execute code but never verify outcomes)
- Coverage targets that incentivise testing getters/setters instead of business logic
- Excluding failing tests from coverage reports to hit targets

### Step 6: Define Quality Gates

Quality gates are automated pass/fail criteria in the CI pipeline.

**Recommended quality gates:**

| Gate | Threshold | Stage | Blocks Merge? |
| --- | --- | --- | --- |
| **All tests pass** | 100% pass rate | Every PR | Yes |
| **No new test failures** | Zero regressions | Every PR | Yes |
| **Coverage threshold** | Per team standard (e.g., 80%) | Every PR | Yes (for new code) |
| **No coverage decrease** | Coverage delta ≥ 0% | Every PR | Yes (recommended) |
| **Performance budget** | p95 latency ≤ threshold | Pre-deploy | Yes (for critical paths) |
| **Security scan** | No critical/high findings | Pre-deploy | Yes |
| **E2E smoke suite** | 100% pass rate | Post-deploy to staging | Yes (blocks production deploy) |

**Quality gate design principles:**

- Gates must be fast. A gate that takes 30 minutes to run will be bypassed. Move slow gates to asynchronous or nightly pipelines.
- Gates must be reliable. A flaky gate trains engineers to ignore failures. Fix or remove flaky gates within one sprint.
- Gates must be actionable. Every gate failure must produce a clear message explaining what failed and how to fix it.
- Gates should ratchet. Set thresholds based on current state and incrementally tighten — do not set aspirational targets that block all work.

## Output Template — Test Plan

```
# Test Plan: [Feature/Change Name]

## Overview
- Feature: [name and brief description]
- Risk level: [Critical / High / Medium / Low]
- Test types selected: [list]
- Estimated test effort: [hours/days]

## Test Pyramid Allocation
- Unit tests: [count/percentage] — [what they cover]
- Integration tests: [count/percentage] — [what they cover]
- E2E tests: [count/percentage] — [what they cover]
- Other: [type: count] — [what they cover]

## Test Cases
[Structured test cases per Step 4]

## Coverage Targets
- New code: [target]%
- Modified code: [target]%
- Excluded from coverage: [list with rationale]

## Quality Gates
[Gate definitions per Step 6]

## Risks and Gaps
- [Areas with insufficient test coverage and rationale]
- [Dependencies that cannot be tested in CI and mitigation]
- [Known test infrastructure limitations]
```

## Guardrails

- Never fabricate coverage numbers or test counts. If current coverage data is not provided, state "Current coverage data needed — request from CI reports."
- Never claim specific defect detection rates. Defect detection depends on test quality, not test type alone.
- This skill plans strategy and produces the test plan and test cases as text — it does not run code, scripts, or test runners. Illustrative test code shown inside an output template is fine as text; writing production-ready tests requires knowing the language, framework, and test library.
- Source-label outputs as `[From user context]`, `[Testing methodology]`, or `[AI recommendation — verify]`.

> **Tip:** Ask for XLSX or Markdown output via companyFILES to get a formatted test plan ready to share.
