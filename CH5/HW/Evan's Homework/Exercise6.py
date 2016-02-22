def main():
    print("A program to convert any full name to divine number!")
    name = input("Please enter your full name: ")
    name = name.replace(" ","") 
    total = 0
    for i in name.lower():
        total = total+ord(i)-96
    print("\nYour lucky number is:",total)