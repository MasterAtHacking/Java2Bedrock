JAVA_BLOCKS = {
    "minecraft:air": {
        "id": 0
    },

    "minecraft:stone": {
        "id": 1
    },

    "minecraft:grass_block": {
        "id": 2
    },

    "minecraft:dirt": {
        "id": 3
    },

    "minecraft:cobblestone": {
        "id": 4
    }
}


def get_java_block(identifier):
    return JAVA_BLOCKS.get(identifier)
