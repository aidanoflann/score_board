from sql_wrapper.transactions import insert_into_table_transaction, create_table_transaction


def create_scoreboard_transaction(game_name):
    """ Create a fresh scoreboard for a game.

    :param game_name:   name of the game. used as the scoreboard name.
    """
    column_names = ["user", "score"]
    column_data_types = ["TEXT", "INTEGER"]
    create_table_transaction(game_name, column_names, column_data_types)


def insert_score_transaction(game_name, user, score):
    """ Add the user's name, score, and current server time to the table (based on game_name).

    :param game_name:
    :param user:
    :param score:
    """
    field_names = ["user", "score"]
    field_values = [user, score]
    insert_into_table_transaction(game_name, field_names, field_values)