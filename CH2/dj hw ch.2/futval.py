# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years= 10
    for i in range(10):
        principal = principal * (1 + apr)

    print("The value "years" in years is:", principal)

main()
