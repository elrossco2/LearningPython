def alg(temp,wind):
    t = temp
    w = wind
    windchill = (35.74+(0.6215*t)-(35.75*(w**0.16))+(0.4275*t)*(w**0.16))
    #print(windchill)
    return windchill

def main():
    print("Couldn't make the chart properly, but I managed to do the rest of the problem")
    w = 0
    while w <= 50:
        t = -20
        while t <= 60:
            wind = round(alg(t,w))
            print("At ", t ,"degrees F and ", w ," windspeed, the windchill is:",wind)
            t = t + 10
        w = w + 5
        
main()
