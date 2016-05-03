# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:22:19 2016

@author: kiaph
"""

def main():
	import math
	sum = 0
	count = 0
	usernames = open("UserNames.prn", "r")
	skip = usernames.readline()
	for line in usernames:
		value = line.split()
		x = int(value[3])
		sum = sum + x
		count = count + 1
	print ("The average preliminary score is", sum/count)
main()
