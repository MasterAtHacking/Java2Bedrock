from collections import deque


packet_queue = deque()


def add_packet(packet):
    packet_queue.append(packet)


def get_packet():

    if packet_queue:
        return packet_queue.popleft()

    return None
