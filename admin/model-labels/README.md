# Model labels

Curated display names and short descriptions for every chat model deployed in companyGPT, so users see
"Claude Sonnet 5.5 – Programming, writing and demanding everyday work" instead of a bare model id like
`claude-sonnet-5-5`.

Everything lives in one file, [`labels.yaml`](labels.yaml) (format v2): structure (groups, order, menu
recommendation, successors, aliases, endpoint preference) once, and label and description per language. It replaces
the former `de.yaml` / `en.yaml`.

## Format v2

```yaml
version: 2                          # required; other values are rejected
locales: [de, en]                   # every label/description must carry each listed locale
groups:                             # order = order of first appearance for new labels
  - id: openai                      # referenced by models[].group
    label: OpenAI                   # string, or { de: …, en: … }
    icon: openAI                    # provider name (LibreChat built-in icon) or https:// URL; optional
models:
  - model: gpt-6.1-sol              # canonical model id; unique across model ids and aliases
    group: openai
    menu: featured                  # featured | available; default available
    supersededBy: []                # model ids from this file; acyclic
    aliases: [gpt-61-sol]           # other deployment ids that mean this model; optional
    endpoints: [openAI, azureOpenAI]   # endpoint preference when offered on several; optional
    label: { de: GPT-6.1 Sol, en: GPT-6.1 Sol }
    description: { de: "Stärkstes GPT: …", en: "Strongest GPT: …" }
```

