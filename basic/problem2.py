def main():
    number = get_number()
    odd_or_even(number)
    multiple(number, 4)

    print("\n")

    mult_check()

def get_number():
    num = int(input("Give me a number:\n"))
    return num

def mult_check():
    num = int(input("Give me a number to check:\n"))
    check = int(input("Give me a number to divide:\n"))
    if num % check == 0:
        print("{} divides evenly into {}".format(check, num))
    else:
        print("{} divided by {} leaves a remainder of {}".format(num, check, num % check))

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
