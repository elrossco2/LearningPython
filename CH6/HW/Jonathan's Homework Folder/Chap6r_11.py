# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:56:18 2016

@author: kiaph
"""

def squareEach(nums):
    entry = 0
    for i in nums:
        nums[entry] = i*i
        entry = entry + 1

def main():
    nums = input("Enter numbers to be squared, separated by spaces: ")

    nums = nums.split()

    entry = 0
    for i in nums:
        nums[entry] = int(i)
        entry = entry + 1

    squareEach(nums)

    print("New Numbers: ", nums)

main()