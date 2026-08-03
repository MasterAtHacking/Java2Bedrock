import socket
import threading


from reader import BotPacketReader


from packets import (
    create_packet,
    write_varint,
    write_string
)



HOST = "127.0.0.1"
PORT = 25565
PROTOCOL = 772

stop_event = threading.Event()

def receive_loop(
    sock,
    stop_event
):

    reader = BotPacketReader(
        sock
    )


    try:

        while not stop_event.is_set():

            packet = reader.read_packet()


            print()

            print(
                "[Server Packet]",
                packet["id"]
            )


            print(
                packet["data"].hex()
            )

            print()

            print(
                "> ",
                end="",
                flush=True
            )


    except Exception:

        if not stop_event.is_set():

            print()

            print(
                "Receiver stopped"
            )


def send(
    sock,
    packet_id,
    payload
):

    sock.send(
        create_packet(
            packet_id,
            payload
        )
    )



def handshake(sock):

    payload = b""


    payload += write_varint(
        PROTOCOL
    )


    payload += write_string(
        "localhost"
    )


    payload += (25565).to_bytes(
        2,
        "big"
    )


    payload += write_varint(
        2
    )


    send(
        sock,
        0x00,
        payload
    )



def login_start(
    sock,
    username
):

    payload = write_string(
        username
    )


    send(
        sock,
        0x00,
        payload
    )



def show_help():

    print()

    print(
        "Commands:"
    )

    print()

    print(
        " help   - Show commands"
    )

    print(
        " status - Show bot status"
    )

    print(
        " quit   - Disconnect"
    )

    print()



def command_loop(
    sock,
    username
):

    show_help()


    while True:

        command = input(
            "> "
        )


        command = command.strip()



        if command == "help":

            show_help()



        elif command == "status":

            print()

            print(
                "Connected: True"
            )

            print(
                "Bot name:",
                username
            )

            print(
                "Server:",
                HOST,
                PORT
            )

            print()



        elif command == "quit":

            print(
                "Stopping bot..."
            )

            break



        else:

            print(
                "Unknown command. Type help."
            )



def main():

    username = input(
        "Bot name: "
    )


    sock = socket.socket()


    try:

        print(
            "Connecting..."
        )


        sock.connect(
            (
                HOST,
                PORT
            )
        )


        print(
            "Connected!"
        )


        handshake(
            sock
        )


        print(
            "Handshake sent"
        )


        receiver = threading.Thread(
            target=receive_loop,
            args=(
                sock,
                stop_event
            )
        )


        receiver.start()

        login_start(
            sock,
            username
        )


        print(
            "Login Start sent"
        )


        command_loop(
            sock,
            username
        )


    except KeyboardInterrupt:

        print()

        print(
            "Stopping bot..."
        )


    finally:

        stop_event.set()


        sock.close()


        if "receiver" in locals():

            receiver.join(
                timeout=2
            )


        print(
            "Disconnected"
        )


if __name__ == "__main__":

    main()
