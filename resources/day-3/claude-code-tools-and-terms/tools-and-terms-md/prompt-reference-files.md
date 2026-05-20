# Reference files with @

> **Use `@` to pull files into context directly — Claude reads the file before responding.**

Instead of describing where code lives, use `@` to reference it:

```
look at @src/api/handlers/user.ts and follow the same pattern for a new /orders handler
```

You can also:
- **Paste images directly** — copy/paste or drag and drop screenshots into the prompt
- **Give URLs** for documentation and API references
- **Pipe in data** — run `cat error.log | claude` to send file contents directly
- **Let Claude fetch what it needs** — tell Claude to pull context itself using Bash commands, MCP tools, or by reading files
