import socket
import time



HOST = "127.0.0.1"
PORT = 25565



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

    encoded = value.encode(
        "utf-8"
    )


    return (
        write_varint(
            len(encoded)
        )
        +
        encoded
    )



def create_handshake():

    packet = b""


    packet += write_varint(0)


    packet += write_varint(
        772
    )


    packet += write_string(
        "localhost"
    )


    packet += (
        25565
        .to_bytes(
            2,
            "big"
        )
    )


    packet += write_varint(
        2
    )


    return (
        write_varint(
            len(packet)
        )
        +
        packet
    )



def create_login_start():

    packet = b""


    # Login Start packet ID
    packet += write_varint(
        0
    )


    packet += write_string(
        "TestPlayer"
    )


    return (
        write_varint(
            len(packet)
        )
        +
        packet
    )


def create_login_acknowledged():

    packet = b""


    # Login Acknowledged packet ID
    packet += write_varint(
        3
    )


    return (
        write_varint(
            len(packet)
        )
        +
        packet
    )

def create_finish_configuration():

    packet = b""


    # Finish Configuration packet ID
    packet += write_varint(
        3
    )


    return (
        write_varint(
            len(packet)
        )
        +
        packet
    )

def create_play_test_packet():

    packet = b""


    # Fake PLAY packet ID
    packet += write_varint(
        0
    )


    return (
        write_varint(
            len(packet)
        )
        +
        packet
    )
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


client.connect(
    (
        HOST,
        PORT
    )
)


print(
    "Connected"
)



client.send(
    create_handshake()
)


print(
    "Handshake sent"
)



time.sleep(1)



client.send(
    create_login_start()
)

time.sleep(2)


client.send(
    create_login_acknowledged()
)


print(
    "Login Acknowledged sent"
)

time.sleep(2)


client.send(
    create_finish_configuration()
)


print(
    "Finish Configuration sent"
)


time.sleep(2)


client.send(
    create_play_test_packet()
)


print(
    "PLAY test packet sent"
)

print(
    "PLAY test packet sent"
)

print(
    "Login Start sent"
)



try:

    sent_ack = False


    while True:

        data = client.recv(
            1024
        )


        if not data:

            break


        print(
            "Received:",
            data
        )



except KeyboardInterrupt:

    pass



client.close()


print(
    "Disconnected"
)
