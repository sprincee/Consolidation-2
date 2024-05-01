#Title: Word Guessing Game or 'Eldrow'

'''

Coding-Outline:



Summary: 
- A word guessing game; pretty simple.

Object:
- To guess a secret word from a bank of words.

Parameters:
- Each turn, the player can guess a letter, or the whole word.
- At the beginning of the game, there'll be a theme, which can be chosen.
- After guessing a letter, the game will let the player know how many occurances of that letter are in the word.
- If the player is right, the letter & position of the letter will show. (Taking inspiration from Wordle)
- The player only has three 'word' guesses.
- A player's final score is how many turns it took to find the word.

Notes:
- Taking inspiration from NYT's Wordle; I'll allow only one player.

Functions/Structural Elements:
- A list of themes, which can be chosen. --> (Fruits, Animals, Colors)
- A list of words, which correspond to a theme. --> (TBD)
- A function to randomly choose words, probably using import random.
- A function to check if the letter guessed is within the secret word.



A note for grading:
- I used this as an initial commit; also as a way to organize my thoughts.
- It's not all encompassing & things are probably going to change during dev cycle.
- It's just a way to get my ideas on paper (or screen, in this case).


'''

#Imports
import random
import time
import os

#Custom-Imports (coded by Mahad)
import game_v2



#Establishing a bank of themes for the game
theme_bank = ["Fruits", "Animals", "Colors"]

#Establishing banks for each theme
fruit_bank = ["apple", "banana", "orange", "grape", "strawberry"]
animal_bank = ["lion", "giraffe", "bison", "tiger", "elephant"]
color_bank = ["white", "black", "red", "blue", "yellow"]


#Default Start
username = game_v2.start()

#A function to select a theme
def choose_theme():
  print(f"{username}, here are the available themes:\n")
    time.sleep(1)
    for n, theme in enumerate(theme_bank, start= 1):
        print(f"{n}. {theme}")
    while True:
        try:
            choice = int(input("\nChoose a theme: "))
            if 1 <= choice <= len(theme_bank):
                return choice
            else:
                print("Invalid choice. Enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Enter a number.")


#A function to choose a word from a selected theme
def choose_words(theme_choice):
    if theme_choice == 1:
        #print('Testing a test-case.') #Testcase #1
        return random.choice(fruit_bank)
    if theme_choice == 2:
        #print('Testing a test-case again.') #Testcase #2
        return random.choice(animal_bank)
    if theme_choice == 3:
        return random.choice(color_bank)

    return theme_choice   
    
    
    
    
    
    
#Function-Caller:
chosen_theme = choose_theme()
time.sleep(1)
os.system("cls")
chosen_word = choose_words(chosen_theme)


