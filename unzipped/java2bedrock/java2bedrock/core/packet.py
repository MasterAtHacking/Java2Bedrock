class Packet:
    def __init__(self, packet_type, data):
        self.type = packet_type
        self.data = data

    def __str__(self):
        return f"{self.type}: {self.data}"
