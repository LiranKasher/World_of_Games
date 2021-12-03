from Class import Game
import random
import time


class GuessGame(Game):
    def play(self, difficulty):
        return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    is_answer_correct = False
    while not is_answer_correct:
        try:
            guess = input(f"Please enter your guess, a number between 1-{difficulty}:\n")
            if guess.isnumeric():
                if 0 < int(guess) <= difficulty:
                    is_answer_correct = True
                    return int(guess)
                else:
                    print(f"\nPlease try again, make sure to use a number between 1-{difficulty}.\n")
                    time.sleep(2)
            else:
                print(f"\nPlease try again, make sure to use numbers only.\n")
                time.sleep(2)
                is_answer_correct = False
        except ValueError:
            print(f"\nPlease try again, make sure to use numbers only.\n")
            time.sleep(2)


def compare_results(secret_number, guess):
    return secret_number == guess
