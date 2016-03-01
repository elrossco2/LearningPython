def main():
	import math
	usernames = open("UserNames.prn", "r")
	skip = usernames.readline()
	
	first = usernames.readline()
	split1 = first.split()
	a = int(split1[3])

	second = usernames.readline()
	split2 = second.split()
	b = int(split2[3])
	
	third = usernames.readline()
	split3 = third.split()
	c = int(split3[3])
	
	fourth = usernames.readline()
	split4 = fourth.split()
	d = int(split4[3])
	
	fifth = usernames.readline()
	split5 = fifth.split()
	e = int(split5[3])
	
	sixth = usernames.readline()
	split6 = sixth.split()
	f = int(split6[3])

	seventh = usernames.readline()
	split7 = seventh.split()
	g = int(split7[3])

	eighth = usernames.readline()
	split8 = eighth.split()
	h = int(split8[3])

	ninth = usernames.readline()
	split9 = ninth.split()
	i = int(split9[3])

	tenth = usernames.readline()
	split10 = tenth.split()
	j = int(split10[3])

	eleventh = usernames.readline()
	split11 = eleventh.split()
	k = int(split11[3])

	twelfth = usernames.readline()
	split12 = twelfth.split()
	l = int(split12[3])

	thirteenth = usernames.readline()
	split13 = thirteenth.split()
	m = int(split13[3])

	fourteenth = usernames.readline()
	split14 = fourteenth.split()
	n = int(split14[3])

	fifteenth = usernames.readline()
	split15 = fifteenth.split()
	o = int(split15[3])

	sixteenth = usernames.readline()
	split16 = sixteenth.split()
	p = int(split16[3])

	seventeenth = usernames.readline()
	split17 = seventeenth.split()
	q = int(split17[3])

	eighteenth = usernames.readline()
	split18 = eighteenth.split()
	r = int(split18[3])

	nineteenth = usernames.readline()
	split19 = nineteenth.split()
	s = int(split19[3])

	x = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s
	print("The average of the preliminary scores from the UserNames.prn file is", x/19)
