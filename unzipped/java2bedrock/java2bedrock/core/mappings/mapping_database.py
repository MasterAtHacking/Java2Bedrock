import json
import shutil
from pathlib import Path


class MappingDatabase:
    """
    Manages the generated database.
    """

    def __init__(self, project_root):

        self.project_root = Path(project_root)

        self.generated_directory = (
            self.project_root / "generated"
        )


    def prepare(self):
        """
        Create a fresh generated directory.
        """

        if self.generated_directory.exists():

            shutil.rmtree(
                self.generated_directory
            )

        self.generated_directory.mkdir(
            parents=True,
            exist_ok=True
        )


    def save_json(
        self,
        filename,
        data,
        folder=None
    ):
        """
        Save a JSON artifact.
        """

        if folder:

            directory = (
                self.generated_directory
                / folder
            )

            directory.mkdir(
                parents=True,
                exist_ok=True
            )

            path = (
                directory
                / filename
            )

        else:

            path = (
                self.generated_directory
                / filename
            )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                sort_keys=True
            )

        return path
