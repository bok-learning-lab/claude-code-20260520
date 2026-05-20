# Path-Specific Rules

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

**See also:** [Rules](rules.md) · [Context Window](context-window.md)
