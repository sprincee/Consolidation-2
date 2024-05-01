#Title: Word Guessing Game or 'Eldrow'

#Imports
import random
import time
import os

#Custom-Imports (coded by Mahad-- reused from Consolidation 1/Ethics Game!
import game_v2

#Establishing a bank of themes for the game
theme_bank = ["Fruits", "Animals", "Colors"]

#Establishing banks for each theme
fruit_bank = ["strawberry", "apple", "orange", "grape", "banana"]
animal_bank = ["lion", "giraffe", "bison", "tiger", "elephant"]
color_bank = ["white", "black", "red", "blue", "yellow"]

#Default Start
username = game_v2.start()


def choose_theme():
    '''

    A function to select the theme.

    Arguements:
        - None.
    
    '''
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

def choose_words(theme_choice):
    '''
    
    A function to choose a word from a selected theme.

    Arguements:
        - theme_choice (int): the numerical repersentation of each theme.
    
    '''
    if theme_choice == 1:
        return random.choice(fruit_bank)
    if theme_choice == 2:
        return random.choice(animal_bank)
    if theme_choice == 3:
        return random.choice(color_bank)


def check_letter(word, letter):
    '''
    
    A function used to return the count of a certain letter within the chosen word.

    Arguements:
        - word (str): The string which is being counted from.
        - letter (str): The character whose occurances are being counted. 
    
    '''
    return word.count(letter)



def game_begin(theme_choice, chosen_word):
    '''

    A function for starting the game with the specified theme and chosen word.

    Arguements:
        - theme_choice (str): the theme chosen for the game.
        - chosen_word (str): the word chosen for the game.

    
    '''
    guessed_word = ['_'] * len(chosen_word) #Formatting
    guessed_letters = set()

    #Initializing player's guesses to 0
    letter_guesses = 0
    word_guesses = 0

   
    #Implementation of Primary Game-Logic
    while '_' in guessed_word and word_guesses < 3:
        print("Secret Word:", " ".join(guessed_word))
        print("Guessed Letters:", ", ".join(guessed_letters))

        guess = input("\nGuess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
                time.sleep(2)
                os.system('cls')
            else:
                guessed_letters.add(guess)
                occurences = check_letter(chosen_word, guess)
                if occurences:
                    print(f"There are {occurences} occurrence(s) of the letter '{guess}' in the word.")
                    time.sleep(2)
                    os.system('cls')
                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guess:
                            guessed_word[i] = guess
                else:
                    print(f"The letter '{guess}' is not in the word.")
                    time.sleep(2)
                    os.system('cls')
                letter_guesses += 1
        elif guess == chosen_word and guess.isalpha():
            time.sleep(1)
            os.system('cls')
            time.sleep(1)
            print("Congratulations! You guessed the word correctly.")
            break
        elif len(guess) != len(chosen_word) and guess != chosen_word and guess.isalpha():
            print("\nIncorrect guess.")
            time.sleep(1)
            os.system('cls')
            word_guesses += 1
            if word_guesses == 3:
                print("You've used all your word guesses. Game over!")
                time.sleep(2)
                os.system('cls')
                break
        elif len(guess) == len(chosen_word) and guess != chosen_word and guess.isalpha():
            print("\nIncorrect guess.")
            time.sleep(1)
            os.system('cls')
            word_guesses += 1
            if word_guesses == 3:
                print("You've used all your word guesses. Game over!")
                time.sleep(2)
                os.system('cls')
                break
        elif guess.isdigit():
            print("Invalid input. Please enter a single letter or a word-guess.")
            time.sleep(1)
            os.system('cls')
        elif len(guess) == 0:
            print("Invalid input. Please enter a single letter or a word-guess.")
            time.sleep(1)
            os.system('cls')

    print(f"\nThe secret word was: {chosen_word}")
    print(f"Number of letter guesses: {letter_guesses}")
    print(f"Number of word guesses: {word_guesses}")
    time.sleep(5)
    os.system('cls')

#Function-Caller:
chosen_theme = choose_theme()
time.sleep(1)
os.system("cls")
chosen_word = choose_words(chosen_theme)
time.sleep(1)
game_begin(chosen_theme, chosen_word)
game_v2.credits(username)

# PROJECT by MAHAD KHAN from KHAN STUDIOS
