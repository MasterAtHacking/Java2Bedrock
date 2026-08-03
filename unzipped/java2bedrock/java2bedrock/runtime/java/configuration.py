from runtime.state import ConnectionState


class ConfigurationHandler:
    """
    Handles the Java configuration phase.
    """


    def __init__(self, session):

        self.session = session



    def handle(self, packet):

        packet_id = packet["id"]


        self.session.log(
            "Configuration packet:",
            packet_id
        )


        # Client Information
        if packet_id == 0:

            self.handle_client_information(
                packet["data"]
            )


        # Finish Configuration
        elif packet_id == 3:

            self.handle_finish_configuration()

    def handle_client_information(self, data):

        self.session.log(
            "Client Information received"
        )

    def handle_finish_configuration(self):

        self.session.log(
            "Finish Configuration received"
        )


        self.session.state = ConnectionState.PLAY


        self.session.log(
            "Switching to PLAY state"
        )

        self.session.writer.send_join_game()

        self.session.log(
            "Join Game sent"
        )
