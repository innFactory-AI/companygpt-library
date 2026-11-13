---
name: en-architecture-design
description: System design with trade-off analysis, capacity estimation, and architecture decision records. Use when designing a new system, evaluating architectural options, or documenting design decisions. Trigger with "design architecture for", "how should we build", "architecture for [system]".
---

# Architecture Design Skill

Design software systems from requirements through documented architecture decisions. The skill covers trade-off analysis, capacity estimation, and Architecture Decision Records (ADRs) for decisions that are expensive to reverse. Context and existing material come from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Wiki / docs via MCP** (e.g. Confluence, GitHub) | Existing architecture docs, ADRs, infrastructure diagrams, system inventories |
| **Project tracker via MCP** (e.g. Jira, Linear) | Epics, requirements, and technical spikes |
| **companyRAG / file upload** | Existing design documents, assessments, notes from discovery sessions |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Design Workflow

Run these six phases sequentially. The first two phases (requirements and constraints) must be complete before generating architectural options — designing without understanding constraints produces solutions that cannot be built.

### Phase 1: Clarify Requirements

Separate functional requirements (what the system does) from non-functional requirements (how well it does it). Both shape architecture, but non-functional requirements typically have a larger impact on architectural choices.

**Functional requirements gathering:**

1. List the core use cases. For each: who is the actor, what do they do, what is the expected outcome?
2. Identify data entities and their relationships. What data does the system create, read, update, and delete?
3. Map integration points. What external systems does this interact with? What are their APIs, data formats, and reliability characteristics?
4. Define the system boundary. What is inside the system being designed, and what is an external dependency?

**Non-functional requirements (quality attributes):**

Probe each attribute. Not all are equally important — the user must prioritise.

| Attribute | Key Questions |
| --- | --- |
| **Availability** | What is the target uptime? What is the cost of downtime (per minute, per hour)? Which components are critical vs. degradable? |
| **Scalability** | What are the expected load levels (users, requests/sec, data volume) at launch and at 1yr/3yr? Is growth linear or bursty? |
| **Latency** | What are the response time targets? p50, p95, p99? Which operations are latency-sensitive? |
| **Durability** | What is the acceptable data loss window? Zero (financial data) or small window (analytics)? |
| **Consistency** | Does the system need strong consistency (bank transfers) or is eventual consistency acceptable (social feeds)? |
| **Security** | What data classification levels? What compliance frameworks (SOC 2, GDPR, HIPAA, PCI-DSS)? What are the threat actors? |
| **Operability** | What is the team's operational capacity? 24/7 on-call or business-hours only? What observability maturity? |
| **Cost** | What is the budget? CapEx vs. OpEx preference? Cost optimisation priority relative to other attributes? |

**Gate**: A prioritised list of non-functional requirements exists with measurable targets. "The system should be fast" is not a requirement. "p95 API latency under 200ms at 10,000 concurrent users" is.

### Phase 2: Identify Constraints

Constraints are non-negotiable boundaries. They eliminate options before you evaluate them.

| Constraint Category | Examples |
| --- | --- |
| **Technical** | Must integrate with existing Oracle database; team only has Python expertise; must run on-premises |
| **Organisational** | Must launch within 3 months; cannot hire new engineers; must use approved vendor list |
| **Regulatory** | Data must reside in EU; must comply with PCI-DSS; audit log retention of 7 years |
| **Financial** | Infrastructure budget of $X/month; no new licensing costs; must reduce current hosting cost |
| **Existing commitments** | Already signed contract with cloud provider X; existing SLA with upstream service Y |

Document every constraint. Unstated constraints surface during implementation as blockers.

### Phase 3: Propose Architectural Options

Generate at minimum two and ideally three distinct options. A design document with one option is a justification, not a decision.

For each option:

1. Architecture style: monolith, modular monolith, microservices, event-driven, serverless, CQRS, etc.
2. Component diagram: name the major components, their responsibilities, and how they communicate (sync vs. async, protocols, data formats).
3. Data architecture: where does data live? What are the storage technologies and data flow patterns?
4. Deployment model: how and where does it run? Cloud region, container orchestration, scaling approach.
5. Key technical choices: the 3–5 decisions within this option that most impact the system's behaviour.

**Option generation strategies:**

- Vary the primary decomposition axis: one option decomposes by business domain, another by technical layer, another by deployment unit.
- Vary the consistency/availability trade-off: one option favours strong consistency, another favours availability with eventual consistency.
- Vary the build/buy ratio: one option builds a custom component, another uses a managed service, another uses an open-source solution.

### Phase 4: Analyse Trade-offs

This is the core intellectual work of architecture. Use the trade-off matrix below.

**Trade-off Analysis Matrix:**

For each non-functional requirement from Phase 1, score each option:

```
| Requirement       | Target              | Option A       | Option B       | Option C       |
|-------------------|---------------------|----------------|----------------|----------------|
| Availability      | 99.9%               | [assessment]   | [assessment]   | [assessment]   |
| Scalability       | 50k concurrent      | [assessment]   | [assessment]   | [assessment]   |
| Latency (p95)     | < 200ms             | [assessment]   | [assessment]   | [assessment]   |
| Operational cost  | < $X/month          | [assessment]   | [assessment]   | [assessment]   |
| Time to market    | 3 months            | [assessment]   | [assessment]   | [assessment]   |
| Team capability   | Current skills      | [assessment]   | [assessment]   | [assessment]   |
```

For each cell, assess as: Meets / Partially meets / Does not meet — with a brief explanation.

**Common architectural trade-offs to address explicitly:**

