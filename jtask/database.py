import json
from pathlib import Path

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_tasks.json"
)


def get_db_path(config_path: Path) -> Path:
    with open(config_path, "r") as config_file:
        configs = json.load(config_file)
    return Path(configs.get("database"))


def init_database(db_path: Path):
    db_path.write_text("[]")


if __name__ == "__main__":
    config_file_path = Path("C:/Users/diaby/AppData/Roaming/jtask/config.json")
    db = get_db_path(config_file_path)

    init_database(db)
    print(f"database initialized to: {db}")


