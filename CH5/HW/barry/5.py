def main():
    print("Find the numeric value of your name")
    name = input("Enter your first name in lowercase: ")
    value = 0
    for i in name:
        value = value + ord(i)-96
    print("The value of your name is", value)
    
    
main()
