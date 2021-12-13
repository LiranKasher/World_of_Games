from flask import Flask
import Score

app = Flask(__name__)


@app.route('/')
def index():
    return f"<html><head><title>Game scores</title></head><body><h1>The score is <div id='score'>" \
           f"{Score.points_of_winning}</div></h1></body></html> "


# app.run(port=5001, debug=True)
