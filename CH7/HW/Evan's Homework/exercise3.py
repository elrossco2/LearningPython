def main():
	print ("This program converts a point grade to a letter grade.")
	score = eval(input("What is the score of the test (0-100)?: "))
	if score > 89:
		print ("The letter grade is A.")
	elif 80 <= score <= 89:
		print ("The letter grade is B.")
	elif 70 <= score <= 79:
		print ("The letter grade is C.")
	elif 60 <= score <= 69:
		print ("The letter grade is D.")
	else:
		print ("The letter grade is F.")
