from graphics import *

def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(25, 230), ' 0.0K').draw(win)
    Text(Point(25, 180), ' 5.0K').draw(win)
    Text(Point(25, 130), ' 10.0K').draw(win)
    Text(Point(25, 80), ' 15.0K').draw(win)
    Text(Point(25, 30), '20.0K').draw(win)
    input = Entry(Point(280,90),5)
    input.setText("0.0")
    input.getAnchor()
    input.setFill("yellow")
    input.draw(win)
    output = Text(Point(170,90),"Enter the initial principal: ")
    output.draw(win)
    submit = Text(Point(280,150),"NEXT")
    clickme = Circle(Point(280,150),35)
    clickme.setFill("green")
    clickme.draw(win)
    submit.setOutline("black")
    submit.draw(win)
    win.getMouse()
    principal = eval(input.getText())
    output.undraw()
    output = Text(Point(155,90),"Enter the annual interest rate: ")
    output.draw(win)
    input.setText("0.0")
    win.getMouse()
    apr = eval(input.getText())
    submit.undraw()
    input.undraw()
    output.undraw()
    clickme.undraw()
    
    # Draw bar for initial principal
    height = principal * 0.01

    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.01
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

   # Click box to End
    clickme2 = Rectangle((Point(315,235)),(Point(245,195)))
    clickme2.setFill("red")
    clickme2.draw(win)
    submit2 = Text(Point(280,215),"EXIT")
    submit2.setOutline("black")
    submit2.draw(win)
    win.getMouse()
    win.close()

main()
