import os
import json

from core.registries.block_registry import register_block
from core.registries.block_registry import block_count


def load_vanilla_blocks():
    """Load vanilla Minecraft blocks."""

    vanilla = [
        "minecraft:air",
        "minecraft:stone",
        "minecraft:grass_block",
        "minecraft:dirt",
        "minecraft:cobblestone",
        "minecraft:oak_log",
        "minecraft:oak_planks"
    ]

    for block in vanilla:
        register_block(block)

    print(f"Loaded {block_count()} vanilla blocks.")


def scan_block_file(file):

    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

    except:
        return


    if "minecraft:block" in data:
        identifier = data.get("format_version")

    blocks = data.get("minecraft:block")

    if blocks:

        description = blocks.get("description", {})

        identifier = description.get("identifier")

        if identifier:
            register_block(identifier)
            print("Loaded addon block:", identifier)



def load_addon_blocks(world_path):

    behavior_path = os.path.join(
        world_path,
        "behavior_packs"
    )

    if not os.path.exists(behavior_path):
        print("No behavior packs found")
        return


    for root, dirs, files in os.walk(behavior_path):

        for file in files:

            if file.endswith(".json"):

                scan_block_file(
                    os.path.join(root, file)
                )



def load_blocks(world_path=None):

    load_vanilla_blocks()

    if world_path:
        load_addon_blocks(world_path)

