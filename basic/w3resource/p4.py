"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program which accepts the radius of a circle from the user and
compute the area.

Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
from math import pi

def main():
    try:
        r = float(input("Enter the radius of your circle: "))
        print(f"r = {r}")
        print(f"Area =  {pi * r**2}")
    except ValueError:
        print("ERROR: Input must be a number.")

if __name__ == "__main__":
    main()
