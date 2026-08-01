from core.packet import Packet
from core.translator import translate_java_to_bedrock
from core.queue import PacketQueue


queue = PacketQueue()


queue.add(Packet(
    "player_move",
    {
        "x": 10,
        "y": 64,
        "z": 5
    }
))


queue.add(Packet(
    "chat",
    {
        "message": "Hello Bedrock!"
    }
))


while True:
    packet = queue.get()

    if packet is None:
        break

    print("Received:")
    print(packet)

    translated = translate_java_to_bedrock(packet)

    print("Translated:")
    print(translated)
    print("---")
