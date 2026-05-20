# Skills (`.claude/skills/`)

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

**See also:** [CLAUDE.md](claude-md.md) · [Agents / Subagents](agents.md)
