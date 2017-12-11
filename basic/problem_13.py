# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#
# Objectives:
# 1. Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#
# ------------------------------------------------------------------- 

def main():
    while True:
        try:
            length = int(input("Give me a number for the length of your Fibonacci sequence:\n"))
            break
        except ValueError:
            print("Length must be an integer. Please try again.\n")
    print(fib_seq(length))

def fib_seq(length):
    seq = []
    while True:
        try:
            if length <= 0:
                return seq
            elif length == 1:
                seq = [1]
                return seq
            elif length == 2:
                seq = [1, 1]
                return seq
            elif length > 2:
                seq = [1, 1]
                for element in range(2, length):
                    seq.append(seq[-1] + seq[-2])
                return seq
        except ValueError:
            print("Length must be an integer. Please try again.")

if __name__ == "__main__":
    main()
