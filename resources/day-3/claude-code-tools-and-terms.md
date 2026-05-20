# Claude Code: Tools and Terms

A dictionary-style reference for beginners. Each entry defines one concept, explains it in plain language, and shows you what it looks like in practice. Read straight through, or jump to whatever term you just encountered.

---

## Quick index

[Claude Code](#claude-code) · [Context Window](#context-window) · [CLAUDE.md](#claudemd) · [CLAUDE.local.md](#claudelocalmd) · [Auto Memory](#auto-memory) · [Skills](#skills-claudeskills) · [Agents / Subagents](#agents--subagents-claudeagents) · [Rules](#rules-clauderules) · [Path-Specific Rules](#path-specific-rules) · [Plan Mode](#plan-mode) · [Permissions](#permissions) · [Hooks](#hooks) · [MCP Servers](#mcp-servers) · [Plugins](#plugins) · [Non-Interactive Mode](#non-interactive-mode) · [Checkpoints](#checkpoints) · [Sessions](#sessions)

**Slash commands:** [/init](#init) · [/clear](#clear) · [/compact](#compact) · [/memory](#memory) · [/permissions](#permissions-command) · [/rewind](#rewind) · [/rename](#rename) · [/btw](#btw) · [/sandbox](#sandbox)

**Prompting:** [Give Claude a way to verify its work](#give-claude-a-way-to-verify-its-work) · [Explore first, then plan, then code](#explore-first-then-plan-then-code) · [Provide specific context](#provide-specific-context) · [Reference files with @](#reference-files-with-) · [Course-correct early](#course-correct-early) · [Use subagents for investigation](#use-subagents-for-investigation)

---

## Claude Code

> **In one line:** Claude Code is an agentic coding environment — Claude running in your terminal, able to read your files, run commands, and make changes to your project while you watch or step away.

Claude Code is fundamentally different from a chatbot. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.

This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.

**The most important thing to understand:** almost all best practices for Claude Code trace back to one constraint — Claude's context window fills up fast, and performance degrades as it fills. Claude's context window holds your entire conversation, including every message, every file Claude reads, and every command output. When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage.

**See also:** [Context Window](#context-window) · [CLAUDE.md](#claudemd) · [Skills](#skills-claudeskills)

---

## Context Window

> **In one line:** The context window is the fixed amount of text Claude can hold in view at one time — it fills up, and when it does, Claude's performance degrades.

Claude's context window holds your entire conversation: every message you send, every file Claude reads, and every command output. This can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens.

When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. This is the single most important resource to manage in a Claude Code session.

**What fills the window:**
- Every message you send and every reply Claude gives
- Every file Claude reads (even if it only reads part of it)
- Output from every command Claude runs
- Your CLAUDE.md files (loaded at the start of every session)

**What you can do about it:**
- Use `/clear` to reset the context window entirely between unrelated tasks
- Use `/compact` to summarize a long conversation and continue in a leaner state
- Use subagents to offload research — they run in their own context windows
- Keep your CLAUDE.md short so it doesn't eat context at the start of every session

**See also:** [/clear](#clear) · [/compact](#compact) · [CLAUDE.md](#claudemd) · [Agents / Subagents](#agents--subagents-claudeagents)

---

## CLAUDE.md

> **In one line:** CLAUDE.md is a special markdown file that Claude reads at the start of every conversation — a place to write down standing instructions so you don't have to re-explain them every session.

CLAUDE.md is how you give Claude persistent context. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone.

There is no required format for CLAUDE.md files, but keep it short and human-readable. For example:

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, not the whole test suite, for performance
```

**Where to put CLAUDE.md files — each location has a different scope:**

| Location | Who sees it | What it's for |
|---|---|---|
| `~/.claude/CLAUDE.md` | Just you, on all your projects | Personal preferences across every project |
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Everyone on the team | Project conventions — commit this to git |
| `./CLAUDE.local.md` | Just you, this project | Personal project-specific notes — add to `.gitignore` |
| `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | Everyone on the machine | Organization-wide policies managed by IT |

CLAUDE.md files in parent directories above your working directory are also loaded automatically. Files in subdirectories load on demand when Claude works with files in those directories.

**What to include:**

| ✅ Include | ❌ Exclude |
|---|---|
| Bash commands Claude can't guess | Anything Claude can figure out by reading the code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Architectural decisions specific to your project | Information that changes frequently |
| Common gotchas or non-obvious behaviors | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |

**Keep it short.** CLAUDE.md is loaded into the context window at the start of every session, consuming tokens. Target under 200 lines. Longer files reduce adherence — if Claude keeps doing something you don't want despite a rule against it, the file may be too long and the rule is getting lost. For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it.

**CLAUDE.md can import other files** using `@path/to/file` syntax:

```markdown
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
```

Imported files are expanded and loaded into context at launch. Use relative or absolute paths.

Run `/init` to generate a starter CLAUDE.md automatically — Claude analyzes your codebase and creates a file with build commands, test instructions, and project conventions it discovers.

**See also:** [CLAUDE.local.md](#claudelocalmd) · [Auto Memory](#auto-memory) · [Rules](#rules-clauderules) · [/init](#init) · [/memory](#memory)

---

## CLAUDE.local.md

> **In one line:** CLAUDE.local.md is a personal, private version of CLAUDE.md for one project — for notes you don't want to share with your team via git.

CLAUDE.local.md sits alongside CLAUDE.md at the project root and is loaded in the same way. The difference: it's meant for personal preferences that shouldn't be checked into version control. Add it to your `.gitignore`.

Use it for things like:
- Your local sandbox URLs
- Preferred test data you use personally
- Shortcuts specific to your machine setup

When you run `/init` and choose the personal option, it creates CLAUDE.local.md and adds it to `.gitignore` for you.

**See also:** [CLAUDE.md](#claudemd)

---

## Auto Memory

> **In one line:** Auto memory is a feature where Claude automatically saves notes about your project and preferences across sessions — without you writing anything.

Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself as it works: build commands, debugging insights, architecture notes, code style preferences, and workflow habits. Claude doesn't save something every session — it decides what's worth remembering based on whether the information would be useful in a future conversation.

**Where it lives:** Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The directory contains a `MEMORY.md` entrypoint and optional topic files:

```
~/.claude/projects/<project>/memory/
├── MEMORY.md          # Concise index, loaded into every session
├── debugging.md       # Detailed notes on debugging patterns
├── api-conventions.md # API design decisions
└── ...
```

The first 200 lines of `MEMORY.md` are loaded at the start of every conversation. Claude keeps it concise by moving detailed notes into separate topic files, which it reads on demand.

**How CLAUDE.md and auto memory differ:**

| | CLAUDE.md | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| What it contains | Instructions and rules | Learnings and patterns Claude discovered |
| Use for | Coding standards, workflows, project architecture | Build commands, debugging insights, preferences Claude found |

**To see what Claude has saved:** run `/memory`. Everything is plain markdown you can read, edit, or delete at any time.

**To turn it off:** open `/memory` and use the auto memory toggle, or add `"autoMemoryEnabled": false` to your project settings.

**See also:** [CLAUDE.md](#claudemd) · [/memory](#memory)

---

## Skills (`.claude/skills/`)

> **In one line:** Skills are reusable workflows and domain knowledge you give Claude — stored in `.claude/skills/`, each skill is a folder with a SKILL.md file that Claude applies automatically when relevant.

Skills extend Claude's knowledge with information specific to your project, team, or domain. Claude applies them automatically when relevant, or you can invoke them directly with `/skill-name`.

Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`:

```markdown
<!-- .claude/skills/api-conventions/SKILL.md -->
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

Skills can also define repeatable workflows you invoke directly:

```markdown
<!-- .claude/skills/fix-issue/SKILL.md -->
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

Run `/fix-issue 1234` to invoke it. Use `disable-model-invocation: true` for workflows with side effects that you want to trigger manually rather than have Claude invoke automatically.

**Full skill folder structure:**

```
.claude/skills/
└── my-skill/
    ├── SKILL.md           ← required: instructions and trigger description
    ├── scripts/           ← optional: helper scripts the skill calls
    ├── references/        ← optional: docs Claude loads into context as needed
    └── assets/            ← optional: templates, icons, other files
```

**Skills vs. CLAUDE.md:** CLAUDE.md is loaded into context every session — use it for things that apply broadly. Skills load on demand, keeping every conversation lean. If an instruction is only relevant sometimes, or for a specific task, it belongs in a skill.

**See also:** [CLAUDE.md](#claudemd) · [Agents / Subagents](#agents--subagents-claudeagents)

---

## Agents / Subagents (`.claude/agents/`)

> **In one line:** Subagents are specialized versions of Claude that run in their own context window — Claude can delegate tasks to them so the research or analysis doesn't clutter your main conversation.

Subagents run in their own context with their own set of allowed tools. They're useful for tasks that read many files or need specialized focus without cluttering your main conversation.

```markdown
<!-- .claude/agents/security-reviewer.md -->
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

Tell Claude to use subagents explicitly: *"Use a subagent to review this code for security issues."*

**Why subagents matter for context:** since the context window is your fundamental constraint, subagents are one of the most powerful tools available. When Claude researches a codebase it reads lots of files, all of which consume your context. Subagents run in separate context windows and report back summaries — keeping your main conversation clean for implementation.

**Required frontmatter fields:**

| Field | Required | Options | Notes |
|---|---|---|---|
| `name` | Yes | lowercase, hyphens only | 3–50 characters |
| `description` | Yes | text + `<example>` blocks | This is how Claude decides when to use the agent |
| `model` | Recommended | `inherit`, `sonnet`, `opus`, `haiku` | `inherit` uses the same model as the parent |
| `color` | Optional | `blue`, `cyan`, `green`, `yellow`, `magenta`, `red` | Visual identifier in the UI |
| `tools` | Optional | array of tool names | Omit for full access; restrict for least privilege |

**See also:** [Skills](#skills-claudeskills) · [Context Window](#context-window) · [Use subagents for investigation](#use-subagents-for-investigation)

---

## Rules (`.claude/rules/`)

> **In one line:** Rules are instruction files in `.claude/rules/` — a way to organize project instructions into separate topic files instead of one long CLAUDE.md.

For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain.

```
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Code style guidelines
│       ├── testing.md      # Testing conventions
│       └── security.md     # Security requirements
```

Place markdown files in `.claude/rules/`. Each file should cover one topic, with a descriptive filename. All `.md` files are discovered recursively, so you can organize rules into subdirectories.

Rules without a `paths` field (see below) are loaded at launch alongside CLAUDE.md.

**Rules vs. skills:** Rules load into context every session, or when matching files are opened. For task-specific instructions that don't need to be in context all the time, use skills instead — skills only load when you invoke them or when Claude determines they're relevant.

**See also:** [CLAUDE.md](#claudemd) · [Path-Specific Rules](#path-specific-rules) · [Skills](#skills-claudeskills)

---

## Path-Specific Rules

> **In one line:** Path-specific rules are rule files with a `paths:` field in their frontmatter — they only load into context when Claude is working with files matching the specified pattern.

Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules

- All API endpoints must include input validation
- Use the standard error response format
- Include OpenAPI documentation comments
```

Rules without a `paths` field are loaded unconditionally and apply to all files. Path-scoped rules trigger when Claude reads files matching the pattern — not on every tool use.

**Glob pattern examples:**

| Pattern | Matches |
|---|---|
| `**/*.ts` | All TypeScript files in any directory |
| `src/**/*` | All files under `src/` |
| `*.md` | Markdown files in the project root |
| `src/components/*.tsx` | React components in a specific directory |
| `src/**/*.{ts,tsx}` | TypeScript and TSX files anywhere under `src/` |

**Why this matters:** loading instructions only when relevant keeps the context window lean. If you have 500 lines of API conventions and 500 lines of frontend conventions, there's no reason both are in context when you're editing a database migration.

**See also:** [Rules](#rules-clauderules) · [Context Window](#context-window)

---

## Plan Mode

> **In one line:** Plan mode lets Claude read files and think through a problem without making any changes — you review and approve before anything gets written.

Plan mode separates exploration from execution. Letting Claude jump straight to coding can produce code that solves the wrong problem. Plan mode gives you a chance to check the approach first.

**The recommended four-phase workflow:**

**1. Explore** — enter plan mode. Claude reads files and answers questions without making changes.
```
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.
```

**2. Plan** — ask Claude to create a detailed implementation plan.
```
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.
```
Press `Ctrl+G` to open the plan in your text editor for direct editing before Claude proceeds.

**3. Implement** — switch out of plan mode and let Claude code, verifying against its plan.
```
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.
```

**4. Commit** — ask Claude to commit with a descriptive message and create a PR.
```
commit with a descriptive message and open a PR
```

**When to use plan mode:** most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified. For tasks where the scope is clear and the fix is small (fixing a typo, renaming a variable), ask Claude to do it directly — planning adds overhead that isn't always worth it.

---

## Permissions

> **In one line:** Permissions control what Claude Code is allowed to do — write files, run commands, use tools — and how much it asks you before doing it.

By default, Claude Code requests permission for actions that might modify your system: file writes, Bash commands, MCP tools, etc. This is safe but tedious. After the tenth approval you're not really reviewing anymore, you're just clicking through.

**Three ways to reduce interruptions:**

**Auto mode** — a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions. Best when you trust the general direction of a task but don't want to click through every step.

**Permission allowlists** — permit specific tools you know are safe, like `npm run lint` or `git commit`. Use `/permissions` to configure these.

**Sandboxing** — enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries. Use `/sandbox` to enable.

**See also:** [/permissions](#permissions-command) · [/sandbox](#sandbox)

---

## Hooks

> **In one line:** Hooks are shell commands that run automatically at specific points in Claude's workflow — they're deterministic, unlike CLAUDE.md instructions which Claude may or may not follow.

Hooks run scripts automatically at specific points in Claude's workflow. Unlike CLAUDE.md instructions which are advisory (Claude reads them and tries to follow them), hooks are deterministic and guarantee the action happens.

Claude can write hooks for you. Try prompts like:
- *"Write a hook that runs eslint after every file edit"*
- *"Write a hook that blocks writes to the migrations folder."*

Edit `.claude/settings.json` directly to configure hooks by hand, and run `/hooks` to browse what's configured.

**Hooks vs. CLAUDE.md:** If an instruction is something that must run at a specific point — before every commit, after each file edit — write it as a hook. Hooks execute as shell commands at fixed lifecycle events and apply regardless of what Claude decides to do.

**See also:** [CLAUDE.md](#claudemd)

---

## MCP Servers

> **In one line:** MCP (Model Context Protocol) servers are external tools Claude can connect to — things like Notion, Figma, your database, or a GitHub integration.

Run `claude mcp add` to connect external tools. With MCP servers, you can ask Claude to implement features from issue trackers, query databases, analyze monitoring data, integrate designs from Figma, and automate workflows across external services.

MCP servers appear as additional tools in Claude's toolbox — Claude can call them the same way it calls built-in tools like reading files or running Bash commands.

---

## Plugins

> **In one line:** Plugins bundle skills, hooks, subagents, and MCP servers into a single installable unit — browse and install them from the marketplace with `/plugin`.

Run `/plugin` to browse the marketplace. Plugins add skills, hooks, subagents, and MCP servers into a single installable unit from the community and Anthropic.

If you work with a typed language, install a code intelligence plugin to give Claude precise symbol navigation and automatic error detection after edits.

---

## Non-Interactive Mode

> **In one line:** Non-interactive mode lets you run Claude from the command line without starting a session — useful for scripts, CI pipelines, and automated workflows.

With `claude -p "your prompt"`, you can run Claude non-interactively, without a session. This is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow.

```bash
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

Add `--allowedTools` to restrict what Claude can do when running unattended:

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

Use `--verbose` for debugging during development, and turn it off in production.

---

## Checkpoints

> **In one line:** Every prompt you send creates a checkpoint — a snapshot of your conversation and files that you can restore at any time.

Claude automatically snapshots files before each change so a checkpoint can restore them. Double-tap `Escape` or run `/rewind` to open the rewind menu. You can:
- Restore conversation only
- Restore code (files) only
- Restore both conversation and files
- Summarize from a selected message

Checkpoints persist across sessions, so you can close your terminal and still rewind later. Instead of carefully planning every move, you can tell Claude to try something risky — if it doesn't work, rewind and try a different approach.

**Important:** checkpoints only track changes made *by Claude*, not external processes. This isn't a replacement for git.

**See also:** [/rewind](#rewind)

---

## Sessions

> **In one line:** Claude Code saves conversations locally so you can pick up exactly where you left off — resume the most recent session with `claude --continue`, or choose from a list with `claude --resume`.

Claude Code saves conversations locally, so when a task spans multiple sittings you don't have to re-explain the context.

```bash
claude --continue    # pick up the most recent session
claude --resume      # choose from a list of saved sessions
```

Give sessions descriptive names so you can find them later. Run `/rename` inside a session to name it (e.g. `oauth-migration`). Treat named sessions like branches — each workstream gets its own persistent context.

**See also:** [/rename](#rename)

---

---

# Slash Commands

Commands you type directly in the Claude Code prompt. Each one is a built-in shortcut for a common operation.

---

## /init

> **In one line:** `/init` generates a starter CLAUDE.md file for your current project by analyzing your codebase.

Running `/init` makes Claude analyze your project to detect build systems, test frameworks, and code patterns, then creates a CLAUDE.md with build commands, test instructions, and project conventions it discovers.

If a CLAUDE.md already exists, `/init` suggests improvements rather than overwriting it.

Set `CLAUDE_CODE_NEW_INIT=1` to enable an interactive multi-phase flow. `/init` asks which artifacts to set up (CLAUDE.md files, skills, hooks), explores your codebase with a subagent, fills in gaps via follow-up questions, and presents a reviewable proposal before writing any files.

**See also:** [CLAUDE.md](#claudemd)

---

## /clear

> **In one line:** `/clear` resets the context window entirely — use it between unrelated tasks to start fresh.

Running `/clear` wipes the conversation and starts a new session. Use it when:
- You're switching to a completely different task
- Claude has made the same mistake twice and the context is polluted with failed approaches
- The session has accumulated irrelevant conversation that's dragging performance down

If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. A clean session with a better prompt almost always outperforms a long session with accumulated corrections.

**See also:** [Context Window](#context-window) · [/compact](#compact)

---

## /compact

> **In one line:** `/compact` summarizes the current conversation to free context space while keeping the session going — unlike `/clear`, you don't lose the thread.

Running `/compact` automatically summarizes conversation history, preserving important code and decisions while freeing space. Use it when:
- You're in the middle of a task and don't want to start over
- The context is getting long but the work is ongoing
- You want to carry only the essentials forward

You can add a hint: `/compact Focus on the API changes` — Claude will emphasize those details in the summary.

For more control, use `Esc + Esc` or `/rewind`, select a message checkpoint, and choose **Summarize from here** or **Summarize up to here**:
- *Summarize from here* — condenses messages from that point forward while keeping earlier context intact
- *Summarize up to here* — condenses earlier messages while keeping recent ones in full

**Customize compaction in CLAUDE.md** with instructions like `"When compacting, always preserve the full list of modified files and any test commands"` — this ensures critical context survives summarization.

**Project-root CLAUDE.md survives compaction:** after `/compact`, Claude re-reads it from disk and re-injects it. Nested CLAUDE.md files in subdirectories are not re-injected automatically — they reload the next time Claude reads a file in that subdirectory.

**See also:** [/clear](#clear) · [Context Window](#context-window) · [Checkpoints](#checkpoints)

---

## /memory

> **In one line:** `/memory` lists all CLAUDE.md, CLAUDE.local.md, and rules files loaded in your current session, and provides a link to open the auto memory folder.

Running `/memory` shows you everything Claude is reading as context at the start of this session — a useful debugging tool when instructions aren't being followed.

From `/memory` you can:
- See which CLAUDE.md and rules files are loaded
- Toggle auto memory on or off
- Open the auto memory folder to browse or edit what Claude has saved
- Select any file to open it in your editor

When you ask Claude to remember something ("always use pnpm, not npm"), Claude saves it to auto memory. To add instructions to CLAUDE.md instead, ask Claude directly ("add this to CLAUDE.md") or edit the file yourself via `/memory`.

**See also:** [CLAUDE.md](#claudemd) · [Auto Memory](#auto-memory)

---

## /permissions (command)

> **In one line:** `/permissions` opens the permission configuration UI — use it to allowlist specific commands so Claude stops asking for approval every time.

Use `/permissions` to permit specific tools and commands you know are safe, like `npm run lint` or `git commit`. Once allowlisted, Claude runs them without prompting.

You can also allowlist frequently-used documentation domains so Claude can fetch them with the URL tool without asking each time.

**See also:** [Permissions](#permissions)

---

## /rewind

> **In one line:** `/rewind` opens a checkpoint menu where you can restore your conversation, your files, or both to any earlier state.

Press `Esc + Esc` or run `/rewind` to open the rewind menu. You can restore:
- **Conversation only** — rolls back the chat, leaves files as-is
- **Code (files) only** — restores file state from a checkpoint, leaves the conversation intact
- **Both** — full restore to that moment
- **Summarize from here / up to here** — condense instead of restore

Every prompt you send creates a checkpoint automatically. Checkpoints persist across sessions.

**See also:** [Checkpoints](#checkpoints)

---

## /rename

> **In one line:** `/rename` lets you give the current session a descriptive name so you can find it later.

By default, sessions are named automatically. Use `/rename` to give a session a meaningful name like `oauth-migration` or `refactor-api-layer`. This makes it easy to find and resume specific workstreams with `claude --resume`.

**See also:** [Sessions](#sessions)

---

## /btw

> **In one line:** `/btw` lets you ask a quick side question that appears in a dismissible overlay and never enters conversation history.

Use `/btw` when you need to check a detail without growing your context. The answer appears in a dismissible overlay — it never becomes part of the conversation, so you can ask something without spending tokens on it.

Useful for quick factual lookups or clarifications mid-session that you don't want influencing the rest of the conversation.

**See also:** [Context Window](#context-window)

---

## /sandbox

> **In one line:** `/sandbox` enables OS-level isolation — Claude can work more freely within defined boundaries without the risk of affecting the rest of your system.

Sandboxing restricts filesystem and network access, allowing Claude to work more freely within defined boundaries while preventing actions outside them.

**See also:** [Permissions](#permissions)

---

---

# Prompting Patterns

These are specific patterns — drawn directly from Anthropic's best practices — that make a measurable difference in the quality of Claude's work.

---

## Give Claude a way to verify its work

> **The single highest-leverage thing you can do.** Claude performs dramatically better when it can verify its own work.

Without clear success criteria, Claude might produce something that looks right but doesn't work. You become the only feedback loop, and every mistake requires your attention.

| Strategy | Before | After |
|---|---|---|
| **Provide verification criteria** | *"implement a function that validates email addresses"* | *"write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing"* |
| **Verify UI changes visually** | *"make the dashboard look better"* | *"[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them"* |
| **Address root causes, not symptoms** | *"the build is failing"* | *"the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error"* |

Your verification can be a test suite, a linter, or a Bash command that checks output. Invest in making your verification rock-solid.

---

## Explore first, then plan, then code

> **Separate research and planning from implementation to avoid solving the wrong problem.**

Use plan mode to separate exploration from execution. See [Plan Mode](#plan-mode) for the full four-phase workflow.

If you could describe the fix in one sentence, skip planning. Planning is most useful when:
- You're uncertain about the approach
- The change modifies multiple files
- You're unfamiliar with the code being modified

---

## Provide specific context

> **The more precise your instructions, the fewer corrections you'll need.** Claude can infer intent, but it can't read your mind.

Reference specific files, mention constraints, and point to example patterns.

| Strategy | Before | After |
|---|---|---|
| **Scope the task** | *"add tests for foo.py"* | *"write a test for foo.py covering the edge case where the user is logged out. avoid mocks."* |
| **Point to sources** | *"why does ExecutionFactory have such a weird api?"* | *"look through ExecutionFactory's git history and summarize how its api came to be"* |
| **Reference existing patterns** | *"add a calendar widget"* | *"look at how existing widgets are implemented on the home page. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards."* |
| **Describe the symptom** | *"fix the login bug"* | *"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it"* |

Vague prompts can be useful when you're exploring and can afford to course-correct. A prompt like *"what would you improve in this file?"* can surface things you wouldn't have thought to ask about.

---

## Reference files with @

> **Use `@` to pull files into context directly — Claude reads the file before responding.**

Instead of describing where code lives, use `@` to reference it:

```
look at @src/api/handlers/user.ts and follow the same pattern for a new /orders handler
```

You can also:
- **Paste images directly** — copy/paste or drag and drop screenshots into the prompt
- **Give URLs** for documentation and API references
- **Pipe in data** — run `cat error.log | claude` to send file contents directly
- **Let Claude fetch what it needs** — tell Claude to pull context itself using Bash commands, MCP tools, or by reading files

---

## Course-correct early

> **The best results come from tight feedback loops.** Correct Claude as soon as you notice it going off track.

- **`Esc`** — stop Claude mid-action. Context is preserved, so you can redirect.
- **`Esc + Esc` or `/rewind`** — restore previous conversation and code state, or summarize from a selected message.
- **`"Undo that"`** — have Claude revert its changes.
- **`/clear`** — reset context between unrelated tasks.

If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned.

---

## Use subagents for investigation

> **Delegate research to subagents so the exploration doesn't consume your main context.**

Since context is your fundamental constraint, subagents are one of the most powerful tools available. When Claude researches a codebase it reads lots of files — all of which consume your context. Subagents run in separate context windows and report back summaries:

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

The subagent explores the codebase, reads relevant files, and reports back with findings — without cluttering your main conversation.

You can also use subagents for verification after Claude implements something:

```
use a subagent to review this code for edge cases
```

**See also:** [Agents / Subagents](#agents--subagents-claudeagents) · [Context Window](#context-window)

---

## Common failure patterns to avoid

These are the most common mistakes — recognizing them early saves time.

**The kitchen sink session.** You start with one task, then ask Claude something unrelated, then go back to the first task. Context is full of irrelevant information.
> Fix: `/clear` between unrelated tasks.

**Correcting over and over.** Claude does something wrong, you correct it, it's still wrong, you correct again. Context is polluted with failed approaches.
> Fix: after two failed corrections, `/clear` and write a better initial prompt incorporating what you learned.

**The over-specified CLAUDE.md.** Your CLAUDE.md is too long, so Claude ignores half of it because important rules get lost in the noise.
> Fix: ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.

**The trust-then-verify gap.** Claude produces a plausible-looking implementation that doesn't handle edge cases.
> Fix: always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it.

**The infinite exploration.** You ask Claude to "investigate" something without scoping it. Claude reads hundreds of files, filling the context.
> Fix: scope investigations narrowly or use subagents so the exploration doesn't consume your main context.
