import re

from core.registries.block_state_registry import register_block_state


def detect_type(values):
    """
    Detect the type of a block property.
    """

    if all(isinstance(v, bool) for v in values):
        return "boolean"


    if all(isinstance(v, int) for v in values):
        return "integer"


    return "string"



def extract_properties(permutations):
    """
    Extract block properties and values.
    """

    properties = {}


    for permutation in permutations:

        condition = permutation.get(
            "condition",
            ""
        )


        matches = re.findall(
            r"block_property\('([^']+)'\)\s*==\s*(true|false|[0-9]+|'[^']+')",
            condition
        )


        for name, value in matches:

            if value == "true":
                value = True

            elif value == "false":
                value = False

            elif value.isdigit():
                value = int(value)

            elif value.startswith("'"):
                value = value.strip("'")


            if name not in properties:

                properties[name] = []


            if value not in properties[name]:

                properties[name].append(
                    value
                )


    formatted = {}


    for name, values in properties.items():

        formatted[name] = {
            "type": detect_type(values),
            "values": sorted(
                values,
                key=str
            )
        }


    return formatted



def load_block_states(identifier, block_data):
    """
    Load block states from a block definition.
    """

    permutations = block_data.get(
        "permutations",
        []
    )


    if not permutations:
        return


    states = {

        "properties": extract_properties(
            permutations
        ),

        "permutations": permutations

    }


    register_block_state(
        identifier,
        states
    )
