from graphics import *


class spaceTest:

    myTest = "nameSpace-->spaceTest"

    def __init__(self):
        print("init")
        #print(myTest)
        print(self.myTest)
        inInit = "nameSpace-->init"
        self.inInit = "nameSpace-->spaceTest-2"
        print(inInit)

    def someFnc(self):
        print(self.inInit)
    



win = GraphWin('test window')
win.setBackground('red')
p = win.getMouse()
c = Circle(p, 10)
c.draw(win)


def main():

    t = spaceTest()
    t.someFnc()

    s = spaceTest()
    print("in main", s.myTest)


main()
