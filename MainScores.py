from flask import Flask
from Utils import player_name_file
import Score


def score_server():
    app = Flask(__name__)
    with open(player_name_file, "r") as pnf:
        player_name = pnf.read()

    @app.route('/')
    def index():
        return f"<html><head><title>Game scores</title></head><body><h1>Hi {player_name}," \
               f"The score is <div id='score'>" \
               f"{Score.points_of_winning}</div></h1></body></html> "
    app.run(port=5001)
