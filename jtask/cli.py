from pathlib import Path
from typing import List

import typer

from jtask import __version__, __app_name__, database, config
from jtask.jtask import TasksController, JTask

app = typer.Typer(name=__app_name__)


def get_tasks_conroller() -> TasksController:
    path = database.get_db_path(config.CONFIG_FILE_PATH)
    return TasksController(path)


@app.command()
def set_done(task_id: int = typer.Argument(..., help="Id of the task you want to set done")):

    """ Set a task to done status """

    tasks_controller = get_tasks_conroller()
    tasks = tasks_controller.get_all_tasks().task_list

    if not tasks_controller.set_done(task_id):
        typer.secho(f"Tache '{tasks[task_id-1]['description']}' déjà éffectué !", fg=typer.colors.BLUE)
        raise typer.Exit()

    typer.secho(
        f"Tache '{tasks[task_id-1]['description']}' effectué.",
        fg=typer.colors.GREEN
    )


@app.command(name="list")
def list_all():
    """ List all tasks """

    tasks_controller = get_tasks_conroller()
    db_response = tasks_controller.get_all_tasks()
    tasks_list = db_response.task_list
    if not tasks_list:
        typer.secho("Aucune tache trouvé.", fg=typer.colors.BLUE)
        raise typer.Exit()

    columns = [
        "ID.  ",
        "| Priorité  ",
        "| Catégorie  ",
        "| Effectué  ",
        "| Description  ",
    ]
    listing_header = "".join(columns)

    typer.secho(listing_header, bold=True)

    typer.secho("-" * len(listing_header), fg=typer.colors.BLUE)
    for id, task in enumerate(tasks_list, 1):
        desc, category, priority, done = task.values()
        if done:
            done = "Oui"
        else:
            done = "Non"

        if not category:
            category = "-"

        typer.secho(
            f"{id}{(len(columns[0]) - len(str(id))) * ' '}"
            f"| ({priority}){(len(columns[1]) - len(str(priority)) - 4) * ' '}"
            f"| {category}{(len(columns[2]) - len(str(category)) - 2) * ' '}"
            f"| {done}{(len(columns[3]) - len(str(done)) - 2) * ' '}"
            f"| {desc}",
            fg=typer.colors.BLUE,
        )
    typer.secho("-" * len(listing_header) + "\n", fg=typer.colors.BLUE)


@app.command()
def add(
        description: List[str] = typer.Argument(
            ...,
            help="Task description"
        ),
        category: str = typer.Option(
            "",
            "--category",
            "-c",
            help="The categorie of the task"
        ),
        priority: int = typer.Option(
            3,
            "--priority",
            "-p",
            help="Task priority [1 - 3]",
            min=1,
            max=3
        )
):
    """ Add a new task """

    description_text = " ".join(description)
    if not description_text.endswith("."):
        description_text += "."

    task = JTask(
        description=description_text,
        category=category,
        priority=priority,
        done=False
    )

    tasks_controller = get_tasks_conroller()
    tasks_controller.add(task.to_dict)
    typer.secho(
        f"La tache '{task.description}' a été ajouté"
        f" avec la priorité {task.priority}.",
        fg=typer.colors.GREEN
    )


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

