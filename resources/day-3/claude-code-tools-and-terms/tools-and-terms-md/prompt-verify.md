# Give Claude a way to verify its work

> **The single highest-leverage thing you can do.** Claude performs dramatically better when it can verify its own work.

Without clear success criteria, Claude might produce something that looks right but doesn't work. You become the only feedback loop, and every mistake requires your attention.

| Strategy | Before | After |
|---|---|---|
| **Provide verification criteria** | *"implement a function that validates email addresses"* | *"write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing"* |
| **Verify UI changes visually** | *"make the dashboard look better"* | *"[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them"* |
| **Address root causes, not symptoms** | *"the build is failing"* | *"the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error"* |

Your verification can be a test suite, a linter, or a Bash command that checks output. Invest in making your verification rock-solid.
