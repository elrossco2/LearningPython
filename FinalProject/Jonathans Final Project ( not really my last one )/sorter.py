# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:05:26 2016

@author: kiaph
"""
"""
def printfile():
    #fname = input("Enter filename: ")
    fname = 'UserNames.prn'
    infile = open(fname, "r")
    data = infile.read()
    print(data)
    print("------------------------------------------------------------------------------")
printfile()

def newcode():
    someFile = 'UserNames.prn'
    infile = open(someFile, "r")
    line = infile.readline()
    print(line)
    print("----------------------------------------------------------------------------------")
newcode()

def othercode():
    infile = open('UserNames.prn', "r")
    for i in range(5):
        
        line = infile.readline()
        print(line[:-1])
    print("----------------------------------------------------------------------------")
othercode()

def othercode():
    infile = open('UserNames.prn', "r")
    for i in range(5):
        
        line = infile.readline()
        print(line)
    print("-------------------------------------------------------------------------------")
othercode()

def othercode2():
    infile = open('UserNames.prn', "r")
    for i in range(5):
        
        line = infile.readline()
        print(line, end="")
    print("-------------------------------------------------------------------------")
othercode2()

def othercode3():
    infile = open('UserNames.prn', "r")
    for line in infile.readlines():
        print(line)
    infile.close()
    print("---------------------------------------------------------------------------")
othercode3()

def othercode4():
    infile = open('UserNames.prn', "r")
    for line in infile:
        print(line)
    infile.close()
    print("---------------------------------------------------------------------------")
othercode4()


def write1():
    outfile = open('outputfile',"w")
    print('Woah doggy',file=outfile)
    outfile.close()
    print("---------------------------------------------------------------------------")
    infile = open('outputfile', "r")
    for line in infile.readlines():
        print(line)
    infile.close()
    print("---------------------------------------------------------------------------")
write1()



def userfile():
    infile = open('UserNames.prn',"r")
    outfile = open('NamesOnly.prn',"w")
    
    for line in infile:
        first, last, gender, score, major = line.split()
        uname = (first[0] + last[:7]).lower()
        print(uname, file=outfile)
    infile.close()
    outfile.close()

    pinfile = open('NamesOnly.prn', "r")
    for line in pinfile:
        print(line)
    pinfile.close()
    print("---------------------------------------------------------------------------")
    
userfile()

def userfile1():
    infile = open('UserNames.prn',"r")
    soutfile = open('females',"w")
    
    for line in infile:
        first, last, gender, score, major = line.split()
        x = first
        print(x)
        
        y = last
        print(y)
        
        z = gender
        print(z)
        
        if z == 'f':
            print(x,y,file=soutfile)
            
        
    soutfile.close()

    pinfile = open('females', "r")
    for line in pinfile:
        print(line)
    pinfile.close()
    print("---------------------------------------------------------------------------")
userfile1()
"""



class Sortme:
    
    
    
    ############# this class will sort the file by given criteria.
    
    def __init__(self,filename,row,collumn):
        
        file = filename
        x = row
        y = collumn
        if collumn == 'n':
           self.datafinder2(file,x)
        else:
           self.datafinder3(file,x,y)
        
        


        
        


















    def datafinder3(self,filename,row,collumn):
        filename = "UserNames.prn"
        infile = open(filename, 'r')
        objects = []
        for line in infile:
             lines = []
             for i in line.split():
                 lines.append(i)
                 
             objects.append(lines)
        print(objects[0][1])
        
        infile.close()

    def datafinder2(self,filename,row):
        filename = "UserNames.prn"
        infile = open(filename, 'r')
        objects = []
        for line in infile:
             lines = []
             for i in line.split():
                 lines.append(i)
                 
             objects.append(lines)
        print(objects[0][1])
        
        infile.close()
    



























