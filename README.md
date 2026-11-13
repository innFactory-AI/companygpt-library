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
catalog.json                          # skill categories, order, docs index texts
skills/<locale>-<id>/SKILL.md         # one skill per language: skills/de-excel, skills/en-excel
skills/<locale>-<id>/references/      # optional bundled files (part of the skill package)
pages/<locale>/<category>/<id>.md     # docs page wrapper (title, label, intro)
agents/<locale>-<slug>.yaml           # ready-made agents (DemoGPT, Researcher) per language
admin/model-labels/                   # curated model labels (LibreChat modelSpecs) per language
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
  sources `skill` → `skills` and optionally `agent` → `agents`. To use only one language, exclude the other one
  under **Exclude**.
- **Model labels:** see [admin/model-labels/README.md](admin/model-labels/README.md).

The agent picks a skill up when a request matches its `description`. Placeholders such as `<your-collection>` /
`<deine-collection>` need to be filled in with your own values first.

## Skills

### General · Allgemein

| Skill | DE | EN |
| --- | --- | --- |
| Tool Search · Tool-Suche | [`de-tool-search`](skills/de-tool-search/SKILL.md) | [`en-tool-search`](skills/en-tool-search/SKILL.md) |
| File Routing · Datei-Routing | [`de-file-routing`](skills/de-file-routing/SKILL.md) | [`en-file-routing`](skills/en-file-routing/SKILL.md) |

### companyRAG

| Skill | DE | EN |
| --- | --- | --- |
| AI Search | [`de-ai-search`](skills/de-ai-search/SKILL.md) | [`en-ai-search`](skills/en-ai-search/SKILL.md) |
| Dataset | [`de-dataset`](skills/de-dataset/SKILL.md) | [`en-dataset`](skills/en-dataset/SKILL.md) |

### companyLEARN

| Skill | DE | EN |
| --- | --- | --- |
| Course Authoring · Kurse erstellen | [`de-course-authoring`](skills/de-course-authoring/SKILL.md) | [`en-course-authoring`](skills/en-course-authoring/SKILL.md) |

### companyFILES

| Skill | DE | EN |
| --- | --- | --- |
| Charts & Diagrams · Charts & Diagramme | [`de-charts-diagram`](skills/de-charts-diagram/SKILL.md) | [`en-charts-diagram`](skills/en-charts-diagram/SKILL.md) |
| Convert · Konvertierung | [`de-convert`](skills/de-convert/SKILL.md) | [`en-convert`](skills/en-convert/SKILL.md) |
| Excel | [`de-excel`](skills/de-excel/SKILL.md) | [`en-excel`](skills/en-excel/SKILL.md) |
| File Management · Dateiverwaltung | [`de-file-management`](skills/de-file-management/SKILL.md) | [`en-file-management`](skills/en-file-management/SKILL.md) |
| PDF | [`de-pdf`](skills/de-pdf/SKILL.md) | [`en-pdf`](skills/en-pdf/SKILL.md) |
| PowerPoint | [`de-powerpoint`](skills/de-powerpoint/SKILL.md) | [`en-powerpoint`](skills/en-powerpoint/SKILL.md) |
| Settings & UI · Einstellungen & UI | [`de-settings-ui`](skills/de-settings-ui/SKILL.md) | [`en-settings-ui`](skills/en-settings-ui/SKILL.md) |
| Templates · Vorlagen | [`de-templates`](skills/de-templates/SKILL.md) | [`en-templates`](skills/en-templates/SKILL.md) |
| Word & ODT | [`de-word-odt`](skills/de-word-odt/SKILL.md) | [`en-word-odt`](skills/en-word-odt/SKILL.md) |
| CAD, BIM & 3D | [`de-cad-bim`](skills/de-cad-bim/SKILL.md) | [`en-cad-bim`](skills/en-cad-bim/SKILL.md) |

### Customer Success

