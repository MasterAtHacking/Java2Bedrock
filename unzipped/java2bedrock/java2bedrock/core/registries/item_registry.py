# Stores every valid item and its metadata.


ITEMS = {}


def register_item(identifier, data=None):
    """
    Register one item.
    """

    if not isinstance(identifier, str):
        raise TypeError(
            "Item identifier must be a string."
        )


    if ":" not in identifier:
        raise ValueError(
            "Item identifier must be namespaced."
        )


    if data is None:
        data = {}


    data["id"] = identifier


    ITEMS[identifier] = data



def unregister_item(identifier):
    """
    Remove one item.
    """

    ITEMS.pop(
        identifier,
        None
    )



def is_valid_item(identifier):
    """
    Check if an item exists.
    """

    return identifier in ITEMS



def get_item(identifier):
    """
    Get item information.
    """

    return ITEMS.get(
        identifier
    )



def clear_items():
    """
    Remove all items.
    """

    ITEMS.clear()



def get_all_items():
    """
    Return every registered item.
    """

    return sorted(
        ITEMS.keys()
    )



def item_count():
    """
    Return number of registered items.
    """

    return len(ITEMS)



def print_items():
    """
    Debug: print all items.
    """

    print("========== ITEM REGISTRY ==========")

    for identifier, data in ITEMS.items():

        print()
        print("Item:", identifier)

        for key, value in data.items():

            print(
                " ",
                key,
                ":",
                value
            )


    print()
    print("========== END ITEM REGISTRY ==========")
