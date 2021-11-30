import random
import time
from GameClass import Game
from currency_converter import CurrencyConverter, SINGLE_DAY_ECB_URL

random_num = 0
interval_low = 0
interval_high = 0


class CurrencyRouletteGame(Game):
    def play(self, difficulty):
        get_money_interval(difficulty)
        guess = get_guess_from_user()
        if interval_low < guess < interval_high:
            is_won = True
        else:
            is_won = False
        return is_won


def get_money_interval(difficulty):
    global interval_low, interval_high, random_num
    c = CurrencyConverter(SINGLE_DAY_ECB_URL)
    random_num = random.randint(1, 101)
    converted_value = c.convert(random_num, 'USD', 'ILS')
    interval_low = converted_value - (5 - difficulty)
    interval_high = converted_value + (5 - difficulty)
    return interval_low, interval_high, random_num


def get_guess_from_user():
    is_answer_correct = False
    while not is_answer_correct:
        try:
            guess = input(f"Welcome to Currency Roulette game.\n"
                          f"Please write, what will be the amount of converted currency in ILS, if we convert "
                          f"{random_num}$ to ILS?\n")
            if guess.isnumeric():
                is_answer_correct = True
                return int(guess)
            else:
                print(f"\nPlease try again, make sure to use numbers only.\n")
                time.sleep(2)
                is_answer_correct = False
        except ValueError:
            print(f"\nPlease try again, make sure to use numbers only.\n")
            time.sleep(2)


kj = 1
