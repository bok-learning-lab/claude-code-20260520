# Claude Code Documentation for Faculty Workshop

Reference documentation assembled for the Claude Code for Faculty workshop. These files are condensed versions of the official Anthropic documentation, organized for quick reference as you learn and use Claude Code.

**Workshop context**: Day 1 introduced LLMs and Claude. Day 2 covered setup (Homebrew, Git, npm, VS Code, and the Claude Code CLI). Days 3-4 focus on hands-on use.

---

## Table of Contents

### Getting Started

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 1 | [Overview](01-overview.md) | What Claude Code is, how to install it across platforms (terminal, VS Code, desktop, web), and a summary of everything it can do | First thing to read; the "what is this and what can it do" overview | [link](https://code.claude.com/docs/en/overview) |
| 2 | [Quickstart](02-quickstart.md) | Step-by-step first session: install, log in, ask questions, make edits, use Git, fix bugs | Walking through your very first Claude Code session | [link](https://code.claude.com/docs/en/quickstart) |
| 3 | [Best Practices](03-best-practices.md) | Proven patterns: how to verify work, plan before coding, provide context, manage sessions, and avoid common mistakes | After your first session, when you want to get better results and work more efficiently | [link](https://code.claude.com/docs/en/best-practices) |

### Day-to-Day Usage

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 4 | [Common Workflows](04-common-workflows.md) | Recipes for exploring codebases, fixing bugs, refactoring, writing tests, creating PRs, working with images, and running scheduled tasks | When you have a specific task and want to see how others approach it with Claude Code | [link](https://code.claude.com/docs/en/common-workflows) |
| 5 | [Memory & CLAUDE.md](05-memory-claude-md.md) | How to give Claude persistent project instructions (CLAUDE.md files) and how auto-memory works across sessions | When you want Claude to remember your project's conventions, build commands, or coding standards | [link](https://code.claude.com/docs/en/memory) |

### Reference

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 6 | [CLI Reference](06-cli-reference.md) | All terminal commands (`claude`, `claude -p`, `claude -c`, etc.) and flags (`--model`, `--effort`, `--worktree`, etc.) | When you need to look up a specific command-line option or flag | [link](https://code.claude.com/docs/en/cli-usage) |
| 7 | [Slash Commands](07-slash-commands.md) | All `/` commands available inside a Claude Code session (`/init`, `/clear`, `/plan`, `/memory`, `/compact`, etc.) | When you're inside Claude Code and want to know what slash commands are available | [link](https://code.claude.com/docs/en/commands) |
| 8 | [Settings](08-settings.md) | Configuration scopes (user, project, local, managed), permissions, sandbox settings, and example config files | When you want to customize Claude Code's behavior, set up permissions, or configure for a team | [link](https://code.claude.com/docs/en/settings) |

### Prompting

| # | File | What it covers | When to reference it | Official docs |
|---|---|---|---|---|
| 9 | [Prompt Engineering](09-prompt-engineering.md) | How to write effective prompts: clarity, examples, XML tags, roles, tool use, thinking, and agentic patterns | When you want to understand how to communicate more effectively with Claude, both in Claude Code and in general | [link](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices) |

---

## Quick Links to Official Documentation

- **Claude Code docs**: https://code.claude.com/docs/en/overview
- **Claude platform docs**: https://platform.claude.com/docs
- **Claude Code product page**: https://code.claude.com
- **Community Discord**: https://www.anthropic.com/discord

---

## Suggested Reading Order

1. **First**: [Overview](01-overview.md) and [Quickstart](02-quickstart.md) to get oriented
2. **Next**: [Best Practices](03-best-practices.md) -- the single most useful doc for improving your experience
3. **As needed**: [Common Workflows](04-common-workflows.md) for specific task patterns
4. **When customizing**: [Memory & CLAUDE.md](05-memory-claude-md.md) and [Settings](08-settings.md)
5. **For reference**: [CLI Reference](06-cli-reference.md) and [Slash Commands](07-slash-commands.md) when you need to look something up
6. **Going deeper**: [Prompt Engineering](09-prompt-engineering.md) for advanced prompting techniques
