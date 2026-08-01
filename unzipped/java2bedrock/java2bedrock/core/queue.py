from collections import deque


packet_queue = deque()



def add_packet(packet):
    """
    Add a Packet object to the queue.
    """

    packet_queue.append(
        packet
    )



def get_packet():
    """
    Retrieve the next packet.
    """

    if packet_queue:

        return packet_queue.popleft()


    return None
