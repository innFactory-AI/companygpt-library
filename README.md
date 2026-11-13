# companyGPT Library

Ready-made content for companyGPT that customers can take as it is: agent skills and agents in German and
English, plus curated admin defaults. 76 skills across 12 categories, each in both languages.

Each skill is a self-contained prompt that teaches an agent one job: how to run a QBR, prep a deployment, audit SEO,
or query a companyRAG collection. They are prompt-first: every skill works without code execution and is designed
around companyGPT's MCP servers, companyRAG collections and companyFILES output tools. Some skills add an optional
code-execution section (always with a fallback) and bundle longer recipes as extra files (`references/…`), which the
agent only has when the skill is installed as a package (zip), not when just `SKILL.md` is pasted.

## Layout

```text
catalog.json                                 # skill categories, order, docs index texts
skills/<category>/<locale>-<id>/SKILL.md     # one skill per language: skills/files/de-excel, skills/files/en-excel
skills/<category>/<locale>-<id>/references/  # optional bundled files (part of the skill package)
pages/<category>/<id>.<locale>.md            # docs page wrapper (title, label, intro)
agents/<locale>-<slug>.yaml                  # ready-made agents (DemoGPT, Researcher) per language
admin/model-labels/                          # curated model labels (LibreChat modelSpecs) per language
```

Skill names carry the language as a prefix (`de-excel`, `en-excel`), so both languages can be installed in the
same companyGPT at the same time. Agents do the same (`agent_de_demogpt`, `agent_en_demogpt`) and use the skills of
their language.

