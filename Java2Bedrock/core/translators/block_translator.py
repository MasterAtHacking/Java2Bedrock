class BlockTranslator:
    """
    Converts Bedrock block definitions into Java-compatible data.
    """


    def __init__(
        self,
        blocks
    ):

        self.blocks = blocks
        self.output = {}



    def translate(self):

        for identifier, data in self.blocks.items():

            java_id = identifier.replace(
                ":",
                "_"
            )


            self.output[identifier] = {

                "bedrock_id": identifier,

                "java_id": java_id,

                "properties": data.get(
                    "states",
                    {}
                ),

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
