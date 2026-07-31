from core.loaders.block_loader import load_blocks
from core.loaders.addon_loader import load_addons
from core.loaders.resource_loader import load_resources
from core.loaders.server_loader import load_server

from core.generators.asset_exporter import AssetExporter
from core.generators.java_project_generator import JavaProjectGenerator

from core.translators.block_translator import BlockTranslator
from core.translators.item_translator import ItemTranslator
from core.translators.entity_translator import EntityTranslator

from core.registries.block_registry import (
    BLOCKS,
    block_count,
    clear_blocks
)

from core.registries.block_state_registry import (
    get_all_block_states,
    clear_block_states
)

from core.registries.item_registry import (
    ITEMS,
    item_count,
    clear_items
)

from core.registries.entity_registry import (
    ENTITIES,
    entity_count,
    clear_entities
)

from core.registries.resource_registry import (
    RESOURCES,
    resource_count
)

from core.mappings.block_mapper import BlockMapper
from core.mappings.resource_mapper import ResourceMapper
from core.mappings.mapping_database import MappingDatabase
from core.mappings.build_metadata import build_metadata

from core.mappings.block_definition_builder import (
    BlockDefinitionBuilder
)

from core.mappings.item_definition_builder import (
    ItemDefinitionBuilder
)

from core.mappings.entity_definition_builder import (
    EntityDefinitionBuilder
)

from core.mappings.item_resource_mapper import (
    ItemResourceMapper
)

from core.mappings.entity_resource_mapper import (
    EntityResourceMapper
)



def load_everything(server_path):

    clear_blocks()
    clear_block_states()
    clear_items()
    clear_entities()


    print()
    print("Loading registries...")
    print()

    print("========== REGISTRY SUMMARY ==========")
    print()


    # SERVER

    server = load_server(
        server_path
    )


    if server is None:
        print("Server loading failed")
        return


    world_path = server["world-path"]


    # LOAD DATA

    load_blocks()

    addon_manifests = load_addons(
        world_path
    )

    resource_packs = load_resources(
        world_path
    )


    print()


    # BLOCKS

    print(
        "Total blocks loaded:",
        block_count()
    )


    block_mappings = BlockMapper(
        BLOCKS
    ).generate()


    resource_mappings = ResourceMapper(
        BLOCKS,
        RESOURCES
    ).generate()


    block_definitions = BlockDefinitionBuilder(
        BLOCKS,
        get_all_block_states(),
        resource_mappings
    ).generate()


    block_translations = BlockTranslator(
        block_definitions
    ).translate()


    print(
        "Block pipeline complete"
    )


    # ITEMS

    item_resource_mappings = ItemResourceMapper(
        ITEMS,
        RESOURCES
    ).generate()


    item_definitions = ItemDefinitionBuilder(
        ITEMS,
        item_resource_mappings
    ).generate()


    item_translations = ItemTranslator(
        item_definitions
    ).translate()


    print(
        "Item pipeline complete"
    )



    # ENTITIES

    entity_resource_mappings = EntityResourceMapper(
        ENTITIES,
        RESOURCES
    ).generate()


    entity_definitions = EntityDefinitionBuilder(
        ENTITIES,
        entity_resource_mappings
    ).generate()


    entity_translations = EntityTranslator(
        entity_definitions
    ).translate()


    print(
        "Entity pipeline complete"
    )



    # DATABASE

    database = MappingDatabase(
        "/root/java2bedrock"
    )


    database.prepare()



    outputs = [

        (
            "block_mappings.json",
            block_mappings,
            "mappings"
        ),

        (
            "resource_mappings.json",
            resource_mappings,
            "mappings"
        ),

        (
            "block_definitions.json",
            block_definitions,
            "definitions"
        ),

        (
            "item_definitions.json",
            item_definitions,
            "definitions"
        ),

        (
            "entity_definitions.json",
            entity_definitions,
            "definitions"
        ),

        (
            "block_registry.json",
            BLOCKS,
            "registries"
        ),

        (
            "block_state_registry.json",
            get_all_block_states(),
            "registries"
        ),

        (
            "item_registry.json",
            ITEMS,
            "registries"
        ),

        (
            "entity_registry.json",
            ENTITIES,
            "registries"
        ),

        (
            "resource_registry.json",
            RESOURCES,
            "registries"
        ),

        (
            "block_translations.json",
            block_translations,
            "java"
        ),

        (
            "item_translations.json",
            item_translations,
            "java"
        ),

        (
            "entity_translations.json",
            entity_translations,
            "java"
        )

    ]


    for filename, data, folder in outputs:

        database.save_json(
            filename,
            data,
            folder
        )

        print(
            "Generated artifact:",
            filename
        )



    metadata = build_metadata(
        server,
        block_count(),
        len(get_all_block_states()),
        item_count(),
        entity_count(),
        resource_count(),
        len(addon_manifests),
        len(resource_packs)
    )


    database.save_json(
        "metadata.json",
        metadata
    )


    print(
        "Generated artifact: metadata.json"
    )



    # JAVA PROJECT GENERATION
    # MUST BE LAST

    java_project_path = "/root/java2bedrock/generated/java_project"


    java_generator = JavaProjectGenerator(
        block_translations,
        item_translations,
        entity_translations,
        java_project_path
    )


    java_generator.generate()


    asset_exporter = AssetExporter(
        RESOURCES,
        java_project_path
    )


    asset_exporter.export()


    print(
        "Exported assets:",
        asset_exporter.count()
    )


    print()
    print("Finished loading registries")
    print()
    print("==========END OF SUMMARY==========")
    print()
