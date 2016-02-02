def main():
    list = eval(input("Enter numbers separated by commas: "))
    sum(list)
    avg = float(sum(list)/len(list))
    print("The average of the scores is:", avg)

main()
