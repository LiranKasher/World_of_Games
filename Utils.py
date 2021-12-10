import os
import platform

score_file_name = "Scores.txt"
bad_return_code = 1


def screen_cleaner():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("/usr/bin/osascript -e")
    else:
        print("\n" * 1000)
