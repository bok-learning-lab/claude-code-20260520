# How Claude Remembers Your Project (CLAUDE.md & Memory)

> Source: https://code.claude.com/docs/en/memory

Give Claude persistent instructions with CLAUDE.md files, and let Claude accumulate learnings automatically with auto memory.

Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions:

- **CLAUDE.md files**: instructions you write to give Claude persistent context
- **Auto memory**: notes Claude writes itself based on your corrections and preferences

---

## CLAUDE.md vs Auto Memory

| | CLAUDE.md files | Auto memory |
|---|---|---|
| **Who writes it** | You | Claude |
| **What it contains** | Instructions and rules | Learnings and patterns |
| **Scope** | Project, user, or org | Per repository |
| **Use for** | Coding standards, workflows, project architecture | Build commands, debugging insights, preferences |

---

## CLAUDE.md files

CLAUDE.md files are markdown files that give Claude persistent instructions. Claude reads them at the start of every session.

### When to add to CLAUDE.md

- Claude makes the same mistake a second time
- A code review catches something Claude should have known
- You type the same correction into chat that you typed last session
- A new teammate would need the same context to be productive

### Where to put CLAUDE.md files

| Scope | Location | Purpose | Shared with |
|---|---|---|---|
| **Managed policy** | System-level path | Organization-wide instructions | All users |
| **User instructions** | `~/.claude/CLAUDE.md` | Personal preferences for all projects | Just you (all projects) |
| **Project instructions** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared instructions | Team via source control |
| **Local instructions** | `./CLAUDE.local.md` | Personal project-specific preferences (add to `.gitignore`) | Just you (current project) |

### Set up a project CLAUDE.md

Run `/init` to generate a starting CLAUDE.md automatically. Claude analyzes your codebase and creates a file with build commands, test instructions, and project conventions.

### Write effective instructions

- **Size**: target under 200 lines per CLAUDE.md file
- **Structure**: use markdown headers and bullets to group related instructions
- **Specificity**: write instructions that are concrete enough to verify
  - "Use 2-space indentation" instead of "Format code properly"
  - "Run `npm test` before committing" instead of "Test your changes"
  - "API handlers live in `src/api/handlers/`" instead of "Keep files organized"
- **Consistency**: if two rules contradict each other, Claude may pick one arbitrarily

### Import additional files

CLAUDE.md files can import additional files using `@path/to/import` syntax:

```markdown
See @README for project overview and @package.json for available npm commands.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

### Organize rules with `.claude/rules/`

For larger projects, organize instructions into multiple files:

```
your-project/
  .claude/
    CLAUDE.md           # Main project instructions
    rules/
      code-style.md     # Code style guidelines
      testing.md        # Testing conventions
      security.md       # Security requirements
```

#### Path-specific rules

Rules can be scoped to specific files using YAML frontmatter:

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules

- All API endpoints must include input validation
- Use the standard error response format
```

---

## Auto Memory

Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself: build commands, debugging insights, architecture notes, code style preferences.

### Enable or disable

Auto memory is on by default. Toggle with `/memory` in a session.

### Storage location

Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`.

The directory contains:
```
~/.claude/projects/<project>/memory/
  MEMORY.md            # Concise index, loaded into every session
  debugging.md         # Detailed notes on debugging patterns
  api-conventions.md   # API design decisions
```

### How it works

The first 200 lines of `MEMORY.md` (or first 25KB) are loaded at the start of every conversation. Claude keeps it concise by moving detailed notes into separate topic files.

### Audit and edit your memory

Auto memory files are plain markdown you can edit or delete at any time. Run `/memory` to browse.

---

## View and edit with `/memory`

The `/memory` command lists all CLAUDE.md, CLAUDE.local.md, and rules files loaded in your current session. Select any file to open it in your editor.

When you ask Claude to remember something ("always use pnpm, not npm"), Claude saves it to auto memory. To add instructions to CLAUDE.md instead, ask Claude directly ("add this to CLAUDE.md") or edit the file yourself.

---

## Troubleshooting

### Claude isn't following my CLAUDE.md
- Run `/memory` to verify files are being loaded
- Make instructions more specific
- Look for conflicting instructions across files
- If instructions are too long, they may get lost -- prune aggressively

### Instructions seem lost after `/compact`
- Project-root CLAUDE.md survives compaction
- Nested CLAUDE.md files in subdirectories reload when Claude reads files there
- Add conversation-only instructions to CLAUDE.md to make them persist
