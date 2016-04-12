def main():
    print('       Table for Wind Chill at certain temperatures and wind speeds')
    print('-----------------------------------------------------------------------------')
    print('    |  -20  |  -10  |   0   |   10  |   20  |   30  |   40  |   50  |   60  |')
    print('-----------------------------------------------------------------------------')
     
    v = 0
     
    while v <= 50:
         
        wind = str(v)

        print(wind.center(2),end="  |  ")     
        t = -20
         
        while t <=60:
            x = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
            x = str(round(x))
                               
            print(x.center(3),end="  |  ")     
            t = t+10
         
        print()
        v = v+5
         
    print('-----------------------------------------------------------------------------')
main()
