# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# CodeWar you're a square! challenge 
def is_square(n):
    if n > 0:
        sqrtn = n ** 0.5 
        if n % sqrtn == 0: 
            return True
        else:
            return False
    else:
        return False 