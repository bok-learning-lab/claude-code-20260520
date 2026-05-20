# /rewind

> **In one line:** `/rewind` opens a checkpoint menu where you can restore your conversation, your files, or both to any earlier state.

Press `Esc + Esc` or run `/rewind` to open the rewind menu. You can restore:
- **Conversation only** — rolls back the chat, leaves files as-is
- **Code (files) only** — restores file state from a checkpoint, leaves the conversation intact
- **Both** — full restore to that moment
- **Summarize from here / up to here** — condense instead of restore

Every prompt you send creates a checkpoint automatically. Checkpoints persist across sessions.

**See also:** [Checkpoints](checkpoints.md)
