---
name: en-debugging
description: Work through a systematic debugging workflow with hypothesis generation, isolation testing, and root-cause analysis. Use when stuck on a bug, investigating unexpected behaviour, or diagnosing a production issue. Trigger with "help me debug", "why is this happening", "investigate this error".
---

# Debugging Skill

Reason from symptom to root cause through a disciplined methodology for diagnosing software defects. This prevents the two most common debugging failures: random code changes without understanding, and fixing symptoms while root causes persist. Logs, errors, and code come from you, a connected MCP source, companyRAG collections, or file upload.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Error tracking / monitoring via MCP** (e.g. Sentry, Datadog) | Error messages, stack traces, metrics, latency and error-rate trends |
| **Repository via MCP** (e.g. GitHub) | Source code, recent changes, commit history, deployment boundary |
| **companyRAG / file upload** | Pasted logs, stack traces, source files, runbooks, prior incident notes |

> **No connected source?** Paste logs, error messages, or code in chat or upload the relevant files — the skill works the same way.

## Debugging Workflow

Follow these seven phases. The discipline is in NOT skipping phases — the temptation to jump from symptom to fix is the primary cause of debugging failure.

### Phase 1: Reproduce the Bug

A bug you cannot reproduce is a bug you cannot verify as fixed.

**Reproduction checklist:**

1. Identify the exact symptom : What observable behaviour is wrong? Distinguish the symptom ("page shows error 500") from the assumed cause ("the database is down"). Work with the symptom.
2. Establish reproduction steps : What is the minimum sequence of actions that triggers the symptom? Strip away everything unrelated.
3. Determine consistency : Does it happen every time (deterministic) or intermittently (non-deterministic)? Intermittent bugs require additional data collection before hypothesis generation.
4. Identify the environment : Where does it occur? Production only? Staging? Local? The difference narrows the search space.
5. Find the boundary : What is the most recent change after which the bug appeared? Check recent deployments, configuration changes, data migrations, and dependency updates.

**When reproduction fails:**

- Increase logging at the suspected area and wait for recurrence
- Check whether the bug is environment-specific (data, configuration, scale, timing)
- Look for non-deterministic triggers: race conditions, cache state, clock-dependent logic, external service behaviour
- Ask: "Under what conditions would this code produce this symptom?" and work backward

### Phase 2: Gather Evidence

Collect data before forming hypotheses. Premature hypotheses create confirmation bias.

| Evidence Type | Where to Look | What to Extract |
| --- | --- | --- |
| **Error messages** | Application logs, browser console, stderr | Exact message, error code, stack trace |
| **Stack traces** | Exception handlers, crash dumps, APM tools | Full call chain, the frame where the error originates vs. where it is caught |
| **Logs** | Application logs, system logs, request logs | Entries from the time window around the failure, correlated by request ID or timestamp |
| **Metrics** | APM dashboards, infrastructure monitoring | Latency spikes, error rate changes, resource utilisation (CPU, memory, connections) |
| **State** | Database, cache, session storage, message queues | Actual values at the time of failure vs. expected values |
| **Recent changes** | Git log, deployment history, config changes | What changed between "working" and "not working" |

**Evidence triage:** Not all evidence is equally valuable. Prioritise:

1. The error message and stack trace (most direct)
2. What changed recently (highest prior probability)
3. Correlated timing with external events (deployment, traffic spike, dependency outage)

### Phase 3: Form Hypotheses

Generate candidate explanations ranked by probability. A good hypothesis is:

- Specific : "The user session cookie is not being set because the SameSite attribute is Strict and the login flow involves a cross-origin redirect" — not "something is wrong with cookies."
- Testable : You can design an observation or experiment that would confirm or refute it.
- Falsifiable : You can describe what evidence would prove it wrong.

**Hypothesis generation techniques:**

1. Change-based : What changed recently? The most common cause of "it was working yesterday" is "something changed today." Check deployments, config changes, dependency updates, data migrations, and infrastructure changes.
2. Error-message driven : Parse the error message literally. Error messages are often precise — "Connection refused on port 5432" means exactly what it says before it means anything else.
3. Fault-tree analysis : Work backward from the symptom. "The API returns 500" → "The handler threw an uncaught exception" → "The database query failed" → "The connection pool is exhausted" → "Connections are leaking because transactions are not closed on error paths."
4. Analogical : Have you seen a similar symptom before? What caused it then? Apply cautiously — similar symptoms can have different causes.

