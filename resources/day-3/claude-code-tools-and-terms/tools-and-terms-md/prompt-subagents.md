# Use subagents for investigation

> **Delegate research to subagents so the exploration doesn't consume your main context.**

Since context is your fundamental constraint, subagents are one of the most powerful tools available. When Claude researches a codebase it reads lots of files — all of which consume your context. Subagents run in separate context windows and report back summaries:

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

The subagent explores the codebase, reads relevant files, and reports back with findings — without cluttering your main conversation.

You can also use subagents for verification after Claude implements something:

```
use a subagent to review this code for edge cases
```

**See also:** [Agents / Subagents](agents.md) · [Context Window](context-window.md)