| Field | Required | Meaning |
| --- | --- | --- |
| `version` | yes | Always `2`. |
| `locales` | yes | Languages of the file. Every `label` and `description` map carries exactly these keys. |
| `groups[].id` | yes | Key that `models[].group` refers to; unique. |
| `groups[].label` | yes | Submenu name in the model picker: one string for all languages, or a map per locale. |
| `groups[].icon` | no | Icon of the submenu, see [Group icons](#group-icons). |
| `models[].model` | yes | Canonical model id as companyGPT knows it. Unique across all model ids **and** aliases. |
| `models[].group` | yes | `id` of a group in this file. |
| `models[].menu` | no | `featured` or `available` (default), see [Menu recommendation](#menu-recommendation). |
| `models[].supersededBy` | no | Model ids from this file that replace this model, see [Successors](#successors). |
| `models[].aliases` | no | Other deployment ids that mean the same model, see [Aliases](#aliases). |
| `models[].endpoints` | no | Endpoint preference, see [Endpoint preference](#endpoint-preference). |
| `models[].label` | yes | Map per locale: what the model picker shows. 1–128 characters, no control characters. |
| `models[].description` | no | Map per locale: one line for the user, at most 120 characters. |

Unknown keys are rejected everywhere, so a typo fails validation instead of being ignored. The order of `groups`
is the order of the submenus; the order of `models` is the order inside a submenu.

The descriptions are written from the user's point of view: what a model is good for, so people can choose
without knowing the model family. Where the provider publishes a short description, it is the basis.

### Menu recommendation

`menu` says whether a model should be offered prominently in the picker:

- `featured`: the newest generation of each model family (e.g. GPT-6.1 Sol, Claude Opus 5.5, Gemini 3.8 Flash)
  and the `auto*` router entries.
- `available` (default): older generations and everything else. They still work and keep their label; they are
  just not recommended for the menu.

When a new generation arrives, set it to `featured` and the model it replaces to `available` with `supersededBy`.

### Successors

`supersededBy` lists the model(s) that replace an older one, normally the current `featured` model of the same
family and tier (GPT-5.6 Sol → GPT-6.1 Sol, Claude Opus 4.8 → Claude Opus 5.5, Gemini 3.1 Pro (Preview) → Gemini 4
Argon). Older GPT-5.x/4.x models point to the GPT-6 tier that fits their role: full and Codex models to Sol,
chat-style and non-reasoning all-rounders to Terra, mini/nano and o3-mini to Luna. Entries must be model ids of this
file (not aliases), and following them may never lead back to the same model. Models without a newer model of the
same family in the file have no `supersededBy`.

### Aliases

Some providers deploy the same model under another id, e.g. Bedrock's `anthropic.claude-opus-4-8` for
`claude-opus-4-8`. Such ids go into `aliases` of the canonical entry instead of a second, identical entry, so the
label and description exist once. An id can only be either a model id or an alias of one model.

### Endpoint preference

Where one model is offered on several endpoints in an environment (e.g. `openAI` and `azureOpenAI`), `endpoints`
lists them in order of preference, so the label sync knows which one to show. Leave it out when the model is only
offered on one endpoint or there is no preference; none of today's entries sets it.

## Applying the labels

Tenants apply the labels through the **companyADMIN label sync**, which reads `admin/model-labels/labels.yaml` from
this repo. It adds labels only for models the environment actually has, in the users' language, and uses `menu`,
`supersededBy`, `aliases` and `endpoints` as described above. Users only see the labels of models their role
allows.

Copying by hand in **companyADMIN → Configuration → Labels** (`/config/labels`) is only the fallback, e.g. where the
label sync is not available yet:

1. The page lists the models of the environment that have no label yet. Look up the model in `labels.yaml` (as
   `model` or under `aliases`) and copy the **label** and **description** of your users' language, plus the
   group's **label** and **icon**.
2. Only add labels for models the environment actually has. The file covers every model deployed anywhere in the
   fleet, so most environments use only part of it.
3. For GPT models on the `openAI` / `azureOpenAI` endpoint, keep the **Responses API** switch as it is in the
   environment (it is on where the GPT models run through the AI gateway).

### Group icons

Each group has one icon (`groups[].icon`). Keep them as below; they are what the tenants already use.

| Group | `icon` | |
| --- | --- | --- |
| Auto, OpenAI | `openAI` | LibreChat's built-in OpenAI icon (as on groku/schoenklinik, where Auto sits in the OpenAI group) |
| Anthropic | `anthropic` | built-in |
| Google | `google` | built-in |
| Mistral | `mistral` | built-in |
| Perplexity | `perplexity` | built-in |
| STACKIT | `https://storage.googleapis.com/compangygpt-public-data/misc/stackit-icon.svg` | no built-in icon; the icon the tenants' STACKIT endpoint already uses |

A provider name (any case, also aliases like `claude`, `gemini`) becomes LibreChat's built-in icon; anything else is
loaded as an image URL. The bucket `compangygpt-public-data/misc/` also has `google-icon.svg` and
`perplexity-icon.svg` if a tenant prefers the endpoint icons.

## What is not in the list

- Models that are not chat models: image generation (`gpt-image-*`), speech (`whisper`, `tts`,
  `gpt-realtime-*`), OCR (`mistral-document-ai-*`), embeddings (`text-embedding-*`) and the gateway's routing
  model `Microsoft-Decision-1`. They never appear in the model picker.
- `auto-pro` and `auto-dev` are router flows set up per environment in the AI gateway; their descriptions are
  generic. Adjust them if a tenant's flow does something else.

## Maintaining the list

- When a model is deployed for the first time (`companyGPT/env/<tenant>/config.tfvars` or `librechat.yaml`), add
  it to `labels.yaml` in the same PR, with label and description in every locale. Retired models can stay until no
  environment has them any more.
- A new generation: mark it `featured`, set the older model to `available` and point its `supersededBy` at it.
- Descriptions: one line, at most 120 characters, no prices or cost hints. Labels: at most 128 characters.
- `npm run validate` checks the file: `version` 2, unique model ids and aliases, known groups, known and acyclic
  successors, every locale text present, label and description limits, no unknown keys. `npm test` runs the
  validator's self-test.

## Sources

The descriptions are based on the providers' own model descriptions where they exist (as of 2026-11-16):

- OpenAI: [model pages](https://developers.openai.com/api/docs/models); model router:
  [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-router)
- Anthropic: [models overview](https://platform.claude.com/docs/en/models/overview) and the launch posts on
  [anthropic.com/news](https://www.anthropic.com/news)
- Google: [Vertex AI models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models),
  [AI Studio models](https://aistudio.google.com/docs/models)
- Mistral: [docs.mistral.ai/models](https://docs.mistral.ai/models/mistral-large-3-25-12)
- STACKIT: [available shared models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models)
  and the model cards on Hugging Face
- Perplexity: [Sonar models](https://docs.perplexity.ai/docs/sonar/models.md)
- `auto*`: the AI gateway's auto router (`innFactory/ai-gateway`, `docs/auto-router.md`)
