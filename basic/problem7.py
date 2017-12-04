# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# 
# Initial Conditions:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# Objectives:
# 1. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
#
# ------------------------------------------------------------------- 

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even = [num] for num in a if num % 2 == 0]
    print(even)

if __name__ == "__main__":
    main()
