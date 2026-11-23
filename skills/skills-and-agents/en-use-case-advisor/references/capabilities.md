# companyGPT Capabilities

What each building block is for, what it is not for, and what has to be in place. An app is only usable if it is
enabled for the organisation and the user; its tools then appear in the agent's tool list.

Contents: Chat and agent features · companyRAG · companyFILES · companyM365 · Office add-in · companyTRANSCRIBE ·
companyTRANSLATE · companyLEARN · Connected systems (MCP) · Automation (n8n) · Skills and agents

## Chat and Agent Features

Built into companyGPT, no app needed.

- **Chat:** questions, texts, summaries, ideas, analysis of attached files. Choose a model to fit: stronger models
  for analysis and long documents, faster ones for simple tasks.
- **File upload:** attach files in the chat for this conversation. Not permanent and not searchable for others.
- **File Context / File Search (in an agent):** a few key documents the agent always sees (File Context, costs
  context in every message), or a small document set it searches as needed (File Search). For many or changing
  documents, use companyRAG.
- **Run Code (code execution):** Python in a sandbox without network access, for calculations, data analysis,
  charts and bulk file edits. Not enabled everywhere (organisation, role or user can switch it off).
- **Web search, memory, artifacts, `ask_user_question`:** depending on the agent and the organisation's setup.

## companyRAG

Company knowledge search over document collections, and SQL over tables.

- **For:** many documents that a team searches again and again: manuals, policies, contracts, wikis, project
  folders, product documentation. Answers come with sources.
- **Sources:** upload in the companyRAG app, SharePoint, Google Drive, Nextcloud, GitHub, web crawl (which ones
  depends on the setup). Collections are kept in sync with their source.
- **Datasets:** tables (CSV/Excel) queried with SQL, e.g. price lists, stock levels, KPIs. Only where datasets are
  enabled.
- **Access:** each collection has its own access; the user only searches collections they may use
  (`list_collections` shows them).
- **Not for:** a file attached in the chat (companyRAG cannot index chat attachments), one-off questions on a few
  documents (just attach them), live data from business systems (MCP server).
- **Tools:** `list_collections`, `search_content`; datasets: `execute_sql` and further dataset tools.
- **Skills:** **en-ai-search**, **en-dataset**.
- **Prerequisite:** a collection with the right documents, set up in the companyRAG app by users with the right
  permission or by the administrators.

## companyFILES

Creates and reads Office documents. Created files come back as normal chat files.

- **For:** Word, Excel, PowerPoint, PDF (and ODT) from scratch or from company templates, filling PDF forms,
  converting formats, charts and diagrams, reading attached documents, editing existing files.
- **Templates:** company templates (letterhead, slide master, report layout) are filled with `list_templates` and
  `create_*_from_template`.
- **Not for:** files in OneDrive/SharePoint (companyM365), permanent search over many files (companyRAG).
- **Tools (examples):** `create_word`, `create_excel`, `create_powerpoint`, `read_word`, `read_excel`, `read_pdf`,
  `convert_document`, `list_templates`.
- **Skills:** **en-file-routing**, **en-word-odt**, **en-excel**, **en-powerpoint**, **en-pdf**, **en-templates**,
  **en-convert**, **en-charts-diagram**.

## companyM365

The user's Microsoft 365, on their behalf and with their permissions.

- **For:** mail (search, read, attachments, drafts, replies, folders, rules, categories, shared mailboxes),
  calendar (events, free slots, scheduling), OneDrive and SharePoint files (search, read, Excel ranges, share
  links), Teams messages and chats (read), Teams meeting transcripts, OneNote, Planner and To Do tasks, people and
  groups.
- **Safety:** mails are created as drafts; the user sends them in Outlook. Changes to calendars, tasks or files
  happen only after the user confirms.
- **Not for:** sending mails automatically or posting in Teams, data of other people the user has no access to.
- **Tools (examples):** `search_emails`, `get_email`, `create_email_draft`, `list_upcoming_events`,
  `find_meeting_times`, `search_files`, `read_file`, `search_teams_messages`, `list_my_meeting_transcripts`,
  `create_planner_task`.
- **Prerequisite:** enabled by the administrators; on first use the user may have to consent.

## Office Add-in

companyGPT as a pane inside Word, Excel, PowerPoint and Outlook.

- **For:** working on the open document or mail: write and rewrite text, format, build tables and charts in Excel,
  add slides, draft a reply in the open mail.
- **Not for:** a new separate file to download (companyFILES).
- **Prerequisite:** rolled out by the administrators (Microsoft 365 admin center).

## companyTRANSCRIBE

Audio and video to text, as its own app and in the chat.

- **For:** meetings, interviews, voice memos, phone calls; speaker labels (who said what); export of the
  transcript. Also the other direction: speech audio (MP3) from a text (voiceover).
- **In the chat:** `transcribe_chat_file` on an attached audio/video file, then `get_transcript`; voiceover with
  `create_voiceover`. Transcription takes minutes.
- **Typical combination:** transcribe → summarise or write minutes in the chat → companyFILES for the Word file →
  companyM365 for the mail draft to the participants.
- **Not for:** Teams meetings that already have a Teams transcript (companyM365 reads those).

## companyTRANSLATE

Translation of texts and documents, as its own app and in the chat.

- **For:** texts and whole documents with the layout kept (Word, PowerPoint, Excel, PDF, …), glossaries for company
  terms, translation history.
- **Tools:** `translate_text`, `translate_document`, `list_glossaries`, `list_languages`.
- **Not for:** rewriting or summarising (the chat does that), very short texts where the chat is enough.

## companyLEARN

Corporate learning: courses with chapters, lessons, quizzes and a final exam, shown right in the chat.

- **For learners:** find courses, take lessons and quizzes in the chat, see their own progress (`learn_list_courses`,
  `learn_watch_lesson`, `learn_take_quiz`, `learn_my_progress`).
- **For course admins:** create courses from documents, companyRAG collections or SharePoint content, publish,
  assign to people, report on progress (`learn_admin_*` tools).
- **Skill:** **en-course-authoring** (admins).

## Connected Systems (MCP Servers)

MCP (Model Context Protocol) is the way agents get tools for other systems.

- **For:** live data or actions in a business system (CRM, ERP, ticketing, internal databases, specialised
  software).
- **REST APIs:** if the system has a REST API with an OpenAPI description, the administrators can connect it as an
  MCP server without programming (companyMCPROXY); every API operation becomes a tool. Also for on-premises
  systems reachable through the company network.
- **Other MCP servers:** existing MCP servers from vendors can be connected by the administrators.
- **Prerequisite:** always the administrators (connection, credentials, which users or agents get access).

## Automation (n8n)

Workflows that run without a chat, if the organisation uses n8n.

- **For:** jobs on a schedule or on an event: every night, on every new mail or form entry, between several
  systems (e.g. "every new support ticket is classified and assigned").
- **Not for:** jobs where a person asks, checks and decides in between: that is a chat, a skill or an agent.
- **Prerequisite:** n8n enabled for the organisation; workflows are built by administrators or trained power
  users.

## Skills and Agents

- **Skill:** a reusable instruction for one recurring job (steps, rules, output format). Any agent with the skill
  can use it; users start it with `$` in the chat. Build with **en-create-skill**.
- **Agent:** a permanent assistant with a model, instructions, tools, files and skills, shared with a team if
  allowed. Usually one agent plus skills is enough. Design with **en-agent-design**.
- **Ready-made skills and agents:** the companyGPT library has skills for files, sales, marketing, HR, engineering
  and more; the administrators can make them available.
