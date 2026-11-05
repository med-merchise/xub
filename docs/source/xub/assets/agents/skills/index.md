(xub-assets-skills)=
# Shared skills `skills/`

The `src/xub/assets/agents/skills/` folder holds the skills shared by all the
AI coding agents. A skill is a packaged set of instructions that an agent
loads on demand, instead of on every turn as it does with
{ref}`xub-assets-agents-md`. Moving specialized rules out of `AGENTS.md` and
into skills keeps the global instructions short.

Skills are named with the `xub-` prefix, and the folder is linked into the
skills location of each agent, as described in {doc}`/how-to/shared-ai-files`.

```{note}
The folder is currently empty.
```
