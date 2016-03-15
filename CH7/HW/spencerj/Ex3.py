def main():
    grade = eval(input("Please input the number grade: "))
    #print(grade)
    if grade >= 90:
        print("The letter grade is an 'A'")
    elif grade >= 80 and grade < 90:
        print("The letter grade is a 'B'")
    elif grade >= 70 and grade < 80:
        print("The letter grade is a 'C'")
    elif grade >= 60 and grade < 70:
        print("The letter grade is a 'D'")
    else:
        print("The letter grade is an 'F'")
    
main()
