# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#
# Objectives:
# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 2. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 3. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
#
# -------------------------------------------------------------------

from datetime import datetime

def main():
    name = get_name()
    age = get_age()
    count = get_message_count()

    answer(name, age, count)

def get_name():
    name = str(input('Welcome! What is your first name? '))
    return name

def get_age():
    while True:
        try:
            age = -1
            while age < 0:
                age = int(input('How old are you? '))
                return age
        except ValueError:
            print("That is not a valid number. Try again.")

def get_message_count():
    while True:
        try:
            count = int(input('Number of messages: '))
            return count
        except ValueError:
            print("That is not a valid number. Try again.")

def answer(name, age, count):
    age_difference = 100 - age
    current = datetime.now()
    answer = current.year + age_difference

    for i in range(count):
        print('{}, you will be 100 years old in the year {}.'.format(name, answer))

if __name__ == '__main__':
    main()
