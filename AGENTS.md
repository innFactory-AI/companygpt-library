# companygpt-library: agent instructions

This repo is the **single source** for the ready-made companyGPT content that customers can take: agent skills,
agents and admin defaults (model labels). The docs site ([innFactory-AI/docs](https://github.com/innFactory-AI/docs),
docs.company-gpt.com → Tutorials → Skills) does not keep its own copy: its build runs `scripts/sync-skills.mjs`,
which reads this repo (branch `main`) and generates every skill page, the skills index and the sidebar. Never edit
the generated skill pages in the docs repo; they are gitignored there (only the intros above each skill are
kept there). Customers also connect this repo directly in companyADMIN
Library Sync.

It replaces `innFactory-AI/company-ai-stack-skills` (archived), where DE and EN skills had the same name and could
not be installed side by side.

## Layout

```text
catalog.json                                  # skill categories, order (by <id>), index texts (DE/EN)
skills/<category>/<locale>-<id>/SKILL.md      # the skill: what users upload in companyGPT under "Skills"
skills/<category>/<locale>-<id>/references/…  # optional bundled files (Markdown recipes; optionally scripts/…)
agents/<locale>-<slug>.md                     # ready-made companyGPT agents (agent markdown)
admin/model-labels/labels.yaml                # curated model labels (format v2) for companyADMIN, README.md explains them
scripts/validate.mjs                          # `npm run validate`, runs in CI (label file v2: scripts/model-labels.mjs,
                                              # self-test `npm test`)
```

- `<locale>` is `de` or `en`. **The locale is part of every name**, so both languages can live in one companyGPT:
  skill `de-excel` / `en-excel`, agent id `agent_de_companygpt` / `agent_en_companygpt`. Every skill exists in both
  locales with the same `<id>`, in the same `<category>` folder.
- `<category>` groups skills by domain (`files`, `sales`, …). Library Sync finds skills at any depth, so the category
  is not part of the name; moving a skill to another category keeps its identity (the docs URL changes, though).
- `<id>`: English kebab-case, no `-skill` suffix. `catalog.json` lists skills by `<id>`, and the docs URL is
  `/<locale>/tutorials/skills/<category>/<id>`. Don't rename an `<id>` once it is live: the skill name is the
  identity in Library Sync (a rename deletes and re-creates the skill in every tenant, agents lose the reference),
  and links point at the URL.
- **Package = the skill folder.** Put nothing docs-only into it: companyADMIN Library Sync imports every file in a
  folder that has a `SKILL.md`, so docs-only content stays out of it (the page intros live in the docs repo, see
  below). Everything in the folder
  (`SKILL.md`, `references/`, `scripts/`, …) is part of the skill package: the docs offer it as a zip
  (`<name>/SKILL.md` plus bundled files) that companyGPT imports under Skills (`.zip`/`.skill`). The agent reads
  bundled files with the built-in `read_file` tool (`<name>/references/x.md`, works without code execution); with
  code execution they are also copied read-only to `/mnt/data/skills/<name>/…` in the sandbox. A skill pasted or
  uploaded as a single `SKILL.md` has no bundled files.
- `catalog.json` lists every category (`id` = folder under `skills/`, docs URL segment, `label.de`/
  `label.en` = sidebar group and index heading) and its skills in display order, plus the title, description and
  intro of the skills index page. A skill folder that is not in `catalog.json` fails validation, and so does a
  catalog entry without its skill in both locales.

### SKILL.md

```markdown
---
name: en-excel
description: One or two sentences; LibreChat uses it to decide when to load the skill.
---

# Excel Skill
…
```

- `name`: `<locale>-<id>`, identical to the folder name. LibreChat allows `^[a-z0-9][a-z0-9-]*$`, max. 64
  characters.
- `description`: max. 1024 characters, in the skill's language. It decides when the skill is activated, so say what
  the skill does *and* when to use it.
- Body max. 100,000 characters. The docs wrap it in a fence that is longer than any backtick run inside, so inner
  ```` ``` ```` blocks are fine.
- Cross-references to other skills (`**de-powerpoint**`, `de-templates/references/…`) use the same locale prefix.

### Docs pages

The docs page of a skill is the `SKILL.md` plus a short docs-only intro (title, description, sidebar label, intro
text, notes such as placeholders to replace). The intros live in the docs repo, `src/skill-pages/<category>/<id>.<locale>.md`
in innFactory-AI/docs (see its `AGENTS.md`). A new skill works without one: the page then takes its title and label
from the `SKILL.md` heading and its description from the first sentence of `description`. Add the intro with a docs PR
on a branch with the same name; this repo's CI builds the docs against it.

### agents/<locale>-<slug>.md

companyGPT agents as agent markdown (Library Sync, companyADMIN 3.20.0 or later): the frontmatter holds every agent
setting a companyGPT export has (`id`, `name`, `description`, `provider`, `model`, `tools`, `mcpServerNames`, `skills`,
`subagents`, …), the body is the `instructions`. The `id` in the frontmatter is what makes the file an agent (a `.md`
without one is read as a plain Claude Code subagent). It is the identity in Library Sync and must be
`agent_<locale>_<slug>` with the file's slug (`-` → `_`); never change it once released. No `avatar`: an uploaded
avatar path only exists in the tenant it came from. Write the instructions so any customer can use them unchanged:
no tenant, customer or person names, and tools named with "if available" where a tenant may not have them. DE and EN
files share the same tools, MCP servers and settings; only `name`, `description`, the body and the locale of
`skills:` / `subagents.agent_ids` differ. Every
name under `skills:` must be a skill of the same locale in this repo, and every subagent id an agent of the same
locale.

### admin/

Admin defaults for companyADMIN, each folder with a `README.md`. `admin/model-labels/labels.yaml` (label file v2)
holds a label and user-facing description per locale, the group, the menu recommendation, successors and aliases for
every chat model deployed anywhere in the fleet. Tenants apply it through the companyADMIN label sync (hand copying in
companyADMIN → Configuration → Labels is only the fallback). Keep the file path stable: tenants use it as their label
source. A newly deployed chat model gets its entry in the same rollout; the README describes the format.
**Format changes:** the tenants' companyADMIN rejects unknown keys in the label file (the whole file, not just the
entry). Use a new key here only after a companyADMIN version that knows it runs fleet-wide; otherwise bump `version`,
and companyADMIN must support the new version first.

## Writing rules

- **Language:** DE files are German (du-form), EN files English. Keep the `<id>` part of `name:`, tool/parameter names, product
  names (companyFILES, companyRAG, MCP, …) and format keywords (PDF, DOCX, XLSX) unchanged. DE and EN must say the
  same thing; change both in one PR.
- **Prompt-first, code optional:** every `SKILL.md` must work as plain instructions without code execution. Code
  execution (sandbox without network; Python/Node/Bash) is on in most tenants, but not everywhere: the tenant, the
  role permission `RUN_CODE` or the user can switch it off. Point to companyFILES for file output (DOCX/XLSX/PPTX/PDF)
  and to companyRAG collections / MCP servers / file upload for data.
  - Code steps go into an optional section that starts with "If code execution is available …" (DE: "Wenn
    Code-Ausführung verfügbar ist …") and always names the fallback without code (usually a companyFILES tool).
  - Check Python packages with `import` before relying on them, and fall back if one is missing.
  - Longer recipes or scripts go into bundled files next to `SKILL.md` (`references/<topic>.md`, optionally
    `scripts/…`), in both locales. Reference them from `SKILL.md` (`<name>/references/x.md`, with the skill's own locale prefix) with a note that they only exist when the skill was
    installed as a package (zip / sync), not when only `SKILL.md` was pasted. `SKILL.md` must still be complete
    without them.
- **Tools must be real.** Every tool name, parameter, enum and limit in a skill must exist in the current release of
  the app that provides it. Check the source before changing a skill:
  - companyFILES: `src/mcp/server.ts`, `cad-tools.ts`, `docs-tools.ts`, `ui-tools.ts`, `template-handoff-tools.ts` (repo `innFactory/companyFILES`;
    it also keeps reviewed templates in `.skills/*/SKILL.md`). Some tools only exist when an extension is configured
    (CAD tools, `read_file`/`convert_to_markdown`, Azure-Maps map options); say "if available" for those.
  - companyRAG: `apps/mcp/internal/handlers/` (repo `innFactory/companyRAG`). The MCP server is usually called
    `ai-search`; dataset tools only exist when DuckDB is enabled.
  - companyM365, companyTRANSCRIBE, companyTRANSLATE, companyLEARN: their MCP tool definitions. Only name an app in
    a skill's "Where the data comes from" section if the tool really exists.
- When an app release adds, renames or removes tools, update the affected skills here in the same rollout.

## Workflow

1. Branch, edit the skill in both locales, update `catalog.json` and the README table for new skills (intro for the
   docs page: docs repo, see "Docs pages").
2. `npm ci && npm run validate`.
3. Preview locally with a docs checkout next to this repo:
   `cd ../docs && SKILLS_DIR=../companygpt-library npm run dev` (or `npm run build`).
4. Open a PR. CI (`.github/workflows/ci.yml`) validates and builds the docs site against your branch (and against a
   docs branch with the same name, if one exists).
5. After merge to `main`, CI sends a `repository_dispatch` (`skills-updated`) to innFactory-AI/docs, which rebuilds
   and deploys the site. That step needs the repo secret `DOCS_DISPATCH_TOKEN` (fine-grained token for
   innFactory-AI/docs with "Contents: read and write").

Conventional commits, feature branches and PRs; never push to `main`.
