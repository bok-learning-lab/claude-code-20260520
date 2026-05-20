# Sessions

> **In one line:** Claude Code saves conversations locally so you can pick up exactly where you left off — resume the most recent session with `claude --continue`, or choose from a list with `claude --resume`.

Claude Code saves conversations locally, so when a task spans multiple sittings you don't have to re-explain the context.

```bash
claude --continue    # pick up the most recent session
claude --resume      # choose from a list of saved sessions
```

Give sessions descriptive names so you can find them later. Run `/rename` inside a session to name it (e.g. `oauth-migration`). Treat named sessions like branches — each workstream gets its own persistent context.

**See also:** [/rename](slash-rename.md)
