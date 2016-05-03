# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:24:41 2016

@author: kiaph
"""



def main():
    names = open("UserNames.prn", "r")
    #print out what it in file
    line = names.readline()
    #namesofstudents = names.readline()
    #make counter
    totalgrade = 0
    counter = 0
    for line in names:
        #print(namesofstudents)
        #print(line)
        location = (line.split())
        grade = int(location[3])
        #print(grade)
        counter = counter + 1
        #print(counter)
        #print(totalgrade)
        totalgrade = totalgrade + grade
        names.write(totalgrade)
    #print("The prelim scores average is: ", int(totalgrade/counter))
    print("The prelim scores average is: ", str(totalgrade/counter))
main()
   
    
