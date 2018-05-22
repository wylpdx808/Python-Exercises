# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:34:13 2018

@author: Wai Yan
"""

def median(alist): 
  alist.sort()
  listlength = len(alist)
  if listlength % 2 == 0: 
    midIndex = listlength/2
    minusIndex = midIndex - 1 
    median_even = (alist[minusIndex] + alist[midIndex])/2.0
    return median_even
  else: 
    oddIndex = int(listlength/2.0)
    median_odd = alist[oddIndex]
    return median_odd 