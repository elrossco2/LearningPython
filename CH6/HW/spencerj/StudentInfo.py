def main():
    infile = open("UserNames.prn", "r")
    header = infile.readline()
    #print (header)
    avg = 0
    count = 0
    for line in infile:
        line = line.split()
        score = line[3]
        avg = avg+eval(score)
        count = count + 1
       # print(avg)
    average = avg/count
    print("The average score was {0:.2f}.".format(average))
main()
