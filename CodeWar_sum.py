# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar sum 
def get_sum(a,b): 
    if a == b: 
        return a
    else: 
        ab = sorted([a,b])
        return sum(range(ab[0],ab[1]+1))
    
print get_sum(2,-1)