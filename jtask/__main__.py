from jtask import cli, __app_name__


def run_app():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    run_app()

