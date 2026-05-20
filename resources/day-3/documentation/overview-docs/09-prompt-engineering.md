# Prompt Engineering Best Practices

> Source: https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices

Comprehensive guide to prompt engineering techniques for Claude, covering clarity, examples, XML structuring, thinking, and agentic systems.

---

## General Principles

### Be clear and direct

Claude responds well to clear, explicit instructions. Think of Claude as a brilliant but new employee who lacks context on your norms and workflows.

**Golden rule**: Show your prompt to a colleague with minimal context and ask them to follow it. If they'd be confused, Claude will be too.

| Less effective | More effective |
|---|---|
| "Create an analytics dashboard" | "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics." |

### Add context to improve performance

Explain why your instructions matter:

| Less effective | More effective |
|---|---|
| "NEVER use ellipses" | "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the engine won't know how to pronounce them." |

### Use examples effectively (few-shot prompting)

Examples are one of the most reliable ways to steer Claude's output. Include 3-5 examples that are:
- **Relevant**: mirror your actual use case
- **Diverse**: cover edge cases
- **Structured**: wrap in `<example>` tags to distinguish from instructions

### Structure prompts with XML tags

XML tags help Claude parse complex prompts. Wrap each type of content in its own tag (e.g., `<instructions>`, `<context>`, `<input>`).

### Give Claude a role

Setting a role focuses behavior and tone:

```python
client.messages.create(
    model="claude-opus-4-7",
    system="You are a helpful coding assistant specializing in Python.",
    messages=[
        {"role": "user", "content": "How do I sort a list of dictionaries by key?"}
    ],
)
```

### Long context prompting

For large documents (20k+ tokens):
- **Put longform data at the top** of your prompt, above your query
- **Structure with XML tags**: wrap each document in `<document>` tags
- **Ground responses in quotes**: ask Claude to quote relevant parts first

---

## Output and Formatting

### Communication style

Claude's latest models are more direct, conversational, and less verbose. If you want more visibility into reasoning:

```
After completing a task that involves tool use, provide a quick summary of the work you've done.
```

### Control response format

1. **Tell Claude what to do** instead of what not to do
2. **Use XML format indicators**: "Write prose in `<smoothly_flowing_prose>` tags"
3. **Match your prompt style** to desired output style
4. **Be explicit about formatting preferences**

---

## Tool Use

### Be explicit about actions

| Less effective | More effective |
|---|---|
| "Can you suggest some changes?" | "Change this function to improve its performance." |

To make Claude more proactive:
```
By default, implement changes rather than only suggesting them. If the user's intent 
is unclear, infer the most useful likely action and proceed.
```

### Optimize parallel tool calling

Claude excels at parallel tool execution. Boost this with:

```
If you intend to call multiple tools and there are no dependencies between the calls,
make all independent tool calls in parallel. For example, when reading 3 files, run 3 
tool calls in parallel.
```

---

## Thinking and Reasoning

### Leverage thinking capabilities

Claude can use extended thinking for complex multi-step reasoning:

```
After receiving tool results, carefully reflect on their quality and determine 
optimal next steps before proceeding.
```

### Avoid overthinking

If Claude is too thorough:
- Replace blanket defaults with targeted instructions
- Remove over-prompting
- Use a lower `effort` setting

---

## Agentic Systems

### Long-horizon reasoning

Claude excels at long-horizon tasks with exceptional state tracking. For tasks spanning multiple context windows:

1. Use the first window to set up a framework (write tests, create scripts)
2. Have Claude write tests in a structured format
3. Set up quality-of-life tools (setup scripts, test suites)
4. Encourage saving progress to files for state management

### Balancing autonomy and safety

```
Consider the reversibility and potential impact of your actions. Take local, 
reversible actions freely, but for destructive or shared-system actions, 
ask the user before proceeding.
```

### Research and information gathering

```
Search for this information in a structured way. Develop competing hypotheses. 
Track confidence levels. Regularly self-critique your approach.
```

### Minimize overengineering

```
Avoid over-engineering. Only make changes that are directly requested or clearly 
necessary. Don't add features beyond what was asked. Don't create helpers or 
abstractions for one-time operations.
```

### Minimize hallucinations

```
Never speculate about code you have not opened. If the user references a specific 
file, you MUST read the file before answering. Investigate before answering questions.
```
