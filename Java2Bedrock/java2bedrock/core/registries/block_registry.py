# block_registry.py
# Stores every valid block and its metadata.


BLOCKS = {}


def register_block(identifier, data=None):
    """
    Register one block.
    """

    if not isinstance(identifier, str):
        raise TypeError(
            "Block identifier must be a string."
        )


    if ":" not in identifier:
        raise ValueError(
            "Block identifier must be namespaced."
        )


    if data is None:
        data = {}


    data["id"] = identifier


    BLOCKS[identifier] = data



def unregister_block(identifier):
    """
    Remove one block.
    """

    BLOCKS.pop(
        identifier,
        None
    )



def is_valid_block(identifier):
    """
    Check if a block exists.
    """

    return identifier in BLOCKS



def get_block(identifier):
    """
    Get block information.
    """

    return BLOCKS.get(
        identifier
    )



def clear_blocks():
    """
    Remove every registered block.
    """

    BLOCKS.clear()



def get_all_blocks():
    """
    Return every registered block.
    """

    return sorted(
        BLOCKS.keys()
    )



def block_count():
    """
    Return number of registered blocks.
    """

    return len(BLOCKS)




def print_blocks():
    """
    Debug: print all blocks and their data.
    """

    print("========== BLOCK REGISTRY ==========")

    for identifier, data in BLOCKS.items():

        print()
        print("Block:", identifier)

        for key, value in data.items():

            print(
                " ",
                key,
                ":",
                value
            )


    print()
    print("========== END BLOCK REGISTRY ==========")
