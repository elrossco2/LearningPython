# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:08:21 2016

@author: kiaph
"""

from graphics import *
from projectile import Projectile

class Tracker:
    
    def __init__(self, win, obj):
        
        self.x = obj.getX()
        self.y = obj.getY()
        self.c = Circle(Point(self.x,self.y),10)
        self.c.draw(win)
        self.update(self.x,self.y,self.c,win,obj)
        
 
## couldnt figure out how to get it to go right side down ( without 100 - self.y ) and couldnt figure out how to deal with permant circles.      
        
        
    def update(self,x,y,c,win,obj):
        
        self.x1 = obj.getX()
        self.y1 = obj.getY()
        
        self.c.move((self.x1-self.x),(self.y1-self.y))
        self.x = self.x1
        self.y = self.y1
        return self.x, self.y
        
''' class Tracker:
    def __init__(self, window, objToTrack):
        #window = window
        #self.winx.draw(winx)
        #obj = objToTrack
        #self.xpos = objToTrack.getX()
        #self.ypos = objToTrack.getY()
        xpos = 10*objToTrack.getX()+20
        ypos = 10*objToTrack.getY()+20
        center = Point(xpos,ypos)
        circ = Circle(center,10)
        circ.draw(window)
        self.updater(window,objToTrack)
    
   
   
    def updater(self,window,objToTrack):
        #draws circle
        #self.xpos = objToTrack.getX()
        #self.ypos = objToTrack.getY()
        #center = Point(xpos,ypos)
        #self.circ = Circle(center,5)
        #self.circ.fillOutline("red")
        xpos = 10*objToTrack.getX()+20
        ypos = 10*objToTrack.getY()+20
         #circ.undraw()
        circ = Circle(Point(xpos,ypos),20)
        circ.undraw()
        circ.draw(window)
        
        # window is a graphWin and objToTrack is an object whose
        #    position is to be show in the window. objToTrack is 
        #    an object that has getX() and getY() methods 
        #    that report its current position
        #
        
        # Creates a Tracker object and draws a circle in a window 
        #    at the current position of objToTrack.
        # 
        #   def update():
        #       moves the circle in the window to the current position   
        #           of the object being tracked
        #
        
        
        
        
        
        
        def window(self,window):
            self.win = GraphWin(window,420,420)
            self.win.setBackground("white")
            
            self.win.getMouse()
            self.win.close()
        
         #this was my first attempt.
        
def objToTrack(self,x,y):
          
                
        def update(self,x,y):
            self.xpos = x
            self.ypos = y
            self.Circle(Point(xpos,ypos),3) = cir
            self.cir.fillOutline("red")
            self.cir.draw(win)'''
            
            
    #def objToTrack():
        
        

