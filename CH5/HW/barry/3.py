#Turns Exam Score 0-100 into a letter grade
def main():
    grade = input("What was your score on the exam? ")
    if grade >=90:
        print("You got an A on the exam.")
    if 90 > grade >=80:
        print("You got a B on the exam.")
    if 80 > grade >=70:
        print("You got a C on the exam.")
    if 70 > grade >=60:
        print("You got a D on the exam.")
    if 60 > grade:
        print("You got a F on the exam.")


main()
