---
title: AI-Search Skill
description: Starter-Skill für den Wissensabruf aus companyRAG-Collections über den ai-search MCP-Server.
label: AI Search
---

Verwende diesen Skill, wenn ein Agent Fragen ausschließlich auf Basis deiner companyRAG-Collection beantworten soll. Er enthält das Minimum: die drei Such-Tools und `list_collections` des companyRAG-MCP-Servers (in den meisten Umgebungen **ai-search** genannt), ihre Eingaben, das Ergebnisformat und die wichtigsten Regeln.

:::note
Ersetze `<deine-collection>` durch den exakten (technischen) Namen deiner companyRAG-Collection. Der Agent kann ihn mit `list_collections` nachschlagen (ab companyRAG 2.39). Der MCP-Server heißt standardmäßig **ai-search**; in manchen Umgebungen gibt es zusätzlich eigene Server pro Collection (z. B. `wiki` oder `Normensuche`), die fest auf eine Collection eingestellt sind. Dort wird der Parameter `collection` ignoriert. Der Skill ist als Startpunkt gedacht: Erweitere ihn bei Bedarf um Antwortformat, Zitierregeln oder eine Retry-Strategie.
:::
