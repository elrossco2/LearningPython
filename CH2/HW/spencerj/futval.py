# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years the investment will last:"))
    
    for i in range(years):
        principal = principal * (1 + apr)
    if years>1:
        print("The value in " , years , " years is:", principal)
    else:
        print("The value in " , years , " year is:", principal)
main()
