#!/usr/bin/env python3
"""
generate.py — Split claude-code-tools-and-terms.md into per-entry HTML + MD files.

Usage (run from any directory):
    python3 resources/day-3/claude-code-tools-and-terms/generate.py
"""
from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent.resolve()
SRC_FILE   = SCRIPT_DIR.parent / "claude-code-tools-and-terms.md"
HTML_DIR   = SCRIPT_DIR / "tools-and-terms-html"
MD_DIR     = SCRIPT_DIR / "tools-and-terms-md"
SITE_TITLE = "Claude Code: Tools and Terms"

# ── slug map ───────────────────────────────────────────────────────────────
HEADING_TO_SLUG: dict[str, str] = {
    "Claude Code": "claude-code",
    "Context Window": "context-window",
    "CLAUDE.md": "claude-md",
    "CLAUDE.local.md": "claude-local-md",
    "Auto Memory": "auto-memory",
    "Skills (`.claude/skills/`)": "skills",
    "Agents / Subagents (`.claude/agents/`)": "agents",
    "Rules (`.claude/rules/`)": "rules",
    "Path-Specific Rules": "path-specific-rules",
    "Plan Mode": "plan-mode",
    "Permissions": "permissions",
    "Hooks": "hooks",
    "MCP Servers": "mcp-servers",
    "Plugins": "plugins",
    "Non-Interactive Mode": "non-interactive-mode",
    "Checkpoints": "checkpoints",
    "Sessions": "sessions",
    "/init": "slash-init",
    "/clear": "slash-clear",
    "/compact": "slash-compact",
    "/memory": "slash-memory",
    "/permissions (command)": "slash-permissions",
    "/rewind": "slash-rewind",
    "/rename": "slash-rename",
    "/btw": "slash-btw",
    "/sandbox": "slash-sandbox",
    "Give Claude a way to verify its work": "prompt-verify",
    "Explore first, then plan, then code": "prompt-explore-plan-code",
    "Provide specific context": "prompt-specific-context",
    "Reference files with @": "prompt-reference-files",
    "Course-correct early": "prompt-course-correct",
    "Use subagents for investigation": "prompt-subagents",
    "Common failure patterns to avoid": "prompt-failure-patterns",
}

SECTIONS: list[tuple[str, list[str]]] = [
    ("Core Concepts", [
        "claude-code", "context-window", "claude-md", "claude-local-md",
        "auto-memory", "skills", "agents", "rules", "path-specific-rules",
        "plan-mode", "permissions", "hooks", "mcp-servers", "plugins",
        "non-interactive-mode", "checkpoints", "sessions",
    ]),
    ("Slash Commands", [
        "slash-init", "slash-clear", "slash-compact", "slash-memory",
        "slash-permissions", "slash-rewind", "slash-rename", "slash-btw",
        "slash-sandbox",
    ]),
    ("Prompting Patterns", [
        "prompt-verify", "prompt-explore-plan-code", "prompt-specific-context",
        "prompt-reference-files", "prompt-course-correct", "prompt-subagents",
        "prompt-failure-patterns",
    ]),
]

ANCHOR_TO_HTML: dict[str, str] = {
    "#claude-code": "claude-code.html",
    "#context-window": "context-window.html",
    "#claudemd": "claude-md.html",
    "#claudelocalmd": "claude-local-md.html",
    "#auto-memory": "auto-memory.html",
    "#skills-claudeskills": "skills.html",
    "#agents--subagents-claudeagents": "agents.html",
    "#rules-clauderules": "rules.html",
    "#path-specific-rules": "path-specific-rules.html",
    "#plan-mode": "plan-mode.html",
    "#permissions": "permissions.html",
    "#hooks": "hooks.html",
    "#mcp-servers": "mcp-servers.html",
    "#plugins": "plugins.html",
    "#non-interactive-mode": "non-interactive-mode.html",
    "#checkpoints": "checkpoints.html",
    "#sessions": "sessions.html",
    "#init": "slash-init.html",
    "#clear": "slash-clear.html",
    "#compact": "slash-compact.html",
    "#memory": "slash-memory.html",
    "#permissions-command": "slash-permissions.html",
    "#rewind": "slash-rewind.html",
    "#rename": "slash-rename.html",
    "#btw": "slash-btw.html",
    "#sandbox": "slash-sandbox.html",
    "#give-claude-a-way-to-verify-its-work": "prompt-verify.html",
    "#explore-first-then-plan-then-code": "prompt-explore-plan-code.html",
    "#provide-specific-context": "prompt-specific-context.html",
    "#reference-files-with-": "prompt-reference-files.html",
    "#course-correct-early": "prompt-course-correct.html",
    "#use-subagents-for-investigation": "prompt-subagents.html",
}
ANCHOR_TO_MD = {k: v.replace(".html", ".md") for k, v in ANCHOR_TO_HTML.items()}


# ── markdown → html ────────────────────────────────────────────────────────

