from core import Handler


class ScoreBoardHandler(Handler):
    def ping(self):
        return self.package_response("pong")

    def __init__(self):
        self.services = {"/": self.ping}
