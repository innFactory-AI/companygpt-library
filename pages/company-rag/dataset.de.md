---
title: Dataset Skill
description: Starter-Skill für die Analyse von companyRAG-Datasets per DuckDB-SQL.
label: Dataset
---

Verwende diesen Skill, wenn ein Agent Tabellen (CSV, TSV, Excel, Parquet) oder Live-Datasets aus companyRAG auswerten soll. Er enthält das Minimum: die Dataset-Tools des companyRAG-MCP-Servers (in den meisten Umgebungen **ai-search** genannt), ihre Eingaben und den Ablauf von der Schema-Erkundung bis zur SQL-Abfrage.

:::note
Der Skill ist als Startpunkt gedacht: Erweitere ihn bei Bedarf um deine Collection-Namen, fachliche Kennzahlen oder ein festes Ausgabeformat. Die Dataset-Tools stehen nur zur Verfügung, wenn die SQL-Engine (DuckDB) des Servers aktiv ist. Fehlen sie in der Tool-Liste, kann der Agent nur die Such-Tools nutzen.
:::
