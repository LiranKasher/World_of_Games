from flask import Flask
import Score
from Live import current_name


def score_server():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return f"<html><head><title>Game scores</title></head><body><h1>Hi {current_name}," \
               f"The score is <div id='score'>" \
               f"{Score.points_of_winning}</div></h1></body></html> "
    app.run(port=5001)
