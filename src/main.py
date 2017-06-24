import time

from flask import Flask

from database.storagelayer import connect
from scoreboard.handler import ScoreBoardHandler
from sql_wrapper.handler import SQLWrapperHandler


def initialise_database():
    connect()


def initialise_handlers(app):
    ScoreBoardHandler().register(app)
    SQLWrapperHandler().register(app)

if __name__ == "__main__":
    time.sleep(20)  # This is really dumb
    app = Flask(__name__)

    initialise_database()
    initialise_handlers(app)

    app.run(host="0.0.0.0")
