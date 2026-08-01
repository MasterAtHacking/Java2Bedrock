# Stores every valid entity and its metadata.


ENTITIES = {}


def register_entity(identifier, data=None):
    """
    Register one entity.
    """

    if not isinstance(identifier, str):
        raise TypeError(
            "Entity identifier must be a string."
        )


    if ":" not in identifier:
        raise ValueError(
            "Entity identifier must be namespaced."
        )


    if data is None:
        data = {}


    data["id"] = identifier


    ENTITIES[identifier] = data



def unregister_entity(identifier):
    """
    Remove one entity.
    """

    ENTITIES.pop(
        identifier,
        None
    )



def is_valid_entity(identifier):
    """
    Check if an entity exists.
    """

    return identifier in ENTITIES



def get_entity(identifier):
    """
    Get entity information.
    """

    return ENTITIES.get(
        identifier
    )



def clear_entities():
    """
    Remove all entities.
    """

    ENTITIES.clear()



def get_all_entities():
    """
    Return every registered entity.
    """

    return sorted(
        ENTITIES.keys()
    )



def entity_count():
    """
    Return number of registered entities.
    """

    return len(ENTITIES)



def print_entities():
    """
    Debug: print all entities.
    """

    print("========== ENTITY REGISTRY ==========")

    for identifier, data in ENTITIES.items():

        print()
        print("Entity:", identifier)

        for key, value in data.items():

            print(
                " ",
                key,
                ":",
                value
            )


    print()
    print("========== END ENTITY REGISTRY ==========")
