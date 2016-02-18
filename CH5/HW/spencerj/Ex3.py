def main():

    grade = input("Enter the score of the test: ")
    if (eval(grade) >= 90):
        print("The grade for this test is an A")
    elif (eval(grade) >= 80 and eval(grade) <= 89):
        print("The grade for this test is a B")
    elif (eval(grade) >= 70 and eval(grade) <= 79):
        print("The grade for this test is a C")
    elif (eval(grade) >= 60 and eval(grade) <= 69):
        print("The grade for this test is a D")
    elif (eval(grade) < 60):
        print("The grade for this test is an F")

main()
    
