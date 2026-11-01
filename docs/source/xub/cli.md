(xub-cli)=
# Module `xub.cli`

```{eval-rst}
.. automodule:: xub.cli
```

For the options and behavior of the resulting `xub` command, see
{ref}`cli-reference`.

## Root callback

`xub.cli` defines a root callback on purpose. Without one, an application
with exactly one command collapses into that single command. With the
callback, `xub` is always a group of commands, and the callback is where
global options such as `--version` are declared.

Typer builds the Click command tree, including all help output, from the
registry of {data}`app` when the application runs.

## Register a command

Use {func}`command`, a thin wrapper over `app.command()`:

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

## Register a group of commands

Use {func}`add_group`, a thin wrapper over `app.add_typer()`, to attach a
sub-application:

```python
import typer

from xub.cli import add_group

net = typer.Typer(help="Network commands.")


@net.command()
def ping() -> None:
    """Reply with pong."""
    typer.echo("pong")


add_group(net, 'net')
```

The group is invoked as `xub net ping`. Unless the call passes its own
`context_settings`, the group inherits the `-h`/`--help` option names of the
root application.

A module that registers commands must be imported before {func}`main` runs;
otherwise its commands are not part of the registry.

## API

```{eval-rst}
.. autodata:: app
   :no-value:

.. autodata:: PROG_NAME

.. autodata:: HELP_OPTION_NAMES

.. autodata:: CONTEXT_SETTINGS

.. autofunction:: command

.. autofunction:: add_group

.. autofunction:: main
```
