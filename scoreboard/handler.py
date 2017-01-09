from core import Handler

from flask import request

class ScoreBoardHandler(Handler):
    def ping(self):
        return self.package_response("pong")

    def pingback(self):
        return self.package_response(request.form)

    def attach_db(self, db):
        self.db = db

    def __init__(self):
        self.db = None
        self.services = {
            "/ping": self.ping,
            "/pingback": self.pingback}
