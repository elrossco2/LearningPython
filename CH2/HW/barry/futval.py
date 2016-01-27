# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a wise or not so wise of an investment.")

    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate: ")
    years = input("Enter the number of years invested: ")

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years ,"years is:", principal)

main()
