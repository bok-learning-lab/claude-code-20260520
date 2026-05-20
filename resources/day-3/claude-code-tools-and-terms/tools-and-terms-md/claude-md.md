# CLAUDE.md

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

**See also:** [CLAUDE.local.md](claude-local-md.md) · [Auto Memory](auto-memory.md) · [Rules](rules.md) · [/init](slash-init.md) · [/memory](slash-memory.md)
