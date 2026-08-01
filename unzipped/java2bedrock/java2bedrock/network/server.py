import socket
import threading
import json
import sys

sys.path.append("..")

from core.packet import Packet

from core.validator import validate
from core.queue import add_packet, get_packet
from core.translator import translate
from core.loaders.loader_manager import load_everything


HOST = "0.0.0.0"
PORT = 9000


# Load registries before starting the server
load_everything(
    "/root/test_server"
)


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server.bind(
    (HOST, PORT)
)

server.listen(5)


print("Java2Bedrock waiting...")



def process_queue(connection):

    while True:

        packet = get_packet()


        if packet is None:
            continue


        translated = translate(
            packet
        )


        print(
            "Translated:",
            translated
        )


        try:

            connection.send(
                json.dumps(
                    translated
                ).encode()
            )


        except OSError:

            print(
                "Client disconnected before response"
            )

            break





def handle_client(connection, address):

    print(
        "Connected:",
        address
    )


    processor = threading.Thread(
        target=process_queue,
        args=(connection,),
        daemon=True
    )

    processor.start()



    while True:

        try:

            data = connection.recv(
                1024
            )


        except ConnectionResetError:

            print(
                "Client disconnected unexpectedly"
            )

            break



        if not data:

            break



        try:

            raw_packet = json.loads(
                data.decode()
            )


        except json.JSONDecodeError:

            print(
                "Invalid JSON"
            )

            continue



        print(
            "Received:",
            raw_packet
        )



        if validate(raw_packet):

            packet = Packet(
                raw_packet["type"],
                raw_packet
            )


            add_packet(
                packet
            )


            print(
                "Queued:",
                packet
            )


        else:

            print(
                "Invalid packet!"
            )



    connection.close()


    print(
        "Disconnected:",
        address
    )





while True:

    connection, address = server.accept()


    client = threading.Thread(
        target=handle_client,
        args=(connection, address),
        daemon=True
    )


    client.start()
