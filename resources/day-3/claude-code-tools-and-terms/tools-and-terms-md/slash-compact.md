# /compact

> **In one line:** `/compact` summarizes the current conversation to free context space while keeping the session going — unlike `/clear`, you don't lose the thread.

Running `/compact` automatically summarizes conversation history, preserving important code and decisions while freeing space. Use it when:
- You're in the middle of a task and don't want to start over
- The context is getting long but the work is ongoing
- You want to carry only the essentials forward

You can add a hint: `/compact Focus on the API changes` — Claude will emphasize those details in the summary.

For more control, use `Esc + Esc` or `/rewind`, select a message checkpoint, and choose **Summarize from here** or **Summarize up to here**:
- *Summarize from here* — condenses messages from that point forward while keeping earlier context intact
- *Summarize up to here* — condenses earlier messages while keeping recent ones in full

**Customize compaction in CLAUDE.md** with instructions like `"When compacting, always preserve the full list of modified files and any test commands"` — this ensures critical context survives summarization.

**Project-root CLAUDE.md survives compaction:** after `/compact`, Claude re-reads it from disk and re-injects it. Nested CLAUDE.md files in subdirectories are not re-injected automatically — they reload the next time Claude reads a file in that subdirectory.

**See also:** [/clear](slash-clear.md) · [Context Window](context-window.md) · [Checkpoints](checkpoints.md)
