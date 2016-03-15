def main():
	count = 0
	x = eval(input("What is the annualized interest rate?: "))
	i = eval(input("What is the initial investment?: "))
	h = 2 * i
	while i <= h:
		i = i * x
		count = count + 1
	print (count)
