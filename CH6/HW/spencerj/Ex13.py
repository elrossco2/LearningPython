def toNumbers(strList):
    newList = []
    count = 0
    for string in strList:
       # print(string)
        count = count + 1
        newList.append(count)
    return newList

def main():
    stlist = ["a","b","c"]
    print(toNumbers(stlist))

main()
