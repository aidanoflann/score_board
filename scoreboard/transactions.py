from database.storagelayer import execute_mysql

from scoreboard.controller import validate_table_create


def create_table_transaction(table_name, column_names, column_data_types):
    validate_table_create(table_name, column_data_types, column_data_types)
    args = [item for pair in zip(column_names, column_data_types) for item in pair]
    args = " ".join(args)
    command = "CREATE TABLE {}({})".format(table_name, args)
    execute_mysql(command)
