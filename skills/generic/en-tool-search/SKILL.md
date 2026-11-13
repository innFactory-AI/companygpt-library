---
name: en-tool-search
description: Always use this skill whenever you need to find, select, and execute a tool for a specific task but do not yet know its exact name or input schema.
---

# Tool Search Skill

Finds the right tool via tool search, selects it based on name and schema, and then executes it with the correct parameters.

## Step 1: Discover Available Tools

Call the `search_tools` (or `tool_search`) utility first to find out which tools exist.

- **The query rule:** The `query` parameter MUST be a generic, functional keyword describing *what* you want to achieve (e.g. `"search"`, `"files"`, `"excel"`, `"database"`, `"sql"`, `"image"`).
- **CRITICAL – Do NOT use the user's content search query.** Do not search for `"machine learning"` or `"maschinelles Lernen"`.
- **CRITICAL – Do NOT pass tool-specific arguments** (such as `collection`, `topK`, `searchMode`, `mcp_server`) to the tool discovery utility. Only use the arguments defined in the discovery tool's schema.

Example call:

```json
{
  "query": "search"
}
```

## Step 2: Analyse and Select the Correct Tool

Review the list of tools returned by your discovery search.

1. **Identify the exact name:** Look at the `name` field of the matched tool. You must use the full, exact name (e.g. `search_content_mcp_ai-search`, NEVER truncate it to `search_content`).
2. **Locate the schema:** Read the tool's description and parameter definitions to understand which parameters it expects.

## Step 3: Execute the Target Tool

Invoke the selected tool.

- Only in this step do you apply the user's actual search query, filters, and operational parameters (e.g. `collection: "ai_rag_ml"`, `searchMode`, `query`).
- Match the input schema of the target tool precisely. Do not carry over any parameters from the discovery step.

## Core Rules

| Rule | Meaning |
| --- | --- |
| **Strict parameter separation** | Never mix discovery parameters (the discovery query) with operational parameters (`collection`, `topK`, …). |
| **Query distinction** | A functional tool keyword (e.g. `"search"`) is not the user's content query (e.g. `"machine learning"`). |
| **Exact name matching** | Copy the full tool name character by character to prevent "tool not found" errors. |
