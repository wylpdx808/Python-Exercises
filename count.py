# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:10:18 2018

@author: Wai Yan
"""

sequence = [1,1,1,2,1]
def count(sequence, item): 
  sum = 0 
  newseq=str(sequence)
  for element in newseq: 
    if element == str(item): 
      sum += 1 
    else: 
      continue
  return sum 

something =[[1,1,2,1],1]
item1 = 1