import time

import MySQLdb

import settings

db = None


def connect():
    # Create the database if not present
    # TODO: put all inside if db doesn't exist block (no need to connect twice every time)
    attempts = 0
    print("Attempting to connect to mysql database...")
    while attempts < settings.RETRY_ATTEMPTS:
        try:
            db = MySQLdb.connect(host="mysql_db", user=settings.MYSQL_USERNAME, passwd=settings.MYSQL_PASSWORD)
            cursor = db.cursor()
            sql = 'CREATE DATABASE IF NOT EXISTS {}'.format(settings.MYSQL_SCOREBOARD_DB_NAME)
            cursor.execute(sql)

            db = MySQLdb.connect(user=settings.MYSQL_USERNAME, passwd=settings.MYSQL_PASSWORD,
                                 db=settings.MYSQL_SCOREBOARD_DB_NAME)
        except Exception as e:
            print("Attempt to connect to mysql DB failed. Retrying in {} seconds.".format(settings.RETRY_PERIOD))
            print("Attempt number: {}. Max attempts: {}.".format(attempts, settings.RETRY_ATTEMPTS))
            print("Error args: {}".format(str(e.args)))
            attempts += 1
            time.sleep(settings.RETRY_PERIOD)

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
