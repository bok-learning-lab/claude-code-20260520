# Hooks

> **In one line:** Hooks are shell commands that run automatically at specific points in Claude's workflow — they're deterministic, unlike CLAUDE.md instructions which Claude may or may not follow.

Hooks run scripts automatically at specific points in Claude's workflow. Unlike CLAUDE.md instructions which are advisory (Claude reads them and tries to follow them), hooks are deterministic and guarantee the action happens.

Claude can write hooks for you. Try prompts like:
- *"Write a hook that runs eslint after every file edit"*
- *"Write a hook that blocks writes to the migrations folder."*

Edit `.claude/settings.json` directly to configure hooks by hand, and run `/hooks` to browse what's configured.

**Hooks vs. CLAUDE.md:** If an instruction is something that must run at a specific point — before every commit, after each file edit — write it as a hook. Hooks execute as shell commands at fixed lifecycle events and apply regardless of what Claude decides to do.

**See also:** [CLAUDE.md](claude-md.md)
