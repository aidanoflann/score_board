import time

from sql_wrapper.transactions import insert_into_table_transaction, create_table_transaction, \
    select_all_transaction

from utils.formatting_utils import enquote


def create_scoreboard_transaction(game_name):
    """ Create a fresh scoreboard for a game.

    :param game_name:   name of the game. used as the scoreboard name.
    """
    # TODO: store metadata?
    column_names = ["user", "score", "time"]
    column_data_types = ["TEXT", "INTEGER", "DATETIME"]
    create_table_transaction(game_name, column_names, column_data_types)


def insert_score_transaction(game_name, user, score):
    """ Add the user's name, score, and current server time to the table (based on game_name).

    :param game_name:
    :param user:
    :param score:
    """
    field_names = ["user", "score", "time"]
    field_values = [enquote(user), enquote(score), enquote(time.strftime('%Y-%m-%d %H:%M:%S'))]
    insert_into_table_transaction(game_name, field_names, field_values)


def get_top_scores_transaction(game_name):
    """ Get all scores from the "top x" score board.

    :param game_name:
    :return:
    """
    sql_fetch_data = select_all_transaction(game_name)
    sql_fetch_list_of_dicts = []
    for data_tuple in sql_fetch_data:
        sql_fetch_list_of_dicts.append({
            "user": data_tuple[0],
            "score": data_tuple[1],
            "time": str(data_tuple[2])
        })
    return {"scores": sql_fetch_list_of_dicts}
