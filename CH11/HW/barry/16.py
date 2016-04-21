from math import *
from statistics import *
 
class StatSet:
     
    def __init__(self):
        self.nums = []
        
         
    def addNumber(self,x):
        self.nums.append(x)
        
         
    def mean(self):
        avg = mean(self.nums)

        return avg
    
         
    def median(self):
        self.nums.sort()
         
        m =  median(self.nums)

        return m
     
     
    def stdDev(self):
        avg = self.mean()
         
        x = 0
        for i in self.nums:
            x = x + (avg-i)**2
         
        return sqrt(x/ (len(self.nums)-1))
 
 
    def count(self):
        return len(self.nums)
         
         
    def min(self):
        self.nums.sort()
        return self.nums[0]
     
     
    def max(self):
        self.nums.sort()
        return self.nums[-1]
         
 
def main():
    print('Does simple statistical calculations of an entered list.\n')

    try:
        group = StatSet()
        i = input('Add a number to calculate [enter to quit]: ')
     
        while i !='':
            group.addNumber(int(i))
            i = input('Add a number to calculate [enter to quit]: ')
     
     
        print("\nMean:",group.mean())
        print("Median:",group.median())
        print("Stand Deviation:",group.stdDev())
        print("Smallest number:",group.min())
        print("Largest number:",group.max())
        print("Total: {} numbers in record".format(group.count()))

    except ValueError:
        print("Enter only numbers. Not letters or symbols.")

     
if __name__ == '__main__': main()
