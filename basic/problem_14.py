# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
#
# Objectives:
# 1. Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# 2. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#
# ------------------------------------------------------------------- 

def combine_lists(list_1, list_2):
    new = set(list_1 + list_2)
    new = list(new)
    return new

def remove_dupes(x):
    new = []
    for i in x:
        if i in new:
            continue
        else:
            new.append(i)
    return new

def main():
    list_1 = [1, 4, 6, 8, 9, 9, 11, 11]
    list_2 = [3, 6, 7, 9]

    print(list_1)
    print(list_2, end="\n\n")

    print("Removed dupes of list_1:")
    print(remove_dupes(list_1), end="\n\n")

    print("Combined list_1 and list_2:")
    print(combine_lists(list_1, list_2))

if __name__ == "__main__":
    main()
