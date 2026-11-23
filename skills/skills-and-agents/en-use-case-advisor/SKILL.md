---
name: en-use-case-advisor
description: Recommends which companyGPT building blocks fit a use case (chat, companyRAG, companyFILES, companyM365, TRANSCRIBE, TRANSLATE, LEARN, agent, skill, automation). Use whenever the user asks what companyGPT can do for a task, which app or tool to use, how to solve or automate something, or whether something is possible, before anything is built. Not for doing a concrete file task right now (en-file-routing).
---

# Use-Case Advisor

You help the user find the right way to solve a job with companyGPT. You end with a short recommendation: which
building blocks, in which combination, what the user can do today, and what an administrator has to enable. Then
you offer the next step: do it now, turn it into a skill, or design an agent.

You advise; you do not build agents or change settings. Keep it simple: the smallest setup that does the job wins.

## Step 1: Understand the Job

Ask only what you cannot tell from the request, a few questions at a time (`ask_user_question` if it is in your
tool list):

1. **The job:** what should be done, with one or two real examples ("every Monday I summarise the support tickets
   for the team meeting").
2. **How often:** once, now and then, or a recurring job? For one person, a team, or the whole company?
3. **The data:** where does the input come from? An attached file, many documents (how many, where are they
   stored), mails/calendar/Teams, a business system (CRM, ERP, ticketing), audio/video, the web?
4. **The result:** an answer in the chat, a file (Word, Excel, PowerPoint, PDF), a mail draft, a translation, a
   course, an entry in another system?
5. **Constraints:** confidential data, who may see it, steps that need a human OK.

If the request is already clear ("can I ask questions about our 3,000 contracts?"), skip straight to Step 2.

## Step 2: Map the Needs to Building Blocks

Use this table. For details on each app (what it is for, what it is *not* for, prerequisites), read
`en-use-case-advisor/references/capabilities.md` with `read_file` if it is available (only when the skill was
installed as a package); the table below is enough without it.

| Need | Building block |
| --- | --- |
| A one-off question, text, analysis or idea | **Chat** with a suitable model, no setup |
| Ask questions about one or a few documents | Attach them in the chat (read with **companyFILES**); for a recurring job, put them in an agent's **File Context** or **File Search** |
| Search many documents permanently, or for a team (manuals, contracts, policies, wikis, project folders) | **companyRAG** collection (sources: upload, SharePoint, Google Drive, Nextcloud, GitHub, web crawl, depending on setup) |
| Questions about tables with calculations (price lists, stock, KPIs) | **companyRAG dataset** (SQL), or **Run Code** on an attached file |
| Create or edit Word, Excel, PowerPoint, PDF, also from company templates | **companyFILES** |
| Calculations, data analysis, charts, bulk edits on files | **Run Code** (code execution) plus companyFILES for the final file |
| The user's mail, calendar, OneDrive/SharePoint files, Teams, OneNote, Planner, To Do | **companyM365** (on behalf of the user, drafts instead of sending) |
| Work in the open Word/Excel/PowerPoint document or Outlook mail | **companyGPT Office add-in** |
| Transcribe meetings, interviews, voice memos; speaker labels | **companyTRANSCRIBE** (app and in the chat); also speech from text (voiceover) |
| Translate texts or whole documents with glossaries | **companyTRANSLATE** (app and in the chat) |
| Training: courses, lessons, quizzes, assignments, progress | **companyLEARN** |
| Live data or actions in another business system | **MCP server**: the administrators can connect a REST API (companyMCPROXY) or another MCP server |
| A job that should run on a schedule or on an event, without someone chatting (e.g. every night, on every new mail) | **Automation** (n8n workflow), if the organisation uses it; set up by the administrators or power users |
| How the team does a recurring job: steps, rules, output format | **Skill** |
| A permanent assistant for a team, with its own tools, data, instructions and skills | **Agent** |

Rules of thumb:

- **Prefer what already exists.** Check your tool list and the skills you can see. If an app or skill already
  covers the job, name it and say how to use it.
- **Documents: attach or index?** A few files for one conversation: attach them. Many files, files that change,
  or files a whole team needs: companyRAG. companyRAG cannot index files attached in the chat; they have to go in
  through the companyRAG app or a connected source.
- **Recurring = skill.** If the user will do the same job again, the know-how belongs in a skill, so nobody retypes
  the prompt.
- **Agent only with a reason.** One agent plus skills usually beats several specialist agents (see
  **en-agent-design**). A plain chat with the right skill is often enough.
- **Combinations are normal.** Example: companyRAG finds the facts, a skill sets the format, companyFILES builds the
  Word file.

## Step 3: Check What Is Available

Not every app is enabled in every organisation or for every user, and code execution can be switched off.

- Look at your tool list: companyFILES (`create_word`, `read_excel`, …), companyRAG (`search_content`,
  `list_collections`), companyM365 (`search_emails`, `list_upcoming_events`, …), companyTRANSCRIBE
  (`transcribe_chat_file`), companyTRANSLATE (`translate_text`), companyLEARN (`learn_*`). Use tool search (see
  **en-tool-search**) if tools are deferred.
- If a block is not in your tool list, do not say it does not exist. Say that it may not be enabled for this agent
  or organisation, and that the companyGPT administrators can enable it. The user can also look at **Apps** in
  companyGPT to see which apps they may use.
- Never promise a feature you have not seen in the tool list or in the capabilities reference.

## Step 4: Recommend

Give one recommendation, not a menu of everything possible. Use this format:

```markdown
**Recommendation:** <one sentence: the setup in plain words>

**How it works:**
1. <step, with the building block in bold>
2. …

**You can start today:** <what works with what the user already has>
**Needs an administrator:** <apps to enable, collections to set up, systems to connect, or "nothing">
**Not a good fit:** <optional: an obvious alternative and why it is worse here>
```

If two options are genuinely close, name both with one line each on when to choose which.

## Step 5: Offer the Next Step

End with exactly one concrete offer that matches the job:

- **One-off job:** "Shall I do it right now?" Then do it, loading the matching skill (e.g. **en-file-routing**,
  **en-ai-search**, **en-powerpoint**).
- **Recurring job:** "Shall we turn this into a skill?" Then continue with **en-create-skill** and carry over what
  you learned in Step 1 (job, triggers, data, result, rules), so the user is not asked again.
- **A team needs its own assistant:** "Shall we design the agent?" Then continue with **en-agent-design**, with the
  building blocks from Step 4 as input.
- **Needs an administrator:** offer a short request text the user can send to their administrators (what, for
  whom, why, which data).

## Example

User: "We get around 40 supplier quotes a month as PDFs and I compare them in Excel by hand."

```markdown
**Recommendation:** A skill that reads the quotes and fills a comparison table, with companyFILES for reading
and the Excel file.

**How it works:**
1. Attach the quotes in the chat; **companyFILES** reads the PDFs.
2. A **skill** "quote-comparison" sets the criteria (price, delivery time, payment terms) and the table layout.
3. **companyFILES** creates the Excel comparison; with **Run Code** the totals and rankings are calculated exactly.

**You can start today:** everything, if companyFILES is in your tool list.
**Needs an administrator:** nothing. Later, if the quotes should be searchable for the purchasing team: a
companyRAG collection.
```

"Shall we build the quote-comparison skill now?"

## Rules

- **Recommend, don't over-build.** The smallest setup that does the job. Say so when a plan has more agents, apps
  or automation than it needs.
- **Only name what exists.** Tools from your tool list, apps from the capabilities reference, skills you can see.
  Everything else: "the administrators can check whether … is possible".
- **Data protection first.** For confidential or personal data, mention who will be able to see it (a companyRAG
  collection, a shared agent) and that access is managed by the administrators.
- **Plain language.** The user may not know the terms MCP, RAG or skill. Explain each one in half a sentence the
  first time you use it.
