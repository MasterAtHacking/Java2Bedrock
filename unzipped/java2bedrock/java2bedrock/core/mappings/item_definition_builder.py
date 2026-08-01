class ItemDefinitionBuilder:
    """
    Combines item data and resources.
    """


    def __init__(
        self,
        items,
        resources
    ):

        self.items = items
        self.resources = resources
        self.definitions = {}



    def generate(self):

        for identifier, data in self.items.items():

            definition = {
                "id": identifier,
                "metadata": data,
                "resources": []
            }


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
