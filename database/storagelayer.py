import MySQLdb

db = None


def connect():
    db = MySQLdb.connect(user="root", passwd="panda123", db="test")
    return db


def execute_mysql(command):
    cursor = connect().cursor()
    # TODO: get cursor without reconnecting?
    cursor.execute(command)
    cursor.close()