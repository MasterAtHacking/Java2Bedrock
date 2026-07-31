from pathlib import Path


class JavaBlockCodeGenerator:
    """
    Generates Java block source files.
    """


    def __init__(self, blocks, output_path):

        self.blocks = blocks
        self.output_path = Path(output_path)
        self.generated = 0



    def generate(self):

        java_path = (
            self.output_path
            / "src/main/java/generated/blocks"
        )

        java_path.mkdir(
            parents=True,
            exist_ok=True
        )


        for identifier, data in self.blocks.items():

            class_name = self.make_class_name(
                identifier
            )


            file = java_path / (
                class_name + ".java"
            )


            code = f"""
package generated.blocks;


public class {class_name} {{

    public static final String ID =
        "{identifier}";


    public {class_name}() {{

    }}

}}
"""


            with open(
                file,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(
                    code.strip()
                )


            self.generated += 1



    def make_class_name(self, identifier):

        name = identifier.split(":")[-1]

        return "".join(
            part.capitalize()
            for part in name.split("_")
        )



    def count(self):

        return self.generated
