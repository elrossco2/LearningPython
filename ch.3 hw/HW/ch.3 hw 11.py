Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #A program to find the sum of the first n natural numbers, where the value of n is provided by the user
>>> 
>>> def main():
	print("Find an average of the group of numbers.")
	n=input("How many numbers will be averaged?")
	for i in range(n):
		number= input("enter a number: ")
		number= number+number
		print("the Sum of your number is", number)
	main()
