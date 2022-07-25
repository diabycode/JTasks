

class JTask:

    def __init__(self, description: str, category: str, done: bool = False):
        self.description = description
        self.done = done
        self.category = category


if __name__ == "__main__":
    task = JTask(
        "Avancer sur le projet portfolio !",
        "boulot, progrommation",
    )

