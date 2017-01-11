def validate_table_create(table_name, column_names, column_data_types):
    if not isinstance(table_name, str):
        raise ValueError("Cannot create table. Table name must be a string: '{}'".format(table_name))
    if len(column_names) != len(column_data_types):
        raise ValueError("Cannot create table. {} column names but {} column data types were given."
                         .format(len(column_names), len(column_data_types)))
