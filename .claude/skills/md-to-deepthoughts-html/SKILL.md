---
name: md-to-deepthoughts-html
description: Convert a Markdown file into a single, self-contained HTML file styled like the "Deep thoughts" essay pages from /Users/mk/Development/ai-enhancement-stories (cream/serif Dario-style layout, Newsreader font, scoped to the article view — not the index). Writes the .html alongside the source .md. Includes screen + mobile + print styles, plus a Print button (window.print) and a Copy MD button. Use when the user asks to turn an .md into an html doc, render markdown as a deep-thoughts-style page, generate a standalone html version of an essay, or print/export a markdown essay to html. Triggers on phrasings like "make an html of this md", "convert X.md to deepthoughts html", "render this essay as a standalone html", or "give me a printable html of this markdown".
---

# md-to-deepthoughts-html

## What this skill does

Given an input Markdown file, produce a **single, self-contained `.html` file** placed next to the source (same directory, same basename, `.html` extension). The HTML renders the markdown using the same visual design as the live "Deep thoughts" essay view in `/Users/mk/Development/ai-enhancement-stories/app/deep-thoughts/[slug]/` — Dario-style cream/serif typography on `rgb(240, 238, 230)`, Newsreader font.

Hard constraints:

- **One static `.html` file.** No React, no build step, no Next.js, no external assets besides Google Fonts.
- **No client-side Markdown library.** You — Claude — convert the Markdown to literal HTML at authoring time.
- **TOC sidebar and footer are intentionally omitted** for the standalone view. The header keeps the author name plus a Print and Copy-MD button.

## Inputs

The user supplies a path to a `.md` file. If they don't, ask. Treat anything else as a parameter:

- **Author name** — defaults to `Marlon Kuzmick`. Override if asked.
- **Output path** — defaults to `<source-dir>/<basename>.html`. Override if asked.

## Assets

This skill ships two assets in `assets/`:

- `assets/essay-style.css` — the full screen/mobile/print stylesheet. Read this verbatim and inline into the template.
- `assets/template.html` — the HTML skeleton with `{{...}}` placeholders.

Do not rewrite the CSS from memory. Read the file. If the user wants design tweaks, edit `essay-style.css` directly so future runs inherit the change.

## Workflow

### 1. Read the source

Read the user-supplied `.md` file with the Read tool.

### 2. Extract title, subtitle, date

Try YAML frontmatter first (`title:`, `subtitle:`, `date:`). If there's no frontmatter, fall back to the file body:

- **Title** — the first `# ` heading line (strip the `# `).
- **Subtitle** — if the line(s) immediately after the title (skipping blank lines) form a non-heading paragraph, treat that paragraph as the subtitle. This matches `_content/deep-thoughts/CLAUDE.md`'s convention of "a one- or two-sentence subtitle immediately after" the title. If the next non-blank thing is another heading (`##`/`###`) or a list/quote, there is no subtitle.
- **Date** — only from frontmatter. Do not invent.

