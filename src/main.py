import time

from flask import Flask

from database.storagelayer import connect
from scoreboard.handler import ScoreBoardHandler
from sql_wrapper.handler import SQLWrapperHandler

import settings


def initialise_database():
    connect()


def initialise_handlers(app):
    ScoreBoardHandler().register(app)
    SQLWrapperHandler().register(app)

if __name__ == "__main__":
    print("Waiting twenty seconds for the lulz.")
    time.sleep(settings.STARTUP_WAIT)  # This is really dumb
    app = Flask(__name__)

    initialise_database()
    initialise_handlers(app)

    app.run(host="0.0.0.0", port=80)
