# -*- coding: utf-8 -*-
"""
Created on Tue May  3 03:58:49 2016

@author: kiaph
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:25:05 2016

craps game

@author: kiaph
"""
from random import random
##making my die, with the help of random from random

class Craps:
    
    def __init__(self):
        #init stuff
        w,h = width/2.0, height/2.0
    
        
    
    def rolldie():
        n = random()
        if n >= 5/6:
            die = 6
        elif n >= 4/6:
            die = 5
        elif n >= 3/6:
            die = 4
        elif n >= 2/6:
            die = 3
        elif n >= 1/6:
            die = 2
        else:
            die = 1
        #print(die)
        return die
    
 
###making the game
###turn 1

    def rolldice():
        die1 = rolldie()
        die2 = rolldie()
        dice = die1 + die2
        #print("This is the dice",dice)
        return dice
    
    
    def turn1():
        win = 2
        roll = rolldice()
        #print("first roll",roll)
        if roll == 2:
            win = 0
            
        elif roll == 3:
            win = 0
            
        elif roll == 12:
            win = 0
        
        elif roll == 7:
            win = 1
            
        elif roll == 11:
            win = 1
        else:
            self.roll1 = roll
            
        #print("check",win)
        return win
    
    
    def turnN():
        win = 2
        roll = rolldice()
        if roll == self.roll1:
            win = 1
        elif roll == 7:
            win = 0
        return win
        
    def gameplay():
        n = 0
        ##betting
        ##bank
        ##roll1
        ##betting again
        ##bank
        ##roll agains
        
    ####The counter
     
    def window():
        n = 0
        