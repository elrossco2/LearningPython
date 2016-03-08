def sumList(nums):
    total = 0
    for i in nums:
        total = total+i
    return total
 
def main():
    print('This program sums the numbers that you enter.')
    nums = input('Please enter a list of numbers separated by a comma: ')
     
    nums = nums.split(',')      
        
    entry = 0
    for i in nums:                 
        nums[entry] = int(i)
        entry = entry+1 
     
    sumTotal = sumList(nums)     
     
    print('The sum of your numbers is {}.'.format(sumTotal))


main()
