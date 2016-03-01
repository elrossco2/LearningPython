from math import *

def toNumbers(nums):
    x = 0
    for i in nums:
        nums[x]= int(i)
        x = x+1
     
def squareEach(nums):
    x = 0
    for i in nums:
        nums[x]= i**2
        x = x+1
 
def sumList(nums):
    sum = 0
    for i in nums:
        sum = sum+i
    return sum
     
def main():
    print('A program to read numbers from file, squaring and compute total sums.')
    file = input('Please enter filename: ')
     
    infile = open(file,'r')
 
    nums = []
    for i in infile:                 
        nums.append(i[:-1])          
     
    toNumbers(nums)                  
    squareEach(nums)
    total = sumList(nums)
     
    print('\nTotal sum of numbers from file "{0}" is {1}.'.format(file,total))

main()
