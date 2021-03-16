"""
Exercise from:
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program to display the current date and time.

Sample Output :
    Current date and time :
    2014-07-05 14:34:14
"""
from datetime import datetime

print('Current date and time:')
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
