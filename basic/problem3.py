# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#
# Initial Conditions:
#   x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# Objectives:
# 1. Take the list and write a program that prints out all the elements of the list that are less than 5.
# 2. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 3. Write this in one line of Python.
# 4. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.#
#
# -------------------------------------------------------------------

def main():
    x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    print("Print list objective")
    print_list(5, x)
    
    y = new_list(5, x)
    print("New List objective\n", y, "\n")

    print("One-line objective")
    one_line(5, x)
    
    z = input_list(x)
    print("Input List objective\n", z, "\n")

def print_list(num, x):
    for i in x:
        if i < num:
            print(i)

def new_list(num, x):
    y = []
    for i in x:
        if i < num:
            y.append(i)
    return y

def one_line(num, x):
    print([i for i in x if i < num])
    
def input_list(x):
    while True:
        y = []
        try:
            num = int(input("Give a number to sort by:\n"))
            for i in x:
                if i < num:
                    y.append(i)
            return y
        except ValueError:
            print("Input not a number.\n")

if __name__ == "__main__":
    main()
