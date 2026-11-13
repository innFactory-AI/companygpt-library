---
title: AI Search Skill
description: Starter skill for knowledge retrieval from companyRAG collections via the ai-search MCP server.
label: AI Search
---

Use this skill when an agent should answer questions exclusively from your companyRAG collection. It contains the minimum: the three search tools and `list_collections` of the companyRAG MCP server (called **ai-search** in most environments), their inputs, the result format, and the core rules.

:::note
Replace `<your-collection>` with the exact (technical) name of your companyRAG collection. The agent can look it up with `list_collections` (companyRAG 2.39 or later). The MCP server is called **ai-search** by default; some environments also have dedicated servers per collection (e.g. `wiki` or `Normensuche`) that are pinned to one collection. On those, the `collection` parameter is ignored. The skill is meant as a starting point: extend it with a response format, citation rules, or a retry strategy as needed.
:::
