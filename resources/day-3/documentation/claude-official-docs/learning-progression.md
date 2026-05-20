# When Do I Need Which Document?

Here's a guide to developing intuitions about which documentation in this folder to reach for as you use Claude Code.

---

## Decision Tree

```
I need help with Claude Code. What should I read?

├── I've never used it before
│   └── Overview → Quickstart → Best Practices
│
├── I'm using it but want better results
│   ├── Claude's output quality is declining mid-session
│   │   └── Context Window (02)
│   ├── Claude doesn't follow my project's rules
│   │   └── Memory & CLAUDE.md (overview 05) → Path Rules (04)
│   ├── I want Claude to respond differently
│   │   └── Output Styles (03)
│   └── I want Claude to do more automatically
│       └── Extending Claude Code (05)
│
├── I have a specific task pattern to optimize
│   ├── Research is flooding my context
│   │   └── Subagents (06)
│   ├── I keep repeating the same setup
│   │   └── Extending Claude Code (05)
│   └── I need to look up a command or flag
│       └── CLI Reference (overview 06) / Slash Commands (overview 07)
│
└── I want to master it or teach others
    └── Best Practices Full (07) + Full Index (01)
```

---

## The Learning Cycle

New users typically move through these phases, cycling back as they take on new kinds of tasks.

```
                    ┌─────────────────────────────────┐
                    │                                  │
                    ▼                                  │
           ┌──────────────┐                            │
           │   GETTING    │  Overview docs:            │
           │   STARTED    │  01-Overview, 02-Quickstart │
           └──────┬───────┘                            │
                  │                                    │
                  ▼                                    │
           ┌──────────────┐                            │
           │   FIRST      │  Overview: 03-Best Practices│
           │   SESSIONS   │  Overview: 04-Workflows    │
           └──────┬───────┘                            │
                  │                                    │
        ┌─────────┼─────────┐                          │
        ▼         ▼         ▼                          │
   ┌─────────┐ ┌────────┐ ┌─────────┐                 │
   │ "Why is │ │ "How   │ │ "I keep │                 │
   │ Claude  │ │ do I   │ │ typing  │                 │
   │ forget- │ │ make   │ │ the     │                 │
   │ ting?"  │ │ Claude │ │ same    │                 │
   │         │ │ follow │ │ thing"  │                 │
   │ Context │ │ my     │ │         │                 │
   │ Window  │ │ rules?"│ │ Extend- │                 │
   │ (02)    │ │        │ │ ing CC  │                 │
   │         │ │ Path   │ │ (05)    │                 │
   │         │ │ Rules  │ │         │                 │
   │         │ │ (04)   │ │ Sub-    │                 │
   │         │ │        │ │ agents  │                 │
   │         │ │ Output │ │ (06)    │                 │
   │         │ │ Styles │ │         │                 │
   │         │ │ (03)   │ │         │                 │
   └────┬────┘ └───┬────┘ └────┬────┘                 │
        │          │           │                       │
        └──────────┼───────────┘                       │
                   ▼                                   │
           ┌──────────────┐                            │
           │  LEVELING UP │  Best Practices Full (07)  │
           │              │  Full Doc Index (01)       │
           └──────┬───────┘                            │
                  │                                    │
                  │   New project, new language,       │
                  │   new team member joins...         │
                  └────────────────────────────────────┘
```

---

## Phase-by-Phase Guide

### Phase 1: Getting Started
**You're here when**: You just installed Claude Code and want to know what it can do.

| Reach for | When |
|---|---|
| [Overview](../overview-docs/01-overview.md) | "What is this thing?" |
| [Quickstart](../overview-docs/02-quickstart.md) | "How do I use it for the first time?" |

### Phase 2: First Real Sessions
**You're here when**: You're using Claude Code on real tasks and want to get better results.

| Reach for | When |
|---|---|
| [Best Practices](../overview-docs/03-best-practices.md) | "How do I get better output?" |
| [Common Workflows](../overview-docs/04-common-workflows.md) | "How do people typically do X?" |
| [Slash Commands](../overview-docs/07-slash-commands.md) | "What commands are available?" |
| [CLI Reference](../overview-docs/06-cli-reference.md) | "What flags can I pass?" |

### Phase 3: Hitting Walls
**You're here when**: Something isn't working the way you expect, or you're doing the same thing over and over.

| Symptom | Document | Why |
|---|---|---|
| Claude forgets things mid-conversation, gets slow, or gives worse answers over time | [Context Window](02-context-window.md) | Understanding token limits explains why `/clear` and `/compact` exist |
| Claude doesn't follow your project's conventions | [Memory & CLAUDE.md](../overview-docs/05-memory-claude-md.md) then [Path-Specific Rules](04-path-specific-rules.md) | First set up persistent instructions, then scope them to specific file types |
| Claude's responses are too terse / too verbose / wrong tone | [Output Styles](03-output-styles.md) | Change how Claude communicates without changing what it knows |
| You keep typing the same setup instructions | [Extending Claude Code](05-extending-claude-code.md) | Skills, Hooks, and MCP eliminate repetitive prompting |
| Research tasks flood your conversation | [Subagents](06-subagents.md) | Delegate exploration to a separate context window |

### Phase 4: Leveling Up
**You're here when**: You're comfortable and want to master the tool or help others learn it.

| Reach for | When |
|---|---|
| [Best Practices (Full)](07-best-practices-full.md) | You want the complete playbook, including parallel sessions and failure patterns |
| [Full Documentation Index](01-llms-txt-full-index.md) | You want to find a specific topic or discover features you haven't tried |

### The Cycle Repeats
Every time you start a new project, or switch languages, you'll find yourself back in Phase 1-2 for that new context. 
