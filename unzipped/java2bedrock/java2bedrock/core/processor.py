import time
import sys

sys.path.append("..")

from core.queue import get_packet
from core.translator import translate

print("Processor running...")

def process_packets(connection):

    while True:

        packet = get_packet()

        if packet:

            translated = translate(packet)

            connection.send(
                str(translated).encode()
            )

        time.sleep(0.01)
