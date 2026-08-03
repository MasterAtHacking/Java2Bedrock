class BotPacketReader:
    """
    Reads Minecraft Java packets.
    """



    def __init__(self, connection):

        self.connection = connection



    def read_varint(self):

        value = 0

        position = 0


        while True:

            raw = self.connection.recv(
                1
            )


            if not raw:

                raise ConnectionError(
                    "Connection closed"
                )


            byte = raw[0]


            value |= (
                (byte & 0x7F)
                <<
                position
            )


            if not (byte & 0x80):

                break


            position += 7


            if position >= 35:

                raise ValueError(
                    "VarInt too large"
                )


        return value



    def read_packet(self):

        length = self.read_varint()


        data = b""


        while len(data) < length:

            chunk = self.connection.recv(
                length - len(data)
            )


            if not chunk:

                raise ConnectionError(
                    "Connection closed"
                )


            data += chunk



        packet_id = self.read_varint_bytes(
            data
        )


        return {
            "length": length,
            "id": packet_id,
            "data": data
        }



    def read_varint_bytes(self, data):

        value = 0

        position = 0


        for byte in data:

            value |= (
                (byte & 0x7F)
                <<
                position
            )


            if not (byte & 0x80):

                break


            position += 7


        return value
