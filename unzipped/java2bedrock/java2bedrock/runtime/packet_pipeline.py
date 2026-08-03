from runtime.java.packet_decoder import JavaPacketDecoder
from core.validator import validate
from runtime.packet_adapter import PacketAdapter
from runtime.state import ConnectionState

class PacketPipeline:
    """
    Handles gameplay packets only.
    """


    def __init__(self, session):

        self.session = session

        self.adapter = PacketAdapter()

        self.decoder = JavaPacketDecoder()


    def process(self, packet):

        # Ignore handshake/login packets

        if self.session.state != ConnectionState.PLAY:

            print(
                "[Pipeline] Skipping non-play packet"
            )

            return True


        print(
            "[Pipeline] Processing gameplay packet"
        )


        decoded_packet = self.decoder.decode(
            packet
        )


        internal_packet = self.adapter.adapt(
            decoded_packet
        )

        if not validate(internal_packet):

            print(
                "[Pipeline] Packet rejected"
            )

            return False


        print(
            "[Pipeline] Packet accepted"
        )

        return True
