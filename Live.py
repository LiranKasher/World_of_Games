from Class import Game
import time
import os

current_name = ""
game_type = 0
difficulty = 0


def player_name():
    global current_name
    while True:
        current_name = input(f"\nPlease enter your first name:\n")
        if not current_name.isalpha():
            print(f"Please use only letters A-Z, capital or non capital.")
            time.sleep(1)
        else:
            break
    return current_name


def welcome(name):
    print(f"\nHello {name} and welcome to World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    global game_type
    global difficulty
    while True:
        try:
            os.system('clear')
            game_type = int(input(f"Please choose a game to play:\n"
                                  f"1. Memory Game - a sequence of numbers will appear for 1 second, and you have to "
                                  f"guess it back.\n"
                                  f"2. Guess Game - guess a number and see if you chose like the computer.\n"
                                  f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")
                            )
            if game_type in range(1, 4):
                break
            else:
                print(f"Oops, it seems like you hit the wrong number, please try again using numbers between 1-3.\n")
                time.sleep(2)
        except ValueError:
            print(f"Please use only numbers between 1-3.\n")
            time.sleep(2)
    while True:
        try:
            os.system('clear')
            difficulty = int(input(f"Please choose game difficulty from 1 to 5:\n"))
            if difficulty in range(1, 6):
                break
            else:
                print(f"Oops, it seems like you hit the wrong number, please try again using numbers between 1-5.\n")
                time.sleep(2)
        except ValueError:
            print(f"Please use only numbers between 1-5.\n")
            time.sleep(2)
    return Game(game_type, difficulty)