This repo is the single source for the skills on [docs.company-gpt.com](https://docs.company-gpt.com)
(Tutorials → Skills). The docs build generates its skill pages from `main`, and every push to `main` redeploys the
docs. See [AGENTS.md](AGENTS.md) for the authoring rules and workflow. It replaces
[company-ai-stack-skills](https://github.com/innFactory-AI/company-ai-stack-skills), where both languages used the
same skill names.

## Usage

- **Skills:** in companyGPT, upload a `SKILL.md` under **Skills**, or paste its contents into a new skill. Skills
  with bundled files are uploaded as a zip package of the skill folder; the docs offer it as a download.
- **Library Sync:** administrators connect this repo in companyADMIN **Library Sync** (no token needed) with the
  sources `skill` → `skills` and optionally `agent` → `agents`. A source can also be a single domain, e.g.
  `skills/files`. To use only one language, exclude the other one under **Exclude**.
- **Model labels:** see [admin/model-labels/README.md](admin/model-labels/README.md).

The agent picks a skill up when a request matches its `description`. Placeholders such as `<your-collection>` /
`<deine-collection>` need to be filled in with your own values first.

## Skills

### General · Allgemein

| Skill | DE | EN |
| --- | --- | --- |
| Tool Search · Tool-Suche | [`de-tool-search`](skills/generic/de-tool-search/SKILL.md) | [`en-tool-search`](skills/generic/en-tool-search/SKILL.md) |
| File Routing · Datei-Routing | [`de-file-routing`](skills/generic/de-file-routing/SKILL.md) | [`en-file-routing`](skills/generic/en-file-routing/SKILL.md) |

### companyRAG

| Skill | DE | EN |
| --- | --- | --- |
| AI Search | [`de-ai-search`](skills/company-rag/de-ai-search/SKILL.md) | [`en-ai-search`](skills/company-rag/en-ai-search/SKILL.md) |
| Dataset | [`de-dataset`](skills/company-rag/de-dataset/SKILL.md) | [`en-dataset`](skills/company-rag/en-dataset/SKILL.md) |

### companyLEARN

| Skill | DE | EN |
| --- | --- | --- |
| Course Authoring · Kurse erstellen | [`de-course-authoring`](skills/company-learn/de-course-authoring/SKILL.md) | [`en-course-authoring`](skills/company-learn/en-course-authoring/SKILL.md) |

### companyFILES

| Skill | DE | EN |
| --- | --- | --- |
| Charts & Diagrams · Charts & Diagramme | [`de-charts-diagram`](skills/files/de-charts-diagram/SKILL.md) | [`en-charts-diagram`](skills/files/en-charts-diagram/SKILL.md) |
| Convert · Konvertierung | [`de-convert`](skills/files/de-convert/SKILL.md) | [`en-convert`](skills/files/en-convert/SKILL.md) |
| Excel | [`de-excel`](skills/files/de-excel/SKILL.md) | [`en-excel`](skills/files/en-excel/SKILL.md) |
| File Management · Dateiverwaltung | [`de-file-management`](skills/files/de-file-management/SKILL.md) | [`en-file-management`](skills/files/en-file-management/SKILL.md) |
| PDF | [`de-pdf`](skills/files/de-pdf/SKILL.md) | [`en-pdf`](skills/files/en-pdf/SKILL.md) |
| PowerPoint | [`de-powerpoint`](skills/files/de-powerpoint/SKILL.md) | [`en-powerpoint`](skills/files/en-powerpoint/SKILL.md) |
| Settings & UI · Einstellungen & UI | [`de-settings-ui`](skills/files/de-settings-ui/SKILL.md) | [`en-settings-ui`](skills/files/en-settings-ui/SKILL.md) |
| Templates · Vorlagen | [`de-templates`](skills/files/de-templates/SKILL.md) | [`en-templates`](skills/files/en-templates/SKILL.md) |
| Word & ODT | [`de-word-odt`](skills/files/de-word-odt/SKILL.md) | [`en-word-odt`](skills/files/en-word-odt/SKILL.md) |
| CAD, BIM & 3D | [`de-cad-bim`](skills/files/de-cad-bim/SKILL.md) | [`en-cad-bim`](skills/files/en-cad-bim/SKILL.md) |

### Customer Success

| Skill | DE | EN |
| --- | --- | --- |
| Onboarding Plan · Onboarding-Plan | [`de-onboarding-plan`](skills/customer-success/de-onboarding-plan/SKILL.md) | [`en-onboarding-plan`](skills/customer-success/en-onboarding-plan/SKILL.md) |
| QBR Builder · QBR-Builder | [`de-qbr-builder`](skills/customer-success/de-qbr-builder/SKILL.md) | [`en-qbr-builder`](skills/customer-success/en-qbr-builder/SKILL.md) |
| Customer Health · Kundengesundheit | [`de-customer-health`](skills/customer-success/de-customer-health/SKILL.md) | [`en-customer-health`](skills/customer-success/en-customer-health/SKILL.md) |
| Escalation Brief · Eskalations-Brief | [`de-escalation-brief`](skills/customer-success/de-escalation-brief/SKILL.md) | [`en-escalation-brief`](skills/customer-success/en-escalation-brief/SKILL.md) |
| Renewal Prep · Vertragsverlängerung | [`de-renewal-prep`](skills/customer-success/de-renewal-prep/SKILL.md) | [`en-renewal-prep`](skills/customer-success/en-renewal-prep/SKILL.md) |
| Success Plan · Success-Plan | [`de-success-plan`](skills/customer-success/de-success-plan/SKILL.md) | [`en-success-plan`](skills/customer-success/en-success-plan/SKILL.md) |

### Engineering

| Skill | DE | EN |
| --- | --- | --- |
| Deployment Prep · Deployment-Vorbereitung | [`de-deployment-prep`](skills/engineering/de-deployment-prep/SKILL.md) | [`en-deployment-prep`](skills/engineering/en-deployment-prep/SKILL.md) |
| Code Review · Code-Review | [`de-code-review`](skills/engineering/de-code-review/SKILL.md) | [`en-code-review`](skills/engineering/en-code-review/SKILL.md) |
| Standup | [`de-standup`](skills/engineering/de-standup/SKILL.md) | [`en-standup`](skills/engineering/en-standup/SKILL.md) |
| Tech Debt · Tech-Debt | [`de-tech-debt`](skills/engineering/de-tech-debt/SKILL.md) | [`en-tech-debt`](skills/engineering/en-tech-debt/SKILL.md) |
| Debugging | [`de-debugging`](skills/engineering/de-debugging/SKILL.md) | [`en-debugging`](skills/engineering/en-debugging/SKILL.md) |
| Tech Docs · Technische Doku | [`de-tech-docs`](skills/engineering/de-tech-docs/SKILL.md) | [`en-tech-docs`](skills/engineering/en-tech-docs/SKILL.md) |
| Architecture Design · Architektur-Design | [`de-architecture-design`](skills/engineering/de-architecture-design/SKILL.md) | [`en-architecture-design`](skills/engineering/en-architecture-design/SKILL.md) |
| Postmortem | [`de-postmortem`](skills/engineering/de-postmortem/SKILL.md) | [`en-postmortem`](skills/engineering/en-postmortem/SKILL.md) |
| Test Planning · Test-Planung | [`de-test-planning`](skills/engineering/de-test-planning/SKILL.md) | [`en-test-planning`](skills/engineering/en-test-planning/SKILL.md) |

### Human Resources

| Skill | DE | EN |
| --- | --- | --- |
| Interview Guide · Interview-Leitfaden | [`de-interview-guide`](skills/human-resources/de-interview-guide/SKILL.md) | [`en-interview-guide`](skills/human-resources/en-interview-guide/SKILL.md) |
| Performance Review · Leistungsbeurteilung | [`de-performance-review`](skills/human-resources/de-performance-review/SKILL.md) | [`en-performance-review`](skills/human-resources/en-performance-review/SKILL.md) |
| Employee Onboarding · Mitarbeiter-Onboarding | [`de-employee-onboarding`](skills/human-resources/de-employee-onboarding/SKILL.md) | [`en-employee-onboarding`](skills/human-resources/en-employee-onboarding/SKILL.md) |
| Learning Plan · Lernplan | [`de-learning-plan`](skills/human-resources/de-learning-plan/SKILL.md) | [`en-learning-plan`](skills/human-resources/en-learning-plan/SKILL.md) |
| Compensation · Vergütung | [`de-compensation`](skills/human-resources/de-compensation/SKILL.md) | [`en-compensation`](skills/human-resources/en-compensation/SKILL.md) |
| Job Description · Stellenbeschreibung | [`de-job-description`](skills/human-resources/de-job-description/SKILL.md) | [`en-job-description`](skills/human-resources/en-job-description/SKILL.md) |

### IT Knowledge Management

| Skill | DE | EN |
| --- | --- | --- |
| Change Request | [`de-change-request`](skills/it-knowledge-management/de-change-request/SKILL.md) | [`en-change-request`](skills/it-knowledge-management/en-change-request/SKILL.md) |
| Security Assessment · Security-Assessment | [`de-security-assessment`](skills/it-knowledge-management/de-security-assessment/SKILL.md) | [`en-security-assessment`](skills/it-knowledge-management/en-security-assessment/SKILL.md) |
| Vendor Assessment · Vendor-Assessment | [`de-vendor-assessment`](skills/it-knowledge-management/de-vendor-assessment/SKILL.md) | [`en-vendor-assessment`](skills/it-knowledge-management/en-vendor-assessment/SKILL.md) |
| IT Docs · IT-Doku | [`de-it-docs`](skills/it-knowledge-management/de-it-docs/SKILL.md) | [`en-it-docs`](skills/it-knowledge-management/en-it-docs/SKILL.md) |
| Incident Response | [`de-incident-response`](skills/it-knowledge-management/de-incident-response/SKILL.md) | [`en-incident-response`](skills/it-knowledge-management/en-incident-response/SKILL.md) |
| Knowledge Article | [`de-knowledge-article`](skills/it-knowledge-management/de-knowledge-article/SKILL.md) | [`en-knowledge-article`](skills/it-knowledge-management/en-knowledge-article/SKILL.md) |

### Marketing

| Skill | DE | EN |
| --- | --- | --- |
| Content Draft · Content-Entwurf | [`de-content-draft`](skills/marketing/de-content-draft/SKILL.md) | [`en-content-draft`](skills/marketing/en-content-draft/SKILL.md) |
| Brand Voice | [`de-brand-voice`](skills/marketing/de-brand-voice/SKILL.md) | [`en-brand-voice`](skills/marketing/en-brand-voice/SKILL.md) |
| Performance Report · Performance-Report | [`de-performance-report`](skills/marketing/de-performance-report/SKILL.md) | [`en-performance-report`](skills/marketing/en-performance-report/SKILL.md) |
| Campaign Planning · Kampagnen-Planung | [`de-campaign-planning`](skills/marketing/de-campaign-planning/SKILL.md) | [`en-campaign-planning`](skills/marketing/en-campaign-planning/SKILL.md) |
| Email Sequence · E-Mail-Sequenz | [`de-email-sequence`](skills/marketing/de-email-sequence/SKILL.md) | [`en-email-sequence`](skills/marketing/en-email-sequence/SKILL.md) |
| SEO Audit · SEO-Audit | [`de-seo-audit`](skills/marketing/de-seo-audit/SKILL.md) | [`en-seo-audit`](skills/marketing/en-seo-audit/SKILL.md) |

### Operations

| Skill | DE | EN |
| --- | --- | --- |
| Change Management · Change-Management | [`de-change-management`](skills/operations/de-change-management/SKILL.md) | [`en-change-management`](skills/operations/en-change-management/SKILL.md) |
| Status Report · Statusbericht | [`de-status-report`](skills/operations/de-status-report/SKILL.md) | [`en-status-report`](skills/operations/en-status-report/SKILL.md) |
| Capacity Planning · Kapazitätsplanung | [`de-capacity-planning`](skills/operations/de-capacity-planning/SKILL.md) | [`en-capacity-planning`](skills/operations/en-capacity-planning/SKILL.md) |
| Process Doc · Prozess-Doku | [`de-process-doc`](skills/operations/de-process-doc/SKILL.md) | [`en-process-doc`](skills/operations/en-process-doc/SKILL.md) |
| Process Optimization · Prozessoptimierung | [`de-process-optimization`](skills/operations/de-process-optimization/SKILL.md) | [`en-process-optimization`](skills/operations/en-process-optimization/SKILL.md) |
| Risk Assessment · Risikobewertung | [`de-risk-assessment`](skills/operations/de-risk-assessment/SKILL.md) | [`en-risk-assessment`](skills/operations/en-risk-assessment/SKILL.md) |
| Runbook | [`de-runbook`](skills/operations/de-runbook/SKILL.md) | [`en-runbook`](skills/operations/en-runbook/SKILL.md) |
| Compliance Tracking · Compliance-Tracking | [`de-compliance-tracking`](skills/operations/de-compliance-tracking/SKILL.md) | [`en-compliance-tracking`](skills/operations/en-compliance-tracking/SKILL.md) |

### Product Management

| Skill | DE | EN |
| --- | --- | --- |
| Competitor Brief · Wettbewerber-Briefing | [`de-competitor-brief`](skills/product-management/de-competitor-brief/SKILL.md) | [`en-competitor-brief`](skills/product-management/en-competitor-brief/SKILL.md) |
| Sprint Planning · Sprint-Planung | [`de-sprint-planning`](skills/product-management/de-sprint-planning/SKILL.md) | [`en-sprint-planning`](skills/product-management/en-sprint-planning/SKILL.md) |
| Stakeholder Update · Stakeholder-Update | [`de-stakeholder-update`](skills/product-management/de-stakeholder-update/SKILL.md) | [`en-stakeholder-update`](skills/product-management/en-stakeholder-update/SKILL.md) |
| Research Synthesis · Research-Synthese | [`de-research-synthesis`](skills/product-management/de-research-synthesis/SKILL.md) | [`en-research-synthesis`](skills/product-management/en-research-synthesis/SKILL.md) |
| Metrics Review · Metriken-Review | [`de-metrics-review`](skills/product-management/de-metrics-review/SKILL.md) | [`en-metrics-review`](skills/product-management/en-metrics-review/SKILL.md) |
| Product Brainstorm · Produkt-Brainstorming | [`de-product-brainstorm`](skills/product-management/de-product-brainstorm/SKILL.md) | [`en-product-brainstorm`](skills/product-management/en-product-brainstorm/SKILL.md) |
| Roadmap Update · Roadmap-Update | [`de-roadmap-update`](skills/product-management/de-roadmap-update/SKILL.md) | [`en-roadmap-update`](skills/product-management/en-roadmap-update/SKILL.md) |
| Product Spec · Produkt-Spec | [`de-product-spec`](skills/product-management/de-product-spec/SKILL.md) | [`en-product-spec`](skills/product-management/en-product-spec/SKILL.md) |

### Productivity

| Skill | DE | EN |
| --- | --- | --- |
| Meeting Prep · Meeting-Vorbereitung | [`de-meeting-prep`](skills/productivity/de-meeting-prep/SKILL.md) | [`en-meeting-prep`](skills/productivity/en-meeting-prep/SKILL.md) |
| Weekly Review · Wochenrückblick | [`de-weekly-review`](skills/productivity/de-weekly-review/SKILL.md) | [`en-weekly-review`](skills/productivity/en-weekly-review/SKILL.md) |
| Memory Management · Memory-Management | [`de-memory-management`](skills/productivity/de-memory-management/SKILL.md) | [`en-memory-management`](skills/productivity/en-memory-management/SKILL.md) |

### Sales

| Skill | DE | EN |
| --- | --- | --- |
| Deal Strategy · Deal-Strategie | [`de-deal-strategy`](skills/sales/de-deal-strategy/SKILL.md) | [`en-deal-strategy`](skills/sales/en-deal-strategy/SKILL.md) |
| Account Research · Account-Research | [`de-account-research`](skills/sales/de-account-research/SKILL.md) | [`en-account-research`](skills/sales/en-account-research/SKILL.md) |
| Forecast | [`de-forecast`](skills/sales/de-forecast/SKILL.md) | [`en-forecast`](skills/sales/en-forecast/SKILL.md) |
| Battlecard | [`de-battlecard`](skills/sales/de-battlecard/SKILL.md) | [`en-battlecard`](skills/sales/en-battlecard/SKILL.md) |
| Call Prep · Gesprächsvorbereitung | [`de-call-prep`](skills/sales/de-call-prep/SKILL.md) | [`en-call-prep`](skills/sales/en-call-prep/SKILL.md) |
| Pipeline Review · Pipeline-Review | [`de-pipeline-review`](skills/sales/de-pipeline-review/SKILL.md) | [`en-pipeline-review`](skills/sales/en-pipeline-review/SKILL.md) |
| Sales Asset · Sales-Asset | [`de-sales-asset`](skills/sales/de-sales-asset/SKILL.md) | [`en-sales-asset`](skills/sales/en-sales-asset/SKILL.md) |
| Outreach | [`de-outreach`](skills/sales/de-outreach/SKILL.md) | [`en-outreach`](skills/sales/en-outreach/SKILL.md) |
| Call Summary · Gesprächszusammenfassung | [`de-call-summary`](skills/sales/de-call-summary/SKILL.md) | [`en-call-summary`](skills/sales/en-call-summary/SKILL.md) |

## Agents

| Agent | DE | EN |
| --- | --- | --- |
| DemoGPT: all-round agent with the key tools and skills | [`de-demogpt.yaml`](agents/de-demogpt.yaml) | [`en-demogpt.yaml`](agents/en-demogpt.yaml) |
| Researcher · Recherche-Agent: web research subagent of DemoGPT | [`de-researcher.yaml`](agents/de-researcher.yaml) | [`en-researcher.yaml`](agents/en-researcher.yaml) |

## License

See [LICENSE](LICENSE).
