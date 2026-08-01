import os


def find_server_properties(path):
    """
    Find server.properties in a server folder.
    """

    file = os.path.join(path, "server.properties")

    if os.path.exists(file):
        return file

    return None


def read_server_properties(file):
    """
    Read server.properties into a dictionary.
    """

    properties = {}

    with open(file, "r") as f:

        for line in f:

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" in line:

                key, value = line.split("=", 1)

                properties[key] = value

    return properties


def load_server(path):
    """
    Load a Minecraft Bedrock server.
    """

    properties_file = find_server_properties(path)

    if properties_file is None:

        print("server.properties not found")
        return None


    properties = read_server_properties(properties_file)


    print("Server found!")
    print("World:", properties.get("level-name"))


    # Create the world folder path
    world_path = os.path.join(
        path,
        "worlds",
        properties.get("level-name")
    )


    properties["world-path"] = world_path


    print("World path:", world_path)


    return properties
