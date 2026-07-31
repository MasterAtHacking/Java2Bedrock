import os
import json

from core.registries.block_registry import register_block
from core.registries.block_state_registry import register_block_state
from core.loaders.block_state_loader import load_block_states

def find_block_files(pack_path):
    """
    Find all block JSON files inside a behavior pack recursively.
    """

    blocks_path = os.path.join(
        pack_path,
        "blocks"
    )


    if not os.path.exists(blocks_path):
        return []


    files = []


    for root, dirs, filenames in os.walk(blocks_path):

        for file in filenames:

            if file.endswith(".json"):

                files.append(
                    os.path.join(
                        root,
                        file
                    )
                )


    return files



def load_block_file(file):
    """
    Load one block JSON file and extract metadata.
    """

    try:

        with open(file, "r") as f:
            data = json.load(f)


        block = data.get(
            "minecraft:block",
            {}
        )


        description = block.get(
            "description",
            {}
        )


        identifier = description.get(
            "identifier"
        )


        if not identifier:
            return


        components = block.get(
            "components",
            {}
        )
        
        load_block_states(
            identifier,
            block
        )


        


        metadata = {
            "hardness": None,
            "friction": None,
            "explosion_resistance": None,
            "components": components
        }


        if "minecraft:destructible_by_mining" in components:

            mining = components["minecraft:destructible_by_mining"]

            metadata["hardness"] = mining.get(
                "seconds_to_destroy"
            )


        if "minecraft:friction" in components:

            metadata["friction"] = components[
                "minecraft:friction"
            ]


        if "minecraft:destructible_by_explosion" in components:

            explosion = components[
                "minecraft:destructible_by_explosion"
            ]

            metadata["explosion_resistance"] = explosion.get(
                "explosion_resistance"
            )

        register_block(
            identifier,
            metadata
        )


        print(
            "Registered block:",
            identifier
        )


    except Exception as e:

        print(
            "Failed loading block:",
            file,
            e
        )



def load_blocks_from_pack(pack_path):
    """
    Load all blocks from one behavior pack.
    """

    files = find_block_files(
        pack_path
    )


    for file in files:

        load_block_file(
            file
        )
