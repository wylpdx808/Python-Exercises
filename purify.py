# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:58:30 2018

@author: Wai Yan
"""

def purify(numbers): 
  odds = []
  for n in numbers: 
    if n % 2 == 0: 
      odds.append(n)
  return odds

numbers = [1,2,3,4,5,6,7]
odds= purify(numbers)
