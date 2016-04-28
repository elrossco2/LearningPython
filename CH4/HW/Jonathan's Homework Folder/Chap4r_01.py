# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:00:09 2016

@author: book, modified by kiaph (JOnathan martin)
"""

from graphics import *

def main():
    win = GraphWin("Rectangle", 300, 300)
    win.setCoords(-10, -10, 10, 10)
    point1 = Point(-2, 2)
    point2 = Point(2, -2)
    shape = Rectangle(point1, point2)
    shape.setOutline("red")
    shape.setFill("pink")
    shape.draw(win)
    
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = shape.clone()
        shape2.move(dx, dy)
        shape2.draw(win)
        
    end = Text(Point(0, 0), "You have beaten me!")
    end.setSize(18)
    end.draw(win)
    win.getMouse()
    win.close()

    
main()