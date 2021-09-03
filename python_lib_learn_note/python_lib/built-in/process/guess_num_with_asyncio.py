import random


class EOFError(Exception):
    pass


class ConnectionBase:
    def __init__(self, connection) -> None:
        self.connection = connection
        self.file = connection.makefile('rb')

    def send(self, commad):
        line = commad + '\n'
        data = line.encode()
        self.connection.send(data)

    def receive(self):
        line = self.file.readline()
        if not line:  # line会是什么
            raise EOFError("Connection closed")
        return line[:-1].decode()


WARMER = 'Warmer'
COLDER = 'Colder'
UNSURE = 'Unsure'
CORRECT = 'Correct'


class UnknownCommandError(Exception):
    pass


class Session(ConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state(None, None)

    def _clear_state(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []