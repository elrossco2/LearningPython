# -*- coding: utf-8 -*-
"""
Created on Wed May  4 06:50:12 2016

@author: kiaph


Most work only been done in sorter.py <---------------
please look at it

"""

def load_sections(filename):
    with open(filename, 'r') as infile:
        line = ''
        while True:
            while not line.startswith('****'): 
                line = next(infile)  # raises StopIteration, ending the generator
                continue  # find next entry

            entry = {}
            for line in infile:
                line = line.strip()
                if not line: break

                key, value = map(str.strip, line.split(':', 1))
                entry[key] = value
            print(entry)

            yield entry
            
            
load_sections('UserNames.prn')

def datafinder3(filename,row,collumn):
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
        
        
        


def datafinder2(filename,row):
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
          