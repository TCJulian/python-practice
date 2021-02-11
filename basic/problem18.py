# -------------------------------------------------------------------
#
# Exercise from: http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
#
# Objective:
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#  - Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
#  - For every digit that the user guessed correctly in the correct place, they have a “cow”. 
#  - For every digit the user guessed correctly in the wrong place is a “bull.” 
#  - Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
#  - Once the user guesses the correct number, the game is over. 
#  - Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#
# -------------------------------------------------------------------
import random

def check_guess(guess, answer):
    """
    Takes an integer "guess" and compares its digit placement and value against
    each digit in "answer". Both inputs must be integers.

    Returns a tuple with the number of correctly guessed integers in the 
    right place (cows), and the number of correctly guessed in the wrong place 
    (bulls).
    """

def play_CowsAndBulls():
    # TODO:

if __name__ == "__main__":
play_CowsAndBulls()