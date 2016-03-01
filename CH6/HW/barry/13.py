from math import *

def toNumbers(strList): 
    entry = 0
    for i in strList:
        strList[entry] = int(i)
        entry = entry+1
     
def main():
    print("Convert a string to a real number. ")
    strList = input("Enter a string of number seperated by a space: ")
     
    strList = strList.split()
     
    toNumbers(strList)                     
     
    print("Your number are: ",strList)

main()
