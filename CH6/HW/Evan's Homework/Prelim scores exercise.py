def main():
	import math
	sum = 0
	count = 0
	usernames = open("Usernames.prn", "r")
	skip = usernames.readline()
	for line in usernames:
		value = line.split()
		x = int(value[3])
		sum = sum + x
		count = count + 1
	print ("The average preliminary score is", sum/count)
