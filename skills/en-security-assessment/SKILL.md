---
name: en-security-assessment
description: Assess proposed changes, features, and system modifications against security and data protection policies using STRIDE-based threat modeling, data flow analysis, access control review, and EU data protection assessment. Use when reviewing a new integration, evaluating a feature for security implications, or running a pre-deployment security check. Trigger with "security assessment for", "is this integration safe", "review security of".
---

# Security Assessment Skill

Assess the security implications of proposed changes, integrations, and system modifications using STRIDE-based threat modeling, data flow analysis, access control review, and EU data protection considerations. System-specific details come from you, a connected MCP source, or companyRAG collections — the skill analyses the information provided and does not run scans itself.

## Where the Data Comes From

| Source | What It Adds |
| --- | --- |
| **Security tools via MCP** (e.g. vulnerability scanners, SIEM, ticketing) | Scan results, vulnerability findings, security incidents, open tickets |
| **companyRAG collections** | Architecture documentation, security policies, prior assessments, data flow descriptions |
| **File upload** | System diagrams, requirement documents, integration specs, contract documents |

> **No connected source?** Provide the data in chat or upload the relevant files — the skill works the same way.

## Assessment Workflow

### Step 1: Define Assessment Scope

Before analyzing anything, establish boundaries:

| Scope Element | Question to Answer |
| --- | --- |
| **Subject** | What is being assessed? (feature, integration, infrastructure change, architecture proposal) |
| **Data involved** | What data does this touch? Classify: Public, Internal, Confidential, Restricted/PII |
| **System boundaries** | Which systems, services, or components are in scope? What is explicitly out of scope? |
| **Users and actors** | Who interacts with this? (end users, admins, service accounts, external systems, third parties) |
| **Deployment context** | Where does this run? (production, staging, internal only, customer-facing, multi-tenant) |
| **Regulatory context** | Which regulations apply? (GDPR, NIS2, DORA, AI Act, industry-specific) |

A clear scope prevents the assessment from expanding indefinitely. Document what is NOT being assessed as explicitly as what is.

### Step 2: Data Flow Analysis

Map how data moves through the system under assessment. This is the foundation for identifying exposure points.

#### Data Flow Diagram Elements

For each data flow, document:

```
Source → [Protocol/Method] → Destination
  Data: [what data is transmitted]
  Classification: [Public / Internal / Confidential / Restricted]
  Authentication: [how the connection is authenticated]
  Encryption: [in transit / at rest / both / none]
  Storage: [where data persists, retention period]
```

#### Data Flow Inventory Table

| # | Source | Destination | Data | Classification | Auth | Encryption | Storage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [component] | [component] | [description] | [level] | [method] | [TLS/mTLS/none] | [where/how long] |
| 2 | [component] | [component] | [description] | [level] | [method] | [TLS/mTLS/none] | [where/how long] |

Pay special attention to:

- Trust boundary crossings: Data moving between networks, environments, organizations, or jurisdictions
- Data aggregation points: Where multiple data flows converge (databases, logs, analytics)
- Data transformation points: Where data is enriched, combined, or derived (may create new data classifications)
- External integrations: Any connection to a third-party service or system

### Step 3: Threat Modeling (STRIDE-Based)

Apply STRIDE to each component and data flow identified in Step 2. STRIDE is a mnemonic for six threat categories developed at Microsoft. For each category, identify whether the threat applies and what the impact would be.

#### STRIDE Categories

| Category | Threat | Question | Examples |
| --- | --- | --- | --- |
| **S — Spoofing** | Impersonation of a user or system | Can an attacker pretend to be a legitimate user, service, or component? | Stolen credentials, forged tokens, IP spoofing, certificate impersonation |
| **T — Tampering** | Unauthorized modification of data | Can an attacker modify data in transit, at rest, or during processing? | SQL injection, parameter manipulation, log tampering, man-in-the-middle |
| **R — Repudiation** | Denial of actions performed | Can a user deny performing an action with no way to prove otherwise? | Missing audit logs, unsigned transactions, no activity tracking |
| **I — Information Disclosure** | Unauthorized data exposure | Can an attacker access data they should not see? | Verbose error messages, insecure storage, log leakage, API over-exposure |
| **D — Denial of Service** | Disruption of service availability | Can an attacker or fault make the service unavailable? | Resource exhaustion, rate limit bypass, cascading failures, dependency failure |
| **E — Elevation of Privilege** | Gaining unauthorized access levels | Can an attacker gain higher privileges than intended? | Broken access control, privilege escalation, insecure default roles |

