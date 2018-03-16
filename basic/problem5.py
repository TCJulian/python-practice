# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#
# Objectives:
# 1. Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure # your program works on two lists of different sizes.
# 2. Randomly generate two lists to test this
# 3. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#
# ------------------------------------------------------------------- 

from random import randint

def main():
    x, y = rand_list(0, 10, 20), rand_list(0, 10, 20)
    z = compare_lists(x, y)
    print(z)

def rand_list(min_value, max_value, max_elements):
    my_list = []
    size = randint(0, max_elements)
    for element in range(size):
        my_list.append(randint(min_value, max_value))
    return my_list

def compare_lists(x, y):
    return list({element for element in x if element in y})

if __name__ == "__main__":
    main()
