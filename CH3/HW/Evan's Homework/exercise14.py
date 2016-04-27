def main():
	print ("This program finds the average of a list of numbers of your choice!")
	x = eval(input("How many numbers would you like to average?"))
	y = 0
	for i in range(x):
		num = eval(input("Enter one of your numbers:"))
		y = y + num
	result = y/x
	round(result,2)
	print ("The average of your values is:", result)