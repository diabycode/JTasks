

class JTask:

    def __init__(
            self,
            description: str,
            category: str,
            importance_level: int = 3,
            done: bool = False
    ):
        self.description = description
        self.category = category
        self.importance_level = importance_level
        self.done = done


if __name__ == "__main__":
    task = JTask(
        "Avancer sur le projet portfolio !",
        "boulot, progrommation",
    )

