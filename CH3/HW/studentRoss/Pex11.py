def main():
    print("The sum of the first n integers.")

    n = eval(input("Enter the integer n: "))
    numList = range(0, n+1)
    nsum = sum(numList)
    print("the sum = ", nsum)

main()
    
