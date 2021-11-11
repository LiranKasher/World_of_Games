from Game import Game

from random import randrange

import time


class MemoryGame(Game):
    # def __init__(self, game_type, difficulty):
    #     super().__init__(game_type, difficulty)
    #     self.game_type = game_type
    #     self.difficulty = difficulty
    def play(self, difficulty):
        generate_sequence(difficulty)


def generate_sequence(difficulty):
    print("\n" * 1000)
    random_num = []
    for i in range(1, difficulty + 1):
        random_num.append(randrange(1, 102))
    print(*random_num, sep=', ')
    time.sleep(0.7)
    print("\n" * 1000)
    return random_num


def get_list_from_user(difficulty):
    user_num_list = []
    for i in range(1, difficulty + 1):
        user_num = input(f"Please enter one number you remember and press 'Enter'")
        user_num_list.append(user_num)
    return user_num_list
