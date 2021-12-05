import os
import platform

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


def screen_cleaner():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("/usr/bin/osascript -e")
    else:
        print("\n" * 1000)
