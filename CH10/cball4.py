# cball4.py
from projectile import Projectile
from tracker import Tracker
from graphics import *

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))
    
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    window = GraphWin("window",250,250)
    cball = Projectile(angle, vel, h0)
    #Tracker(window,cball)  
    while cball.getY() >= 0:
        cball.update(.001)
        Tracker(window,cball)  
        
    window.getMouse()      
    window.close()
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

if __name__ == "__main__":
    main()
