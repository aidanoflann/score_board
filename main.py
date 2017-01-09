import MySQLdb

from flask import Flask

from scoreboard.handler import ScoreBoardHandler


def initialise_database():
    db=MySQLdb.connect(user="root", passwd="panda123")
    ScoreBoardHandler().attach_db(db)


def initialise_handlers(app):
    ScoreBoardHandler().register(app)

if __name__ == "__main__":
    app = Flask(__name__)

    initialise_database()
    initialise_handlers(app)

    app.run()