If the source is ambiguous (e.g., no `# ` heading, or the first paragraph isn't clearly a subtitle), ask the user before guessing.

### 3. Convert the Markdown body to HTML

Strip frontmatter and the leading `# Title` + subtitle paragraph from the body before converting. Then walk the remaining markdown and emit literal HTML using the mapping below.

| Markdown | HTML |
|---|---|
| `## Heading` | `<h2>Heading</h2>` |
| `### Heading` | `<h3>Heading</h3>` |
| `#### Heading` | `<h4>Heading</h4>` |
| Blank-line-separated paragraph | `<p>…</p>` |
| `**bold**` | `<strong>bold</strong>` |
| `*italic*` or `_italic_` | `<em>italic</em>` |
| `[text](url)` | `<a href="url">text</a>` |
| `> quoted` (one or more consecutive lines) | `<blockquote><p>quoted</p></blockquote>` |
| `- item` / `* item` list | `<ul><li>…</li></ul>` |
| `1. item` list | `<ol><li>…</li></ol>` |
| `---` on its own line | `<hr>` |
| Fenced ```` ``` ```` block | `<pre><code>…</code></pre>` |
| Inline `` `code` `` | `<code>code</code>` |
| GFM tables (`| a | b |` / `|---|---|`) | `<table><thead><tr><th>…</th></tr></thead><tbody><tr><td>…</td></tr></tbody></table>` |

Escaping:

- In body text (outside fenced code), escape literal `<`, `>`, `&` to `&lt;`, `&gt;`, `&amp;`.
- Inside `<pre><code>` blocks, escape the same three characters from the raw source.
- In `<a href="…">` URLs, escape `"` to `&quot;` and `&` to `&amp;`.
- Preserve inline HTML the author already wrote (e.g. `<sup>`, `<br>`) — only escape when the source character clearly isn't intentional HTML.

Headings only run up to `####`. The skill never emits a body `<h1>` — the article's `<h1>` is the title, and the source's leading `# Title` was already consumed in step 2.

### 4. Build the template fills

Load `assets/essay-style.css` and `assets/template.html`. Substitute:

| Placeholder | Value |
|---|---|
| `{{TITLE}}` | The extracted title, HTML-escaped. |
| `{{AUTHOR}}` | Author name (default `Marlon Kuzmick`). |
| `{{STYLES}}` | Full contents of `assets/essay-style.css`, inlined unchanged. |
| `{{SUBTITLE_BLOCK}}` | `      <p class="subtitle">…</p>` if a subtitle exists, else an empty string. |
| `{{DATE_BLOCK}}` | `      <p class="date">…</p>` if a date exists, else an empty string. |
| `{{BODY_HTML}}` | The converted body HTML, indented two spaces deeper than `<article>` for readability (cosmetic only). |
| `{{RAW_MD}}` | The **original** markdown source (before stripping frontmatter / title) so Copy MD copies what the user wrote. See escaping note. |

**Escaping `{{RAW_MD}}`** — it goes inside `<script type="text/x-markdown-source">…</script>`. The only sequence that can break out is a literal `</script` substring. Replace `</script` with `<\/script` (case-insensitive) in the raw markdown before substituting. No other escaping is needed; whitespace and other characters survive verbatim.

### 5. Write the file

Default output path: same directory as the source `.md`, same basename, `.html` extension. Use the Write tool. After writing, tell the user the path.

### 6. Sanity check (silent)

Before reporting done, mentally verify:

- The title `<h1>` is non-empty.
- No `{{…}}` placeholders remain in the output.
- Heading hierarchy doesn't skip levels in a way that suggests a conversion bug.
- No raw markdown syntax (e.g. `**`, `[…](…)`) leaked into the body — a quick scan of the generated HTML is enough.
- Fenced code blocks didn't swallow following content.

Don't dump these checks to the user unless something failed.

## Tips for edge cases

- **No `# ` heading in the source.** Ask the user for a title.
- **The leading paragraph isn't really a subtitle.** Ask — better than guessing wrong, since the subtitle gets prominent italic styling.
- **Source is heavy with custom HTML.** Pass it through; the stylesheet's `.essay-content` selectors handle most tags. If the author used unusual tags (e.g. `<aside>`, `<figure>`), they'll inherit body styles — flag this to the user only if it looks visibly broken.
- **Footnotes** (`[^1]` / `[^1]: …`). Render `[^N]` as `<sup><a href="#fn-N" id="fnref-N">N</a></sup>` and the definitions as an `<ol class="footnotes">` at the end with back-refs. The base stylesheet doesn't include footnote-specific rules, but the default list styling is fine.
- **Smart-quote / em-dash conversion.** Leave punctuation as the author wrote it. Don't auto-convert.

## Reference: where the design came from

If the user asks why the styling looks the way it does, point them at:

- `components/essay-layout.module.css` — original source of truth
- `components/essay-layout.tsx` — the live React view
- `app/deep-thoughts/[slug]/page.tsx` — the route this is mimicking
- `HANDOFF-md-to-html.md` — the prior design doc that fed this skill
