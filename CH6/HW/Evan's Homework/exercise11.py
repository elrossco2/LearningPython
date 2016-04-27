def squareEach(nums):
    entry = 0
    for i in nums:
        nums[entry] = i**2
        entry = entry+1   
 
def main():
    print('This program squares numbers that you enter.')
    nums = input('Please enter your numbers separated by comma: ')
     
    nums = nums.split(',')         
                                   
    entry = 0
    for i in nums:                 
        nums[entry] = int(i)
        entry = entry+1           
     
    squareEach(nums)              
                                    
    print('Here are your new numbers: ',nums)
