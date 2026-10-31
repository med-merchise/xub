(cli-reference)=
# Command-line interface

The `xub.cli` module is the foundation of the `xub` command-line interface
(CLI). It is built on [Typer](https://typer.tiangolo.com/), which bundles its
own copy of [Click](https://click.palletsprojects.com/) and renders output
with [Rich](https://rich.readthedocs.io/).

## Usage

```console
$ xub [OPTIONS] COMMAND [ARGS]...
```

The CLI can also be run as a Python module:

```console
$ python -m xub [OPTIONS] COMMAND [ARGS]...
```

Running `xub` with no arguments prints the help text.

## Command registry

Typer already provides a standard registry, so `xub` does not add a separate
one. Every `typer.Typer` instance records what is attached to it:

| Attribute             | Contents                                         |
|-----------------------|--------------------------------------------------|
| `registered_commands` | Commands added with `@app.command()`.            |
| `registered_groups`   | Sub-applications added with `app.add_typer()`.   |
| `registered_callback` | The root callback, which declares global options. |

The root application is `xub.cli.app`. Typer builds the Click command tree,
including all help output, from these attributes when the application runs.

`xub.cli` defines a root callback on purpose. Without one, an application
with exactly one command collapses into that single command. With the
callback, `xub` is always a group of commands, and the callback is where
global options such as `--version` are declared.

### Register a command

Use `xub.cli.command()`, a thin wrapper over `app.command()`:

```python
import typer

from xub.cli import command


@command()
def hello(name: str = "world") -> None:
    """Say hello."""
    typer.echo(f"hello {name}")
```

The first line of the docstring becomes the short help shown in the command
list. The full docstring is shown by `xub hello --help`.

### Register a group of commands

Use `xub.cli.add_group()`, a thin wrapper over `app.add_typer()`, to attach a
sub-application:

```python
import typer

from xub.cli import add_group

net = typer.Typer(help="Network commands.")


@net.command()
def ping() -> None:
    """Reply with pong."""
    typer.echo("pong")


add_group(net, "net")
```

The group is invoked as `xub net ping`. Unless the call passes its own
`context_settings`, the group inherits the `-h`/`--help` option names of the
root application.

A module that registers commands must be imported before `xub.cli.main()`
runs; otherwise its commands are not part of the registry.

## Global options

These options belong to the root application, so they go before any command
name.

| Option                 | Origin | Description                                  |
|------------------------|--------|----------------------------------------------|
| `-h`, `--help`         | Typer  | Show the help text and exit.                 |
| `--install-completion` | Typer  | Install completion for the current shell.    |
| `--show-completion`    | Typer  | Print the completion script for the current shell. |
| `-V`, `--version`      | `xub`  | Show the program version and exit.           |

### `-h`, `--help`

Typer adds `--help` to the application, to every group, and to every command.
The help text comes from the registry: the usage line, the description,
every option with its type, default value, and environment variable, and
every registered command and group with its short help.

`xub` adds `-h` as an alias by setting the Click context setting
`help_option_names` to `["-h", "--help"]`. Context settings are passed down
to subcommands, so the alias works at every level:

```console
$ xub -h
$ xub net -h
$ xub net ping -h
```

### `--install-completion`

Detects the current shell and installs a completion script for `xub`. Open
a new shell for the change to take effect. Where the script is installed
depends on the shell:

| Shell                   | What Typer changes                                       |
|-------------------------|----------------------------------------------------------|
| Bash                    | Writes `~/.bash_completions/xub.sh` and sources it from `~/.bashrc`. |
| Zsh                     | Writes `~/.zfunc/_xub` and updates `~/.zshrc`.           |
| Fish                    | Writes `~/.config/fish/completions/xub.fish`.            |
| PowerShell (`pwsh`)     | Appends the script to the PowerShell profile.            |

### `--show-completion`

Prints the completion script for the current shell instead of installing it.
Use it to review the script or to install it by hand:

```console
$ xub --show-completion > ~/.config/fish/completions/xub.fish
```

Typer adds both completion options because `add_completion` is `True` by
default. Only the root application has them; commands and groups do not.

### `-V`, `--version`

Prints the program name and installed version, then exits. The option is
eager: it runs before any other option or command is processed.

```console
$ xub --version
xub 0.1.0
```

## Other built-in behavior

Typer also provides the following without extra code.

Suggestions for mistyped commands
: When a command name is not recognized, Typer suggests the closest
  registered name (controlled by `suggest_commands`, on by default).

Rich help output
: Help text is rendered as panels by Rich. `xub` sets `rich_markup_mode` to
  `"rich"`, so docstrings and help strings can use Rich markup such as
  `[bold]` or `[green]`.

Pretty exceptions
: Uncaught exceptions are shown as a short, formatted Rich traceback that
  hides Typer and Click internals. Local variables are not shown.

## Environment variables

Typer and Rich read these variables. None of them are specific to `xub`.

| Variable                   | Effect                                              |
|----------------------------|-----------------------------------------------------|
| `TYPER_STANDARD_TRACEBACK` | If set, show the standard Python traceback instead of the Rich one. |
| `TYPER_USE_RICH`           | Set to a false value to turn off Rich formatting.   |
| `TERMINAL_WIDTH`           | Maximum width of the help output, in columns.       |
| `FORCE_COLOR`, `PY_COLORS` | If set, force colored output, even when not writing to a terminal. |
| `NO_COLOR`                 | If set, turn off colors (handled by Rich).          |

Shell completion uses the variable `_XUB_COMPLETE` internally. The scripts
installed by `--install-completion` set it; do not set it by hand.

## Generate CLI documentation

The `typer` command, installed with Typer, can generate a Markdown reference
of every registered command and option:

```console
$ uv run typer xub.cli utils docs --name xub --output cli-commands.md
```

## Official documentation

- [Typer documentation](https://typer.tiangolo.com/)
- [Typer: commands and help](https://typer.tiangolo.com/tutorial/commands/help/)
- [Typer: subcommands](https://typer.tiangolo.com/tutorial/subcommands/)
- [Typer: shell completion](https://typer.tiangolo.com/tutorial/options-autocompletion/)
- [Click: context settings](https://click.palletsprojects.com/en/stable/api/#click.Context)
