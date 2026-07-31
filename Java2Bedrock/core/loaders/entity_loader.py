import os
import json

from core.registries.entity_registry import register_entity


def find_entity_files(pack_path):
    """
    Find entity JSON files inside a behavior pack.
    """

    entities_path = os.path.join(
        pack_path,
        "entities"
    )


    if not os.path.exists(entities_path):
        return []


    files = []


    for root, dirs, filenames in os.walk(entities_path):

        for file in filenames:

            if file.endswith(".json"):

                files.append(
                    os.path.join(
                        root,
                        file
                    )
                )


    return files



def load_entity_file(file):
    """
    Load one entity JSON file.
    """

    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        entity = data.get(
            "minecraft:entity",
            {}
        )


        description = entity.get(
            "description",
            {}
        )


        identifier = description.get(
            "identifier"
        )


        if not identifier:
            return


        components = entity.get(
            "components",
            {}
        )


        metadata = {
            "components": components
        }


        register_entity(
            identifier,
            metadata
        )


        print(
            "Registered entity:",
            identifier
        )


    except Exception as e:

        print(
            "Failed loading entity:",
            file,
            e
        )



def load_entities_from_pack(pack_path):
    """
    Load all entities from one behavior pack.
    """

    files = find_entity_files(
        pack_path
    )


    for file in files:

        load_entity_file(
            file
        )
