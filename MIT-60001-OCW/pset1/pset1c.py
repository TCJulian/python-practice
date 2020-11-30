# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:22:36 2018

@author: Tyler
"""
salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = 0.25
down_payment = portion_down_payment*total_cost
r = 0.04

high = 10000
low = 0
portion_saved = (high+low)//2
alpha = 100
steps = 0

while True:
    steps += 1
    current_savings = 0.0
    annual_salary = salary
    monthly_salary = annual_salary/12
    saving_rate = portion_saved/10000

    for month in range(1, 37):
        current_savings += monthly_salary*saving_rate + current_savings*r/12
        if month%6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
    if portion_saved == low or portion_saved == high:
        print("It is not possible to pay down the payment in three years.")
        break
    elif current_savings < down_payment-alpha:
        low = portion_saved
        portion_saved = (high+low)//2
    elif current_savings > down_payment+alpha:
        high = portion_saved
        portion_saved = (high+low)//2
    else:
        print("Best savings rate:", portion_saved/10000)
        print("Steps in bisection search:", steps)
        break
    if steps > 1000:
        print("RUNTIME ERROR")
        break
