from Live import *
from Utils import screen_cleaner
from GuessGame import *
from MemoryGame import *
from CurrencyRouletteGame import *
import time


def play_game():
    game_on = True
    just_played = False
    screen_cleaner()
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
        while True:
            screen_cleaner()
            answer = input(f"Would you like to play again (answer with 'yes' or 'no')?\n")
            if answer not in ["yes", "no"]:
                print(f"Please try again, use only 'yes' or 'no'.")
                time.sleep(2)
            else:
                break
        if answer == "no":
            break
        else:
            just_played = True


play_game()
