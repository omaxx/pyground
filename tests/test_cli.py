from click.testing import CliRunner
from app.__main__ import cli


def test_cli() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Jon Snow"])
    assert result.exit_code == 0
    assert result.output == "Hello Jon Snow!\n"
