from sql_wrapper.transactions import insert_into_table_transaction


def insert_score_transaction(game_name, user, score):
    """ Add the user's name, score, and current server time to the table (based on game_name).

    :param game_name:
    :param user:
    :param score:
    :return:
    """
    field_names = ["user", "score"]
    field_values = [user, score]
    insert_into_table_transaction(game_name, field_names, field_values)