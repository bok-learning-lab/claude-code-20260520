# Common failure patterns to avoid

These are the most common mistakes — recognizing them early saves time.

**The kitchen sink session.** You start with one task, then ask Claude something unrelated, then go back to the first task. Context is full of irrelevant information.
> Fix: `/clear` between unrelated tasks.

**Correcting over and over.** Claude does something wrong, you correct it, it's still wrong, you correct again. Context is polluted with failed approaches.
> Fix: after two failed corrections, `/clear` and write a better initial prompt incorporating what you learned.

**The over-specified CLAUDE.md.** Your CLAUDE.md is too long, so Claude ignores half of it because important rules get lost in the noise.
> Fix: ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.

**The trust-then-verify gap.** Claude produces a plausible-looking implementation that doesn't handle edge cases.
> Fix: always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it.

**The infinite exploration.** You ask Claude to "investigate" something without scoping it. Claude reads hundreds of files, filling the context.
> Fix: scope investigations narrowly or use subagents so the exploration doesn't consume your main context.
