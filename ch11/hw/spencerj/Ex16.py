from math import *
from statistics import *
class StatSet:
    def __init__(self):
        self.nums = []
        
    def addNumber(self, x):
        self.nums.append(x)
        
    def mean(self):
        avg = mean(self.nums)
        return avg
    def median(self):
        self.nums.sort()
        m = median(self.nums)
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
        lst = sorted(self.nums)
        return self.nums[0]
    
    def max(self):
        lst = sorted(self.nums)
        return self.nums[-1]

def main():
    
        nums = StatSet()
        i = input('Add a number: ')
        while i !='':
            nums.addNumber(int(i))
            i = input('Add a number: ')
        print("Mean:", nums.mean())
        print("Median:", nums.median())
        print("Stand Deviation:", nums.stdDev())
        print("Smallest number:", nums.min())
        print("Largest number:", nums.max())
        print("Total: " , nums.count())


     
if __name__ == '__main__': main()
    
            
            