**Rank hypotheses** by: (1) consistency with all evidence, (2) simplicity (Occam's razor), (3) proximity to recent changes.

### Phase 4: Isolate and Test

Test each hypothesis starting with the most probable. The goal is to confirm or eliminate.

**Isolation techniques:**

| Technique | When to Use | Method |
| --- | --- | --- |
| **Binary search (bisect)** | Bug appeared at an unknown point in a sequence of changes | git bisect or manually halve the change range until the introducing commit is found |
| **Minimal reproduction** | Bug occurs in a complex system | Strip components one at a time until you find the minimum setup that still triggers the bug |
| **Variable substitution** | Uncertain whether the issue is data, code, or environment | Swap one variable at a time: run the same code with different data, the same data with different code, or the same code+data in a different environment |
| **Logging injection** | Internal state is opaque | Add targeted logging at decision points to trace actual execution path vs. expected path |
| **Breakpoint debugging** | Need to inspect state at a specific point in execution | Set breakpoints before the failure point and inspect variable state step by step |
| **Divide and conquer** | Multiple components could be at fault | Test each component in isolation to identify which one produces the incorrect output |

**Isolation discipline:**

- Change ONE thing at a time. If you change two things and the bug disappears, you do not know which change fixed it.
- Record what you tried and what you observed. Debugging without notes leads to re-testing the same hypothesis.
- Set a time-box. If a hypothesis cannot be confirmed or eliminated within a reasonable time, park it and move to the next one.

### Phase 5: Verify Root Cause

Finding the line that breaks is not enough. Establish WHY it breaks.

**Root cause verification:**

1. Explain the full chain : Can you trace from root cause → intermediate failures → observed symptom without gaps? If there are gaps, the root cause may be deeper.
2. Predict other symptoms : If this is the root cause, what other observable effects should exist? Check for those effects as corroborating evidence.
3. Explain the timing : Why did the bug appear now? If the root cause was always present, what changed to trigger it (data pattern, load, dependency behaviour, configuration)?
4. Distinguish root cause from contributing factors : The root cause is what must change to prevent recurrence. Contributing factors made the impact worse but are not the origin.

**5 Whys technique (applied to code):**

```
Symptom: Users see a blank page after login
Why 1: The dashboard API returns a 500 error
Why 2: The user profile query throws a null pointer exception
Why 3: The "preferences" field is null for newly created users
Why 4: The user creation endpoint does not initialise the preferences object
Why 5: The preferences initialisation was removed during a refactor (commit abc123)
Root cause: Refactor removed preferences initialisation without updating the user creation path
```

Stop when you reach a cause that is actionable and systemic — something you can fix in a way that prevents the entire class of bug.

### Phase 6: Fix and Verify

1. Write the fix : Address the root cause, not just the symptom. If the root cause is "user creation does not initialise preferences," the fix is to initialise preferences — not to add a null check in the dashboard.
2. Add a regression test : Write a test that fails without the fix and passes with it. This is the single most important step for preventing recurrence.
3. Verify the fix : Confirm the original symptom no longer occurs using the exact reproduction steps from Phase 1.
4. Check for collateral damage : Did the fix break anything else? Run the existing test suite. Check related functionality manually if test coverage is incomplete.

### Phase 7: Prevent Recurrence

The bug is fixed. Now ask: why did the system allow this bug to exist?

| Prevention Category | Actions |
| --- | --- |
| **Detection** | Could monitoring or alerting have caught this earlier? Add alerts for the failure mode. |
| **Defence in depth** | Could input validation, type safety, or invariant checks have prevented the bad state? |
| **Process** | Was this a category of bug that code review, testing, or linting should have caught? Update checklists or tooling. |
| **Documentation** | Is there an implicit assumption that should be made explicit? Document the invariant. |

## Debugging Strategies by Bug Type

Different bug categories benefit from different investigation approaches. Use the general workflow above, but adjust emphasis based on the bug type.

### Race Conditions and Concurrency Bugs

- Reproduce under load or with artificial delays (sleep statements at suspected race points)
- Look for shared mutable state accessed without synchronisation
- Check for time-of-check to time-of-use (TOCTOU) patterns
- Add logging with thread/process IDs and timestamps to establish event ordering
- Consider whether the fix needs to be atomic (transaction, lock, CAS operation)

### Memory Leaks

- Use profiling tools to take heap snapshots at intervals and compare
- Look for event listeners not removed, closures retaining large scopes, growing caches without eviction
- Check for circular references preventing garbage collection
- Reproduce under sustained load, not just single-request testing

### Performance Regressions

- Profile before guessing — measure to find the actual bottleneck, not the assumed one
- Compare metrics from before and after the regression appeared
- Check for N+1 query patterns, missing indices, algorithmic complexity changes, serialisation overhead
- Verify under realistic data volumes — performance issues often only manifest at scale

### Intermittent Failures (Flaky Behaviour)

- Increase sample size: run the reproduction many times and track the failure rate
- Look for timing dependencies: network latency, thread scheduling, cache warm/cold state
- Check for external dependencies: is the test or feature dependent on a service that is occasionally slow or unavailable?
- Isolate randomness: fix seeds, mock time, stub external calls to make the test deterministic

### Data-Dependent Bugs

- Compare the data that triggers the bug with data that does not — what differs?
- Check for encoding issues (Unicode, character sets, byte order marks)
- Look for boundary values: empty strings, null vs. empty, very large values, special characters
- Verify data assumptions: does the code assume uniqueness, ordering, or format that the data does not guarantee?

## Guardrails

- Never diagnose without evidence. Walk through evidence and hypothesis testing. If evidence is insufficient, say what additional data is needed — do not pattern-match to a conclusion.
- Never fabricate error messages, stack traces, or log output. All diagnostic data must come from the user. Label illustrative examples as [Illustrative example — not from your system] .
- Never claim a fix is verified without reproduction. If the user has not confirmed the symptom is resolved, state that verification is pending.
- Source-label conclusions as [From evidence] , [Hypothesis — requires testing] , or [Debugging methodology] .

> **Tip:** Ask for a Markdown or DOCX write-up via companyFILES to capture the investigation and root-cause analysis as a shareable document.
