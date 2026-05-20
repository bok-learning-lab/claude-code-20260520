---
name: pdf-rename
description: Renames a folder of academic PDFs to the citation-style filename format "Lastname_Year_Title", "Last1 & Last2_Year_Title", or "Last1 et al_Year_Title". Use whenever the user wants to clean up, organize, normalize, or rename a folder of papers, preprints, or PDFs whose filenames are cryptic (e.g. arXiv IDs like "2605.16143v1.pdf", Elsevier IDs like "1-s2.0-...main.pdf", or ACM DOIs like "3772318.3790935.pdf"). Trigger on phrases like "rename my PDFs", "fix these paper filenames", "give my research folder real names", "make these papers easy to find", or any request that pairs a folder of papers with a citation/author/year naming pattern. The default target folder is /Users/orange/Downloads/research.
---

# pdf-rename

Rename a folder of academic PDFs to citation-style filenames so they're easy to scan and sort.

## The target filename format

For each PDF, build a new filename of the form:

```
<author_block>_<year>_<title>.pdf
```

Where:
- `<author_block>` depends on how many authors the paper has:
  - **1 author** → `Lastname` (e.g. `Smith`)
  - **2 authors** → `Last1 & Last2` (e.g. `Smith & Jones`)
  - **3 or more authors** → `Last1 et al` (e.g. `Smith et al`) — note: no period after "al", spaces around "et al"
- `<year>` is the four-digit publication year (e.g. `2026`).
- `<title>` is a ~6-word snippet of the paper's title that captures **what the paper is about**, drawn from the words of the title itself (don't paraphrase). Aim for the words a reader would skim for to recognize the paper — the system name, the method, the topic, the contribution. Not necessarily the literal first six words. Preserve the original capitalization. Remove characters that are unsafe in filenames.

The separator between the three sections is an underscore (`_`). Inside each section, spaces are spaces — do not turn the title or author block into snake_case.

### Examples

```
Dai et al_2026_Scenario-based test of AI ethical competence.pdf
Hu et al_2026_AI-powered learning-by-teaching for mathematics outcomes.pdf
Ye et al_2026_Autonomous Exploration for LLM Agents.pdf
Smith & Jones_2024_Toward a theory of foo.pdf
Vaswani et al_2017_Attention Is All You Need.pdf
```

The "~6" is approximate — anywhere from 4 to 8 words is fine if it reads naturally. The goal is "I can tell at a glance what this paper is about", not a mechanical character count.

## When to invoke this skill

The user wants a folder of PDFs (typically academic papers) renamed into citation form. Common triggers include "rename these papers", "fix the filenames in my research folder", "make these PDFs scannable", or simply dragging a messy folder of arXiv/Elsevier/ACM downloads into the conversation and asking for help organizing them.

If the user did not name a folder, assume `/Users/orange/Downloads/research`.

## How to run the skill

The skill is a three-step pipeline:

1. **Extract** the first-page text from every PDF in the folder using `scripts/extract.py`.
2. **Parse** the text yourself to determine author last names, year, and title for each paper, and build the proposed new filename. Compile these into a rename plan.
3. **Show the plan to the user**, get confirmation, then **apply** it with `scripts/apply.py`.

Each step is detailed below.

### Step 1 — Extract first-page text

Run the bundled extraction script against the folder. It uses `pypdf` to pull the text of page 1 from each PDF and emits one JSON object per file:

```bash
python3 <SKILL_DIR>/scripts/extract.py "<folder>" --out /tmp/pdf_rename_extract.json
```

`<SKILL_DIR>` is the absolute path to this skill's folder (the one containing `SKILL.md`). `<folder>` is the directory of PDFs.

The script prints `pip install pypdf` instructions if the library is missing. Install it once with `pip install pypdf --break-system-packages` and rerun.

The output JSON looks like:

```json
[
  {
    "path": "/Users/.../research/2605.16143v1.pdf",
    "filename": "2605.16143v1.pdf",
    "page1_text": "Look Before You Leap: Autonomous Exploration for\nLLM Agents\nZiang Ye1,2...",
    "page2_snippet": "..."
  },
  ...
]
```

`page2_snippet` is the first ~1500 characters of page 2. Use it **only** for year detection when page 1 doesn't have one — for some publishers (notably ACM) the copyright line and "ACM Reference Format" block live on page 2. Always extract the title and authors from `page1_text`.

### Step 2 — Parse and build the rename plan

Read the JSON. For each entry, extract the metadata from `page1_text`:

**Title.** First reconstruct the **full title** so you have something to choose from. The title is almost always the first non-empty block of text on page 1, often spanning two or three lines. Join those lines with single spaces, undo soft hyphens / line-break hyphenation (e.g. `multiple-choice \n test` is fine as-is, but `multi-\nchoice` should become `multichoice`).

Then **choose a ~6-word snippet** from the title that captures what the paper is about. Use words from the title — don't paraphrase. Good snippets usually include the system name (e.g. `AmIWrite`), the method (e.g. `learning-by-teaching`), the domain (e.g. `LLM Agents`), or the contribution (e.g. `Autonomous Exploration`), and skip purely structural words like "The alignment of" or "Development and validation of a". The aim is that someone glancing at the folder can guess the paper from its filename. 4–8 words is fine; the exact count matters less than readability.

