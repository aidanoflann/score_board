def validate_table_create(table_name, column_names, column_data_types):
    if len(column_names) != len(column_data_types):
        raise ValueError("Cannot create table. {} column names but {} column data types were given."
                         .format(len(column_names), len(column_data_types)))
