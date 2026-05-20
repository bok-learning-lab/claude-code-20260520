# Best Practices for Claude Code

> Source: https://code.claude.com/docs/en/best-practices

Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions.

Claude Code is an agentic coding environment. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it.

**Key constraint**: Claude's context window fills up fast, and performance degrades as it fills. The context window holds your entire conversation, including every message, every file Claude reads, and every command output.

---

## Give Claude a way to verify its work

**This is the single highest-leverage thing you can do.**

Claude performs dramatically better when it can verify its own work -- run tests, compare screenshots, validate outputs.

| Strategy | Before | After |
|---|---|---|
| Provide verification criteria | "implement a function that validates email addresses" | "write a validateEmail function. example test cases: user@example.com is true, invalid is false. run the tests after implementing" |
| Verify UI changes visually | "make the dashboard look better" | "[paste screenshot] implement this design. take a screenshot of the result and compare it to the original" |
| Address root causes | "the build is failing" | "the build fails with this error: [paste error]. fix it and verify the build succeeds" |

---

## Explore first, then plan, then code

Separate research and planning from implementation to avoid solving the wrong problem.

1. **Explore**: Enter plan mode. Claude reads files and answers questions without making changes.
2. **Plan**: Ask Claude to create a detailed implementation plan.
3. **Implement**: Switch out of plan mode and let Claude code.
4. **Commit**: Ask Claude to commit with a descriptive message and create a PR.

For small, clear tasks (fixing a typo, adding a log line), skip the plan and ask Claude to do it directly.

---

## Provide specific context in your prompts

The more precise your instructions, the fewer corrections you'll need.

| Strategy | Before | After |
|---|---|---|
| Scope the task | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| Point to sources | "why does ExecutionFactory have such a weird api?" | "look through ExecutionFactory's git history and summarize how its api came to be" |
| Reference existing patterns | "add a calendar widget" | "look at how existing widgets are implemented. HotDogWidget.php is a good example. follow the pattern." |
| Describe the symptom | "fix the login bug" | "users report login fails after session timeout. check the auth flow in src/auth/, especially token refresh" |

### Provide rich content

- **Reference files with `@`** instead of describing where code lives
- **Paste images directly** -- copy/paste or drag and drop
- **Give URLs** for documentation and API references
- **Pipe in data** -- `cat error.log | claude`
- **Let Claude fetch what it needs** using Bash commands, MCP tools, or by reading files

---

## Configure your environment

### Write an effective CLAUDE.md

Run `/init` to generate a starter CLAUDE.md, then refine over time. Example:

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, not the whole test suite, for performance
```

| Include | Exclude |
|---|---|
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | File-by-file descriptions of the codebase |

### Configure permissions

- **Auto mode**: a classifier reviews commands and blocks only what looks risky
- **Permission allowlists**: permit specific tools you know are safe
- **Sandboxing**: OS-level isolation that restricts filesystem and network access

### Use CLI tools

Tell Claude Code to use CLI tools like `gh`, `aws`, `gcloud`, and `sentry-cli`. Claude is also effective at learning CLI tools it doesn't already know: "Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C."

---

## Communicate effectively

### Ask codebase questions

Use Claude Code for learning and exploration, the same sorts of questions you would ask another engineer:
- How does logging work?
- How do I make a new API endpoint?
- What edge cases does `CustomerOnboardingFlowImpl` handle?

### Let Claude interview you

For larger features, have Claude interview you first:

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs.
Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

---

## Manage your session

### Course-correct early and often

- **`Esc`**: stop Claude mid-action
- **`Esc + Esc` or `/rewind`**: restore previous conversation and code state
- **`"Undo that"`**: have Claude revert its changes
- **`/clear`**: reset context between unrelated tasks

If you've corrected Claude more than twice on the same issue, run `/clear` and start fresh with a better prompt.

### Manage context aggressively

- Use `/clear` frequently between tasks
- Run `/compact <instructions>` to summarize context with specific focus
- Use subagents for investigation to keep your main context clean

### Use subagents for investigation

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

### Resume conversations

Name sessions with `/rename` and treat them like branches. Run `claude --continue` to pick up the most recent session, or `claude --resume` to choose from a list.

---

## Automate and scale

### Run non-interactive mode

```bash
claude -p "Explain what this project does"
claude -p "List all API endpoints" --output-format json
```

### Run multiple Claude sessions

- **Worktrees**: isolated git checkouts so edits don't collide
- **Desktop app**: manage multiple local sessions visually
- **Web**: sessions on Anthropic-managed cloud infrastructure

### Fan out across files

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

---

## Avoid common failure patterns

- **The kitchen sink session**: mixing unrelated tasks in one session. Fix: `/clear` between tasks.
- **Correcting over and over**: context polluted with failed approaches. Fix: after two corrections, `/clear` and write a better prompt.
- **Over-specified CLAUDE.md**: too long, Claude ignores half of it. Fix: ruthlessly prune.
- **Trust-then-verify gap**: plausible implementation that doesn't handle edge cases. Fix: always provide verification.
- **Infinite exploration**: unscoped investigation fills context. Fix: scope narrowly or use subagents.
