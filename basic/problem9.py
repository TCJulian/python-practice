# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#
# Objectives:
# 1. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# 2. Keep the game going until the user types “exit”
# 3. Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# ------------------------------------------------------------------- 

import random

def main():
    while True:
        magic_number = random.randint(1, 9)
        reply = input("I am thinking of a number between 1 and 9. What is it?\n")

        if number_logic(reply, magic_number) == False:
            exit()

def number_logic(reply, magic_number):
    guesses = 0
    while True:
        try:
            if reply == 'exit':
                exit()
            elif int(reply) < magic_number:
                reply = input("That number is too low. Try again!\n")
                guesses += 1
            elif int(reply) > magic_number:
                reply = input("That number is too high. Try again!\n")
                guesses += 1
            elif int(reply) == magic_number:
                guesses += 1
                print("{} is the correct number. It took you {} guesses to get it right!\n".format(reply, guesses))
                repeat = input("Would you like to play again?\n")
                if repeat.lower() == ("y" or "yes"):
                    return True
                else:
                    return False
        except ValueError:
            reply = input('Input must be number. Type "exit" to quit.')

if __name__ == "__main__":
    main()
