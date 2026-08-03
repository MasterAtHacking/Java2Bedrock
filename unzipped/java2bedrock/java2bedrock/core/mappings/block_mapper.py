from core.mappings.java_block_registry import JAVA_BLOCKS


class BlockMapper:

    def __init__(self, bedrock_blocks):
        self.bedrock_blocks = bedrock_blocks
        self.mappings = {}


    def generate(self):

        for identifier, data in self.bedrock_blocks.items():

            if identifier in JAVA_BLOCKS:

                self.mappings[identifier] = {
                    "java": identifier,
                    "type": "direct",
                    "java_id": JAVA_BLOCKS[identifier]["id"]
                }

            else:

                self.mappings[identifier] = {
                    "java": "minecraft:barrier",
                    "type": "fallback",
                    "java_id": None
                }


        return self.mappings


    def count(self):

        return len(self.mappings)
