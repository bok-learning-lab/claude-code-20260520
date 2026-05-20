# Path-specific rules

> Source: https://code.claude.com/docs/en/memory#path-specific-rules
>
> Scope instructions to specific file types or directories so they only load when Claude works with matching files.

Path-specific rules are part of the `.claude/rules/` system for organizing instructions. Instead of putting everything in CLAUDE.md (which loads every session), rules let you scope instructions to specific file types or directories. Rules with a `paths` field only load when Claude reads files matching the specified patterns, saving context and reducing noise.

> **Note:** Rules load into context every session or when matching files are opened. For task-specific instructions that don't need to be in context all the time, use [skills](/en/skills) instead, which only load when you invoke them or when Claude determines they're relevant to your prompt.

---

## Setting up rules

Place markdown files in your project's `.claude/rules/` directory. Each file should cover one topic, with a descriptive filename like `testing.md` or `api-design.md`. All `.md` files are discovered recursively, so you can organize rules into subdirectories like `frontend/` or `backend/`:

```
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Code style guidelines
│       ├── testing.md      # Testing conventions
│       └── security.md     # Security requirements
```

Rules without `paths` frontmatter are loaded at launch with the same priority as `.claude/CLAUDE.md`.

---

## Path scoping with frontmatter

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

Rules **without** a `paths` field are loaded unconditionally and apply to all files. Path-scoped rules trigger when Claude reads files matching the pattern, not on every tool use.

---

## Glob pattern examples

Use glob patterns in the `paths` field to match files by extension, directory, or any combination:

| Pattern | Matches |
|---|---|
| `**/*.ts` | All TypeScript files in any directory |
| `src/**/*` | All files under `src/` directory |
| `*.md` | Markdown files in the project root |
| `src/components/*.tsx` | React components in a specific directory |

You can specify multiple patterns and use brace expansion to match multiple extensions in one pattern:

```markdown
---
paths:
  - "src/**/*.{ts,tsx}"
  - "lib/**/*.ts"
  - "tests/**/*.test.ts"
---
```

---

## Rules without paths (always loaded)

If a rule file has no `paths` frontmatter, it loads at session start alongside CLAUDE.md:

```markdown
# Code Style Rules

- Use 2-space indentation
- Prefer const over let
- Use descriptive variable names
```

This is equivalent to putting the content in CLAUDE.md but helps keep things organized.

---

## Sharing rules across projects with symlinks

The `.claude/rules/` directory supports symlinks, so you can maintain a shared set of rules and link them into multiple projects. Symlinks are resolved and loaded normally, and circular symlinks are detected and handled gracefully.

This example links both a shared directory and an individual file:

```bash
ln -s ~/shared-claude-rules .claude/rules/shared
ln -s ~/company-standards/security.md .claude/rules/security.md
```

---

## User-level rules

Personal rules in `~/.claude/rules/` apply to every project on your machine. Use them for preferences that aren't project-specific:

```
~/.claude/rules/
├── preferences.md    # Your personal coding preferences
└── workflows.md      # Your preferred workflows
```

User-level rules are loaded before project rules, giving project rules higher priority.

---

## Rules vs. CLAUDE.md vs. Skills

All three store instructions, but they load differently:

| Aspect | CLAUDE.md | `.claude/rules/` | Skill |
|---|---|---|---|
| **Loads** | Every session | Every session, or when matching files are opened | On demand, when invoked or relevant |
| **Scope** | Whole project | Can be scoped to file paths | Task-specific |
| **Best for** | Core conventions and build commands | Language-specific or directory-specific guidelines | Reference material, repeatable workflows |

**Use CLAUDE.md** for instructions every session needs: build commands, test conventions, project architecture.

**Use rules** to keep CLAUDE.md focused. Rules with `paths` frontmatter only load when Claude works with matching files, saving context.

**Use skills** for content Claude only needs sometimes, like API documentation or a deployment checklist you trigger with `/<name>`.

**Rule of thumb**: If you find your CLAUDE.md growing past 200 lines, move specialized content into path-scoped rules.

---

## Debugging rules

> **Tip:** Use the `InstructionsLoaded` hook to log exactly which instruction files are loaded, when they load, and why. This is useful for debugging path-specific rules or lazy-loaded files in subdirectories.

If Claude isn't following a rule:

- Run `/memory` to verify the rule file is listed
- Check that the `paths` pattern matches the files you're working with
- Make instructions more specific ("Use 2-space indentation" works better than "format code nicely")
- Look for conflicting instructions across CLAUDE.md files and rules
