from database.storagelayer import execute_mysql

from sql_wrapper.controller import validate_table_create


def create_table_transaction(table_name, column_names, column_data_types):
    """ Create a table with the given name, columns and data types.

    :param table_name:          string, name of table to be created
    :param column_names:        [str], names of clumns to be created
    :param column_data_types:   [str], SQL-style data types. list len must match column_names
    """
    validate_table_create(table_name, column_data_types, column_data_types)
    # generate comma-separated inputs to CREATE TABLE from the two input lists
    # TODO: make this next line not horrible
    args = [item for pair in zip(column_names, column_data_types, [","] * len(column_names)) for item in pair][:-1]
    args = " ".join(args)
    command = "CREATE TABLE {}({})".format(table_name, args)
    execute_mysql(command)


def drop_table_transaction(table_name):
    """ Destroy the named table and all data contained within

    :param table_name:      name of table to be deleted.
    """
    command = "DROP TABLE {}".format(table_name)
    execute_mysql(command)


def insert_into_table_transaction(table_name, field_names, field_values):
    """

    :param table_name:
    :param field_names:
    :param field_values:
    :return:
    """
    cs_field_names = ", ".join(field_names)
    cs_field_values = ", ".join(field_values)
    command = "INSERT INTO {} ({}) VALUES ({})".format(table_name, cs_field_names, cs_field_values)
    execute_mysql(command)


def select_all_transaction(table_name):
    """ Get all rows from the given table.

    :param table_name:
    :return:
    """
    command = "SELECT * FROM {}".format(table_name)
    result = execute_mysql(command)
    return result
