# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:22:36 2018

@author: Tyler
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
current_savings = 0.0
portion_down_payment = 0.25
monthly_salary = annual_salary/12

months = 0
r = 0.04
down_payment = portion_down_payment*total_cost
while current_savings < down_payment:
    months += 1
    current_savings += monthly_salary*portion_saved + current_savings*r/12
    if months > 1000:
        print("You wont' afford this home with your current salary and savings.")
        break
print("Number of months:", months)