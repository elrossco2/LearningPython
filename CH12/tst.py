from graphics import *

win = GraphWin("test", 400,400)


p = win.getMouse()

c = Circle(p, 10)

c.draw(win)

while True:
    p = win.getMouse()
    c = Circle(p, 10)
    c.draw(win)
