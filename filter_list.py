# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:26:25 2018

@author: Wai Yan
"""

def filter_list(l):
    'return a new list with the strings filtered out'
    intlist = []
    for i in range(len(l)): 
        if type(l[i]) == int:
            intlist.append(l[i])
    return intlist
    
print filter_list([1,2,'a','b'])