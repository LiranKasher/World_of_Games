from flask import Flask
from Utils import player_name_file
import Score


def score_server():
    app = Flask(__name__)
    with open(player_name_file, "r") as pnf:
        player_name = pnf.read()

    @app.route('/')
    def index():
        try:
            return f"<html><head><title>Game scores</title></head><body><h1> Hi {player_name}, your score is: " \
                   f"<div id='score'>{Score.points_of_winning}</div></h1></body></html> "
        except OSError:
            return f"<html><head><title>Scores Game</title></head><body><body><h1><div id='score' style='color:red'>" \
                   f"{ERROR}</div></h1></body></html>"
    app.run(port=5001)
