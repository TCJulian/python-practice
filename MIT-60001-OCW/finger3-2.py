# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:47:46 2018

@author: Tyler
"""

s = "1.23,2.4,3.123"

total = 0
num = ""
for c in s:
    if c != ",":
        num += c
    else:
        total += float(num)
        num = ""

if len(num) > 0:
    total += float(num)
print(total)       
    