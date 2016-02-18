def main():

    grade = input("Enter the score of the test: ")
    if (eval(grade) == 5):
        print("The grade for this test is an A")
    elif (eval(grade) == 4):
        print("The grade for this test is a B")
    elif (eval(grade) == 3):
        print("The grade for this test is a C")
    elif (eval(grade) == 2):
        print("The grade for this test is a D")
    elif (eval(grade) == 1 or eval(grade) == 0):
        print("The grade for this test is an F")

main()
    
