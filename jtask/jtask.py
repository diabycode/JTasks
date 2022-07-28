from pathlib import Path
from typing import Dict, Any

from .database import DatabaseHandler


class JTask:

    def __init__(
            self,
            description: str,
            category: str = "NULL",
            priority: int = 3,
            done: bool = False
    ):
        self.description = description
        self.category = category
        self.priority = priority
        self.done = done

    @property
    def to_dict(self):
        return self.__dict__


class TasksController:

    def __init__(self, db_path: Path):
        self._db_handler = DatabaseHandler(db_path)

    def add(self, task: Dict[str, Any]):
        read_reponse = self._db_handler.read_tasks()
        read_reponse.task_list.append(task)

        self._db_handler.write_tasks(read_reponse.task_list)

    def set_done(self, task_id: int):
        read_reponse = self._db_handler.read_tasks()

        tasks_list = read_reponse.task_list
        tasks_list[task_id - 1]["done"] = True

        self._db_handler.write_tasks(tasks_list)

    @property
    def all_tasks(self):
        return self._db_handler.read_tasks()


if __name__ == "__main__":
    t = JTask(
        "Avancer sur le projet portfolio !",
        "boulot, progrommation",
    )