Examples of good snippet picks:
- Full title `Look Before You Leap: Autonomous Exploration for LLM Agents` → snippet `Autonomous Exploration for LLM Agents` (or keep the memorable hook: `Look Before You Leap LLM Agents`)
- Full title `AmIWrite: Exploring Scalable One-on-One Handwriting-Based Tutoring for Mathematical Problem-Solving with an LLM-Powered AI Tutor` → snippet `AmIWrite Handwriting-Based AI Math Tutor`
- Full title `Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most` → snippet `LLM Tutoring Agents Struggle With Feedback`
- Full title `Development and validation of a scenario-based multiple-choice test of AI ethical competence (AIEC) using item response theory` → snippet `Scenario-based test of AI ethical competence`

Clean the snippet of characters that are problematic in filenames on macOS/Linux/Windows: `/ \ : * ? " < > |`. The simplest move is to delete colons and replace slashes with a space, then collapse runs of whitespace. Keep apostrophes, hyphens, parentheses, and ampersands — they're fine on all three OSes.

Do not lowercase or snake_case the title. Preserve original capitalization.

**Authors.** The author block sits just below the title. For each author, the **last name** is the last whitespace-separated alphabetic token in their name, after stripping footnote markers and affiliation symbols. Common things to strip from the end of a name:

- Trailing single letters used as affiliation markers (`Yun Daia,*` → `Yun Dai`, the trailing `a` and `,*` go away)
- Trailing digits (`Ziang Ye1,2` → `Ziang Ye`)
- Asterisks, daggers, section signs (`Mingjia Hu *` → `Mingjia Hu`)
- The Unicode characters `∗ † ‡ §`

So `Yun Daia,*` → last name `Dai`; `Ziang Ye1,2∗` → last name `Ye`; `Mingjia Hu a` → last name `Hu`; `Ziyi Liu∗` → last name `Liu`.

For compound surnames like `van der Berg` or `de la Cruz`, keep the particle (the last name is `van der Berg`, not `Berg`). When in doubt, prefer the form the author would actually use in a citation.

Count the **distinct authors** to decide the author block format:
- 1 author → just the last name
- 2 authors → `Last1 & Last2`
- 3+ authors → `Last1 et al` (where Last1 is the **first listed author's** last name)

**Year.** Look for a four-digit year (1990–2030 range, to be safe). Reliable signals, in order of preference:

1. Conference/journal banner: `Computers & Education 251 (2026) 105642`, `CHI '26`, etc.
2. Copyright line: `© 2026 The Authors`, `0360-1315/© 2026 ...`
3. arXiv banner: `arXiv:2605.16143v1 [cs.AI] 15 May 2026`
4. The `Received... Accepted...` line on Elsevier papers — use the **Accepted** year.
5. ACM "Reference Format" block: `Ziyi Liu, ... 2026. AmIWrite: ...` — this is often on page 2 only.

Start with `page1_text`. If you can't find a year there, check `page2_snippet` — ACM conference papers put their copyright/year on page 2. If neither has it, fall back to the **arXiv ID in the filename**: arXiv IDs of the form `YYMM.NNNNN` encode year+month, so `2605.16207v1.pdf` is May 2026 → year `2026`. If even that fails, use `unknown` and flag it to the user when you show the plan.

**Build the new filename.** Join `<author_block>_<year>_<title>.pdf`. Sanity-check that the result fits in 255 characters (filesystem limit on common filesystems). If it's longer, drop title words from the end until it fits.

**Compile the plan** as a JSON array:

```json
[
  {"old": "/abs/path/old.pdf", "new": "/abs/path/Dai et al_2026_Development and validation of a scenario.pdf"},
  ...
]
```

Save it to e.g. `/tmp/pdf_rename_plan.json`.

### Step 3 — Show the plan, confirm, apply

Before touching any files, show the user a clear before-and-after list (old filename → new filename). If any entries have `unknown` for year or look obviously wrong (e.g. a one-word title that smells like a section header rather than a paper title), call those out specifically and ask the user to confirm or correct them.

Once the user confirms, apply the plan:

```bash
python3 <SKILL_DIR>/scripts/apply.py /tmp/pdf_rename_plan.json
```

The apply script:
- Validates that every `old` exists and every `new` does not already exist (preventing accidental overwrite).
- Detects collisions where two papers would end up with the same `new` name and aborts before doing anything.
- Performs the rename in place.
- Prints a summary of what it did.

If you want to preview without changing files, pass `--dry-run`.

## Things to watch out for

The first-page text from PDFs is often messy: ligatures may render oddly, line breaks may appear mid-word, footnote markers cluster around author names, and abstract/affiliation/keyword sections can intrude before the author list ends. Read the extracted text carefully rather than running it through a rigid regex. The whole reason this skill orchestrates an LLM step rather than relying on pure scripting is that you're better at this kind of fuzzy text parsing than any regex.

If a particular PDF is clearly an outlier — a scanned book chapter with no useful text on page 1, a working paper with no year, a multi-paper compendium — just say so to the user and skip that file rather than fabricating metadata.

After renaming, the original cryptic filenames (DOIs, arXiv IDs) are lost from the filename, but they're still recoverable from the paper's text or from the URL the user downloaded from. If the user might want the originals preserved, suggest they back up the folder first — though the user originally asked for in-place renaming, so don't force this.