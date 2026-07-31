class ResourceMapper:
    """
    Links blocks/items to resource files.
    """


    def __init__(
        self,
        blocks,
        resources
    ):

        self.blocks = blocks
        self.resources = resources
        self.mappings = {}


    def generate(self):

        for identifier in self.blocks:

            name = identifier.split(":")[1]

            matches = []

            for resource in self.resources:

                if name in resource:

                    matches.append(
                        resource
                    )


            self.mappings[identifier] = matches


        return self.mappings



    def count(self):

        return len(
            self.mappings
        )
