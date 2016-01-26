#illustrate multiple input:

def ave():
    print("Output the average of 3 numbers.")
    n1, n2, n3 = eval(input("Enter the comma separated numbers on one line: "))
    av = (n1+n2+n3)/3
    print("The average = ", av)
ave()

def ave2():
    print("Output the average of N numbers.")
    nlist = eval(input("Enter the comma separated numbers on one line: "))
    numsum=0
    count=0
    for n in nlist:
        numsum=numsum+n
        count = count + 1
    print(numsum/count)
        
