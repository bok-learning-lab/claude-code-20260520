# Permissions

> **In one line:** Permissions control what Claude Code is allowed to do — write files, run commands, use tools — and how much it asks you before doing it.

By default, Claude Code requests permission for actions that might modify your system: file writes, Bash commands, MCP tools, etc. This is safe but tedious. After the tenth approval you're not really reviewing anymore, you're just clicking through.

**Three ways to reduce interruptions:**

**Auto mode** — a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions. Best when you trust the general direction of a task but don't want to click through every step.

**Permission allowlists** — permit specific tools you know are safe, like `npm run lint` or `git commit`. Use `/permissions` to configure these.

**Sandboxing** — enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries. Use `/sandbox` to enable.

**See also:** [/permissions](slash-permissions.md) · [/sandbox](slash-sandbox.md)
