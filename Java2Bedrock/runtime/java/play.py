from runtime.state import ConnectionState


class PlayHandler:
    """
    Handles Java PLAY state packets.
    """


    def __init__(self, session):

        self.session = session



    def handle(self, packet):

        packet_id = packet["id"]


        self.session.log(
            "Play packet:",
            packet_id
        )


        # Temporary test packet
        if packet_id == 0:

            self.handle_test_packet(
                packet["data"]
            )


    def handle_test_packet(self, data):

        self.session.log(
            "Test PLAY packet received"
        )
