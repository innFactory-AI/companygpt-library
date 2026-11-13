---
name: en-deployment-prep
description: Pre-deployment verification checklist with rollback planning and progressive rollout guidance. Use when preparing a release, planning a risky deployment, or creating deployment runbooks. Trigger with "prepare deployment", "release checklist", "deploy plan for".
---

# Deployment Prep Skill

Catch deployment issues before they reach your users and keep the blast radius small when they do slip through. This skill covers pre-deployment checklists, rollback planning, canary/blue-green rollout strategies, and communication plans. The context-specific data comes from you, a connected MCP source, or companyRAG collections.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Git provider via MCP** (e.g. GitHub, GitLab) | Release branch, changelog, merged PRs |
| **Project tracker via MCP** (e.g. Jira, Linear) | Completed tickets; verify all planned items are merged |
| **CI system via MCP** (e.g. GitHub Actions, GitLab CI) | CI check status on the release branch |
| **companyRAG / file upload** | Existing runbooks, infrastructure docs, SLA definitions, past post-mortems |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Pre-Deployment Checklist

Work through every section before initiating deployment. Check items off only once verified — do not rely on assumptions.

### Code Readiness

- All planned changes are merged to the release branch
- No open PRs blocking the release
- All CI checks pass on the release branch (tests, linting, type checks, security scans)
- Code review completed for all changes since last deployment
- No known critical or high-severity bugs in the release

### Database and Data

- Database migrations are tested against a production-like dataset
- Migrations are backward-compatible (old code can run against new schema)
- Migration rollback has been tested (if the migration is reversible)
- Large data migrations have been benchmarked for duration and lock impact
- Data backups are current and verified restorable

### Dependencies and Configuration

- New environment variables are set in all target environments
- New feature flags are configured with correct default states
- Third-party service dependencies are operational (check status pages)
- API version compatibility verified with upstream and downstream services
- New secrets are provisioned in the secrets manager

### Infrastructure

- Target environment has sufficient capacity for the release (compute, memory, storage)
- Auto-scaling policies are configured for expected load changes
- Health check endpoints are updated if health criteria changed
- Load balancer routing rules are updated if new services or paths are introduced
- SSL certificates are valid and not near expiration

### Observability

- Monitoring dashboards cover new features and changed components
- Alerts are configured for new failure modes
- Log levels are appropriate (not debug in production)
- Deployment markers or annotations are ready for monitoring tools
- Runbook links are attached to new alerts

### Communication

- Deployment schedule communicated to stakeholders
- On-call engineer identified and available during deployment window
- Customer-facing changes documented for support team
- Maintenance window communicated (if applicable)
- Status page update prepared (if applicable)

## Rollback Plan

Every deployment must have a rollback plan before execution. "Roll forward" is a valid strategy only when explicitly chosen — not when rollback was never planned.

### Rollback Plan Template

```
# Rollback Plan: [Release Version/Name]

## Rollback Decision Criteria
Initiate rollback when ANY of these conditions is met:
- [ ] Error rate exceeds [X]% (baseline: [Y]%)
- [ ] p95 latency exceeds [X]ms (baseline: [Y]ms)
- [ ] Health check failures on [N]+ instances
- [ ] Customer-reported critical issue confirmed
- [ ] Data integrity issue detected

## Rollback Authority
- Primary: [name/role — who can authorise rollback]
- Backup: [name/role]

## Rollback Procedure
1. [Step-by-step procedure specific to your deployment method]
2. [e.g., Revert Kubernetes deployment to previous revision]
3. [e.g., Run database migration rollback script]
4. [e.g., Revert feature flag to previous state]
5. [e.g., Clear CDN/cache if static assets changed]

## Estimated Rollback Time
- Application rollback: [X minutes]
- Database rollback: [X minutes — or "irreversible, see mitigation"]
- Full recovery: [X minutes]

## Irreversible Components
[List any changes that cannot be rolled back — data migrations, external notifications, third-party provisioning — and their mitigation strategy]

## Post-Rollback Verification
- [ ] Application health checks passing
- [ ] Error rate returned to baseline
- [ ] Customer-facing functionality verified
- [ ] Stakeholders notified of rollback
```

### Rollback Strategy by Change Type

