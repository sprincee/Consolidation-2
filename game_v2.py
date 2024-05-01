#game_v2

import os
import time


def display_rules():
    print("\nRules:")
    print("Simply put, to play, you'll choose a theme.\nFollowing that, a secret word will be chosen from a bank of words.\nIt's up to you to guess the word in one go, or gradually narrow it down after guessing letters!")
    time.sleep(2)

def start():
    username = str(input("Enter a username: "))
    os.system('cls')
    time.sleep(0.5)
    print(f"Welcome, {username}, to Eldrow!")
    time.sleep(1)
    while True:
        try:
            user_exp = input("\nWe're glad you're here! Would you like to hear the rules? (Y/N): ").upper()
            if user_exp not in ("Y", "N"):
                raise ValueError("Please, input only 'Y' or 'N'.")
            break
        except ValueError as e:
            print(e)

    if user_exp.upper() == "N":
        os.system('cls')
        print("Well, well, well. . .")
        time.sleep(2)
        print("Someone's smart, huh? We'll see how you feel after this game.")
        time.sleep(3)
        os.system('cls')
    else:
        display_rules()
        input("\nPress Enter to continue...")
        os.system('cls')

    return username
