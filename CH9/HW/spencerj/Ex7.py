from random import randrange
def main():
    print("Craps Dice simulation")
    numGames = eval(input("Number of games to simulate: "))
    #print(numGames)
    win = 0
    for i in range(numGames):
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        total = die1 + die2
        if total == 7 or total == 11:
            win = win + 1
        elif total == 2 or total == 3 or total == 12:
            win = win + 0
        else:
            point = 0
            while point != 7 and point != total:
                die3 = randrange(1,7)
                die4 = randrange(1,7)
                point = die3 + die4
            else:
                if point == 7:
                    win = win + 0
                elif point == total:
                    wint = win + 1
    
            
    print("Probabilty: ", (win/numGames))


main()
