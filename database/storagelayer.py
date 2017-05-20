import MySQLdb
import settings

db = None


def connect():
    # Create the database if not present
    # TODO: put all inside if db doesn't exist block (no need to connect twice every time)
    db = MySQLdb.connect(user=settings.MYSQL_USERNAME, passwd=settings.MYSQL_PASSWORD)
    cursor = db.cursor()
    sql = 'CREATE DATABASE IF NOT EXISTS {}'.format(settings.MYSQL_SCOREBOARD_DB_NAME)
    cursor.execute(sql)

    db = MySQLdb.connect(user=settings.MYSQL_USERNAME, passwd=settings.MYSQL_PASSWORD,
                         db=settings.MYSQL_SCOREBOARD_DB_NAME)
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
