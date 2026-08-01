# Stores block states and permutations.


BLOCK_STATES = {}


def register_block_state(identifier, states=None):
    """
    Register states for a block.
    """

    if states is None:
        states = {}


    BLOCK_STATES[identifier] = states



def get_block_states(identifier):
    """
    Get states for a block.
    """

    return BLOCK_STATES.get(
        identifier,
        {}
    )



def has_block_states(identifier):
    """
    Check if block has states.
    """

    return identifier in BLOCK_STATES



def clear_block_states():
    """
    Clear all block states.
    """

    BLOCK_STATES.clear()



def block_state_count():
    """
    Return number of blocks with states.
    """

    return len(BLOCK_STATES)



def get_all_block_states():
    """
    Return all registered block states.
    """

    return BLOCK_STATES

