# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:19:58 2016

@author: kiaph
"""
def main():
    print()    
    print("This program will magicly deduce your letter grade from any whole number between/or 0 and 5")
    varx = (input("What is the whole number you want to know about? "))
    if varx == "0":
        print("What a wonderful score! F")
    elif varx == "1":
        print("F, for Fantastic!")
    elif varx == "2":
        print("Delightful, the score is a D")
    elif varx == "3":
        print("Such a charming score! C")
    elif varx == "4":
        print("Better luck next time! You're a B")
    elif varx == "5":
        print("A, awesome, way to go, what did you expect with all that hard work?")
    else:
        print("Woah doggy, you typed: \"",varx,"\", We only accept the 6 following characters: 0,1,2,3,4,5. Thanks for playing, better luck next time!")
    print("Would you like to play again?")
    y = (input(":"))
    print("We are sorry, you entered:  \"",y,"\", we did not undertand you please check your answer and try again next time.")
    







main()
