# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
#
# Initial Conditions:
#   x = [5, 10, 15, 20, 25]
#
# Objectives:
# 1. Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
#
# ------------------------------------------------------------------- 

def main():
    x = [5, 10, 15, 20, 25]
    print(first_last(x))

def first_last(obj):
    return [obj[0], obj[-1]]

if __name__ == "__main__":
    main()
