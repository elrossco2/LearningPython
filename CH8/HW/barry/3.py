
#This program determines how many years it takes for an investment to double
#at a given interest rate

def interest(apr):
    present = 1
    future = present
    years = 0 

    while future <= present * 2:
        future = future * (1 + apr)
        years = years + 1

    return years
        
def main():
    print("This program determines how many years it takes for an investment")
    print("to double at a given interest rate.\n")
    print("Enter interest rate as a decimal. Example --> 0.03 = 3%\n")

    try:
        apr = eval(input("Enter your annualized interest rate: "))

        years = interest(apr)

        print("It will take", years,"years to double the present value of your")
        print("principal.")

    except SyntaxError:
        print("Enter only numbers. Not symbols.")
    
    except NameError:
        print("Enter only numbers. Not letters.")

main()

