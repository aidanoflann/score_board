from database.storagelayer import execute_mysql

from scoreboard.controller import validate_table_create

def create_table_transaction(table_name, column_names, column_data_types):
    validate_table_create(table_name, column_data_types, column_data_types)
    