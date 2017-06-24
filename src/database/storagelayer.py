import MySQLdb


def connect():
    # TODO: Create the database if not present
    print("Attempting to connect to mysql database...")
    db = MySQLdb.connect(host="mysql_db", user="root", passwd="my-secret-pw", db="test")
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
