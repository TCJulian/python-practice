# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#
# Objectives:
# 1. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# 2. If the number is a multiple of 4, print out a different message.
# 3. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.#
#
# -------------------------------------------------------------------

def main():
    number = get_number()
    odd_or_even(number)
    multiple(number, 4)

    print("\n")

    mult_check()

def get_number():
    while True:
        try:
            num = int(input("Give me a number:\n"))
            return num
        except ValueError:
            pass

def mult_check():
    while True:
        try:
            num = int(input("Give me a number to check:\n"))
            check = int(input("Give me a number to divide:\n"))
            if num % check == 0:
                print("{} divides evenly into {}".format(check, num))
            else:
                print("{} divided by {} leaves a remainder of {}".format(num, check, num % check))
            break
        except ValueError:
            pass

def odd_or_even(num):
    if num == 0:
        print("The number is zero")
    elif num % 2 == 0:
        print("{} is even".format(num))
    elif num % 2 != 0:
        print("{} is odd".format(num))

def multiple(num, mult):
    if num % mult == 0:
        print("{} is a multiple of {}".format(num, mult))
    else:
        print("{} is not multiple of {}".format(num, mult))

if __name__ == "__main__":
    main()
