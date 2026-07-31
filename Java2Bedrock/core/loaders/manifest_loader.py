import os
import json


def load_manifest(pack_path):

    manifest = os.path.join(
        pack_path,
        "manifest.json"
    )


    if not os.path.exists(manifest):
        print("No manifest:", pack_path)
        return None


    with open(manifest, "r") as f:
        data = json.load(f)


    header = data.get("header", {})


    return {
        "name": header.get("name"),
        "uuid": header.get("uuid"),
        "version": header.get("version")
    }



def scan_pack_manifests(packs):

    results = []


    for pack in packs:

        info = load_manifest(pack)

        if info:
            print(
                "Loaded pack:",
                info["name"]
            )

            results.append(info)


    return results
