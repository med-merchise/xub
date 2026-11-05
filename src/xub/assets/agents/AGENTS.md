# AI coding-agent instructions

- Inspect the project and its existing conventions before modifying files.
- Prefer small, verifiable changes and run relevant tests.
- Prefer concise documentation.
- Do not disclose secrets or execute destructive operations without explicit approval.
- Follow project-local instructions when they are more specific and compatible.
- Use available `xub-*` skills when relevant; do not assume all agents support the same invocation syntax.

## Git Guidelines

- Always end the subject line or summary of a commit message with a period (`.`). For example: "Initialize documentation project."
- Create worktrees only if a task is large enough to require multiple commits, or if a task is accidentally initiated on the `main` branch.

## Documentation Formatting

<!-- ChatGPT prompting -->

When creating or editing MarkDown (`.md`) or reStructuredText (`.rst`) files:

- Determine the fill column using the following precedence:
  1. `TEXT_COLUMN_LIMIT` defined in the project's `.env` file.
  2. The `TEXT_COLUMN_LIMIT` environment variable.
  3. `78` as the default.
- The project's `.env` value takes precedence over the process environment.
- Treat the resolved value as the maximum line length for prose.
- Wrap and reflow prose at the resolved fill column.
- Separate section headings from their following content with exactly one
  blank line.
- Do not wrap content where reflowing would alter its meaning or document structure, including:
  - fenced or indented code blocks;
  - literal and code blocks;
  - tables;
  - URLs and other non-breakable references;
  - directives or constructs whose formatting is whitespace-sensitive.
- Preserve intentional hard line breaks.
- Preserve the native syntax and conventions of the document format.
- Exclude from this rule all documents related to AI agents, such as skills.

## Python

### Python String Quoting Conventions

Use string quotation marks according to the semantic purpose of the string:

- **Double quotes (`"`)**: Use for natural language text intended for human consumption, including messages, descriptions, documentation, and user-facing output.
- **Single quotes (`'`)**: Use for all other strings, including identifiers, dictionary keys, configuration values, paths, regular expressions, and machine-readable literals.
- **Docstrings**: Always use triple double quotes (`"""`) in accordance with PEP 257.
- **Embedded quotes**: Prefer the designated quotation style, but use the alternative when it avoids unnecessary escaping.
- **Consistency**: Apply these conventions to both new and modified code.

For example: `parser.add_argument('--verbose', help="Enable verbose output.")`.

When generating `pyproject.toml`, Configure Ruff to preserve the existing quotation style rather than enforce a uniform style:

```
[tool.ruff.format]
quote-style = "preserve"
```

### Python package documentation

Documentation files will use Markdown; `myst-parser` must be included in the `docs` dependency group.

Source code documentation will be located in a subfolder within `docs/source`—sharing the project's name and mirroring the code's structure—and will use `sphinx.ext.autodoc` to incorporate docstrings.
