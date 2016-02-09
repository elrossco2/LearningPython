def main():
    print("Return the average of n numbers")

    nlist=eval(input("Enter the numbers in a comma separated list: "))

    print(type(nlist))
    print(len(nlist))

    print("the average is :", sum(nlist)/len(nlist))


main()
    
