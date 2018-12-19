# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:22:29 2018

@author: Tyler
"""

num = int(input("Give an integer: "))

pwr = 1

while pwr < 6:
    root = 0
    while root**pwr < num:
        root += 1
    if root**pwr == num:
        break
    pwr += 1

if pwr >= 6:
    print("No pair exists")
else:
    print(root, pwr)