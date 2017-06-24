from flask import request

from sql_wrapper.transactions import create_table_transaction, drop_table_transaction
from src.core import Handler


class SQLWrapperHandler(Handler):
    """ Direct calls to SQL commands - mostly for testing
    """
    #TODO: all services here should require extra validation
    def create_table(self):
        request_json = request.get_json(force=True)
        table_name = request_json.get("table_name")
        column_names = request_json.get("column_names")
        column_data_types = request_json.get("column_data_types")
        create_table_transaction(table_name, column_names, column_data_types)
        return "Done"

    def drop_table(self):
        request_json = request.get_json(force=True)
        table_name = request_json.get("table_name")
        drop_table_transaction(table_name)
        return "Done"

    def __init__(self):
        self.services = {
            "/create_table": self.create_table,
            "/drop_table": self.drop_table
        }