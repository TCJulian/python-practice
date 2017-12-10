# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#
# Objectives:
# 1. Ask the user for a number and determine whether the number is prime or not.
#
# ------------------------------------------------------------------- 

def main():
    number = ask_number()
    is_prime(number)

def ask_number():
    while True:
        try:
            return int(input("Give me a number:\n"))
        except ValueError:
            print("That is not a number. Please try again.")

def is_prime(number):
    if number == (0 or 1):
        print(str(number) + " is not a prime number.")
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            print(str(number) + " is not a prime number.")
            return False
        else:
            continue
    print(str(number) + " is a prime number.")
    return True

if __name__ == "__main__":
    main()
