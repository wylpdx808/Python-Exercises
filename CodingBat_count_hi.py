# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:00:20 2018

@author: Wai Yan
"""

# CodingBat Python String-2 count 'hi' exercise 
def count_hi(str): 
    letters2 = [str[x:x+2] for x in range(len(str))] # list comp 
    return letters2.count('hi')
    
print count_hi('abc hi ho')