# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:59:05 2018

@author: Wai Yan
"""

def product(numbers): 
  result = 1 
  for i in range(len(numbers)): 
    result *= int(numbers[i])
  return result 
  
hello=product([1,2,3,3,4])