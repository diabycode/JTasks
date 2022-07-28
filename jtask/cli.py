from pathlib import Path

import typer

from jtask import __version__, __app_name__, database, config

app = typer.Typer(name=__app_name__)


@app.command()
def init(
        db_path: str = typer.Option(
            str(database.DEFAULT_DB_FILE_PATH),
            "--db-path",
            "-db",
            help="database location",
            prompt="Chemin de la base de donnée de tache ?"
        )
):
    """ initialize a new database to save tasks """

    config.init_app(db_path=db_path)
    database.init_database(db_path=Path(db_path))
    typer.secho(f"Votre base de donnée de tache est: {db_path}", fg=typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.secho(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: bool = typer.Option(
            None,
            "--version",
            "-v",
            help="show jtask app version and exit.",
            callback=_version_callback,
            is_eager=True
        )
) -> None:
    return

