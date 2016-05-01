# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:11:38 2016

@author: kiaph
"""

def main():
    print()    
    print(" This program will take inputed values and use them to determine an employee's weekly earning based on hours worked.")
    print()
    name = input("What is the employee's name: ")
    weeklyhours = input("Hours worked this week?: ")
    hourlypay = input("?Hourly pay this week?: " )
    print()
    if float(weeklyhours) > 40:
        pay = 40*float(hourlypay)
        overtime = float(weeklyhours) - 40
        overpay = 1.5*float(hourlypay)*float(overtime)
        pay = float(overpay) + float(pay)
    else:
        pay = float(weeklyhours)*float(hourlypay)
        
    print("The weekly wages earned for ",name," is: $",pay, sep="")
main()

