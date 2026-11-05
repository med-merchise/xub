(xub-assets-skills)=
# Shared skills `skills/`

The `src/xub/assets/agents/skills/` folder holds the skills shared by all the
AI coding agents. A skill is a packaged set of instructions that an agent
loads on demand, instead of on every turn as it does with
{ref}`xub-assets-agents-md`. Moving specialized rules out of `AGENTS.md` and
into skills keeps the global instructions short.

## Skills

| Skill                  | Purpose                                                |
| ---------------------- | ------------------------------------------------------ |
| `format-prose`         | Wrap Markdown and reStructuredText at the fill column. |
| `scaffold-python-docs` | Set up Sphinx, MyST, and autodoc for a Python package. |

## Format

Each skill is a folder with a `SKILL.md` file. The file starts with YAML
front matter that holds the `name` and `description` of the skill, followed
by its instructions in Markdown. Agents read the description to decide when
to load the skill. This format is understood by Claude Code, Codex, and
Gemini CLI.

## Claude Code plugin

The `agents` folder is also the root of a Claude Code plugin named `xub`,
declared in `.claude-plugin/plugin.json`. Claude Code finds the plugin skills
in `skills/` and prefixes them with the plugin name, so `format-prose` is
invoked as `/xub:format-prose`. Other agents use the bare skill name.

Check the plugin with:

```console
$ claude plugin validate src/xub/assets/agents
```

Load it for a single session with:

```console
$ claude --plugin-dir src/xub/assets/agents
```

## Other agents

Codex and Gemini CLI read skills from a folder in their home directory. Link
the shared `skills` folder there, as described in
{doc}`/how-to/shared-ai-files`.
