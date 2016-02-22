def main():
    print("This program is used to convert exams score to a corresponding grade.")
    scores = eval(input("Please enter a score (0-100): "))
    grade = "F"*60+"D"*10+"C"*10+"B"*10+"A"*11
    print("Your grade is",grade[scores])
