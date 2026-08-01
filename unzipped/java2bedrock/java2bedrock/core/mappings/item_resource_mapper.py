class ItemResourceMapper:
    """
    Links items to resource files.
    """


    def __init__(
        self,
        items,
        resources
    ):

        self.items = items
        self.resources = resources
        self.mappings = {}



    def generate(self):

        for identifier in self.items:

            name = identifier.split(":")[1]

            matches = []


            for resource in self.resources:

                if "textures/items/" in resource:

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
