import time

from core.registries.block_registry import is_valid_block
from core.registry import PACKET_REGISTRY


def validate(packet):

    # Check required fields
    required = [
        "id",
        "time",
        "type"
    ]

    for field in required:

        if field not in packet:
            print("Missing field:", field)
            return False

    # Check packet ID
    if not isinstance(packet["id"], int):
        print("Invalid packet ID")
        return False

    # Check timestamp
    age = time.time() - packet["time"]

    if age > 10:
        print("Packet too old")
        return False

    # Check packet type using registry
    if packet["type"] not in PACKET_REGISTRY:
        print("Unknown packet type")
        return False

    # Validate blocks
    if packet["type"] in ("block_break", "block_place"):

        if "block" not in packet:
            print("Missing block identifier")
            return False

        if not is_valid_block(packet["block"]):
            print("Unknown block:", packet["block"])
            return False

    return True
