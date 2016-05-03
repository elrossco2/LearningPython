# -*- coding: utf-8 -*-
"""
Created on Tue May  3 02:12:08 2016

@author: kiaph
"""

####StatSet
from math import sqrt
class StatSet:
#initself
    def __init__(self):
        #emptyset
        self.stats = []
#add
    def addNumber(self,x,):
        self.stats.append(x)
        
        
#mean
    def mean(self):
        for i in self.stats:
            self.mean = sum(self.stats)/(self.count())
        return self.mean

#median
    def median(self):
        self.stats.sort
        self.median = self.stats[int(self.count()/2)]
        return self.median
#variance
    def variance(self):
        v = 0
        for i in self.stats:
            v = v + ((self.stats(i) - self.mean)**2)
        self.var = v/self.count()
        return self.var
#stddev
    def stddev(self):
        self.stddev = sqrt(self.var)
        return self.stddev
#count
    def count(self):
        n = 0
        for i in self.stats:
            n = n + 1
        self.cou = n
        return self.cou
#min
    def mini(self):
        self.stats.sort
        self.mini = self.stats[0]
        return self.mini
#max
    def maxu(self):
        self.stats.sort
        self.stats.reverse
        self.maxu = self.status[0]
        return self.maxu