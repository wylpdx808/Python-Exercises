# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar square digits challenge 
def square_digits(num):
   return ''.join([str(int(digit)**2) for digit in str(num)])
   
print square_digits(9119)