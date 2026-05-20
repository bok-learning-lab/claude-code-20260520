# Plan Mode

> **In one line:** Plan mode lets Claude read files and think through a problem without making any changes — you review and approve before anything gets written.

Plan mode separates exploration from execution. Letting Claude jump straight to coding can produce code that solves the wrong problem. Plan mode gives you a chance to check the approach first.

**The recommended four-phase workflow:**

**1. Explore** — enter plan mode. Claude reads files and answers questions without making changes.
```
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.
```

**2. Plan** — ask Claude to create a detailed implementation plan.
```
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.
```
Press `Ctrl+G` to open the plan in your text editor for direct editing before Claude proceeds.

**3. Implement** — switch out of plan mode and let Claude code, verifying against its plan.
```
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.
```

**4. Commit** — ask Claude to commit with a descriptive message and create a PR.
```
commit with a descriptive message and open a PR
```

**When to use plan mode:** most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified. For tasks where the scope is clear and the fix is small (fixing a typo, renaming a variable), ask Claude to do it directly — planning adds overhead that isn't always worth it.
