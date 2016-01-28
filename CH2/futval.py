# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment for a given number of years.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the lenth in years for your investment: "))
    for i in range(year):
        principal = principal * (1 + apr)

    print("The value in", year , "years is $", principal)

main()
