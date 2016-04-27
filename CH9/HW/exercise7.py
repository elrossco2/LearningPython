from random import randrange

def main():
    print ("This program simulates games of craps, then computes the probability of winning a game based on the results of the simulations.")
    b = eval(input("How many games do you want to simulate?"))
    win = 0
    for i in range(b):
        x = randrange(1,7)
        y = randrange(1,7)
        z = x + y
        if z == 7 or z == 11:
            win = win + 1
        elif z == 2 or z == 3 or z == 12:
            win = win + 0
        else:
            q = 0
            while q !=7 and q !=z:
                m = randrange(1,7)
                n = randrange(1,7)
                q = m + n
            else:
                if q == 7:
                    win = win + 0
                elif q == z:
                    win = win + 1

    print ("The probability of winning a game of craps is", win/b)
