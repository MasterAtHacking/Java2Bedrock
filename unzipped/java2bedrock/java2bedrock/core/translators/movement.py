def translate_movement(packet):

    return {
        "type": "move_player",
        "x": packet.get("x"),
        "y": packet.get("y"),
        "z": packet.get("z")
    }

