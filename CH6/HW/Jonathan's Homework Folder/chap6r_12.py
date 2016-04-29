# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:01:05 2016

@author: kiaph
"""

def sumList(nums):
    summ = 0
    for i in nums:
        summ = summ + i
    return summ

def main():
    nums = input("Enter numbers to be summed, separated by spaces: ")

    nums = nums.split()

    entry = 0
    for i in nums:
        nums[entry] = int(i)
        entry = entry + 1

    summation = sumList(nums)

    print("The summation is: ", summation)

main()