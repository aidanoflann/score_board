from flask import request

from core import Handler

from scoreboard.transactions import create_table_transaction


class ScoreBoardManagementHandler(Handler):
    #TODO: all services here should require extra validation
    def create_table(self):
        request_json = request.get_json(force=True)
        table_name = request_json.get("table_name")
        column_names = request_json.get("column_names")
        column_data_types = request_json.get("column_data_types")
        create_table_transaction(table_name, column_names, column_data_types)
        return "Done"

    def __init__(self):
        self.services = {
            "/create_table": self.create_table
        }

class ScoreBoardHandler(Handler):
    def __init__(self):
        self.db = None
        self.services = {}
