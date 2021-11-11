import random
from Game import Game


class GuessGame(Game):
    def play(self, difficulty):
        print(compare_results(generate_number(difficulty), int(get_guess_from_user(difficulty))))


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess = 0
    while not any([guess == "1", guess == "2", guess == "3", guess == "4", guess == "5"]):
        guess = input(f"Please enter your guess, a number between 1-{difficulty}\n")
    return guess


def compare_results(secret_number, guess):
    return secret_number == guess

Blabla
