def main():
        print("Find the average of a group of numbers.")
        n = input("How many numbers will you be averaging?: ")
        sum = 0
        average = 0
        for i in range(n):
                x = input("Enter a number: ")
                sum = sum + x
        print("Average of your numbers is", sum / n)
	
main()
