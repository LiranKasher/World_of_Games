import numpy as np
from Utils import score_file_name

points_of_winning = 0


def add_score(difficulty):
    global points_of_winning
    latest_points_of_winning = (difficulty * 3) + 5
    previous_points_of_winning = np.genfromtxt(score_file_name, dtype=int)
    points_of_winning = previous_points_of_winning + latest_points_of_winning
    with open(score_file_name, "r+") as score:
        score.write(f"{points_of_winning}")
    return points_of_winning


def score_file_cleaner():
    with open(score_file_name, "w") as score:
        score.write(f"0")
