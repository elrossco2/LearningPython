def main():
    initial = eval(input("Initial amount: "))
    interest = eval(input("Interest rate: "))
    x = 0
    end = initial*2
    #print(end)
    while initial <= (end):
        y = initial * interest
        initial = initial + y
        x = x + 1
    print("It will take", x ,"years to double the investment at a rate of ", interest ,".")
main()
