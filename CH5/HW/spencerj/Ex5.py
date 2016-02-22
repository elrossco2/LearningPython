def main():
    name = input("Please enter a name: ")
    name = name.lower()
    output = []
    for character in name:
        number = abs(ord(character) - 96)
        output.append(number)
    #print(output)
    print("The number corresponding to the name",name.title(),"is:",sum(output))
main()
