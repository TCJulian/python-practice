# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:20:19 2018

@author: Tyler
"""

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x%2 != 0:
    if not max_odd or x > max_odd:
        max_odd = x
        
if y%2 != 0:
    if not max_odd or y > max_odd:
        max_odd = y
        
if z%2 != 0:
    if not max_odd or z > max_odd:
        max_odd = z
        
if max_odd:
    print(max_odd)
else:
    print("All values are even.")
