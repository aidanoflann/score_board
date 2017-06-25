import MySQLdb

import settings


def connect():
    # Create the database if not present
    # TODO: put all inside if db doesn't exist block (no need to connect twice every time)
    print("Attempting to connect to mysql database...")
    db = MySQLdb.connect(host="localhost", user=settings.MYSQL_USERNAME, passwd=settings.MYSQL_PASSWORD)
    cursor = db.cursor()
    sql = 'CREATE DATABASE IF NOT EXISTS {}'.format(settings.MYSQL_SCOREBOARD_DB_NAME)
    cursor.execute(sql)
    db = MySQLdb.connect(host="localhost", user="root", passwd="my-secret-pw", db="test")
    if db is None:
        raise Exception("Failed to connect to mysql database. Exiting...")
    print("Connection successful.")
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
