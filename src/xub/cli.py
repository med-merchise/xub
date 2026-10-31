"""Command-line interface (CLI) foundation for `xub`.

The registry of commands and options is the root :class:`typer.Typer`
instance, `app`.  Typer already keeps a registry of everything attached to
an application:

- `app.registered_commands` -- commands added with `@app.command()`;
- `app.registered_groups` -- sub-applications added with `app.add_typer()`;
- `app.registered_callback` -- the root callback, which declares the global
  options shared by all commands.

Other modules register their commands through `command()` and their
sub-applications through `add_group()`, both thin wrappers over the native
Typer API.  The help option (`-h`/`--help`) is generated automatically from
that registry for the application and for every command.

"""

from __future__ import annotations

import typing as t
from importlib.metadata import PackageNotFoundError, version

import typer

if t.TYPE_CHECKING:
    from collections.abc import Callable

__all__ = ["add_group", "app", "command", "main"]

PROG_NAME = "xub"

#: Names that trigger the help output, both for the application and for
#: every registered command and group.
HELP_OPTION_NAMES = ["-h", "--help"]

CONTEXT_SETTINGS = {"help_option_names": HELP_OPTION_NAMES}

app = typer.Typer(
    name=PROG_NAME,
    help="Set up and manage a Linux-based workstation.",
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


def _get_version() -> str:
    """Return the installed version of the package."""
    try:
        return version(PROG_NAME)
    except PackageNotFoundError:  # pragma: no cover
        return "unknown"


def _version_callback(value: bool) -> None:
    """Print the program version and exit when `--version` is given."""
    if value:
        typer.echo(f"{PROG_NAME} {_get_version()}")
        raise typer.Exit()


@app.callback()
def _root(
    version: t.Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Show the program version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """Set up and manage a Linux-based workstation."""


def command(
    name: str | None = None, **kwargs: t.Any
) -> Callable[[Callable[..., t.Any]], Callable[..., t.Any]]:
    """Register a function as a top-level command of the application.

    Equivalent to `app.command(name, **kwargs)`; see :meth:`typer.Typer.command`
    for the accepted keyword arguments.

    """
    return app.command(name, **kwargs)


def add_group(group: typer.Typer, name: str, **kwargs: t.Any) -> None:
    """Register a Typer sub-application as a group of commands.

    The group inherits the application's help option names unless it defines
    its own `context_settings`.  See :meth:`typer.Typer.add_typer` for the
    accepted keyword arguments.

    """
    kwargs.setdefault("context_settings", CONTEXT_SETTINGS)
    app.add_typer(group, name=name, **kwargs)


def main() -> None:
    """Run the command-line interface."""
    app(prog_name=PROG_NAME)
