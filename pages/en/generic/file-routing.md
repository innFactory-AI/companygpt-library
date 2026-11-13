---
title: File Routing Skill
description: Route file tasks to the right tool — companyFILES, code execution, companyRAG, companyTRANSCRIBE, companyTRANSLATE or companyM365 — with a fallback for each.
label: File Routing
---

Use this skill when users attach files or want files as output and the agent has several apps to choose from. It
teaches the agent to take the `file_id` from the "Attached files" block, to pick the right tool for each task
(native Office output, calculations on a spreadsheet, templates, e-mails and archives, transcription, translation,
company knowledge), and to fall back cleanly when an app or code execution is not available.

:::note
Apps and code execution differ per tenant and role. The skill only names a route as an option; the agent checks its
own tool list before using it.
:::
