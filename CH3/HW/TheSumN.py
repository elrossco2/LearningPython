# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:15:32 2016


@author: kiaph

This small script will sum numbers from 0 to your desired value n.



"""

def main():
    print(" This program will sum numbers starting from 0 ending at n. ")
    
    n = eval(input("Please enter a value for n: "))
    
    total = 0
    p = n
    i = 0
    
    if n < 0:
        print("Please try again, without use of a negative number.")
   
    if n == 0:
        print("The sum of numbers between 0 and 0 is 0")        
        print("Do you really need help with such a thing?")
        print("Please try harder next time.")
        
    else:
        
        while i != n:
            i = i + 1
           ### print("the current value of n is: ", p)
            ### this was used for trouble shooting.
            total = total + i
            p = p - 1
        else:
            print( total, "is the sum of the numbers between 0 and ", n )
    
            
main()