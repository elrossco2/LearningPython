from graphics import *

def main():
    win = GraphWin("CH4 Problem1")
    shape = Rectangle(Point(30,30),Point(50,50))
    shape.setOutline("red")
    shape.setFill("red")
    p = Point(40,40)
    label = Text(p, 1)
    shape.draw(win)
    label.draw(win)
    quitButton = Text(Point(100,10), "Keep Clicking to Quit")
    quitButton.draw(win)

    for i in range (10):
        p = win.getMouse()
        c = shape.getCenter()
        shape = Rectangle(Point(p.getX()+20,p.getY()+20),Point(p.getX(),p.getY()))
        shape.setOutline("red")
        shape.setFill("red")
        center = Point(p.getX()+10,p.getY()+10)
        label = Text(center, i+2)
        shape.draw(win)
        label.draw(win)
    win.close()

main()
