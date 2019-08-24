import os
import subprocess
from typing import List

import click

from cli.decorators import load_env, setup_django


@click.group()
def cli():
    pass


@cli.command(help="test services", context_settings=dict(ignore_unknown_options=True))
@click.argument("test_args", nargs=-1, type=click.UNPROCESSED)
@load_env
def test(test_args: List[str]) -> None:
    """Run tests for service. Defaults to all."""

    os.environ["TESTING"] = "1"

    subprocess.run(["pytest", *test_args], cwd="backend")


@cli.command(add_help_option=False, context_settings=dict(ignore_unknown_options=True))
@click.argument("management_args", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
@setup_django
def django(ctx: click.core.Context, management_args: List[str]) -> None:
    """run django management commands"""
    from django.core.management import execute_from_command_line

    execute_from_command_line([ctx.command_path, *management_args])
