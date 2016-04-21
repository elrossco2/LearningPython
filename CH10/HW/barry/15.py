from graphics import *
from projectile import *
from random import randrange
import time

class Tracker:

    def __init__(self, window, objToTrack):
        #print("construct Tracker object.")
        self.p = objToTrack
        self.x = self.p.getX()
        self.y = self.p.getY()
        #print(window.height)
        radius = 0.01*window.height
        #colors = ["red","green","blue","yellow","orange","black"]
        self.prt = Circle(Point(self.x,self.y), radius)
        self.prt.setFill("green")
        self.prt.draw(window)
        
        

    def update(self):
        #print("move object in window.")
        x1 = self.p.getX()
        y1 = self.p.getY()
        #print(self.x, self.y)
        dx = x1 - self.x
        dy = y1 - self.y
        #print("dx,dy: ", dx, dy)
        self.prt.move(dx, dy)
        self.x = x1
        self.y = y1

def main():
    print("Flight of a cannonball.\n")
    print("Angle = 45 degrees\nVelocity = 27 m/s\nIntial height = 0\n")
    print("Coodinates for every tracked position are:\n")

    p = Projectile(45, 27, 0)
    h = 200
    w = 400
    scale = .2
    win = GraphWin("Projectile Motion", w, h)
    win.setCoords(-5,-2, w*scale, h*scale)
    pTrace = Tracker(win, p)

    dt = .05
    p.update(dt)
    #print(p.getX(), p.getY())
    #print("x, y = ", p.getX(), p.getY())
    #print("\nDistance traveled: {0:0.1f} meters.".format(p.getX()))
    
    for theta in range(1):
        prj = Projectile(45, 27, 0)
        pTr = Tracker(win, prj)
        while prj.getY() >= 0:
            prj.update(dt)
            pTr.update()
            print(prj.getX(), prj.getY())
            time.sleep(.67*dt)

if __name__ == '__main__': main()
