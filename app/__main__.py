import os

import click
import dotenv
from rich.console import Console

from . import hello

dotenv.load_dotenv()
console = Console()


@click.command()
@click.option("--name", "-n", default=os.getenv("PG_NAME", "None"), show_default=True)
def cli(name: str) -> None:
    console.print(hello(name))


if __name__ == "__main__":
    cli()
