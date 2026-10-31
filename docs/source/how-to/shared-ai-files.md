# Unify AI configuration into a single source

## Global Configuration

To share configurations seamlessly across Claude Code, Codex, Antigravity, and
Gemini, you can implement a unified multi-agent instruction matrix using a
single central directory and symbolic links.

- <https://www.reddit.com/r/ClaudeCode/comments/1pjysfa/managing_context_hell_with_a_multiagent_stack/>
- <https://www.mindstudio.ai/blog/omarchy-shared-skills-folder-across-agents>

Because AGENTS.md has emerged as the native standard for Codex and is the
universal fallback for the others, it serves as your perfect source of
truth.

- <https://antigravity.google/docs/rules/>
- <https://learn.chatgpt.com/docs/agent-configuration/agents-md>

### Step 1: Initialize Your Central Configuration Hub

Instead of spreading files across your file system, create a central directory
in your home folder. This allows you to manage all global agent instructions
from one place and commit them to Git.

```bash
mkdir -p ~/.config/agent-hub/global
touch ~/.config/agent-hub/global/AGENTS.md
```

Populate your central AGENTS.md file with common parameters (machine
constraints, coding preferences, terse language requests, safety boundaries).

- <https://www.mindstudio.ai/blog/omarchy-shared-skills-folder-across-agents>

### Step 2: Global Configuration Matrix (User Level)

Run the following script block to map your single AGENTS.md to the expected
directories for all four tools simultaneously:

- <https://www.reddit.com/r/ClaudeCode/comments/1pjysfa/managing_context_hell_with_a_multiagent_stack/>
- <https://www.mindstudio.ai/blog/omarchy-shared-skills-folder-across-agents>

```bash
# 1. Create target directories if they don't exist
mkdir -p ~/.claude
mkdir -p ~/.codex
mkdir -p ~/.gemini

# 2. Claude Code Symlink
ln -sf ~/.config/agent-hub/global/AGENTS.md ~/.claude/CLAUDE.md

# 3. Codex Symlink
ln -sf ~/.config/agent-hub/global/AGENTS.md ~/.codex/AGENTS.md

# 4. Gemini CLI & Google Antigravity Symlink
ln -sf ~/.config/agent-hub/global/AGENTS.md ~/.gemini/GEMINI.md
```

### File Path & Format Matching Summary

| AI Harness  |	Native Location | Target Symlink | Support Notes                                |
| ----------- | --------------- | -------------- | -------------------------------------------- |
| Claude Code |	`~/.claude/`    | `CLAUDE.md`    | Reads fallback if CLAUDE.md is empty/linked. |
| Codex       |	`~/.codex/`     | `AGENTS.md`    | Natively parses AGENTS.md on every turn.     |
| Gemini CLI  |	`~/.gemini/`    | `GEMINI.md`    | Plain Markdown parsing from user home.       |
| Antigravity |	`~/.gemini/`    | `GEMINI.md`    | Merges workspace files and global markdown.  |


### Step 3: Project-Level Configuration (Workspace Matrix)

If you want a shared file inside your git projects that all four tools respect
when you open their respective CLIs in that workspace, place an AGENTS.md file
at the root of your repository.
- <https://learn.chatgpt.com/docs/agent-configuration/agents-md>
- <https://antigravity.google/docs/rules/>

To prevent Claude Code from ignoring it (since it expects CLAUDE.md), add a
thin proxy CLAUDE.md file next to it:

**.root/CLAUDE.md**

```markdown
@AGENTS.md
```

- Codex and Antigravity will read AGENTS.md natively in the directory tree.
- Claude Code will read CLAUDE.md and use the @ import token to seamlessly
  inherit the parameters.
  - <https://antigravity.google/docs/rules/>
  - <https://learn.chatgpt.com/docs/agent-configuration/agents-md>

### 💡 Multi-Agent Skill Sharing (Bonus Setup)

If you want to share functional skills, slash commands, or tools across your
agents (for example, custom automation routines), they also look in distinct
directories. You can unify them under your central agent hub as well:

- <https://antigravity.google/docs/skills/>
- <https://www.mindstudio.ai/blog/omarchy-shared-skills-folder-across-agents>

