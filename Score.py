from Utils import scores_file_name


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    with open(scores_file_name, "w+") as score:
        score.write(f"{points_of_winning}")
    return points_of_winning