def esc(s: str) -> str:
    return html_lib.escape(s, quote=True)


def inline_html(text: str) -> str:
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # split on inline code spans to avoid mangling their content
    parts = re.split(r'(`[^`\n]+`)', text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(f'<code>{esc(part[1:-1])}</code>')
        else:
            s = esc(part)
            s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
            s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
            s = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', s)
            s = re.sub(
                r'\[([^\]]+)\]\(([^)]+)\)',
                lambda m: (
                    f'<a href="{esc(ANCHOR_TO_HTML.get(m.group(2), m.group(2)))}">'
                    f'{m.group(1)}</a>'
                ),
                s,
            )
            out.append(s)
    return ''.join(out)


def md_to_html(md: str) -> str:
    """Convert a markdown string to an HTML fragment."""
    lines = md.split('\n')
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r'[-*_]{3,}', line.strip()):
            out.append('<hr>')
            i += 1
            continue

        # fenced code block
        if line.startswith('```'):
            lang = line[3:].strip()
            code: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1  # closing fence
            cls = f' class="language-{esc(lang)}"' if lang else ''
            code_text = esc('\n'.join(code))
            out.append(f'<pre><code{cls}>{code_text}</code></pre>')
            continue

        # blockquote
        if line.startswith('> '):
            bq: list[str] = []
            while i < len(lines) and lines[i].startswith('> '):
                bq.append(lines[i][2:])
                i += 1
            bq_html = md_to_html('\n'.join(bq))
            out.append(f'<blockquote>{bq_html}</blockquote>')
            continue

        # table (detected by separator row on next line)
        if (
            '|' in line
            and i + 1 < len(lines)
            and re.match(r'\|?[\s\-:|]+\|', lines[i + 1])
        ):
            header = [c.strip() for c in line.strip('|').split('|')]
            i += 2  # skip separator row
            rows: list[list[str]] = []
            while i < len(lines) and '|' in lines[i]:
                rows.append([c.strip() for c in lines[i].strip('|').split('|')])
                i += 1
            thead = '<tr>' + ''.join(f'<th>{inline_html(c)}</th>' for c in header) + '</tr>'
            tbody = ''.join(
                '<tr>' + ''.join(f'<td>{inline_html(c)}</td>' for c in row) + '</tr>'
                for row in rows
            )
            out.append(
                f'<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>'
            )
            continue

        # heading within entry body (## or deeper → h2/h3/…)
        m = re.match(r'^(#{2,6})\s+(.*)', line)
        if m:
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline_html(m.group(2))}</h{lvl}>')
            i += 1
            continue

        # unordered list
        if re.match(r'^[*\-+] ', line):
            items: list[str] = []
            while i < len(lines) and re.match(r'^[*\-+] ', lines[i]):
                items.append(inline_html(lines[i][2:].lstrip()))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
            continue

        # ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append(inline_html(re.sub(r'^\d+\. ', '', lines[i])))
                i += 1
            out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>')
            continue

        # paragraph
        out.append(f'<p>{inline_html(line)}</p>')
        i += 1

    return '\n'.join(out)


def remap_md_links(text: str) -> str:
    """Replace #anchor links with .md file links for cross-linking in MD files."""
    def repl(m: re.Match) -> str:
        return f'[{m.group(1)}]({ANCHOR_TO_MD.get(m.group(2), m.group(2))})'
    return re.sub(r'\[([^\]]+)\]\((#[^)]+)\)', repl, text)


# ── HTML page template ─────────────────────────────────────────────────────

def html_page(
    title_raw: str,
    body: str,
    prev_slug: str | None,
    next_slug: str | None,
) -> str:
    nav_items = ['<a href="index.html">← Index</a>']
    if prev_slug:
        nav_items.append(f'<a href="{prev_slug}.html">← Prev</a>')
    if next_slug:
        nav_items.append(f'<a href="{next_slug}.html">Next →</a>')
    nav = '<nav class="topnav">' + ' &nbsp;·&nbsp; '.join(nav_items) + '</nav>'

    title_html = inline_html(title_raw)
    title_plain = re.sub(r'`([^`]+)`', r'\1', title_raw)

    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{esc(title_plain)} — {esc(SITE_TITLE)}</title>\n'
        '<link rel="stylesheet" href="style.css">\n'
        '</head>\n'
        '<body>\n'
        '<main class="entry">\n'
        f'{nav}\n'
        f'<h1>{title_html}</h1>\n'
        f'{body}\n'
        '</main>\n'
        '</body>\n'
        '</html>'
    )


# ── parsing ────────────────────────────────────────────────────────────────

