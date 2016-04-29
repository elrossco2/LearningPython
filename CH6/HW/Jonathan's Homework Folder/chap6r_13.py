# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:18:32 2016

@author: kiaph
"""
def toNumbers(strList):
    entry = 0
    for i in strList:
        strList[entry] = int(i)
        entry = entry + 1
    return strList
        
def main():
    strList = input("Enter a string of numbers: ")

    strList = strList.split()

    numbers = toNumbers(strList)

    print("The string has been converted to numbers", numbers)

main()