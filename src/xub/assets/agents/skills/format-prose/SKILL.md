---
name: format-prose
description: Wrap and reflow prose in Markdown (.md) and reStructuredText (.rst) files at the project's fill column. Use whenever creating or editing a .md or .rst file, except documents for AI agents such as skills or agent instructions.
---

# Format prose

Apply these rules when creating or editing Markdown (`.md`) or
reStructuredText (`.rst`) files.

## Scope

Do not apply these rules to documents related to AI agents, such as skills
(`SKILL.md`), `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.

## Resolve the fill column

Use the first value found, in this order:

1. `TEXT_COLUMN_LIMIT` defined in the project's `.env` file.
2. The `TEXT_COLUMN_LIMIT` environment variable.
3. `78` as the default.

The project's `.env` value takes precedence over the process environment. For
example:

```bash
limit=$(sed -n 's/^TEXT_COLUMN_LIMIT=["'\'']\{0,1\}\([0-9]*\).*/\1/p' .env 2>/dev/null)
echo "${limit:-${TEXT_COLUMN_LIMIT:-78}}"
```

## Wrap prose

- Treat the resolved value as the maximum line length for prose.
- Wrap and reflow prose at the resolved fill column.
- Separate section headings from their following content with exactly one
  blank line.
- Preserve intentional hard line breaks.
- Preserve the native syntax and conventions of the document format.

## Do not wrap

Leave content alone where reflowing would alter its meaning or document
structure, including:

- fenced or indented code blocks;
- literal and code blocks;
- tables;
- URLs and other non-breakable references;
- directives or constructs whose formatting is whitespace-sensitive.

## Verify

After editing, list prose lines longer than the limit and check that each one
is an exception from the list above:

```bash
awk -v max="$limit" 'length > max {print FILENAME ":" FNR ": " length}' FILE...
```
