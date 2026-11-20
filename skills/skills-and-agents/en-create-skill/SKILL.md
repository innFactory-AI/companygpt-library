---
name: en-create-skill
description: Creates, improves and tests skills for companyGPT agents. Use whenever the user wants to write a new skill, turn a workflow from this chat into a skill, improve or fix an existing skill, write a better skill description, or asks why a skill is not picked up, even if they only say "save this as a reusable instruction" or "teach the agent how we do X".
---

# Create Skill

You help the user build a skill: a reusable instruction that teaches companyGPT agents one job. A good skill turns
the general agent into a specialist for that job without anyone retyping the prompt. You interview, write, save,
test and improve the skill together with the user.

## How skills work in companyGPT

Knowing this lets you write skills that actually get used:

- **Catalog:** the agent sees only the `name` and `description` of every available skill, about 250 characters
  each. The description is the only trigger text. If it is vague, the skill is never loaded.
- **Loading:** when a request matches, the agent calls the `skill` tool and gets the body of `SKILL.md`. Users can
  also start a skill by typing `$` and picking it in the chat input.
- **Bundled files:** a skill can carry extra files (`references/…`, `scripts/…`, `assets/…`). The agent reads them
  with `read_file` (`skills/<name>/references/x.md`) only when it needs them, so they cost nothing until then. With
  code execution they are also in the sandbox, read-only, under `/mnt/data/skills/<name>/`.
- **Availability:** your own skills are active for you. An agent uses skills only if its Skills mode is **All** or
  **Selected** (with the skill selected). Each user can switch a skill off with **Available to agent**.

## Step 1: Capture the Intent

If the chat already contains the workflow (the user just did the task with you), extract it first: the steps, the
tools you used, the corrections the user made, the format of the result. Then fill the gaps. You need:

1. **The job:** what should the agent be able to do with this skill? One job per skill.
2. **The trigger:** which requests should load it? Collect the words users actually type, in every language your
   users write in.
3. **The result:** what does a good outcome look like (format, length, file type, tone)? Ask for a real example.
4. **The data and tools:** where does the input come from (attached file, companyRAG collection, Microsoft 365,
   web), and what must the output go into (chat answer, Word/Excel/PowerPoint/PDF via companyFILES, mail draft)?
5. **The rules:** company-specific conventions, things that went wrong before, what must never happen.

Ask only for what you cannot extract, a few questions at a time. Use `ask_user_question` if it is in your tool
list. Do not ask about things the model already knows (how to write a summary, what a SWOT is); a skill adds the
team's know-how, not general knowledge.

## Step 2: Check That a Skill Is the Right Fit

A skill holds **procedural knowledge**: how this organisation does a job. Check the other options first:

| The need is … | Better fit |
| --- | --- |
| A one-off task | Just do it in the chat |
| Reference material (manuals, policies, price lists) the agent should search | A companyRAG collection, or files in the agent |
| Access to a system (read live data, perform an action) | A tool / MCP server; an admin can connect REST APIs |
| A permanent persona with its own model, tools and instructions for a team | An agent (see **en-agent-design**), which then uses this skill |
| How to do a recurring job, with steps, rules and an output format | **A skill** |

Often the answer is a combination: the MCP server provides access, the skill says how to use it.

## Step 3: Check the Tools

A skill must only name tools that exist. Look at your own tool list, or use tool search (see **en-tool-search**),
and copy tool names and parameters exactly. For a tool that is not always present (an app the tenant has not
enabled, code execution switched off for a role), write "if available" and give a fallback. Never invent a tool,
a parameter or a limit.

Typical building blocks in companyGPT (only if present in your tool list):

- **companyFILES:** create and read Word, Excel, PowerPoint, PDF; templates; charts (see the file skills such as
  **en-excel**, **en-powerpoint**, **en-templates**).
- **companyRAG (`ai-search`):** search company knowledge collections, query datasets.
- **companyM365:** mail, calendar, OneDrive/SharePoint, Teams, OneNote, Planner.
- **companyTRANSLATE, companyTRANSCRIBE:** translate texts and documents, transcribe audio and video.
- **Code execution:** calculations, data analysis, running bundled scripts. Not available everywhere.
- **Web search / WebFetch, `ask_user_question`, memory:** depending on the agent.

## Step 4: Write the Skill

### Name

- Lowercase letters, digits and hyphens, at most 64 characters, e.g. `quarterly-report` or `offer-review`.
  It must not start with `claude-` or `anthropic-`.
- Specific, not `helper` or `tools`. If your organisation keeps skills in several languages, follow its prefix
  convention (e.g. `de-…` / `en-…`).
- The name is the skill's identity: agents reference it, and it cannot be renamed later (only re-created under a
  new name). Choose it carefully.

### Description (the most important part)

Max. 1024 characters, but put everything that decides the trigger into the **first 250 characters**, because the
catalog shortens longer descriptions.

- Say **what** the skill does and **when** to use it, in the third person: "Creates … Use when …".
- Name the concrete triggers: task words, document types, systems, the phrases users type.
- Be a little pushy, because agents tend to skip skills they are unsure about: "Use whenever the user mentions …,
  even if they do not ask for it explicitly."
- If the skill is easy to confuse with another one, say what it is **not** for.

Weak: `Helps with reports.`
Strong: `Creates the monthly sales report as an Excel file from the CRM export. Use whenever the user asks for the
sales report, monthly figures, revenue by region or attaches a CRM export, even if they don't say "report".`

### Body

Write the body for a capable colleague who is new to the team: the model already knows how to write, calculate and
summarise. Every paragraph must earn its tokens. A proven structure:

