# avg2.py
#   A simple program to average two exam scores  
#   Illustrates use of multiple input

def main():
    print("This program use to computes the average of two exam scores.")
    print("Thanks to my expert coding skills it now computes 3")

    score1, score2, score4 = eval(input("Enter three scores separated by comma: "))
    average = (score1 + score2 + score4) / 3

    print("The average of the scores is:", average)

main()
