# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:02:27 2016

@author: kiaph
"""
from graphics import *

def main():
    win = GraphWin()
    shape = Circle(Point(50,50),20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p= win.getMouse()
        c= shape.getCenter()
        dx= p.getX() - c.getX()
        dy= p.getY() - c.getY()
        shape.move(dx,dy)
    win.close()
main()

