import socket

from runtime.java.connection import JavaConnection


class JavaListener:
    """
    Listens for incoming Java Edition connections.
    """

    def __init__(
        self,
        host="0.0.0.0",
        port=25565
    ):

        self.host = host
        self.port = port
        self.server = None


    def start(self):

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        self.server.bind(
            (self.host, self.port)
        )

        self.server.listen(5)


    def accept(self):

        socket_connection, address = self.server.accept()

        print(
            f"Java client connected: {address}"
        )

        return JavaConnection(
            socket_connection,
            address
        )


    def stop(self):

        if self.server:

            self.server.close()

            self.server = None

            print(
                "Java listener stopped."
            )
