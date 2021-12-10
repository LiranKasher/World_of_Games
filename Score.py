import numpy as np
from Utils import score_file_name


def add_score(difficulty):
    latest_points_of_winning = (difficulty * 3) + 5
    with open(score_file_name, "r+") as score:
        previous_points_of_winning = np.genfromtxt(score_file_name, dtype=int)
        points_of_winning = previous_points_of_winning + latest_points_of_winning
        score.write(f"{points_of_winning}")
    return points_of_winning


def score_file_cleaner():
    with open(score_file_name, "w") as score:
        score.write(f"0")
