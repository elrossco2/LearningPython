def main():
    print("A program to convert your first name to divine number!")
    name = input("Please enter your first name: ")
    total = 0
    for i in name.lower():
        total = total+ord(i)-96
    print("\nYour lucky number is:",total)

main()
