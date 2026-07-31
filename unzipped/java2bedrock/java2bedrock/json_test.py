import json


java_packet = {
    "type": "player_move",
    "x": 10,
    "y": 64,
    "z": 5,
    "yaw": 90,
    "pitch": 0
}


encoded = json.dumps(java_packet)

print(encoded)
