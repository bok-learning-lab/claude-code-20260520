# CLAUDE.md — Project Instructions

This file is read by Claude Code at the start of every session in this project. Use it to document project context, conventions, and standing instructions.

---

## Project Overview

[Describe what this project is for, who it's for, and what problem it solves.]

## Folder Structure

```
my-project/
  inputs/                   # Raw materials Claude should read
  outputs/                  # Where Claude writes finished files
  operations-tools-commands/ # Scripts, prompts, and reusable operations

resources/
  cheatsheets/              # Quick-reference docs (markdown cheatsheet, etc.)
  checklists/               # Setup and onboarding checklists
  glossary-md/              # Term-by-term glossary in markdown
  glossary-html/            # Term-by-term glossary rendered as HTML

documentation/
  sample-prompts/           # Example prompts to use with Claude

.claude/
  commands/                 # Project-level slash commands (user-invokable)
  agents/                   # Custom subagent definitions (Claude-invokable)
```

## Conventions

- **Inputs go in `my-project/inputs/`** before asking Claude to work with them.
- **Outputs go in `my-project/outputs/`** — Claude should write finished files here unless told otherwise.
- **Operations and reusable prompts** live in `my-project/operations-tools-commands/`.

## Slash Commands (`.claude/commands/`)

Files here become available as `/command-name` in this project. Each `.md` file is the instruction set for that command. See `skill-creator.md` for the official guide to writing new skills.

## Agents (`.claude/agents/`)

Files here define custom subagents Claude can spawn with the Agent tool. Each `.md` file needs YAML frontmatter (`name`, `description`, `model`, `color`) and a system prompt body. See `example-agent.md` for the template.

## Standing Instructions

[Add any standing preferences here — tone, output format, what to avoid, etc.]
