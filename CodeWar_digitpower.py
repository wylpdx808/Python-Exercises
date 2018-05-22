# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar digit power
def dig_pow(n,p):
    N = list(str(n))
    intN = [int(digit) for digit in N]
    intNp = [intN[i] ** (p+i) for i in range(len(intN))]
    if sum(intNp) % n == 0: 
        return sum(intNp) / n
    else: 
        return -1 
        
def dig_pow(n,p):
    s = 0 
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1 