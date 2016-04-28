# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:05:23 2016

@author: kiaph
"""

def main():
    print("This program calculates the numeric value of a name.")
    
    """ Ask for the name to be calculated to numeric value"""
    name = input("Enter a name: ")
    name.lower()
    
    """ make alphabet list """    


    farts = " abcdefghijklmnopqrstuvwxyz"
    
    summ = 0 
    for i in name:
        farts.find(i)
        summ = farts.find(i) + summ
        
    print("The numeric value of your name is", summ)
    
main()