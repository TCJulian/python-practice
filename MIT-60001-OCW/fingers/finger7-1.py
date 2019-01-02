# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:47:48 2019

@author: Tyler
"""

def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
           For example, if s is 'a2b3c' it returns 5"""
    sum = 0
    for c in s:
        try:    
            sum += int(c)
        except ValueError:
            continue
    return sum
        
print(sumDigits('ab1c2'))