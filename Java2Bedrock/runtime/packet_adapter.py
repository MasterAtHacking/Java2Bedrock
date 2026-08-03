import time


class PacketAdapter:
    """
    Converts decoded Java packets into Java2Bedrock internal packets.
    """


    def adapt(self, packet):

        return {
            "id": packet["id"],
            "time": time.time(),
            "type": packet.get(
                "type",
                "unknown"
            ),
            "data": packet.get(
                "data"
            )
        }
