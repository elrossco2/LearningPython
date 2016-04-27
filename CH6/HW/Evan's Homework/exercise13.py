def toNumbers(strList):
     
    entry = 0
    for i in strList:
        strList[entry] = int(i)
        entry = entry+1
     
def main():
    print('This program converts lists of strings to numbers.')
    strList = input('Please enter your numbers seperated by a comma: ')
     
    strList = strList.split(',')
     
    toNumbers(strList)                     
     
    print('The list of numbers is',strList)

