from math import *

def squareEach(nums):
    entry = 0
    for i in nums:
        nums[entry] = i**2
        entry = entry + 1

def main():
    print("Square a list of numbers. ")
    nums = input("Enter a list of numbers seperated by a space: ")

    nums = nums.split()

    entry = 0
    for i in nums:
        nums[entry] = int(i)
        entry = entry + 1

    squareEach(nums)

    print("The square of your numbers are: ",nums)

main()
