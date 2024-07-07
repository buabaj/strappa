import click
from strappa.main import setup_project, run_in_venv


@click.group()
def cli() -> None:
    """Strappa: A Python project bootstrapper."""
    pass


@cli.command()
def run() -> None:
    """Set up a Python project in the current directory."""
    click.echo("Running Strappa in the current directory")
    setup_project()


@cli.command()
@click.argument("command", nargs=-1)
def execute(command: str) -> None:
    """Execute a command in the project's virtual environment."""
    run_in_venv(" ".join(command))


if __name__ == "__main__":
    cli()
