# Claude Code

> **In one line:** Claude Code is an agentic coding environment — Claude running in your terminal, able to read your files, run commands, and make changes to your project while you watch or step away.

Claude Code is fundamentally different from a chatbot. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.

This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.

**The most important thing to understand:** almost all best practices for Claude Code trace back to one constraint — Claude's context window fills up fast, and performance degrades as it fills. Claude's context window holds your entire conversation, including every message, every file Claude reads, and every command output. When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage.

**See also:** [Context Window](context-window.md) · [CLAUDE.md](claude-md.md) · [Skills](skills.md)
