from GameClass import Game
from random import randrange
import time


class MemoryGame(Game):
    def play(self, difficulty):
        print(is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty)))


def generate_sequence(difficulty):
    print("\n" * 1000)
    random_num_list = []
    for i in range(1, difficulty + 1):
        random_num_list.append(randrange(1, 102))
    print(*random_num_list, sep=', ')
    time.sleep(0.7)
    print("\n" * 1000)
    return random_num_list


def get_list_from_user(difficulty):
    while True:
        user_num_list = []
        for i in range(1, difficulty + 1):
            user_num = input(f"Please enter a number you remember, and press 'Enter':\n")
            if type(user_num) != int:
                print(f"\nPlease try again, make sure to use numbers only.\n")
                time.sleep(2)
                break
            else:
                user_num_list.append(user_num)
        return user_num_list


def is_list_equal(random_num_list, user_num_list):
    is_equal = random_num_list == user_num_list
    return is_equal
