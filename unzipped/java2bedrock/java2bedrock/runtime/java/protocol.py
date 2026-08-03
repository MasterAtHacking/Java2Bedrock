class ProtocolError(Exception):
    """
    Raised when a Minecraft protocol error occurs.
    """
    pass



def read_varint(stream):
    """
    Read a Minecraft VarInt from a socket.
    """

    value = 0
    position = 0

    while True:

        raw = stream.recv(1)

        if not raw:
            raise ConnectionError(
                "Connection closed while reading VarInt"
            )


        byte = raw[0]


        value |= (byte & 0x7F) << position


        if not (byte & 0x80):
            break


        position += 7


        if position >= 35:
            raise ProtocolError(
                "VarInt is too large"
            )


    return value



def write_varint(value):
    """
    Encode an integer as a Minecraft VarInt.
    """

    output = bytearray()


    while True:

        temp = value & 0x7F

        value >>= 7


        if value:

            temp |= 0x80


        output.append(
            temp
        )


        if not value:
            break


    return bytes(output)



def read_string(stream):
    """
    Read a Minecraft UTF-8 string.
    """

    length = read_varint(
        stream
    )


    data = stream.recv(
        length
    )


    if len(data) != length:

        raise ConnectionError(
            "Incomplete string received"
        )


    return data.decode(
        "utf-8"
    )



def write_string(value):
    """
    Write a Minecraft UTF-8 string.
    """

    data = value.encode(
        "utf-8"
    )


    return (
        write_varint(len(data))
        +
        data
    )
