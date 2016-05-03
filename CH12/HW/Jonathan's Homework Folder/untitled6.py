# -*- coding: utf-8 -*-
"""
Created on Tue May  3 04:14:08 2016

@author: kiaph
"""
from graphics import *
from button import Button
from dieview import DieView




def window():
    
    pointA = Point(125,75)
    pointB = Point(125,175)
    pointC = Point(125,275)
    pointD = Point(350,150)
    pointE = Point(500,150)
    pointF = Point(450,275)
    pointG = Point(475,50)
    pointX = Point(575,25)
    
    win = GraphWin("Crap Heaven",600,350)
    win.setBackground("purple")

    pt = win.getMouse()
    bA = Button(win,pointA,150,50,"Bet 1000!")
    bB = Button(win,pointB,150,50,"Bet 100!")
    bC = Button(win,pointC,150,50,"Bet 10!")
    bD = DieView(win,pointD,100)
    bE = DieView(win,pointE,100)
    bF = Button(win,pointF,200,50,"Bank Account")
    button2 = Button(win,pointG,150,50,"Win!")
    button1 = Button(win,pointX,25,25,"X")  
    button2.activate
    button2.active
    while not button2.clicked(pt):
        if button2.clicked(pt):
            win.close()
    pt = win.getMouse()

    
window()    
    
    