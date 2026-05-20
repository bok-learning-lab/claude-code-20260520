# Context Window

> **In one line:** The context window is the fixed amount of text Claude can hold in view at one time — it fills up, and when it does, Claude's performance degrades.

Claude's context window holds your entire conversation: every message you send, every file Claude reads, and every command output. This can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens.

When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. This is the single most important resource to manage in a Claude Code session.

**What fills the window:**
- Every message you send and every reply Claude gives
- Every file Claude reads (even if it only reads part of it)
- Output from every command Claude runs
- Your CLAUDE.md files (loaded at the start of every session)

**What you can do about it:**
- Use `/clear` to reset the context window entirely between unrelated tasks
- Use `/compact` to summarize a long conversation and continue in a leaner state
- Use subagents to offload research — they run in their own context windows
- Keep your CLAUDE.md short so it doesn't eat context at the start of every session

**See also:** [/clear](slash-clear.md) · [/compact](slash-compact.md) · [CLAUDE.md](claude-md.md) · [Agents / Subagents](agents.md)
