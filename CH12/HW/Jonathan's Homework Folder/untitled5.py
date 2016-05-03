# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:03:59 2016

@author: kiaph
"""

def main():
    t = 1
    v = 1
    wc = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)

    
    print(wc)
main()
