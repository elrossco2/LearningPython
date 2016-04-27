def toNumbers(strList):
    newList = []
    count = 0
    for string in strList:
       # print(string)
        count = count + 1
        newList.append(count)
    return newList

def sumList(numList):
    nsum = 0
    #newList = []
    for num in numList:
       # print(num)
        nsum = nsum + num
        #print(sq)
        #newList.append(nsum)
    #print(newList)
    return nsum

def squareEach(numList):
    sq = 0
    newList = []
    for num in numList:
       # print(num)
        sq = num*num
        #print(sq)
        newList.append(sq)
    #print(newList)
    return newList

def main():
    fileName = input("Please input the name of the file: ")
    infile = open(fileName, "r")
    nlist = []
    count = 0
    for line in infile:
        line = line.split()
        #print(line)
        nlist.append(eval(line[0]))
       # print(line)
        count = count + 1
   # print (nlist)
   # print (squareEach(nlist))
    square = (squareEach(nlist))
    print (sumList(squareEach(nlist)))
    
main()
    