| Skill | DE | EN |
| --- | --- | --- |
| Onboarding Plan · Onboarding-Plan | [`de-onboarding-plan`](skills/de-onboarding-plan/SKILL.md) | [`en-onboarding-plan`](skills/en-onboarding-plan/SKILL.md) |
| QBR Builder · QBR-Builder | [`de-qbr-builder`](skills/de-qbr-builder/SKILL.md) | [`en-qbr-builder`](skills/en-qbr-builder/SKILL.md) |
| Customer Health · Kundengesundheit | [`de-customer-health`](skills/de-customer-health/SKILL.md) | [`en-customer-health`](skills/en-customer-health/SKILL.md) |
| Escalation Brief · Eskalations-Brief | [`de-escalation-brief`](skills/de-escalation-brief/SKILL.md) | [`en-escalation-brief`](skills/en-escalation-brief/SKILL.md) |
| Renewal Prep · Vertragsverlängerung | [`de-renewal-prep`](skills/de-renewal-prep/SKILL.md) | [`en-renewal-prep`](skills/en-renewal-prep/SKILL.md) |
| Success Plan · Success-Plan | [`de-success-plan`](skills/de-success-plan/SKILL.md) | [`en-success-plan`](skills/en-success-plan/SKILL.md) |

### Engineering

| Skill | DE | EN |
| --- | --- | --- |
| Deployment Prep · Deployment-Vorbereitung | [`de-deployment-prep`](skills/de-deployment-prep/SKILL.md) | [`en-deployment-prep`](skills/en-deployment-prep/SKILL.md) |
| Code Review · Code-Review | [`de-code-review`](skills/de-code-review/SKILL.md) | [`en-code-review`](skills/en-code-review/SKILL.md) |
| Standup | [`de-standup`](skills/de-standup/SKILL.md) | [`en-standup`](skills/en-standup/SKILL.md) |
| Tech Debt · Tech-Debt | [`de-tech-debt`](skills/de-tech-debt/SKILL.md) | [`en-tech-debt`](skills/en-tech-debt/SKILL.md) |
| Debugging | [`de-debugging`](skills/de-debugging/SKILL.md) | [`en-debugging`](skills/en-debugging/SKILL.md) |
| Tech Docs · Technische Doku | [`de-tech-docs`](skills/de-tech-docs/SKILL.md) | [`en-tech-docs`](skills/en-tech-docs/SKILL.md) |
| Architecture Design · Architektur-Design | [`de-architecture-design`](skills/de-architecture-design/SKILL.md) | [`en-architecture-design`](skills/en-architecture-design/SKILL.md) |
| Postmortem | [`de-postmortem`](skills/de-postmortem/SKILL.md) | [`en-postmortem`](skills/en-postmortem/SKILL.md) |
| Test Planning · Test-Planung | [`de-test-planning`](skills/de-test-planning/SKILL.md) | [`en-test-planning`](skills/en-test-planning/SKILL.md) |

### Human Resources

| Skill | DE | EN |
| --- | --- | --- |
| Interview Guide · Interview-Leitfaden | [`de-interview-guide`](skills/de-interview-guide/SKILL.md) | [`en-interview-guide`](skills/en-interview-guide/SKILL.md) |
| Performance Review · Leistungsbeurteilung | [`de-performance-review`](skills/de-performance-review/SKILL.md) | [`en-performance-review`](skills/en-performance-review/SKILL.md) |
| Employee Onboarding · Mitarbeiter-Onboarding | [`de-employee-onboarding`](skills/de-employee-onboarding/SKILL.md) | [`en-employee-onboarding`](skills/en-employee-onboarding/SKILL.md) |
| Learning Plan · Lernplan | [`de-learning-plan`](skills/de-learning-plan/SKILL.md) | [`en-learning-plan`](skills/en-learning-plan/SKILL.md) |
| Compensation · Vergütung | [`de-compensation`](skills/de-compensation/SKILL.md) | [`en-compensation`](skills/en-compensation/SKILL.md) |
| Job Description · Stellenbeschreibung | [`de-job-description`](skills/de-job-description/SKILL.md) | [`en-job-description`](skills/en-job-description/SKILL.md) |

### IT Knowledge Management

