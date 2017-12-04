# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/solution/2014/03/05/04-divisors-solutions.html
#
# Objectives:
# 1. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#
# ------------------------------------------------------------------- 

def main():
    x = get_string()
    x_rev = reverse_slow(x)

    if x == x_rev:
        print("This word is a palindrome.")
    else:
        print("This word is not a palindrome: {}, {}.".format(repr(x), repr(x_rev)))

def get_string():
    return str(input("Give me a word: \n"))

def reverse_fast(word):
    return a_string[::-1]

def reverse_slow(word):
    new_word = ""
    for i in range(1, len(word) + 1):
        new_word = new_word + word[i * -1]
    return new_word

if __name__ == "__main__":
    main()
