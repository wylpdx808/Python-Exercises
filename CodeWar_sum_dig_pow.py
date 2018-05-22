# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# codewar sum_dig_pow 
def sum_dig_pow(a,b): 
    ab = range(a, b+1) 
    digits = []
    for n in ab: 
        cpower = []
        for i, c in enumerate(str(n),1):
            cpower.append(int(c) ** i)
        if sum(cpower) == n: 
            digits.append(n)
    return digits 
        

print sum_dig_pow(1,10)
print sum_dig_pow(1,100)