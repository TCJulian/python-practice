# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:53:06 2018

@author: Tyler
"""
max_odd = None
count = 0
while(count < 10):
    x = int(input("Give me an integer: "))
    if x%2 != 0:
        if not max_odd or x > max_odd:
            max_odd = x
    count += 1
    
if max_odd:
    print(max_odd)
else:
    print("All values are even.")