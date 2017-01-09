from core import Handler


class ScoreBoardHandler(Handler):
    def hello(self):
        return "Hello World!"

    def __init__(self):
        self.services = {"/": self.hello}