import os
import shutil


class AssetExporter:
    """
    Copies Bedrock resources into the Java project.
    """


    def __init__(
        self,
        resources,
        output_path
    ):

        self.resources = resources
        self.output_path = output_path
        self.exported = 0



    def export(self):

        assets_path = os.path.join(
            self.output_path,
            "assets"
        )

        os.makedirs(
            assets_path,
            exist_ok=True
        )


        for resource, data in self.resources.items():

            source = data.get(
                "path"
            )

            if source is None:
                continue


            destination = os.path.join(
                assets_path,
                resource
            )


            os.makedirs(
                os.path.dirname(destination),
                exist_ok=True
            )


            shutil.copy2(
                source,
                destination
            )


            self.exported += 1



    def count(self):

        return self.exported
