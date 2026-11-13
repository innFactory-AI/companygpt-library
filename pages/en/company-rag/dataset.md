---
title: Dataset Skill
description: Starter skill for analysing companyRAG datasets with DuckDB SQL.
label: Dataset
---

Use this skill when an agent should analyse tables (CSV, TSV, Excel, Parquet) or live datasets from companyRAG. It contains the minimum: the dataset tools of the companyRAG MCP server (called **ai-search** in most environments), their inputs, and the path from schema exploration to SQL query.

:::note
The skill is meant as a starting point: extend it with your collection names, domain metrics, or a fixed output format as needed. The dataset tools are only available when the server's SQL engine (DuckDB) is active. If they are missing from the tool list, the agent can only use the search tools.
:::
