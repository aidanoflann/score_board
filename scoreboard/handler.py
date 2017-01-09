from core import Handler


class ScoreBoardHandler(Handler):
    def ping(self):
        return self.package_response("pong")

    def pingback(self, ping_data):
        return self.package_response(ping_data)

    def attach_db(self, db):
        self.db = db

    def __init__(self):
        self.db = None
        self.services = {
            "/ping": self.ping,
            "/pingback": self.pingback}
