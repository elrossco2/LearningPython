Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #A program that finds the average of a series of numbers entered by the user.
>>> def main():
	print("Find the average of numbers you will add.")
	n=input("How many numbers will be averaged?":")
		
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> #A program that finds the average of a series of numbers entered by the user.
>>> def main():
	print("Find the average of numbers you will add.")
	n=input("How many numbers will be averaged?")
	for i in range(n)
	
SyntaxError: invalid syntax
>>> for i in range(n):
	number=input("Enter a number.")
	number=number+number
	average=number/n
	print("Average of your number is", average)

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for i in range(n):
NameError: name 'n' is not defined
>>> main()
