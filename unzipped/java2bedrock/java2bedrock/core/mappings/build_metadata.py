from datetime import datetime


def build_metadata(
    server,
    block_count,
    block_state_count,
    item_count,
    entity_count,
    resource_count,
    behavior_pack_count,
    resource_pack_count
):
    """
    Build metadata describing the generated artifacts.
    """

    return {

        "generator": "Java2Bedrock",

        "generator_version": "0.1.0",

        "generated_at": datetime.utcnow().isoformat() + "Z",

        "world_name": server["level-name"],

        "world_path": server["world-path"],

        "blocks": block_count,

        "block_states": block_state_count,

        "items": item_count,

        "entities": entity_count,

        "resources": resource_count,

        "behavior_packs": behavior_pack_count,

        "resource_packs": resource_pack_count

    }

