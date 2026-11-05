(xub-assets-agents-md)=
# Global instructions `AGENTS.md`

The `src/xub/assets/agents/AGENTS.md` file contains the instructions that
every AI coding agent loads at the start of a session, regardless of the
project. `AGENTS.md` is the native format of Codex and the common fallback of
the other agents, so the same file is installed under each of the names they
expect:

| Agent                    | Target file           |
| ------------------------ | --------------------- |
| Claude Code              | `~/.claude/CLAUDE.md` |
| Codex                    | `~/.codex/AGENTS.md`  |
| Gemini CLI / Antigravity | `~/.gemini/GEMINI.md` |

Project-local instructions take precedence over this file when they are more
specific and compatible.

## Sections

General rules
: Inspect the project before modifying it, prefer small and verifiable
  changes, protect secrets, avoid destructive operations without approval,
  and use the `xub-*` skills ({ref}`xub-assets-skills`) when relevant.

Git Guidelines
: Commit message style (the subject ends with a period) and when to create
  worktrees.

Documentation Formatting
: How to resolve the fill column (`TEXT_COLUMN_LIMIT` from the project's
  `.env`, then from the environment, then `78`) and how to wrap prose in
  Markdown and reStructuredText files without altering code blocks, tables,
  URLs, or other whitespace-sensitive constructs.

Python
: String quoting conventions (double quotes for human-readable text, single
  quotes for everything else, `"""` for docstrings), the Ruff
  `quote-style = "preserve"` setting, and the layout of package
  documentation (Markdown with `myst-parser`, and a `docs/source/<project>`
  folder that mirrors the code and uses `sphinx.ext.autodoc`).

## Source

```{literalinclude} /../../src/xub/assets/agents/AGENTS.md
:language: markdown
```
