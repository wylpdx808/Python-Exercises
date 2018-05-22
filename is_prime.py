# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:09:19 2018

@author: Wai Yan
"""

def is_prime(x): 
  if x < 2: 
    return False 
  else: 
    for n in range(2,x): 
      if x % n == 0: 
        return False 
      else: 
        return True 
    
    
zero = is_prime(0)
print zero