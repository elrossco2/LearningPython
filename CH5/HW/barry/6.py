def main():
    print("Find the numeric value of your name")
    name = input("Enter your first name in lowercase: ")
    name = name.replace(" ", "")
    value = 0
    for ch in name:
        value = value + ord(ch)-96
    print("The value of your name is", value)
    
    
main()
