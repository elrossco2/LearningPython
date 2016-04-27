from math import *

def sumList(nums):
    total = 0
    for i in nums:
        total = total + i
    return total

def main():
    print("Sum a list of numbers. ")
    nums = input("Enter a list of numbers seperated by a space: ")

    nums = nums.split()

    entry = 0
    for i in nums:
        nums[entry] = int(i)
        entry = entry + 1

    sumTotal = sumList(nums)

    print("The sum of your list is: ",sumTotal)

main()
