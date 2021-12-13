from Live import player_name, welcome, load_game
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Utils import screen_cleaner
from Score import add_score, score_file_cleaner
from MainScores import app
import time


def play_game():
    just_played = False
    is_won = False
    screen_cleaner()
    while True:
        if not just_played:
            score_file_cleaner()
            welcome(player_name())
        game = load_game()
        if game.game_type == 1:
            is_won = MemoryGame(game.game_type, game.difficulty).play(game.difficulty)
        elif game.game_type == 2:
            is_won = GuessGame(game.game_type, game.difficulty).play(game.difficulty)
        elif game.game_type == 3:
            is_won = CurrencyRouletteGame(game.game_type, game.difficulty).play(game.difficulty)
        if is_won:
            add_score(game.difficulty)
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
    app.run(port=5001)


play_game()
