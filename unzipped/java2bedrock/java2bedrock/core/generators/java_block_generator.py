import os
import json


class JavaBlockGenerator:
    """
    Generates Java block files from translated block data.
    """


    def __init__(
        self,
        blocks,
        output_path
    ):

        self.blocks = blocks
        self.output_path = output_path
        self.generated = 0



    def generate(self):

        blocks_path = os.path.join(
            self.output_path,
            "blocks"
        )

        os.makedirs(
            blocks_path,
            exist_ok=True
        )


        for identifier, data in self.blocks.items():

            java_id = data["java_id"]


            file_path = os.path.join(
                blocks_path,
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
