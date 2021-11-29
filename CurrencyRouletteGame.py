import random
import time
from GameClass import Game
from currency_converter import CurrencyConverter, SINGLE_DAY_ECB_URL

random_num = 0
interval_low = 0
interval_high = 0


class CurrencyRouletteGame(Game):
    def play(self, difficulty):
        guess = get_guess_from_user(difficulty)
        if interval_low < guess < interval_high:
            is_won = True
        else:
            is_won = False
        print(is_won)
        return is_won


def get_money_interval(difficulty):
    global interval_low, interval_high, random_num
    c = CurrencyConverter(SINGLE_DAY_ECB_URL)
    get_money_interval.random_num = random.randint(1, 100)
    random_num = random.randint(1, 100)
    convert_value = c.convert(get_money_interval.random_num, 'USD', 'ILS')
    interval_low = convert_value - (5 - difficulty)
    interval_high = convert_value + (5 - difficulty)
    print(f"rnd = {get_money_interval.random_num}, con = {convert_value}")
    return interval_low, interval_high, random_num


def get_guess_from_user(difficulty):
    global random_num
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
