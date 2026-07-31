from core.handler_registry import TRANSLATORS



def translate(packet):

    packet_type = packet.type


    if packet_type in TRANSLATORS:

        translator = TRANSLATORS[
            packet_type
        ]

        return translator(
            packet.data
        )


    return {
        "type": "unknown"
    }
