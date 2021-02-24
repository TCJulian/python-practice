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
    each digit in "answer". Both inputs must be strings.

    Returns a tuple with the number of correctly guessed integers in the
    right place (cows), and the number of correctly guessed integers in the
     wrong place (bulls).
    """
    cows = 0
    bulls = 0
    for pos, char in enumerate(guess):
        if char == answer[pos]:
            cows += 1
        elif char in answer:
            bulls += 1
    return (cows, bulls)

def play_CowsAndBulls():
    # TODO:
    # Generate random number
    answer = str(random.randint(1000, 9999))
    # Track number of guesses
    guesses = 0
    # Intro text
    print("Welcome to the Cows and Bulls Game!")
    print("Enter a number:")
    # Start game loop and Collect user guess
    while True:
        guess = input()
        # Validate if guess is correct and print result.
        result = check_guess(guess, answer)
        print(f"{result[0]} cow(s), {result[1]} bull(s)")
        # If wrong, increase guess count by one and repeat loop
        # If right, increase guess by one and exit loop
        guesses += 1
        if result[0] == 4:
            break
    # Congradulate user, show score, and end game
    print(f"You have found the correct number in {guesses} guesses! It was {answer}.")

if __name__ == "__main__":
    play_CowsAndBulls()