| Change Type | Rollback Approach | Considerations |
| --- | --- | --- |
| **Application code only** | Redeploy previous version | Fastest rollback. Verify no state was written that the old version cannot read. |
| **Code + additive schema migration** | Redeploy previous code; leave new schema in place | New columns/tables are harmless to old code if defaults are set. Cleaner than rolling back the migration. |
| **Code + destructive schema migration** | Requires tested migration rollback script | Column renames, drops, and type changes are dangerous. Prefer expand-contract pattern. |
| **Feature flag change** | Toggle flag back to previous state | Fastest. No deployment needed. Verify flag state propagation time. |
| **Infrastructure change** | Revert Terraform/Helm to previous state | Longer rollback time. Some infra changes (DNS, certificate) have propagation delays. |
| **Data migration/backfill** | Restore from backup or run reverse migration | Slowest. May cause data loss for records created after migration. Plan compensating actions. |

## Progressive Rollout Strategies

Choose a rollout strategy based on risk level and infrastructure capability.

### Strategy Selection

| Risk Level | Recommended Strategy | Rationale |
| --- | --- | --- |
| **Low** (config change, copy update, low-traffic feature) | Direct deployment with monitoring | Fast, low overhead. Monitor for 15-30 minutes post-deploy. |
| **Medium** (new feature, API change, dependency update) | Canary deployment | Expose to a small percentage first. Validate before full rollout. |
| **High** (database migration, auth changes, payment flow) | Blue-green with traffic shifting | Full parallel environment. Instant rollback via traffic switch. |
| **Critical** (core infrastructure, multi-service change) | Blue-green + manual verification gates | Full parallel environment with human checkpoints at each stage. |

### Canary Deployment

1. Deploy to canary instances (typically 5-10% of fleet)
2. Route a small percentage of traffic to canary (start at 1-5%)
3. Monitor canary vs. baseline for a defined bake time (minimum 15 minutes):   - Error rates (canary should not exceed baseline + threshold)   - Latency percentiles (p50, p95, p99)   - Business metrics (conversion rate, transaction success rate)
4. If canary is healthy, increase traffic percentage in stages (5% → 25% → 50% → 100%)
5. If canary shows degradation, route all traffic back to baseline and investigate

### Blue-Green Deployment

1. Deploy new version to the green (inactive) environment
2. Run smoke tests against green environment
3. Shift traffic from blue (current) to green:   - Option A: Instant switch (load balancer rule change)   - Option B: Gradual shift (weighted routing, 10% → 50% → 100%)
4. Monitor green environment for the bake time period
5. If healthy, decommission or retain blue as next deployment target
6. If unhealthy, switch traffic back to blue (instant rollback)

### Bake Time Guidance

| System Characteristic | Minimum Bake Time |
| --- | --- |
| Stateless API with consistent traffic | 15-30 minutes |
| Stateful service with sessions | 1-2 hours (full session lifecycle) |
| Batch processing system | 1 full batch cycle |
| System with daily traffic patterns | 24 hours (cover peak and off-peak) |
| System with weekly patterns | Consider extended monitoring through first weekly cycle |

## Deployment Runbook Template

For complex or high-risk deployments, create a step-by-step runbook:

```
# Deployment Runbook: [Release Version/Name]

## Pre-Deployment (T-60 min)
- [ ] Verify pre-deployment checklist complete
- [ ] Confirm on-call engineer availability
- [ ] Take database backup and verify
- [ ] Notify stakeholders of deployment start
- [ ] Open monitoring dashboards

## Deployment Execution
- [ ] Step 1: [specific action with expected outcome]
- [ ] Step 2: [specific action with expected outcome]
- [ ] Step 3: [specific action with expected outcome]
- [ ] Verify: [health check / smoke test / metric check]

## Post-Deployment Verification (T+0 to T+30 min)
- [ ] Health checks passing on all instances
- [ ] Error rate within threshold
- [ ] Latency within threshold
- [ ] Key user flows manually verified
- [ ] No unexpected log entries

## Post-Deployment Monitoring (T+30 min to bake time end)
- [ ] Automated monitoring confirms stability
- [ ] No customer-reported issues
- [ ] Business metrics (if applicable) within expected range

## Deployment Complete
- [ ] Remove deployment marker/annotation
- [ ] Update status page (if maintenance window was communicated)
- [ ] Notify stakeholders of successful deployment
- [ ] Update release notes / changelog
```

## Guardrails

- Never fabricate infrastructure details. Do not assume cloud provider, orchestration platform, or deployment tooling. Ask the user for their context.
- Never generate specific monitoring thresholds. Alert thresholds must come from the user's SLAs and baseline metrics — provide the template for them to fill in.
- Never claim a rollback is safe without understanding the change. Destructive migrations, data backfills, and external side effects may make rollback impossible. Always assess irreversibility explicitly.
- Source-label outputs as `[From user context]`, `[Deployment methodology]`, or `[AI recommendation — verify]`.

> **Tip:** Ask for Markdown or DOCX output via companyFILES to get a formatted runbook ready to share.
