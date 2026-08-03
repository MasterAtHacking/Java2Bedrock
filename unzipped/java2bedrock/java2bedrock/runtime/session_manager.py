class SessionManager:
    """
    Keeps track of active Java sessions.
    """

    def __init__(self):

        self.sessions = {}

    def add(self, session):

        self.sessions[session.session_id] = session

    def remove(self, session):

        self.sessions.pop(
            session.session_id,
            None
        )

    def get(self, session_id):

        return self.sessions.get(
            session_id
        )

    def count(self):

        return len(
            self.sessions
        )

    def all(self):

        return list(
            self.sessions.values()
        )
