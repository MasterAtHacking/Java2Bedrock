from packets.java_packets import JAVA_PACKETS


def translate(packet):
    if packet in JAVA_PACKETS:
        return JAVA_PACKETS[packet]
    else:
        return "UNKNOWN_PACKET"


while True:
    data = input("Java packet: ")
    result = translate(data)
    print("Bedrock packet:", result)
