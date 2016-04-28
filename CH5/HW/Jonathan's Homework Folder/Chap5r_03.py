# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:00:52 2016

@author: kiaph
"""

def main():
    print("This program will convert whole number exam scores to their corresponding grades.")
    
    """Ask for the exam score"""
    x = eval(input("Enter the exam score as a whole number between 0 and 100: "))
    grade = (x // 10) - 1 #Find remainder, subtract one because we start from 0
    
    """ Index and list grades 1-10 : F-A """
    grades = ['F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A'] 
    
    print("The grade is", grades[grade])   
    
main()