| Skill | DE | EN |
| --- | --- | --- |
| Change Request | [`de-change-request`](skills/de-change-request/SKILL.md) | [`en-change-request`](skills/en-change-request/SKILL.md) |
| Security Assessment · Security-Assessment | [`de-security-assessment`](skills/de-security-assessment/SKILL.md) | [`en-security-assessment`](skills/en-security-assessment/SKILL.md) |
| Vendor Assessment · Vendor-Assessment | [`de-vendor-assessment`](skills/de-vendor-assessment/SKILL.md) | [`en-vendor-assessment`](skills/en-vendor-assessment/SKILL.md) |
| IT Docs · IT-Doku | [`de-it-docs`](skills/de-it-docs/SKILL.md) | [`en-it-docs`](skills/en-it-docs/SKILL.md) |
| Incident Response | [`de-incident-response`](skills/de-incident-response/SKILL.md) | [`en-incident-response`](skills/en-incident-response/SKILL.md) |
| Knowledge Article | [`de-knowledge-article`](skills/de-knowledge-article/SKILL.md) | [`en-knowledge-article`](skills/en-knowledge-article/SKILL.md) |

### Marketing

| Skill | DE | EN |
| --- | --- | --- |
| Content Draft · Content-Entwurf | [`de-content-draft`](skills/de-content-draft/SKILL.md) | [`en-content-draft`](skills/en-content-draft/SKILL.md) |
| Brand Voice | [`de-brand-voice`](skills/de-brand-voice/SKILL.md) | [`en-brand-voice`](skills/en-brand-voice/SKILL.md) |
| Performance Report · Performance-Report | [`de-performance-report`](skills/de-performance-report/SKILL.md) | [`en-performance-report`](skills/en-performance-report/SKILL.md) |
| Campaign Planning · Kampagnen-Planung | [`de-campaign-planning`](skills/de-campaign-planning/SKILL.md) | [`en-campaign-planning`](skills/en-campaign-planning/SKILL.md) |
| Email Sequence · E-Mail-Sequenz | [`de-email-sequence`](skills/de-email-sequence/SKILL.md) | [`en-email-sequence`](skills/en-email-sequence/SKILL.md) |
| SEO Audit · SEO-Audit | [`de-seo-audit`](skills/de-seo-audit/SKILL.md) | [`en-seo-audit`](skills/en-seo-audit/SKILL.md) |

### Operations

| Skill | DE | EN |
| --- | --- | --- |
| Change Management · Change-Management | [`de-change-management`](skills/de-change-management/SKILL.md) | [`en-change-management`](skills/en-change-management/SKILL.md) |
| Status Report · Statusbericht | [`de-status-report`](skills/de-status-report/SKILL.md) | [`en-status-report`](skills/en-status-report/SKILL.md) |
| Capacity Planning · Kapazitätsplanung | [`de-capacity-planning`](skills/de-capacity-planning/SKILL.md) | [`en-capacity-planning`](skills/en-capacity-planning/SKILL.md) |
| Process Doc · Prozess-Doku | [`de-process-doc`](skills/de-process-doc/SKILL.md) | [`en-process-doc`](skills/en-process-doc/SKILL.md) |
| Process Optimization · Prozessoptimierung | [`de-process-optimization`](skills/de-process-optimization/SKILL.md) | [`en-process-optimization`](skills/en-process-optimization/SKILL.md) |
| Risk Assessment · Risikobewertung | [`de-risk-assessment`](skills/de-risk-assessment/SKILL.md) | [`en-risk-assessment`](skills/en-risk-assessment/SKILL.md) |
| Runbook | [`de-runbook`](skills/de-runbook/SKILL.md) | [`en-runbook`](skills/en-runbook/SKILL.md) |
| Compliance Tracking · Compliance-Tracking | [`de-compliance-tracking`](skills/de-compliance-tracking/SKILL.md) | [`en-compliance-tracking`](skills/en-compliance-tracking/SKILL.md) |

### Product Management

