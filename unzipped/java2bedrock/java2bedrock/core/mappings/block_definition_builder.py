class BlockDefinitionBuilder:
    """
    Combines block data, states, and resources.
    """


    def __init__(
        self,
        blocks,
        states,
        resources
    ):

        self.blocks = blocks
        self.states = states
        self.resources = resources

        self.definitions = {}



    def generate(self):

        for identifier, data in self.blocks.items():

            definition = {
                "id": identifier,
                "metadata": data,
                "states": {},
                "resources": []
            }


            if identifier in self.states:

                definition["states"] = self.states[
                    identifier
                ]


            if identifier in self.resources:

                definition["resources"] = self.resources[
                    identifier
                ]


            self.definitions[identifier] = definition


        return self.definitions



    def count(self):

        return len(
            self.definitions
        )
