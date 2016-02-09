# futval_graph.py

from graphics import *

def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 400, 300)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    
    # Get principal and interest rate
    principal = Entry(Point(390,200),4)
    principal.draw(win)
    apr = Entry(Point(390,230),4)
    apr.draw(win)
    principalText = Text(Point(345,200), 'PRNC')
    principalText.draw(win)
    aprText = Text(Point(350,230), 'APR')
    aprText.draw(win)

    # Wait for mouse click
    submit = Text(Point(180,290), 'Click here to submit your Principal and APR')
    submit.draw(win)
    win.getMouse()

    # Get the input
    principalVal = eval(principal.getText())
    aprVal = eval(apr.getText())
    
    # Draw bar for initial principal
    height = principalVal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next year
        principalVal = principalVal * (1 + aprVal)
        # draw bar for this value
        xll = year * 25 + 40
        height = principalVal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    
    submit.setText('Click here to exit the program')
    win.getMouse()
    win.close()

main()
