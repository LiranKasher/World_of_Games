from Class import Game
from Utils import scores_file_name


class Score(Game):
    def add_score(self, difficulty):
        points_of_winning = (difficulty * 3) + 5
        with open(scores_file_name, "w+") as score:
            score.write(f"{points_of_winning}")
