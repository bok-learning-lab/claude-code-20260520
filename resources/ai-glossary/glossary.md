# Glossary

Plain-language definitions of every term, concept, and tool introduced in the workshop. Written for absolute beginners: each entry defines the term in a sentence, gives an analogy, says why it matters, and points to related entries.

---

## Quick index

**The basics — who and what**
[Claude](#claude) · [Anthropic](#anthropic) · [Claude Code](#claude-code) · [Claude Cowork](#claude-cowork) · [Project](#project) · [Model (Opus / Sonnet / Haiku)](#model-opus--sonnet--haiku) · [API](#api)

**How Claude "thinks"**
[Large Language Model (LLM)](#large-language-model-llm) · [Token / Tokenization](#token--tokenization) · [Tool Call](#tool-call) · [Hallucination](#hallucination) · [Agent](#agent) · [Harness](#harness)

**How Claude remembers — the context story**
[Context](#context) · [Context Window](#context-window) · [Context Rot](#context-rot) · [Context Engineering](#context-engineering) · [Memory](#memory) · [Compact](#compact)

**Talking to Claude**
[Prompt](#prompt) · [System Prompt](#system-prompt)

**Files, formats, and outputs**
[Markdown](#markdown) · [Markdown — Intro & Cheatsheet](#markdown--intro--cheatsheet) · [HTML](#html) · [CLAUDE.md](#claudemd) · [SKILL.md](#skillmd) · [Artifact](#artifact)

**Using Claude safely at Harvard**
[Data Classification](#data-classification)

---

## Claude

> **In one line:** Claude is the AI assistant you talk to in this workshop — you type to it in plain English, and it writes back.

### In plain terms

Claude is a computer program you interact with by *writing*. You ask a question or describe a task in ordinary language; Claude responds with text, and — as we'll see later — it can also make documents, charts, and small web pages for you.

There is no special command language to learn. If you can write an email, you can use Claude. The skill this workshop teaches is not "commands" but *how to set Claude up to do good work* — what to tell it, and what to give it to work with.

A few things to know early:

- Claude doesn't "look things up" the way a search engine does. It generates each reply based on what it has learned and on what you've put in front of it right now. (Why that matters is the whole story of [Context](#context).)
- It can be confidently wrong. Part of the workshop is building intuition for *when* to trust it and *how* to check.

### Why it matters in this workshop

Everything else — [Claude Code](#claude-code), [Skills](#skillmd), [context engineering](#context-engineering) — is a way of getting more out of this same assistant. Start here.

**See also:** [Anthropic](#anthropic) · [Claude Code](#claude-code) · [Context](#context)

---

## Anthropic

> **In one line:** Anthropic is the company that builds Claude.

### In plain terms

When you use Claude — on the web, in the desktop app, or in [Claude Code](#claude-code) — you're using software made by a company called Anthropic. Anthropic builds the underlying models and the apps you interact with them through.

You don't need to know anything about the company to do the workshop. The one useful distinction: **"Claude" is the assistant; "Anthropic" is the maker.** You'll occasionally see "Anthropic" in menus, billing, or documentation — same thing, just the company name.

### Why it matters in this workshop

Mostly for orientation, so the names aren't confusing. It also explains why the different places you meet Claude (web, desktop, Claude Code) feel like one consistent assistant: they're all the same company's models behind the scenes.

**See also:** [Claude](#claude) · [Claude Code](#claude-code)

---

## Claude Code

> **In one line:** Claude Code is a version of Claude that can read, change, and create the actual files and folders on your computer.

### In plain terms

The Claude you meet on the web answers in a chat box. **Claude Code** is the same assistant, but with hands: it can open the files in a folder on your machine, edit them, make new ones, and run things for you — while explaining what it's doing.

Think of the difference this way:

- **Web Claude** is like emailing an expert: you paste things in, it sends text back.
- **Claude Code** is like that expert sitting at *your* desk, working directly in *your* documents.

In this workshop you'll first meet it through the **desktop app's Cowork tab**, so you don't need to think of it as a programming tool. It's for working on a folder of real materials — a course's readings, a messy spreadsheet, a pile of notes.

### Why it matters in this workshop

This is where the workshop is heading. Once Claude can see a whole folder, the key skill becomes deciding *what's in that folder* and *what notes you leave it* — which is exactly [context engineering](#context-engineering), [CLAUDE.md](#claudemd), and [Skills](#skillmd).

**See also:** [Claude](#claude) · [CLAUDE.md](#claudemd) · [Context](#context)

---

## Claude Cowork

> **In one line:** Claude Cowork is the desktop-app mode where Claude can read and change the actual files in a folder on your computer — not just talk in a chat.

### In plain terms

In the web interface, Claude only sees what you paste or upload, and whatever it makes comes back as text or an [artifact](#artifact) you copy out by hand. In **Cowork**, you point Claude at a folder and it can work *on* the files there: read a stack of images, rename them, pull the text out of them, write new files, and build a small local website from the result. The button even changes from "new chat" to "new task" to signal the shift from talking to doing.

A few things to hold onto:

- It's the desktop app's middle tab — between plain chat (the same thing as the website) and [Claude Code](#claude-code) (the terminal version, covered later).
- The power and the danger are the same fact: it can touch your files. Pointing it at your Downloads or Screenshots folder is a great demo and a bad idea if those hold sensitive material — link it to a deliberate project folder instead.
- Whether it can *change* files (vs. only read them) is something you grant.

### Why it matters in this workshop

The second half of Day 1 lives here. It's the leap from "Claude generates text" to "Claude does things to my stuff" — the same mechanics as the web demos, but now acting on many local files at once.

**See also:** [Claude Code](#claude-code) · [Project](#project) · [Data Classification](#data-classification) · [Artifact](#artifact)

---

## Project

> **In one line:** A Project is a saved workspace that bundles related chats — and, in Cowork, a folder on your computer — so Claude keeps the right context together and out of unrelated conversations.

### In plain terms

In the web interface, a Project is an organizational container: you can drop a conversation into one to keep a body of work together rather than scattered across loose chats. In [Cowork](#claude-cowork), it's more than tidiness — "work in a project" links Claude to an actual folder on your machine, which is what lets it read and change those files.

The reason this belongs in the [context](#context) story: a Project is a way of deciding, on purpose, what Claude has in front of it. Keeping a task in its own project (and starting a "new task" rather than continuing an unrelated thread) keeps stray material from earlier conversations out of the model's view.

### Why it matters in this workshop

Projects are the practical handle for [context engineering](#context-engineering) in the everyday interface — the difference between Claude working from exactly the right folder and Claude working from whatever happened to be in the last chat.

**See also:** [Claude Cowork](#claude-cowork) · [Context](#context) · [Context Engineering](#context-engineering) · [Memory](#memory)

---

## Model (Opus / Sonnet / Haiku)

> **In one line:** "The model" is the specific version of Claude doing the thinking; Claude comes in a few — Opus, Sonnet, Haiku — that trade off depth against speed.

### In plain terms

"Claude" is the assistant; **the model** is the particular engine behind it on a given task. Anthropic offers a small family, and the names follow a poetry theme by length:

- **Opus** — the most capable and thorough; best for hard, high-stakes work. Slower and more expensive.
- **Sonnet** — a strong middle: very capable, noticeably faster. A good default for most work.
- **Haiku** — the fastest and lightest; great for quick, simple, high-volume tasks.

The names also carry a version number (e.g. "Opus 4.7"); higher is newer and more capable. You'll sometimes choose a model from a menu; often a sensible default is picked for you.

The beginner takeaway is just the trade-off intuition: **bigger model = more depth, less speed; smaller = faster, lighter.** Match the model to the job — you don't need the heaviest one to reformat a list.

### Why it matters in this workshop

It explains the model-picker menu and reduces "which one do I pick?" anxiety.

**See also:** [Claude](#claude) · [LLM](#large-language-model-llm) · [API](#api)

---

## API

> **In one line:** An API is a way for one piece of software to talk to another directly — here, a way to use Claude from code instead of through a chat window.

### In plain terms

So far you meet Claude through an app with a text box. An **API** (application programming interface) is the other door: a way for a *program* to send text to Claude and get text back, with no human typing in a chat. Same Claude, no chat window.

A loose analogy: the chat app is the dining room — you order, a meal arrives. The API is the kitchen's service window — other software places orders directly and collects the results, at scale and automatically.

For an absolute beginner this is mostly a **vocabulary** entry. You will not need the API to do the intro workshop. It matters because:

- You'll see the word in documentation and later sessions.
- It's where the series eventually goes — automating repetitive scholarly and teaching tasks, where you don't want to sit and chat through each one.

The one idea to keep: *anything you can do by chatting, software can also do through the API* — which is what makes automation possible later.

### Why it matters in this workshop

Orientation and foreshadowing. Beginners need the term defined so it isn't intimidating when the advanced parts of the series build on it.

**See also:** [Claude](#claude) · [Anthropic](#anthropic) · [Model](#model-opus--sonnet--haiku)

---

## Large Language Model (LLM)

> **In one line:** A large language model is the kind of system Claude is — at its core, it predicts the next bit of text, one piece at a time, based on patterns learned from an enormous amount of writing.

### In plain terms

"LLM" stands for **large language model**. Strip away the jargon and the core mechanic is surprisingly humble: given the text so far, the model predicts what [token](#token--tokenization) (roughly, the next chunk of a word) is most likely to come next — then does it again, and again, building up a reply.

It learned those predictions from a vast amount of text — loosely, "the average of the internet." That has two consequences worth feeling in your bones early:

- **It's astonishingly fluent**, because fluent text is what it learned to continue.
- **It can be confidently wrong**, because "what sounds likely" is not the same as "what is true." The classic demo: ask for a long multiplication and it often gets it wrong — not from stupidity, but because it's *predicting* an answer rather than *calculating* one. (Have it write and run code instead, and it's exact — a preview of why code matters in this series.)

This is why [context](#context) is everything: a next-text predictor is only as good as the text you put in front of it.

### Why it matters in this workshop

Understanding "it predicts, it doesn't look up or calculate" explains both Claude's brilliance and its failure modes — and motivates everything we do with code and context engineering to compensate.

**See also:** [Token](#token--tokenization) · [Context](#context)

---

## Token / Tokenization

> **In one line:** A token is a small chunk of text — often a word or part of a word — and tokenization is the act of slicing text into those chunks. It's the unit Claude actually reads and writes in.

### In plain terms

Claude doesn't process text letter by letter or exactly word by word. It breaks text into **tokens**: pieces that are usually a short word or a fragment of a longer one. "Teaching" might be one token; "Bok Center" might be three. Splitting text this way is called **tokenization**.

Two reasons a beginner should care:

- **It explains some weird failures.** Because the model sees chunks, not letters, tasks like "count the r's in *strawberry*" or reversing a word can trip it up — it's not looking at letters the way you are.
- **It's the unit the [context window](#context-window) is measured in.** When we say the window holds a large but finite amount, the count is in tokens. A rough feel: a token is about ¾ of a word, so a page of text is several hundred tokens.

You never have to count tokens yourself. The takeaway is just the mental model: *Claude reads in chunks, and those chunks are what fill the limited window.*

### Why it matters in this workshop

It demystifies a class of "why can't it do something that simple?" moments, and it gives [context window](#context-window) and [context rot](#context-rot) a concrete unit instead of a hand-wave.

**See also:** [LLM](#large-language-model-llm) · [Context Window](#context-window)

---

## Tool Call

> **In one line:** A tool call is when Claude, instead of just writing an answer, *does something* — runs code, reads a file, fetches a page — and uses the result.

### In plain terms

A plain LLM only predicts text. That alone can't reliably multiply large numbers or know what's in your folder. **Tool calls** are how Claude steps outside pure text prediction: it can reach for a tool, get a real result, and continue with that result in hand.

Two kinds you'll see early in the workshop:

1. **Doing something exactly** — e.g. writing and running a snippet of code to do arithmetic. The earlier multiplication failure disappears, because now it's *computing*, not *guessing*.
2. **Grounding in real material** — e.g. opening the actual reading or spreadsheet so the answer is based on *your* document, not a plausible-sounding average.

You usually don't invoke tools yourself; Claude decides a task needs one and you see it happen ("reading file…", "running…"). The idea to hold onto: **Claude can act, not just talk — and acting is what makes it accurate and grounded.**

This is also the foundation of an [agent](#agent): an agent is largely Claude choosing and chaining tool calls toward a goal.

### Why it matters in this workshop

Tool calls resolve the tension from the LLM section: the model is unreliable at some things *until* it can use tools. Tool calls are *why* code and folder access make Claude trustworthy for real work.

**See also:** [LLM](#large-language-model-llm) · [Agent](#agent) · [Context](#context)

---

## Hallucination

> **In one line:** A hallucination is when Claude states something false with complete confidence — fluent, plausible, and wrong — because it is predicting likely text, not looking facts up.

### In plain terms

Because a [large language model](#large-language-model-llm) works by continuing patterns in text rather than retrieving stored facts, it will sometimes produce an answer that *sounds* right and *is* wrong — and it won't sound any less sure when it does. The workshop showed two clean examples:

- **Big-number multiplication.** Ask it to multiply two seven-digit numbers and it gets the first few digits and the digit-count right, but the middle wrong — it's pattern-matching toward a plausible-looking number, not calculating.
- **The scene that doesn't exist.** Ask for a close reading of a passage that isn't real and it will confidently say so — or, given a slightly different prompt, confidently analyze something fabricated — until you paste in the actual text.

The fix in both cases is the same move: give it the right tool or the right material. "Try it again with Python" turns the math right; supplying the real passage turns the reading right. Hallucination isn't random noise — it's what prediction looks like when the model is asked for something it can't pattern-match its way to.

### Why it matters in this workshop

This is the workshop's core trust lesson: not "AI is unreliable," but *when* to check and *how* to set Claude up so it doesn't have to guess. Almost everything later — giving it [context](#context), letting it run code — is a defense against this.

**See also:** [LLM](#large-language-model-llm) · [Context](#context) · [Tool Call](#tool-call) · [Model](#model-opus--sonnet--haiku)

---

## Agent

> **In one line:** An agent is Claude working toward a goal over multiple steps — deciding what to do, doing it (tool calls), checking the result, and continuing — instead of answering in a single reply.

### In plain terms

A normal exchange is one round: you ask, Claude answers. An **agent** is Claude given a goal and the room to take several steps to reach it: read this, then change that, then check it worked, then move on — looping until the job is done.

An analogy: the difference between asking a colleague a question (one answer) and handing them a task to go complete (they'll take many small actions on their own and come back when it's done). [Claude Code](#claude-code) working through a folder is acting as an agent.

What makes this possible is the combination you've already met:

- [Tool calls](#tool-call) — so it can actually *do* each step.
- [Context](#context) — so each step's result informs the next.

For beginners the word matters less than the shift in expectation: Claude isn't only a question-answerer; it can carry out a multi-step task.

### Why it matters in this workshop

It frames where the series is heading and reframes Claude Code: not "chat that can touch files," but "an assistant that can carry out a piece of work."

**See also:** [Tool Call](#tool-call) · [Harness](#harness) · [Claude Code](#claude-code)

---

## Harness

> **In one line:** The harness is the program around Claude that actually runs the loop — feeding it context, carrying out its tool calls, and passing results back — turning a text predictor into something that gets work done.

### In plain terms

Claude itself only takes text in and produces text out. By itself it can't open a file or run code. The **harness** is the surrounding software that makes the rest happen: it assembles what goes into the [context](#context), notices when Claude asks to use a tool, performs that action, and hands the result back so Claude can continue.

An analogy: Claude is the engine; the harness is the rest of the car — wheels, pedals, dashboard. The engine provides the intelligence, but you only get anywhere because the harness connects it to the road.

[Claude Code](#claude-code) is, in effect, a harness: it's why the same Claude that just chats on the web can, here, read your folder and make changes. Different harnesses give the same underlying Claude different abilities.

### Why it matters in this workshop

It explains why "Claude" feels different on the web vs. in Claude Code — same model, different harness — and sets up later parts of the series where the harness is configured deliberately.

**See also:** [Tool Call](#tool-call) · [Agent](#agent) · [Claude Code](#claude-code)

---

## Context

> **In one line:** Context is everything Claude can "see" at this moment — your messages, its replies, any files or notes in front of it. Every answer is built only from this.

### In plain terms

Claude has no memory of you between conversations unless you give it one. Each reply is generated *only* from what's currently in front of it. That "what's in front of it" is the **context**.

The workshop's running analogy is the film *Memento*: the main character can't form new long-term memories, so he survives by writing notes to himself. Each new conversation with Claude is a fresh "day" for that character. It knows only what's written on the notes you've handed it *so far*: your prompts, its own previous replies in this conversation, plus things like its [memory](#memory) and any files you've shown it.

The practical consequences:

- If something isn't in the context, Claude doesn't know it — even if you told it yesterday, or it's "obvious."
- If something *unhelpful* is in the context, it can drag the answer down (see [Context Rot](#context-rot)).
- So the highest-leverage skill is choosing what goes in — [Context Engineering](#context-engineering).

### Why it matters in this workshop

Almost every "why did Claude do that?" moment traces back to context: something was missing, or something junk was present. Get this idea and the rest of the workshop clicks into place.

**See also:** [Context Window](#context-window) · [Context Rot](#context-rot) · [Context Engineering](#context-engineering)

---

## Context Window

> **In one line:** The context window is the fixed amount of text Claude can hold in view at one time. When it's full, something has to give.

### In plain terms

[Context](#context) is what Claude can see; the **context window** is *how much* of it fits. It's measured in tokens (roughly, chunks of words), and the limit is large but real — think of it as a very big, but finite, desk.

Continuing the *Memento* analogy: each conversation is one "day," and the context window is how many notes can be spread across the desk at once for that day. Every message you send and every reply Claude gives takes up some of the desk. Things that go on the desk early — Claude's memory, the workshop's setup notes — are there from the start; the rest fills up as you talk.

What this means in practice:

- Long conversations gradually fill the window. Very long ones can push earlier details out of view.
- Pasting in a huge document uses a lot of the window at once.
- A fuller window isn't automatically better — see [Context Rot](#context-rot).

You don't need to count tokens. You just need the instinct: *space is limited, so spend it on what matters.*

### Why it matters in this workshop

It's the reason [context engineering](#context-engineering) is a skill and not an afterthought. If the window were infinite, you could dump everything in; because it's finite, *choosing* is the work.

**See also:** [Context](#context) · [Context Rot](#context-rot) · [Context Engineering](#context-engineering)

---

## Context Rot

> **In one line:** Context rot is the way Claude's answers get worse when the context window fills up with stale, irrelevant, or contradictory material.

### In plain terms

More context is not always better. As a conversation gets long and cluttered — abandoned tangents, an early draft you've since rejected, three contradictory sets of instructions — Claude has a harder time telling what *currently* matters. The quality of its answers can quietly degrade. That drift is **context rot**.

A desk analogy: a clear desk with the one document you need is better than a desk buried under every draft from the past hour. The buried-desk state is context rot.

Signs you may be seeing it:

- Claude reverts to an instruction you already corrected.
- It blends two different tasks together.
- Replies get vaguer or more generic the longer you go.

The usual fixes are simple: start a fresh conversation for a new task, restate what matters now, or remove the clutter rather than piling more on top.

### Why it matters in this workshop

It's the counter-intuitive half of [context engineering](#context-engineering): the goal isn't to give Claude *everything*, it's to give it the *right* things and keep the rest out. Naming this failure mode helps participants diagnose "why did it suddenly get worse?"

**See also:** [Context Window](#context-window) · [Context](#context) · [Context Engineering](#context-engineering)

---

## Context Engineering

> **In one line:** Context engineering is the deliberate practice of choosing what Claude can see — and what it can't — so it does its best work.

### In plain terms

Once you know that every answer comes only from the [context](#context), that the [context window](#context-window) is finite, and that clutter causes [context rot](#context-rot), one skill follows from all three: **deciding, on purpose, what to put in front of Claude.** That's context engineering.

It's less like programming and more like preparing a good briefing for a sharp assistant:

- Give it the materials that matter (the actual reading, the real spreadsheet) — not a vague summary.
- Leave out what doesn't (old drafts, unrelated tangents).
- Write down standing instructions once, where Claude will reliably see them — this is what [CLAUDE.md](#claudemd) and [Skills](#skillmd) are for.
- Start fresh when the task changes, instead of dragging old context along.

This workshop's framing: it's the **single most powerful lever** for high-quality output — more than clever wording in any one prompt.

### Why it matters in this workshop

It's the through-line. The web UI, Claude Code, the Inputs → Operations → Outputs triptych, CLAUDE.md, Skills — each is a concrete way of doing context engineering well. Participants who internalize this idea can transfer it everywhere.

**See also:** [Context](#context) · [Context Window](#context-window) · [Context Rot](#context-rot) · [CLAUDE.md](#claudemd) · [SKILL.md](#skillmd)

---

## Memory

> **In one line:** Memory is an optional feature where Claude saves a few notes about you and re-reads them at the start of later conversations — so it doesn't start from zero every time.

### In plain terms

By default, each conversation is a blank slate (the [Context](#context) / *Memento* point: a fresh "day," no recollection of yesterday). **Memory** softens that: when it's on, Claude keeps a short, running set of notes — your preferences, recurring projects — and those notes are placed into the context near the start of new conversations.

The crucial framing from the workshop: **this "memory" is just words.** You're not switching on a mind or a personality. You're arranging for some text to be added to the front of the next conversation automatically. That's all "remembering" is here — and seeing it that way is the first step toward understanding context.

Practical notes:

- It holds a *limited* set of notes, and only the most relevant make it in — not a full transcript of everything you've ever said.
- You can view and edit what it's keeping.
- It's a convenience, not a guarantee: important standing facts about a project belong in a [CLAUDE.md](#claudemd), which is explicit and under your control.

### Why it matters in this workshop

Turning on memory is an early hands-on moment, and it's the perfect hook for the whole context story: "memory is just words" leads straight into how Claude actually works.

**See also:** [Context](#context) · [CLAUDE.md](#claudemd)

---

## Compact

> **In one line:** Compact is a command (`/compact`) that squeezes a long conversation down to a summary and continues in a fresh thread — so a filling context window doesn't quietly degrade Claude's work.

### In plain terms

A conversation can only get so long before it hits the edge of the [context window](#context-window), and well before that, a cluttered window starts to drag answers down ([context rot](#context-rot)). **Compact** is the deliberate version of the *Memento* "summarize the day" move: it crushes the conversation so far into a summary and starts a new thread carrying that summary — alongside the [system prompt](#system-prompt) and [memory](#memory), which are always there.

The workshop's framing matters here: this is not magic. Compact is just a Markdown instruction telling Claude *how* to summarize a long conversation. Because it's only text, it can be customized — you can write your own version that summarizes work the way your field or project actually needs.

It's a slash command: you type `/compact` mid-conversation rather than waiting to run out of room.

### Why it matters in this workshop

It's the first concrete, you-can-type-this-now tool for managing the context story instead of just understanding it — and the cleanest proof that even Claude's "smart" features are, underneath, just text instructions.

**See also:** [Context Window](#context-window) · [Context Rot](#context-rot) · [Memory](#memory) · [SKILL.md](#skillmd)

---

## Prompt

> **In one line:** A prompt is simply what you send to Claude — your message, the question or instruction it responds to.

### In plain terms

There's less mystique here than the word suggests. A **prompt** is your input: the thing you type and send. Claude reads everything in [context](#context) and writes a reply; the prompt is the part *you* just added.

"Prompting" has a reputation as a dark art of magic phrases. This workshop takes a different line: the biggest gains come not from clever wording but from giving Claude the right *materials* and *standing instructions* — that's [context engineering](#context-engineering). A good prompt mostly means a clear one:

- Say what you want and what it's for.
- Give it the actual material to work from, not a vague gesture at it.
- Say what "good" looks like (length, format, audience).

A useful distinction: your prompt is the message you write *this turn*. The background instructions Claude also follows — but that you didn't type — are the [system prompt](#system-prompt).

### Why it matters in this workshop

It right-sizes expectations: prompting is normal writing, not incantation. The leverage is in context, which is what the rest of the glossary is about.

**See also:** [System Prompt](#system-prompt) · [Context](#context) · [Context Engineering](#context-engineering)

---

## System Prompt

> **In one line:** The system prompt is a set of background instructions Claude is given *before* your conversation starts — you don't type it, but it shapes how Claude behaves.

### In plain terms

Every time you talk to Claude, there's text in the [context](#context) that you didn't write: the **system prompt**. It's the standing brief the app gives Claude — things like its role, its tone, what it should and shouldn't do, what tools it has.

An analogy: if your [prompt](#prompt) is what you say to a new staff member today, the system prompt is the job description and house rules they were handed on day one. You don't repeat the rules each time; they're already in effect.

Why a beginner should know it exists:

- It explains why Claude has consistent manners and limits you never asked for — those come from the system prompt, not from you.
- It's the original example of a powerful idea: *instructions placed in context, once, that steer every later turn.* [CLAUDE.md](#claudemd) and [Skills](#skillmd) are you doing the same thing for your own work.

In the basic web and desktop apps you don't write the system prompt — it's set for you. The concept matters more than the mechanics at this stage.

### Why it matters in this workshop

It makes "instructions live in the context" concrete, which is the bridge from "prompting" to context engineering, CLAUDE.md, and Skills.

**See also:** [Prompt](#prompt) · [Context](#context) · [CLAUDE.md](#claudemd)

---

## Markdown

> **In one line:** Markdown is a way of writing plain text so that simple symbols turn into formatting — without a toolbar, and readable even before it's rendered.

### In plain terms

You've used formatted documents your whole career (Word, Google Docs). Markdown is the same idea with a different trick: instead of clicking a "bold" button, you type a couple of symbols, and the text *becomes* formatted when displayed.

A few examples — left is what you type, right is what you get:

- `# Big heading` → a large heading
- `**important**` → **important**
- `- a list item` → a bullet point
- `[Bok Center](https://bokcenter.harvard.edu)` → a clickable link

The point: a Markdown file is just a text file. It opens anywhere, never breaks, and is perfectly readable even *without* the formatting applied. That makes it ideal for materials Claude reads and writes — including every doc in this glossary and the [CLAUDE.md](#claudemd) file.

You don't have to memorize the symbols. You can ask Claude to write Markdown for you; the goal here is just to **recognize it** and not be thrown by the `#` and `*`.

### Why it matters in this workshop

Almost everything Claude produces and reads in [Claude Code](#claude-code) is Markdown. Knowing "oh, those symbols are just formatting" removes a common early source of confusion.

**See also:** [CLAUDE.md](#claudemd) · [SKILL.md](#skillmd) · [Artifact](#artifact)

---

## Markdown — Intro & Cheatsheet

> **In one line:** A beginner intro to Markdown plus a one-screen syntax reference.

See the standalone [markdown-cheatsheet.md](glossary-md/markdown-cheatsheet.md) for the full cheatsheet.

**See also:** [Markdown](#markdown)

---

## HTML

> **In one line:** HTML is the language web pages are written in — when Claude Code hands you an HTML file instead of a plain document, you get something with real visual structure and clickable, interactive parts that opens in any browser.

### In plain terms

[Markdown](#markdown) gives you clean text with light formatting. **HTML** (HyperText Markup Language) is the step up: it's what every web page is made of, and it's what lets a document have genuine *layout* and *behavior* — columns and cards, collapsible sections, a search box, buttons that do something, and colors and spacing you control.

An analogy: Markdown is a tidy typed page; HTML is a small web page. Same words, but now they can be arranged, styled, and clicked. This glossary is the live example — the same entries exist as Markdown (plain, portable) *and* as an HTML site (navigable, styled, linked together).

Why you'd ask Claude Code for HTML output specifically:

- **More visual structure** — headings, tables, cards, side-by-side columns, a styled index page.
- **Interaction** — links between pages, expandable sections, a filter or search box, sortable tables.
- **Self-contained and shareable** — an `.html` file opens in any browser with no app and no install.
- **Consistent styling you control** — one linked CSS file restyles every page at once.

You don't write the HTML yourself. You describe what you want — "turn these notes into a browsable site with an index and a search box" — and Claude Code produces the files. The skill is still [context engineering](#context-engineering): say who it's for and how it should behave.

### Why it matters in this workshop

It widens the idea of an [artifact](#artifact): Claude Code's output doesn't have to be a flat document — it can be a small, styled, interactive site you hand to colleagues or students.

**See also:** [Artifact](#artifact) · [Markdown](#markdown) · [Claude Code](#claude-code)

---

## CLAUDE.md

> **In one line:** `CLAUDE.md` is a plain-text notes file you keep in a project folder; Claude Code reads it first, so it starts every conversation already knowing the basics.

### In plain terms

Remember the *Memento* problem: each conversation is a fresh "day," and Claude only knows what's written on the notes in front of it. `CLAUDE.md` is the note you leave *for next time* — pinned to the front of the folder.

When [Claude Code](#claude-code) opens a folder, it reads the `CLAUDE.md` there before doing anything else. So instead of re-explaining your project every session, you write it down once: what this folder is, who it's for, how you like things done, what to avoid.

A teaching-materials example might say: "This folder is readings for a freshman seminar. Keep summaries under 200 words. Don't change the `originals/` folder." From then on, Claude starts every conversation already knowing that.

It's just a Markdown file — readable text, no code. You can open and edit it like any document.

### Why it matters in this workshop

It's [context engineering](#context-engineering) made concrete and durable: the standing part of the briefing, written once instead of retyped every time.

**See also:** [Context](#context) · [Context Engineering](#context-engineering) · [SKILL.md](#skillmd) · [Claude Code](#claude-code)

---

## SKILL.md

> **In one line:** A `SKILL.md` is a reusable instruction packet for one specific kind of task — write the "how to do this well" once, and Claude can follow it every time that task comes up.

### In plain terms

[CLAUDE.md](#claudemd) describes a *project* ("this folder is X, work this way"). A **Skill** describes a *task* ("here's how to turn a messy reading list into a formatted syllabus") and is packaged so Claude can pull it in whenever that task arises — even across different projects.

The analogy: `CLAUDE.md` is the standing note on the office door; a Skill is a labeled recipe card in a box. When the relevant job comes up, Claude takes out that card and follows your steps, instead of improvising from scratch each time.

Why this is powerful for faculty:

- You capture *your* way of doing a recurring task once (your rubric, your format, your standards).
- It stays consistent across sessions and materials.
- It's shareable — a teaching team can use the same Skill.

At the beginner stage you mostly need the *concept*: repeatable, expert instructions for a task, kept in a file Claude can reach for.

### Why it matters in this workshop

It's the natural next step after [context engineering](#context-engineering): not just curating context for *this* conversation, but saving good context so it pays off again and again.

**See also:** [CLAUDE.md](#claudemd) · [Context Engineering](#context-engineering) · [Claude Code](#claude-code)

---

## Artifact

> **In one line:** An artifact is a finished thing Claude produces *alongside* the conversation — a document, a chart, a small interactive web page — shown in its own panel instead of buried in the chat.

### In plain terms

Most replies are just text in the conversation. Sometimes you want a *deliverable*: a clean handout, a table, a working mini web tool. Claude can produce these as **artifacts** — they open in a separate panel you can read, reuse, copy, or download, and Claude can revise them in place as you give feedback.

The shift for participants is one of imagination: Claude isn't only something you *ask* — it's something that *makes things for you*. A messy spreadsheet can come back as a sortable web page; rough notes as a formatted syllabus.

A few practical notes:

- An artifact is still produced from the [context](#context) — give it the real material and a clear sense of the audience and format.
- It's iterative: "make the headings bigger," "add a column" — it edits the same artifact rather than starting over.
- Many artifacts are written in [Markdown](#markdown) or are small web pages.

### Why it matters in this workshop

Artifacts are how the workshop expands participants' sense of what's possible early on — the bridge from "AI chatbot" to "this can produce real teaching materials."

**See also:** [Context](#context) · [Markdown](#markdown) · [HTML](#html)

---

## Data Classification

> **In one line:** Harvard sorts data by sensitivity level; on the temporary HUIT plan used in this workshop you may only put lower-sensitivity material (up to Level 2) into Claude until the Anthropic Enterprise agreement is in place.

### In plain terms

Harvard classifies information by how sensitive it is. The accounts you're using today are a **temporary HUIT-provided bridge** — kindly fast-tracked so the workshop could run — and they do **not** yet carry the Harvard–Anthropic Enterprise agreement that governs sensitive data.

What that means in practice:

- For today, use only material you'd be comfortable sharing — **nothing above Harvard Level 2.** Student work and research data wait for the agreement.
- This isn't a claim that Anthropic wants to leak your data; it doesn't. The Enterprise agreement is the formal safeguard, and until it's in place the safe assumption is "treat this like a regular account."
- Once Harvard rolls out the full Enterprise plan, the rules change — that's the point at which higher-sensitivity work becomes appropriate.

This intersects with two features you'll turn on: [memory](#memory) (Claude saving notes about your work) and [Cowork](#claude-cowork) (Claude reading a folder on your machine). Both are exactly where sensitive data could end up without you thinking about it — hence pointing Cowork at a deliberate project folder, not your Downloads.

### Why it matters in this workshop

This is the standing safety constraint behind everything in Day 1. Every "at your own risk" aside in the session traces back to this one rule: the bridge plan is temporary, and Level 2 is the ceiling until the agreement lands.

**See also:** [Anthropic](#anthropic) · [Memory](#memory) · [Claude Cowork](#claude-cowork)
