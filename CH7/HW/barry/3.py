#Decision Structure for an exam

def main():
    print("This Program returns your grade from an exam score.")
    grade = eval(input("What score did you get on your exam? "))

    if grade >= 90:
        print("Your corresponding grade on the exam was an A.")

    if grade >=80 and grade <90:
        print("Your corresponding grade on the exam was a B")

    if grade >=70 and grade <80:
        print("Your corresponding grade on the exam was a C")

    if grade >=60 and grade <70:
        print("Your corresponding grade on the exam was a D")

    if grade <60:
        print("Your corresponding grade on the exam was a F")

main()
