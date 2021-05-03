"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program to accept a filename from the user and print the
extension of that.

Sample filename : abc.java
Output : java
"""
filename = input('Enter your file name: ')
period = filename.rfind(".")
if period != -1:
    print(filename[period+1:])
else:
    print("Not a valid filename. Please try again.")
