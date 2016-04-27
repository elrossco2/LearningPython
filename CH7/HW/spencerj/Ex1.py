def main():
    hours = eval(input("Please input the number of hours: "))
    #print(hours)
    wage = eval(input("Please input the hourly wage: "))
    #print(wage)
    if hours < 40:
        print("The total amount earned is", hours*wage)
    else:
        ovrtime = hours - 40
        print("Overtime is", ovrtime,"hours.")
        regtime = hours - ovrtime
        print("Regular time is", regtime,"hours.")
        total = (regtime*wage) + (ovrtime*(wage*1.5))
        print("The total amount earned is ${0}".format(total))
main()
