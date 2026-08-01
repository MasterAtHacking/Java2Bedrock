import os
import json


class JavaEntityGenerator:
    """
    Generates Java entity files from translated entity data.
    """


    def __init__(
        self,
        entities,
        output_path
    ):

        self.entities = entities
        self.output_path = output_path
        self.generated = 0



    def generate(self):

        entities_path = os.path.join(
            self.output_path,
            "entities"
        )

        os.makedirs(
            entities_path,
            exist_ok=True
        )


        for identifier, data in self.entities.items():

            java_id = data["java_id"]


            file_path = os.path.join(
                entities_path,
                java_id + ".json"
            )


            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )


            self.generated += 1



    def count(self):

        return self.generated
