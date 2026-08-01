class EntityResourceMapper:
    """
    Links entities to resource files.
    """


    def __init__(
        self,
        entities,
        resources
    ):

        self.entities = entities
        self.resources = resources
        self.mappings = {}



    def generate(self):

        for identifier in self.entities:

            name = identifier.split(":")[1]

            matches = []


            for resource in self.resources.keys():

                if "textures/entity/" in resource:

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
