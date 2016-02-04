# futval_graph3.py

from graphics import *
from math import pow

def main():
    # Introduction
    print("This program plots the growth of a n-year investment.")
    nmax = eval(input("Enter the number of years n: "))
    # Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    #set graphics design parameters
    bmax = principal*pow((1 + apr),nmax)
    y0 = 0
    dy = bmax/4
    ymin = y0 - dy/2
    ymax = bmax + dy/2
    x_lt = 0
    x_rt = nmax + 1
    dx = (x_rt - x_lt)/(nmax + 1)
    xmin = x_lt - 3*dx*(nmax/10)
    xmax = x_rt + dx
    txp = (x_lt + xmin)/2
    K=1000
    win.setCoords(xmin, ymin, xmax, ymax)
    t0 = str(round(y0/K))+'K'
    p0 = Point(txp, y0)
    t1 = str(round((y0 + dy)/K))+'K'
    p1 = Point(txp, dy)
    t2 = str(round((y0 + 2*dy)/K))+'K'
    p2 = Point(txp, 2*dy)
    t3 = str(round((y0 + 3*dy)/K))+'K'
    p3 = Point(txp, 3*dy) 
    t4 = str(round((y0 + 4*dy)/K))+'K'
    p4 = Point(txp, 4*dy)
    Text(p0, t0).draw(win)
    Text(p1, t1).draw(win)
    Text(p2, t2).draw(win)
    Text(p3, t3).draw(win)
    Text(p4, t4).draw(win)
    
    # Draw bar for initial principal
    bar = Rectangle(Point(x_lt, y0), Point(dx, principal))
    bar.setFill("green")
    bar.setWidth(2*dx)
    bar.draw(win)
    # Draw a bar for each subsequent year
    for year in range(1, nmax + 1):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2*dx)
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()
    



    print(dx)






main()
