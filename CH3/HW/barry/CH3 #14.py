def main():
        print("Find the average of a group of numbers.")
        n = input("How many numbers will you be averaging?: ")
        for i in range(n):
                number = input("Enter a number: ")
                number = number + number
        average = number / n
        print("Average of your numbers is", average)
	
main()
