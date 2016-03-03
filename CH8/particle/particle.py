# average6.py
from random import random

class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


class simBox:
    def __init__(self, X0, XR, Y0, YT):
        self.X0=X0
        self.XR=XR
        self.Y0=Y0
        self.YT=YT

    def bCondition(self, p):
        #print("bC")
        x0 = self.X0
        xR = self.XR
        y0 = self.Y0
        yT = self.YT
        if p.x < x0 or p.x > xR:
            p.vx = -p.vx
        if p.y > yT:
            p.y = p.y - yT
        elif p.y < y0:
            p.y = p.y + yT

        return p
        

    def make_particle(self):
        #print("make p")
        x = self.X0 + (self.XR-self.X0)*random()
        y = self.Y0 + (self.YT-self.Y0)*random()
        vx = 2*( 0.5 - random() )
        vy = 2*( 0.5 - random() )
        return Particle(x,y,vx,vy)

    def move_particle(self, p, dt):      
        p.x = p.x + p.vx*dt
        p.y = p.y + p.vy*dt
        p = self.bCondition(p)
        return p



def main():
    print("get started")

    box = simBox(0,10,0,10)
    #p1 = box.make_particle()
    #print(p1.x)
    N = 30 #number of particles.
    pList = [] #particles in box.
    for i in range(N):
        pList.append(box.make_particle())
        #print(pList[i].vx)

    #print(pList[0].x)
    #box.move_particle(pList[0], 0.5)
    #print(pList[0].x)

    dt = 0.5    
    timeSteps = 5
    for n in range(timeSteps):
        for i in range(N):
            #print(pList[i].x)
            box.move_particle(pList[i], dt)
            print(round(pList[i].x, 2), round(pList[i].y, 2))
            
    
main()
