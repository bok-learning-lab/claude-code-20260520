# Non-Interactive Mode

> **In one line:** Non-interactive mode lets you run Claude from the command line without starting a session — useful for scripts, CI pipelines, and automated workflows.

With `claude -p "your prompt"`, you can run Claude non-interactively, without a session. This is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow.

```bash
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

Add `--allowedTools` to restrict what Claude can do when running unattended:

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

Use `--verbose` for debugging during development, and turn it off in production.
