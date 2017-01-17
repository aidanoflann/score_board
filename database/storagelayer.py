import MySQLdb

db = None


def connect():
    db = MySQLdb.connect(user="root", passwd="panda123", db="test")
    return db


def execute_mysql(command):
    # TODO: get cursor without reconnecting?
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(command)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    return result
