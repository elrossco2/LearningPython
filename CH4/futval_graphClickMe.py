# futval_graph.py

from graphics import *

def main():
    # Introduction
    #print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    
    #point1 = Point(100,10)
    
    #t = Entry(point1,30)
    #t.setText("testing this out ")
    #t.draw(win)
    
   # principal = eval(input("Enter the initial principal: "))
    #apr = eval(input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 420, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    Text(Point(210,10), 'This program plots the growth of a 10-year investment.').draw(win)
    input = Entry(Point(390,90),5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(270,90),"Enter the initial principal: ")
    output.draw(win)
    submit = Text(Point(360,160), "ENTER")
    #submit.draw(win)
    clickme = Rectangle((Point(400,180)),(Point(320,140)))
    clickme.setFill("yellow")
    clickme.draw(win)
    submit.setOutline("black")
    submit.draw(win)
    win.getMouse()
    principal = eval(input.getText())
    output.setText("Enter the initial apr below: ")
    win.getMouse()
    apr = eval(input.getText())
    output.setText("Press continue to start graph: ")
    submit.undraw()
    input.undraw()
    submit.setSize(8)
    submit.setText("CONTINUE")
    submit.draw(win)
    win.getMouse()
    submit.undraw()
    output.undraw()
    clickme.undraw()
    

    # Draw bar for initial principal
    height = principal * 0.02
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
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    
    clickme2 = Rectangle((Point(415,235)),(Point(345,195)))
    clickme2.setFill("red")
    clickme2.draw(win)
    submit2 = Text(Point(380,215), "EXIT")
    submit2.setOutline("Black")
    submit2.draw(win)
    win.getMouse()
    win.close()

main()
