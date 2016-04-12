def main():
	count = 0
	x = eval(input("What is the annualized interest rate?: "))
	i = eval(input("What is the initial investment?: "))
	h = 2 * i
	while i <= h:
		i = i + i * x #fixed by Burrows 4/12/16
		count = count + 1
	print (count)


main()
