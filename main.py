from flask import Flask

from database.storagelayer import connect

from scoreboard.handler import ScoreBoardHandler


def initialise_database():
    connect()


def initialise_handlers(app):
    ScoreBoardHandler().register(app)

if __name__ == "__main__":
    app = Flask(__name__)

    initialise_database()
    initialise_handlers(app)

    app.run()
