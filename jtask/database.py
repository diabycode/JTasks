import json
from pathlib import Path
from typing import NamedTuple, List, Dict, Any

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_tasks.json"
)


def get_db_path(config_path: Path) -> Path:
    with open(config_path, "r") as config_file:
        configs = json.load(config_file)
    return Path(configs.get("database"))


def init_database(db_path: Path):
    db_path.write_text("[]")


class DBResponse(NamedTuple):
    task_list: List[Dict[str, Any]]


class DatabaseHandler:

    def __init__(self, db_path):
        self._db_path = db_path

    def read_tasks(self) -> DBResponse:
        """ Read all tasks to database """

        with open(self._db_path, "r") as db_file:
            return DBResponse(list(json.load(db_file)))

    def write_tasks(self, tasks_list: List[Dict[str, Any]]) -> DBResponse:
        """ Write all tasks to database """

        with open(self._db_path, "w") as db_file:
            json.dump(tasks_list, db_file, indent=4)
            return DBResponse(list(tasks_list))


if __name__ == "__main__":
    config_file_path = Path("C:/Users/diaby/AppData/Roaming/jtask/config.json")
    db = get_db_path(config_file_path)

    init_database(db)
    print(f"database initialized to: {db}")


