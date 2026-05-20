# Quickstart Guide

> Source: https://code.claude.com/docs/en/quickstart

This quickstart guide will have you using AI-powered coding assistance in a few minutes.

## Before you begin

Make sure you have:

- A terminal or command prompt open
- A code project to work with
- A Claude subscription (Pro, Max, Team, or Enterprise), Claude Console account, or access through a supported cloud provider

## Step 1: Install Claude Code

**macOS, Linux, WSL:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Homebrew:**
```bash
brew install --cask claude-code
```

## Step 2: Log in to your account

```bash
claude
# You'll be prompted to log in on first use
```

You can log in using:
- Claude Pro, Max, Team, or Enterprise (recommended)
- Claude Console (API access with pre-paid credits)
- Amazon Bedrock, Google Vertex AI, or Microsoft Foundry (enterprise cloud providers)

## Step 3: Start your first session

```bash
cd /path/to/your/project
claude
```

## Step 4: Ask your first question

```
what does this project do?
```

Other useful starting prompts:
```
what technologies does this project use?
where is the main entry point?
explain the folder structure
```

Claude Code reads your project files as needed. You don't have to manually add context.

## Step 5: Make your first code change

```
add a hello world function to the main file
```

Claude Code will find the appropriate file, show you proposed changes, ask for your approval, and make the edit.

## Step 6: Use Git with Claude Code

```
what files have I changed?
commit my changes with a descriptive message
create a new branch called feature/quickstart
show me the last 5 commits
help me resolve merge conflicts
```

## Step 7: Fix a bug or add a feature

```
add input validation to the user registration form
there's a bug where users can submit empty forms - fix it
```

## Step 8: Try other common workflows

**Refactor code:**
```
refactor the authentication module to use async/await instead of callbacks
```

**Write tests:**
```
write unit tests for the calculator functions
```

**Update documentation:**
```
update the README with installation instructions
```

**Code review:**
```
review my changes and suggest improvements
```

## Essential commands

| Command | What it does | Example |
|---|---|---|
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or Ctrl+D | Exit Claude Code | `exit` |

## Pro tips for beginners

1. **Be specific with your requests**: Instead of "fix the bug", try "fix the login bug where users see a blank screen after entering wrong credentials"

2. **Use step-by-step instructions**: Break complex tasks into steps

3. **Let Claude explore first**: Before making changes, let Claude understand your code (e.g., "analyze the database schema")

4. **Save time with shortcuts**:
   - Type `/` to see all commands and skills
   - Use Tab for command completion
   - Press up arrow for command history
   - Press `Shift+Tab` to cycle permission modes
