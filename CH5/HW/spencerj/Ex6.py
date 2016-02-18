def main():
    name = input("Please enter a name: ")
    name = name.lower()
    mulName = name.split(" ")
    #print(mulName)
    output = []
    for names in mulName:
        for characters in names:
            number = abs(ord(characters) - 96)
            output.append(number)
    #print(output)
    print("The number corresponding to the name",name.title(),"is:",sum(output))
main()
