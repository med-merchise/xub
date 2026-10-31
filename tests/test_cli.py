"""Tests for the `xub.cli` module."""

import pytest
import typer
from typer.testing import CliRunner

from xub import cli

runner = CliRunner()


@pytest.mark.parametrize("flag", cli.HELP_OPTION_NAMES)
def test_help_option(flag):
    result = runner.invoke(cli.app, [flag], prog_name=cli.PROG_NAME)
    assert result.exit_code == 0
    assert "Usage: xub" in result.output
    assert "--install-completion" in result.output


def test_no_args_shows_help():
    result = runner.invoke(cli.app, [], prog_name=cli.PROG_NAME)
    assert "Usage: xub" in result.output


@pytest.mark.parametrize("flag", ["--version", "-V"])
def test_version_option(flag):
    result = runner.invoke(cli.app, [flag], prog_name=cli.PROG_NAME)
    assert result.exit_code == 0
    assert result.output.startswith("xub ")


def test_registry(monkeypatch):
    monkeypatch.setattr(cli.app, "registered_commands", [])
    monkeypatch.setattr(cli.app, "registered_groups", [])

    @cli.command()
    def hello(name: str = "world"):
        """Say hello."""
        typer.echo(f"hello {name}")

    group = typer.Typer(help="Grouped commands.")

    @group.command()
    def ping():
        """Reply with pong."""
        typer.echo("pong")

    cli.add_group(group, "net")

    assert [c.callback for c in cli.app.registered_commands] == [hello]
    assert [g.name for g in cli.app.registered_groups] == ["net"]

    result = runner.invoke(cli.app, ["-h"])
    assert "hello" in result.output and "net" in result.output

    result = runner.invoke(cli.app, ["hello", "--name", "xub"])
    assert result.output == "hello xub\n"

    result = runner.invoke(cli.app, ["net", "ping"])
    assert result.output == "pong\n"

    result = runner.invoke(cli.app, ["net", "-h"])
    assert result.exit_code == 0 and "ping" in result.output
