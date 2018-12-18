# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:07:09 2018

@author: Tyler
"""

def isIn(string1, string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False
    
print(isIn("hello", "el"))