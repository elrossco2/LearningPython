#Total wages for the week

def main():
    print("This program calculates your weekly wages")

    try:
        hours = eval(input("How many hours did you work this week? "))
        wages = eval(input("How much do you get paid hourly? "))

        if hours <= 40:
            total = hours * wages
            print("Your bank roll should increase by $", round(total,2))

        elif hours > 40:
            extra = hours - 40
            total = (extra * (1.5 * wages) + ((hours - extra) * wages))
            print("Your bank roll should increase by $", round(total,2))

    except SyntaxError:
        print("Enter only numbers. Not $ signs")
    


main()
