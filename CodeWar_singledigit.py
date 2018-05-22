# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar single digit 
    
def single_digit(n): 
    while len(str(n)) > 1: 
        n = sum_bin(n)
    else: 
        return n 
        
def sum_bin(n): 
    binN = [int(x) for x in list(bin(n)[2:])]
    return sum(binN)
    

print single_digit(123456789) 