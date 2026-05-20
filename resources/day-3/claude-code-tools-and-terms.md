# Claude Code: Tools and Terms

A plain-language reference for how Claude Code works and how to talk to it effectively.

---

## What Claude Code is

Claude Code is Claude running in your terminal. Unlike the chat window, it can read files, run commands, and make changes to your project — autonomously, if you let it. Think of it less like a chatbot and more like a junior developer who is sitting at your computer and can do work while you watch (or step away).

The most important constraint: Claude has a **context window** — a fixed amount it can hold in memory at once. Every file it reads, every command it runs, and every message you send fills that window. When it fills up, Claude starts forgetting earlier instructions and makes more mistakes. Managing that window is the core skill.

---

## Key files Claude reads automatically

### `CLAUDE.md`

A plain-text file Claude reads at the start of every session. Put project conventions, build commands, and standing preferences here — anything you'd otherwise re-explain every time.

**Where to put it:**

| Location | Scope |
|---|---|
| `~/.claude/CLAUDE.md` | Every project on your machine |
| `./CLAUDE.md` (project root) | Everyone on the team (commit to git) |
| `./CLAUDE.local.md` | Just you, this project (add to `.gitignore`) |

**What to put in it:**
- Bash commands Claude can't guess (build, test, lint)
- Code style rules that differ from defaults
- Architectural decisions specific to this project
- Common gotchas

**What to leave out:** anything Claude can figure out from the code, standard conventions, long tutorials. Keep it under 200 lines — if it grows too long, Claude starts ignoring parts of it.

Run `/init` in any project to generate a starter `CLAUDE.md` automatically.

---

## Key folders

### `.claude/skills/`

Skills give Claude reusable workflows and domain knowledge. Each skill is a folder containing a `SKILL.md` file. Claude picks them up automatically when relevant, or you can invoke one directly with `/skill-name`.

```
.claude/skills/
└── my-skill/
    ├── SKILL.md        ← instructions and trigger description
    └── scripts/        ← optional helper scripts the skill calls
```

A minimal `SKILL.md`:
```markdown
---
name: my-skill
description: Use this skill when the user wants to [do X]
---

Instructions for what Claude should do...
```

### `.claude/agents/`

Agents are specialized versions of Claude that run in their own context window and report back. Useful for research or analysis that would otherwise fill up your main conversation.

```markdown
---
name: my-agent
description: Use this agent when... (with examples)
model: inherit
color: blue
tools: ["Read", "Grep", "Glob"]
---

You are a [role]. Your responsibilities are...
```

Claude spawns agents automatically based on the description, or you can ask explicitly: *"use a subagent to review this for security issues."*

### `.claude/rules/`

For larger projects: organize instructions into separate `.md` files by topic. Rules can be scoped to specific file types so they only load when relevant.

```markdown
---
paths:
  - "src/api/**/*.ts"
---

All API endpoints must include input validation.
```

---

## Slash commands

Type these directly in the Claude Code prompt.

| Command | What it does |
|---|---|
| `/init` | Generate a starter `CLAUDE.md` from your codebase |
| `/clear` | Reset the context window entirely — use between unrelated tasks |
| `/compact` | Summarize the conversation to free context space while keeping the session going |
| `/compact Focus on the API changes` | Compact with a hint about what matters |
| `/memory` | Browse and edit your `CLAUDE.md` files and auto memory |
| `/permissions` | Allowlist commands so Claude stops asking for approval every time |
| `/rewind` | Open a menu to restore conversation or files to a previous checkpoint |
| `/rename` | Name the current session so you can find it later |
| `/btw` | Ask a quick question that won't enter the conversation history |

Keyboard shortcuts: `Esc` stops Claude mid-action (context preserved). `Esc Esc` opens the rewind menu.

---

## Auto memory

Claude can take notes on your preferences and discoveries as it works. These go into `~/.claude/projects/<project>/memory/` and are loaded at the start of future sessions. You don't have to write anything — Claude decides what's worth saving.

To see what Claude has saved, run `/memory`. Everything is plain markdown you can edit or delete.

The difference from `CLAUDE.md`:

| | `CLAUDE.md` | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| Contains | Instructions and rules | Learnings and patterns Claude picked up |
| Use for | Standards, commands, conventions | Debugging insights, build commands Claude discovered |

---

## Prompting patterns that work

**Be specific about which file and what scenario:**
> "Write a test for `auth.py` covering the case where the session has expired. No mocks."

**Reference files with `@`:**
> "Look at `@src/api/handlers/user.ts` and follow the same pattern for a new `/orders` handler."

**Scope investigations to avoid filling context:**
> "Use a subagent to explore how session tokens are stored. Report back with just the relevant files and a summary."

**Verify Claude's work:**
> "Run the test suite after implementing. Fix any failures before stopping."

**Give Claude a way to check itself** — tests, expected outputs, screenshots — so it can catch mistakes without your help.

---

## Managing context

The context window fills up fast. These habits help:

- **`/clear` between unrelated tasks.** A long session with irrelevant history slows Claude down.
- **If Claude makes the same mistake twice, `/clear` and rewrite the prompt** incorporating what you learned. Correcting in place pollutes context with failed approaches.
- **Use subagents for exploration.** When Claude reads many files to understand something, all of that fills your window. A subagent does the reading in its own window and reports back.
- **Keep `CLAUDE.md` short.** A bloated instructions file is worse than a short one — Claude starts ignoring sections.

---

## Non-interactive mode

Run Claude from the command line without a session:

```bash
claude -p "Explain what this project does"
claude -p "List all API endpoints" --output-format json
```

Useful in CI pipelines, pre-commit hooks, or any automated workflow. Add `--allowedTools` to restrict what Claude can do when running unattended.

---

## What to try on day 3

1. Run `/init` in your project and review the generated `CLAUDE.md`.
2. Create a simple skill in `.claude/skills/` for a task you do repeatedly.
3. Try `/compact` after a long session and see what survives.
4. Use `/memory` to see what Claude has noticed about your workflow.
