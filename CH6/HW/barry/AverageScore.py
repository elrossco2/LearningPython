from math import *

def main():
    infile = open("UserNames.prn", "r+")
    header = infile.readline()

    sum = 0.0
    count = 0
    for line in infile.readlines():
        linelist = line.split()
        score = linelist[3]
        #print(score)
        sum = sum + eval(score)
        count = count + 1
    print("The average Prelim Score for the class is", round(sum / count),".")
    
main()
