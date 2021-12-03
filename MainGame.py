from Live import player_name, welcome, load_game
from GuessGame import *
from MemoryGame import *
from CurrencyRouletteGame import *
import time
import os


def play_game():
    game_on = True
    answer = ""
    just_played = False
    while game_on:
        if not just_played:
            welcome(player_name())
        game = load_game()
        if game.game_type == 1:
            MemoryGame(game.game_type, game.difficulty).play(game.difficulty)
        elif game.game_type == 2:
            GuessGame(game.game_type, game.difficulty).play(game.difficulty)
        elif game.game_type == 3:
            CurrencyRouletteGame(game.game_type, game.difficulty).play(game.difficulty)
        os.system('clear')
        print(f"answer = {answer}")
        while True:
            answer = input(f"\nWould you like to play again (please answer with 'yes' or 'no')?\n")
            if answer not in ["yes", "no"]:
                print(f"answer in if = {answer}")
                print(f"\nPlease try again, use only 'yes' or 'no'.")
                time.sleep(2)
            else:
                print(f"answer in else = {answer}")
                break
        print(f"answer after while = {answer}")
        if answer == "no":
            break
        else:
            just_played = True


play_game()
