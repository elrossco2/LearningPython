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
def main():
    nlist = [2,4,6,8]
    sumList(nlist)
    print(sumList(nlist))
main()
