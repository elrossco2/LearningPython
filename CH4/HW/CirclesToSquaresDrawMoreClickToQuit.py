# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:11:38 2016

@author: kiaph

Drawing Squares instead of circles.


"""
from graphics import *


"""

def main():
    win = GraphWin()
    shape = Circle(Point(50,50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c =shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    win.close()
main()
        
    """
    
def squares():
    win = GraphWin()
    sx = 50
    sy = 50
    point1 = Point(sx+5,sy+5)
    point2 = Point(sx-5,sy-5)
    shape2 = Rectangle(point1,point2)    
    shape2.setOutline("red")
    shape2.setFill("red")
    shape2.draw(win)
    for i in range(10):
        p = win.getMouse()
        c =shape2.getCenter()
        
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        
        sx = 50 + dx
        sy = 50 + dy
        point3 = Point(sx+5,sy+5)
        point4 = Point(sx-5,sy-5)
        ###shape2.move(dy,dx)
        ### above was for part a
        
        shape3 = Rectangle(point3,point4)
        shape3.setOutline("red")
        shape3.setFill("red")
        shape3.draw(win)
        
        
    point5 = Point(100,10)          
    t = Text(point5, "click again to quit")
    t.setFace("courier")
    t.setSize(10)
    t.setFill("red")
    t.setOutline("red")
    t.draw(win)
    
    win.getMouse()
    
    win.close()
    
squares()
