# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:44:32 2016

@author: kiaph
"""

def main():
    print("")
    print("This program will accept a grade between the numbers 0-1000 and return the letter value associated with the grade")
    print()
    score = float(input("Numeric value for the grade: "))
    print()
    if score < 59.45:
        print("The student failed, F")
    elif score < 69.45:
        print("The student did poorly, D")
    elif score < 79.45:
        print("The student did subpar, C")
    elif score < 89.45:
        print("The student did better than average, B")
    elif score < 100.01:
        print("The student did well, A")
    elif score < 1000:
        print("The student has suprassed the teacher!, PHD")
    else:
        print("Something went wrong, try again with a known number between 0 and 1000, example(fifty does not equal 50, so please use 50.), thankyou.")
main()        