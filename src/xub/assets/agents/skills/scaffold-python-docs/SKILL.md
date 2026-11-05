---
name: scaffold-python-docs
description: Set up or extend Sphinx documentation for a Python package using Markdown (myst-parser) and autodoc, with a docs/source/<project> folder that mirrors the code. Use when creating a docs/ tree for a Python project, adding pages for new modules, or wiring docstrings into the documentation.
---

# Scaffold Python package documentation

## Rules

- Documentation files use Markdown. Include `myst-parser` in the `docs`
  dependency group.
- Source code documentation lives in a subfolder of `docs/source` that shares
  the project's name and mirrors the structure of the code.
- Use `sphinx.ext.autodoc` to incorporate docstrings.

## Dependencies

Add a `docs` dependency group to `pyproject.toml` that contains at least
`sphinx` and `myst-parser`. For example, with uv:

```bash
uv add --group docs sphinx myst-parser
```

## Configuration

In `docs/source/conf.py`, enable at least:

```python
extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
]
```

Follow the project's string quoting conventions in `conf.py`.

## Layout

For a package `pkg` with modules `pkg/cli.py` and `pkg/util/io.py`:

```text
docs/source/
├── conf.py
├── index.md          root toctree, links pkg/index
└── pkg/
    ├── index.md      package `pkg`
    ├── cli.md        module `pkg.cli`
    └── util/
        ├── index.md  package `pkg.util`
        └── io.md     module `pkg.util.io`
```

- A package maps to a folder with an `index.md`.
- A module maps to a page named after the module.
- Each `index.md` lists its children in a `toctree`.

## Page template

Pull the API reference from docstrings with `automodule`, wrapped in an
`eval-rst` block because autodoc directives are reStructuredText:

````markdown
(pkg-cli)=
# Module `pkg.cli`

```{eval-rst}
.. automodule:: pkg.cli
   :members:
```

Prose that explains usage and design goes after the reference.
````

## Verify

Build the documentation and fix every warning introduced by the change:

```bash
uv run --group docs sphinx-build -b html docs/source docs/_build/html
```
