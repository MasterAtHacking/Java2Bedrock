from runtime.packet_pipeline import PacketPipeline
from runtime.state import ConnectionState

from runtime.java.packet_writer import PacketWriter
from runtime.java.play import PlayHandler
from runtime.java.configuration import ConfigurationHandler
from runtime.java.login import LoginHandler
from runtime.java.packet_reader import PacketReader
from runtime.java.handshake import decode_handshake


class Session:
    """
    Represents one Java player connection.
    """

    def __init__(
        self,
        java_socket,
        address,
        logger=None
    ):

        self.java_socket = java_socket
        self.address = address

        self.writer = PacketWriter(
            java_socket
        )

        self.logger = logger

        self.session_id = 0

        self.bedrock_connection = None

        self.username = None
        self.uuid = None

        self.running = False

        self.state = ConnectionState.HANDSHAKE

        self.login_handler = LoginHandler(
            self
        )

        self.configuration_handler = ConfigurationHandler(
            self
        )

        self.play_handler = PlayHandler(
            self
        )

        self.pipeline = PacketPipeline(
            self
        )


        def log(self, *message):

            text = " ".join(
                str(x)
                for x in message
            )

            output = (
                f"[Session #{self.session_id}] {text}"
            )

            print(output)

            if self.logger:

                self.logger.log(output)


    def log(self, *message):

        text = " ".join(
            str(x)
            for x in message
        )

        output = (
            f"[Session #{self.session_id}] {text}"
        )

        print(output)

        if self.logger:

            self.logger.log(output)

    def start(self):

        self.running = True

        self.log(
            "Session started"
        )


        reader = PacketReader(
            self.java_socket
        )


        while self.running:

            try:

                packet = reader.read_packet()

                self.pipeline.process(
                    packet
                )

                print()

                self.log(
                    "Java packet received"
                )

                self.log(
                    "ID:",
                    packet["id"]
                )


                if self.state == ConnectionState.HANDSHAKE:

                    self.handle_handshake(
                        packet
                    )


                elif self.state == ConnectionState.LOGIN:

                    self.login_handler.handle(
                        packet
                    )

                elif self.state == ConnectionState.PLAY:

                    self.play_handler.handle(
                        packet
                    )

                elif self.state == ConnectionState.CONFIGURATION:

                    self.configuration_handler.handle(
                        packet
                    )

            except OSError as e:

                # Expected when server shuts down
                # and closes the socket.

                if not self.running:

                    break


                self.log(
                    "Socket error:",
                    e
                )

                break


            except Exception as e:

                self.log(
                    "Session error:",
                    e
                )

                break


        self.stop()



    def handle_handshake(self, packet):

        try:

            handshake = decode_handshake(
                packet["data"]
            )


            print()

            self.log(
                "========== HANDSHAKE =========="
            )

            self.log(
                "Protocol:",
                handshake["protocol_version"]
            )

            self.log(
                "Address:",
                handshake["server_address"]
            )

            self.log(
                "Port:",
                handshake["server_port"]
            )

            self.log(
                "Next state:",
                handshake["next_state"]
            )

            self.log(
                "==============================="
            )


            if handshake["next_state"] == 2:

                self.state = ConnectionState.LOGIN

                self.log(
                    "Switching to LOGIN state"
                )


            elif handshake["next_state"] == 1:

                self.state = ConnectionState.STATUS

                self.log(
                    "Switching to STATUS state"
                )


        except Exception as e:

            self.log(
                "Handshake error:",
                e
            )



    def stop(self):

        if not self.running:

            return


        self.running = False


        try:

            self.java_socket.close()

        except OSError:

            pass


        self.log(
            "Session closed"
        )
