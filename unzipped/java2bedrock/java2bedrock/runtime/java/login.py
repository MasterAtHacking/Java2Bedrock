from runtime.java.login_decoder import LoginDecoder


class LoginHandler:
    """
    Handles the Java login phase.
    """



    def __init__(self, session):

        self.session = session



    def handle(self, packet):

        packet_id = packet["id"]

        self.session.log(
            "Login packet:",
            packet_id
        )


        # Login Start

        if packet_id == 0:

            decoded = LoginDecoder.decode_login_start(
                packet["data"]
            )


            self.handle_login_start(
                decoded
            )


        # Login Acknowledged

        elif packet_id == 3:

            self.handle_login_acknowledged()



    def handle_login_acknowledged(self):

        self.session.log(
            "Login Acknowledged received"
        )


        from runtime.state import ConnectionState


        self.session.state = ConnectionState.CONFIGURATION


        self.session.log(
            "Switching to CONFIGURATION state"
        )



    def handle_login_start(self, data):

        self.session.log(
            "Received Login Start"
        )


        self.session.username = data["username"]


        self.session.log(
            "Player:",
            self.session.username
        )


        self.session.log(
            "Sending Login Success..."
        )


        self.session.writer.send_login_success(
            self.session.username
        )


        self.session.log(
            "Login Success sent."
        )