#### STRIDE Application Process

For each component or data flow in scope:

1. Walk through each STRIDE category
2. For each applicable threat, document: Threat description: What specifically could happen. Attack vector: How an attacker would exploit this. Existing controls: What mitigations are already in place. Residual risk: What risk remains after existing controls. Recommended mitigation: Additional controls to consider
3. Skip categories that genuinely don't apply (e.g., Repudiation may not matter for a read-only public API) — but document WHY they don't apply

#### Threat Assessment Table

| # | Component/Flow | STRIDE Category | Threat | Existing Controls | Residual Risk | Severity | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [name] | [S/T/R/I/D/E] | [description] | [what's in place] | [what remains] | [C/H/M/L] | [action] |

### Step 4: Access Control Review

Evaluate the authorization model for the system under assessment:

#### Authentication Assessment

| Criterion | Assessment |
| --- | --- |
| **Authentication method** | What mechanism? (SSO, username/password, API key, certificate, service account) |
| **MFA enforcement** | Is MFA required? For which users/roles? Can it be bypassed? |
| **Credential management** | How are credentials stored, rotated, and revoked? |
| **Service-to-service auth** | How do services authenticate to each other? (mTLS, JWT, shared secrets, IAM roles) |
| **Session management** | Session duration, timeout, concurrent session handling, revocation |

#### Authorization Assessment

| Criterion | Assessment |
| --- | --- |
| **Access model** | RBAC, ABAC, ACL, or custom? |
| **Least privilege** | Are default permissions minimal? Do users start with no access and get granted what they need? |
| **Separation of duties** | Can a single user both create and approve sensitive actions? |
| **Admin access** | How many admin accounts exist? Are they personal or shared? Are admin actions audited? |
| **API authorization** | Are API endpoints individually authorized? Is there scope-based access control? |
| **Data-level access** | Can users access only their own data (multi-tenancy)? How is tenant isolation enforced? |

#### Access Control Findings Template

```
## Access Control Findings

### Strengths
- [What is well-implemented]

### Gaps
| # | Gap | Risk | Severity | Recommendation |
|---|-----|------|----------|---------------|
| 1 | [description] | [what could happen] | [C/H/M/L] | [action] |

### Excessive Permissions Identified
| Principal | Current Access | Required Access | Action |
|-----------|---------------|----------------|--------|
| [user/role/service] | [what they have] | [what they need] | [reduce/revoke] |
```

### Step 5: EU Data Protection Assessment

For any system processing personal data of EU/EEA individuals, assess data protection implications:

| Criterion | Assessment |
| --- | --- |
| **Personal data processed** | What categories of personal data? (identifiers, contact, behavioral, sensitive/special category) |
| **Lawful basis** | What legal basis under GDPR Article 6 (and Article 9 for special categories)? |
| **Purpose limitation** | Is data used only for the stated purpose? Could new processing expand scope? |
| **Data minimization** | Is only necessary data collected? Could the same outcome be achieved with less data? |
| **Storage limitation** | What is the retention period? Is automated deletion in place? |
| **Cross-border transfers** | Does data leave the EU/EEA? What transfer mechanism is in place? |
| **Processor relationships** | Are any third parties processing data? Is there a DPA in place per Article 28? |
| **DPIA trigger** | Does this processing trigger a Data Protection Impact Assessment per Article 35? (New technology, profiling, large-scale processing, automated decision-making) |

Flag any processing that would require a DPIA or changes to the Records of Processing Activities (ROPA). For detailed GDPR operational workflows, refer the user to the handle-gdpr skill.

