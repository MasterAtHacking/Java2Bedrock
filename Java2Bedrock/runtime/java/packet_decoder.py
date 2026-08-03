from runtime.java.play_registry import PLAY_PACKETS


class JavaPacketDecoder:
    """
    Decodes Java PLAY packets into internal packet formats.
    """


    def decode(self, packet):

        packet_id = packet["id"]

        packet_type = PLAY_PACKETS.get(
            packet_id,
            "unknown"
        )

        print(
            "[Decoder] Packet:",
            packet_id,
            packet_type
        )

        return {
            "id": packet_id,
            "type": packet_type,
            "data": packet.get("data")
        }
