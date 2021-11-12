from Game import Game

current_name = ""
game_type = 0
difficulty = 0


def player_name():
    global current_name
    current_name = input(f"Please enter your first name: \n")
    return current_name


def welcome(name):
    print(f"Hello {name} and welcome to World of Games (WoG). \nHere you can find many cool games to play. \n")


def load_game():
    global game_type
    global difficulty
    while not any([game_type == "1", game_type == "2", game_type == "3"]):
        game_type = input(f"Please choose a game to play: \n"
                          f"1. Memory Game - a sequence of numbers will appear for 1 second, and you have to "
                          f"guess it back. \n"
                          f"2. Guess Game - guess a number and see if you chose like the computer. \n"
                          f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS. \n")
    while not any([difficulty == "1", difficulty == "2", difficulty == "3", difficulty == "4", difficulty == "5"]):
        difficulty = input(f"Please choose game difficulty from 1 to 5:\n")
    return Game(game_type, difficulty)


