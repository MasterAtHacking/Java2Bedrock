from runtime.java.protocol import read_varint


class PacketReader:
    """
    Reads Minecraft Java packets.
    """


    def __init__(self, connection):

        self.connection = connection



    def read_packet(self):

        length = read_varint(
            self.connection
        )


        packet_data = b""


        while len(packet_data) < length:

            chunk = self.connection.recv(
                length - len(packet_data)
            )


            if not chunk:

                raise ConnectionError(
                    "Connection closed"
                )


            packet_data += chunk



        packet_id = read_varint_from_bytes(
            packet_data
        )


        packet_id_length = 1


        packet_payload = packet_data[
            packet_id_length:
        ]


        return {
            "length": length,
            "id": packet_id,
            "data": packet_payload
        }


def read_varint_from_bytes(data):

    value = 0
    position = 0


    for byte in data:

        value |= (byte & 0x7F) << position


        if not (byte & 0x80):

            break


        position += 7


    return value
