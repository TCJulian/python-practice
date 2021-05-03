"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.

Sample value of n is 5
Expected Result : 615
"""
while True:
    try:
        value = input("Enter a whole number: ")
        n = int(value)
        nn = int(value*2)
        nnn = int(value*3)
        print(n + nn + nnn)
        break
    except ValueError:
        print("Entered value was not whole number. Try again.")
