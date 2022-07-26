import json
from pathlib import Path

import typer

from __init__ import __app_name__
from database import DEFAULT_DB_FILE_PATH

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.json"


# init app
def init_app(db_path: str):
    _init_config_file()
    _init_db_path_to_config(db_path)


# create the config.json file -> init_config_file()
def _init_config_file():
    CONFIG_DIR_PATH.mkdir(exist_ok=True)
    CONFIG_FILE_PATH.touch(exist_ok=True)


# add db path to config
def _init_db_path_to_config(db_path: str):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(
            {
                "database": db_path
            },
            config_file,
            indent=4
        )


if __name__ == "__main__":
    init_app(str(DEFAULT_DB_FILE_PATH))
    # print(CONFIG_FILE_PATH)
