# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:53:43 2024

@author: mmacarty
"""

TAX_RATE = 0.20
STANDARD_DEDUCTION = 12200
DEDUCTION = 2000

print("Enter your income: ")
income = float(input())
print("Enter number of dependents: ")
dependents = int(input())
taxable_income = income - STANDARD_DEDUCTION - DEDUCTION * dependents
tax = taxable_income * TAX_RATE  
 

print("Your tax liability is:")
print(taxable_income)
print(tax)