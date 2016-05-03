from math import sqrt

class Statset:

    def __init__(self):
        self.list = []

    def addnumber(self, x):
        self.list.append(x)

    def mean(self):
        x = 0
        for i in self.list:
            x = x + i
        return x/len(self.list)

    def median(self):
        self.list.sort()
        size = len(self.list)
        middle = size // 2
        if size % 2 == 0:
            median = (self.list[middle] + self.list[middle - 1]) / 2
        else:
            median = self.list[middle]
        return median

    def stddev(self):
        average = self.mean()
        x = 0
        for i in self.list:
            x = x + (average - i) ** 2
        return sqrt(x / (len(self.list)-1))

    def count(self):
        return len(self.list)

    def min(self):
        self.list.sort()
        return self.list[0]

    def max(self):
        self.list.sort()
        return self.list[len(self.list) - 1]

def main():
    print ("This program collects values and prints the mean, median, standard deviation, count, max and min values of the list.")
    calculations = Statset()
    y = input("Please enter a number (<Enter> to quit): ")
    while y != "":
        calculations.addnumber(int(y))
        y = input("Please enter a number (<Enter> to quit): ")
    print ("The mean of the list is", calculations.mean())
    print ("The median of the list is", calculations.median())
    print ("The standard deviation of the list is", calculations.stddev())
    print ("There are", calculations.count(), "values in the list")
    print ("The smallest value in the list is", calculations.min())
    print ("The largest value in the list is", calculations.max())
    
main()   
    
