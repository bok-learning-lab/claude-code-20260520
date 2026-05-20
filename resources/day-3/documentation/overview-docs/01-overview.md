# Claude Code Overview

> Source: https://code.claude.com/docs/en/overview

Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.

Claude Code is an AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks. It understands your entire codebase and can work across multiple files and tools to get things done.

## Get started

Choose your environment to get started. Most surfaces require a [Claude subscription](https://claude.com/pricing) or [Anthropic Console](https://console.anthropic.com/) account.

### Terminal (CLI)

The full-featured CLI for working with Claude Code directly in your terminal. Edit files, run commands, and manage your entire project from the command line.

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Homebrew (macOS):**

```bash
brew install --cask claude-code
```

**WinGet (Windows):**

```powershell
winget install Anthropic.ClaudeCode
```

Then start Claude Code in any project:

```bash
cd your-project
claude
```

You'll be prompted to log in on first use.

### VS Code

The VS Code extension provides inline diffs, @-mentions, plan review, and conversation history directly in your editor. Search for "Claude Code" in the Extensions view (`Cmd+Shift+X` on Mac, `Ctrl+Shift+X` on Windows/Linux).

### Desktop App

A standalone app for running Claude Code outside your IDE or terminal. Review diffs visually, run multiple sessions side by side, schedule recurring tasks, and kick off cloud sessions.

- [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect) (Intel and Apple Silicon)
- [Windows](https://claude.ai/api/desktop/win32/x64/setup/latest/redirect) (x64)

### Web

Run Claude Code in your browser with no local setup at [claude.ai/code](https://claude.ai/code).

### JetBrains

A plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs.

## What you can do

- **Automate tedious tasks**: writing tests, fixing lint errors, resolving merge conflicts, updating dependencies, writing release notes
- **Build features and fix bugs**: describe what you want in plain language; Claude plans, writes code across multiple files, and verifies
- **Create commits and pull requests**: stages changes, writes commit messages, creates branches, and opens PRs
- **Connect your tools with MCP**: Model Context Protocol lets Claude read design docs, update tickets, pull data from Slack, etc.
- **Customize with instructions, skills, and hooks**: CLAUDE.md files, skills for repeatable workflows, hooks for automated actions
- **Run agent teams and build custom agents**: spawn multiple agents working in parallel, or build your own with the Agent SDK
- **Pipe, script, and automate with the CLI**: composable Unix-style tool for CI, pre-commit hooks, batch processing
- **Schedule recurring tasks**: routines on Anthropic infrastructure, desktop scheduled tasks, or `/loop` for quick polling

## Use Claude Code everywhere

Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them.

| I want to... | Best option |
|---|---|
| Continue a local session from my phone or another device | Remote Control |
| Start a task locally, continue on mobile | Web or Claude iOS app |
| Run Claude on a recurring schedule | Routines or Desktop scheduled tasks |
| Automate PR reviews and issue triage | GitHub Actions or GitLab CI/CD |
| Route bug reports from Slack to pull requests | Slack |
| Debug live web applications | Chrome extension |
| Build custom agents for your own workflows | Agent SDK |
