class JavaConnection:
    """
    Wrapper around a Java client socket.
    """


    def __init__(
        self,
        socket,
        address
    ):

        self.socket = socket
        self.address = address


    def recv(
        self,
        size=4096
    ):

        return self.socket.recv(
            size
        )


    def send(
        self,
        data
    ):

        return self.socket.send(
            data
        )


    def close(self):

        try:

            self.socket.close()

        except OSError:

            pass
