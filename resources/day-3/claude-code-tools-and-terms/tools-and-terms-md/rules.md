# Rules (`.claude/rules/`)

> **In one line:** Rules are instruction files in `.claude/rules/` — a way to organize project instructions into separate topic files instead of one long CLAUDE.md.

For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain.

```
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Code style guidelines
│       ├── testing.md      # Testing conventions
│       └── security.md     # Security requirements
```

Place markdown files in `.claude/rules/`. Each file should cover one topic, with a descriptive filename. All `.md` files are discovered recursively, so you can organize rules into subdirectories.

Rules without a `paths` field (see below) are loaded at launch alongside CLAUDE.md.

**Rules vs. skills:** Rules load into context every session, or when matching files are opened. For task-specific instructions that don't need to be in context all the time, use skills instead — skills only load when you invoke them or when Claude determines they're relevant.

**See also:** [CLAUDE.md](claude-md.md) · [Path-Specific Rules](path-specific-rules.md) · [Skills](skills.md)
