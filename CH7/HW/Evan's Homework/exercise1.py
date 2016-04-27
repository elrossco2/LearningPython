def main():
	print ("This program calculates the weekly paycheck of an employee.")
	wage = eval(input("What is the hourly wage of the employee?: "))
	hours = eval(input("How many hours did the employee work this week?: "))
	if hours < 41:
		weeklywage = wage * hours
		print ("This employee's paycheck for this week is", weeklywage, "dollars.")
	else:
		overtime = (hours - 40) * (1.5 * wage)
		hardworker = (wage * 40) + overtime
		print ("This employee's paycheck for this week is", hardworker, "dollars.")
