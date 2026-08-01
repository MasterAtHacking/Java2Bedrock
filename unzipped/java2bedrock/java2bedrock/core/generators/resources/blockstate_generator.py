import json
from pathlib import Path


class BlockstateGenerator:
    """
    Generates Minecraft Java blockstate files.
    """


    def __init__(
        self,
        blocks,
        output_path
    ):

        self.blocks = blocks
        self.output_path = Path(output_path)
        self.generated = 0



    def generate(self):

        blockstates_path = (
            self.output_path
            / "assets"
            / "generated"
            / "blockstates"
        )

        blockstates_path.mkdir(
            parents=True,
            exist_ok=True
        )


        for identifier, data in self.blocks.items():

            java_id = data["java_id"]


            blockstate = {
                "variants": {
                    "": {
                        "model": (
                            "generated:block/"
                            + java_id
                        )
                    }
                }
            }


            with open(
                blockstates_path / (java_id + ".json"),
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    blockstate,
                    file,
                    indent=4
                )


            self.generated += 1



    def count(self):

        return self.generated
