def translate_block_break(packet):

    return {
        "type": "player_action",
        "action": "break",
        "block": packet.get("block"),
        "x": packet.get("x"),
        "y": packet.get("y"),
        "z": packet.get("z")
    }

def translate_block_place(packet):

    return {
        "type": "player_action",
        "action": "place",
        "block": packet.get("block"),
        "x": packet.get("x"),
        "y": packet.get("y"),
        "z": packet.get("z")
    }