def parse_entries(src: str) -> dict[str, dict]:
    matches = list(re.finditer(r'^## (.+)$', src, re.MULTILINE))
    entries: dict[str, dict] = {}

    for idx, m in enumerate(matches):
        heading = m.group(1).strip()
        slug = HEADING_TO_SLUG.get(heading)
        if slug is None:
            print(f'  [skip] no slug mapped for: {heading!r}', file=sys.stderr)
            continue

        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(src)
        body = src[start:end].strip()

        # strip section-header bleeds (e.g. ---\n---\n# Slash Commands\n…)
        body = re.sub(r'\n+---\n+---\n+# .*', '', body, flags=re.DOTALL).strip()
        # strip trailing --- entry separator
        body = re.sub(r'\n---\s*$', '', body).strip()

        entries[slug] = {"title": heading, "body_md": body}

    return entries


# ── writers ────────────────────────────────────────────────────────────────

def one_liner(body_md: str) -> str:
    m = re.search(r'^> \*\*In one line:\*\* (.+?)$', body_md, re.MULTILINE)
    if m:
        return inline_html(m.group(1))
    m = re.search(r'^> \*\*(.+?)\*\*', body_md, re.MULTILINE)
    if m:
        return inline_html(m.group(1))
    return ''


def write_html_entry(slug: str, entry: dict, all_slugs: list[str]) -> None:
    idx = all_slugs.index(slug)
    prev_s = all_slugs[idx - 1] if idx > 0 else None
    next_s = all_slugs[idx + 1] if idx < len(all_slugs) - 1 else None
    page = html_page(entry['title'], md_to_html(entry['body_md']), prev_s, next_s)
    (HTML_DIR / f'{slug}.html').write_text(page, encoding='utf-8')


def write_md_entry(slug: str, entry: dict) -> None:
    content = f'# {entry["title"]}\n\n{remap_md_links(entry["body_md"])}\n'
    (MD_DIR / f'{slug}.md').write_text(content, encoding='utf-8')


def write_html_index(entries: dict[str, dict]) -> None:
    sections_html: list[str] = []
    for section_title, slugs in SECTIONS:
        rows = ''.join(
            f'<tr>'
            f'<td><a href="{s}.html">{inline_html(entries[s]["title"])}</a></td>'
            f'<td>{one_liner(entries[s]["body_md"])}</td>'
            f'</tr>'
            for s in slugs if s in entries
        )
        sections_html.append(
            f'<h2>{esc(section_title)}</h2>'
            f'<table><thead><tr><th>Term</th><th>One-line gist</th></tr></thead>'
            f'<tbody>{rows}</tbody></table>'
        )

    body = '\n'.join(sections_html)
    page = (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>Index — {esc(SITE_TITLE)}</title>\n'
        '<link rel="stylesheet" href="style.css">\n'
        '</head>\n'
        '<body>\n'
        '<main class="entry">\n'
        f'<h1>{esc(SITE_TITLE)}</h1>\n'
        '<p>A dictionary-style reference for beginners. Each entry defines one concept, '
        'explains it in plain language, and shows what it looks like in practice. '
        'Open an entry or browse by section.</p>\n'
        f'{body}\n'
        '</main>\n'
        '</body>\n'
        '</html>'
    )
    (HTML_DIR / 'index.html').write_text(page, encoding='utf-8')


def write_md_index(entries: dict[str, dict]) -> None:
    lines = [f'# {SITE_TITLE}', '', 'A dictionary-style reference for beginners.', '']
    for section_title, slugs in SECTIONS:
        lines += [f'## {section_title}', '']
        lines += [
            f'- [{entries[s]["title"]}]({s}.md)' for s in slugs if s in entries
        ]
        lines.append('')
    (MD_DIR / '00-index.md').write_text('\n'.join(lines), encoding='utf-8')


# ── main ───────────────────────────────────────────────────────────────────

def main() -> None:
    if not SRC_FILE.is_file():
        print(f'error: source not found: {SRC_FILE}', file=sys.stderr)
        sys.exit(1)

    src = SRC_FILE.read_text(encoding='utf-8')
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    MD_DIR.mkdir(parents=True, exist_ok=True)

    entries = parse_entries(src)
    all_slugs = [s for _, slugs in SECTIONS for s in slugs if s in entries]

    print(f'parsed {len(entries)} entries')

    # copy style.css from glossary
    css_src = SCRIPT_DIR.parent.parent / 'ai-glossary' / 'glossary-html' / 'style.css'
    if css_src.is_file():
        (HTML_DIR / 'style.css').write_bytes(css_src.read_bytes())
        print('  copied style.css from glossary')
    else:
        print(f'  warning: style.css not found at {css_src}', file=sys.stderr)

    for slug in all_slugs:
        if slug not in entries:
            print(f'  [skip] not parsed: {slug}', file=sys.stderr)
            continue
        write_html_entry(slug, entries[slug], all_slugs)
        write_md_entry(slug, entries[slug])
        print(f'  {slug}')

    write_html_index(entries)
    write_md_index(entries)

    print(f'\ndone — {len(all_slugs)} entries across {len(SECTIONS)} sections')
    print(f'  HTML → {HTML_DIR}')
    print(f'  MD   → {MD_DIR}')
    print(f'\n  Open locally: file://{HTML_DIR}/index.html')


if __name__ == '__main__':
    main()
