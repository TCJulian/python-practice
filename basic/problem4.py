# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/solution/2014/03/05/04-divisors-solutions.html
#
# Objectives:
# 1. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#
# ------------------------------------------------------------------- 

def main():
    num = int(input("Give me a number:"))

    my_list = []
    for element in range(1, abs(num) + 1):
        if num % element == 0:
            container = [element, element * -1]
            my_list.extend(container)
    my_list.sort()
    print(my_list)

if __name__ == "__main__":
    main()
