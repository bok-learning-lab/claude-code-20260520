# /init

> **In one line:** `/init` generates a starter CLAUDE.md file for your current project by analyzing your codebase.

Running `/init` makes Claude analyze your project to detect build systems, test frameworks, and code patterns, then creates a CLAUDE.md with build commands, test instructions, and project conventions it discovers.

If a CLAUDE.md already exists, `/init` suggests improvements rather than overwriting it.

Set `CLAUDE_CODE_NEW_INIT=1` to enable an interactive multi-phase flow. `/init` asks which artifacts to set up (CLAUDE.md files, skills, hooks), explores your codebase with a subagent, fills in gaps via follow-up questions, and presents a reviewable proposal before writing any files.

**See also:** [CLAUDE.md](claude-md.md)
