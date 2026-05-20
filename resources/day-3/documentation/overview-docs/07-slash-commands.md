# Slash Commands Reference

> Source: https://code.claude.com/docs/en/commands

Commands control Claude Code from inside a session. Type `/` to see every command available, or type `/` followed by letters to filter.

---

## Commands across a typical workflow

**First session in a repo**: `/init` to generate CLAUDE.md, `/memory` to refine it, `/permissions` to set approval rules.

**During a task**: `/plan` for plan mode, `/model` and `/effort` to adjust reasoning, `/compact` to summarize context, `/btw` for a quick aside.

**Running work in parallel**: `/agents` to manage subagents, `/tasks` for background tasks, `/background` to detach a session.

**Before you ship**: `/diff` to see changes, `/simplify` for quality fixes, `/review` or `/security-review` for deeper passes.

**Between sessions**: `/clear` to start fresh, `/resume` to return to earlier conversations.

**When something is wrong**: `/rewind` to roll back, `/doctor` to diagnose issues.

---

## Most useful commands for beginners

| Command | Purpose |
|---|---|
| `/help` | Show help and available commands |
| `/init` | Initialize project with a CLAUDE.md guide |
| `/clear` | Start a new conversation with empty context |
| `/compact [instructions]` | Free up context by summarizing the conversation |
| `/context` | Visualize current context usage |
| `/diff` | Show uncommitted changes and per-turn diffs |
| `/doctor` | Diagnose and verify your installation |
| `/effort [level]` | Set model effort level (low, medium, high, xhigh, max) |
| `/export [filename]` | Export conversation as plain text |
| `/help` | Show help and available commands |
| `/memory` | Edit CLAUDE.md files and manage auto-memory |
| `/model [model]` | Set the AI model for the session |
| `/permissions` | Manage allow, ask, and deny rules |
| `/plan [description]` | Enter plan mode |
| `/resume [session]` | Resume a previous conversation |
| `/rewind` | Rewind conversation/code to a previous point |
| `/usage` | Show session cost and plan usage limits |

---

## All commands

| Command | Purpose |
|---|---|
| `/add-dir <path>` | Add a working directory for file access |
| `/agents` | Manage agent configurations |
| `/background [prompt]` | Detach session to run as background agent |
| `/batch <instruction>` | Orchestrate large-scale changes in parallel |
| `/branch [name]` | Create a branch of the current conversation |
| `/btw <question>` | Ask a quick side question without adding to conversation |
| `/chrome` | Configure Claude in Chrome settings |
| `/clear [name]` | Start a new conversation |
| `/color [color]` | Set prompt bar color for the session |
| `/compact [instructions]` | Summarize conversation to free context |
| `/config` | Open Settings interface |
| `/context [all]` | Visualize context usage |
| `/copy [N]` | Copy last assistant response to clipboard |
| `/debug [description]` | Enable debug logging and troubleshoot |
| `/desktop` | Continue session in Desktop app |
| `/diff` | Show uncommitted changes |
| `/doctor` | Diagnose installation |
| `/effort [level]` | Set model effort level |
| `/exit` | Exit the CLI |
| `/export [filename]` | Export conversation as text |
| `/fast [on\|off]` | Toggle fast mode |
| `/feedback [report]` | Submit feedback or report a bug |
| `/fewer-permission-prompts` | Auto-configure permission allowlist |
| `/goal [condition]` | Set a goal for Claude to work toward |
| `/hooks` | View hook configurations |
| `/init` | Initialize project CLAUDE.md |
| `/login` | Sign in |
| `/logout` | Sign out |
| `/loop [interval] [prompt]` | Run a prompt repeatedly |
| `/mcp` | Manage MCP server connections |
| `/memory` | Edit CLAUDE.md and auto-memory |
| `/model [model]` | Set the AI model |
| `/permissions` | Manage tool permissions |
| `/plan [description]` | Enter plan mode |
| `/plugin` | Manage plugins |
| `/powerup` | Discover features through interactive lessons |
| `/recap` | Generate one-line session summary |
| `/release-notes` | View changelog |
| `/remote-control` | Make session available for remote control |
| `/rename [name]` | Rename the current session |
| `/resume [session]` | Resume a conversation |
| `/review [PR]` | Review a pull request |
| `/rewind` | Rewind to a previous point |
| `/sandbox` | Toggle sandbox mode |
| `/schedule [description]` | Create/manage routines |
| `/security-review` | Analyze changes for security vulnerabilities |
| `/simplify [focus]` | Review changed files for quality issues |
| `/skills` | List available skills |
| `/status` | Show version, model, account info |
| `/theme` | Change color theme |
| `/ultrareview [PR]` | Deep multi-agent code review |
| `/usage` | Show session cost and usage |
| `/voice [mode]` | Toggle voice dictation |
