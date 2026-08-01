import os

from core.loaders.entity_loader import load_entities_from_pack
from core.loaders.manifest_loader import scan_pack_manifests
from core.loaders.block_pack_loader import load_blocks_from_pack
from core.loaders.block_pack_loader import load_blocks_from_pack
from core.loaders.item_loader import load_items_from_pack

def find_behavior_packs(world_path):
    """
    Find all behavior packs in the world.
    """

    path = os.path.join(
        world_path,
        "behavior_packs"
    )


    if not os.path.exists(path):
        return []


    packs = []


    for name in os.listdir(path):

        full_path = os.path.join(
            path,
            name
        )


        if os.path.isdir(full_path):
            packs.append(full_path)


    return packs



def load_addons(world_path):

    print("Scanning addons...")


    packs = find_behavior_packs(
        world_path
    )


    if not packs:
        print("Found 0 behavior packs")
        return []


    for pack in packs:
        print(
            "Found addon folder:",
            pack
        )

        load_blocks_from_pack(
            pack
        )
    

        load_items_from_pack(
        pack
        )


        load_entities_from_pack(
            pack
        )

    manifests = scan_pack_manifests(
        packs
    )


    print(
        "Found",
        len(manifests),
        "behavior packs"
    )


    return manifests
