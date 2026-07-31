from pathlib import Path

from core.generators.java_code.block_code_generator import JavaBlockCodeGenerator

from core.generators.java_block_generator import JavaBlockGenerator
from core.generators.java_item_generator import JavaItemGenerator
from core.generators.java_entity_generator import JavaEntityGenerator



class JavaProjectGenerator:
    """
    Generates the Java project structure.
    """


    def __init__(
        self,
        block_translations,
        item_translations,
        entity_translations,
        output_path
    ):

        self.block_translations = block_translations
        self.item_translations = item_translations
        self.entity_translations = entity_translations

        self.output_path = Path(
            output_path
        )



    def prepare(self):

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )


        (self.output_path / "blocks").mkdir(
            exist_ok=True
        )


        (self.output_path / "items").mkdir(
            exist_ok=True
        )


        (self.output_path / "entities").mkdir(
            exist_ok=True
        )



    def generate(self):

        print()
        print("Generating Java project...")
        print()


        self.prepare()


        block_generator = JavaBlockGenerator(
            self.block_translations,
            str(self.output_path)
        )

        print("BLOCK OUTPUT PATH:", block_generator.output_path)
        print("BLOCK COUNT INPUT:", len(self.block_translations))

        block_generator.generate()


        print(
            "Generated Java blocks:",
            block_generator.count()
        )



        item_generator = JavaItemGenerator(
            self.item_translations,
            str(self.output_path)
        )


        print("ITEM COUNT INPUT:", len(self.item_translations))

        item_generator.generate()


        print(
            "Generated Java items:",
            item_generator.count()
        )



        entity_generator = JavaEntityGenerator(
            self.entity_translations,
            str(self.output_path)
        )

        print("ENTITY COUNT INPUT:", len(self.entity_translations))
        entity_generator.generate()


        print(
            "Generated Java entities:",
            entity_generator.count()
        )



        print()
        print("Generating Java source code...")
        print()


        block_code_generator = JavaBlockCodeGenerator(
            self.block_translations,
            str(self.output_path)
        )


        block_code_generator.generate()


        print(
            "Generated Java block classes:",
            block_code_generator.count()
        )


        print()
        print("Java project generation complete.")
        print()


        return True
