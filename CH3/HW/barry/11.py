def main():
        print("Find the sum of a group of numbers.")
        n = input("How many numbers will you be adding?: ")
        sum = 0
        for i in range(n):
                x = input("Enter a number: ")
                sum = sum + x
        print("Sum of your numbers is", sum)
	
main()
