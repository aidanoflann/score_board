from flask import request

from core import Handler

from scoreboard.transactions import insert_score_transaction, create_scoreboard_transaction, get_top_scores_transaction


class ScoreBoardHandler(Handler):
    def create_scoreboard(self):
        request_json = request.get_json(force=True)
        game_name = request_json.get("game_name")
        create_scoreboard_transaction(game_name)
        return "Done"

    def insert_score(self):
        request_json = request.get_json(force=True)
        game_name = request_json.get("game_name")
        user = request_json.get("user")
        score = str(request_json.get("score"))
        insert_score_transaction(game_name, user, score)
        return "Done"

    def get_scores(self):
        request_json = request.get_json(force=True)
        game_name = request_json.get("game_name")
        result = get_top_scores_transaction(game_name)
        return str(result)

    def __init__(self):
        self.db = None
        self.services = {
            "/insert_score": self.insert_score,
            "/create_scoreboard": self.create_scoreboard,
            "/get_scores": self.get_scores
        }
