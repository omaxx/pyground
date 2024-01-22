import os

import click
import dotenv
from rich.console import Console

from . import hello

dotenv.load_dotenv()
console = Console()


@click.command()
# fmt: off
@click.option(
    "--greet", "-g",
    default=os.getenv("PG_GREET", "Hello"), show_default=True, required=True,
)
@click.option(
    "--name", "-n",
    default=os.getenv("USER"), show_default=True, required=True,
)
# fmt: on
def cli(greet: str, name: str) -> None:
    console.print(hello(greet, name))


if __name__ == "__main__":
    cli()
