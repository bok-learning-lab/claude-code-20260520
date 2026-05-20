# Explore the context window

> Source: https://code.claude.com/docs/en/context-window
>
> An interactive simulation of how Claude Code's context window fills during a session. This document captures the full data from that interactive page — every event, token cost, description, and tip.

The context window holds everything Claude can "see": your conversation, every file it reads, every command output. Claude's context window is approximately **200,000 tokens**. When it fills up, performance degrades — Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage.

The [original page](https://code.claude.com/docs/en/context-window) is an interactive simulation you can play through. This document captures all the data from that simulation so you can reference it offline.

---

## What loads at startup (before you type anything)

When you start a Claude Code session, several things load automatically. These are **invisible in your terminal** — you don't see them, but they consume context.

| Order | What loads | Tokens | Visibility | Description |
|---|---|---|---|---|
| 1 | System prompt | ~4,200 | Invisible | Core instructions for behavior, tool use, and response formatting. Always loaded first. You never see it. |
| 2 | Auto memory (MEMORY.md) | ~680 | Invisible | Claude's notes to itself from previous sessions: build commands it learned, patterns it noticed, mistakes to avoid. The first 200 lines or 25KB, whichever comes first, are loaded into the conversation context. |
| 3 | Environment info | ~280 | Invisible | Working directory, platform, shell, OS version, and whether this is a git repo. Git branch, status, and recent commits load as a separate block at the very end of the system prompt. |
| 4 | MCP tools (deferred) | ~120 | Invisible | MCP tool names listed so Claude knows what is available. By default, full schemas stay deferred and Claude loads specific ones on demand via tool search when a task needs them. Set `ENABLE_TOOL_SEARCH=auto` to load schemas upfront when they fit within 10% of the context window, or `ENABLE_TOOL_SEARCH=false` to load everything. |
| 5 | Skill descriptions | ~450 | Invisible | One-line descriptions of available skills so Claude knows what it can invoke. Full skill content loads only when Claude actually uses one. Skills with `disable-model-invocation: true` are not in this list. They stay completely out of context until you invoke them with `/name`. **Unlike the rest of the startup content, this listing is not re-injected after `/compact`.** Only skills you actually invoked get preserved. |
| 6 | ~/.claude/CLAUDE.md | ~320 | Invisible | Your global preferences. Applies to every project. Loaded alongside project instructions at the start of every conversation. |
| 7 | Project CLAUDE.md | ~1,800 | Invisible | Project conventions, build commands, architecture notes. The most important file you can create. Lives in your project root, so your whole team gets the same instructions. |

> **Tip:** Keep CLAUDE.md under 200 lines. Move reference content to skills or path-scoped rules so it only loads when needed.

**Total startup cost**: roughly **8,000–10,000 tokens** before you type anything.

---

## A complete session walkthrough

The interactive simulation walks through a realistic debugging session. Here's every event, in order, with token costs and what you see vs. what only Claude sees.

### Phase 1: Your first prompt

| Event | Tokens | You see | Description |
|---|---|---|---|
| Your prompt: "Fix the auth bug where users get 401 after token refresh" | 45 | Full text | Your prompt appears in the terminal. |

### Phase 2: Claude investigates

| Event | Tokens | You see | Description |
|---|---|---|---|
| Read `src/api/auth.ts` | 2,400 | One-liner | Main auth file. You see "Read auth.ts" in your terminal, but the 2,400 tokens of file content only Claude sees. |
| Read `src/lib/tokens.ts` | 1,100 | One-liner | Following imports to the token module. Shown as a one-liner in your terminal. |
| **Rule fires:** `api-conventions.md` | 380 | One-liner | This rule in `.claude/rules/` has a `paths:` pattern matching `src/api/**`. It loaded automatically when Claude read a file in that directory. You see "Loaded .claude/rules/api-conventions.md" in your terminal, but not the rule content. |
| Read `middleware.ts` | 1,800 | One-liner | Tracing the auth flow deeper. |
| Read `auth.test.ts` | 1,600 | One-liner | Checking existing tests for expected behavior. |
| **Rule fires:** `testing.md` | 290 | One-liner | Another path-scoped rule, this one matching `*.test.ts` files. Triggered when Claude read auth.test.ts. Shown as a one-line "Loaded" notice. |
| `grep "refreshToken"` | 600 | One-liner | Search results across the codebase. You see the command ran, not the full output. |

> **Tip:** File reads dominate context usage. Be specific in prompts ("fix the bug in auth.ts") so Claude reads fewer files. For research-heavy tasks, use a subagent.

### Phase 3: Claude responds and fixes

| Event | Tokens | You see | Description |
|---|---|---|---|
| Claude's analysis | 800 | Full text | Explains the bug: token invalidated too early in the rotation. This text appears in your terminal. |
| Edit `auth.ts` | 400 | Full diff | Fixes the token rotation order. The diff appears in your terminal. |
| **Hook: prettier** | 120 | Nothing | A `PostToolUse` hook in `settings.json` runs prettier after every file edit and reports back via `hookSpecificOutput.additionalContext`. That field enters Claude's context. Plain stdout on exit 0 does not — it is written to the debug log only. |
| Edit `auth.test.ts` | 600 | Full diff | Adds a regression test for the fix. The diff appears in your terminal. |
| **Hook: prettier** | 100 | Nothing | The same hook fires again for the test file. Every matching tool event triggers it. |
| `npm test` output | 1,200 | One-liner | Runs the test suite. You see "Running npm test..." and the pass count, not the full 1,200 tokens of output. |
| Summary | 400 | Full text | "Fixed token rotation. Added regression test. All tests pass." |

> **Tip:** Output JSON with `additionalContext` to send info to Claude from hooks. For `PostToolUse` hooks, exit code 2 surfaces stderr as an error but cannot block since the tool already ran. Keep output concise since it enters context without truncation.

### Phase 4: Follow-up with a subagent

| Event | Tokens (main) | Tokens (subagent) | Description |
|---|---|---|---|
| Your follow-up: "Use a subagent to research session timeout handling, then fix it" | 40 | — | Follow-ups add to the same context. Delegating research to a subagent keeps large file reads out of your main window. |
| Spawn research subagent | 80 | — | Claude delegates the research to a subagent with a fresh, separate context window. It loads CLAUDE.md and the same MCP and skill setup, but starts without your conversation history or the main session's auto memory. |
| *Subagent: System prompt* | 0 | 900 | The subagent gets its own system prompt, shorter than the main session's. The main session's auto memory is not included. If a custom agent has `memory:` in its frontmatter, it loads its own separate MEMORY.md here instead. |
| *Subagent: Project CLAUDE.md (own copy)* | 0 | 1,800 | The subagent loads CLAUDE.md too. Same file, same content, but it counts against the subagent's context, not yours. The built-in Explore and Plan agents skip this for a smaller context. |
| *Subagent: MCP tools + skills* | 0 | 970 | The subagent has access to the same MCP servers and skills. It gets most of the parent's tools, minus several that don't apply in a nested context, including plan-mode controls, background-task tools, and by default the Agent tool itself to prevent recursion. |
| *Subagent: Task prompt from main* | 0 | 120 | Instead of a user prompt, the subagent receives the task Claude wrote for it: "Research session timeout handling in this codebase." |
| *Subagent: Read session.ts* | 0 | 2,200 | Now the subagent does its work. This file read fills the subagent's context, not yours. |
| *Subagent: Read timeouts.ts* | 0 | 800 | Another file read in the subagent's separate context. |
| *Subagent: Read config/*.ts* | 0 | 3,100 | The subagent can read as many files as it needs. None of this touches your main context. |
| **Subagent returns summary** | 420 | — | Only the subagent's final text response comes back to your context, plus a small metadata trailer with token counts and duration. The subagent read 6,100 tokens of files. You got a 420-token result. **That's the context savings.** |
| Claude's response | 1,200 | — | Analysis and fix for session timeouts. This text appears in your terminal. |

### Phase 5: Shell command and skill invocation

| Event | Tokens | You see | Description |
|---|---|---|---|
| `!git status` | 180 | Full output | You ran a shell command with the `!` prefix to see which files Claude modified. The command and its output both enter context as part of your message. Useful for grounding Claude in command output without Claude running it. |
| `/commit-push` (skill) | 620 | One-liner | You invoked a skill that has `disable-model-invocation: true`. Its description was not in the skill index at startup, so it cost zero context until this moment. Now the full skill content loads and Claude follows its instructions to stage, commit, and push your changes. |

> **Tip:** Set `disable-model-invocation: true` on skills with side effects like committing, deploying, or sending messages. They stay out of context entirely until you need them.

### Phase 6: Compaction

| Event | Description |
|---|---|
| `/compact` | Replaces the conversation with a structured summary. You see a "Conversation compacted" message. The summarization happens without appearing in your terminal. |

---

## What survives compaction

When you run `/compact` (or auto-compaction triggers at ~95% capacity), the conversation is replaced with a structured summary. Here's what happens to each type of content:

| Content | After compaction |
|---|---|
| **Startup auto-loads** (system prompt, CLAUDE.md, environment, MCP tools) | **Survives** — re-injected from disk |
| **Skill descriptions** | **Does NOT survive** — only skills you actually invoked get preserved |
| **Conversation history** (prompts, file reads, responses, tool output) | **Replaced** with a summary. Key decisions, code patterns, and file states are preserved in the summary; detailed conversation is lost. |
| **Path-scoped rules** | Reload the next time Claude reads a file matching their pattern |
| **Subagent results** | Included in the summary if they were significant |

You can customize what survives by adding instructions to your CLAUDE.md like: "When compacting, always preserve the full list of modified files and any test commands."

Auto-compaction triggers at approximately 95% capacity. To trigger compaction earlier, set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` to a lower percentage (for example, `50`).

---

## Visibility legend

The simulation categorizes what you see in your terminal:

| Visibility | Meaning |
|---|---|
| **Invisible** | This content does not appear in your terminal. |
| **One-liner** | You see a brief mention, not the full content. |
| **Full text** | The actual content appears in your terminal. |

---

## Context management strategies

### Use `/clear` between tasks
Each new task should start fresh. Don't let context from a debugging session leak into a feature implementation.

### Use `/compact` with focus instructions
```
/compact Focus on the API changes and test results
```

### Use partial summarization with `/rewind`
`Esc + Esc` or `/rewind` to open the rewind menu. Choose **Summarize from here** to condense messages from a selected point forward while keeping earlier context intact, or **Summarize up to here** to condense earlier messages while keeping recent ones in full.

### Delegate research to subagents
Subagents run in their own context window. They can read dozens of files but only return a summary to your main conversation.

### Use `/btw` for side questions
For quick questions that don't need to stay in context, use `/btw`. The answer appears in a dismissible overlay and never enters conversation history.

### Be specific in prompts
"Fix the bug in auth.ts" causes Claude to read 1 file. "Fix the auth bug" might cause Claude to read 10 files exploring the codebase.

### Track context usage
Track context usage continuously with a [custom status line](/en/statusline). See [Reduce token usage](/en/costs#reduce-token-usage) for additional strategies.

---

## Key numbers

- **Total context window**: ~200,000 tokens
- **Startup cost**: ~8,000–10,000 tokens
- **Average file read**: 500–5,000 tokens
- **CLAUDE.md target**: under 200 lines
- **Auto memory limit**: 200 lines or 25KB of MEMORY.md
- **Compaction trigger**: automatic at ~95% capacity (configurable via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`)
- **Subagent context savings**: subagent reads stay in the subagent's window; only the summary returns (e.g., 6,100 tokens of file reads → 420-token summary)
