import os

from core.registries.resource_registry import register_resource


def find_resource_files(pack_path):
    """
    Find resource files inside a resource pack.
    """

    files = []


    for root, dirs, filenames in os.walk(pack_path):

        for file in filenames:

            full_path = os.path.join(
                root,
                file
            )

            files.append(
                full_path
            )


    return files



def load_resource_file(file, pack_path):
    """
    Register one resource file.
    """

    relative = os.path.relpath(
        file,
        pack_path
    )


    identifier = relative.replace(
        "\\",
        "/"
    )


    register_resource(
        identifier,
        {
            "path": file
        }
    )


    print(
        "Registered resource:",
        identifier
    )



def load_resources_from_pack(pack_path):
    """
    Load all resources from one pack.
    """

    files = find_resource_files(
        pack_path
    )


    for file in files:

        load_resource_file(
            file,
            pack_path
        )
