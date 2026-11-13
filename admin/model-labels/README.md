# Model labels

Curated display names and short descriptions for the chat models companyGPT offers, so users see
"Claude Sonnet 5.5 – Programming, complex text …" instead of a bare model id like `claude-sonnet-5-5`.

| File | Language |
| --- | --- |
| [`de.yaml`](de.yaml) | German labels and descriptions |
| [`en.yaml`](en.yaml) | English labels and descriptions |

companyGPT shows one label per model, not one per user language, so pick the file that matches your users. Both
files list the same models in the same order; only `label` and `description` differ.

## Format

LibreChat has no per-model display name. Labels are `modelSpecs` entries: a labelled preset per model.

```yaml
modelSpecs:
  prioritize: true        # labels are the default picker for new chats
  enforce: false          # true = users can ONLY pick labelled models (and agents need their own label)
  list:
  - name: claude-sonnet-5-5           # stable key, stored in conversations: never change it
    label: Claude Sonnet 5.5          # what the model picker shows
    description: Programming, complex text and demanding all-round tasks
    order: 12                         # position in the picker
    group: Anthropic                  # submenu in the picker
    groupIcon: anthropic              # icon of that submenu (first entry of a group)
    preset:
      endpoint: anthropic             # LibreChat endpoint that serves the model
      model: claude-sonnet-5-5        # model id at that endpoint
```

`default: true` preselects a model for new chats (here `gpt-6-luna`). GPT models carry `useResponsesApi: true`:
behind the AI gateway, reasoning only stays on during tool calls with the Responses API.

## Applying the labels

1. Copy the file for your language and **keep only the models your tenant has**. A label for a model that does not
   exist shows up in the picker and fails when used.
2. Check `preset.endpoint` against your `librechat.yaml`: `openAI` (GPT), `anthropic` (Claude) and `Google`
   (custom endpoint for Gemini) are the usual names, but tenants differ.
3. Apply it in one of two ways:
   - **companyADMIN → Model labels** (`/config/labels`): enter label, description, group, endpoint and model per
     row. companyADMIN stores them as a database override; `librechat.yaml` stays untouched.
   - **`librechat.yaml`** (companyGPT Terraform, `env/<tenant>/librechat.yaml`): paste the `modelSpecs` block.
     Also set `addedEndpoints` to the endpoints that should stay in the picker next to the labels (usually
     `agents` and `AI-Gateway`). A non-empty `addedEndpoints` is the picker's allow-list: endpoints missing from it
     are hidden.

Users see the models their role allows; labels for models they may not use are dropped automatically.

## Maintaining the list

- The descriptions follow the model overview in the docs (`/de/company-gpt/modellauswahl`,
  `/en/company-gpt/modellauswahl`). Update both when a model is added or retired.
- Never change a `name` that is already released: conversations store it.
- `npm run validate` checks that both files are valid and list the same models.
