from random import randrange


def dice():
    return randrange(1,7)+randrange(1,7)


def Craps(games):
         
    win = 0
    for i in range(games):
        first = FirstRoll()
        if first == "win": win = win+1
             
        elif first == "lose": win = win + 0

        else:
            next = Point(first)
            if next == "win": win = win+1
             
    return win


def FirstRoll():
     
    x = dice()
    if x == 7 or x == 11:
        status = "win"
         
    elif x ==2 or x ==3 or x ==12:
        status = "lose"
         
    else:
        status = x
     
    return status


def Point(point):
 
    x = 0
    while x !=7 and x !=point:
        x = dice()
         
        if x == point:
            status = "win"

        elif x == 7:
            status = "lose"
     
    return status



def main():
    try:
        print("This Program simulates the probability of winning Craps.")

        n = eval(input("How many games to simulate: "))

    except SyntaxError:
        print("Enter only numbers. Not symbols.")

    except NameError:
        print("Enter only numbers. Not letters.")
        
    x = Craps(n)

    print("\nGames simulated: ",n)
    print("Total winning: ",x)
    print("\nThe probability of winning Craps is: {:0.2}".format(x/n))
    
 
if __name__ == '__main__': main()
