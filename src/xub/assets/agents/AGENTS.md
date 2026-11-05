# AI coding-agent instructions

- Inspect the project and its existing conventions before modifying files.
- Prefer small, verifiable changes and run relevant tests.
- Prefer concise documentation.
- Do not disclose secrets or execute destructive operations without explicit approval.
- Follow project-local instructions when they are more specific and compatible.
- Use the available `xub` skills when relevant (`/xub:<skill>` in Claude Code, `<skill>` in other agents); do not assume all agents support the same invocation syntax.

## Git Guidelines

- Always end the subject line or summary of a commit message with a period (`.`). For example: "Initialize documentation project."
- Create worktrees only if a task is large enough to require multiple commits, or if a task is accidentally initiated on the `main` branch.

## Documentation Formatting

When creating or editing Markdown (`.md`) or reStructuredText (`.rst`) files, use the `format-prose` skill.

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

When creating or extending the documentation of a Python package, use the `scaffold-python-docs` skill.
