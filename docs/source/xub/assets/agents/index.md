(xub-assets-agents)=
# Assets `xub.assets.agents`

The `src/xub/assets/agents/` folder is the single source of truth for the
configuration of the AI coding agents used on the workstation: Claude Code,
Codex, Gemini CLI, and Antigravity. Each agent expects its global files in a
different location, so the same files are linked into every one of them. The
procedure is described in {doc}`/how-to/shared-ai-files`.

## Components

| Component   | Description                                       |
| ----------- | ------------------------------------------------- |
| `AGENTS.md` | Global instructions, {ref}`xub-assets-agents-md`. |
| `skills/`   | Shared skills, {ref}`xub-assets-skills`.          |

## Content

```{toctree}
:maxdepth: 1

instructions/index
skills/index
```
