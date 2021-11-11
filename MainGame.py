from Live import player_name, welcome, load_game
from GuessGame import *
from MemoryGame import *

welcome(player_name())
game = load_game()
if game.game_type == "1":
    MemoryGame(game.game_type, game.difficulty).play(int(game.difficulty))
elif game.game_type == "2":
    GuessGame(game.game_type, game.difficulty).play(int(game.difficulty))
# elif game.game_type == "3":
#     play3(int(game.difficulty))

