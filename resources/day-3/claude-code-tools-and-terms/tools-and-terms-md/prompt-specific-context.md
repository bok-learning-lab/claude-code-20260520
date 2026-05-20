# Provide specific context

> **The more precise your instructions, the fewer corrections you'll need.** Claude can infer intent, but it can't read your mind.

Reference specific files, mention constraints, and point to example patterns.

| Strategy | Before | After |
|---|---|---|
| **Scope the task** | *"add tests for foo.py"* | *"write a test for foo.py covering the edge case where the user is logged out. avoid mocks."* |
| **Point to sources** | *"why does ExecutionFactory have such a weird api?"* | *"look through ExecutionFactory's git history and summarize how its api came to be"* |
| **Reference existing patterns** | *"add a calendar widget"* | *"look at how existing widgets are implemented on the home page. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards."* |
| **Describe the symptom** | *"fix the login bug"* | *"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it"* |

Vague prompts can be useful when you're exploring and can afford to course-correct. A prompt like *"what would you improve in this file?"* can surface things you wouldn't have thought to ask about.
