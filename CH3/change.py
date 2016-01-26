#Calculate the value of change in dollars--as an excersise to understand
#integer (int) and floating point (float) data types.

def count():
    print("Change Counter")
    print()
    print("Enter the number of each coin type.")
    q = eval(input("Quarters: ")) #integer (int) inputs
    d = eval(input("Dimes: "))
    n = eval(input("Nickels: "))
    p = eval(input("Pennies: "))
    total = 0.25*q + 0.10*d + 0.05*n + 0.01*p #floating point (float) output
    print()
    print("The total is: $", round(total, 2), sep='')

count()
