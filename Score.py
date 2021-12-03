from Class import Game
from Utils import SCORES_FILE_NAME


class Score(Game):
    def add_score(self, difficulty):
        with open(SCORES_FILE_NAME, "w+") as score:
            score.write("pass")
