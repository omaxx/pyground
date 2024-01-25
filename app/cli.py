import logging
import os
from typing import Any

import click
import dotenv
from rich.console import Console
from rich.logging import RichHandler

from . import __version__, hello

dotenv.load_dotenv()

console = Console()


def print_version(ctx: click.Context, _: click.Option, value: Any) -> None:
    if not value or ctx.resilient_parsing:
        return
    # click.echo(__version__)
    console.print(__version__)
    ctx.exit()


@click.command(epilog=f"Version: {__version__}")
# fmt: off
@click.option(
    "--greet", "-g",
    default=os.getenv("PG_GREET", "Hello"), show_default=True, required=True,
)
@click.option(
    "--name", "-n",
    default=os.getenv("USER"), show_default=True, required=True,
)
@click.option("--verbose", "-v", count=True)
@click.option(
    "--version",
    is_flag=True, callback=print_version, expose_value=False, is_eager=True,
)
# fmt: on
def cli(greet: str, name: str, verbose: int) -> None:
    """
    Hello world script
    """
    if verbose == 0:
        level = logging.WARNING
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG
    logger = logging.getLogger(__name__.split(".")[0])
    logger.setLevel(level)
    logger.addHandler(RichHandler(level=level))

    console.print(hello(greet, name))
