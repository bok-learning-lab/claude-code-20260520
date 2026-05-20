# Auto Memory

> **In one line:** Auto memory is a feature where Claude automatically saves notes about your project and preferences across sessions — without you writing anything.

Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself as it works: build commands, debugging insights, architecture notes, code style preferences, and workflow habits. Claude doesn't save something every session — it decides what's worth remembering based on whether the information would be useful in a future conversation.

**Where it lives:** Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The directory contains a `MEMORY.md` entrypoint and optional topic files:

```
~/.claude/projects/<project>/memory/
├── MEMORY.md          # Concise index, loaded into every session
├── debugging.md       # Detailed notes on debugging patterns
├── api-conventions.md # API design decisions
└── ...
```

The first 200 lines of `MEMORY.md` are loaded at the start of every conversation. Claude keeps it concise by moving detailed notes into separate topic files, which it reads on demand.

**How CLAUDE.md and auto memory differ:**

| | CLAUDE.md | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| What it contains | Instructions and rules | Learnings and patterns Claude discovered |
| Use for | Coding standards, workflows, project architecture | Build commands, debugging insights, preferences Claude found |

**To see what Claude has saved:** run `/memory`. Everything is plain markdown you can read, edit, or delete at any time.

**To turn it off:** open `/memory` and use the auto memory toggle, or add `"autoMemoryEnabled": false` to your project settings.

**See also:** [CLAUDE.md](claude-md.md) · [/memory](slash-memory.md)