```bash
mkdir -p ~/.config/agent-hub/skills
mkdir -p ~/.gemini/config

# Link the shared skills folder across your toolchains

ln -sf ~/.config/agent-hub/skills ~/.claude/skills
ln -sf ~/.config/agent-hub/skills ~/.codex/skills
ln -sf ~/.config/agent-hub/skills ~/.gemini/config/skills
```

Any procedural .md skill or custom command you drop into
`~/.config/agent-hub/skills/` will instantly update slash commands across all
your running AI terminals.

- <https://antigravity.google/docs/skills/>
- <https://www.mindstudio.ai/blog/omarchy-shared-skills-folder-across-agents>

## Project

To unify AI assistant configuration into a single source of truth while
ensuring Claude Code reads it flawlessly, you should treat `AGENTS.md` as your
primary universal instruction file and configure CLAUDE.md as a thin wrapper
that imports it.

- <https://pub.towardsai.net/your-ai-agent-rules-one-source-of-truth-for-cursor-claude-code-and-every-tool-youll-adopt-next-cd7f1353dbbc)>
- <https://dev.to/deployhq/claudemd-agentsmd-and-every-ai-config-file-explained-4pde>

While Claude Code reads `AGENTS.md` natively as a fallback, it will stop
reading it the moment a `CLAUDE.md` is detected in your directory tree. Using
an explicit import strategy gives you the best of both worlds: universal
cross-tool compatibility via `AGENTS.md` and deep optimization for Claude
Code.

- <https://www.buildthisnow.com/blog/guide/mechanics/agents-md-vs-claude-md)>
- <https://nimbalyst.com/blog/agents-md-vs-claude-md/>

### Strategy 1: The Import Syntax (Recommended)

This approach allows you to maintain all cross-tool settings (like styling,
testing commands, and architecture rules) in AGENTS.md for tools like Cursor,
Windsurf, or Codex CLI, while keeping a dedicated space for Claude-specific
modes.

- <https://dev.to/deployhq/claudemd-agentsmd-and-every-ai-config-file-explained-4pde>
- [] (https://www.buildthisnow.com/blog/guide/mechanics/agents-md-vs-claude-md)

#### 1. Create your universal AGENTS.md in the repository root:

```markdown
# Repository Agent Guidelines

Standard instructions for all coding agents.

## Build and Test Commands
- Build: `npm run build`
- Test: `npm test`

## Style Guide
- Use TypeScript with strict null checks.
- Keep components functional and under 150 lines.
```

#### 2. Create a thin CLAUDE.md wrapper referencing it:

```markdown
@AGENTS.md

# Claude-Specific Behaviors
- Use Plan Mode (`/plan`) before executing complex multi-file refactors.
```

## Strategy 2: The Symlink Method (Hard Link)

If you want absolutely zero duplication and do not have any Claude-specific
configurations to add, you can trick your operating system into pointing both
files to the exact same memory space.

- <https://www.linkedin.com/pulse/how-i-share-global-context-across-all-my-agent-harnesses-sean-wright-nxn8e)>
- <https://www.buildthisnow.com/blog/guide/mechanics/agents-md-vs-claude-md>

```bash
ln -s AGENTS.md CLAUDE.md
```

### ⚠️ Critical Constraints to keep in mind

- Keep it under 300 lines: Context degradation occurs uniformly as
  configuration files bloat. Claude Code's system prompt already uses a
  sizeable allocation; keeping your files concise avoids wasting expensive
  context tokens on every turn.

  - <https://www.youtube.com/watch?v=S_oN3vlzpMw&t=111>
  - [] (https://www.humanlayer.dev/blog/writing-a-good-claude-md)
  - [] (https://dev.to/deployhq/claudemd-agentsmd-and-every-ai-config-file-explained-4pde)

- Write rules deterministically: Focus rules on product constraints, commands,
  and hard technical limits. Avoid using these files to ask the AI to acts as
  a linting tool—leave that to your native project linters.

  - <https://www.youtube.com/watch?v=6VC-TuWVlCc>
  - <https://www.humanlayer.dev/blog/writing-a-good-claude-md>

- Leverage local uncommitted files: If you have specific machine-level
settings or personal notes you don't want to sync to Git, use a file. Claude
will concatenate this automatically with your project-level settings.

  - <https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9>
  - <https://www.buildthisnow.com/blog/guide/mechanics/agents-md-vs-claude-md>
  - <https://nimbalyst.com/blog/agents-md-vs-claude-md/>
