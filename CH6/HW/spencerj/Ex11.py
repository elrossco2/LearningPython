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
    nlist = [2,4,6,8]
    squareEach(nlist)
    print(squareEach(nlist))
main()
