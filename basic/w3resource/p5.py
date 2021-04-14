"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program which accepts the user's first and last name and print
them in reverse order with a space between them.
"""

def main():
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    print(f"Hello {last} {first}. I have reversed your name!")

if __name__ == "__main__":
    main()
