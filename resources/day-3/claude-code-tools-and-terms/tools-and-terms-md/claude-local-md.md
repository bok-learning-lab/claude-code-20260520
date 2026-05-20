# CLAUDE.local.md

> **In one line:** CLAUDE.local.md is a personal, private version of CLAUDE.md for one project — for notes you don't want to share with your team via git.

CLAUDE.local.md sits alongside CLAUDE.md at the project root and is loaded in the same way. The difference: it's meant for personal preferences that shouldn't be checked into version control. Add it to your `.gitignore`.

Use it for things like:
- Your local sandbox URLs
- Preferred test data you use personally
- Shortcuts specific to your machine setup

When you run `/init` and choose the personal option, it creates CLAUDE.local.md and adds it to `.gitignore` for you.

**See also:** [CLAUDE.md](claude-md.md)
