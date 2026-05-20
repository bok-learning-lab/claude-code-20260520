# CLI Reference

> Source: https://code.claude.com/docs/en/cli-usage

Complete reference for the Claude Code command-line interface, including commands and flags.

---

## CLI Commands

| Command | Description | Example |
|---|---|---|
| `claude` | Start interactive session | `claude` |
| `claude "query"` | Start session with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session>" "query"` | Resume session by ID or name | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude auth login` | Sign in to your Anthropic account | `claude auth login --console` |
| `claude auth logout` | Log out from your account | `claude auth logout` |
| `claude auth status` | Show authentication status | `claude auth status` |
| `claude mcp` | Configure MCP servers | See MCP documentation |
| `claude agents` | Open agent view for background sessions | `claude agents --json` |

---

## Key CLI Flags

| Flag | Description | Example |
|---|---|---|
| `--add-dir` | Add additional working directories | `claude --add-dir ../apps ../lib` |
| `--allowedTools` | Tools that execute without permission prompts | `"Bash(git log *)" "Read"` |
| `--append-system-prompt` | Append custom text to system prompt | `claude --append-system-prompt "Always use TypeScript"` |
| `--continue`, `-c` | Load the most recent conversation | `claude --continue` |
| `--dangerously-skip-permissions` | Skip permission prompts (use with caution) | `claude --dangerously-skip-permissions` |
| `--effort` | Set effort level: low, medium, high, xhigh, max | `claude --effort high` |
| `--model` | Set model for the session | `claude --model claude-sonnet-4-6` |
| `--name`, `-n` | Set a display name for the session | `claude -n "my-feature-work"` |
| `--output-format` | Output format for print mode: text, json, stream-json | `claude -p "query" --output-format json` |
| `--permission-mode` | Start in a permission mode: default, acceptEdits, plan, auto | `claude --permission-mode plan` |
| `--print`, `-p` | Print response without interactive mode | `claude -p "query"` |
| `--resume`, `-r` | Resume a specific session | `claude --resume auth-refactor` |
| `--verbose` | Enable verbose logging | `claude --verbose` |
| `--version`, `-v` | Output the version number | `claude -v` |
| `--worktree`, `-w` | Start in an isolated git worktree | `claude -w feature-auth` |

---

## System prompt flags

| Flag | Behavior | Example |
|---|---|---|
| `--system-prompt` | Replace the entire default prompt | `claude --system-prompt "You are a Python expert"` |
| `--system-prompt-file` | Replace with file contents | `claude --system-prompt-file ./prompts/review.txt` |
| `--append-system-prompt` | Append to the default prompt | `claude --append-system-prompt "Always use TypeScript"` |
| `--append-system-prompt-file` | Append file contents to default prompt | `claude --append-system-prompt-file ./style-rules.txt` |

Use an **append** flag when Claude should remain a coding assistant that also follows your extra rules. Use a **replacement** flag when the identity or permission model differs from Claude Code's defaults.
