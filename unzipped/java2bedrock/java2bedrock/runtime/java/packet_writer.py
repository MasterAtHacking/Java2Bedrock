import uuid


class PacketWriter:
    """
    Writes Java protocol packets.
    """


    def __init__(self, connection):

        self.connection = connection



    def write_varint(self, value):

        data = b""


        while True:

            temp = value & 0x7F

            value >>= 7


            if value:

                temp |= 0x80


            data += bytes([temp])


            if not value:

                break


        return data



    def write_string(self, value):

        encoded = value.encode("utf-8")

        return (
            self.write_varint(len(encoded))
            +
            encoded
        )



    def send_packet(self, packet_id, payload):

        packet = b""

        packet += self.write_varint(packet_id)

        packet += payload

        packet = (
            self.write_varint(len(packet))
            +
            packet
        )

        self.connection.send(packet)



    def send_login_success(self, username):

        payload = b""

        player_uuid = uuid.uuid4().bytes

        payload += player_uuid

        payload += self.write_string(username)

        payload += self.write_varint(0)

        self.send_packet(
            0x02,
            payload
        )

    def send_join_game(self):

        payload = b""


        # Entity ID
        payload += (1).to_bytes(
            4,
            "big",
            signed=True
        )


        # Hardcore
        payload += bytes([0])


        # Game mode
        payload += bytes([1])


        # Previous game mode
        payload += bytes([0])


        # World count
        payload += self.write_varint(1)


        # World name
        payload += self.write_string(
            "minecraft:overworld"
        )


        # Dimension codec placeholder
        payload += self.write_varint(0)


        # Dimension type placeholder
        payload += self.write_varint(0)


        # World name
        payload += self.write_string(
            "minecraft:overworld"
        )


        # Hashed seed
        payload += (0).to_bytes(
            8,
            "big",
            signed=True
        )


        # Max players
        payload += self.write_varint(20)


        # View distance
        payload += self.write_varint(10)


        # Simulation distance
        payload += self.write_varint(10)


        # Reduced debug info
        payload += bytes([0])


        # Enable respawn screen
        payload += bytes([1])


        self.send_packet(
            0x28,
            payload
        )
