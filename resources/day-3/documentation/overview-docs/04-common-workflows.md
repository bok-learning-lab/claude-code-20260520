# Common Workflows

> Source: https://code.claude.com/docs/en/common-workflows

Step-by-step guides for exploring codebases, fixing bugs, refactoring, testing, and other everyday tasks with Claude Code.

---

## Understand new codebases

### Get a quick codebase overview

1. Navigate to the project root: `cd /path/to/project`
2. Start Claude Code: `claude`
3. Ask for a high-level overview:
   ```
   give me an overview of this codebase
   ```
4. Dive deeper:
   ```
   explain the main architecture patterns used here
   what are the key data models?
   how is authentication handled?
   ```

**Tips**: Start broad, then narrow down. Ask about coding conventions and project-specific terms.

### Find relevant code

```
find the files that handle user authentication
how do these authentication files work together?
trace the login process from front-end to database
```

---

## Fix bugs efficiently

1. Share the error:
   ```
   I'm seeing an error when I run npm test
   ```
2. Ask for fix recommendations:
   ```
   suggest a few ways to fix the @ts-ignore in user.ts
   ```
3. Apply the fix:
   ```
   update user.ts to add the null check you suggested
   ```

**Tips**: Tell Claude the command to reproduce the issue. Mention steps to reproduce. Note if the error is intermittent.

---

## Refactor code

1. Identify legacy code:
   ```
   find deprecated API usage in our codebase
   ```
2. Get recommendations:
   ```
   suggest how to refactor utils.js to use modern JavaScript features
   ```
3. Apply changes safely:
   ```
   refactor utils.js to use ES2024 features while maintaining the same behavior
   ```
4. Verify:
   ```
   run tests for the refactored code
   ```

---

## Work with tests

1. Identify untested code:
   ```
   find functions in NotificationsService.swift that are not covered by tests
   ```
2. Generate test scaffolding:
   ```
   add tests for the notification service
   ```
3. Add edge cases:
   ```
   add test cases for edge conditions in the notification service
   ```
4. Run and verify:
   ```
   run the new tests and fix any failures
   ```

Claude examines your existing test files to match the style, frameworks, and assertion patterns already in use.

---

## Create pull requests

```
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context about the security improvements
```

Or just: `create a pr for my changes`

---

## Handle documentation

```
find functions without proper JSDoc comments in the auth module
add JSDoc comments to the undocumented functions in auth.js
improve the generated documentation with more context and examples
check if the documentation follows our project standards
```

---

## Work with images

You can add images to the conversation by:
1. Drag and drop an image into the Claude Code window
2. Copy an image and paste it with `Ctrl+V`
3. Provide an image path: "Analyze this image: /path/to/your/image.png"

Then ask Claude to analyze, describe UI elements, suggest CSS from a mockup, etc.

---

## Reference files and directories

Use `@` to quickly include files or directories:

```
Explain the logic in @src/utils/auth.js
What's the structure of @src/components?
```

File paths can be relative or absolute. You can reference multiple files in a single message.

---

## Resume previous conversations

```bash
claude --continue        # Resume most recent session
claude --resume          # Choose from a list
```

Or use `/resume` from inside a running session.

---

## Run parallel sessions with worktrees

Work on a feature in one terminal while Claude fixes a bug in another:

```bash
claude --worktree feature-auth
```

---

## Plan before editing

Switch to plan mode for changes you want to review first:

```bash
claude --permission-mode plan
```

Or press `Shift+Tab` mid-session to toggle into plan mode.

---

## Delegate research to subagents

```
use a subagent to investigate how our auth system handles token refresh
```

The subagent explores in a separate context window and reports back a summary.

---

## Pipe Claude into scripts

```bash
git log --oneline -20 | claude -p "summarize these recent commits"
```

---

## Run Claude on a schedule

| Option | Where it runs | Best for |
|---|---|---|
| Routines | Anthropic-managed infrastructure | Tasks that run even when your computer is off |
| Desktop scheduled tasks | Your machine, via the desktop app | Tasks needing local file access |
| GitHub Actions | Your CI pipeline | Tasks tied to repo events |
| `/loop` | The current CLI session | Quick polling while a session is open |
