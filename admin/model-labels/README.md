# Model labels

Curated display names and short descriptions for every chat model deployed in companyGPT, so users see
"Claude Sonnet 5.5 – Programming, writing and demanding everyday work" instead of a bare model id like
`claude-sonnet-5-5`.

| File | Language |
| --- | --- |
| [`de.yaml`](de.yaml) | German labels and descriptions |
| [`en.yaml`](en.yaml) | English labels and descriptions |

companyGPT shows one label per model, not one per user language, so pick the file that matches your users. Both
files list the same models in the same order; only `label` and `description` are translated.

## Format

```yaml
labels:
  - model: claude-sonnet-5-5          # model id as companyGPT knows it
    label: Claude Sonnet 5.5          # what the model picker shows
    group: Anthropic                  # submenu in the picker
    description: Programming, writing and demanding everyday work
```

The descriptions are written from the user's point of view: what a model is good for, so people can choose
without knowing the model family. Where the provider publishes a short description, it is the basis.

## Applying the labels

Labels are maintained by hand in **companyADMIN → Configuration → Labels** (`/config/labels`):

1. The page lists the models of the environment that have no label yet. For each one, look up its `model` in the
   file for your language and copy **label**, **description** and **group**.
2. Only add labels for models the environment actually has. The files cover every model deployed anywhere in the
   fleet, so most environments use only part of them.
3. For GPT models on the `openAI` / `azureOpenAI` endpoint, keep the **Responses API** switch as it is in the
   environment (it is on where the GPT models run through the AI gateway).

Users only see the labels of models their role allows.

## What is not in the list

- Models that are not chat models: image generation (`gpt-image-*`), speech (`whisper`, `tts`,
  `gpt-realtime-*`), OCR (`mistral-document-ai-*`), embeddings (`text-embedding-*`) and the gateway's routing
  model `Microsoft-Decision-1`. They never appear in the model picker.
- `auto-pro` and `auto-dev` are router flows set up per environment in the AI gateway; their descriptions are
  generic. Adjust them if a tenant's flow does something else.

## Maintaining the list

- When a model is deployed for the first time (`companyGPT/env/<tenant>/config.tfvars` or `librechat.yaml`), add
  it to both files in the same PR. Retired models can stay until no environment has them any more.
- Keep `de.yaml` and `en.yaml` in the same order with the same `model` and `group`; `npm run validate` checks it.
- Descriptions: one line, at most 120 characters, no prices or cost hints.

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
