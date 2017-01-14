from core import Handler


class ScoreBoardHandler(Handler):
    def __init__(self):
        self.db = None
        self.services = {}
