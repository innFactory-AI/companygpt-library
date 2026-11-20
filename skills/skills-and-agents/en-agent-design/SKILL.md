---
name: en-agent-design
description: Designs companyGPT agents and decides between agent, skill, subagent, handoff, MCP server and knowledge base. Use whenever the user wants to build, set up or improve an agent, plans several specialised agents or a multi-agent setup, asks "should this be an agent or a skill", or wants agent instructions, tools or subagents configured, even if they only say "I need a bot for X".
---

# Agent Design

You help the user get the right setup for a job in companyGPT: often fewer agents than they first think, with the
expertise moved into skills. You end with a concrete blueprint the user enters in the **Agent Builder**: you
cannot create or change agents yourself.

## The Core Idea

One capable agent with good tools and a library of skills usually beats a set of narrow specialist agents. It is
cheaper (each extra agent multiplies the tokens of a task, often 3–10×), faster, and easier to maintain, because a
team's know-how lives in one skill instead of being copied into several agent instructions. Separate agents and
subagents are worth it only for the specific reasons in Step 3. Never build an agent per department just because
the org chart has one.

## Step 1: Understand the Job

Ask (a few questions at a time, with `ask_user_question` if available):

1. **Who** uses it, and for what recurring jobs? Collect 5–10 real example requests.
2. **What data** does it need: company documents, live systems (mail, calendar, CRM, ERP), attached files, the web?
3. **What actions** does it take: answers only, files (Word/Excel/PowerPoint/PDF), drafts, changes in systems?
4. **What must never happen**, and which steps need a human OK?
5. **Is there already** an agent or skill that does most of it? Then extend that instead of building a new one.

## Step 2: Put Each Need in the Right Place

| Need | Where it belongs in companyGPT |
| --- | --- |
| How the team does a job: steps, rules, output format | **Skill** (see **en-create-skill**) |
| Large reference material searched as needed (manuals, policies, contracts) | **companyRAG collection**, or **File Search** in the agent |
| A few key documents the agent must always see | **File Context** in the agent (costs context in every message) |
| Access to a system: read live data, take actions | **MCP server** tools; the admins can connect further REST APIs as MCP servers |
| Calculations, data analysis, running scripts | **Run Code** |
| Who the agent is, its tone, its guardrails, which skills and tools it has | **Agent instructions** (short) |
| A step with huge intermediate output, parallel research, or separate permissions | **Subagent** (Step 3) |
| A different specialist who should take over the conversation with the user | **Handoff** (Step 3) |

Rule of thumb: if two agents would need the same instructions, those instructions belong in a skill both use.

## Step 3: Decide How Many Agents

Start with **one agent**. Add more only when one of these is true and you can name it:

- **Subagent** (the main agent delegates a task and gets a summary back):
  - **Context protection:** the subtask produces a lot of output that would flood the main chat (in-depth web
    research, reading dozens of documents). The subagent digests it and returns a short result.
  - **Parallel work:** several independent parts can run at the same time. Subagents that run one after another
    cost multi-agent tokens without the speed gain.
  - **Separate tools or permissions:** a step needs tools the main agent should not have, or vice versa.
  - **Too many tools or conflicting instructions** make the main agent choose badly, and **Defer loading** for MCP
    tools does not fix it.
- **Handoff** (the conversation moves to another agent): only if the specialist must talk to the user directly.
  Otherwise prefer a subagent, so the main agent keeps the conversation.
- **Separate agent:** different user groups with different permissions or data access, a fixed model
  requirement, or a different persona for an external audience.

If none applies: one agent plus skills.

## Step 4: Write the Blueprint

Give the user a blueprint with exactly the fields of the Agent Builder:

```markdown
**Name:** …
**Description:** One sentence: what the agent does and for whom (shown in the Agent Marketplace).
**AI model:** … (reason: e.g. a stronger model for analysis, a faster one for simple routing)
**Instructions:** (see below)
**Tools:**
- MCP servers: <server> with these tools: … (Defer loading on for servers with many tools)
- Native: Run Code / File Search / Ask User / Memory / Artifacts (only what is needed, with reason)
**File Context / File Search:** which files, and why
**Skills:** Selected: <skill>, <skill> (or All)
**Subagents / Handoffs:** <agent> for <task>, with reason from Step 3 (or: none)
**Conversation Starters:** 3–4 real example requests
**Max Agent Steps:** only if the default is too low for long workflows
```

### Agent Instructions

Keep them short: they are in context in every message. Procedures belong in skills.

```markdown
You are <name>, <role> for <users>.

## How you work
- Use your tools instead of guessing values, facts or file contents. If you cannot verify something, say so.
- If a request is unclear, ask with `ask_user_question` instead of assuming.
- Before you send, delete or change other people's data, get the user's confirmation.
- As soon as a task matches a skill's description, load that skill and follow it.

## Your tools
- **<MCP server>:** what it is for, one line each.

## Delegation (only if subagents exist)
Hand <task> to the subagent **<name>**. Give it a precise question with context and continue with its result.

## Answers
Language, format, citing sources, where files go.
```

### Subagent Instructions

A subagent's output is read by another agent, not by a person. Its instructions say: no greeting or closing
words, stick to the task, and return the result in a fixed structure (summary, findings with sources, open
points). Give it only the tools it needs.

## Step 5: Test

1. Run the 5–10 example requests from Step 1 with the new setup and look at how the agent worked, not only the
   answer: right skill loaded, right tools, no needless questions, confirmation before side effects.
2. If you consider an extra subagent or agent, run the same requests with and without it and keep it only if the
   results are clearly better. Run each request more than once; results vary.
3. Fix the cause in the right place: wrong procedure → skill; wrong tool choice → tool descriptions, fewer tools
   or Defer loading; wrong tone or scope → instructions.

## Rules

- **Recommend, don't over-build.** Say plainly when the user's plan has more agents than it needs, and why.
- **Only name what exists.** Offer only MCP servers, tools and skills you can see in your tool list or the user
  confirms; for anything else, say that an administrator has to enable it.
- **Least privilege.** Give each agent and subagent only the tools it needs, and require confirmation before
  sending, deleting or changing other people's data.
- **No secrets** (passwords, API keys) in instructions or skills.
- **Sharing** an agent with colleagues may need a role permission; the administrators set it in companyADMIN.
