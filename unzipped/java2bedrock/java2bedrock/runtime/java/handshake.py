from runtime.java.protocol import read_varint


def read_unsigned_short(data, offset):

    value = int.from_bytes(
        data[offset:offset+2],
        "big"
    )

    return value, offset + 2



def read_string_from_bytes(data, offset):

    length = 0
    position = 0


    while True:

        byte = data[offset]

        offset += 1

        length |= (
            byte & 0x7F
        ) << position


        if not byte & 0x80:
            break


        position += 7


    string = data[
        offset:
        offset + length
    ].decode("utf-8")


    return string, offset + length



def decode_handshake(data):

    offset = 0


    protocol_version, offset = read_varint_bytes(
        data,
        offset
    )


    server_address, offset = read_string_from_bytes(
        data,
        offset
    )


    server_port, offset = read_unsigned_short(
        data,
        offset
    )


    next_state, offset = read_varint_bytes(
        data,
        offset
    )


    return {

        "protocol_version": protocol_version,

        "server_address": server_address,

        "server_port": server_port,

        "next_state": next_state

    }

def read_varint_bytes(data, offset):

    value = 0
    position = 0


    while True:

        byte = data[offset]

        offset += 1


        value |= (
            byte & 0x7F
        ) << position


        if not byte & 0x80:

            break


        position += 7


    return value, offset
