# Claude Official Documentation for Faculty Workshop

Reference documentation sourced from Anthropic's official Claude Code docs, covering internals and customization options in detail. These complement the [overview docs](../overview-docs/README.md) with more detailed, topic-specific material.

**When to use these**: After you're comfortable with the basics from the overview docs and want to understand *how things work under the hood* or *how to customize Claude Code* for your workflow.

---

## Table of Contents

### Reference & Discovery

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 1 | [Full Documentation Index](01-llms-txt-full-index.md) | Every page in Claude Code's documentation, organized by category (Core, Configuration, Extending, Tutorials, Reference, Platform) | When you're looking for a specific topic and aren't sure which doc covers it | [link](https://code.claude.com/docs/en/llms-full.txt) |

### Understanding the Engine

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 2 | [Context Window](02-context-window.md) | How Claude's ~200K token window works: what consumes tokens at startup, how conversations flow through the window, and what happens when it fills up (compaction) | When you notice Claude forgetting things, responses slowing down, or you want to understand why `/clear` and `/compact` matter | [link](https://code.claude.com/docs/en/context-window) |
| 7 | [Best Practices (Full)](07-best-practices-full.md) | The complete best practices guide: verification, planning, context management, session management, parallel workflows, and common failure patterns | When you want the comprehensive version of the best practices (the overview doc is a condensed version) | [link](https://code.claude.com/docs/en/best-practices) |

### Customizing Claude Code

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 3 | [Output Styles](03-output-styles.md) | Built-in styles (Default, Proactive, Explanatory, Learning) and how to create custom styles that change Claude's voice, tone, and format | When you want Claude to respond differently (more educational, more autonomous, diagram-first, etc.) | [link](https://code.claude.com/docs/en/output-styles) |
| 4 | [Path-Specific Rules](04-path-specific-rules.md) | Scoping instructions to specific file types or directories using `.claude/rules/` with glob patterns, so rules only load when relevant | When your CLAUDE.md is getting long and you want different rules for different parts of your codebase | [link](https://code.claude.com/docs/en/memory#path-specific-rules) |

### Extending & Scaling

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 5 | [Extending Claude Code](05-extending-claude-code.md) | The full extension layer: CLAUDE.md, Skills, Subagents, MCP, Hooks, and Plugins -- what each does, when to use it, and how they compare | When you want to connect Claude to external tools, automate repetitive workflows, or understand how all the extension features fit together | [link](https://code.claude.com/docs/en/features-overview) |
| 6 | [Subagents](06-subagents.md) | Built-in subagents (Explore, Plan, General-purpose), creating custom subagents, configuration options, and usage patterns (research, review, parallel, specialized worker) | When a side task is flooding your main conversation, or you want to run multiple tasks in parallel | [link](https://code.claude.com/docs/en/sub-agents) |

### Navigation

| File | What it covers |
|---|---|
| [Learning Progression](learning-progression.md) | Decision tree and cycle diagram showing which document to reach for based on where you are in your Claude Code journey |

---

## Quick Links to Official Documentation

- **Claude Code docs**: https://code.claude.com/docs/en/overview
- **Full documentation index**: https://code.claude.com/docs/en/llms-full.txt
- **Claude platform docs**: https://platform.claude.com/docs
- **Community Discord**: https://www.anthropic.com/discord

---

## Suggested Reading Order

1. **Start here**: [Context Window](02-context-window.md) -- understanding this one concept explains most of Claude Code's behavior
2. **Then**: [Best Practices (Full)](07-best-practices-full.md) -- the complete playbook for getting good results
3. **When customizing**: [Output Styles](03-output-styles.md) and [Path-Specific Rules](04-path-specific-rules.md) -- quick wins for tailoring Claude to your needs
4. **When scaling up**: [Extending Claude Code](05-extending-claude-code.md) and [Subagents](06-subagents.md) -- the power-user features
5. **As a reference**: [Full Documentation Index](01-llms-txt-full-index.md) -- when you need to find something specific

---

## How These Relate to the Overview Docs

The [overview docs](../overview-docs/README.md) cover the breadth of Claude Code: what it is, how to start, common commands, and settings. These official docs go deeper on specific topics:

| If you read this overview doc... | ...go deeper with |
|---|---|
| [Best Practices](../overview-docs/03-best-practices.md) | [Best Practices (Full)](07-best-practices-full.md) for the complete version |
| [Memory & CLAUDE.md](../overview-docs/05-memory-claude-md.md) | [Path-Specific Rules](04-path-specific-rules.md) for scoped rules, [Extending Claude Code](05-extending-claude-code.md) for Skills and Hooks |
| [Settings](../overview-docs/08-settings.md) | [Output Styles](03-output-styles.md) for custom response formats |
| [Slash Commands](../overview-docs/07-slash-commands.md) | [Context Window](02-context-window.md) to understand *why* `/clear` and `/compact` matter |
