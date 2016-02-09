import graphics
from graphics import Text
from graphics import Rectangle
from graphics import Point
from graphics import Entry
def main():
 
    win = graphics.GraphWin('Investment Grow Chart',320,240)
    win.setBackground('White')
    win.setCoords(-1.75,-9000,11.5,15400)
     
    Text(Point(4.87,13500),'Future Value Calculator').draw(win)
         
    Text(Point(4.5,-2000),'Input first principal:').draw(win)
    inputP = Entry(Point(9,-2000),6)
    inputP.setText('0')
    inputP.draw(win)
     
    Text(Point(3,-4000),' Input interest rate in decimal:').draw(win)
    inputR = Entry(Point(9,-4000),6)
    inputR.setText('0.0')
    inputR.draw(win)
     
     
    button = Rectangle(Point(2,-6000),Point(8,-8500))
    button.setFill('Green')
    button.draw(win)
    buttontext = Text(Point(5,-7250),'Show Result!:')
    buttontext.draw(win)
    win.getMouse()
     
    p = eval(inputP.getText())
    r = eval(inputR.getText())   
     
     
    Text(Point(-1,0),'0 K').draw(win)
    Text(Point(-1,2500),'2.5K').draw(win)
    Text(Point(-1,5000),'5 K').draw(win)
    Text(Point(-1,7500),'7.5K').draw(win)
    Text(Point(-1,10000),'10 K').draw(win)
     
    bar = Rectangle(Point(0,0),Point(1,p))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
     
    for i in range(1,11):
        p = p*(1+r)
        bar= Rectangle(Point(i,0),Point(i+1,p))
        bar.setFill('Green')
        bar.setWidth(2)
        bar.draw(win) 
     
    buttontext.setText('Quit.')
     
    win.getMouse()
    win.close()
