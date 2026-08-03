def write_varint(value):

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



def write_string(value):

    encoded = value.encode("utf-8")

    return (
        write_varint(len(encoded))
        +
        encoded
    )



def create_packet(packet_id, payload=b""):

    packet = (
        write_varint(packet_id)
        +
        payload
    )

    return (
        write_varint(len(packet))
        +
        packet
    )
