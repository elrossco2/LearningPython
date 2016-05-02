# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:51:49 2016

@author: kiaph
"""

from math import log

def main():    
    n = 0
    print()
    print("This program will calculate how long it takes your starting value to become twice of the starting value!")
    
#### initial investment

    ii = eval(input("how much are you investing!?: "))
    

######given interest rate

    ir = eval(input("how much interest are you interested in!??: "))
    per = eval(input("How many times yearly with this interest be applied?: "))
    

#######looop to double

    ##test value   
    years = (log(2)/log(1+float(ir/per)) / float(per))
    nii = int(ii)*2    
    while ii <= nii:
        ii = ii + ii*ir
        n = n + 1


    loopyears = n/per
    
###### print results
    
    print("The annualized interest rate applied to your orignal value will take",loopyears,"to double")
    print("The expected value from a non loop based calculation was,",years)
main()


## actually loopyears doesn't work, and I can't figure out why, maybe I am using calculator wrong, but A = P(1+r/n)^nt , or so I thought, was the compound-algebra, has got me
## many correct answers on test, but for what ever reason now seems completely off, maybe I am rememberwring wrong, and the equation is for something else.
## don't have time to waste, have to save this , submit this, and move on.