```markdown
# <Title>

<One or two sentences: what the skill achieves.>

## Step 1: … (Gather input)
## Step 2: … (Do the work, with the exact tools)
## Step 3: … (Deliver the result: format, file, where it goes)

## Output Format
<A template or a short example of a good result.>

## Rules
<Conventions and guardrails, each with its reason.>
```

- **Steps:** numbered and in order. For long or risky jobs, add a checklist the agent works through.
- **Explain the why.** "Round to whole euros, because the board report does too" works better than "ALWAYS ROUND".
  A rule in capitals without a reason is a warning sign.
- **One default, one fallback.** Not five options. Example: "Create the file with companyFILES `create_excel`; if
  companyFILES is not available, give the table as Markdown."
- **Concrete examples** of input and output, not abstract descriptions.
- **Match the strictness to the risk:** free text for open tasks, exact steps or a fixed template where mistakes
  are expensive (contracts, numbers, mails to customers).
- **Confirmation before side effects:** sending mails, deleting files or changing other people's calendars only
  after the user says yes.
- **Consistent terms:** one word per concept throughout.
- **No dates or "currently"** that go stale; no passwords, keys, personal data or customer secrets in the skill.
- **Length:** keep `SKILL.md` well under 500 lines. Move long material into bundled files (next section).

### Bundled Files (Optional)

For long reference material (a style guide, a detailed recipe, a script):

- Put it in `references/<topic>.md` (or `scripts/…`, `assets/…`), one level deep, and link it from `SKILL.md`
  with the path and when to read it: "For the full price table, read `skills/<name>/references/prices.md`."
- Reference files over about 100 lines start with a short table of contents.
- `SKILL.md` must still work on its own, because a skill pasted as a single file has no bundled files.

### Code (Optional)

The skill must work without code execution. Code steps go into an optional section that starts with "If code
execution is available …", names the fallback, checks Python packages with `import` before relying on them, and
remembers that the sandbox has no network access. Scripts the agent should run go into `scripts/`; they must handle
their own errors and say what each constant means.

### Optional Frontmatter Fields

Most skills only need `name` and `description`. Use these only when there is a reason:

| Field | Effect |
| --- | --- |
| `disable-model-invocation: true` | The agent never loads the skill on its own; only `$` in the chat starts it. For skills with side effects. |
| `user-invocable: false` | Hidden from the `$` menu; only the agent loads it. |
| `always-apply: true` | Loaded in every conversation. Use rarely: it costs context in every chat. |
| `allowed-tools` | Tools the skill brings into the turn, as a list. |

`$ARGUMENTS` in the body is replaced by what the user typed after the skill when starting it with `$`.

## Step 5: Save the Skill

Show the user the full `SKILL.md` and get their OK first. Then save it:

1. **If `create_file` is in your tool list** and accepts `skills/…` paths: create `skills/<name>/SKILL.md` (and
   bundled files under `skills/<name>/references/…`). The `name` in the frontmatter must equal `<name>`. Do not
   set `overwrite` for a new skill; if the name exists, ask before overwriting. Change an existing skill with
   `edit_file` instead of rewriting it.
2. **Otherwise, with code execution:** write the folder `/mnt/data/<name>/` with `SKILL.md` (and bundled files) and
   zip it as `/mnt/data/<name>.zip`; the zip comes back as a chat attachment. The user uploads it under
   **Skills → + → Upload a skill**.
3. **Otherwise:** give the complete `SKILL.md` in one Markdown code block. The user creates it under
   **Skills → + → Write skill instructions** (name, description and the body as instructions) or saves it as
   `SKILL.md` and uploads it.

Tell the user how to make the skill available: switch on **Available to agent** in the skill view, and add it to
an agent with Skills mode **Selected** if needed. Sharing with colleagues may need a role permission; a skill for
the whole organisation goes through the companyGPT administrators.

## Step 6: Test and Improve

A skill is not done until it has been tested. With the user:

1. **Write 2–3 realistic test requests**, phrased the way users actually write, with real details (file names,
   customer names, numbers).
2. **Check the trigger:** list 3–5 requests that should load the skill and 3–5 near misses that should not
   (similar wording, different job). Adjust the description if one lands on the wrong side.
3. **Run the tests** in a new chat with the agent that has the skill (loading it via `$` once is a quick check of
   the body alone). If you saved the skill yourself, you can also load it with the `skill` tool here and run a test
   request directly.
4. **Read how the agent worked, not only the result.** Did it skip a step, guess a tool, ask needless questions,
   produce the wrong format? Fix the instruction that caused it.
5. **Improve in general terms.** Do not patch the skill for one test case only; ask what the case shows about the
   instructions. Remove instructions that did not help.

Repeat until the user is satisfied with the results.

## Review Checklist

Before you call a skill done, check:

- [ ] Name: lowercase, hyphens, ≤64 characters, specific, follows the organisation's convention.
- [ ] Description: what + when + trigger words in the first 250 characters, third person.
- [ ] Every tool, parameter and limit exists in the tool list; optional apps have a fallback.
- [ ] Works without code execution and without bundled files.
- [ ] Steps are numbered; the output format is shown with an example.
- [ ] Rules give their reason; no unexplained capital-letter MUSTs.
- [ ] Confirmation before sending, deleting or changing other people's data.
- [ ] No secrets, personal data or time-sensitive statements.
- [ ] Under 500 lines; long material in `references/`, linked one level deep.
- [ ] Tested with realistic requests, including near misses for the trigger.
