def main():
    print ("This program evaulates a quiz score based on a pre-determined scale")
    x = eval(input("What is the quiz score?: "))
    score = int(x)
    scale = ["F","F","D","C","B","A"]
    print ("The letter grade of the score is: ", scale[score])

