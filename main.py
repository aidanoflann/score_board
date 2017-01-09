from flask import Flask

from scoreboard.handler import ScoreBoardHandler

app = Flask(__name__)

ScoreBoardHandler().register(app)

if __name__ == "__main__":
    app.run()