### Step 6: Risk Scoring and Prioritization

Score each finding from the assessment using the following matrix:

#### Severity Levels

| Level | Definition |
| --- | --- |
| **Critical** | Exploitable vulnerability with high likelihood, leading to data breach, complete service compromise, or regulatory penalty. Requires immediate action. |
| **High** | Significant security gap that could be exploited under realistic conditions. Material risk of data exposure or service disruption. Requires action before deployment. |
| **Medium** | Security weakness that increases risk but requires additional factors to exploit. Should be addressed in the next development cycle. |
| **Low** | Minor security improvement opportunity. Enhances defense-in-depth but not an immediate risk. Address opportunistically. |

#### Prioritization Logic

1. Critical findings block deployment or approval. No exceptions without documented CISO/risk-owner sign-off.
2. High findings must have a remediation plan with a deadline before approval is granted. Compensating controls may be accepted as interim mitigation.
3. Medium findings are logged in the risk register and tracked to resolution. They do not block deployment.
4. Low findings are documented as recommendations and addressed at the team's discretion.

### Step 7: Assessment Report

```
# Security Assessment Report

**Subject**: [what was assessed]
**Date**: [date]
**Assessor**: [name/team]
**Assessment type**: [Pre-deployment / Integration review / Architecture review / Periodic review]
**Overall risk rating**: [Critical / High / Medium / Low]

## Executive Summary
[3-5 sentences: what was assessed, key findings, overall risk posture, primary recommendations.]

## Scope
[From Step 1 — what is in scope, what is explicitly excluded.]

## Data Flow Summary
[From Step 2 — high-level data flow description with trust boundary crossings highlighted.]

## Threat Model Findings
[From Step 3 — STRIDE findings table, ordered by severity.]

## Access Control Findings
[From Step 4 — authentication and authorization assessment results.]

## Data Protection Findings
[From Step 5 — EU data protection assessment, DPIA trigger analysis.]

## Risk Register

| # | Finding | Category | Severity | Recommendation | Owner | Status |
|---|---------|----------|----------|---------------|-------|--------|
| 1 | [description] | [STRIDE/Access/Data Protection] | [C/H/M/L] | [action] | [name] | [Open] |

## Conditions for Approval
[List any conditions that must be met before the change/feature/integration can proceed.]

## Accepted Risks
[Risks explicitly accepted by the risk owner, with justification and sign-off.]
```

---

## Common Integration Security Patterns

When assessing third-party integrations, check these patterns:

| Pattern | Security Concern | What to Verify |
| --- | --- | --- |
| **OAuth 2.0 connection** | Token scope, refresh token storage, consent screen accuracy | Minimum required scopes, secure token storage, token expiration handling |
| **Webhook receiver** | Input validation, authentication of incoming requests | HMAC signature verification, IP allowlisting, payload validation |
| **API key integration** | Key exposure, rotation, scope limitation | Key storage (vault, not code), rotation process, per-environment keys |
| **File sync / data export** | Data exfiltration, over-sharing, stale permissions | What data is shared, who can access shared data, retention on the remote side |
| **SSO / SAML federation** | Trust boundary expansion, attribute mapping, session management | Assertion validation, audience restriction, signed assertions, session timeout alignment |
| **Embedded iframe / widget** | XSS, clickjacking, data leakage via postMessage | CSP headers, sandbox attributes, origin validation for cross-origin messaging |

---

## Guardrails

- Never assess a system's security from training data. All system-specific details come from the user. Do not generate vulnerability assessments based on assumed architecture.
- Never claim a system is "secure" or "safe." Use "no findings identified in scope" — security assessments identify known risks, not certify absence of risk.
- Never generate specific CVEs from memory. Vulnerability databases change daily — use web search to verify.
- Source-label all output: `[From system description]`, `[Assessment framework]`, or `[AI analysis — verify with security team]`. Mark unevaluated STRIDE categories explicitly.

> **Tip:** Ask for DOCX, XLSX, or Markdown output via companyFILES to get a formatted report ready to share.
