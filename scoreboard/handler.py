from flask import request

from core import Handler

from scoreboard.transactions import insert_score_transaction


class ScoreBoardHandler(Handler):
    def insert_score(self):
        request_json = request.get_json(force=True)
        game_name = request_json.get("game_name")
        user = request_json.get("user")
        score = str(request_json.get("score"))
        insert_score_transaction(game_name, user, score)
        return "Done"

    def __init__(self):
        self.db = None
        self.services = {
            "/insert_score": self.insert_score
        }