| Skill | DE | EN |
| --- | --- | --- |
| Competitor Brief · Wettbewerber-Briefing | [`de-competitor-brief`](skills/de-competitor-brief/SKILL.md) | [`en-competitor-brief`](skills/en-competitor-brief/SKILL.md) |
| Sprint Planning · Sprint-Planung | [`de-sprint-planning`](skills/de-sprint-planning/SKILL.md) | [`en-sprint-planning`](skills/en-sprint-planning/SKILL.md) |
| Stakeholder Update · Stakeholder-Update | [`de-stakeholder-update`](skills/de-stakeholder-update/SKILL.md) | [`en-stakeholder-update`](skills/en-stakeholder-update/SKILL.md) |
| Research Synthesis · Research-Synthese | [`de-research-synthesis`](skills/de-research-synthesis/SKILL.md) | [`en-research-synthesis`](skills/en-research-synthesis/SKILL.md) |
| Metrics Review · Metriken-Review | [`de-metrics-review`](skills/de-metrics-review/SKILL.md) | [`en-metrics-review`](skills/en-metrics-review/SKILL.md) |
| Product Brainstorm · Produkt-Brainstorming | [`de-product-brainstorm`](skills/de-product-brainstorm/SKILL.md) | [`en-product-brainstorm`](skills/en-product-brainstorm/SKILL.md) |
| Roadmap Update · Roadmap-Update | [`de-roadmap-update`](skills/de-roadmap-update/SKILL.md) | [`en-roadmap-update`](skills/en-roadmap-update/SKILL.md) |
| Product Spec · Produkt-Spec | [`de-product-spec`](skills/de-product-spec/SKILL.md) | [`en-product-spec`](skills/en-product-spec/SKILL.md) |

### Productivity

| Skill | DE | EN |
| --- | --- | --- |
| Meeting Prep · Meeting-Vorbereitung | [`de-meeting-prep`](skills/de-meeting-prep/SKILL.md) | [`en-meeting-prep`](skills/en-meeting-prep/SKILL.md) |
| Weekly Review · Wochenrückblick | [`de-weekly-review`](skills/de-weekly-review/SKILL.md) | [`en-weekly-review`](skills/en-weekly-review/SKILL.md) |
| Memory Management · Memory-Management | [`de-memory-management`](skills/de-memory-management/SKILL.md) | [`en-memory-management`](skills/en-memory-management/SKILL.md) |

### Sales

| Skill | DE | EN |
| --- | --- | --- |
| Deal Strategy · Deal-Strategie | [`de-deal-strategy`](skills/de-deal-strategy/SKILL.md) | [`en-deal-strategy`](skills/en-deal-strategy/SKILL.md) |
| Account Research · Account-Research | [`de-account-research`](skills/de-account-research/SKILL.md) | [`en-account-research`](skills/en-account-research/SKILL.md) |
| Forecast | [`de-forecast`](skills/de-forecast/SKILL.md) | [`en-forecast`](skills/en-forecast/SKILL.md) |
| Battlecard | [`de-battlecard`](skills/de-battlecard/SKILL.md) | [`en-battlecard`](skills/en-battlecard/SKILL.md) |
| Call Prep · Gesprächsvorbereitung | [`de-call-prep`](skills/de-call-prep/SKILL.md) | [`en-call-prep`](skills/en-call-prep/SKILL.md) |
| Pipeline Review · Pipeline-Review | [`de-pipeline-review`](skills/de-pipeline-review/SKILL.md) | [`en-pipeline-review`](skills/en-pipeline-review/SKILL.md) |
| Sales Asset · Sales-Asset | [`de-sales-asset`](skills/de-sales-asset/SKILL.md) | [`en-sales-asset`](skills/en-sales-asset/SKILL.md) |
| Outreach | [`de-outreach`](skills/de-outreach/SKILL.md) | [`en-outreach`](skills/en-outreach/SKILL.md) |
| Call Summary · Gesprächszusammenfassung | [`de-call-summary`](skills/de-call-summary/SKILL.md) | [`en-call-summary`](skills/en-call-summary/SKILL.md) |

## Agents

| Agent | DE | EN |
| --- | --- | --- |
| DemoGPT: all-round agent with the key tools and skills | [`de-demogpt.yaml`](agents/de-demogpt.yaml) | [`en-demogpt.yaml`](agents/en-demogpt.yaml) |
| Researcher · Recherche-Agent: web research subagent of DemoGPT | [`de-researcher.yaml`](agents/de-researcher.yaml) | [`en-researcher.yaml`](agents/en-researcher.yaml) |

## License

See [LICENSE](LICENSE).
