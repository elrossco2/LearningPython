# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:51:49 2016

@author: kiaph
"""

from math import log

def main():    
    n = 0
    print("This program will calculate how long it takes your starting value to become twice of the starting value!")
    
#### initial investment

    ii = input("how much are you investing!?: ")
    

######given interest rate

    ir = input("how much interest are you interested in!?? :")
    per = input("How many times yearly with this interest be applied??" )
    

#######looop to double

    ##test value   
    years = (log(2)/log(1+(ir/per))) - per
    nii = ii*2    
    while ii <= nii:
        ii = ii + ii*ir
        n = n + 1


    loopyears = n/per
    
###### print results
    
    print("The annualized interest rate applied to your orignal value will take",loopyears,"to double")
    print("The expected value from a non loop based calculation was,",years)
    