class ItemTranslator:
    """
    Converts Bedrock item definitions into Java-compatible data.
    """


    def __init__(
        self,
        items
    ):

        self.items = items
        self.output = {}



    def translate(self):

        for identifier, data in self.items.items():

            java_id = identifier.replace(
                ":",
                "_"
            )


            self.output[identifier] = {

                "bedrock_id": identifier,

                "java_id": java_id,

                "metadata": data.get(
                    "metadata",
                    {}
                ),

                "resources": data.get(
                    "resources",
                    []
                )

            }


        return self.output



    def count(self):

        return len(
            self.output
        )
