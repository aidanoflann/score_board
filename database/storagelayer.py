import MySQLdb

db = None


def connect():
    db = MySQLdb.connect(user="root", passwd="panda123")
    return db


def execute_mysql(command):
    cursor = connect().cursor()
    cursor.execute(command)
    cursor.close()