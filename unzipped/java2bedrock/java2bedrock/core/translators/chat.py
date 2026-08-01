def translate_chat(packet):

    return {
        "type": "text",
        "message": packet.get("message")
    }
