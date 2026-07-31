class Packet:
    def __init__(self, packet_type, data):
        self.type = packet_type
        self.data = data

    def __str__(self):
        return f"{self.type}: {self.data}"
class Packet:
    """
    Internal packet representation.

    This is the common format used between
    network layers and translators.
    """


    def __init__(
        self,
        packet_type,
        data=None
    ):

        self.type = packet_type

        if data is None:
            data = {}

        self.data = data



    def get(self, key, default=None):
        """
        Allow translators to access packet data
        like a normal dictionary.
        """

        return self.data.get(
            key,
            default
        )



    def __getitem__(self, key):
        """
        Backwards compatibility with
        dictionary-style packet access.
        """

        return self.data[key]



    def __str__(self):

        return f"{self.type}: {self.data}"
