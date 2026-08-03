from runtime.state import ConnectionState


STATE_NAMES = {
    ConnectionState.HANDSHAKE: "HANDSHAKE",
    ConnectionState.STATUS: "STATUS",
    ConnectionState.LOGIN: "LOGIN",
    ConnectionState.CONFIGURATION: "CONFIGURATION",
    ConnectionState.PLAY: "PLAY",
    ConnectionState.CLOSED: "CLOSED"
}


def get_state_name(state):

    return STATE_NAMES.get(
        state,
        "UNKNOWN"
    )
