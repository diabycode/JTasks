
import typer

from jtask import __version__, __app_name__

app = typer.Typer(name=__app_name__)


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

