# Claude Code Documentation Index (llms.txt)

> Source: https://code.claude.com/docs/llms.txt
>
> This is the complete machine-readable index of every page in the Claude Code documentation. Use it to discover what documentation exists and find the right page for any topic.

## Core Documentation

- [Overview](https://code.claude.com/docs/en/overview.md): Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools.
- [Quickstart](https://code.claude.com/docs/en/quickstart.md): Welcome to Claude Code!
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works.md): Understand the agentic loop, built-in tools, and how Claude Code interacts with your project.
- [Best practices](https://code.claude.com/docs/en/best-practices.md): Tips and patterns for getting the most out of Claude Code.
- [Common workflows](https://code.claude.com/docs/en/common-workflows.md): Step-by-step guides for exploring codebases, fixing bugs, refactoring, testing, and other everyday tasks.

## Configuration & Setup

- [Settings](https://code.claude.com/docs/en/settings.md): Configure Claude Code with global and project-level settings.
- [Memory (CLAUDE.md)](https://code.claude.com/docs/en/memory.md): Give Claude persistent instructions with CLAUDE.md files, and auto memory.
- [Authentication](https://code.claude.com/docs/en/authentication.md): Log in and configure authentication for individuals, teams, and organizations.
- [Advanced setup](https://code.claude.com/docs/en/setup.md): System requirements, platform-specific installation, version management.
- [Environment variables](https://code.claude.com/docs/en/env-vars.md): Reference for environment variables that control Claude Code behavior.
- [Permissions](https://code.claude.com/docs/en/permissions.md): Control what Claude Code can access and do.
- [Permission modes](https://code.claude.com/docs/en/permission-modes.md): Control whether Claude asks before editing files or running commands.
- [Sandboxing](https://code.claude.com/docs/en/sandboxing.md): Filesystem and network isolation for safer agent execution.

## Extending Claude Code

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview.md): Understand when to use CLAUDE.md, Skills, subagents, hooks, MCP, and plugins.
- [Skills](https://code.claude.com/docs/en/skills.md): Create, manage, and share skills to extend Claude's capabilities.
- [Subagents](https://code.claude.com/docs/en/sub-agents.md): Create and use specialized AI subagents for task-specific workflows.
- [Hooks reference](https://code.claude.com/docs/en/hooks.md): Hook events, configuration schema, and JSON formats.
- [Hooks guide](https://code.claude.com/docs/en/hooks-guide.md): Run shell commands automatically when Claude edits files, finishes tasks, or needs input.
- [MCP](https://code.claude.com/docs/en/mcp.md): Connect Claude Code to your tools with the Model Context Protocol.
- [Plugins](https://code.claude.com/docs/en/plugins.md): Create custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers.
- [Output styles](https://code.claude.com/docs/en/output-styles.md): Adapt Claude Code for uses beyond software engineering.

## References

- [CLI reference](https://code.claude.com/docs/en/cli-reference.md): Complete CLI reference including commands and flags.
- [Commands](https://code.claude.com/docs/en/commands.md): Complete reference for slash commands.
- [Tools reference](https://code.claude.com/docs/en/tools-reference.md): Complete reference for tools Claude Code can use.
- [Glossary](https://code.claude.com/docs/en/glossary.md): Definitions for Claude Code terminology.
- [Error reference](https://code.claude.com/docs/en/errors.md): Runtime error messages and how to fix them.

## Context & Performance

- [Context window](https://code.claude.com/docs/en/context-window.md): Interactive simulation of how the context window fills during a session.
- [Costs](https://code.claude.com/docs/en/costs.md): Track token usage, set limits, and reduce costs.
- [Prompt caching](https://code.claude.com/docs/en/prompt-caching.md): How Claude Code manages prompt caching automatically.
- [Model configuration](https://code.claude.com/docs/en/model-config.md): Model aliases, effort levels, and model selection.

## Interfaces

- [VS Code](https://code.claude.com/docs/en/vs-code.md): Install and configure the Claude Code extension for VS Code.
- [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains.md): Use Claude Code with IntelliJ, PyCharm, WebStorm, and more.
- [Desktop app](https://code.claude.com/docs/en/desktop.md): Parallel sessions, drag-and-drop layout, integrated terminal, Dispatch.
- [Web](https://code.claude.com/docs/en/claude-code-on-the-web.md): Run Claude Code in the cloud from your browser or phone.
- [Chrome](https://code.claude.com/docs/en/chrome.md): Connect Claude Code to Chrome for web app testing and debugging.
- [Slack](https://code.claude.com/docs/en/slack.md): Delegate coding tasks from your Slack workspace.
- [Interactive mode](https://code.claude.com/docs/en/interactive-mode.md): Keyboard shortcuts, input modes, and interactive features.

## Parallelism & Automation

- [Agent view](https://code.claude.com/docs/en/agent-view.md): Dispatch and manage many sessions from one screen.
- [Agent teams](https://code.claude.com/docs/en/agent-teams.md): Coordinate multiple Claude Code instances working together.
- [Run agents in parallel](https://code.claude.com/docs/en/agents.md): Compare subagents, agent view, agent teams, and worktrees.
- [Worktrees](https://code.claude.com/docs/en/worktrees.md): Isolate parallel sessions in separate git worktrees.
- [Headless / non-interactive](https://code.claude.com/docs/en/headless.md): Run Claude Code programmatically.
- [Routines](https://code.claude.com/docs/en/routines.md): Automate work on Anthropic-managed cloud infrastructure.
- [GitHub Actions](https://code.claude.com/docs/en/github-actions.md): Integrate Claude Code into CI/CD.
- [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd.md): Claude Code with GitLab.
- [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks.md): Run prompts on a schedule with /loop and cron.

## Session Management

- [Checkpointing](https://code.claude.com/docs/en/checkpointing.md): Track, rewind, and summarize session state.
- [Remote Control](https://code.claude.com/docs/en/remote-control.md): Continue local sessions from any device.

## Agent SDK

- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview.md): Build production AI agents with Claude Code as a library.
- [SDK quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart.md): Get started with the Python or TypeScript Agent SDK.
- [Python reference](https://code.claude.com/docs/en/agent-sdk/python.md): Complete API reference for the Python Agent SDK.
- [TypeScript reference](https://code.claude.com/docs/en/agent-sdk/typescript.md): Complete API reference for the TypeScript Agent SDK.

## Enterprise & Security

- [Admin setup](https://code.claude.com/docs/en/admin-setup.md): A decision map for administrators deploying Claude Code.
- [Security](https://code.claude.com/docs/en/security.md): Security safeguards and best practices.
- [Data usage](https://code.claude.com/docs/en/data-usage.md): Anthropic's data usage policies for Claude.
- [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock.md): Configure Claude Code through Amazon Bedrock.
- [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai.md): Configure Claude Code through Google Vertex AI.
- [Network config](https://code.claude.com/docs/en/network-config.md): Proxy servers, custom CAs, and mTLS.

## Troubleshooting

- [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install.md): Fix command not found, PATH, permission, and auth errors.
- [Troubleshooting](https://code.claude.com/docs/en/troubleshooting.md): Fix high CPU, memory, hangs, and other runtime issues.
- [Debug your config](https://code.claude.com/docs/en/debug-your-config.md): Diagnose why CLAUDE.md, settings, hooks, or MCP aren't working.
