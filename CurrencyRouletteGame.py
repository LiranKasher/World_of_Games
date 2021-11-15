import random
from GameClass import Game
from currency_converter import CurrencyConverter, SINGLE_DAY_ECB_URL


class CurrencyRouletteGame(Game):
    def play(self, difficulty):
        interval_low, interval_high, random_num = get_money_interval(difficulty)
        user_guess = get_guess_from_user(difficulty)
        if interval_low < int(user_guess) < interval_high:
            is_won = True
        else:
            is_won = False
        print(is_won)
        return is_won


def get_money_interval(difficulty):
    c = CurrencyConverter(SINGLE_DAY_ECB_URL)
    random_num = random.randint(1, 100)
    convert_value = c.convert(random_num, 'USD', 'ILS')
    interval_low = convert_value - (5 - difficulty)
    interval_high = convert_value + (5 - difficulty)
    return interval_low, interval_high, random_num


def get_guess_from_user(difficulty):
    interval_low, interval_high, random_num = get_money_interval(difficulty)
    user_guess = int(input(f"Welcome to Currency Roulette game.\n"
                           f"Please write, what will be the amount of converted currency in ILS, if we convert "
                           f"{random_num}$ to ILS?\n"))
    return user_guess
