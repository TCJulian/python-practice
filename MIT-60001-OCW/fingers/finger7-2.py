# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:49:53 2019

@author: Tyler
"""

def findAnEven(l):
    """Assumes l is a list of integers
       Returns the first even number in l
       Raises ValueError if l does not contain an even number"""
    for item in l:
        if item%2 == 0:
            return item
    raise ValueError

l1 = [1, 3, 4, 5, 8]    
l2 = [1, 3, 5]

print(findAnEven(l1))
print(findAnEven(l2))