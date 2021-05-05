"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program to print the documents (syntax, description etc.) of
Python built-in function(s).

Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
from inspect import getargspec

func = abs
print(f"{func.__name__}()")
print(func.__doc__)
