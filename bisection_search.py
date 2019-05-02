#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:38:06 2018

@author: cypherman
"""

#bisection search implementation
#program to find the best savings rate for down payment on the house
#all values are static except salary

annual_salary = float(input("Enter the starting salary: "))
salary = annual_salary
down_payment = 250000
semi_annual_raise = 0.07
current_savings = 0
high = 10000
low = 0
res = (high + low) // 2
steps = 0
flag = False
#looking for a rate
while abs(current_savings - down_payment) >= 100:
    current_savings = 0
    annual_salary = salary
    for i in range(36):
        if i > 1 and i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        portion = annual_salary / 12 * res / 10000.0
        roi = current_savings * 0.04 / 12
        current_savings += portion + roi
    if current_savings > down_payment + 100:
        high = res
    elif current_savings < down_payment - 100:
        low = res
    if steps > 100:
        break
    if abs(current_savings - down_payment) < 100:
        flag = True
    res = (high + low) // 2
    steps += 1
if flag:
    print("Best savings rate:", res / 10000.0)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
