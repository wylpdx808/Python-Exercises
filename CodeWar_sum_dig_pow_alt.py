# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# codewar sum_dig_pow 
def filter_func(a): 
    apower = [int(d) ** i for i, d in enumerate(str(a),1)]
    return sum(apower) == a 

print filter_func(89)

def sum_dig_power(a,b): 
    return filter(filter_func, range(a, b+1))

print sum_dig_power(1,100)