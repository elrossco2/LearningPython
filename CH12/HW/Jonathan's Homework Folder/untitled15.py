# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:05:23 2016

@author: kiaph
"""

def main():
    print("This program calculates the numeric value of a name.")
    
    """ Ask for the name to be calculated to numeric value"""
    name = input("Enter your name: ")
    name.lower()
    
    """ Index the alphabet"""    
#    pha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    pha = " abcdefghijklmnopqrstuvwxyz"
    
    summ = 0 
    for i in name:
        pha.find(i)
        summ = pha.find(i) + summ
        
    print("The numeric value of your name is", summ)
    
main()