from database.storagelayer import execute_mysql

from scoreboard.controller import validate_table_create


def create_table_transaction(table_name, column_names, column_data_types):
    validate_table_create(table_name, column_data_types, column_data_types)
    # generate comma-separated inputs to CREATE TABLE from the two input lists
    # TODO: make this next line not horrible
    args = [item for pair in zip(column_names, column_data_types, [","] * len(column_names)) for item in pair][:-1]
    args = " ".join(args)
    command = "CREATE TABLE {}({})".format(table_name, args)
    execute_mysql(command)
