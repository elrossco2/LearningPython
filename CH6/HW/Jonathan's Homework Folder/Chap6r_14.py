# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:18:53 2016

@author: kiaph
"""



def main():
#read the file
    print(" ")
    print("Welcome, this program will read the numbers in a file line by line beggining on line 1, in case of error, please check your file for non-number entries beyond line 0, thank you. \n")
    inputs = input("what is the name of your file?(example = numbers.prn) ")
    #startingline = input("What lines do the numbers begin on?: ")
    #sline = int(startingline)
    #numbs = open("numbers.prn","r")
    #numbs = open(inputs, "r")
    numbs = open(inputs,"r")
    number = numbs.readline()
    numb = numbs.readlines()
    #modify the value
    for number in numb:
        #number = numbs.readline()
        #print(number)
        num = int(number)
        newnum = num*num
        print(newnum)
        
main()



