# Agents / Subagents (`.claude/agents/`)

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

**See also:** [Skills](skills.md) · [Context Window](context-window.md) · [Use subagents for investigation](prompt-subagents.md)
