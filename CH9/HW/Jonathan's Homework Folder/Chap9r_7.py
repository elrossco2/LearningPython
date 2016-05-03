# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:25:05 2016

craps game

@author: kiaph
"""
from random import random
##making my die, with the help of random from random

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


def win():
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
        while win == 2:
            roll2 = rolldice()
            #print("reroll",roll2)
            if(roll2 == roll):
                win = 1
                
            elif(roll2 == 7):
                win = 0
                
            else:
                win = 2
                
        
    
    
    #print("check",win)
    return win
            
####The counter
 
def main():
    print()
    print("This program will simulate the odds off winning x number of crap games, where x is the number you would like to know about.")   
    print()
    number_of_games = eval(input("How many games would you like to simulate?: "))    
    print()
    gamesplayed = 0
    wins = 0
    loss = 0
    
    while gamesplayed < number_of_games:
        game = win()
        if game == 1:
            wins = wins + 1
        else:
            loss = loss + 1
        gamesplayed = gamesplayed + 1
    print("There was a total of,",wins,"won and",loss,"loss.")
    winningchance = int(wins)/int(number_of_games)
    print("The probability of winning based of these stats is",int(winningchance*100),"percent.")        
            

main()

