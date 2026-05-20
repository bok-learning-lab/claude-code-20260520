# Checkpoints

> **In one line:** Every prompt you send creates a checkpoint — a snapshot of your conversation and files that you can restore at any time.

Claude automatically snapshots files before each change so a checkpoint can restore them. Double-tap `Escape` or run `/rewind` to open the rewind menu. You can:
- Restore conversation only
- Restore code (files) only
- Restore both conversation and files
- Summarize from a selected message

Checkpoints persist across sessions, so you can close your terminal and still rewind later. Instead of carefully planning every move, you can tell Claude to try something risky — if it doesn't work, rewind and try a different approach.

**Important:** checkpoints only track changes made *by Claude*, not external processes. This isn't a replacement for git.

**See also:** [/rewind](slash-rewind.md)
