from runtime.java.protocol import ProtocolError



def read_varint_bytes(data, offset=0):

    value = 0

    position = 0


    while True:

        if offset >= len(data):

            raise ProtocolError(
                "Incomplete VarInt"
            )


        byte = data[offset]


        offset += 1


        value |= (
            (byte & 0x7F)
            <<
            position
        )


        if not (byte & 0x80):

            break


        position += 7


        if position >= 35:

            raise ProtocolError(
                "VarInt is too large"
            )


    return value, offset



def read_string_bytes(data, offset=0):

    length, offset = read_varint_bytes(
        data,
        offset
    )


    value = data[
        offset:
        offset + length
    ]


    if len(value) != length:

        raise ProtocolError(
            "Incomplete string"
        )


    return (
        value.decode(
            "utf-8"
        ),
        offset + length
    )



class LoginDecoder:
    """
    Decodes Java LOGIN packets.
    """



    @staticmethod
    def decode_login_start(data):

        username, _ = read_string_bytes(
            data
        )


        return {
            "username": username
        }
