import socket
import json
import time


HOST = "127.0.0.1"
PORT = 9000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


packets = [
    {
        "id": 1,
        "time": time.time(),
        "type": "player_move",
        "x": 10,
        "y": 64,
        "z": 5
    },
    {
        "id": 2,
        "time": time.time(),
        "type": "chat",
        "message": "Hello from Java2Bedrock"
    },
    {
        "id": 3,
        "time": time.time(),
        "type": "block_break",
        "block": "minecraft:stone",
        "x": 11,
        "y": 64,
        "z": 5
    }
]

for packet in packets:

    client.send(
        json.dumps(packet).encode()
    )

    print("Sent:", packet)

    time.sleep(0.5)


response = client.recv(1024)

print("Received:", response.decode())


client.close()
