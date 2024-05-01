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