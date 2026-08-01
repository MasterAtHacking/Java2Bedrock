# Stores resource pack data.


RESOURCES = {}


def register_resource(identifier, data=None):
    """
    Register one resource.
    """

    if data is None:
        data = {}


    RESOURCES[identifier] = data



def get_resource(identifier):
    """
    Get resource information.
    """

    return RESOURCES.get(
        identifier
    )



def clear_resources():
    """
    Clear all resources.
    """

    RESOURCES.clear()



def get_all_resources():
    """
    Return all resources.
    """

    return RESOURCES



def resource_count():
    """
    Return resource count.
    """

    return len(RESOURCES)
