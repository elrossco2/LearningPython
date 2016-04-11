from math import sin,cos,radians
from graphics import *
from time import sleep
 
 
class Projectile:
    '''Projectile class copy from the book'''
     
    def __init__(self,angle,velocity,height):
         
        self.xpos = 0
        self.ypos = height
        theta = radians(angle)            
        self.xvel = velocity * cos(theta)      
        self.yvel = velocity * sin(theta)
         
    def update(self,time):
         
        self.xpos = self.xpos + time*self.xvel
        yvel1 = self.yvel - time*9.8           
        self.ypos = self.ypos + time*(yvel1+self.yvel)/2
        self.yvel = yvel1
         
    def getX(self):
        return self.xpos
     
    def getY(self):
        return self.ypos
 
 
class Tracker:
    '''Use to track projectile object and draw it on the screen'''
     
    def __init__(self,window,objToTrack):
         
        self.objToTrack = objToTrack
         
        self.x = objToTrack.getX()
        self.y = objToTrack.getY()

        self.c = Circle(Point(self.x+3,self.y+3),1)
        self.c.setFill('grey')
        self.c.setWidth(0)
        self.c.draw(window)
     
     
    def update(self,time):
         
        self.objToTrack.update(time)

        x = self.objToTrack.getX()
        y = self.objToTrack.getY()

        Xmoving = x - self.x
        Ymoving = y - self.y

        self.c.move(Xmoving,Ymoving)

        self.x = x
        self.y = y
         
    def undraw(self):
        self.c.undraw()
         
                 
     
         
class Button:
 
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""
 
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
 
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
 
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
 
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
 
    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
 
 
def drawGUI():
    '''Drawing all graphic object into screen'''

    win = GraphWin('Projectile Tracker,',1500,800)
    win.setBackground('white')
    win.setCoords(0,0,150,80)
         

    Line(Point(3,3),Point(3,73)).draw(win)
    Line(Point(3,3),Point(143,3)).draw(win)
     

    for i in range(1,141):
        Line(Point(i+3,2.5),Point(i+3,3.5)).draw(win)
        if i%5 == 0:
            Line(Point(i+3,2),Point(i+3,4)).draw(win)
            Text(Point(i+3,1.5),i).draw(win)
             
         
    for i in range(1,71):   
        Line(Point(2.5,i+3),Point(3.5,i+3)).draw(win)
        if i%5 == 0:
            Line(Point(2,i+3),Point(4,i+3)).draw(win)
            Text(Point(1.5,i+3),i).draw(win)
             
    Text(Point(2,2),0).draw(win)
    Text(Point(148,3),'metre').draw(win)
    Text(Point(2.5,77),'metre').draw(win)       

    a_input = Entry(Point(13,75),5)
    a_input.draw(win)
    Text(Point(8,75),'Angle:').draw(win)
     
    v_input = Entry(Point(27,75),5)
    v_input.draw(win)
    Text(Point(21,75),'Velocity:').draw(win)
     
    h_input = Entry(Point(40,75),5)
    h_input.draw(win)
    Text(Point(34.5,75),'Height:').draw(win)
     
    t_input = Entry(Point(52,75),5)
    t_input.draw(win)
    Text(Point(47,75),'Time:').draw(win)

    throw_button = Button(win,Point(63,75),5,3,'Throw')
    throw_button.activate()
         
    quit_button = Button(win,Point(73,75),5,3,'Quit')
         
     
    return win, a_input, v_input, h_input, t_input, throw_button, quit_button
 
 
 
def getInput(win, a_input, v_input, h_input, t_input, throw_button, quit_button):
     
    p = win.getMouse()
     
    while not quit_button.clicked(p):
         
        if throw_button.clicked(p) == True:
             
            quit_button.activate()
             
            a = float(a_input.getText())
            v = int(v_input.getText())
            h = int(h_input.getText())
            t = float(t_input.getText())
             
            cball = Projectile(a,v,h)
            track_ball = Tracker(win,cball)
     
            while cball.getY() >= 0:

                sleep(0.02)
                track_ball.update(t)
                 
            track_ball.undraw()
             
        p = win.getMouse()
 
 
def main():
     
    win, a_input, v_input, h_input, t_input, throw_button, quit_button = drawGUI()
     
     
    a,v,h,t = getInput(win, a_input, v_input, h_input, t_input, throw_button, quit_button)
 
     
    win.getMouse()
     
if __name__ == '__main__': main()
