import os

from core.loaders.resource_pack_loader import load_resources_from_pack

def find_resource_packs(world_path):

    path = os.path.join(
        world_path,
        "resource_packs"
    )

    if not os.path.exists(path):
        print("No resource packs found")
        return []


    packs = []

    for item in os.listdir(path):

        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            packs.append(full_path)


    return packs



def load_resources(world_path):

    print("Scanning resource packs...")


    packs = find_resource_packs(world_path)


    for pack in packs:
        print(
            "Found resource pack:", 
            pack
        )

        load_resources_from_pack(
            pack
        )


    print(
        "Found",
        len(packs),
        "resource packs"
    )
    return packs