| Trade-off | Tension |
| --- | --- |
| **Consistency vs. availability** | CAP theorem — in a partition, you choose one. Which does this system prioritise and why? |
| **Simplicity vs. flexibility** | A monolith is simpler to develop and deploy; microservices offer independent scaling and deployment. What does the system actually need? |
| **Latency vs. throughput** | Batching improves throughput but increases latency. Which matters more for this use case? |
| **Build vs. buy** | Custom code gives control; managed services reduce operational burden. What is the team's operational capacity? |
| **Coupling vs. autonomy** | Shared databases simplify data access; independent data stores enable team autonomy. What is the organisational structure? |
| **Cost now vs. cost later** | A quick solution may incur technical debt; a robust solution takes longer. What is the time horizon? |

**Failure mode analysis** (for each option):

1. What happens when [component X] fails?
2. What is the blast radius — which other components are affected?
3. How does the system detect the failure?
4. How does the system recover — automatically, with manual intervention, or not at all?
5. What data is at risk during the failure window?

### Phase 5: Estimate Capacity

Back-of-the-envelope calculations to validate that the proposed architecture can handle the expected load. These are order-of-magnitude estimates — precise numbers come from load testing. Work the estimate through as a reasoning exercise directly in chat; no code or execution is needed.

**Capacity estimation framework:**

1. Start with user behaviour: how many users? How many actions per user per day? What is the peak-to-average ratio?
2. Convert to system load: actions per second at peak. Read-to-write ratio. Payload sizes.
3. Estimate storage: data per record × records per day × retention period. Account for indices, replicas, and backups.
4. Estimate compute: requests per second × processing time per request = required compute capacity. Add headroom (typically 2–3x for peak handling and growth).
5. Estimate network: data transfer per request × requests per second. Cross-region replication if applicable.

**Estimation template:**

```
CAPACITY ESTIMATE: [System Name]
Assumptions (state all):
  - [Users: X]
  - [Actions per user per day: Y]
  - [Peak-to-average ratio: Z]
  - [Read:write ratio: R:W]
  - [Average payload size: N KB]

Peak load:
  X users × Y actions/day ÷ 86,400 sec/day × Z peak ratio = [N] req/sec at peak

Storage (1 year):
  [N] writes/day × [M] bytes/write × 365 days = [T] GB/year
  With indices and replicas (× 3 estimate): [T×3] GB/year

Compute:
  [N] req/sec × [M] ms/req = [C] compute-seconds/sec
  Required instances: [C] ÷ [instance capacity] = [I] instances + [headroom]

Validation: Does this fit within the cost constraint from Phase 2?
```

### Phase 6: Document the Decision

Record the decision using an Architecture Decision Record (ADR). The ADR is the deliverable — without it, the reasoning is lost and the decision will be re-debated.

## Architecture Decision Record (ADR) Template

```
# ADR-[NNN]: [Decision Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-NNN]

## Date
[YYYY-MM-DD]

## Context
[What is the architectural question being addressed? What forces are at play — technical, organisational, business? What constraints exist?]

## Decision
[The architectural choice made. State it clearly: "We will use [approach X] for [purpose Y]."]

## Options Considered

### Option A: [Name]
- Description: [brief]
- Pros: [list]
- Cons: [list]

### Option B: [Name]
- Description: [brief]
- Pros: [list]
- Cons: [list]

### Option C: [Name] (if applicable)
- Description: [brief]
- Pros: [list]
- Cons: [list]

## Trade-off Analysis
[The matrix from Phase 4, summarised. Which requirements drove the decision?]

## Capacity Estimate
[Summary from Phase 5 — key numbers that validate the choice]

## Consequences
[What becomes easier? What becomes harder? What new constraints does this decision introduce?]

## Risks
[What could go wrong with this decision? What would trigger reconsideration?]

## Review Triggers
[Under what conditions should this decision be revisited? Examples: traffic exceeds 10x estimate, team size doubles, compliance requirements change.]
```

> **Tip:** If the ADR should include a diagram, provide it in the output as a Mermaid block — companyFILES can render Mermaid.

## Architecture Evaluation Checklist

Use after completing the design to validate completeness:

### Requirements Coverage

- Every functional requirement maps to a component
- Every non-functional requirement has a measurable target and the design addresses it
- All integration points are identified with protocols, data formats, and failure modes

### Resilience

- Single points of failure are identified and mitigated (or accepted as documented risk)
- Failure modes for each component are documented with recovery strategies
- Data backup and recovery strategy exists with tested RPO/RTO targets
- Graceful degradation paths exist for non-critical components

### Scalability

- Capacity estimates validate the design handles target load
- Horizontal scaling path exists for the bottleneck components
- Data partitioning strategy exists if single-node storage is insufficient

### Security

- Data classification is applied (what is sensitive, what is public)
- Authentication and authorisation boundaries are defined
- Network segmentation separates trust zones
- Encryption at rest and in transit is specified

### Operability

- Observability strategy covers metrics, logs, and traces
- Deployment strategy supports zero-downtime releases
- Rollback procedure exists for each deployable component
- On-call scope is defined — what requires human intervention vs. automatic recovery

### Evolutionary Architecture

- The design allows components to be replaced independently
- The decision includes review triggers for when the architecture should be reconsidered
- Migration paths exist from the current state if this is a redesign

## Guardrails

- Never fabricate performance numbers or benchmarks. Performance depends on configuration, hardware, and workload. State `[Requires benchmarking with your workload and configuration]` instead.
- Never recommend specific technologies without user context. Structure the trade-off analysis; do not assert one option is better without knowing the requirements.
- Never present capacity estimates as precise. Label all estimates as `[Order-of-magnitude estimate — validate with load testing]`.
- Source-label outputs as `[From user requirements]`, `[Design methodology]`, or `[AI assessment — verify]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted document ready for distribution. companyFILES renders Mermaid blocks as a separate interactive diagram with PNG download, not inside the document.
