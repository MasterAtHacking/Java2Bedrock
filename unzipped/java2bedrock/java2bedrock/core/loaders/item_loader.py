import os
import json

from core.registries.item_registry import register_item


def find_item_files(pack_path):
    """
    Find item JSON files inside a behavior pack.
    """

    items_path = os.path.join(
        pack_path,
        "items"
    )


    if not os.path.exists(items_path):
        return []


    files = []


    for root, dirs, filenames in os.walk(items_path):

        for file in filenames:

            if file.endswith(".json"):

                files.append(
                    os.path.join(
                        root,
                        file
                    )
                )


    return files



def load_item_file(file):
    """
    Load one item JSON file.
    """

    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        item = data.get(
            "minecraft:item",
            {}
        )


        description = item.get(
            "description",
            {}
        )


        identifier = description.get(
            "identifier"
        )


        if not identifier:
            return


        components = item.get(
            "components",
            {}
        )


        metadata = {
            "components": components
        }


        register_item(
            identifier,
            metadata
        )


        print(
            "Registered item:",
            identifier
        )


    except Exception as e:

        print(
            "Failed loading item:",
            file,
            e
        )



def load_items_from_pack(pack_path):
    """
    Load all items from one behavior pack.
    """

    files = find_item_files(
        pack_path
    )


    for file in files:

        load_item_file(
            file
        )
