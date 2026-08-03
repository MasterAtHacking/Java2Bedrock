import os
from datetime import datetime


class Logger:

    def __init__(self):
        self.enabled = False
        self.file = None


    def enable(self):

        os.makedirs(
            "generated/logs",
            exist_ok=True
        )

        filename = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S.txt"
        )

        path = os.path.join(
            "generated/logs",
            filename
        )

        self.file = open(
            path,
            "w"
        )

        self.enabled = True

        self.log(
            "Logging started"
        )


    def setup(self):

        pass


    def log(self, message):

        if self.enabled and self.file:

            timestamp = datetime.now().strftime(
                "%H:%M:%S"
            )

            self.file.write(
                f"[{timestamp}] {message}\n"
            )

            self.file.flush()


    def close(self):

        if self.file:

            self.file.close()
