import os
import json


class JavaItemGenerator:
    """
    Generates Java item files from translated item data.
    """


    def __init__(
        self,
        items,
        output_path
    ):

        self.items = items
        self.output_path = output_path
        self.generated = 0



    def generate(self):

        items_path = os.path.join(
            self.output_path,
            "items"
        )

        os.makedirs(
            items_path,
            exist_ok=True
        )


        for identifier, data in self.items.items():

            java_id = data["java_id"]


            file_path = os.path.join(
                items_path,
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

