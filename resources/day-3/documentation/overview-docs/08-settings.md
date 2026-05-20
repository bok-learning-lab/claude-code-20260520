# Claude Code Settings

> Source: https://code.claude.com/docs/en/settings

Claude Code offers configurable settings across multiple scopes to control its behavior.

---

## Configuration Scopes

| Scope | Location | Who it affects | Shared with team? |
|---|---|---|---|
| **Managed** | Server/system-level | All users on the machine | Yes (deployed by IT) |
| **User** | `~/.claude/` directory | You, across all projects | No |
| **Project** | `.claude/` in repository | All collaborators | Yes (committed to git) |
| **Local** | `.claude/settings.local.json` | You, in this repo only | No (gitignored) |

### Priority order (highest to lowest)

1. Managed (cannot be overridden)
2. Command line arguments
3. Local
4. Project
5. User

---

## Settings Files

- **User settings**: `~/.claude/settings.json` -- applies to all projects
- **Project settings**: `.claude/settings.json` -- shared with team via git
- **Local settings**: `.claude/settings.local.json` -- personal, gitignored

---

## Key Settings Reference

### Model Configuration
- `model` -- Default model to use
- `effortLevel` -- Persist effort level across sessions

### Permissions
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./secrets/**)"
    ]
  }
}
```

Rules follow the format `Tool` or `Tool(specifier)`. Evaluation order: deny first, then ask, then allow.

### UI/Display
- `editorMode` -- Key binding mode: "normal" or "vim"
- `language` -- Preferred response language
- `theme` -- Color theme

### Memory
- `autoMemoryEnabled` -- Enable auto memory (default: true)
- `claudeMdExcludes` -- Glob patterns of CLAUDE.md files to skip

### Tools & Integrations
- `hooks` -- Configure custom commands at lifecycle events
- `enableAllProjectMcpServers` -- Auto-approve all project MCP servers

---

## Sandbox Settings

Configure bash sandboxing (macOS, Linux, WSL2):

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": {
      "allowWrite": ["/tmp/build", "~/.kube"],
      "denyRead": ["~/.aws/credentials"]
    },
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org"]
    }
  }
}
```

---

## Example Settings File

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  }
}
```
