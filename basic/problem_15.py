# -------------------------------------------------------------------
#
# Excercise from: http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
#
# Objectives:
# 1. Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
#
# -------------------------------------------------------------------

def main():
    text = input("Please provide a sentence to reverse:\n")
    text_list = text.split()
    text_list.reverse()
    new_list = " ".join(text_list)
    print(new_list)

if __name__ == '__main__':
    main()
