(xub-assets)=
# Package data `xub.assets`

The `src/xub/assets/` folder holds non-Python files distributed with the `xub`
package. It is not a Python package (it has no `__init__.py`), but the build
backend ships its content inside the wheel, so the files are available
wherever `xub` is installed.

Read an asset at run time with {mod}`importlib.resources`:

```python
from importlib.resources import files

text = files('xub').joinpath('assets/agents/AGENTS.md').read_text()
```

## Layout

```text
src/xub/assets/
└── agents/                 AI coding-agent configuration
    ├── .claude-plugin/     Claude Code plugin manifest
    ├── AGENTS.md           global instructions shared by all agents
    └── skills/             skills shared by all agents
```

## Content

```{toctree}
:maxdepth: 2

agents/index
```
